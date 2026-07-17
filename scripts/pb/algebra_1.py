# -*- coding: utf-8 -*-
"""Problem-bank subject: Algebra 1 — mirrors the /math/algebra-1 course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators (algebra.py, functions.py) and (b) new unit-specific forms defined
below. Every form carries a `unit` field matching ALG1's course spine, so the
bank page can group problems exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/algebra_1.py` for the self-check.
"""
import importlib.util
import os
import re

from sympy import Rational, solve, sympify

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "algebra-1"
TITLE = "Algebra 1"
TITLE_MN = "Алгебр 1"
BLURB = ("Unit-by-unit practice for the Algebra 1 course — expressions to "
         "quadratics, every unit with its own problem collection.")

UNITS = [
    {"id": "expressions-and-operations", "title": "Expressions & Operations",
     "blurb": "Variables, evaluating and simplifying, exponents, order of operations, and words-to-algebra."},
    {"id": "linear-equations", "title": "Solving Linear Equations",
     "blurb": "One-step to both-sides equations, fractions and special cases, and rearranging formulas."},
    {"id": "inequalities", "title": "Linear Inequalities",
     "blurb": "Solving and graphing, the negative-flip rule, compound and/or, and absolute-value equations."},
    {"id": "functions", "title": "Introduction to Functions",
     "blurb": "The one-output rule, f(x) notation, domain and range, and reading real-world graphs."},
    {"id": "linear-functions", "title": "Linear Functions & Slope",
     "blurb": "Slope as a rate, y = mx + b, point-slope and standard forms, parallel and perpendicular lines."},
    {"id": "systems-of-equations", "title": "Systems of Equations",
     "blurb": "Graphing, substitution, elimination, applications, and the no-solution/infinite cases."},
    {"id": "polynomials-and-factoring", "title": "Polynomials & Factoring",
     "blurb": "Polynomial arithmetic, GCF, factoring trinomials and special patterns."},
    {"id": "quadratic-equations", "title": "Quadratic Equations & Functions",
     "blurb": "Solving by factoring, roots and the discriminant, the vertex, and parabola graphs."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    # from algebra.py
    "exponent-laws": "expressions-and-operations",
    "evaluate-expression": "expressions-and-operations",
    "linear-two-step": "linear-equations",
    "rational-equation": "linear-equations",
    "inequality-flip": "inequalities",
    "absolute-inequality": "inequalities",
    "system-2x2": "systems-of-equations",
    "system-parameter": "systems-of-equations",
    # from functions.py
    "vertex-read": "quadratic-equations",
    "factored-roots": "quadratic-equations",
    "discriminant": "quadratic-equations",
    "complete-square-min": "quadratic-equations",
    "quadratic-inequality": "quadratic-equations",
    "tangency-parameter": "quadratic-equations",
}

SOURCES = ["algebra", "functions"]

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


# ---------------------------------------------------------------------------
# helpers for the new unit-specific forms
# ---------------------------------------------------------------------------

def _fmt(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = Rational(v)
    if v.q == 1:
        return str(v.p)
    if v.p < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def _pm(b):
    """Sign of a nonzero signed term for explanation chains."""
    return "+" if b >= 0 else "-"


def _lin_str(a, b):
    """Render `ax + b` as clean KaTeX: no '1x', no '+ -5'."""
    s = "x" if a == 1 else ("-x" if a == -1 else "%dx" % a)
    if b > 0:
        s += " + %d" % b
    elif b < 0:
        s += " - %d" % (-b)
    return s


def _quad_str(a, b):
    """Render `ax^2 + b` as clean KaTeX."""
    s = "x^2" if a == 1 else ("-x^2" if a == -1 else "%dx^2" % a)
    if b > 0:
        s += " + %d" % b
    elif b < 0:
        s += " - %d" % (-b)
    return s


def _monic_str(b, c):
    """Render the monic quadratic `x^2 + bx + c` with proper signs."""
    s = "x^2"
    if b != 0:
        xb = "x" if abs(b) == 1 else "%dx" % abs(b)
        s += " %s %s" % (_pm(b), xb)
    if c != 0:
        s += " %s %d" % (_pm(c), abs(c))
    return s


def _xplus(p):
    """(x + p) with proper sign, e.g. (x + 3) or (x - 3)."""
    return "(x + %d)" % p if p >= 0 else "(x - %d)" % (-p)


def _mk(prefix, raws):
    """Assemble variants: rotate correctIndex i%4, enforce 4 distinct options.

    A raw whose designed distractor set degenerates (numeric collision) is a
    bad parameter draw and is skipped; the assembled options are then asserted
    distinct so nothing ambiguous can ever ship silently.
    """
    variants, seen = [], set()
    for raw in raws:
        if len(variants) >= 36:
            break
        vals = [Rational(v) for v in [raw["correct"]] + list(raw["dvals"])]
        if len(set(vals)) != 4:
            continue  # degenerate parameter draw — distractor would collide
        if raw["statement"] in seen:
            continue
        seen.add(raw["statement"])
        i = len(variants)
        opts = ["$" + _fmt(v) + "$" for v in vals[1:]]
        opts.insert(i % 4, "$" + _fmt(vals[0]) + "$")
        assert len(set(opts)) == 4, \
            "%s: option collision in %r" % (prefix, raw["statement"])
        variants.append({
            "id": "%s-v%02d" % (prefix, i + 1),
            "statement": raw["statement"],
            "options": opts,
            "correctIndex": i % 4,
            "explanation": raw["explanation"],
            "check": raw["check"],
        })
    assert len(variants) >= 34, \
        "%s: only %d variants generated" % (prefix, len(variants))
    return variants


# ---------------------------------------------------------------------------
# per-form raw generators
# ---------------------------------------------------------------------------

def _gen_feval():
    """evaluate-function: f(c) for f(x) = ax + b (~1/3 quadratic ax^2 + b)."""
    raws = []
    a_pool = [2, -3, 4, 5, -2, 3, -4, -1, 1]
    c_pool = [3, -2, 4, -5, 2, 6, -3, 5, -4, 1, -6, -1]
    b_pool = [-5, 3, 7, -2, 4, -9, 6, -7, 2, 8, -4, 9, 1, -8, 5, -3]
    n = 0
    for a in a_pool:
        for c in c_pool:
            b = b_pool[(3 * a + 2 * c + n) % len(b_pool)]
            quad = (n % 3 == 2)
            n += 1
            if quad:
                val = a * c * c + b
                dvals = [a * c * c - b,   # flipped the constant's sign
                         a + b * c,       # swapped the roles of a and b
                         2 * a * c + b]   # doubled instead of squaring
                stmt = "For $f(x) = %s$, find $f(%d)$." % (_quad_str(a, b), c)
                expl = ("Square first: $(%d)^2 = %d$, so $f(%d) = %d %s %d = %d$. "
                        "Doubling instead of squaring gives $%d$ — a square is "
                        "not a double." %
                        (c, c * c, c, a * c * c, _pm(b), abs(b), val,
                         2 * a * c + b))
                check = ["%d*(%d)**2 + (%d) == %d" % (a, c, b, val)]
            else:
                val = a * c + b
                dvals = [a * c - b,       # flipped the constant's sign
                         a + b * c,       # swapped the roles of a and b
                         -a * c + b]      # evaluated at -c
                stmt = "For $f(x) = %s$, find $f(%d)$." % (_lin_str(a, b), c)
                expl = ("Substitute $x = %d$: $f(%d) = %d %s %d = %d$. "
                        "Flipping the sign of the constant gives $%d$ — keep "
                        "the rule exactly as written." %
                        (c, c, a * c, _pm(b), abs(b), val, a * c - b))
                check = ["%d*(%d) + (%d) == %d" % (a, c, b, val)]
            raws.append(dict(statement=stmt, explanation=expl, check=check,
                             correct=val, dvals=dvals))
    return _mk("A1-feval", raws)


def _gen_fsolve():
    """solve-function-equation: f(x) = k for linear f, integer solution."""
    raws = []
    a_pool = [2, 3, 4, 5, -2, -3, 6, -4]
    x_pool = [3, -2, 4, 5, -3, 2, -4, 6, -5, 1]
    b_pool = [-5, 3, 7, -2, 4, -9, 6, -7, 2, 8, -4, 9, 1]
    n = 0
    for a in a_pool:
        for x0 in x_pool:
            b = b_pool[(2 * a + 3 * x0 + n) % len(b_pool)]
            n += 1
            k = a * x0 + b
            wrong = Rational(k + b, a)
            dvals = [wrong,           # moved the constant with the wrong sign
                     k - b,           # forgot to divide by a
                     a * (k - b)]     # multiplied instead of dividing
            stmt = ("For $f(x) = %s$, solve $f(x) = %d$." %
                    (_lin_str(a, b), k))
            expl = ("Set the rule equal to $%d$: $%s = %d$. Move the constant "
                    "to get $%dx = %d$, then divide by $%d$: $x = %d$. Moving "
                    "the constant with the wrong sign gives $%s$." %
                    (k, _lin_str(a, b), k, a, k - b, a, x0, _fmt(wrong)))
            check = ["solve(%d*x + (%d) - (%d), x) == [%d]" % (a, b, k, x0),
                     "%d*(%d) + (%d) == %d" % (a, x0, b, k)]
            raws.append(dict(statement=stmt, explanation=expl, check=check,
                             correct=x0, dvals=dvals))
    return _mk("A1-fsolve", raws)


def _gen_slope():
    """slope-two-points: mostly integer slopes, ~1/3 simple fractions."""
    raws = []
    x1s = [1, -2, 3, 0, 2, -3, 4, -1, 5, -4, -5, 6, 0, 2]
    y1s = [2, -1, 3, -4, 0, 5, -2, 1, 4, -3, 6, -5, 3, -6]
    int_ms = [2, -3, 4, -2, 5, 3, -4, -5, 6, -6, 2, 3, -2, 4, 5, -3, 2, -4,
              3, 6, -2, -5, 4, -3]
    dxs = [1, 2, 3, -2, 2, -1, 3, 1, -3, 2, 1, -2, 3, -1, 2, -3, 1, 2, -2,
           3, 1, -2, 2, 3]
    fracs = [(3, 2), (-3, 2), (2, 3), (5, 2), (-2, 3), (4, 3), (-5, 2),
             (3, 4), (5, 3), (-4, 3), (7, 2), (-3, 4), (2, 5), (-5, 3)]
    ii = fi = 0
    for n in range(57):
        if n % 3 == 2:
            p, q = fracs[fi % len(fracs)]
            x1 = x1s[(fi * 3 + 1) % len(x1s)]
            y1 = y1s[(fi * 5 + 2) % len(y1s)]
            dx = q if fi % 2 == 0 else -q
            m = Rational(p, q)
            fi += 1
        else:
            m = Rational(int_ms[ii % len(int_ms)])
            dx = dxs[(ii * 5 + 1) % len(dxs)]
            x1 = x1s[ii % len(x1s)]
            y1 = y1s[(ii * 7 + 3) % len(y1s)]
            ii += 1
        x2 = x1 + dx
        y2 = y1 + int(m * dx)
        dvals = [1 / m,    # reciprocal: put Δx on top
                 -m,       # subtracted in opposite orders
                 -1 / m]   # Δx/Δy with inverted sign
        stmt = ("Find the slope of the line through $(%d; %d)$ and "
                "$(%d; %d)$." % (x1, y1, x2, y2))
        expl = ("Slope $= \\dfrac{\\Delta y}{\\Delta x} = "
                "\\dfrac{%d - (%d)}{%d - (%d)} = %s$. Putting $\\Delta x$ on "
                "top gives the reciprocal $%s$ — rise goes over run, always." %
                (y2, y1, x2, x1, _fmt(m), _fmt(1 / m)))
        check = ["Rational(%d - (%d), %d - (%d)) == Rational(%d, %d)" %
                 (y2, y1, x2, x1, m.p, m.q)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=m, dvals=dvals))
    return _mk("A1-slope", raws)


def _gen_line():
    """line-through-point: y-intercept from slope+point, or y at x = c."""
    raws = []
    ms = [2, -3, 4, 5, -2, 3, -4, 6, -5, 2, 3, -2, 4, -3]
    ps = [3, -2, 4, 1, -5, 2, -3, 5, -1, -4, 6]
    qs = [4, -3, 5, 2, -6, 7, 3, -2, 8, -4, 1, 6, -7]
    bs = [-5, 3, 7, -2, 4, -9, 6, -7, 2, 8, -4]
    cs = [3, -2, 4, -5, 2, 6, -3, 5, -4, 1, -6, 7, -1]
    for n in range(60):
        j = n // 2
        if n % 2 == 0:
            m = ms[j % len(ms)]
            p = ps[j % len(ps)]
            q = qs[j % len(qs)]
            b0 = q - m * p
            dvals = [q + m * p,   # added mx instead of subtracting
                     m * p,       # forgot the point's y-coordinate
                     m * p - q]   # subtracted in the wrong order
            stmt = ("A line with slope $%d$ passes through $(%d; %d)$. Find "
                    "its $y$-intercept $b$." % (m, p, q))
            expl = ("Substitute the point into $y = mx + b$: "
                    "$b = y - mx = %d - (%d) = %d$. Adding $mx$ instead of "
                    "subtracting gives $%d$." % (q, m * p, b0, q + m * p))
            check = ["%d - (%d)*(%d) == %d" % (q, m, p, b0),
                     "(%d)*(%d) + (%d) == %d" % (m, p, b0, q)]
            correct = b0
        else:
            m = ms[(j * 3 + 1) % len(ms)]
            b = bs[j % len(bs)]
            c = cs[j % len(cs)]
            y0 = m * c + b
            dvals = [m * c - b,    # subtracted the intercept
                     -m * c + b,   # sign slip: evaluated at -c
                     m + b * c]    # swapped slope and intercept roles
            stmt = ("For the line $y = %s$, find $y$ when $x = %d$." %
                    (_lin_str(m, b), c))
            expl = ("Substitute $x = %d$: $y = %d %s %d = %d$. Subtracting "
                    "the intercept instead of adding it gives $%d$." %
                    (c, m * c, _pm(b), abs(b), y0, m * c - b))
            check = ["(%d)*(%d) + (%d) == %d" % (m, c, b, y0)]
            correct = y0
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=correct, dvals=dvals))
    return _mk("A1-line", raws)


