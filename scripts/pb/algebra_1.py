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
