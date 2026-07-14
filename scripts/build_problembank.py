#!/usr/bin/env python3
"""Problem-bank builder — generates data/problembank/*.json.

Every topic is a list of FORMS (exam archetypes, level-tagged 1..3); every
form carries 4+ VARIANTS — the same form with different numbers. Variants are
what the runner serves when a student misses ("practice a similar one").

All answers, distractors, and sympy `check[]` strings are COMPUTED here, not
hand-written, so the bank inherits the platform's zero-mistake discipline.
Regenerate with:  python3 scripts/build_problembank.py
Verify with:      npm run verify:bank
"""
import json
import os
from fractions import Fraction

import sympy as sp
from sympy import Rational, sqrt, pi, latex, nsimplify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "problembank")
os.makedirs(OUT, exist_ok=True)

x = sp.Symbol("x")


def lat(e):
    return latex(nsimplify(e))


def M(s):
    return f"${s}$"


def pick_ds(ans, pool):
    """3 distinct distractors != ans, padding with offsets when the pool thins."""
    out = []
    for c in pool:
        if c != ans and c not in out:
            out.append(c)
        if len(out) == 3:
            return out
    k = 1
    while len(out) < 3:
        for cand in (ans + k, ans - k):
            if cand != ans and cand not in out:
                out.append(cand)
                if len(out) == 3:
                    break
        k += 1
    return out


def pick_ds_sym(ans, pool):
    """3 distinct symbolic distractors != ans (simplify-compared), padded."""
    out = []
    for c in pool:
        c = sp.nsimplify(c)
        if sp.simplify(c - ans) != 0 and not any(sp.simplify(c - o) == 0 for o in out):
            out.append(c)
        if len(out) == 3:
            return out
    k = 1
    while len(out) < 3:
        for cand in (ans + k, ans - k):
            cand = sp.nsimplify(cand)
            if sp.simplify(cand - ans) != 0 and not any(sp.simplify(cand - o) == 0 for o in out):
                out.append(cand)
                if len(out) == 3:
                    break
        k += 1
    return out


def variant(vid, statement, correct, distractors, explanation, check, geo=None):
    """Assemble a variant with the correct answer FIRST (runner shuffles)."""
    opts = [correct] + list(distractors)
    assert len(opts) == 4, f"{vid}: need exactly 4 options, got {len(opts)}"
    assert len(set(opts)) == 4, f"{vid}: duplicate options {opts}"
    v = {
        "id": vid,
        "statement": statement,
        "options": opts,
        "correctIndex": 0,
        "explanation": explanation,
        "check": check,
    }
    if geo:
        v["geoFigure"] = geo
    return v


def form(fid, title, level, skill, variants):
    assert level in (1, 2, 3)
    assert len(variants) >= 4, f"{fid}: needs >= 4 variants"
    return {"id": fid, "title": title, "level": level, "skill": skill, "variants": variants}


# ---------------------------------------------------------------------------
# Topic 1 — Algebra
# ---------------------------------------------------------------------------