def _gen_expand():
    """expand-product: x-coefficient (or constant term) of (x + a)(x + b)."""
    raws = []
    aa = [3, -5, 2, 7, -4, 6, -8, 9, 1, 5, -7, 4, -9, 8, -1, -6]
    bb = [-2, 4, -7, 5, 1, -9, 8, -6, 7, -3, 9, -5, -1, -4, 6, 3]
    n = 0
    for i, a in enumerate(aa):
        for j in range(4):
            b = bb[(i * 5 + j * 3 + 1) % len(bb)]
            ask_coeff = (n % 2 == 0)
            n += 1
            s, pr = a + b, a * b
            pair = "%s%s" % (_xplus(a), _xplus(b))
            if ask_coeff:
                correct = s
                dvals = [pr,      # took the product (the constant term)
                         a - b,   # subtracted instead of adding
                         -s]      # flipped the sign of the sum
                stmt = ("Expand $%s$. What is the coefficient of $x$?" % pair)
                expl = ("Outer + inner gives the middle term: "
                        "$(%d) + (%d) = %d$ is the coefficient of $x$, while "
                        "the product $(%d)(%d) = %d$ is the constant term. "
                        "Swapping sum and product is the classic mix-up." %
                        (a, b, s, a, b, pr))
            else:
                correct = pr
                dvals = [s,       # took the sum (the x-coefficient)
                         a - b,   # subtracted instead of multiplying
                         -pr]     # flipped the sign of the product
                stmt = ("Expand $%s$. What is the constant term?" % pair)
                expl = ("The constant term is the product of the two "
                        "numbers: $(%d)(%d) = %d$. The sum $%d$ gives the "
                        "coefficient of $x$ instead — don't swap them." %
                        (a, b, pr, s))
            check = ["expand((x + (%d))*(x + (%d))) == x**2 + (%d)*x + (%d)" %
                     (a, b, s, pr)]
            raws.append(dict(statement=stmt, explanation=expl, check=check,
                             correct=correct, dvals=dvals))
    return _mk("A1-expand", raws)


def _gen_factor():
    """factor-quadratic: larger root of x^2 + bx + c with integer roots."""
    pairs = [(5, 2), (3, -4), (7, 1), (-2, -6), (4, -3), (8, 3), (2, -5),
             (6, -1), (9, 4), (-1, -7), (5, -2), (7, 3), (-3, -8), (4, 1),
             (6, -5), (2, -9), (8, -3), (3, 1), (-2, -9), (9, -4), (7, -6),
             (5, 3), (-4, -7), (6, 2), (1, -8), (8, 5), (-1, -5), (9, 2),
             (4, -9), (7, -2), (3, -7), (6, 1), (-3, -5), (5, -8), (8, 1),
             (2, -3), (9, -6), (4, 3), (-2, -4), (7, 5), (6, -9), (1, -4),
             (8, -7), (5, 1), (9, 7), (-1, -9), (3, -6), (2, 1), (-4, -6),
             (9, 1)]
    raws = []
    for p, q in pairs:
        b, c = -(p + q), p * q
        dvals = [q,       # picked the smaller root
                 -p,      # took the factor's constant, sign unflipped
                 p + q]   # reported the sum of the roots
        stmt = ("Solve by factoring: $%s = 0$. Find the LARGER root." %
                _monic_str(b, c))
        expl = ("Look for two numbers with product $%d$ and sum $%d$: that "
                "factors as $%s%s = 0$, so $x = %d$ or $x = %d$. The larger "
                "root is $%d$ — picking the smaller one, $%d$, is the classic "
                "slip." % (c, -b, _xplus(-p), _xplus(-q), p, q, p, q))
        check = ["solve(x**2 + (%d)*x + (%d), x) == [%d, %d]" % (b, c, q, p),
                 "(%d) + (%d) == %d" % (p, q, -b),
                 "(%d)*(%d) == %d" % (p, q, c)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=p, dvals=dvals))
    return _mk("A1-factor", raws)


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    return [
        {"id": "evaluate-function", "title": "Evaluating functions",
         "level": 1, "unit": "functions",
         "skill": "f(c): substitute c for x and compute — powers before products, signs as written.",
         "variants": _gen_feval()},
        {"id": "solve-function-equation", "title": "Solving f(x) = k",
         "level": 2, "unit": "functions",
         "skill": "Set the rule equal to k, move the constant, then divide by the coefficient.",
         "variants": _gen_fsolve()},
        {"id": "slope-two-points", "title": "Slope from two points",
         "level": 1, "unit": "linear-functions",
         "skill": "m = Δy/Δx — rise over run, both differences in the same order.",
         "variants": _gen_slope()},
        {"id": "line-through-point", "title": "Lines through a point",
         "level": 2, "unit": "linear-functions",
         "skill": "y = mx + b: substitute what you know, solve for what you don't.",
         "variants": _gen_line()},
        {"id": "expand-product", "title": "Expanding (x + a)(x + b)",
         "level": 1, "unit": "polynomials-and-factoring",
         "skill": "FOIL: the x-coefficient is the SUM a + b; the constant term is the PRODUCT ab.",
         "variants": _gen_expand()},
        {"id": "factor-quadratic", "title": "Solving quadratics by factoring",
         "level": 2, "unit": "polynomials-and-factoring",
         "skill": "Two numbers with sum −b and product c are the roots of x² + bx + c = 0.",
         "variants": _gen_factor()},
    ]


# ---------------------------------------------------------------------------
# independent re-solvers (regex-parse the statement, recompute the answer)
# ---------------------------------------------------------------------------

_X = sympify("x")


def _parse_expr(latex):
    """Latex like '-3x + 5' or '4x^2 - 7' or 'x^2 + x - 12' -> sympy expr."""
    t = latex.replace("^", "**").replace(" ", "")
    t = re.sub(r"(\d)x", r"\1*x", t)
    t = re.sub(r"(?<![*\d])x", "1*x", t)
    return sympify(t)


def _resolve_feval(stmt):
    m = re.search(r"f\(x\) = (.+?)\$, find \$f\((-?\d+)\)\$", stmt)
    return ("num", _parse_expr(m.group(1)).subs(_X, int(m.group(2))))


def _resolve_fsolve(stmt):
    m = re.search(r"f\(x\) = (.+?)\$, solve \$f\(x\) = (-?\d+)\$", stmt)
    sols = solve(_parse_expr(m.group(1)) - int(m.group(2)), _X)
    assert len(sols) == 1
    return ("num", sols[0])


