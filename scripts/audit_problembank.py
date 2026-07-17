#!/usr/bin/env python3
"""Blind re-solve audit for the problem bank.

Independently parses every problem STATEMENT (regex), recomputes the answer
with sympy, and compares against options[correctIndex]. This closes the gap
the check[] gate cannot: check strings and the labeled correct option come
from the same author, so a wrong label with a true-but-irrelevant check would
pass the gate. Here the statement itself is the source of truth.

Coverage is explicit: any variant this script cannot parse is a FAILURE, not
a skip. Run: python3 scripts/audit_problembank.py
"""
import json
import glob
import os
import re
import sys
from fractions import Fraction

import sympy as sp
from sympy import Rational, sqrt, pi, nsimplify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

problems = 0
failures = []
unparsed = []


def latex_to_expr(s):
    """Best-effort latex option string -> sympy expression."""
    t = s.strip().strip("$").strip()
    t = t.replace("\\left", "").replace("\\right", "")
    t = t.replace("\\dfrac", "\\frac").replace("°", "")
    t = re.sub(r"\\text\{[^}]*\}", "", t)
    # innermost-first: sqrt, then frac; repeat to unwind nesting
    for _ in range(8):
        t2 = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", t)
        t2 = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t2)
        if t2 == t:
            break
        t = t2
    t = t.replace("\\pi", "pi").replace("\\cdot", "*")
    t = re.sub(r"\^\{([^{}]*)\}", r"**(\1)", t)
    t = t.replace("^", "**")
    t = re.sub(r"\s+", " ", t).strip()
    # implicit multiplication: "3sqrt(2)" -> 3*sqrt(2), "4pi" -> 4*pi, ")(", ")s"
    t = re.sub(r"(\d)\s*(sqrt|pi)\b", r"\1*\2", t)
    t = re.sub(r"(\d)\s*\(", r"\1*(", t)
    t = re.sub(r"\)\s*\(", r")*(", t)
    t = re.sub(r"\)\s*(sqrt|pi)\b", r")*\1", t)
    return sp.sympify(t)


def num_eq(opt, val):
    try:
        return sp.simplify(latex_to_expr(opt) - sp.sympify(val)) == 0
    except Exception:
        return None  # unparseable option


def ints(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]


def frac_in(s):
    """First \frac{p}{q} (with optional leading -) in a latex string."""
    m = re.search(r"(-?)\\d?frac\{(-?\d+)\}\{(-?\d+)\}", s.replace("\\dfrac", "\\frac"))
    if not m:
        return None
    sign = -1 if m.group(1) == "-" else 1
    return Fraction(sign * int(m.group(2)), int(m.group(3)))


def fail(v, why, expected=None):
    failures.append((v["id"], why, str(expected), v["options"][v["correctIndex"]]))


def check_numeric(v, expected):
    r = num_eq(v["options"][v["correctIndex"]], expected)
    if r is None:
        fail(v, "correct option unparseable", expected)
    elif not r:
        fail(v, "MISMATCH", expected)


# ---------------------------------------------------------------------------
# Per-form resolvers: statement -> expected answer (numeric or structured)
# ---------------------------------------------------------------------------

def quad_coeffs(latex_lhs):
    """Parse a latex quadratic LHS like 'x^2 + 3x - 4' -> (a, b, c)."""
    t = latex_lhs.replace("\\,", "").replace(" ", "").replace("^", "**")
    t = re.sub(r"(\d)x", r"\1*x", t)
    x = sp.Symbol("x")
    poly = sp.Poly(sp.sympify(t, locals={"x": x}), x)
    cs = poly.all_coeffs()
    while len(cs) < 3:
        cs.append(0)
    return cs[0], cs[1], cs[2]