def t_algebra():
    forms = []

    # L1: two-step linear equation
    vs = []
    for i, (a, b, c) in enumerate([(3, 5, 20), (4, -7, 13), (5, 8, 43), (7, -4, 24)], 1):
        sol = Fraction(c - b, a)
        assert sol.denominator == 1
        s = int(sol)
        wrong = {Fraction(c + b, a), Fraction(b - c, a), Fraction(s + 1)}
        wrong.discard(Fraction(s))
        ds = [M(lat(Rational(w.numerator, w.denominator))) for w in sorted(wrong)][:3]
        bs = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        vs.append(variant(
            f"alg-lin-v{i}",
            f"Solve: ${a}x {bs} = {c}$.",
            M(s), ds,
            f"Move the constant first: ${a}x = {c - b}$, then divide by ${a}$: $x = {s}$. Check: ${a} \\cdot {s} {bs} = {c}$ ✓.",
            [f"solve({a}*x + {b} - {c}, x) == [{s}]"],
        ))
    forms.append(form("linear-two-step", "Two-step linear equations", 1,
                      "Undo addition, then undo multiplication — in that order.", vs))

    # L1: exponent laws
    vs = []
    for i, (a, b, c) in enumerate([(5, 3, 4), (7, 2, 6), (4, 5, 3), (6, 4, 8)], 1):
        ans = a + b - c
        ds = pick_ds(ans, [a + b + c, a * b - c, a - b + c])
        vs.append(variant(
            f"alg-exp-v{i}",
            f"Simplify: $\\dfrac{{x^{{{a}}} \\cdot x^{{{b}}}}}{{x^{{{c}}}}}$.",
            M(f"x^{{{ans}}}"), [M(f"x^{{{d}}}") for d in ds],
            f"Multiplying powers adds exponents (${a}+{b}={a+b}$); dividing subtracts (${a+b}-{c}={ans}$). One add, one subtract — never multiply the exponents.",
            [f"{a} + {b} - {c} == {ans}"],
        ))
    forms.append(form("exponent-laws", "Exponent laws", 1,
                      "x^a·x^b = x^(a+b); division subtracts exponents.", vs))

    # L1: evaluate an expression
    vs = []
    for i, (p, q, a, b) in enumerate([(2, 3, 3, 4), (3, 2, 2, 5), (2, 5, 4, 3), (5, 2, 3, 2)], 1):
        ans = p * a ** 2 - q * b
        ds = pick_ds(ans, [(p * a) ** 2 - q * b, p * a ** 2 + q * b, p * a * 2 - q * b])
        vs.append(variant(
            f"alg-eval-v{i}",
            f"Evaluate ${p}a^2 - {q}b$ when $a = {a}$ and $b = {b}$.",
            M(ans), [M(d) for d in ds],
            f"Square first, multiply second: ${p} \\cdot {a}^2 = {p * a**2}$, then subtract ${q} \\cdot {b} = {q * b}$: answer ${ans}$. The classic slip is $({p}a)^2$ — the square belongs to $a$ alone.",
            [f"{p}*{a}**2 - {q}*{b} == {ans}"],
        ))
    forms.append(form("evaluate-expression", "Evaluating expressions", 1,
                      "Powers before products; substitute carefully.", vs))

    # L2: inequality with a sign flip
    vs = []
    for i, (a, b, c) in enumerate([(20, 4, 8), (15, 3, 6), (30, 5, 10), (14, 2, 6)], 1):
        bd = Fraction(a - c, b)
        assert bd.denominator == 1
        bd = int(bd)
        vs.append(variant(
            f"alg-ineq-v{i}",
            f"Solve: ${a} - {b}x < {c}$.",
            M(f"x > {bd}"),
            [M(f"x < {bd}"), M(f"x > {-bd}"), M(f"x < {-bd}")],
            f"Subtract ${a}$: $-{b}x < {c - a}$. Dividing by $-{b}$ FLIPS the inequality: $x > {bd}$. Test $x = {bd + 1}$: ${a} - {b*(bd+1)} < {c}$ ✓.",
            [f"Rational({a} - {c}, {b}) == {bd}", f"{a} - {b}*({bd}+1) < {c}", f"{a} - {b}*({bd}-1) > {c}"],
        ))
    forms.append(form("inequality-flip", "Inequalities with a sign flip", 2,
                      "Dividing by a negative reverses the inequality.", vs))

    # L2: 2x2 system
    vs = []
    for i, (x0, y0, a1, b1, a2, b2) in enumerate([(3, 2, 1, 1, 2, -1), (4, 1, 1, 1, 1, -1), (2, 5, 2, 1, 1, -1), (5, 3, 1, 2, 1, -1)], 1):
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 + b2 * y0
        ans = x0 + y0
        ds = pick_ds(ans, [x0 - y0, x0, ans + 1])
        t1 = f"{a1 if a1 != 1 else ''}x {'+' if b1 >= 0 else '-'} {abs(b1) if abs(b1) != 1 else ''}y = {c1}".replace("  ", " ")
        t2 = f"{a2 if a2 != 1 else ''}x {'+' if b2 >= 0 else '-'} {abs(b2) if abs(b2) != 1 else ''}y = {c2}".replace("  ", " ")
        vs.append(variant(
            f"alg-sys-v{i}",
            f"The system $\\begin{{cases}} {t1} \\\\ {t2} \\end{{cases}}$ has solution $(x; y)$. Find $x + y$.",
            M(ans), [M(d) for d in ds],
            f"Adding or substituting gives $x = {x0}$, $y = {y0}$ (check both equations!), so $x + y = {ans}$.",
            [f"{a1}*{x0} + {b1}*{y0} == {c1}", f"{a2}*{x0} + {b2}*{y0} == {c2}", f"{x0} + {y0} == {ans}"],
        ))
    forms.append(form("system-2x2", "Systems of two equations", 2,
                      "Eliminate one variable; always check the pair in BOTH equations.", vs))

    # L2: rational equation
    vs = []
    for i, (a, b, k) in enumerate([(6, 2, 3), (8, 2, 4), (10, 4, 3), (9, 3, 4)], 1):
        sol = Fraction(a - k * b, k - 1)
        assert sol.denominator == 1
        s = int(sol)
        assert s != -b
        ds = pick_ds(s, [s + 1, -s if s != 0 else s + 2, s - 1])
        vs.append(variant(
            f"alg-rat-v{i}",
            f"Solve: $\\dfrac{{x + {a}}}{{x + {b}}} = {k}$.",
            M(s), [M(d) for d in ds],
            f"Multiply both sides by $x + {b}$ (allowed since $x \\ne -{b}$): $x + {a} = {k}x + {k * b}$, so ${k - 1}x = {a - k * b}$ and $x = {s}$. Check the denominator: ${s} + {b} \\ne 0$ ✓.",
            [f"solve((x + {a})/(x + {b}) - {k}, x) == [{s}]", f"{s} + {b} != 0"],
        ))
    forms.append(form("rational-equation", "Rational equations", 2,
                      "Clear the denominator, solve, then verify the denominator isn't zero.", vs))

    # L3: absolute-value inequality
    vs = []
    for i, (a, b) in enumerate([(3, 5), (2, 7), (4, 3), (1, 6)], 1):
        lo, hi = a - b, a + b
        vs.append(variant(
            f"alg-abs-v{i}",
            f"Solve: $|x - {a}| \\le {b}$.",
            M(f"{lo} \\le x \\le {hi}"),
            [M(f"x \\le {hi}"), M(f"x \\le {lo} \\text{{ or }} x \\ge {hi}"), M(f"{-hi} \\le x \\le {-lo}")],
            f"$|x - {a}| \\le {b}$ means the distance from $x$ to ${a}$ is at most ${b}$: ${a} - {b} \\le x \\le {a} + {b}$, i.e. $[{lo}; {hi}]$. The 'or' split belongs to $\\ge$, not $\\le$.",
            [f"Abs({lo} - {a}) == {b}", f"Abs({hi} - {a}) == {b}", f"Abs({a} - {a}) < {b}"],
        ))
    forms.append(form("absolute-inequality", "Absolute-value inequalities", 3,
                      "|x − a| ≤ b is a distance statement: a ± b bracket the answer.", vs))

    # L3: parameter — when does a system have NO solution
    vs = []
    for i, (a1, b1, c1, a2, c2) in enumerate([(1, 2, 3, 2, 5), (1, 3, 4, 3, 7), (2, 1, 5, 4, 8), (1, 4, 6, 2, 9)], 1):
        m = Fraction(b1 * a2, a1)
        assert m.denominator == 1
        m = int(m)
        assert Fraction(c2, c1) != Fraction(a2, a1)  # truly no solution (not coincident)
        ds = pick_ds(m, [-m, m + 1, b1 * a1])
        vs.append(variant(
            f"alg-par-v{i}",
            f"For which value of $m$ does the system $\\begin{{cases}} {a1 if a1!=1 else ''}x + {b1}y = {c1} \\\\ {a2}x + my = {c2} \\end{{cases}}$ have NO solution?",
            M(m), [M(d) for d in ds],
            f"No solution = parallel lines: coefficients proportional but constants not. $\\frac{{{a2}}}{{{a1}}} = \\frac{{m}}{{{b1}}}$ gives $m = {m}$ — and $\\frac{{{c2}}}{{{c1}}} \\ne \\frac{{{a2}}}{{{a1}}}$ confirms they never meet.",
            [f"Rational({b1}*{a2}, {a1}) == {m}", f"Rational({c2}, {c1}) != Rational({a2}, {a1})"],
        ))
    forms.append(form("system-parameter", "Systems with a parameter", 3,
                      "No solution ⟺ slopes match, intercepts don't (proportional coefficients, unproportional constants).", vs))

    return {
        "slug": "algebra",
        "title": "Algebra",
        "titleMn": "Алгебр",
        "blurb": "Equations, inequalities, systems, exponents — the moves behind a third of any exam.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------
# Topic 2 — Functions & Quadratics
# ---------------------------------------------------------------------------

def t_functions():
    forms = []

    # L1: read the vertex
    vs = []
    for i, (h, k) in enumerate([(3, -4), (-2, 5), (4, 1), (-1, -6)], 1):
        hs = f"(x - {h})" if h >= 0 else f"(x + {abs(h)})"
        ks = f"+ {k}" if k >= 0 else f"- {abs(k)}"
        vs.append(variant(
            f"fun-vertex-v{i}",
            f"The parabola $y = {hs}^2 {ks}$ has its vertex at…",
            M(f"({h}; {k})"),
            [M(f"({-h}; {k})"), M(f"({h}; {-k})"), M(f"({k}; {h})")],
            f"Vertex form $y = (x - h)^2 + k$ puts the vertex at $(h; k)$: here $({h}; {k})$. Watch the sign: $(x - h)$ means the vertex sits at $+h$.",
            [f"({h} - {h})**2 + {k} == {k}", f"({h+1} - {h})**2 + {k} > {k}"],
        ))
    forms.append(form("vertex-read", "Reading the vertex", 1,
                      "y = (x−h)² + k has vertex (h; k) — mind the sign of h.", vs))

    # L1: roots of a factored quadratic
    vs = []
    for i, (p, q) in enumerate([(2, 7), (-3, 5), (4, 9), (-1, 6)], 1):
        ps = f"(x - {p})" if p >= 0 else f"(x + {abs(p)})"
        qs = f"(x - {q})" if q >= 0 else f"(x + {abs(q)})"
        ans = p + q
        ds = pick_ds(ans, [p * q, -(p + q), q - p])
        vs.append(variant(
            f"fun-roots-v{i}",
            f"The equation ${ps}{qs} = 0$ has roots $x_1$ and $x_2$. Find $x_1 + x_2$.",
            M(ans), [M(d) for d in ds],
            f"A product is zero when a factor is zero: $x = {p}$ or $x = {q}$. Sum: ${ans}$. (Vieta agrees: for $x^2 - {p+q}x + {p*q}$, the root sum is ${p+q}$.)",
            [f"solve((x - {p})*(x - {q}), x) == sorted([{p}, {q}])", f"{p} + {q} == {ans}"],
        ))
    forms.append(form("factored-roots", "Roots from factored form", 1,
                      "Zero-product property; Vieta's sum = −b/a.", vs))

    # L1: composition
    vs = []
    for i, (a, b, t) in enumerate([(2, 3, 2), (3, -1, 2), (2, 5, 3), (4, 1, 2)], 1):
        ans = a * t ** 2 + b
        ds = pick_ds(ans, [(a * t + b) ** 2, a * t + b, a * (t + b) ** 2])
        bs = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        vs.append(variant(
            f"fun-comp-v{i}",
            f"If $f(x) = {a}x {bs}$ and $g(x) = x^2$, find $f(g({t}))$.",
            M(ans), [M(d) for d in ds],
            f"Inside first: $g({t}) = {t**2}$. Then $f({t**2}) = {a} \\cdot {t**2} {bs} = {ans}$. The trap $({a} \\cdot {t} {bs})^2$ is $g(f({t}))$ — composition order matters.",
            [f"{a}*{t}**2 + {b} == {ans}"],
        ))
    forms.append(form("composition", "Composing functions", 1,
                      "f(g(x)): evaluate the inner function first.", vs))

    # L2: discriminant — how many real roots
    vs = []
    combos = [(1, 6, 9, "exactly one"), (1, 5, 7, "none"), (2, 7, 3, "two distinct"), (1, 4, 4, "exactly one")]
    for i, (a, b, c, kind) in enumerate(combos, 1):
        D = b * b - 4 * a * c
        correct = {"two distinct": "Two distinct real roots", "exactly one": "Exactly one real root", "none": "No real roots"}[kind]
        ds = [t for t in ["Two distinct real roots", "Exactly one real root", "No real roots"] if t != correct] + ["Infinitely many roots"]
        vs.append(variant(
            f"fun-disc-v{i}",
            f"How many real roots does ${a if a != 1 else ''}x^2 + {b}x + {c} = 0$ have?",
            correct, ds,
            f"Discriminant: $D = {b}^2 - 4 \\cdot {a} \\cdot {c} = {D}$. " +
            ("Positive ⟹ two distinct roots." if D > 0 else "Zero ⟹ one (repeated) root." if D == 0 else "Negative ⟹ no real roots."),
            [f"{b}**2 - 4*{a}*{c} == {D}"],
        ))
    forms.append(form("discriminant", "Counting roots with the discriminant", 2,
                      "D = b² − 4ac: positive two, zero one, negative none.", vs))

    # L2: minimum value by completing the square
    vs = []
    for i, (b, c) in enumerate([(6, 5), (8, 10), (4, 9), (10, 20)], 1):
        h = -b // 2
        mn = c - (b // 2) ** 2
        ds = pick_ds(mn, [c, -mn if -mn != mn else mn + 1, (b // 2) ** 2])
        vs.append(variant(
            f"fun-min-v{i}",
            f"Find the MINIMUM value of $y = x^2 + {b}x + {c}$.",
            M(mn), [M(d) for d in ds],
            f"Complete the square: $y = (x + {b // 2})^2 + ({mn})$. The square is never negative, so the minimum is ${mn}$, reached at $x = {h}$.",
            [f"({h})**2 + {b}*({h}) + {c} == {mn}", f"({h+1})**2 + {b}*({h+1}) + {c} > {mn}"],
        ))
    forms.append(form("complete-square-min", "Minimum via completing the square", 2,
                      "x² + bx + c = (x + b/2)² + (c − b²/4); the constant IS the minimum.", vs))

    # L2: quadratic inequality
    vs = []
    for i, (p, q) in enumerate([(1, 4), (2, 5), (-1, 3), (0, 6)], 1):
        b, c = -(p + q), p * q
        bs = f"+ {b}x" if b >= 0 else f"- {abs(b)}x"
        cs = f"+ {c}" if c >= 0 else f"- {abs(c)}"
        vs.append(variant(
            f"fun-qineq-v{i}",
            f"Solve: $x^2 {bs} {cs} < 0$.",
            M(f"{p} < x < {q}"),
            [M(f"x < {p} \\text{{ or }} x > {q}"), M(f"x < {q}"), M(f"{-q} < x < {-p}")],
            f"Factor: $(x - {p})(x - {q}) < 0$. An upward parabola is NEGATIVE between its roots: ${p} < x < {q}$. Outside the roots is where it's positive.",
            [f"({(p+q)/2 if (p+q)%2==0 else Rational(p+q,2)} - {p})*({(p+q)/2 if (p+q)%2==0 else Rational(p+q,2)} - {q}) < 0".replace(".0", ""),
             f"({q + 1} - {p})*({q + 1} - {q}) > 0"],
        ))
    forms.append(form("quadratic-inequality", "Quadratic inequalities", 2,
                      "Factor, find roots, read the sign between/outside.", vs))

    # L3: parameter for exactly one root (tangency)
    vs = []
    for i, b in enumerate([6, 8, 10, 12], 1):
        m = b * b // 4
        ds = pick_ds(m, [b, 2 * b, m // 2 if m // 2 != m else m + 1])
        vs.append(variant(
            f"fun-tan-v{i}",
            f"For which $m$ does $x^2 + {b}x + m = 0$ have exactly ONE root?",
            M(m), [M(d) for d in ds],
            f"Exactly one root needs $D = 0$: ${b}^2 - 4m = 0$ ⟹ $m = \\frac{{{b * b}}}{{4}} = {m}$. Then $x^2 + {b}x + {m} = (x + {b // 2})^2$ — a perfect square kissing the axis.",
            [f"{b}**2 - 4*{m} == 0", f"expand((x + {b // 2})**2) == x**2 + {b}*x + {m}"],
        ))
    forms.append(form("tangency-parameter", "Parameter for exactly one root", 3,
                      "One root ⟺ D = 0; solve for the parameter.", vs))

    # L3: inverse function value
    vs = []
    for i, (a, b, v) in enumerate([(3, 2, 11), (2, 5, 13), (4, -3, 9), (5, 1, 16)], 1):
        inv = Fraction(v - b, a)
        assert inv.denominator == 1
        inv = int(inv)
        ds = pick_ds(inv, [a * v + b, v - b, inv + 1])
        bs = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        vs.append(variant(
            f"fun-inv-v{i}",
            f"If $f(x) = {a}x {bs}$, find $f^{{-1}}({v})$.",
            M(inv), [M(d) for d in ds],
            f"$f^{{-1}}({v})$ asks: which $x$ gives $f(x) = {v}$? Solve ${a}x {bs} = {v}$: $x = {inv}$. Check: $f({inv}) = {a * inv + b} = {v}$ ✓. (Computing $f({v})$ instead is the classic trap.)",
            [f"solve({a}*x + {b} - {v}, x) == [{inv}]", f"{a}*{inv} + {b} == {v}"],
        ))
    forms.append(form("inverse-value", "Inverse function values", 3,
                      "f⁻¹(v) = the input that outputs v — solve f(x) = v.", vs))

    return {
        "slug": "functions",
        "title": "Functions & Quadratics",
        "titleMn": "Функц",
        "blurb": "Vertices, roots, discriminants, parameters — the parabola in every disguise it wears on exams.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------
# Topic 3 — Exponents & Logarithms
# ---------------------------------------------------------------------------

def t_logarithms():
    forms = []

    # L1: evaluate a log
    vs = []
    for i, (b, k) in enumerate([(2, 5), (3, 4), (5, 3), (2, 7)], 1):
        N = b ** k
        ds = pick_ds(k, [k + 1, N // b, b])
        vs.append(variant(
            f"log-eval-v{i}",
            f"Evaluate: $\\log_{{{b}}} {N}$.",
            M(k), [M(d) for d in ds],
            f"$\\log_{{{b}}} {N}$ asks: ${b}$ to what power gives ${N}$? Since ${b}^{{{k}}} = {N}$, the answer is ${k}$.",
            [f"{b}**{k} == {N}", f"log({N}, {b}) == {k}"],
        ))
    forms.append(form("log-evaluate", "Evaluating logarithms", 1,
                      "log_b N = the exponent that turns b into N.", vs))

    # L1: exponential equation
    vs = []
    for i, (b, shift, k) in enumerate([(3, 0, 4), (2, -1, 5), (5, 1, 3), (2, 2, 6)], 1):
        N = b ** k
        sol = k - shift
        arg = "x" if shift == 0 else (f"x + {shift}" if shift > 0 else f"x - {abs(shift)}")
        ds = pick_ds(sol, [sol + 1, sol - 1, k + shift if k + shift != sol else sol + 2])
        vs.append(variant(
            f"log-expeq-v{i}",
            f"Solve: ${b}^{{{arg}}} = {N}$.",
            M(sol), [M(d) for d in ds],
            f"Write ${N}$ as a power of ${b}$: ${N} = {b}^{{{k}}}$. Equal bases ⟹ equal exponents: ${arg} = {k}$, so $x = {sol}$.",
            [f"{b}**({sol} + {shift}) == {N}"],
        ))
    forms.append(form("exp-equation", "Exponential equations", 1,
                      "Match the bases, then equate exponents.", vs))

    # L1: log addition rule
    vs = []
    for i, (b, m, k) in enumerate([(6, 2, 2), (2, 8, 4), (3, 3, 3), (10, 4, 2)], 1):
        N = b ** k // m
        assert m * N == b ** k
        ds = pick_ds(k, [k + 1, k - 1 if k - 1 != 0 else k + 2, m])
        vs.append(variant(
            f"log-add-v{i}",
            f"Evaluate: $\\log_{{{b}}} {m} + \\log_{{{b}}} {N}$.",
            M(k), [M(d) for d in ds],
            f"Same base: the logs ADD by multiplying arguments: $\\log_{{{b}}}({m} \\cdot {N}) = \\log_{{{b}}} {m * N} = {k}$, since ${b}^{{{k}}} = {m * N}$.",
            [f"{m}*{N} == {b}**{k}", f"simplify(log({m}, {b}) + log({N}, {b}) - {k}) == 0"],
        ))
    forms.append(form("log-add-rule", "Adding logarithms", 1,
                      "log M + log N = log(MN) — same base only.", vs))

    # L2: exponential equation by substitution
    vs = []
    for i, (b, r1, r2) in enumerate([(2, 0, 2), (2, 1, 3), (3, 0, 1), (2, 2, 3)], 1):
        A, B = b ** r1, b ** r2
        s, p = A + B, A * B
        ans = r1 + r2
        ds = pick_ds(ans, [s, p, ans + 1])
        vs.append(variant(
            f"log-sub-v{i}",
            f"The equation ${b}^{{2x}} - {s} \\cdot {b}^{{x}} + {p} = 0$ has two roots. Find their SUM.",
            M(ans), [M(d) for d in ds],
            f"Substitute $t = {b}^x$: $t^2 - {s}t + {p} = 0$ factors as $(t - {A})(t - {B}) = 0$. So ${b}^x = {A}$ or ${b}^x = {B}$: $x = {r1}$ or $x = {r2}$. Sum: ${ans}$.",
            [f"solve(t**2 - {s}*t + {p}, t) == sorted([{A}, {B}])", f"{b}**{r1} == {A}", f"{b}**{r2} == {B}", f"{r1} + {r2} == {ans}"],
        ))
    forms.append(form("exp-substitution", "Exponential equations via substitution", 2,
                      "b^(2x) is (b^x)² — substitute t = b^x and solve the quadratic.", vs))

    # L2: log equation
    vs = []
    for i, (b, a, c) in enumerate([(2, 3, 4), (3, 5, 3), (2, 7, 5), (5, 4, 2)], 1):
        sol = b ** c - a
        ds = pick_ds(sol, [b ** c + a, c - a if c - a != sol else sol + 1, b * c - a])
        vs.append(variant(
            f"log-eq-v{i}",
            f"Solve: $\\log_{{{b}}}(x + {a}) = {c}$.",
            M(sol), [M(d) for d in ds],
            f"Rewrite in exponential form: $x + {a} = {b}^{{{c}}} = {b ** c}$, so $x = {sol}$. Domain check: $x + {a} = {b**c} > 0$ ✓.",
            [f"{b}**{c} - {a} == {sol}", f"{sol} + {a} > 0"],
        ))
    forms.append(form("log-equation", "Logarithmic equations", 2,
                      "log_b(…) = c means (…) = b^c; check the argument stays positive.", vs))

    # L2: chain / change of base
    vs = []
    for i, (a, b2, N) in enumerate([(2, 3, 16), (3, 2, 27), (2, 5, 64), (5, 2, 25)], 1):
        ans = sp.nsimplify(sp.log(N, a))  # log_a b2 · log_b2 N collapses to log_a N
        assert ans.is_Integer
        ans = int(ans)
        ds = pick_ds(ans, [ans + 1, ans - 1 if ans - 1 > 0 else ans + 2, ans * 2])
        vs.append(variant(
            f"log-chain-v{i}",
            f"Evaluate: $\\log_{{{a}}} {b2} \\cdot \\log_{{{b2}}} {N}$.",
            M(ans), [M(d) for d in ds],
            f"The chain rule for logs: $\\log_{{{a}}} {b2} \\cdot \\log_{{{b2}}} {N} = \\log_{{{a}}} {N}$ (the ${b2}$'s cancel by change of base). And $\\log_{{{a}}} {N} = {ans}$ since ${a}^{{{ans}}} = {N}$.",
            [f"simplify(log({b2}, {a}) * log({N}, {b2}) - log({N}, {a})) == 0", f"{a}**{ans} == {N}"],
        ))
    forms.append(form("log-chain", "The log chain (change of base)", 2,
                      "log_a b · log_b c = log_a c — the middle base cancels.", vs))

    # L3: log inequality
    vs = []
    for i, (b, a, c) in enumerate([(2, 1, 3), (3, 2, 2), (2, 5, 4), (5, 3, 1)], 1):
        hi = a + b ** c
        vs.append(variant(
            f"log-ineq-v{i}",
            f"Solve: $\\log_{{{b}}}(x - {a}) < {c}$.",
            M(f"{a} < x < {hi}"),
            [M(f"x < {hi}"), M(f"x > {hi}"), M(f"{-a} < x < {hi}")],
            f"Base ${b} > 1$ keeps the direction: $x - {a} < {b}^{{{c}}} = {b ** c}$, so $x < {hi}$. But the log needs a POSITIVE argument: $x - {a} > 0$, i.e. $x > {a}$. Both together: ${a} < x < {hi}$ — forgetting the domain is the whole trap.",
            [f"{a} + {b}**{c} == {hi}", f"log({hi - a}, {b}) == {c}"],
        ))
    forms.append(form("log-inequality", "Log inequalities (domain trap)", 3,
                      "Solve the inequality AND keep the argument positive — intersect both.", vs))

    # L3: exponential inequality with base < 1
    vs = []
    for i, (den, k) in enumerate([(2, 3), (3, 2), (2, 4), (5, 2)], 1):
        vs.append(variant(
            f"log-flip-v{i}",
            f"Solve: $\\left(\\dfrac{{1}}{{{den}}}\\right)^x > \\dfrac{{1}}{{{den ** k}}}$.",
            M(f"x < {k}"),
            [M(f"x > {k}"), M(f"x < {-k}"), M(f"x > {-k}")],
            f"Write both sides with base $\\frac{{1}}{{{den}}}$: the right side is $\\left(\\frac{{1}}{{{den}}}\\right)^{{{k}}}$. A base BELOW 1 is decreasing, so comparing exponents FLIPS the sign: $x < {k}$. Test $x = 0$: $1 > \\frac{{1}}{{{den ** k}}}$ ✓.",
            [f"Rational(1, {den})**{k} == Rational(1, {den ** k})", f"Rational(1, {den})**0 > Rational(1, {den ** k})", f"Rational(1, {den})**{k + 1} < Rational(1, {den ** k})"],
        ))
    forms.append(form("exp-inequality-flip", "Exponential inequalities, base < 1", 3,
                      "A decreasing base flips the inequality when you compare exponents.", vs))

    return {
        "slug": "logarithms",
        "title": "Exponents & Logarithms",
        "titleMn": "Логарифм",
        "blurb": "From b^x = N to the domain traps of log inequalities — every exponential form the exam knows.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------
# Topic 4 — Trigonometry
# ---------------------------------------------------------------------------

def t_trigonometry():
    forms = []
    exact = {
        ("sin", 30): Rational(1, 2), ("sin", 45): sqrt(2) / 2, ("sin", 60): sqrt(3) / 2,
        ("cos", 30): sqrt(3) / 2, ("cos", 45): sqrt(2) / 2, ("cos", 60): Rational(1, 2),
        ("sin", 150): Rational(1, 2), ("cos", 120): Rational(-1, 2),
        ("sin", 120): sqrt(3) / 2, ("cos", 135): -sqrt(2) / 2,
    }

    # L1: exact values
    vs = []
    for i, (fn, deg) in enumerate([("sin", 150), ("cos", 120), ("sin", 120), ("cos", 135)], 1):
        val = exact[(fn, deg)]
        pool = [Rational(1, 2), Rational(-1, 2), sqrt(3) / 2, -sqrt(3) / 2, sqrt(2) / 2, -sqrt(2) / 2]
        ds = [M(lat(p)) for p in pick_ds_sym(val, pool)]
        ref = 180 - deg
        vs.append(variant(
            f"trig-exact-v{i}",
            f"Evaluate exactly: $\\{fn} {deg}°$.",
            M(lat(val)), ds,
            f"${deg}°$ lies in quadrant II, reference angle ${ref}°$. In QII sine is positive, cosine negative: $\\{fn} {deg}° = {lat(val)}$.",
            [f"{fn}(rad({deg})) == {sp.srepr(val) if False else str(val).replace('sqrt', 'sqrt')}".replace("str", "")
             .replace("  ", " ") if False else f"{fn}(rad({deg})) == {str(val)}"],
        ))
    forms.append(form("exact-values", "Exact values beyond 90°", 1,
                      "Reference angle + quadrant sign (ASTC).", vs))

    # L1: degree-radian conversion
    vs = []
    for i, (deg, rad_str, rad_val) in enumerate([
        (150, "\\dfrac{5\\pi}{6}", Rational(5, 6)), (120, "\\dfrac{2\\pi}{3}", Rational(2, 3)),
        (135, "\\dfrac{3\\pi}{4}", Rational(3, 4)), (240, "\\dfrac{4\\pi}{3}", Rational(4, 3))], 1):
        wrongs = [Rational(5, 6), Rational(2, 3), Rational(3, 4), Rational(4, 3), Rational(5, 4)]
        ds = [M(f"\\dfrac{{{w.p if w.p != 1 else ''}\\pi}}{{{w.q}}}".replace("{\\pi}", "{\\pi}")) for w in wrongs if w != rad_val][:3]
        vs.append(variant(
            f"trig-conv-v{i}",
            f"Convert ${deg}°$ to radians.",
            M(rad_str), ds,
            f"Multiply by $\\frac{{\\pi}}{{180}}$: ${deg}° = \\frac{{{deg}\\pi}}{{180}} = {rad_str}$.",
            [f"Rational({deg}, 180) == Rational({rad_val.p}, {rad_val.q})"],
        ))
    forms.append(form("deg-rad", "Degrees ↔ radians", 1,
                      "Multiply degrees by π/180; reduce the fraction.", vs))

    # L1: right-triangle side
    vs = []
    for i, (deg, hyp) in enumerate([(30, 10), (60, 8), (30, 14), (45, 10)], 1):
        opp = sp.nsimplify(hyp * sp.sin(sp.rad(deg)))
        ds_pool = [sp.nsimplify(hyp * sp.cos(sp.rad(deg))), Rational(hyp, 2) if Rational(hyp, 2) != opp else Rational(hyp, 4), hyp * 2]
        ds = [M(lat(d)) for d in pick_ds_sym(opp, ds_pool)]
        vs.append(variant(
            f"trig-side-v{i}",
            f"A right triangle has hypotenuse ${hyp}$ and an acute angle of ${deg}°$. Find the side OPPOSITE the ${deg}°$ angle.",
            M(lat(opp)), ds,
            f"Opposite over hypotenuse is sine: side $= {hyp}\\sin {deg}° = {lat(opp)}$. (Using cosine would give the ADJACENT side.)",
            [f"{hyp}*sin(rad({deg})) == {str(opp)}"],
        ))
    forms.append(form("right-triangle-side", "Finding a side with sine", 1,
                      "SOH: opposite = hypotenuse × sin(angle).", vs))

    # L2: from sin to cos/tan via a triple
    vs = []
    for i, (a, b, c, ask) in enumerate([(3, 4, 5, "cos"), (5, 12, 13, "tan"), (8, 15, 17, "cos"), (7, 24, 25, "tan")], 1):
        sinv = Rational(a, c)
        cosv = Rational(b, c)
        tanv = Rational(a, b)
        ans = cosv if ask == "cos" else tanv
        pool = [sinv, cosv, tanv, Rational(b, a), Rational(c, b)]
        ds = [M(lat(p)) for p in pick_ds_sym(ans, pool)]
        vs.append(variant(
            f"trig-triple-v{i}",
            f"An acute angle $\\alpha$ has $\\sin\\alpha = \\dfrac{{{a}}}{{{c}}}$. Find $\\{ask}\\alpha$.",
            M(lat(ans)), ds,
            f"Draw the right triangle: opposite ${a}$, hypotenuse ${c}$ ⟹ adjacent $= \\sqrt{{{c}^2 - {a}^2}} = {b}$ (the {a}-{b}-{c} triple). Then $\\{ask}\\alpha = {lat(ans)}$.",
            [f"sqrt({c}**2 - {a}**2) == {b}", f"Rational({a},{c})**2 + Rational({b},{c})**2 == 1"],
        ))
    forms.append(form("sin-to-cos-tan", "From sin to cos and tan", 2,
                      "Build the triangle from the triple; read the other ratios.", vs))

    # L2: solve sin x = k on [0°, 360°)
    vs = []
    for i, (k_str, k_val, s1, s2) in enumerate([
        ("\\dfrac{1}{2}", Rational(1, 2), 30, 150), ("\\dfrac{\\sqrt{3}}{2}", sqrt(3) / 2, 60, 120),
        ("\\dfrac{\\sqrt{2}}{2}", sqrt(2) / 2, 45, 135), ("-\\dfrac{1}{2}", Rational(-1, 2), 210, 330)], 1):
        vs.append(variant(
            f"trig-solve-v{i}",
            f"How many solutions does $\\sin x = {k_str}$ have on $[0°; 360°)$ — and what is their SUM?",
            M(f"2 \\text{{ solutions, sum }} {s1 + s2}°"),
            [M(f"1 \\text{{ solution, sum }} {s1}°"), M(f"2 \\text{{ solutions, sum }} {s1 + s2 + 180}°"), M(f"2 \\text{{ solutions, sum }} {abs(s1 - s2)}°")],
            f"Sine takes each value in $(-1; 1)$ twice per turn: at $x = {s1}°$ and $x = {s2}°$ (mirror pair). Sum: ${s1 + s2}°$.",
            [f"sin(rad({s1})) == {str(sp.nsimplify(k_val))}", f"sin(rad({s2})) == {str(sp.nsimplify(k_val))}", f"{s1} + {s2} == {s1 + s2}"],
        ))
    forms.append(form("solve-sin", "Solving sin x = k on one turn", 2,
                      "Two mirror solutions per turn; supplementary for positive k.", vs))

    # L2: identity simplify
    vs = []
    for i, (a, c) in enumerate([(3, 5), (5, 13), (8, 17), (20, 29)], 1):
        b = sp.sqrt(c * c - a * a)
        assert b.is_Integer
        b = int(b)
        ans = Rational(a * a, c * c)
        ds_pool = [Rational(b * b, c * c), Rational(a, c), 1]
        ds = [M(lat(d)) for d in pick_ds_sym(ans, ds_pool)]
        vs.append(variant(
            f"trig-ident-v{i}",
            f"If $\\cos\\alpha = \\dfrac{{{b}}}{{{c}}}$, evaluate $1 - \\cos^2\\alpha$.",
            M(lat(ans)), ds,
            f"Pythagorean identity: $1 - \\cos^2\\alpha = \\sin^2\\alpha$. With $\\cos\\alpha = \\frac{{{b}}}{{{c}}}$: $1 - \\frac{{{b * b}}}{{{c * c}}} = \\frac{{{a * a}}}{{{c * c}}}$.",
            [f"1 - Rational({b},{c})**2 == Rational({a * a},{c * c})"],
        ))
    forms.append(form("pythagorean-identity", "The Pythagorean identity", 2,
                      "sin² + cos² = 1, so 1 − cos² is sin².", vs))

    # L3: double angle
    vs = []
    for i, (a, b, c) in enumerate([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)], 1):
        s2 = Rational(2 * a * b, c * c)
        ds_pool = [Rational(a * b, c * c), Rational(2 * a, c), Rational(b * b - a * a, c * c)]
        ds = [M(lat(d)) for d in ds_pool if d != s2][:3]
        vs.append(variant(
            f"trig-dbl-v{i}",
            f"An acute angle has $\\sin\\alpha = \\dfrac{{{a}}}{{{c}}}$ and $\\cos\\alpha = \\dfrac{{{b}}}{{{c}}}$. Find $\\sin 2\\alpha$.",
            M(lat(s2)), ds,
            f"Double angle: $\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2 \\cdot \\frac{{{a}}}{{{c}}} \\cdot \\frac{{{b}}}{{{c}}} = {lat(s2)}$. Doubling the ANGLE never doubles the sine.",
            [f"2*Rational({a},{c})*Rational({b},{c}) == Rational({2 * a * b},{c * c})"],
        ))
    forms.append(form("double-angle", "The double-angle formula", 3,
                      "sin 2α = 2 sin α cos α — never just double.", vs))

    # L3: law of cosines
    vs = []
    for i, (a, b, deg, c) in enumerate([(5, 8, 60, 7), (3, 5, 120, 7), (7, 8, 60, sp.sqrt(57)), (5, 8, 120, sp.sqrt(129))], 1):
        cd = Rational(1, 2) if deg == 60 else Rational(-1, 2)
        c_val = sp.sqrt(a * a + b * b - 2 * a * b * cd)
        ds_pool = [sp.sqrt(a * a + b * b), sp.nsimplify(sp.sqrt(a * a + b * b + 2 * a * b * cd)), a + b - 1]
        ds = [M(lat(d)) for d in pick_ds_sym(sp.nsimplify(c_val), ds_pool)]
        vs.append(variant(
            f"trig-loc-v{i}",
            f"A triangle has sides ${a}$ and ${b}$ with a ${deg}°$ angle between them. Find the third side.",
            M(lat(sp.nsimplify(c_val))), ds,
            f"Law of cosines: $c^2 = {a}^2 + {b}^2 - 2 \\cdot {a} \\cdot {b}\\cos {deg}° = {a * a} + {b * b} - {2 * a * b} \\cdot ({lat(cd)}) = {sp.nsimplify(c_val ** 2)}$, so $c = {lat(sp.nsimplify(c_val))}$.",
            [f"sqrt({a}**2 + {b}**2 - 2*{a}*{b}*cos(rad({deg}))) == {str(sp.nsimplify(c_val))}"],
        ))
    forms.append(form("law-of-cosines", "The law of cosines", 3,
                      "c² = a² + b² − 2ab·cos C; 60° and 120° keep it exact.", vs))

    return {
        "slug": "trigonometry",
        "title": "Trigonometry",
        "titleMn": "Тригонометр",
        "blurb": "Exact values, triangles from triples, equations on the circle, and the laws — trig in every exam costume.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------
# Topic 5 — Sequences
# ---------------------------------------------------------------------------

def t_sequences():
    forms = []

    # L1: arithmetic nth term
    vs = []
    for i, (a1, d, n) in enumerate([(5, 3, 12), (7, 4, 10), (2, 6, 15), (11, -2, 20)], 1):
        an = a1 + (n - 1) * d
        ds = pick_ds(an, [a1 + n * d, a1 * n if a1 * n != an else an + d, an - d])
        vs.append(variant(
            f"seq-anth-v{i}",
            f"An arithmetic sequence has $a_1 = {a1}$ and difference $d = {d}$. Find $a_{{{n}}}$.",
            M(an), [M(v) for v in ds],
            f"$a_n = a_1 + (n-1)d$: $a_{{{n}}} = {a1} + {n - 1} \\cdot {d} = {an}$. The count of steps is $n - 1$, not $n$ — you're already standing on the first term.",
            [f"{a1} + ({n}-1)*{d} == {an}"],
        ))
    forms.append(form("arith-nth", "Arithmetic: the nth term", 1,
                      "a_n = a_1 + (n−1)d — n−1 steps from the start.", vs))

    # L1: geometric nth term
    vs = []
    for i, (b1, q, n) in enumerate([(3, 2, 6), (2, 3, 5), (5, 2, 7), (1, 4, 5)], 1):
        bn = b1 * q ** (n - 1)
        ds = pick_ds(bn, [b1 * q ** n, b1 * q * (n - 1), bn // q])
        vs.append(variant(
            f"seq-gnth-v{i}",
            f"A geometric sequence has $b_1 = {b1}$ and ratio $q = {q}$. Find $b_{{{n}}}$.",
            M(bn), [M(v) for v in ds],
            f"$b_n = b_1 q^{{n-1}}$: $b_{{{n}}} = {b1} \\cdot {q}^{{{n - 1}}} = {b1} \\cdot {q ** (n - 1)} = {bn}$.",
            [f"{b1}*{q}**({n}-1) == {bn}"],
        ))
    forms.append(form("geo-nth", "Geometric: the nth term", 1,
                      "b_n = b_1·q^(n−1) — multiply n−1 times.", vs))

    # L1: find the difference
    vs = []
    for i, (a1, k, ak) in enumerate([(4, 9, 28), (3, 7, 27), (10, 11, 40), (2, 6, 22)], 1):
        d = Fraction(ak - a1, k - 1)
        assert d.denominator == 1
        d = int(d)
        ds = pick_ds(d, [d + 1, d - 1, Fraction(ak - a1, k).numerator if Fraction(ak - a1, k).denominator == 1 else d + 2])
        vs.append(variant(
            f"seq-diff-v{i}",
            f"An arithmetic sequence has $a_1 = {a1}$ and $a_{{{k}}} = {ak}$. Find the difference $d$.",
            M(d), [M(v) for v in ds],
            f"From $a_{{{k}}} = a_1 + {k - 1}d$: ${ak} = {a1} + {k - 1}d$ ⟹ $d = \\frac{{{ak - a1}}}{{{k - 1}}} = {d}$.",
            [f"Rational({ak} - {a1}, {k} - 1) == {d}"],
        ))
    forms.append(form("arith-find-d", "Finding the common difference", 1,
                      "d = (a_k − a_1)/(k − 1) — divide by the number of steps.", vs))

    # L2: arithmetic sum
    vs = []
    for i, (a1, d, n) in enumerate([(3, 4, 10), (5, 3, 12), (2, 5, 20), (10, -2, 15)], 1):
        an = a1 + (n - 1) * d
        S = (a1 + an) * n // 2
        ds = pick_ds(S, [(a1 + an) * n, a1 * n + d * n, S + n])
        vs.append(variant(
            f"seq-asum-v{i}",
            f"Find the sum of the first ${n}$ terms: $a_1 = {a1}$, $d = {d}$.",
            M(S), [M(v) for v in ds],
            f"Last term: $a_{{{n}}} = {a1} + {n - 1} \\cdot {d} = {an}$. Sum: $S_n = \\frac{{(a_1 + a_n)n}}{{2}} = \\frac{{({a1} + {an}) \\cdot {n}}}{{2}} = {S}$ — average of the ends, times the count.",
            [f"{a1} + ({n}-1)*{d} == {an}", f"({a1} + {an})*{n}/2 == {S}"],
        ))
    forms.append(form("arith-sum", "Arithmetic series sum", 2,
                      "S_n = (a_1 + a_n)·n/2 — Gauss's pairing.", vs))

    # L2: geometric sum
    vs = []
    for i, (b1, q, n) in enumerate([(3, 2, 5), (2, 3, 4), (1, 2, 8), (5, 2, 6)], 1):
        S = b1 * (q ** n - 1) // (q - 1)
        ds = pick_ds(S, [b1 * q ** n, S - b1, S + b1])
        vs.append(variant(
            f"seq-gsum-v{i}",
            f"Find the sum of the first ${n}$ terms: $b_1 = {b1}$, $q = {q}$.",
            M(S), [M(v) for v in ds],
            f"$S_n = b_1\\frac{{q^n - 1}}{{q - 1}} = {b1} \\cdot \\frac{{{q ** n} - 1}}{{{q - 1}}} = {S}$.",
            [f"{b1}*({q}**{n} - 1)/({q} - 1) == {S}"],
        ))
    forms.append(form("geo-sum", "Geometric series sum", 2,
                      "S_n = b_1(qⁿ − 1)/(q − 1).", vs))

    # L2: which term equals a value
    vs = []
    for i, (a1, d, val) in enumerate([(7, 5, 82), (4, 3, 49), (10, 6, 100), (3, 8, 91)], 1):
        n = Fraction(val - a1, d) + 1
        assert n.denominator == 1
        n = int(n)
        ds = pick_ds(n, [n + 1, n - 1, Fraction(val, d).numerator if Fraction(val, d).denominator == 1 else n + 2])
        vs.append(variant(
            f"seq-which-v{i}",
            f"In the arithmetic sequence with $a_1 = {a1}$, $d = {d}$: which term equals ${val}$?",
            M(f"n = {n}"), [M(f"n = {v}") for v in ds],
            f"Solve ${a1} + (n - 1) \\cdot {d} = {val}$: $n - 1 = \\frac{{{val - a1}}}{{{d}}} = {n - 1}$, so $n = {n}$.",
            [f"{a1} + ({n} - 1)*{d} == {val}"],
        ))
    forms.append(form("which-term", "Which term is it?", 2,
                      "Set a_n = value, solve for n — it must land on a whole number.", vs))

    # L3: infinite geometric sum
    vs = []
    for i, (b1, qp, qq) in enumerate([(6, 1, 2), (8, 1, 3), (9, 2, 3), (12, 1, 4)], 1):
        q = Rational(qp, qq)
        S = sp.nsimplify(b1 / (1 - q))
        ds_pool = [b1 * 2, sp.nsimplify(b1 / (1 + q)), S + 1]
        ds = [M(lat(v)) for v in pick_ds_sym(S, ds_pool)]
        vs.append(variant(
            f"seq-inf-v{i}",
            f"Find the sum of the infinite geometric series with $b_1 = {b1}$ and $q = {lat(q)}$.",
            M(lat(S)), ds,
            f"$|q| < 1$, so the series converges: $S = \\dfrac{{b_1}}{{1 - q}} = \\dfrac{{{b1}}}{{1 - {lat(q)}}} = {lat(S)}$.",
            [f"{b1}/(1 - Rational({qp},{qq})) == {str(S)}"],
        ))
    forms.append(form("infinite-geo", "Infinite geometric series", 3,
                      "S = b_1/(1 − q), valid only when |q| < 1.", vs))

    # L3: geometric from two terms
    vs = []
    for i, (k1, v1, k2, v2) in enumerate([(2, 6, 5, 48), (3, 12, 6, 96), (2, 10, 4, 40), (1, 4, 4, 108)], 1):
        q_pow = k2 - k1
        q = sp.nsimplify((Fraction(v2, v1)) ** Fraction(1, q_pow))
        assert q.is_Integer
        q = int(q)
        b1 = Fraction(v1, q ** (k1 - 1))
        assert b1.denominator == 1
        b1 = int(b1)
        ds = pick_ds(b1, [b1 * q, b1 + q, q])
        vs.append(variant(
            f"seq-twoterms-v{i}",
            f"A geometric sequence has $b_{{{k1}}} = {v1}$ and $b_{{{k2}}} = {v2}$. Find $b_1$.",
            M(b1), [M(v) for v in ds],
            f"Divide the terms: $\\frac{{b_{{{k2}}}}}{{b_{{{k1}}}}} = q^{{{q_pow}}} = \\frac{{{v2}}}{{{v1}}} = {Fraction(v2, v1)}$, so $q = {q}$. Then $b_1 = \\frac{{b_{{{k1}}}}}{{q^{{{k1 - 1}}}}} = {b1}$.",
            [f"({v2}/{v1})**Rational(1,{q_pow}) == {q}", f"{b1}*{q}**({k1}-1) == {v1}", f"{b1}*{q}**({k2}-1) == {v2}"],
        ))
    forms.append(form("geo-two-terms", "Geometric sequence from two terms", 3,
                      "Divide the given terms to isolate a power of q.", vs))

    return {
        "slug": "sequences",
        "title": "Sequences & Series",
        "titleMn": "Дараалал",
        "blurb": "Arithmetic and geometric: nth terms, sums, hidden ratios, and the infinite series that converges.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------
# Topic 6 — Geometry (plane + solid, with figures)
# ---------------------------------------------------------------------------

def tri_geo(a, b, scale, la, lb, lh):
    """True-shape right triangle with legs a (horizontal), b (vertical)."""
    return {
        "points": [
            {"id": "A", "x": 0, "y": 0, "labelDx": -8, "labelDy": 8},
            {"id": "B", "x": round(a * scale, 2), "y": 0, "labelDx": 10, "labelDy": 8},
            {"id": "C", "x": round(a * scale, 2), "y": round(b * scale, 2), "labelDx": 10, "labelDy": -4},
        ],
        "objects": [
            {"kind": "segment", "from": "A", "to": "B", "label": la},
            {"kind": "segment", "from": "B", "to": "C", "label": lb, "color": "blue"},
            {"kind": "segment", "from": "A", "to": "C", "label": lh, "color": "accent"},
            {"kind": "angle", "at": "B", "from": "A", "to": "C", "right": True},
        ],
    }


def t_geometry():
    forms = []

    # L1: Pythagoras (with figure)
    vs = []
    for i, (a, b, c) in enumerate([(6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)], 1):
        scale = 6.0 / max(a, b)
        ds = pick_ds(c, [a + b, c + 1, c - 1])
        vs.append(variant(
            f"geo-pyth-v{i}",
            f"A right triangle has legs ${a}$ and ${b}$. Find the hypotenuse.",
            M(c), [M(v) for v in ds],
            f"$c = \\sqrt{{{a}^2 + {b}^2}} = \\sqrt{{{a * a} + {b * b}}} = \\sqrt{{{c * c}}} = {c}$ — the {a}-{b}-{c} triple.",
            [f"sqrt({a}**2 + {b}**2) == {c}"],
            geo=tri_geo(a, b, scale, str(a), str(b), "?"),
        ))
    forms.append(form("pythagoras", "The Pythagorean theorem", 1,
                      "c² = a² + b² — hypotenuse from the legs.", vs))

    # L1: triangle area
    vs = []
    for i, (b, h) in enumerate([(12, 5), (10, 7), (16, 9), (14, 6)], 1):
        A = b * h // 2
        ds = pick_ds(A, [b * h, b + h, A + b])
        vs.append(variant(
            f"geo-area-v{i}",
            f"A triangle has base ${b}$ and height ${h}$. Find its area.",
            M(A), [M(v) for v in ds],
            f"$A = \\frac{{1}}{{2}}bh = \\frac{{1}}{{2}} \\cdot {b} \\cdot {h} = {A}$. Forgetting the $\\frac12$ gives the surrounding rectangle instead.",
            [f"Rational(1,2)*{b}*{h} == {A}"],
        ))
    forms.append(form("triangle-area", "Triangle area", 1,
                      "A = ½ · base · height.", vs))

    # L1: circle basics
    vs = []
    for i, (r, ask) in enumerate([(6, "area"), (5, "circumference"), (9, "area"), (7, "circumference")], 1):
        if ask == "area":
            ans, wrongs = f"{r * r}\\pi", [f"{2 * r}\\pi", f"{r}\\pi", f"{4 * r * r}\\pi"]
            expl = f"$A = \\pi r^2 = \\pi \\cdot {r}^2 = {r * r}\\pi$. ($2\\pi r = {2 * r}\\pi$ is the circumference — length, not area.)"
            chk = [f"pi*{r}**2 == {r * r}*pi"]
        else:
            ans, wrongs = f"{2 * r}\\pi", [f"{r * r}\\pi", f"{r}\\pi", f"{4 * r}\\pi"]
            expl = f"$C = 2\\pi r = {2 * r}\\pi$. ($\\pi r^2 = {r * r}\\pi$ is the area.)"
            chk = [f"2*pi*{r} == {2 * r}*pi"]
        vs.append(variant(
            f"geo-circ-v{i}",
            f"A circle has radius ${r}$. Find its {ask}, exactly.",
            M(ans), [M(w) for w in wrongs], expl, chk,
        ))
    forms.append(form("circle-basics", "Circle area & circumference", 1,
                      "A = πr² (fills), C = 2πr (wraps) — don't swap them.", vs))

    # L2: special right triangles
    vs = []
    for i, (kind, given) in enumerate([("45", 8), ("30", 12), ("45", 10), ("30", 18)], 1):
        if kind == "45":
            ans = sp.nsimplify(given / sp.sqrt(2) * sp.sqrt(2) / sp.sqrt(2) * sp.sqrt(2))  # given/√2 rationalized
            ans = sp.nsimplify(given * sp.sqrt(2) / 2)
            statement = f"A 45-45-90 triangle has hypotenuse ${given}$. Find each leg."
            expl = f"Legs are hypotenuse over $\\sqrt2$: $\\frac{{{given}}}{{\\sqrt2}} = \\frac{{{given}\\sqrt2}}{{2}} = {lat(ans)}$."
            chk = [f"{given}/sqrt(2) == {str(ans)}"]
            ds_pool = [given * sp.sqrt(2), Rational(given, 2), sp.nsimplify(given * sp.sqrt(3) / 2)]
        else:
            ans = Rational(given, 2)
            statement = f"A 30-60-90 triangle has hypotenuse ${given}$. Find the SHORT leg (opposite $30°$)."
            expl = f"The short leg is HALF the hypotenuse: $\\frac{{{given}}}{{2}} = {ans}$. The $\\sqrt3$ belongs to the long leg."
            chk = [f"{given}*sin(rad(30)) == {ans}"]
            ds_pool = [sp.nsimplify(given * sp.sqrt(3) / 2), given * 2, sp.nsimplify(given * sp.sqrt(2) / 2)]
        ds = [M(lat(d)) for d in pick_ds_sym(ans, ds_pool)]
        vs.append(variant(f"geo-spec-v{i}", statement, M(lat(ans)), ds, expl, chk))
    forms.append(form("special-triangles", "Special right triangles", 2,
                      "45-45-90: x, x, x√2. 30-60-90: x, x√3, 2x.", vs))

    # L2: sector area
    vs = []
    for i, (r, deg) in enumerate([(6, 60), (9, 120), (12, 90), (6, 150)], 1):
        frac = Rational(deg, 360)
        A = sp.nsimplify(frac * sp.pi * r * r)
        coef = sp.nsimplify(A / sp.pi)
        ds_pool = [sp.pi * r * r, sp.nsimplify(frac * 2 * sp.pi * r), sp.nsimplify(A * 2)]
        ds = [M(lat(d)) for d in pick_ds_sym(A, ds_pool)]
        vs.append(variant(
            f"geo-sect-v{i}",
            f"Find the area of a ${deg}°$ sector of a circle with radius ${r}$.",
            M(lat(A)), ds,
            f"A sector is a fraction of the disk: $\\frac{{{deg}}}{{360}} \\cdot \\pi \\cdot {r}^2 = {lat(frac)} \\cdot {r * r}\\pi = {lat(A)}$.",
            [f"Rational({deg},360)*pi*{r}**2 == {str(coef)}*pi"],
        ))
    forms.append(form("sector-area", "Sector area", 2,
                      "Sector = (angle/360) × πr².", vs))

    # L2: similar triangles (with figure)
    vs = []
    for i, (a, b, a2) in enumerate([(4, 6, 10), (3, 8, 9), (5, 7, 15), (6, 10, 9)], 1):
        k = Fraction(a2, a)
        b2 = Fraction(b) * k
        assert b2.denominator == 1
        b2 = int(b2)
        ds = pick_ds(b2, [b + (a2 - a), b * a2, b2 + 1])
        vs.append(variant(
            f"geo-sim-v{i}",
            f"Two similar triangles: the first has sides ${a}$ and ${b}$; the corresponding side to ${a}$ in the second is ${a2}$. Find the side corresponding to ${b}$.",
            M(b2), [M(v) for v in ds],
            f"Scale factor $k = \\frac{{{a2}}}{{{a}}} = {lat(Rational(a2, a))}$. Corresponding sides scale together: ${b} \\cdot {lat(Rational(a2, a))} = {b2}$. (Adding ${a2 - a}$ to everything is the classic wrong move — similarity multiplies, never adds.)",
            [f"Rational({a2},{a})*{b} == {b2}"],
        ))
    forms.append(form("similar-triangles", "Similar triangles", 2,
                      "Corresponding sides share one multiplier k — never an added amount.", vs))

    # L3: solid volumes
    vs = []
    solids = [("cone", 3, 4), ("cylinder", 5, 6), ("sphere", 6, None), ("cone", 6, 8)]
    for i, (kind, r, h) in enumerate(solids, 1):
        if kind == "cone":
            V = Rational(1, 3) * r * r * h
            ans = f"{sp.nsimplify(V)}\\pi"
            expl = f"Cone: $V = \\frac13 \\pi r^2 h = \\frac13 \\pi \\cdot {r * r} \\cdot {h} = {sp.nsimplify(V)}\\pi$. The ⅓ is what separates it from the cylinder."
            chk = [f"Rational(1,3)*pi*{r}**2*{h} == {sp.nsimplify(V)}*pi"]
            ds_l = [f"{r * r * h}\\pi", f"{sp.nsimplify(V * 2)}\\pi", f"{r * h}\\pi"]
            st = f"Find the volume of a cone with radius ${r}$ and height ${h}$, exactly."
        elif kind == "cylinder":
            V = r * r * h
            ans = f"{V}\\pi"
            expl = f"Cylinder: $V = \\pi r^2 h = \\pi \\cdot {r * r} \\cdot {h} = {V}\\pi$."
            chk = [f"pi*{r}**2*{h} == {V}*pi"]
            ds_l = [f"{V // 3}\\pi" if V % 3 == 0 else f"{2 * r * h}\\pi", f"{2 * r * h}\\pi", f"{V * 2}\\pi"]
            st = f"Find the volume of a cylinder with radius ${r}$ and height ${h}$, exactly."
        else:
            V = Rational(4, 3) * r ** 3
            ans = f"{sp.nsimplify(V)}\\pi"
            expl = f"Sphere: $V = \\frac43 \\pi R^3 = \\frac43 \\pi \\cdot {r ** 3} = {sp.nsimplify(V)}\\pi$ — cube the radius, not square it."
            chk = [f"Rational(4,3)*pi*{r}**3 == {sp.nsimplify(V)}*pi"]
            ds_l = [f"{4 * r * r}\\pi", f"{sp.nsimplify(Rational(4, 3) * r ** 2)}\\pi", f"{r ** 3}\\pi"]
            st = f"Find the volume of a sphere with radius ${r}$, exactly."
        ds_l = list(dict.fromkeys([d for d in ds_l if d != ans]))
        k = 1
        while len(ds_l) < 3:
            cand = f"{sp.nsimplify(V) + k}\\pi"
            if cand != ans and cand not in ds_l:
                ds_l.append(cand)
            k += 1
        vs.append(variant(f"geo-vol-v{i}", st, M(ans), [M(d) for d in ds_l[:3]], expl, chk))
    forms.append(form("solid-volumes", "Volumes of solids", 3,
                      "Cylinder πr²h; cone adds ⅓; sphere ⁴⁄₃πR³.", vs))

    # L3: space diagonal
    vs = []
    for i, (l, w, h, d) in enumerate([(3, 4, 12, 13), (2, 3, 6, 7), (9, 12, 8, 17), (2, 6, 9, 11)], 1):
        ds = pick_ds(d, [l + w + h, d + 1, int(sp.sqrt(l * l + w * w)) if sp.sqrt(l * l + w * w).is_Integer else d - 1])
        vs.append(variant(
            f"geo-diag-v{i}",
            f"Find the space diagonal of a ${l} \\times {w} \\times {h}$ box.",
            M(d), [M(v) for v in ds],
            f"$d = \\sqrt{{l^2 + w^2 + h^2}} = \\sqrt{{{l * l} + {w * w} + {h * h}}} = \\sqrt{{{d * d}}} = {d}$ — Pythagoras across the floor, then up the wall.",
            [f"sqrt({l}**2 + {w}**2 + {h}**2) == {d}"],
        ))
    forms.append(form("space-diagonal", "The space diagonal", 3,
                      "d² = l² + w² + h² — all three dimensions enter.", vs))

    return {
        "slug": "geometry",
        "title": "Geometry",
        "titleMn": "Геометр",
        "blurb": "From Pythagoras to sectors, similarity, and 3D volumes — the figures the exam always draws.",
        "forms": forms,
    }


# ---------------------------------------------------------------------------

def main():
    topics = [t_algebra(), t_functions(), t_logarithms(), t_trigonometry(), t_sequences(), t_geometry()]
    n_forms = n_vars = 0
    for t in topics:
        n_forms += len(t["forms"])
        for f in t["forms"]:
            n_vars += len(f["variants"])
        path = os.path.join(OUT, f"{t['slug']}.json")
        with open(path, "w") as fh:
            json.dump(t, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {path}: {len(t['forms'])} forms")
    print(f"TOTAL: {len(topics)} topics, {n_forms} forms, {n_vars} variants")


if __name__ == "__main__":
    main()