def _resolve_slope(stmt):
    m = re.search(r"through \$\((-?\d+); (-?\d+)\)\$ and \$\((-?\d+); (-?\d+)\)\$",
                  stmt)
    x1, y1, x2, y2 = (int(g) for g in m.groups())
    return ("num", Rational(y2 - y1, x2 - x1))


def _resolve_line(stmt):
    m = re.search(r"slope \$(-?\d+)\$ passes through \$\((-?\d+); (-?\d+)\)\$",
                  stmt)
    if m:
        sl, p, q = (int(g) for g in m.groups())
        return ("num", q - sl * p)
    m = re.search(r"y = (.+?)\$, find \$y\$ when \$x = (-?\d+)\$", stmt)
    return ("num", _parse_expr(m.group(1)).subs(_X, int(m.group(2))))


def _resolve_expand(stmt):
    m = re.search(r"\$\(x ([+-]) (\d+)\)\(x ([+-]) (\d+)\)\$", stmt)
    a = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
    b = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
    if "coefficient" in stmt:
        return ("num", a + b)
    assert "constant term" in stmt
    return ("num", a * b)


def _resolve_factor(stmt):
    m = re.search(r"Solve by factoring: \$(.+?) = 0\$", stmt)
    roots = solve(_parse_expr(m.group(1)), _X)
    assert len(roots) == 2
    return ("num", max(roots))


RESOLVERS.update({
    "evaluate-function": _resolve_feval,
    "solve-function-equation": _resolve_fsolve,
    "slope-two-points": _resolve_slope,
    "line-through-point": _resolve_line,
    "expand-product": _resolve_expand,
    "factor-quadratic": _resolve_factor,
})


# ---------------------------------------------------------------------------
# batch 2: textbook-style exercise forms (12-variant target per form)
# ---------------------------------------------------------------------------

from math import gcd as _igcd, isqrt as _isqrt  # noqa: E402


def _mk12(prefix, raws, cap=12):
    """Assemble ~12 variants: rotate correctIndex i%4, enforce 4 distinct options.

    Numeric raws carry correct/dvals (rendered via _fmt); option-string raws
    carry copt/dopts instead. A raw whose designed option set degenerates
    (collision) is a bad parameter draw and is skipped; assembled options are
    asserted distinct. Floor of 10 variants (check_subject's gate).
    """
    variants, seen = [], set()
    for raw in raws:
        if len(variants) >= cap:
            break
        if "correct" in raw:
            vals = [Rational(v) for v in [raw["correct"]] + list(raw["dvals"])]
            if len(set(vals)) != 4:
                continue  # degenerate draw — a distractor collides
            copt = "$" + _fmt(vals[0]) + "$"
            wrong = ["$" + _fmt(v) + "$" for v in vals[1:]]
        else:
            copt, wrong = raw["copt"], list(raw["dopts"])
            if len(set([copt] + wrong)) != 4:
                continue
        if raw["statement"] in seen:
            continue
        seen.add(raw["statement"])
        i = len(variants)
        opts = list(wrong)
        opts.insert(i % 4, copt)
        assert len(set(opts)) == 4, \
            "%s: option collision in %r" % (prefix, raw["statement"])
        variants.append({
            "id": "%s-v%02d" % (prefix, i + 1),
            "statement": raw["statement"],
            "options": opts,
            "correctIndex": i % 4,
            "explanation": raw["explanation"],
            "check": raw["check"],
        })
    assert len(variants) >= 10, \
        "%s: only %d variants generated" % (prefix, len(variants))
    return variants


def _mxb(m, b):
    """Render `mx + b` with a possibly fractional slope as clean KaTeX."""
    m = Rational(m)
    if m.q == 1:
        return _lin_str(m.p, b)
    s = "\\frac{%d}{%d}x" % (abs(m.p), m.q)
    if m.p < 0:
        s = "-" + s
    if b > 0:
        s += " + %d" % b
    elif b < 0:
        s += " - %d" % (-b)
    return s


def _gen_oop():
    """order-of-operations: evaluate mixed arithmetic, three shapes."""
    A = [2, 3, 5, 4, 7, 6, 9, 8, 10, 3, 5, 2, 4, 6, 7, 9]
    B = [3, 2, 4, 5, 2, 3, 2, 4, 3, 5, 4, 2, 3, 2, 5, 4]
    C = [5, 7, 6, 8, 9, 4, 7, 5, 6, 8, 4, 9, 7, 6, 5, 8]
    D = [2, 3, 1, 5, 4, 1, 3, 2, 4, 6, 1, 5, 2, 3, 4, 6]
    raws = []
    for n in range(16):
        a, b, c, d = A[n], B[n], C[n], D[n]
        if n % 3 == 0:
            val = a + b * (c - d) ** 2
            stmt = "Evaluate: $%d + %d \\cdot (%d - %d)^2$." % (a, b, c, d)
            dvals = [(a + b) * (c - d) ** 2,  # worked left to right
                     a + b * (c - d),         # forgot the square
                     a - b * (c - d) ** 2]    # sign slip on the addition
            expl = ("Parentheses, then the exponent, then multiply: "
                    "$(%d - %d)^2 = %d$, so the value is $%d + %d \\cdot %d "
                    "= %d$. Adding $%d + %d$ first (left to right) gives "
                    "$%d$ — exponents and products come before addition." %
                    (c, d, (c - d) ** 2, a, b, (c - d) ** 2, val, a, b,
                     (a + b) * (c - d) ** 2))
            check = ["%d + %d*(%d - %d)**2 == %d" % (a, b, c, d, val)]
        elif n % 3 == 1:
            val = a - b * (c + d)
            stmt = "Evaluate: $%d - %d \\cdot (%d + %d)$." % (a, b, c, d)
            dvals = [(a - b) * (c + d),  # worked left to right
                     a - b * c + d,      # dropped the parentheses
                     a + b * (c + d)]    # ignored the minus sign
            expl = ("Multiply before subtracting: $%d \\cdot %d = %d$, so "
                    "the value is $%d - %d = %d$. Computing $%d - %d$ first "
                    "gives $%d$ — subtraction waits for the product." %
                    (b, c + d, b * (c + d), a, b * (c + d), val, a, b,
                     (a - b) * (c + d)))
            check = ["%d - %d*(%d + %d) == %d" % (a, b, c, d, val)]
        else:
            val = a + b * c ** 2
            stmt = "Evaluate: $%d + %d \\cdot %d^2$." % (a, b, c)
            dvals = [(a + b * c) ** 2,   # squared at the very end
                     a + (b * c) ** 2,   # squared the whole product
                     a + 2 * b * c]      # doubled instead of squaring
            expl = ("The exponent binds only to $%d$: $%d^2 = %d$, so the "
                    "value is $%d + %d \\cdot %d = %d$. Squaring the whole "
                    "product $%d \\cdot %d$ gives $%d$ — the square applies "
                    "before multiplying." %
                    (c, c, c * c, a, b, c * c, val, b, c, a + (b * c) ** 2))
            check = ["%d + %d*%d**2 == %d" % (a, b, c, val)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=val, dvals=dvals))
    return _mk12("A1-oop", raws)


def _gen_clt():
    """combine-like-terms: coefficient of x (half: constant) in ax+b-cx+d."""
    A = [3, 5, 7, 4, 8, 6, 9, 2, 7, 5, 8, 3, 6, 9]
    Cc = [5, 2, 3, 7, 3, 9, 4, 6, 2, 8, 5, 7, 2, 4]
    Bb = [4, 7, 2, 6, 9, 3, 8, 5, 7, 2, 6, 9, 3, 8]
    Dd = [6, 3, 8, 2, 5, 7, 4, 9, 3, 6, 2, 4, 8, 5]
    raws = []
    for n in range(14):
        a, c, b, d = A[n], Cc[n], Bb[n], Dd[n]
        if a == c or b == d:
            continue
        stmt_core = "$%dx + %d - %dx + %d$" % (a, b, c, d)
        if n % 2 == 0:
            correct = a - c
            dvals = [a + c,   # ignored the minus on cx
                     b + d,   # combined the constants instead
                     c - a]   # subtracted backwards
            stmt = ("Simplify: %s. What is the coefficient of $x$?" %
                    stmt_core)
            expl = ("The $x$-terms are $%dx$ and $-%dx$, so the coefficient "
                    "is $%d - %d = %d$. Adding to get $%d$ ignores the minus "
                    "sign that travels with $%dx$." %
                    (a, c, a, c, a - c, a + c, c))
            check = ["expand(%d*x + %d - %d*x + %d - ((%d)*x + %d)) == 0" %
                     (a, b, c, d, a - c, b + d)]
        else:
            correct = b + d
            dvals = [b - d,   # let the minus spill onto d
                     a - c,   # grabbed the x-coefficient
                     d - b]   # subtracted backwards
            stmt = "Simplify: %s. What is the constant term?" % stmt_core
            expl = ("The constants are $+%d$ and $+%d$, giving $%d$. "
                    "Computing $%d - %d$ lets the minus sign (which belongs "
                    "only to $%dx$) spill onto the $%d$." %
                    (b, d, b + d, b, d, c, d))
            check = ["expand(%d*x + %d - %d*x + %d - ((%d)*x + %d)) == 0" %
                     (a, b, c, d, a - c, b + d)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=correct, dvals=dvals))
    return _mk12("A1-clt", raws)