def parse_linear_terms(eq):
    """Parse 'ax + by = c' style with implicit 1 coefficients -> (a, b, c)."""
    eq = eq.replace(" ", "")
    lhs, c = eq.split("=")
    m = re.fullmatch(r"(-?\d*)x([+-]\d*)y", lhs)
    a = m.group(1)
    b = m.group(2)
    a = int(a) if a not in ("", "-") else (-1 if a == "-" else 1)
    b = int(b) if b not in ("+", "-") else (1 if b == "+" else -1)
    return a, b, int(c)


def solve_variant(topic, form_id, v):
    s = v["statement"]

    # ---------------- algebra ----------------
    if form_id == "linear-two-step":
        m = re.search(r"\$(-?\d+)x\s*([+-])\s*(\d+)\s*=\s*(-?\d+)\$", s)
        a, sign, b, c = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4))
        b = b if sign == "+" else -b
        return ("num", Fraction(c - b, a))
    if form_id == "exponent-laws":
        m = re.search(r"x\^\{(-?\d+)\}\s*\\cdot\s*x\^\{(-?\d+)\}\}\{x\^\{(-?\d+)\}", s)
        e = int(m.group(1)) + int(m.group(2)) - int(m.group(3))
        opt = v["options"][v["correctIndex"]]
        got = ints(opt)
        return ("assert", len(got) == 1 and got[0] == e)
    if form_id == "evaluate-expression":
        m = re.search(r"\$(-?\d+)a\^2\s*([+-])\s*(\d+)b\$ when \$a = (-?\d+)\$ and \$b = (-?\d+)\$", s)
        p, sign, q, A, B = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5))
        val = p * A * A + (q * B if sign == "+" else -q * B)
        return ("num", val)
    if form_id == "inequality-flip":
        m = re.search(r"\$(-?\d+)\s*-\s*(\d+)x\s*([<>])\s*(-?\d+)\$", s)
        a, b, op, c = int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4))
        bound = Fraction(a - c, b)
        direction = ">" if op == "<" else "<"  # dividing by -b flips
        opt = v["options"][v["correctIndex"]].replace("$", "").replace(" ", "")
        m2 = re.fullmatch(r"x([<>])(-?\d+)", opt)
        if not m2:
            return ("unparsed-option", opt)
        return ("assert", m2.group(1) == direction and Fraction(int(m2.group(2))) == bound)
    if form_id == "system-2x2":
        eqs = re.search(r"\\begin\{cases\}(.*?)\\\\(.*?)\\end\{cases\}", s)
        a1, b1, c1 = parse_linear_terms(eqs.group(1))
        a2, b2, c2 = parse_linear_terms(eqs.group(2))
        x, y = sp.symbols("x y")
        sol = sp.solve([a1 * x + b1 * y - c1, a2 * x + b2 * y - c2], [x, y])
        ask = re.search(r"Find \$(.*?)\$", s).group(1).replace(" ", "")
        if ask == "x+y":
            return ("num", sol[x] + sol[y])
        if ask == "x-y":
            return ("num", sol[x] - sol[y])
        if ask == "x":
            return ("num", sol[x])
        if ask == "y":
            return ("num", sol[y])
        if ask in ("x\\cdoty", "xy"):
            return ("num", sol[x] * sol[y])
        return ("unparsed", ask)
    if form_id == "rational-equation":
        m = re.search(r"\{x\s*([+-])\s*(\d+)\}\{x\s*([+-])\s*(\d+)\}\s*=\s*(-?\d+)", s)
        a = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
        b = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
        k = int(m.group(5))
        # (x+a)/(x+b)=k -> x = (a - k b)/(k - 1)
        root = Fraction(a - k * b, k - 1)
        if root == -b:
            return ("assert", False)
        return ("num", root)
    if form_id == "absolute-inequality":
        m = re.search(r"\|x\s*([+-])\s*(\d+)\|\s*\\(le|ge)\s*(\d+)", s)
        a = int(m.group(2)) * (1 if m.group(1) == "-" else -1)  # |x - a| with a signed
        op, b = m.group(3), int(m.group(4))
        lo, hi = a - b, a + b
        opt = v["options"][v["correctIndex"]].replace("$", "")
        nums = ints(opt)
        if op == "le":
            return ("assert", len(nums) == 2 and nums[0] == lo and nums[1] == hi and "or" not in opt)
        return ("assert", len(nums) == 2 and nums[0] == lo and nums[1] == hi and ("or" in opt or "cup" in opt))
    if form_id == "system-parameter":
        eqs = re.search(r"\\begin\{cases\}(.*?)\\\\(.*?)\\end\{cases\}", s)
        a1, b1, c1 = parse_linear_terms(eqs.group(1))
        e2 = eqs.group(2).replace(" ", "")
        m = re.fullmatch(r"(-?\d*)x\+my=(-?\d+)", e2)
        a2 = m.group(1)
        a2 = int(a2) if a2 not in ("", "-") else (-1 if a2 == "-" else 1)
        c2 = int(m.group(2))
        mval = Fraction(b1 * a2, a1)
        if Fraction(c2, c1) == Fraction(a2, a1):
            return ("assert", False)  # coincident, not "no solution"
        return ("num", mval)

    # ---------------- functions ----------------
    if form_id == "vertex-read":
        m = re.search(r"\(x\s*([+-])\s*(\d+)\)\^2\s*([+-])\s*(\d+)", s)
        h = int(m.group(2)) * (1 if m.group(1) == "-" else -1)
        k = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
        opt = v["options"][v["correctIndex"]]
        nums = ints(opt)
        return ("assert", len(nums) == 2 and nums[0] == h and nums[1] == k)
    if form_id == "factored-roots":
        m = re.search(r"\(x\s*([+-])\s*(\d+)\)\(x\s*([+-])\s*(\d+)\)", s)
        p = int(m.group(2)) * (-1 if m.group(1) == "+" else 1)
        q = int(m.group(4)) * (-1 if m.group(3) == "+" else 1)
        if "x_1 + x_2" in s:
            return ("num", p + q)
        if "\\cdot" in s or "x_1 x_2" in s:
            return ("num", p * q)
        return ("unparsed", s[-40:])
    if form_id == "composition":
        m = re.search(r"f\(x\) = (-?\d+)x\s*([+-])\s*(\d+)\$ and \$g\(x\) = x\^2", s)
        a = int(m.group(1))
        b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
        m2 = re.search(r"find \$(f\(g|g\(f)\((-?\d+)\)\)", s)
        t = int(m2.group(2))
        if m2.group(1) == "f(g":
            return ("num", a * t * t + b)
        return ("num", (a * t + b) ** 2)
    if form_id == "discriminant":
        m = re.search(r"\$(.+?)\s*=\s*0\$", s)
        a, b, c = quad_coeffs(m.group(1))
        D = b * b - 4 * a * c
        want = "Two distinct real roots" if D > 0 else ("Exactly one real root" if D == 0 else "No real roots")
        return ("assert", v["options"][v["correctIndex"]] == want)
    if form_id == "complete-square-min":
        m = re.search(r"y = x\^2\s*([+-])\s*(\d+)x\s*([+-])\s*(\d+)", s)
        b = int(m.group(2)) * (1 if m.group(1) == "+" else -1)
        c = int(m.group(4)) * (1 if m.group(3) == "+" else -1)
        return ("num", Fraction(4 * c - b * b, 4))
    if form_id == "quadratic-inequality":
        m = re.search(r"\$(.+?)\s*([<>])\s*0\$", s)
        A_, B, C = quad_coeffs(m.group(1))
        op = m.group(2)
        x = sp.Symbol("x")
        roots = sorted(sp.solve(A_ * x * x + B * x + C, x))
        if len(roots) != 2:
            return ("assert", False)
        p, q = roots
        opt = v["options"][v["correctIndex"]].replace("$", "")
        nums = ints(opt)
        if op == "<":
            return ("assert", len(nums) == 2 and nums[0] == p and nums[1] == q and "or" not in opt)
        return ("assert", len(nums) == 2 and nums[0] == p and nums[1] == q and "or" in opt)
    if form_id == "tangency-parameter":
        m = re.search(r"x\^2\s*([+-])\s*(\d+)x \+ m", s)
        b = int(m.group(2))
        return ("num", Fraction(b * b, 4))
    if form_id == "inverse-value":
        m = re.search(r"f\(x\) = (-?\d+)x\s*([+-])\s*(\d+)\$, find \$f\^\{-1\}\((-?\d+)\)", s)
        a = int(m.group(1))
        b = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
        vv = int(m.group(4))
        return ("num", Fraction(vv - b, a))

    # ---------------- geometry ----------------
    if form_id == "pythagoras":
        m = re.search(r"legs \$(\d+)\$ and \$(\d+)\$", s)
        a, b = int(m.group(1)), int(m.group(2))
        return ("num", sp.sqrt(a * a + b * b))
    if form_id == "triangle-area":
        m = re.search(r"base \$(\d+)\$ and height \$(\d+)\$", s)
        return ("num", Fraction(int(m.group(1)) * int(m.group(2)), 2))
    if form_id == "circle-basics":
        m = re.search(r"(radius|diameter) \$(\d+)\$", s)
        r = int(m.group(2)) if m.group(1) == "radius" else Fraction(int(m.group(2)), 2)
        if "area" in s:
            return ("num", sp.pi * r * r)
        return ("num", 2 * sp.pi * r)
    if form_id == "special-triangles":
        return solve_special_triangle(s)
    if form_id == "sector-area":
        m = re.search(r"\$(\d+)°\$ sector of a circle with radius \$(\d+)\$", s)
        ang, r = int(m.group(1)), int(m.group(2))
        return ("num", sp.Rational(ang, 360) * sp.pi * r * r)
    if form_id == "similar-triangles":
        m = re.search(r"sides \$(\d+)\$ and \$(\d+)\$.*corresponding to \$(\d+)\$ is \$(\d+)\$", s)
        a, b, a_, a2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        if a_ != a:
            return ("assert", False)
        return ("num", Fraction(b * a2, a))
    if form_id == "solid-volumes":
        if "cylinder" in s:
            m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
            return ("num", sp.pi * int(m.group(1)) ** 2 * int(m.group(2)))
        if "cone" in s:
            m = re.search(r"radius \$(\d+)\$ and height \$(\d+)\$", s)
            return ("num", sp.Rational(1, 3) * sp.pi * int(m.group(1)) ** 2 * int(m.group(2)))
        m = re.search(r"radius \$(\d+)\$", s)
        return ("num", sp.Rational(4, 3) * sp.pi * int(m.group(1)) ** 3)
    if form_id == "space-diagonal":
        m = re.search(r"\$(\d+) \\times (\d+) \\times (\d+)\$", s)
        l, w, h = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", sp.sqrt(l * l + w * w + h * h))

    # ---------------- logarithms ----------------
    if form_id == "log-evaluate":
        m = re.search(r"\\log_\{(\d+)\}\s*\{?(\d+)\}?", s)
        b, N = int(m.group(1)), int(m.group(2))
        return ("num", sp.log(N, b))
    if form_id == "exp-equation":
        m = re.search(r"\$(\d+)\^\{([^}]*)\}\s*=\s*(\d+)\$", s)
        b, expo, N = int(m.group(1)), m.group(2), int(m.group(3))
        k = sp.log(N, b)
        e = expo.replace(" ", "")
        if e == "x":
            return ("num", k)
        m2 = re.fullmatch(r"x([+-])(\d+)", e)
        if m2:
            sh = int(m2.group(2)) * (1 if m2.group(1) == "+" else -1)
            return ("num", k - sh)
        m3 = re.fullmatch(r"(\d+)x", e)
        if m3:
            return ("num", k / int(m3.group(1)))
        return ("unparsed", e)
    if form_id == "log-add-rule":
        m = re.search(r"\\log_\{(\d+)\}\s*(\d+)\s*([+-])\s*\\log_\{(\d+)\}\s*(\d+)", s)
        b, M, op, b2, N = int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4)), int(m.group(5))
        if b != b2:
            return ("assert", False)
        val = sp.log(M * N, b) if op == "+" else sp.log(sp.Rational(M, N), b)
        return ("num", sp.nsimplify(sp.simplify(val)))
    if form_id == "exp-substitution":
        m = re.search(r"\$(\d+)\^\{2x\}\s*-\s*(\d+)\s*\\cdot\s*\1\^\{?x\}?\s*\+\s*(\d+)\s*=\s*0\$", s)
        if not m:
            m = re.search(r"\$(\d+)\^\{2x\}\s*-\s*(\d+)\s*\\cdot\s*(\d+)\^\{x\}\s*\+\s*(\d+)\s*=\s*0\$", s)
            b, S, P = int(m.group(1)), int(m.group(2)), int(m.group(4))
        else:
            b, S, P = int(m.group(1)), int(m.group(2)), int(m.group(3))
        t = sp.Symbol("t")
        roots = sp.solve(t * t - S * t + P, t)
        xs = [sp.log(rt, b) for rt in roots]
        if "SUM" in s or "sum" in s:
            return ("num", sp.nsimplify(sp.simplify(xs[0] + xs[1])))
        return ("num", sp.nsimplify(sp.simplify(xs[0] * xs[1])))
    if form_id == "log-equation":
        m = re.search(r"\\log_\{(\d+)\}\(x\s*([+-])\s*(\d+)\)\s*=\s*(\d+)", s)
        b = int(m.group(1))
        a = int(m.group(3)) * (1 if m.group(2) == "+" else -1)
        c = int(m.group(4))
        return ("num", b ** c - a)
    if form_id == "log-chain":
        m = re.search(r"\\log_\{(\d+)\}\s*(\d+)\s*\\cdot\s*\\log_\{(\d+)\}\s*(\d+)", s)
        a, b, b2, N = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        if b != b2:
            return ("assert", False)
        return ("num", sp.nsimplify(sp.simplify(sp.log(N, a))))
    if form_id == "log-inequality":
        m = re.search(r"\\log_\{(\d+)\}\(x\s*([+-])\s*(\d+)\)\s*([<>])\s*(\d+)", s)
        b = int(m.group(1))
        a = int(m.group(3)) * (1 if m.group(2) == "-" else -1)  # x - a form: domain x > a
        op, c = m.group(4), int(m.group(5))
        opt = v["options"][v["correctIndex"]].replace("$", "")
        nums = ints(opt)
        if op == "<":
            lo, hi = a, a + b ** c
            return ("assert", nums == [lo, hi] and "<" in opt)
        return ("assert", nums == [a + b ** c] and ">" in opt)
    if form_id == "exp-inequality-flip":
        m = re.search(r"\{1\}\{(\d+)\}\\right\)\^x\s*([<>])\s*(.+?)\$", s)
        d, op = int(m.group(1)), m.group(2)
        rhs_raw = m.group(3).strip()
        fr = frac_in(rhs_raw)
        if fr is not None:
            rhs = fr
        else:
            rhs = Fraction(ints(rhs_raw)[0])
        k = sp.log(sp.nsimplify(rhs), sp.Rational(1, d))
        k = sp.nsimplify(sp.simplify(k))
        direction = "<" if op == ">" else ">"  # base <1 flips
        opt = v["options"][v["correctIndex"]].replace("$", "").replace(" ", "")
        m2 = re.fullmatch(r"x([<>])(-?\d+)", opt)
        if not m2:
            return ("unparsed-option", opt)
        return ("assert", m2.group(1) == direction and sp.Integer(int(m2.group(2))) == k)

    # ---------------- sequences ----------------
    if form_id == "arith-nth":
        m = re.search(r"a_1 = (-?\d+)\$ and difference \$d = (-?\d+)\$. Find \$a_\{(\d+)\}", s)
        a1, d, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", a1 + (n - 1) * d)
    if form_id == "geo-nth":
        m = re.search(r"b_1 = (-?\d+)\$ and ratio \$q = (-?\d+)\$. Find \$b_\{(\d+)\}", s)
        b1, q, n = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", b1 * q ** (n - 1))
    if form_id == "arith-find-d":
        m = re.search(r"a_1 = (-?\d+)\$ and \$a_\{(\d+)\} = (-?\d+)\$", s)
        a1, k, ak = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", Fraction(ak - a1, k - 1))
    if form_id == "arith-sum":
        m = re.search(r"first \$(\d+)\$ terms of the arithmetic sequence with \$a_1 = (-?\d+)\$, \$d = (-?\d+)\$", s)
        n, a1, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", Fraction(n * (2 * a1 + (n - 1) * d), 2))
    if form_id == "geo-sum":
        m = re.search(r"first \$(\d+)\$ terms of the geometric sequence with \$b_1 = (-?\d+)\$, \$q = (-?\d+)\$", s)
        n, b1, q = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", Fraction(b1 * (q ** n - 1), q - 1))
    if form_id == "which-term":
        m = re.search(r"a_1 = (-?\d+)\$, \$d = (-?\d+)\$: which term equals \$(-?\d+)\$", s)
        a1, d, val = int(m.group(1)), int(m.group(2)), int(m.group(3))
        n = Fraction(val - a1, d) + 1
        opt = v["options"][v["correctIndex"]]
        return ("assert", n.denominator == 1 and ints(opt) == [int(n)])
    if form_id == "infinite-geo":
        m = re.search(r"b_1 = (-?\d+)\$ and \$q = (.*?)\$", s)
        b1 = int(m.group(1))
        q = frac_in(m.group(2))
        if q is None:
            return ("unparsed", m.group(2))
        return ("num", Fraction(b1, 1) / (1 - q))
    if form_id == "geo-two-terms":
        m = re.search(r"b_\{(\d+)\} = (-?\d+)\$ and \$b_\{(\d+)\} = (-?\d+)\$. Find \$(b_1|q)\$", s)
        k1, v1, k2, v2, ask = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)
        qv = sp.nsimplify(sp.Rational(v2, v1) ** sp.Rational(1, k2 - k1))
        b1 = sp.nsimplify(v1 / qv ** (k1 - 1))
        return ("num", qv if ask == "q" else b1)

    # ---------------- trigonometry ----------------
    if form_id == "exact-values":
        m = re.search(r"\\(sin|cos|tan)\s*\{?(\d+)°", s)
        fn, deg = m.group(1), int(m.group(2))
        val = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan}[fn](sp.rad(deg))
        return ("num", sp.nsimplify(val))
    if form_id == "deg-rad":
        m = re.search(r"Convert \$(\d+)°\$", s)
        deg = int(m.group(1))
        opt = v["options"][v["correctIndex"]]
        try:
            e = latex_to_expr(opt)
        except Exception:
            return ("unparsed-option", opt)
        return ("assert", sp.simplify(e - sp.Rational(deg, 180) * sp.pi) == 0)
    if form_id == "right-triangle-side":
        m = re.search(r"hypotenuse \$(\d+)\$ and an acute angle of \$(\d+)°\$", s)
        H, A = int(m.group(1)), int(m.group(2))
        if "OPPOSITE" in s:
            return ("num", sp.nsimplify(H * sp.sin(sp.rad(A))))
        return ("num", sp.nsimplify(H * sp.cos(sp.rad(A))))
    if form_id == "sin-to-cos-tan":
        m = re.search(r"\\(sin|cos)\\alpha = \\dfrac\{(\d+)\}\{(\d+)\}\$. Find \$\\(sin|cos|tan)", s)
        gfn, p, c, ffn = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        other = sp.sqrt(c * c - p * p)
        if gfn == "sin":
            sv, cv = sp.Rational(p, c), other / c
        else:
            cv, sv = sp.Rational(p, c), other / c
        val = {"sin": sv, "cos": cv, "tan": sv / cv}[ffn]
        return ("num", sp.nsimplify(sp.simplify(val)))
    if form_id == "solve-sin":
        m = re.search(r"\\(sin|cos) x = (.+?)\$ have on", s)
        if not m:
            m = re.search(r"solutions of \$\\(sin|cos) x = (.+?)\$ on", s)
        fn, kraw = m.group(1), m.group(2)
        fr = frac_in(kraw)
        if fr is not None:
            kv = sp.nsimplify(fr)
        elif "sqrt" in kraw or "\\" in kraw:
            kv = latex_to_expr(kraw)
        else:
            kv = sp.Integer(ints(kraw)[0])
        sols = []
        for degc in range(0, 360):
            pass  # too slow symbolic per-degree; use known special sets
        # enumerate special angles
        cand = sorted(set(list(range(0, 360, 15))))
        f = sp.sin if fn == "sin" else sp.cos
        sols = [d for d in cand if sp.simplify(f(sp.rad(d)) - kv) == 0]
        count, ssum = len(sols), sum(sols)
        opt = v["options"][v["correctIndex"]]
        nums = ints(opt)
        if "solutions" in opt:
            return ("assert", nums[0] == count and nums[-1] == ssum)
        return ("assert", nums[-1] == ssum)
    if form_id == "pythagorean-identity":
        m = re.search(r"\\(sin|cos)\\alpha = \\dfrac\{(\d+)\}\{(\d+)\}\$, evaluate \$1 - \\(sin|cos)\^2", s)
        gfn, p, c, efn = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        if gfn == efn:
            return ("num", sp.Rational(c * c - p * p, c * c))
        return ("num", sp.Rational(p * p, c * c))
    if form_id == "double-angle":
        m = re.search(r"\\sin\\alpha = \\dfrac\{(\d+)\}\{(\d+)\}\$ and \$\\cos\\alpha = \\dfrac\{(\d+)\}\{(\d+)\}", s)
        a, c1, b, c2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        sv, cv = sp.Rational(a, c1), sp.Rational(b, c2)
        if "\\sin 2" in s:
            return ("num", 2 * sv * cv)
        return ("num", cv * cv - sv * sv)
    if form_id == "law-of-cosines":
        m = re.search(r"sides \$(\d+)\$ and \$(\d+)\$ with a \$(\d+)°\$ angle", s)
        p, q, ang = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return ("num", sp.sqrt(sp.nsimplify(p * p + q * q - 2 * p * q * sp.cos(sp.rad(ang)))))

    # New unit-specific forms carry their own independent re-solvers in the
    # subject modules' RESOLVERS dicts (scripts/pb/<subject>.py). They receive
    # the raw statement and return the same tagged tuples as above, plus
    # ("opt", exact-option-string) for categorical answers.
    if form_id in PLUGIN_RESOLVERS:
        return PLUGIN_RESOLVERS[form_id](s)

    return ("no-resolver", form_id)