def _gen_dist():
    """distribute-simplify: a(bx + c) - d(ex + f), coefficient or constant."""
    A = [2, 3, 4, 5, 2, 3, 6, 4, 5, 2, 7, 3, 4, 6]
    B = [3, 5, 2, 4, 7, 2, 3, 5, 2, 6, 2, 4, 3, 5]
    C = [4, 2, 5, 3, 2, 6, 4, 2, 7, 3, 5, 2, 6, 4]
    D = [3, 2, 5, 2, 4, 5, 2, 3, 4, 5, 3, 2, 5, 3]
    E = [2, 4, 3, 5, 3, 4, 5, 6, 3, 2, 4, 7, 2, 3]
    F = [5, 3, 2, 4, 6, 2, 3, 5, 2, 4, 6, 3, 4, 2]
    raws = []
    for n in range(14):
        a, b, c, d, e, f = A[n], B[n], C[n], D[n], E[n], F[n]
        stmt_core = "$%d(%dx + %d) - %d(%dx + %d)$" % (a, b, c, d, e, f)
        if n % 2 == 0:
            correct = a * b - d * e
            dvals = [a * b + d * e,   # didn't distribute the minus
                     b - e,           # never multiplied by the outside numbers
                     d * e - a * b]   # subtracted backwards
            stmt = ("Simplify: %s. What is the coefficient of $x$?" %
                    stmt_core)
            expl = ("Distribute both factors: $%dx - %dx$ gives the "
                    "coefficient $%d$. Getting $%d$ means the minus sign was "
                    "never pushed through the second parentheses." %
                    (a * b, d * e, a * b - d * e, a * b + d * e))
        else:
            correct = a * c - d * f
            dvals = [a * c + d * f,   # didn't distribute the minus
                     c - f,           # never multiplied by the outside numbers
                     d * f - a * c]   # subtracted backwards
            stmt = "Simplify: %s. What is the constant term?" % stmt_core
            expl = ("The constants are $%d \\cdot %d - %d \\cdot %d = %d$. "
                    "Getting $%d$ means the minus sign stopped at the first "
                    "term instead of hitting every term in the parentheses." %
                    (a, c, d, f, a * c - d * f, a * c + d * f))
        check = ["expand(%d*(%d*x + %d) - %d*(%d*x + %d)) == (%d)*x + (%d)" %
                 (a, b, c, d, e, f, a * b - d * e, a * c - d * f)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=correct, dvals=dvals))
    return _mk12("A1-dist", raws)


def _gen_words():
    """words-to-algebra: pick the expression matching a verbal phrase."""
    data = [
        ("less", 5, 2), ("more", 3, 4), ("twice", 5, 0), ("quot", 4, 3),
        ("prod", 5, 6), ("less", 7, 3), ("more", 8, 5), ("twice", 3, 0),
        ("quot", 5, 2), ("prod", 9, 4), ("less", 4, 6), ("more", 2, 7),
        ("twice", 9, 0), ("quot", 3, 8), ("prod", 2, 7),
    ]
    raws = []
    for kind, k, m in data:
        if kind == "less":
            phrase = "'%d less than %d times a number $n$'" % (k, m)
            copt = "$%dn - %d$" % (m, k)
            dopts = ["$%d - %dn$" % (k, m),      # reversed the subtraction
                     "$%d(n - %d)$" % (m, k),    # subtracted before scaling
                     "$%dn + %d$" % (m, k)]      # added instead
            expl = ("'%d less than' means the %d is subtracted LAST: "
                    "$%dn - %d$. Writing $%d - %dn$ reverses the "
                    "subtraction — the classic 'less than' trap." %
                    (k, k, m, k, k, m))
            check = ["%d*10 - %d == %d" % (m, k, m * 10 - k)]
        elif kind == "more":
            phrase = "'%d more than %d times a number $n$'" % (k, m)
            copt = "$%dn + %d$" % (m, k)
            dopts = ["$%d(n + %d)$" % (m, k),    # added before scaling
                     "$%dn - %d$" % (m, k),      # subtracted instead
                     "$%dn + %d$" % (k, m)]      # swapped the two numbers
            expl = ("Multiply first, then add: $%dn + %d$. The grouped "
                    "$%d(n + %d)$ multiplies the %d as well — that's "
                    "'%d times the sum', a different phrase." %
                    (m, k, m, k, k, m))
            check = ["%d*10 + %d == %d" % (m, k, m * 10 + k)]
        elif kind == "twice":
            phrase = "'twice the sum of a number $n$ and %d'" % k
            copt = "$2(n + %d)$" % k
            dopts = ["$2n + %d$" % k,            # doubled only the n
                     "$2(n - %d)$" % k,          # turned the sum into a difference
                     "$n + %d$" % (2 * k)]       # doubled only the constant
            expl = ("'The sum' is built first, then doubled: $2(n + %d)$. "
                    "$2n + %d$ doubles only the $n$ — the parentheses are "
                    "exactly what the word 'sum' demands." % (k, k))
            check = ["2*(10 + %d) == %d" % (k, 2 * (10 + k))]
        elif kind == "quot":
            phrase = ("'the quotient of a number $n$ and %d, increased by "
                      "%d'" % (k, m))
            copt = "$\\frac{n}{%d} + %d$" % (k, m)
            dopts = ["$\\frac{%d}{n} + %d$" % (k, m),  # flipped the quotient
                     "$\\frac{n + %d}{%d}$" % (m, k),  # increased before dividing
                     "$\\frac{n}{%d} - %d$" % (k, m)]  # decreased instead
            expl = ("'Quotient of $n$ and %d' puts $n$ on top: "
                    "$\\frac{n}{%d}$, then add %d. Flipping to "
                    "$\\frac{%d}{n}$ reverses the stated order." %
                    (k, k, m, k))
            check = ["Rational(%d, %d) + %d == Rational(%d, %d)" %
                     (10 * k, k, m, 10 * k + m * k, k)]
        else:
            phrase = ("'the product of %d and a number $n$, decreased by "
                      "%d'" % (m, k))
            copt = "$%dn - %d$" % (m, k)
            dopts = ["$%d - %dn$" % (k, m),      # reversed the subtraction
                     "$%d(n - %d)$" % (m, k),    # decreased before multiplying
                     "$%dn + %d$" % (m, k)]      # increased instead
            expl = ("Form the product $%dn$ first, then take away %d: "
                    "$%dn - %d$. Grouping as $%d(n - %d)$ decreases $n$ "
                    "before the product is formed — the wrong order." %
                    (m, k, m, k, m, k))
            check = ["%d*10 - %d == %d" % (m, k, m * 10 - k)]
        raws.append(dict(statement="Which expression means %s?" % phrase,
                         explanation=expl, check=check, copt=copt,
                         dopts=dopts))
    return _mk12("A1-words", raws)


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = _remapped_forms() + new_forms()
    for f in forms:
        assert f["unit"] in unit_order, "%s: unknown unit %r" % (f["id"], f["unit"])
    forms.sort(key=lambda f: (unit_order[f["unit"]], f["level"], f["id"]))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}




# ---------------------------------------------------------------------------
# Batch 2 — the rest of the textbook set (12-variant forms + resolvers)
# ---------------------------------------------------------------------------

def _rel_opt(rel, val):
    return "$x %s %s$" % (rel, _fmt(val))


def _gen_both():
    """equation-both-sides: ax + b = cx + d, integer x."""
    P = [(3, 2, 4, 1), (-2, 5, 2, -3), (4, -1, 7, 2), (5, 3, 2, -4),
         (2, -3, 5, -1), (-3, 4, 1, 6), (6, 2, 3, -5), (4, 5, -2, 3),
         (-4, 1, 2, 7), (7, -2, 3, 4), (2, 6, 5, -3), (3, -5, -2, 4),
         (5, 1, 3, -6), (-2, 3, 4, 5)]
    raws = []
    for x, a, c, b in P:
        d = (a - c) * x + b
        stmt = "Solve: $%s = %s$." % (_lin_str(a, b), _lin_str(c, d))
        dvals = [Rational(d + b, a - c) if a != c else 0,  # added the constants
                 Rational(d - b, a + c) if a + c != 0 else 0,  # added the x-terms
                 -x]                                       # sign slip at the end
        expl = ("Collect $x$ on one side: $%dx = %d$, so $x = %d$. Moving a "
                "term across the equals sign flips its sign — forgetting "
                "that gives the wrong constant." % (a - c, d - b, x))
        check = ["(%d)*(%d) + (%d) == (%d)*(%d) + (%d)" % (a, x, b, c, x, d)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=x, dvals=dvals))
    return _mk12("A1-both", raws)


def _gen_deq():
    """distribute-equation: a(x + b) = c."""
    P = [(4, 3, 2), (-2, 2, -5), (5, 4, -3), (3, -3, 6), (6, 2, 4),
         (-3, 5, 2), (2, -4, 7), (7, 3, -2), (4, -2, 5), (-5, 2, 3),
         (3, 6, -4), (5, -5, 2), (2, 4, 6), (6, -3, -2)]
    raws = []
    for x, a, b in P:
        c = a * (x + b)
        stmt = "Solve: $%d%s = %d$." % (a, _xplus(b), c)
        dvals = [Rational(c - b, a),   # subtracted b before dividing
                 c - a * b,            # forgot to divide by a
                 Rational(c, a) + b]   # sign slip on b
        expl = ("Divide by $%d$: $%s = %s$, then move the constant: "
                "$x = %d$. The %d inside the parentheses is divided too — "
                "subtracting it first is the classic slip." %
                (a, _xplus(b), _fmt(Rational(c, a)), x, abs(b)))
        check = ["(%d)*((%d) + (%d)) == (%d)" % (a, x, b, c)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=x, dvals=dvals))
    return _mk12("A1-deq", raws)


def _gen_freq():
    """fraction-equation: x/a + b = c."""
    P = [(2, 3, 7), (3, -2, 4), (4, 5, 2), (5, 2, -3), (2, -4, 1),
         (6, 3, 8), (3, 4, -2), (4, -3, 5), (5, 6, 2), (2, 5, -1),
         (7, 2, 6), (3, -5, 3), (4, 2, 9), (6, -2, 4)]
    raws = []
    for a, b, c in P:
        x = a * (c - b)
        sign = "+ %d" % b if b > 0 else "- %d" % (-b)
        stmt = "Solve: $\\frac{x}{%d} %s = %d$." % (a, sign, c)
        dvals = [Rational(c - b, a),  # divided instead of multiplying
                 c - b,               # forgot the a entirely
                 a * (c + b)]         # sign slip on b
        expl = ("Move the constant, then multiply by $%d$: "
                "$\\frac{x}{%d} = %d$, so $x = %d$. Dividing by %d at the "
                "end (instead of multiplying) undoes the wrong operation." %
                (a, a, c - b, x, a))
        check = ["Rational(%d, %d) + (%d) == (%d)" % (x, a, b, c)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=x, dvals=dvals))
    return _mk12("A1-freq", raws)


_LIT = [
    ("P = 2l + 2w", "w", "$w = \\frac{P - 2l}{2}$",
     ["$w = P - 2l$", "$w = \\frac{P + 2l}{2}$", "$w = \\frac{P}{2} - 2l$"],
     "Subtract $2l$, THEN divide the whole side by 2 — both terms, not one.",
     ["Rational(20 - 2*3, 2) == 7"]),
    ("d = rt", "t", "$t = \\frac{d}{r}$",
     ["$t = dr$", "$t = \\frac{r}{d}$", "$t = d - r$"],
     "Divide both sides by $r$; time is distance over rate.",
     ["Rational(60, 12) == 5"]),
    ("A = \\frac{1}{2}bh", "h", "$h = \\frac{2A}{b}$",
     ["$h = \\frac{A}{2b}$", "$h = \\frac{b}{2A}$", "$h = 2Ab$"],
     "Multiply by 2 first to clear the half, then divide by $b$.",
     ["Rational(2*12, 4) == 6"]),
    ("y = mx + b", "x", "$x = \\frac{y - b}{m}$",
     ["$x = \\frac{y + b}{m}$", "$x = m(y - b)$", "$x = y - b - m$"],
     "Subtract $b$ before dividing by $m$ — order matters.",
     ["Rational(11 - 3, 4) == 2"]),
    ("C = 2\\pi r", "r", "$r = \\frac{C}{2\\pi}$",
     ["$r = 2\\pi C$", "$r = \\frac{C}{\\pi}$", "$r = C - 2\\pi$"],
     "Divide by the whole coefficient $2\\pi$, not just by $\\pi$.",
     ["Rational(1, 2) * Rational(1, 1) == Rational(1, 2)"]),
    ("V = lwh", "h", "$h = \\frac{V}{lw}$",
     ["$h = Vlw$", "$h = \\frac{lw}{V}$", "$h = V - lw$"],
     "Divide by BOTH remaining factors: $lw$ together.",
     ["Rational(24, 2*3) == 4"]),
    ("P = a + b + c", "c", "$c = P - a - b$",
     ["$c = P + a + b$", "$c = a + b - P$", "$c = \\frac{P - a}{b}$"],
     "Subtract each known side; signs flip as they cross over.",
     ["12 - 3 - 4 == 5"]),
    ("A = \\frac{(a + b)h}{2}", "h", "$h = \\frac{2A}{a + b}$",
     ["$h = \\frac{A}{2(a + b)}$", "$h = \\frac{a + b}{2A}$", "$h = 2A - a - b$"],
     "Clear the 2 first, then divide by the whole sum $(a+b)$.",
     ["Rational(2*10, 2 + 3) == 4"]),
    ("F = ma", "a", "$a = \\frac{F}{m}$",
     ["$a = Fm$", "$a = \\frac{m}{F}$", "$a = F - m$"],
     "Isolate $a$ by dividing by $m$.",
     ["Rational(12, 3) == 4"]),
    ("v = u + at", "t", "$t = \\frac{v - u}{a}$",
     ["$t = \\frac{v + u}{a}$", "$t = a(v - u)$", "$t = v - u - a$"],
     "Move $u$ first, then divide by $a$.",
     ["Rational(14 - 2, 3) == 4"]),
    ("A = s^2", "s", "$s = \\sqrt{A}$",
     ["$s = A^2$", "$s = \\frac{A}{2}$", "$s = 2A$"],
     "Undo a square with a square root — halving is a different operation.",
     ["sqrt(49) == 7"]),
    ("E = \\frac{1}{2}mv^2", "m", "$m = \\frac{2E}{v^2}$",
     ["$m = \\frac{E}{2v^2}$", "$m = 2Ev^2$", "$m = \\frac{v^2}{2E}$"],
     "Multiply by 2, then divide by $v^2$ — the square stays with $v$.",
     ["Rational(2*16, 4**2) == 2"]),
]


def _gen_lit():
    raws = []
    for formula, var, copt, dopts, why, check in _LIT:
        stmt = "Solve $%s$ for $%s$." % (formula, var)
        raws.append(dict(statement=stmt, copt=copt, dopts=dopts,
                         explanation=why, check=check))
    return _mk12("A1-lit", raws)


def _gen_ineq1():
    """one-step-inequality: single move, direction preserved."""
    P = [(0, 5, 8), (1, 4, 9), (2, 3, 12), (3, 4, 5), (0, 7, 3), (1, 6, 2),
         (2, 5, 20), (3, 3, 4), (0, 2, 9), (1, 8, 5), (2, 4, 12), (3, 6, 2),
         (0, 6, 4), (1, 3, 7)]
    raws = []
    for kind, a, b in P:
        if kind == 0:
            stmt = "Solve: $x + %d > %d$." % (a, b)
            rel, val, wrong = ">", b - a, b + a
            move = "subtract $%d$ from both sides" % a
        elif kind == 1:
            stmt = "Solve: $x - %d \\le %d$." % (a, b)
            rel, val, wrong = "\\le", b + a, b - a
            move = "add $%d$ to both sides" % a
        elif kind == 2:
            stmt = "Solve: $%dx < %d$." % (a, a * b)
            rel, val, wrong = "<", b, a * b - a
            move = "divide both sides by $%d$ (positive, so the sign keeps its direction)" % a
        else:
            stmt = "Solve: $\\frac{x}{%d} \\ge %d$." % (a, b)
            rel, val, wrong = "\\ge", a * b, b
            move = "multiply both sides by $%d$" % a
        flip = {">": "<", "<": ">", "\\le": "\\ge", "\\ge": "\\le"}[rel]
        copt = _rel_opt(rel, val)
        dopts = [_rel_opt(flip, val), _rel_opt(rel, wrong), _rel_opt(flip, wrong)]
        expl = ("One move: %s, giving %s. The inequality sign only flips "
                "when you multiply or divide by a NEGATIVE — no negative "
                "here, so the direction stays." % (move, copt))
        check = ["(%s) - (%s) == 0" % (str(val), str(val))]
        check = ["%d == %d" % (val, val)]
        raws.append(dict(statement=stmt, copt=copt, dopts=dopts,
                         explanation=expl, check=check))
    return _mk12("A1-ineq1", raws)


def _gen_comp():
    """compound-inequality: count the integer solutions."""
    P = [(1, 3, 6), (-2, 1, 4), (0, -2, 5), (2, 4, 9), (-3, 2, 3),
         (1, -1, 8), (3, 5, 7), (-1, 3, 5), (0, 2, 7), (2, -3, 6),
         (-2, 4, 4), (1, 6, 5), (4, -2, 8), (-4, 1, 6)]
    raws = []
    for a, b, span in P:
        c = a + span
        cnt = c - a  # integers in (a-b, c-b]
        stmt = ("How many integers $x$ satisfy $%d < x %s \\le %d$?" %
                (a, ("+ %d" % b) if b >= 0 else ("- %d" % (-b)), c))
        dvals = [cnt + 1,  # counted the open endpoint too
                 cnt - 1,  # dropped the closed endpoint
                 cnt + 2]  # counted both ends of a strict double
        expl = ("Subtract $%d$ everywhere: $%d < x \\le %d$. The left end "
                "is strict (excluded), the right is included — that's "
                "$%d$ integers. Off-by-one errors come from mixing up "
                "which endpoint counts." % (b, a - b, c - b, cnt))
        check = ["floor(%d - (%d)) - floor(%d - (%d)) == %d" %
                 (c, b, a, b, cnt)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=cnt, dvals=dvals))
    return _mk12("A1-comp", raws)


def _gen_abseq():
    """absolute-equation: |x -/+ a| = b, give the larger solution."""
    P = [(3, 7), (-2, 5), (5, 2), (-4, 9), (1, 6), (6, 4), (-3, 8),
         (2, 3), (-5, 7), (4, 6), (-1, 4), (7, 3), (-6, 2), (5, 9)]
    raws = []
    for a, b in P:
        big, small = a + b, a - b
        core = "x - %d" % a if a >= 0 else "x + %d" % (-a)
        stmt = "Solve $|%s| = %d$. Give the LARGER solution." % (core, b)
        dvals = [small,      # the smaller solution
                 b - a,      # sign slip on the center
                 b]          # ignored the center entirely
        expl = ("The two solutions sit $%d$ on each side of $%d$: "
                "$x = %d$ or $x = %d$. The larger is $%d$; picking $%d$ "
                "grabs the left one." % (b, a, small, big, big, small))
        check = ["Abs((%d) - (%d)) == %d" % (big, a, b)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=big, dvals=dvals))
    return _mk12("A1-abseq", raws)


def _gen_inword():
    """inequality-word: at most (floor) / at least (ceiling)."""
    P = [(0, 7, 45), (1, 6, 40), (0, 9, 75), (1, 8, 50), (0, 4, 30),
         (1, 12, 100), (0, 6, 50), (1, 5, 32), (0, 8, 60), (1, 9, 70),
         (0, 12, 90), (1, 4, 27), (0, 5, 42), (1, 7, 55)]
    raws = []
    for kind, p, m in P:
        if kind == 0:
            ans = m // p
            stmt = ("Each photo takes $%d$ MB. Your card has $%d$ MB free. "
                    "AT MOST how many photos can you store?" % (p, m))
            dvals = [ans + 1,                # rounded up instead of down
                     Rational(m, p),          # left the exact fraction
                     ans - 1]                 # over-cautious rounding
            if Rational(m, p) == ans:
                dvals[1] = ans + 2
            expl = ("$%d \\div %d = %s$, and you can only store WHOLE "
                    "photos, so round DOWN to $%d$. Rounding up would "
                    "need more space than you have." %
                    (m, p, _fmt(Rational(m, p)), ans))
            check = ["floor(Rational(%d, %d)) == %d" % (m, p, ans)]
        else:
            ans = -((-m) // p)  # ceiling
            stmt = ("Each box holds $%d$ books. You must pack $%d$ books. "
                    "AT LEAST how many boxes do you need?" % (p, m))
            dvals = [m // p,                  # rounded down — books left over
                     Rational(m, p),          # left the exact fraction
                     ans + 1]                 # one box too many
            if Rational(m, p) == ans:
                dvals[0] = ans - 1
                dvals[1] = ans + 2
            expl = ("$%d \\div %d = %s$; a part-full box is still a box "
                    "you need, so round UP to $%d$. Rounding down leaves "
                    "books unpacked." % (m, p, _fmt(Rational(m, p)), ans))
            check = ["ceiling(Rational(%d, %d)) == %d" % (m, p, ans)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=ans, dvals=dvals))
    return _mk12("A1-inword", raws)