def _load_plugin_resolvers():
    import importlib.util
    out = {}
    pb = os.path.join(ROOT, "scripts", "pb")
    for modname in ("algebra_1", "algebra_2", "geometry_course",
                    "trigonometry_course", "solid_geometry",
                    "prob_stats", "precalculus", "calculus",
                    "vectors_matrices"):
        path = os.path.join(pb, modname + ".py")
        if not os.path.exists(path):
            continue
        spec = importlib.util.spec_from_file_location("pbaud_" + modname, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for fid, fn in getattr(mod, "RESOLVERS", {}).items():
            assert fid not in out, f"duplicate plugin resolver for {fid}"
            out[fid] = fn
    return out


PLUGIN_RESOLVERS = _load_plugin_resolvers()


def solve_special_triangle(s):
    # phrasings vary; return callable result
    m45_leg = re.search(r"45-45-90 triangle has legs? \$(\d+)\$. Find the hypotenuse", s)
    if m45_leg:
        return ("num", int(m45_leg.group(1)) * sp.sqrt(2))
    m45_hyp = re.search(r"45-45-90 triangle has hypotenuse \$(\d+)\$. Find (each|the) leg", s)
    if m45_hyp:
        return ("num", sp.nsimplify(int(m45_hyp.group(1)) / sp.sqrt(2)))
    m30 = re.search(r"30-60-90 triangle has hypotenuse \$(\d+)\$. Find the (SHORT|LONG) leg", s)
    if m30:
        h = int(m30.group(1))
        return ("num", sp.Rational(h, 2) if m30.group(2) == "SHORT" else sp.nsimplify(h * sp.sqrt(3) / 2))
    m30s = re.search(r"30-60-90 triangle has short leg \$(\d+)\$. Find the (hypotenuse|LONG leg|long leg)", s)
    if m30s:
        x = int(m30s.group(1))
        return ("num", 2 * x if "hyp" in m30s.group(2).lower() else x * sp.sqrt(3))
    m30l = re.search(r"30-60-90 triangle has long leg \$(\d+)\\sqrt\{3\}\$. Find the (short leg|hypotenuse)", s)
    if m30l:
        x = int(m30l.group(1))
        return ("num", x if "short" in m30l.group(2) else 2 * x)
    m = re.search(r"the shorter leg \(opposite \$30°\$\) is \$(\d+)\$. Find the (longer leg|hypotenuse)", s)
    if m:
        x = int(m.group(1))
        return ("num", x * sp.sqrt(3) if "longer" in m.group(2) else 2 * x)
    m = re.search(r"the hypotenuse is \$(\d+)\$. Find the (shorter|longer) leg", s)
    if m:
        h = int(m.group(1))
        return ("num", sp.Rational(h, 2) if m.group(2) == "shorter" else sp.nsimplify(h * sp.sqrt(3) / 2))
    m = re.search(r"the longer leg \(opposite \$60°\$\) is \$(\d+)\\sqrt\{3\}\$. Find the (shorter leg|hypotenuse)", s)
    if m:
        x = int(m.group(1))
        return ("num", x if "shorter" in m.group(2) else 2 * x)
    m = re.search(r"45-45-90 triangle has hypotenuse \$(\d+)\\sqrt\{2\}\$. Find (each|the) leg", s)
    if m:
        return ("num", int(m.group(1)))
    return ("unparsed", s[:80])


def main():
    global problems
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "problembank", "*.json"))):
        doc = json.load(open(path))
        for fm in doc["forms"]:
            for v in fm["variants"]:
                problems += 1
                try:
                    kind, val = solve_variant(doc["slug"], fm["id"], v)
                except Exception as e:  # noqa: BLE001
                    unparsed.append((v["id"], f"resolver crashed: {e}", v["statement"][:90]))
                    continue
                if kind == "num":
                    check_numeric(v, val)
                elif kind == "assert":
                    if val is not True:
                        fail(v, "ASSERT-MISMATCH", val)
                elif kind == "opt":
                    if v["options"][v["correctIndex"]] != val:
                        fail(v, "OPT-MISMATCH", val)
                else:
                    unparsed.append((v["id"], kind, str(val)[:90]))

    print(f"blind re-solve: {problems} problems")
    print(f"  unparsed/uncovered: {len(unparsed)}")
    for u in unparsed[:25]:
        print("   ?", u)
    print(f"  MISMATCHES: {len(failures)}")
    for f in failures[:40]:
        print("   ✗", f)
    if failures or unparsed:
        sys.exit(1)
    print("  ✓ every problem independently re-solved and confirmed")


if __name__ == "__main__":
    main()