def _gen_fsum():
    """function-sum: f(p) + f(q) for linear f."""
    P = [(2, 3, 1, 4), (-3, 5, 2, -1), (4, -2, 3, 5), (5, 1, -2, 3),
         (-2, 4, 1, 6), (3, -5, 4, 2), (2, 6, -3, 1), (-4, 2, 5, -2),
         (6, -1, 2, 4), (3, 4, -1, 5), (-2, -3, 6, 2), (4, 5, 1, -3),
         (5, -4, 3, 6), (-3, 2, 4, 1)]
    raws = []
    for a, b, p, q in P:
        val = a * (p + q) + 2 * b
        stmt = ("For $f(x) = %s$, find $f(%d) + f(%d)$." %
                (_lin_str(a, b), p, q))
        dvals = [a * (p + q) + b,   # only counted b once
                 a * (p * q) + b,   # multiplied the inputs
                 a * (p + q)]       # dropped both constants
        expl = ("Each evaluation brings its own constant: "
                "$f(%d) + f(%d) = (%d) + (%d) = %d$. Computing "
                "$f(%d + %d)$ instead counts the $%d$ only once." %
                (p, q, a * p + b, a * q + b, val, p, q, b))
        check = ["(%d)*(%d) + (%d) + (%d)*(%d) + (%d) == %d" %
                 (a, p, b, a, q, b, val)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=val, dvals=dvals))
    return _mk12("A1-fsum", raws)


def _gen_fdom():
    """function-domain: excluded value (rational) / domain (sqrt)."""
    P = [(0, 3, 4), (1, 5, 0), (0, -2, 3), (1, -4, 0), (0, 6, 2),
         (1, 2, 0), (0, -5, 7), (1, 7, 0), (0, 4, 5), (1, -6, 0),
         (0, -3, 2), (1, 3, 0), (0, 7, 6), (1, -2, 0)]
    raws = []
    for kind, a, c in P:
        core = "x - %d" % a if a >= 0 else "x + %d" % (-a)
        if kind == 0:
            stmt = ("For $f(x) = \\frac{%d}{%s}$, which value of $x$ is "
                    "NOT in the domain?" % (c, core))
            dvals = [-a,      # sign slip
                     c,       # grabbed the numerator
                     a + c]   # combined the two numbers
            expl = ("Division by zero is the only ban: $%s = 0$ at "
                    "$x = %d$. The numerator never restricts the domain." %
                    (core, a))
            check = ["(%d) - (%d) == 0" % (a, a)]
            raws.append(dict(statement=stmt, explanation=expl, check=check,
                             correct=a, dvals=dvals))
        else:
            stmt = ("For $f(x) = \\sqrt{%s}$, what is the domain?" % core)
            copt = "$x \\ge %d$" % a
            dopts = ["$x > %d$" % a,     # lost the boundary point
                     "$x \\le %d$" % a,  # flipped the direction
                     "$x \\ge %d$" % (-a)]  # sign slip
            expl = ("The radicand must be $\\ge 0$: $%s \\ge 0$ gives "
                    "$x \\ge %d$ — and $x = %d$ itself IS allowed "
                    "($\\sqrt{0} = 0$)." % (core, a, a))
            check = ["sqrt((%d) - (%d)) == 0" % (a, a)]
            raws.append(dict(statement=stmt, copt=copt, dopts=dopts,
                             explanation=expl, check=check))
    return _mk12("A1-fdom", raws)


def _gen_ftab():
    """function-table: read f(k) from listed pairs."""
    T = [([3, 7, 2, 9], 2), ([5, 1, 8, 4], 3), ([6, 2, 9, 3], 1),
         ([4, 8, 1, 5], 4), ([7, 3, 6, 2], 2), ([2, 9, 5, 7], 1),
         ([8, 4, 3, 6], 3), ([1, 6, 9, 2], 4), ([9, 5, 2, 8], 1),
         ([3, 8, 6, 1], 2), ([5, 2, 7, 9], 4), ([6, 1, 4, 8], 3),
         ([2, 7, 3, 5], 1), ([8, 3, 5, 2], 4)]
    raws = []
    for vals, k in T:
        pairs = ", ".join("$f(%d) = %d$" % (i + 1, v)
                          for i, v in enumerate(vals))
        ans = vals[k - 1]
        stmt = ("A function is given by its table: %s. Find $f(%d)$." %
                (pairs, k))
        others = [v for i, v in enumerate(vals) if i != k - 1]
        dvals = others[:3]
        expl = ("Read the pair whose INPUT is $%d$: $f(%d) = %d$. The "
                "other values belong to different inputs — the input "
                "picks the row, nothing else." % (k, k, ans))
        check = ["%d == %d" % (ans, ans)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=ans, dvals=dvals))
    return _mk12("A1-ftab", raws)


def _gen_read():
    """slope-intercept-read: read m or b straight off y = mx + b."""
    P = [(0, Rational(2), 5), (1, Rational(-3), 4), (0, Rational(1, 2), -3),
         (1, Rational(3, 4), 2), (0, Rational(-5), 7), (1, Rational(4), -6),
         (0, Rational(-1, 3), 2), (1, Rational(-2), -5), (0, Rational(3), -8),
         (1, Rational(2, 5), 3), (0, Rational(-4), 1), (1, Rational(5), 9),
         (0, Rational(7), -2), (1, Rational(-3, 2), 6)]
    raws = []
    for which, m, b in P:
        stmt_core = "$y = %s$" % _mxb(m, b)
        if which == 0:
            stmt = "For the line %s: what is the SLOPE?" % stmt_core
            correct, dvals = m, [Rational(b), -m, m + b]
            expl = ("In $y = mx + b$ the slope is the coefficient ON $x$: "
                    "$m = %s$. The lone constant $%d$ is the y-intercept, "
                    "not the slope." % (_fmt(m), b))
        else:
            stmt = "For the line %s: what is the Y-INTERCEPT?" % stmt_core
            correct, dvals = Rational(b), [m, Rational(-b), m * b]
            expl = ("The y-intercept is the constant term: $b = %d$ (the "
                    "value of $y$ when $x = 0$). $%s$ is the slope." %
                    (b, _fmt(m)))
        check = ["Rational(%d, %d) == Rational(%d, %d)" %
                 (m.p, m.q, m.p, m.q)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=correct, dvals=dvals))
    return _mk12("A1-read", raws)


def _gen_perp():
    """parallel-perpendicular-slope."""
    P = [(0, Rational(2)), (1, Rational(-3)), (0, Rational(1, 2)),
         (1, Rational(3, 4)), (0, Rational(-5)), (1, Rational(4)),
         (0, Rational(-2, 3)), (1, Rational(-2)), (0, Rational(3)),
         (1, Rational(2, 5)), (0, Rational(-4)), (1, Rational(5)),
         (0, Rational(5, 2)), (1, Rational(-3, 2))]
    B = [3, -2, 5, 1, -4, 6, 2, -3, 4, -1, 7, 2, -5, 3]
    raws = []
    for i, (which, m) in enumerate(P):
        b = B[i % len(B)]
        stmt_core = "$y = %s$" % _mxb(m, b)
        if which == 0:
            stmt = ("A line PERPENDICULAR to %s has what slope?" % stmt_core)
            correct = Rational(-1) / m
            dvals = [m, -m, Rational(1) / m]
            expl = ("Perpendicular slopes are NEGATIVE RECIPROCALS: flip "
                    "$%s$ and change its sign, giving $%s$. Only negating "
                    "(or only flipping) is half the job." %
                    (_fmt(m), _fmt(correct)))
        else:
            stmt = ("A line PARALLEL to %s has what slope?" % stmt_core)
            correct = m
            dvals = [Rational(-1) / m, -m, Rational(b)]
            expl = ("Parallel lines have the SAME slope: $%s$. The negative "
                    "reciprocal $%s$ would be perpendicular instead." %
                    (_fmt(m), _fmt(Rational(-1) / m)))
        check = ["Rational(%d, %d) * Rational(%d, %d) == -1" %
                 (m.p, m.q, (Rational(-1) / m).p, (Rational(-1) / m).q)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=correct, dvals=dvals))
    return _mk12("A1-perp", raws)


def _gen_xint():
    """x-intercept of y = mx + b (integer answers, m not ±1)."""
    P = [(2, -6), (3, 9), (-2, 8), (4, -12), (5, 10), (-3, -9),
         (2, 10), (-4, 8), (3, -15), (6, 12), (-5, 10), (4, 8),
         (2, -14), (-6, 18)]
    raws = []
    for m, b in P:
        x0 = Rational(-b, m)
        stmt = ("Find the x-intercept of $y = %s$ (the value of $x$ "
                "where the line crosses the x-axis)." % _mxb(Rational(m), b))
        dvals = [Rational(b), Rational(b, m), Rational(-b)]
        expl = ("Set $y = 0$: $%s = 0$ gives $x = %s$. The constant $%d$ "
                "by itself is the Y-intercept — the other axis." %
                (_mxb(Rational(m), b), _fmt(x0), b))
        check = ["(%d) * Rational(%d, %d) + (%d) == 0" % (m, -b, m, b)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=x0, dvals=dvals))
    return _mk12("A1-xint", raws)


def _gen_std():
    """standard-to-slope: slope of Ax + By = C is -A/B."""
    P = [(3, 4, 8), (2, -5, 10), (1, 3, -6), (5, 2, 4), (4, -3, 9),
         (2, 7, 14), (6, 5, -10), (3, -2, 12), (7, 4, 8), (1, -6, 6),
         (5, 3, -9), (4, 7, 21), (2, 3, 5), (8, -5, 20)]
    raws = []
    for A, Bc, C in P:
        slope = Rational(-A, Bc)
        y_term = "+ %dy" % Bc if Bc > 0 else "- %dy" % (-Bc)
        ax = "x" if A == 1 else "%dx" % A
        stmt = "What is the slope of the line $%s %s = %d$?" % (ax, y_term, C)
        dvals = [Rational(A, Bc), Rational(-Bc, A), Rational(C, Bc)]
        expl = ("Solve for $y$: $%dy = -%s + %d$, so the slope is "
                "$-\\frac{%d}{%d} = %s$. Forgetting the minus (or flipping "
                "the fraction) are the two classic slips." %
                (Bc, ax, C, A, Bc, _fmt(slope)))
        check = ["Rational(-%d, %d) == Rational(%d, %d)" %
                 (A, Bc, slope.p, slope.q)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=slope, dvals=dvals))
    return _mk12("A1-std", raws)


def _gen_subst():
    """substitution-solve: y = ax + b into cx + dy = e."""
    P = [(2, 3, 1, 2, 3), (-1, 2, -3, 3, 2), (3, -2, 4, 2, 5),
         (1, 4, 2, 5, 2), (-2, 3, 5, 4, 3), (2, -4, 3, 3, 4),
         (4, 2, -1, 2, 3), (-3, 5, 2, 3, 2), (1, -3, 6, 4, 5),
         (3, 4, -2, 5, 3), (-2, 2, 4, 2, 7), (2, 5, -3, 3, 2),
         (5, -1, 2, 4, 3), (-1, 3, 3, 2, 5)]
    raws = []
    for x, a, b, c, d in P:
        y = a * x + b
        e = c * x + d * y
        stmt = ("The system: $y = %s$ and $%dx + %dy = %d$. Find $x$." %
                (_lin_str(a, b), c, d, e))
        dvals = [y,    # solved for y and reported it
                 -x,   # sign slip
                 x + 1]
        expl = ("Substitute the first rule into the second: "
                "$%dx + %d(%s) = %d$ collapses to one equation in $x$, "
                "giving $x = %d$ (and $y = %d$ — a common mix-up is "
                "reporting $y$)." % (c, d, _lin_str(a, b), e, x, y))
        check = ["(%d)*(%d) + (%d)*((%d)*(%d) + (%d)) == %d" %
                 (c, x, d, a, x, b, e)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=x, dvals=dvals))
    return _mk12("A1-subst", raws)


def _gen_sysw():
    """system-word: sum s, difference d -> larger number."""
    P = [(14, 4), (20, 6), (17, 5), (26, 8), (15, 3), (32, 10),
         (21, 7), (18, 2), (29, 9), (24, 4), (35, 11), (16, 6),
         (27, 5), (40, 12)]
    raws = []
    for s, d in P:
        big = (s + d) // 2
        stmt = ("Two numbers have sum $%d$ and difference $%d$. "
                "Find the LARGER number." % (s, d))
        dvals = [(s - d) // 2,  # the smaller number
                 s - d,         # subtracted instead of averaging
                 Rational(s, 2)]  # ignored the difference
        expl = ("Add the two facts: $2x = %d + %d$, so the larger is "
                "$%d$ (and the smaller is $%d$). Halving the sum alone "
                "ignores the difference." % (s, d, big, (s - d) // 2))
        check = ["Rational(%d + %d, 2) == %d" % (s, d, big)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=big, dvals=dvals))
    return _mk12("A1-sysw", raws)


def _gen_scount():
    """solution-count: parallel / same line / intersecting."""
    P = [(0, 2, 3, 2, 5), (1, 3, -2, 4, 1), (2, -2, 4, -2, 4),
         (0, -3, 1, -3, 6), (1, 2, 5, -3, 2), (2, 4, -1, 4, -1),
         (0, 5, -2, 5, 3), (1, -4, 3, 2, -5), (2, -3, 2, -3, 2),
         (0, 4, 6, 4, -2), (1, 5, 1, -2, 4), (2, 2, -3, 2, -3),
         (0, -2, 5, -2, -1), (1, 6, 2, 3, 5)]
    raws = []
    for kind, m1, b1, m2, b2 in P:
        stmt = ("The system: $y = %s$ and $y = %s$. How many solutions "
                "does it have?" % (_lin_str(m1, b1), _lin_str(m2, b2)))
        if kind == 0:
            copt, why = "$0$", ("equal slopes but different intercepts — "
                                "parallel lines never meet")
            check = ["Eq(%d, %d)" % (m1, m2), "Ne(%d, %d)" % (b1, b2)]
        elif kind == 1:
            copt, why = "$1$", ("different slopes — the lines cross at "
                                "exactly one point")
            check = ["Ne(%d, %d)" % (m1, m2)]
        else:
            copt, why = "infinitely many", ("both equations describe the "
                                            "SAME line")
            check = ["Eq(%d, %d)" % (m1, m2), "Eq(%d, %d)" % (b1, b2)]
        dopts = [o for o in ("$0$", "$1$", "$2$", "infinitely many")
                 if o != copt][:3]
        expl = ("Compare slopes first: here %s. A linear system can only "
                "have $0$, $1$, or infinitely many solutions — never "
                "exactly $2$." % why)
        raws.append(dict(statement=stmt, copt=copt, dopts=dopts,
                         explanation=expl, check=check))
    return _mk12("A1-scount", raws)


def _gen_gcf():
    """gcf-factor: pull the greatest common factor from ax^2 + bx."""
    P = [(6, 9), (8, 12), (10, 15), (4, 6), (9, 12), (14, 21),
         (6, 8), (15, 20), (12, 18), (10, 25), (8, 20), (18, 24),
         (12, 16), (21, 28)]
    raws = []
    for a, b in P:
        import math as _m
        g = _m.gcd(a, b)
        p, q = a // g, b // g
        if p == q:
            continue
        copt = "$%dx(%dx + %d)$" % (g, p, q)
        stmt = "Factor completely: $%dx^2 + %dx$." % (a, b)
        dopts = ["$x(%dx + %d)$" % (a, b),        # pulled only x
                 "$%d(%dx^2 + %dx)$" % (g, p, q),  # pulled only the number
                 "$%dx(%dx + %d)$" % (g, q, p)]    # swapped the leftovers
        expl = ("The GCF of $%dx^2$ and $%dx$ is $%dx$ — the biggest "
                "NUMBER times the highest shared power of $x$. Pulling "
                "only one of the two leaves the factoring unfinished." %
                (a, b, g))
        check = ["expand(%d*x*(%d*x + %d) - (%d*x**2 + %d*x)) == 0" %
                 (g, p, q, a, b)]
        raws.append(dict(statement=stmt, copt=copt, dopts=dopts,
                         explanation=expl, check=check))
    return _mk12("A1-gcf", raws)


def _gen_dos():
    """difference-of-squares: positive root of x^2 - k^2 = 0."""
    K = [3, 5, 7, 4, 9, 6, 11, 8, 12, 10, 13, 15, 14, 16]
    raws = []
    for k in K:
        Ksq = k * k
        stmt = ("Solve $x^2 - %d = 0$. Give the POSITIVE solution." % Ksq)
        dvals = [Ksq,               # never took the root
                 Rational(Ksq, 2),  # halved instead of rooting
                 k + 1]
        expl = ("Factor as $(x - %d)(x + %d) = 0$ — or just take the "
                "root: $x = \\pm%d$; the positive one is $%d$. Halving "
                "$%d$ is not the inverse of squaring." %
                (k, k, k, k, Ksq))
        check = ["(%d)**2 == %d" % (k, Ksq)]
        raws.append(dict(statement=stmt, explanation=expl, check=check,
                         correct=k, dvals=dvals))
    return _mk12("A1-dos", raws)


# --- batch-2 resolvers (independent: regex the statement, recompute) -------

def _rz_oop(s):
    m = re.search(r"Evaluate: \$(\d+) \+ (\d+) \\cdot \((\d+) - (\d+)\)\^2\$", s)
    if m:
        a, b, c, d = map(int, m.groups())
        return ("num", a + b * (c - d) ** 2)
    m = re.search(r"Evaluate: \$(\d+) - (\d+) \\cdot \((\d+) \+ (\d+)\)\$", s)
    if m:
        a, b, c, d = map(int, m.groups())
        return ("num", a - b * (c + d))
    m = re.search(r"Evaluate: \$(\d+) \+ (\d+) \\cdot (\d+)\^2\$", s)
    a, b, c = map(int, m.groups())
    return ("num", a + b * c ** 2)


def _rz_clt(s):
    m = re.search(r"\$(\d+)x \+ (\d+) - (\d+)x \+ (\d+)\$", s)
    a, b, c, d = map(int, m.groups())
    return ("num", a - c if "coefficient" in s else b + d)


def _rz_dist(s):
    m = re.search(r"\$(\d+)\((\d+)x \+ (\d+)\) - (\d+)\((\d+)x \+ (\d+)\)\$", s)
    a, b, c, d, e, f_ = map(int, m.groups())
    return ("num", a * b - d * e if "coefficient" in s else a * c - d * f_)


def _rz_words(s):
    m = re.search(r"'(\d+) less than (\d+) times a number", s)
    if m:
        k, mm = int(m.group(1)), int(m.group(2))
        return ("opt", "$%dn - %d$" % (mm, k))
    m = re.search(r"'(\d+) more than (\d+) times a number", s)
    if m:
        k, mm = int(m.group(1)), int(m.group(2))
        return ("opt", "$%dn + %d$" % (mm, k))
    m = re.search(r"'twice the sum of a number \$n\$ and (\d+)'", s)
    if m:
        return ("opt", "$2(n + %d)$" % int(m.group(1)))
    m = re.search(r"quotient of a number \$n\$ and (\d+), increased by (\d+)", s)
    if m:
        k, mm = int(m.group(1)), int(m.group(2))
        return ("opt", "$\\frac{n}{%d} + %d$" % (k, mm))
    m = re.search(r"product of (\d+) and a number \$n\$, decreased by (\d+)", s)
    mm, k = int(m.group(1)), int(m.group(2))
    return ("opt", "$%dn - %d$" % (mm, k))


def _rz_both(s):
    m = re.search(r"Solve: \$(.+?) = (.+?)\$\.", s)
    sols = solve(_parse_expr(m.group(1)) - _parse_expr(m.group(2)), _X)
    return ("num", sols[0])


def _rz_deq(s):
    m = re.search(r"Solve: \$(-?\d+)\(x ([+-]) (\d+)\) = (-?\d+)\$", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(m.group(4))
    return ("num", Rational(c, a) - b)


def _rz_freq(s):
    m = re.search(r"\\frac\{x\}\{(\d+)\} ([+-]) (\d+) = (-?\d+)", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(m.group(4))
    return ("num", a * (c - b))


_LIT_MAP = {(row[0], row[1]): row[2] for row in _LIT}


def _rz_lit(s):
    m = re.search(r"Solve \$(.+?)\$ for \$(\w+)\$", s)
    return ("opt", _LIT_MAP[(m.group(1), m.group(2))])


def _rz_ineq1(s):
    m = re.search(r"Solve: \$x \+ (\d+) > (\d+)\$", s)
    if m:
        return ("opt", _rel_opt(">", int(m.group(2)) - int(m.group(1))))
    m = re.search(r"Solve: \$x - (\d+) \\le (\d+)\$", s)
    if m:
        return ("opt", _rel_opt("\\le", int(m.group(2)) + int(m.group(1))))
    m = re.search(r"Solve: \$(\d+)x < (\d+)\$", s)
    if m:
        return ("opt", _rel_opt("<", Rational(int(m.group(2)), int(m.group(1)))))
    m = re.search(r"Solve: \$\\frac\{x\}\{(\d+)\} \\ge (\d+)\$", s)
    return ("opt", _rel_opt("\\ge", int(m.group(1)) * int(m.group(2))))


def _rz_comp(s):
    m = re.search(r"\$(-?\d+) < x ([+-]) (\d+) \\le (-?\d+)\$", s)
    a = int(m.group(1))
    b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    c = int(m.group(4))
    lo, hi = a - b, c - b
    return ("num", len([n for n in range(lo + 1, hi + 1)]))


def _rz_abseq(s):
    m = re.search(r"\$\|x ([+-]) (\d+)\| = (\d+)\$", s)
    a = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
    b = int(m.group(3))
    return ("num", a + b)


def _rz_inword(s):
    nums = [int(n) for n in re.findall(r"\$(\d+)\$", s)]
    p, m = nums[0], nums[1]
    if "AT MOST" in s:
        return ("num", m // p)
    return ("num", -((-m) // p))


def _rz_fsum(s):
    m = re.search(r"f\(x\) = (.+?)\$, find \$f\((-?\d+)\) \+ f\((-?\d+)\)\$", s)
    fx = _parse_expr(m.group(1))
    return ("num", fx.subs(_X, int(m.group(2))) + fx.subs(_X, int(m.group(3))))


def _rz_fdom(s):
    if "NOT in the domain" in s:
        m = re.search(r"\{x ([+-]) (\d+)\}", s)
        return ("num", int(m.group(2)) * (1 if m.group(1) == "-" else -1))
    m = re.search(r"sqrt\{x ([+-]) (\d+)\}", s)
    a = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
    return ("opt", "$x \\ge %d$" % a)


def _rz_ftab(s):
    pairs = dict((int(i), int(v))
                 for i, v in re.findall(r"\$f\((\d+)\) = (\d+)\$", s))
    k = int(re.search(r"Find \$f\((\d+)\)\$", s).group(1))
    return ("num", pairs[k])


def _parse_mxb(t):
    t = t.replace(" ", "")
    m = re.match(
        r"^(-?)(?:\\frac\{(\d+)\}\{(\d+)\}|(\d+))?x(?:([+-])(\d+))?$", t)
    sign = -1 if m.group(1) else 1
    if m.group(2):
        slope = Rational(int(m.group(2)), int(m.group(3))) * sign
    elif m.group(4):
        slope = Rational(int(m.group(4))) * sign
    else:
        slope = Rational(sign)
    b = 0
    if m.group(5):
        b = int(m.group(6)) * (1 if m.group(5) == "+" else -1)
    return slope, b


def _rz_read(s):
    m = re.search(r"\$y = (.+?)\$", s)
    slope, b = _parse_mxb(m.group(1))
    return ("num", slope if "SLOPE" in s else Rational(b))


def _rz_perp(s):
    m = re.search(r"\$y = (.+?)\$", s)
    slope, _b = _parse_mxb(m.group(1))
    return ("num", Rational(-1) / slope if "PERPENDICULAR" in s else slope)


def _rz_xint(s):
    m = re.search(r"\$y = (.+?)\$", s)
    slope, b = _parse_mxb(m.group(1))
    return ("num", Rational(-b) / slope)


def _rz_std(s):
    m = re.search(r"\$(?:(\d+))?x ([+-]) (\d+)y = (-?\d+)\$", s)
    A = int(m.group(1)) if m.group(1) else 1
    Bc = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
    return ("num", Rational(-A, Bc))


def _rz_subst(s):
    m = re.search(r"\$y = (.+?)\$ and \$(\d+)x \+ (\d+)y = (-?\d+)\$", s)
    fx = _parse_expr(m.group(1))
    c, d, e = int(m.group(2)), int(m.group(3)), int(m.group(4))
    sols = solve(c * _X + d * fx - e, _X)
    return ("num", sols[0])


def _rz_sysw(s):
    m = re.search(r"sum \$(\d+)\$ and difference \$(\d+)\$", s)
    return ("num", Rational(int(m.group(1)) + int(m.group(2)), 2))


def _rz_scount(s):
    m = re.search(r"\$y = (.+?)\$ and \$y = (.+?)\$", s)
    e1, e2 = _parse_expr(m.group(1)), _parse_expr(m.group(2))
    m1, b1 = e1.coeff(_X), e1.subs(_X, 0)
    m2, b2 = e2.coeff(_X), e2.subs(_X, 0)
    if m1 != m2:
        return ("opt", "$1$")
    if b1 != b2:
        return ("opt", "$0$")
    return ("opt", "infinitely many")


def _rz_gcf(s):
    import math as _m
    mm = re.search(r"\$(\d+)x\^2 \+ (\d+)x\$", s)
    a, b = int(mm.group(1)), int(mm.group(2))
    g = _m.gcd(a, b)
    return ("opt", "$%dx(%dx + %d)$" % (g, a // g, b // g))


def _rz_dos(s):
    m = re.search(r"\$x\^2 - (\d+) = 0\$", s)
    from sympy import sqrt as _sqrt
    return ("num", _sqrt(int(m.group(1))))


_BATCH2_META = [
    ("order-of-operations", "Order of operations", 1,
     "expressions-and-operations",
     "Parentheses, exponents, then multiply/divide, then add/subtract.",
     _gen_oop, _rz_oop),
    ("combine-like-terms", "Combining like terms", 1,
     "expressions-and-operations",
     "x-terms combine with x-terms; the minus sign travels with its term.",
     _gen_clt, _rz_clt),
    ("distribute-simplify", "Distribute, then combine", 2,
     "expressions-and-operations",
     "Push each outside factor through its parentheses — the minus hits every term.",
     _gen_dist, _rz_dist),
    ("words-to-algebra", "Words to algebra", 1,
     "expressions-and-operations",
     "'Less than' reverses the order; 'the sum' demands parentheses.",
     _gen_words, _rz_words),
    ("equation-both-sides", "Variables on both sides", 1, "linear-equations",
     "Collect x on one side, constants on the other; crossing terms flip sign.",
     _gen_both, _rz_both),
    ("distribute-equation", "Equations with parentheses", 2,
     "linear-equations",
     "Divide by the outside factor (or distribute) before moving constants.",
     _gen_deq, _rz_deq),
    ("fraction-equation", "Equations with fractions", 2, "linear-equations",
     "Clear the fraction by multiplying both sides by the denominator.",
     _gen_freq, _rz_freq),
    ("solve-for-variable", "Solving for a variable", 3, "linear-equations",
     "Same moves as with numbers — undo operations in reverse order.",
     _gen_lit, _rz_lit),
    ("one-step-inequality", "One-step inequalities", 1, "inequalities",
     "One inverse move; the sign flips only for a negative multiply/divide.",
     _gen_ineq1, _rz_ineq1),
    ("compound-inequality", "Compound inequalities", 2, "inequalities",
     "Apply the move to all three parts; watch which endpoint is included.",
     _gen_comp, _rz_comp),
    ("absolute-equation", "Absolute-value equations", 2, "inequalities",
     "|x − a| = b puts x at distance b on BOTH sides of a.",
     _gen_abseq, _rz_abseq),
    ("inequality-word", "Inequality word problems", 2, "inequalities",
     "'At most' rounds down; 'at least' rounds up — context picks the direction.",
     _gen_inword, _rz_inword),
    ("function-sum", "Adding function values", 2, "functions",
     "Evaluate each input separately — every evaluation brings its own constant.",
     _gen_fsum, _rz_fsum),
    ("function-domain", "Domain of a function", 2, "functions",
     "Ban division by zero; keep radicands ≥ 0.",
     _gen_fdom, _rz_fdom),
    ("function-table", "Reading a function table", 1, "functions",
     "The input picks the row: f(input) = output.",
     _gen_ftab, _rz_ftab),
    ("slope-intercept-read", "Slope and intercept by sight", 1,
     "linear-functions",
     "y = mx + b: m rides on x, b stands alone.",
     _gen_read, _rz_read),
    ("parallel-perpendicular-slope", "Parallel & perpendicular slopes", 2,
     "linear-functions",
     "Parallel: same slope. Perpendicular: negative reciprocal.",
     _gen_perp, _rz_perp),
    ("x-intercept", "The x-intercept", 2, "linear-functions",
     "Set y = 0 and solve — the line crosses the x-axis where y vanishes.",
     _gen_xint, _rz_xint),
    ("standard-to-slope", "Slope from standard form", 3, "linear-functions",
     "Ax + By = C has slope −A/B — solve for y to see it.",
     _gen_std, _rz_std),
    ("substitution-solve", "Solving by substitution", 1,
     "systems-of-equations",
     "Replace y with its rule; one equation in x remains.",
     _gen_subst, _rz_subst),
    ("system-word", "Sum-and-difference problems", 2, "systems-of-equations",
     "Adding the equations eliminates one unknown instantly.",
     _gen_sysw, _rz_sysw),
    ("solution-count", "How many solutions?", 3, "systems-of-equations",
     "Compare slopes, then intercepts: 1, 0, or infinitely many — never 2.",
     _gen_scount, _rz_scount),
    ("gcf-factor", "Factoring out the GCF", 1, "polynomials-and-factoring",
     "Pull the biggest number AND the highest shared power of x.",
     _gen_gcf, _rz_gcf),
    ("difference-of-squares", "Difference of squares", 2,
     "polynomials-and-factoring",
     "x² − k² = (x − k)(x + k); the solutions are ±k.",
     _gen_dos, _rz_dos),
]


def _batch2_forms():
    forms = []
    for fid, title, level, unit, skill, gen, _rz in _BATCH2_META:
        forms.append({"id": fid, "title": title, "level": level,
                      "unit": unit, "skill": skill, "variants": gen()})
    return forms


_NEW_FORMS_BATCH1 = new_forms


def new_forms():
    return _NEW_FORMS_BATCH1() + _batch2_forms()


RESOLVERS.update({fid: rz for fid, _t, _l, _u, _s, _g, rz in _BATCH2_META})


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
