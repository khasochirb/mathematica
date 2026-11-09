#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 8 · Linear equations: the "self-teaching" problem-bank unit.

    python3 scripts/pb/g8_linear_equations_tutor.py

REPLACES every form of unit `linear-equations` in data/problembank/8.json (and
its row in data/bank-manifest.json) and WRITES the Mongolian table
i18n/bank-tables/8/linear-equations.mn.json. Deterministic: no randomness.

Why a separate builder. This unit is the sample the whole bank is judged by:
every variant carries two hints, a step-by-step solution in a teacher's voice
(each step: the move, and why it is allowed) and, for every wrong option, a
diagnosis of the one student mistake that produces it. That needs the
solving procedure itself, not a parameter sweep, so the unit is built here
from a small linear-equation engine:

  * an equation is a list of pieces per side (term, number, bracket,
    fraction), rendered to LaTeX exactly as written (sympy would expand);
  * the engine walks it the way a teacher does: clear fractions, open
    brackets, combine like terms, collect the unknowns, move the number,
    divide, check by substitution; every equation it shows is asserted;
  * a distractor is the same walk with ONE named mistake injected (bracket
    multiplied into its first term only, sign kept when a term crosses the
    equals sign, a term left out of the multiplication, no division at the
    end, ...), so each wrong option is a real mistake's real answer.

Mongolian is written first (the reader is a Mongolian student); the English
is written to match it. Case endings on changing numbers come from
scripts/i18n/mn_numerals.py, never typed per variant.

`grade8.py` still generates the OLD forms of this unit; rerunning
scripts/build_problembank.py brings them back, so run this builder after it.
"""
import json
import os
import re
import sys
from fractions import Fraction as Fr
from math import lcm

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "i18n"))
from mn_numerals import suffix as num_suffix  # noqa: E402

UNIT = "linear-equations"
BANK = os.path.join(ROOT, "data", "problembank", "8.json")
MANIFEST = os.path.join(ROOT, "data", "bank-manifest.json")
TABLE = os.path.join(ROOT, "i18n", "bank-tables", "8", f"{UNIT}.mn.json")

UNIT_EN = {"id": UNIT, "title": "Linear Equations",
           "blurb": "Two-step equations, simplifying first, checking a solution, variables on both "
                    "sides, brackets, fractions and decimals, word problems, finding the mistake, "
                    "and how many solutions an equation has."}
UNIT_MN = {"title": "Шугаман тэгшитгэл",
           "blurb": "Хоёр алхамт тэгшитгэл, хялбарчилж бодох, шийдийг шалгах, хоёр талдаа хувьсагчтай, "
                    "хаалттай, бутархайтай тэгшитгэл, үгэн бодлого, алдаа олох, тэгшитгэл хэдэн шийдтэй болохыг тогтоох."}

# ---------------------------------------------------------------------------
# numbers and Mongolian endings
# ---------------------------------------------------------------------------


def ntex(v):
    v = Fr(v)
    if v.denominator == 1:
        n = v.numerator
        body = f"{abs(n):,}".replace(",", "\\,")
        return ("-" if n < 0 else "") + body
    return ("-" if v < 0 else "") + "\\frac{%d}{%d}" % (abs(v.numerator), v.denominator)


def terminating(v):
    d = Fr(v).denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d == 1


def dec_str(v):
    v = Fr(v)
    assert terminating(v), v
    k = 0
    while (v * 10 ** k).denominator != 1:
        k += 1
    n = abs(v.numerator * 10 ** k // v.denominator)
    s = str(n).rjust(k + 1, "0")
    s = s[:-k] + "." + s[-k:] if k else s
    return ("-" if v < 0 else "") + s


def ntexd(v, dec=False):
    """A value as LaTeX; a decimal problem shows its non-integers as decimals."""
    v = Fr(v)
    if dec and v.denominator != 1 and terminating(v):
        return dec_str(v)
    return ntex(v)


def npy(v):
    v = Fr(v)
    return f"({v.numerator})" if v.denominator == 1 else f"Rational({v.numerator},{v.denominator})"


def at(x):
    """A value as sympy source, ready to substitute: at(Fr(1, 2)) -> '(Rational(1,2))'."""
    return f"({npy(x)})"


def M(s):
    return f"${s}$"


def MX(s):
    """Maths written with '·' for \\cdot and '_' for the thin thousands space
    (Python 3.11 f-strings cannot hold a backslash inside an expression)."""
    return M(s.replace("·", "\\cdot").replace("_", "\\,"))


def W(n, case):
    """A number in maths with its hyphenated Mongolian ending: W(12, 'gen') -> '$12$-ын'."""
    n = Fr(n)
    assert n.denominator == 1, n
    return f"${ntex(n)}$-{num_suffix(int(n), case)}"


# endings after a variable or a term like $3x$ (the spoken letter decides)
VSUF = {
    "x": {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"},
    "y": {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"},
    "n": {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"},
    "m": {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"},
    "a": {"gen": "гийн", "acc": "г", "com": "тай", "abl": "гаас"},
}


def VW(tex, var, case):
    return f"${tex}$-{VSUF[var][case]}"


# ---------------------------------------------------------------------------
# expressions: pieces rendered exactly as written
# ---------------------------------------------------------------------------


class P:
    """One top-level piece of a side: 'v' c·x, 'k' number, 'br' c(inner), 'fr' ±inner/den."""

    def __init__(self, kind, c=1, inner=None, den=1, dec=False):
        self.kind, self.c, self.inner, self.den, self.dec = kind, Fr(c), inner or [], den, dec

    def copy(self, **kw):
        d = dict(kind=self.kind, c=self.c, inner=list(self.inner), den=self.den, dec=self.dec)
        d.update(kw)
        return P(**d)


def V(c=1):
    return P("v", Fr(c), dec=isinstance(c, str))


def K(c):
    return P("k", Fr(c), dec=isinstance(c, str))


def BR(c, *inner):
    return P("br", Fr(c), list(inner), dec=isinstance(c, str))


def FR(den, *inner, c=1):
    return P("fr", Fr(c), list(inner), den=den)


def cnum(a, dec):
    return dec_str(a) if (dec and Fr(a).denominator != 1) else ntex(a)


def body(p, var):
    a = abs(p.c)
    if p.kind == "v":
        return var if a == 1 else cnum(a, p.dec) + var
    if p.kind == "k":
        return cnum(a, p.dec)
    if p.kind == "br":
        return ("" if a == 1 else cnum(a, p.dec)) + "(" + etex(p.inner, var) + ")"
    assert a == 1
    return "\\frac{" + etex(p.inner, var) + "}{%d}" % p.den


def join(parts):
    """[(neg, body)] -> 'a - b + c'."""
    out = ""
    for i, (neg, b) in enumerate(parts):
        if i == 0:
            out += ("-" if neg else "") + b
        else:
            out += (" - " if neg else " + ") + b
    return out or "0"


def etex(ps, var):
    return join([(p.c < 0, body(p, var)) for p in ps])


def val(p, X):
    c = sp.Rational(p.c.numerator, p.c.denominator)
    if p.kind == "v":
        return c * X
    if p.kind == "k":
        return c
    s = sum((val(q, X) for q in p.inner), sp.Integer(0))
    return c * s if p.kind == "br" else c * s / p.den


def eval_side(ps, x):
    r = sum((val(p, sp.Rational(x.numerator, x.denominator)) for p in ps), sp.Integer(0))
    return Fr(int(r.p), int(r.q))


def ppy(p, xs):
    if p.kind == "v":
        return f"{npy(p.c)}*{xs}"
    if p.kind == "k":
        return npy(p.c)
    inner = epy(p.inner, xs)
    return f"{npy(p.c)}*({inner})" if p.kind == "br" else f"{npy(p.c)}*({inner})/{p.den}"


def epy(ps, xs):
    return " + ".join(ppy(p, xs) for p in ps) if ps else "0"


def sub_parts(ps, var, x, dec, stage):
    """Substitution of x = value, shown at stage 1 (as written) or 2 (brackets evaluated)."""
    parts = []
    xt = ntexd(x, dec)
    for i, p in enumerate(ps):
        a, neg = abs(p.c), p.c < 0
        if p.kind == "v":
            if a == 1:
                if i == 0 and not neg:
                    parts.append((False, xt))
                else:
                    parts.append((neg, f"({xt})" if x < 0 else xt))
            else:
                parts.append((neg, cnum(a, p.dec) + " \\cdot " + (f"({xt})" if x < 0 else xt)))
        elif p.kind == "k":
            parts.append((neg, cnum(a, p.dec)))
        elif p.kind == "br":
            if stage == 1:
                parts.append((neg, ("" if a == 1 else cnum(a, p.dec)) + "(" + join(sub_parts(p.inner, var, x, dec, 1)) + ")"))
            else:
                iv = eval_side(p.inner, x)
                it = ntexd(iv, dec)
                if a == 1:
                    parts.append((neg, f"({it})" if (iv < 0 and (i > 0 or neg)) else it))
                else:
                    parts.append((neg, cnum(a, p.dec) + " \\cdot " + (f"({it})" if iv < 0 else it)))
        else:
            inner = join(sub_parts(p.inner, var, x, dec, 1)) if stage == 1 else ntexd(eval_side(p.inner, x), dec)
            parts.append((neg, "\\frac{" + inner + "}{%d}" % p.den))
    return parts


def piece_checks(ps, x):
    """sympy checks for every number a substitution chain shows: each piece, each bracket."""
    out = []
    for p in ps:
        out.append(f"Eq({ppy(p, at(x))}, {npy(eval_side([p], x))})")
        if p.kind in ("br", "fr"):
            out.append(f"Eq({epy(p.inner, at(x))}, {npy(eval_side(p.inner, x))})")
    return out


def sub_chain(ps, var, x, dec=False):
    """'5 + 2(4 - 1) = 5 + 2 \\cdot 3 = 5 + 6 = 11' for one side at x."""
    s1 = join(sub_parts(ps, var, x, dec, 1))
    s2 = join(sub_parts(ps, var, x, dec, 2))
    s3 = join([(eval_side([p], x) < 0, ntexd(abs(eval_side([p], x)), dec)) for p in ps])
    total = ntexd(eval_side(ps, x), dec)
    chain = [s1]
    for s in (s2, s3 if len(ps) > 1 else None, total):
        if s and s != chain[-1]:
            chain.append(s)
    return " = ".join(chain)


class Eqn:
    def __init__(self, lhs, rhs, var="x"):
        self.lhs, self.rhs, self.var = list(lhs), list(rhs), var

    def tex(self):
        return etex(self.lhs, self.var) + " = " + etex(self.rhs, self.var)

    def is_dec(self):
        def any_dec(ps):
            return any(p.dec or any_dec(p.inner) for p in ps)
        return any_dec(self.lhs) or any_dec(self.rhs)

    def diff(self):
        X = sp.Symbol(self.var)
        d = sp.expand(sum((val(p, X) for p in self.lhs), sp.Integer(0)) - sum((val(p, X) for p in self.rhs), sp.Integer(0)))
        return sp.Rational(d.coeff(X, 1)), sp.Rational(d.coeff(X, 0))

    def solve(self):
        A, B = self.diff()
        if A != 0:
            r = -B / A
            return "one", Fr(int(r.p), int(r.q))
        return ("all", None) if B == 0 else ("none", None)

    def check_at(self, x):
        xs = f"({npy(x)})"
        return f"Eq({epy(self.lhs, xs)}, {epy(self.rhs, xs)})"

    def holds(self, x):
        return eval_side(self.lhs, x) == eval_side(self.rhs, x)


def equiv_check(a_ps, b_ps, var):
    """Symbolic: two renderings of one side are the same expression."""
    return f"Eq(expand({epy(a_ps, var)}), expand({epy(b_ps, var)}))"


# ---------------------------------------------------------------------------
# the solving engine: a teacher's walk, with an optional injected mistake
# ---------------------------------------------------------------------------


def has_frac(ps):
    return any(p.kind == "fr" or (p.kind in "vk" and p.c.denominator != 1) for p in ps)


def dec_places(ps):
    k = 0
    for p in ps:
        if p.kind in "vk" and p.dec:
            while (p.c * 10 ** k).denominator != 1:
                k += 1
    return k


def scale(p, f):
    """Piece times integer f, as a list of pieces (a fraction's numerator may splice in)."""
    if p.kind in "vk":
        return [p.copy(c=p.c * f, dec=False)]
    if p.kind == "br":
        return [p.copy(c=p.c * f, dec=False)]
    g = Fr(f, p.den) * p.c
    assert g.denominator == 1, (f, p.den)
    if len(p.inner) == 1:
        q = p.inner[0]
        return [q.copy(c=q.c * g, dec=False)]
    if g == 1:
        return [q.copy() for q in p.inner]
    return [BR(g, *p.inner)]


def is_plain(p):
    return p.kind in "vkbr" and p.c.denominator == 1 and not p.dec


def clear(eq, partial=False):
    sides = eq.lhs + eq.rhs
    if any(p.dec for p in sides if p.kind in "vk"):
        Mx = 10 ** dec_places(sides)
    else:
        dens = [p.den for p in sides if p.kind == "fr"] + [p.c.denominator for p in sides if p.kind in "vk"]
        Mx = 1
        for d in dens:
            Mx = lcm(Mx, d)
    left = []

    def side(ps):
        out = []
        for p in ps:
            if partial and is_plain(p):
                out.append(p.copy())
                left.append(p)
            else:
                out += scale(p, Mx)
        return out
    new = Eqn(side(eq.lhs), side(eq.rhs), eq.var)
    prods = []
    for p in sides:
        ap = p.copy(c=abs(p.c))
        prods.append(f"{Mx} \\cdot {body(ap, eq.var)} = {etex(scale(ap, Mx), eq.var)}")
    return Mx, new, prods, left


def expand_piece(p, mode=None):
    out = []
    for i, q in enumerate(p.inner):
        assert q.kind in "vk"
        if mode == "first_only" and i > 0:
            out.append(q.copy())                    # left unmultiplied
        elif mode == "neg_sign" and i > 0:
            c = q.c * (-p.c)
            out.append(q.copy(c=c, dec=c.denominator != 1))
        else:
            c = q.c * p.c
            out.append(q.copy(c=c, dec=(c.denominator != 1 and (p.dec or q.dec))))
    return out


def expand(eq, mode=None, only_dec=False):
    shows, target = [], None
    if mode == "first_only":
        target = next((p for p in eq.lhs + eq.rhs if p.kind == "br" and len(p.inner) > 1 and p.c != 1), None)
    if mode == "neg_sign":
        target = next((p for p in eq.lhs + eq.rhs if p.kind == "br" and len(p.inner) > 1 and p.c < 0), None)

    if mode == "first_all":
        target = next((p for p in eq.lhs + eq.rhs if p.kind == "br" and len(p.inner) > 1 and p.c != 1), None)

    def side(ps):
        out = []
        for p in ps:
            if p.kind == "br" and (not only_dec or p.dec or p.c.denominator != 1):
                if mode == "first_all":
                    m = "first_only" if len(p.inner) > 1 and p.c != 1 else None
                else:
                    m = mode if p is target else None
                e = expand_piece(p, m)
                if p.c != 1:
                    shows.append(f"{etex([p], eq.var)} = {etex(e, eq.var)}")
                out += e
            else:
                out.append(p)
        return out
    return Eqn(side(eq.lhs), side(eq.rhs), eq.var), shows, target


def needs_combine(ps):
    return sum(p.kind == "v" for p in ps) > 1 or sum(p.kind == "k" for p in ps) > 1


def combine(eq, mode=None):
    shows, dropped = [], []

    def side(ps):
        vs = [p for p in ps if p.kind == "v"]
        ks = [p for p in ps if p.kind == "k"]
        if mode == "drop" and len(vs) > 1 and not dropped:
            dropped.append(vs[-1])
            vs = vs[:-1]
        if mode == "abs" and len(vs) > 1 and any(p.c < 0 for p in vs) and not dropped:
            dropped.append(next(p for p in vs if p.c < 0))
            vs = [p.copy(c=abs(p.c)) for p in vs]
        out = []
        if vs:
            s = sum((p.c for p in vs), Fr(0))
            if len(vs) > 1:
                shows.append(f"{etex(vs, eq.var)} = {etex([V(s)], eq.var) if s != 0 else '0'}")
            if s != 0:
                out.append(V(s))
        if ks:
            s = sum((p.c for p in ks), Fr(0))
            if len(ks) > 1:
                shows.append(f"{etex(ks, eq.var)} = {ntex(s)}")
            if s != 0 or not out:
                out.append(K(s))
        return out or [K(0)]
    return Eqn(side(eq.lhs), side(eq.rhs), eq.var), shows, (dropped[0] if dropped else None)


def coeffs(ps):
    a = sum((p.c for p in ps if p.kind == "v"), Fr(0))
    b = sum((p.c for p in ps if p.kind == "k"), Fr(0))
    assert all(p.kind in "vk" for p in ps)
    return a, b


MODE_TAG = {
    "move_const_sign": "sign-not-changed-moving-term",
    "move_var_sign": "sign-not-changed-moving-term",
    "no_divide": "stopped-before-dividing",
    "mul_instead": "multiplied-instead-of-divided",
    "neg": "lost-sign-dividing-by-negative",
    "first_only": "distribute-first-term-only",
    "neg_sign": "distribute-sign-second-term",
    "partial": "multiplied-some-terms-only",
    "add_dens": "added-denominators",
    "abs": "ignored-minus-on-term",
    "drop": "dropped-like-term",
    "divide_instead": "divided-instead-of-multiplied",
    "no_multiply": "stopped-before-multiplying",
}


class Walk:
    """The worked solution of one equation: steps (MN + EN), checks, stages, mistakes."""

    def __init__(self, eq, max_steps=6, extra_steps=0, intro=None):
        self.eq0 = eq
        self.var = eq.var
        self.dec = eq.is_dec()
        kind, self.sol = eq.solve()
        assert kind == "one", (eq.tex(), kind)
        self.steps, self.checks, self.chain = [], [eq.check_at(self.sol)], []
        self.stage_eqs = []
        self.mistake_ctx = {}
        cur = eq
        pre = []
        # 1. a bracket with a decimal or fractional multiplier is opened first
        if any(p.kind == "br" and (p.dec or p.c.denominator != 1) for p in cur.lhs + cur.rhs):
            nxt, shows, _ = expand(cur, only_dec=True)
            pre.append(self._expand_step(cur, nxt, shows))
            self.mistake_ctx["expand_first"] = cur
            cur = nxt
        # 2. fractions or decimals: multiply through
        if has_frac(cur.lhs + cur.rhs) or any(p.dec for p in cur.lhs + cur.rhs if p.kind in "vk"):
            Mx, nxt, prods, _ = clear(cur)
            self.mistake_ctx["clear"] = (cur, Mx)
            pre.append(self._clear_step(cur, nxt, Mx, prods))
            cur = nxt
        # 3. brackets
        if any(p.kind == "br" for p in cur.lhs + cur.rhs):
            nxt, shows, _ = expand(cur)
            self.mistake_ctx["expand"] = cur
            pre.append(self._expand_step(cur, nxt, shows))
            cur = nxt
        # 4. like terms
        if needs_combine(cur.lhs) or needs_combine(cur.rhs):
            nxt, shows, _ = combine(cur)
            self.mistake_ctx["combine"] = cur
            pre.append(self._combine_step(cur, nxt, shows))
            cur = nxt
        self.reduced = cur
        a1, b1 = coeffs(cur.lhs)
        a2, b2 = coeffs(cur.rhs)
        self.abcd = (a1, b1, a2, b2)
        mark = (len(self.chain), len(self.stage_eqs), len(self.checks))
        tail = self._final_steps(a1, b1, a2, b2, merge=False)
        if len(pre) + len(tail) + 1 + extra_steps > max_steps:
            self.chain, self.stage_eqs, self.checks = (self.chain[:mark[0]], self.stage_eqs[:mark[1]],
                                                       self.checks[:mark[2]])
            tail = self._final_steps(a1, b1, a2, b2, merge=True)
        self.steps = pre + tail
        self.steps.append(self._check_step())
        assert self.sol == Fr(self.sol)

    # ----- step texts --------------------------------------------------
    def _note(self, e):
        self.stage_eqs.append(e)
        self.chain.append(e.tex())
        self.checks.append(e.check_at(self.sol))

    def _clear_step(self, cur, nxt, Mx, prods):
        v = self.var
        self._note(nxt)
        dens = sorted({p.den for p in cur.lhs + cur.rhs if p.kind == "fr"} |
                      {p.c.denominator for p in cur.lhs + cur.rhs if p.kind in "vk" and p.c.denominator != 1})
        # each product shown is checked symbolically
        for p in cur.lhs + cur.rhs:
            ap = p.copy(c=abs(p.c))
            self.checks.append(f"Eq(expand({Mx}*({epy([ap], v)})), expand({epy(scale(ap, Mx), v)}))")
        plist = ", ".join(M(x) for x in prods)
        if self.dec:
            k = len(str(Mx)) - 1
            mn_why = ("Хоёр талыг ижил тоогоор үржүүлэхэд тэнцэтгэл алдагдахгүй, харин бүхэл тоотой бодох илүү амар. "
                      "Бүхэл тоо байгаа гишүүнийг ч бас үржүүлэхээ мартаж болохгүй.")
            en_why = ("Multiplying both sides by the same number keeps the equation balanced, and whole numbers "
                      "are easier to work with. Terms that are already whole numbers must be multiplied too.")
            places_mn = "нэг" if k == 1 else "хоёр"
            places_en = "one decimal place" if k == 1 else "two decimal places"
            mn = (f"Аравтын бутархайн таслалаас хойш хамгийн ихдээ {places_mn} орон байна. Хоёр талын гишүүн бүрийг "
                  f"{W(Mx, 'ins')} үржүүлье: {plist}. Тэгшитгэл {M(nxt.tex())} болно.")
            en = (f"The decimals have at most {places_en}. Multiply every term on both sides by ${Mx}$: {plist}. "
                  f"The equation becomes ${nxt.tex()}$.")
        else:
            if len(dens) == 1:
                mn_den = f"Хуваарь нь {M(dens[0])} тул"
                en_den = f"The denominator is ${dens[0]}$, so"
            else:
                ds = ", ".join(M(d) for d in dens[:-1])
                mn_den = f"{ds} ба {W(dens[-1], 'gen')} хамгийн бага ерөнхий хуваарь нь {M(Mx)} тул"
                en_den = f"The least common denominator of {ds} and ${dens[-1]}$ is ${Mx}$, so"
            mn = (f"{mn_den} хоёр талын гишүүн бүрийг {W(Mx, 'ins')} үржүүлье: {plist}. "
                  f"Тэгшитгэл {M(nxt.tex())} болно.")
            en = f"{en_den} multiply every term on both sides by ${Mx}$: {plist}. The equation becomes ${nxt.tex()}$."
            mn_why = ("Хоёр талыг ижил тоогоор үржүүлэхэд тэнцэтгэл алдагдахгүй, харин бутархай алга болно. "
                      "Бутархайгүй гишүүнийг ч бас үржүүлэхээ мартаж болохгүй.")
            en_why = ("Multiplying both sides by the same number keeps the equation balanced and removes the "
                      "fractions. Terms without a fraction must be multiplied too.")
        h2 = (f"Хоёр талын гишүүн бүрийг {W(Mx, 'ins')} үржүүлбэл {M(nxt.tex())} болно.",
              f"Multiplying every term on both sides by ${Mx}$ gives ${nxt.tex()}$.")
        return dict(mn=dict(do=mn, why=mn_why), en=dict(do=en, why=en_why), h2=h2)

    def _expand_step(self, cur, nxt, shows):
        v = self.var
        self._note(nxt)
        for p in cur.lhs + cur.rhs:
            if p.kind == "br":
                self.checks.append(equiv_check([p], expand_piece(p), v))
        neg = any(p.kind == "br" and p.c < 0 for p in cur.lhs + cur.rhs)
        many = sum(p.kind == "br" for p in cur.lhs + cur.rhs) > 1
        sl = ", ".join(M(s) for s in shows)
        mn = (f"{'Хаалтуудыг' if many else 'Хаалтыг'} нээе: {sl}. Тэгшитгэл {M(nxt.tex())} болно."
              if shows else f"Хаалтыг нээе. Тэгшитгэл {M(nxt.tex())} болно.")
        en = (f"Open the bracket{'s' if many else ''}: {sl}. The equation becomes ${nxt.tex()}$."
              if shows else f"Open the bracket. The equation becomes ${nxt.tex()}$.")
        mn_why = "Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг үржүүлнэ (гишүүнчлэн үржүүлэх чанар)."
        en_why = "The number in front of a bracket multiplies every term inside it (the distributive property)."
        if neg:
            mn_why += " Хасах тэмдэгтэй тоогоор үржүүлэхэд хаалтан доторх гишүүн бүрийн тэмдэг өөрчлөгдөнө."
            en_why += " Multiplying by a negative number changes the sign of every term inside."
        h2 = (f"Хаалтыг нээвэл {M(nxt.tex())} болно.", f"Opening the bracket gives ${nxt.tex()}$.")
        return dict(mn=dict(do=mn, why=mn_why), en=dict(do=en, why=en_why), h2=h2)

    def _combine_step(self, cur, nxt, shows):
        v = self.var
        self._note(nxt)
        for side_a, side_b in ((cur.lhs, nxt.lhs), (cur.rhs, nxt.rhs)):
            self.checks.append(equiv_check(side_a, side_b, v))
        sl = ", ".join(M(s) for s in shows)
        mn = f"Тал бүрт төсөөтэй гишүүдийг нэгтгэе: {sl}. Тэгшитгэл {M(nxt.tex())} болно."
        en = f"Combine like terms on each side: {sl}. The equation becomes ${nxt.tex()}$."
        mn_why = (f"{VW(v, v, 'com')} гишүүдийг хооронд нь, тоонуудыг хооронд нь нэмж болно. "
                  f"Харин {VW(v, v, 'com')} гишүүн ба тоог нэгтгэж болохгүй.")
        en_why = f"Terms with ${v}$ add together, and so do plain numbers, but a term with ${v}$ and a number cannot be combined."
        h2 = (f"Төсөөтэй гишүүдийг нэгтгэвэл {M(nxt.tex())} болно.", f"Combining like terms gives ${nxt.tex()}$.")
        return dict(mn=dict(do=mn, why=mn_why), en=dict(do=en, why=en_why), h2=h2)

    def orientation(self, a1, a2):
        if a2 == 0:
            return "L"
        if a1 == 0:
            return "R"
        return "L" if a1 >= a2 else "R"

    def _final_steps(self, a1, b1, a2, b2, merge):
        v = self.var
        steps = []
        side = self.orientation(a1, a2)
        if side == "L":
            A, moved_v, bc, other_c = a1 - a2, a2, b1, b2
        else:
            A, moved_v, bc, other_c = a2 - a1, a1, b2, b1
        assert A != 0
        rhs_val = other_c - bc            # A·x = rhs_val (or rhs_val = A·x)
        self.A, self.side, self.rhs_val, self.bc, self.moved_v = A, side, rhs_val, bc, moved_v
        Ax = etex([V(A)], v)
        Ax_eq = Eqn([V(A)], [K(rhs_val)], v) if side == "L" else Eqn([K(rhs_val)], [V(A)], v)
        side_mn = "зүүн" if side == "L" else "баруун"
        side_en = "left" if side == "L" else "right"

        if merge and moved_v != 0 and bc != 0:
            vs = [V(a1), V(-a2)] if side == "L" else [V(a2), V(-a1)]
            ks = [K(other_c), K(-bc)]
            shown = Eqn(vs, ks, v) if side == "L" else Eqn(ks, vs, v)
            self._note(shown)
            self._note(Ax_eq)
            mn = (f"{VW(v, v, 'com')} гишүүдийг {side_mn} талд, тоонуудыг нөгөө талд цуглуулъя: "
                  f"{M(shown.tex())}, өөрөөр хэлбэл {M(Ax_eq.tex())}.")
            en = (f"Gather the ${v}$-terms on the {side_en} and the numbers on the other side: "
                  f"${shown.tex()}$, that is ${Ax_eq.tex()}$.")
            mn_why = "Нэг талаас нөгөө тал руу шилжсэн гишүүний тэмдэг эсрэгээрээ солигдоно: энэ нь хоёр талаас ижил гишүүн хассантай адил."
            en_why = "A term that crosses to the other side changes its sign: that is the same as subtracting it from both sides."
            steps.append(dict(mn=dict(do=mn, why=mn_why), en=dict(do=en, why=en_why),
                              h2=(f"{VW(v, v, 'com')} гишүүдийг нэг талд, тоонуудыг нөгөө талд цуглуулбал {M(Ax_eq.tex())} болно.",
                                  f"With the ${v}$-terms on one side and the numbers on the other you get ${Ax_eq.tex()}$.")))
        else:
            if moved_v != 0:
                t = etex([V(abs(moved_v))], v)
                if side == "L":
                    e = Eqn([V(A)] + ([K(b1)] if b1 != 0 else []), [K(b2)], v)
                else:
                    e = Eqn([K(b1)], [V(A)] + ([K(b2)] if b2 != 0 else []), v)
                self._note(e)
                if moved_v > 0:
                    mv_mn, mv_en = f"хоёр талаас {VW(t, v, 'acc')} хасвал", f"subtract ${t}$ from both sides"
                    why_mn = (f"{'Баруун' if side == 'L' else 'Зүүн'} талын {VW(v, v, 'gen')} коэффициент бага тул түүнийг хасахад "
                              f"{side_mn} талд эерэг коэффициенттэй {M(v)} үлдэнэ.")
                    why_en = (f"The {'right' if side == 'L' else 'left'} side has the smaller coefficient of ${v}$, so removing it "
                              f"leaves a positive coefficient on the {side_en}.")
                else:
                    mv_mn, mv_en = f"хоёр талд {VW(t, v, 'acc')} нэмбэл", f"add ${t}$ to both sides"
                    why_mn = f"{'Баруун' if side == 'L' else 'Зүүн'} талын $-{t}$ гишүүнийг арилгахын тулд хоёр талд {M(t)} нэмнэ. Ингэхэд {side_mn} талд эерэг коэффициенттэй {M(v)} үлдэнэ."
                    why_en = f"Adding ${t}$ to both sides removes the $-{t}$ on the {'right' if side == 'L' else 'left'} and leaves a positive number of ${v}$'s on the {side_en}."
                mn = f"{VW(v, v, 'com')} гишүүдийг {side_mn} талд цуглуулъя: {mv_mn} {M(e.tex())} болно."
                en = f"Gather the ${v}$-terms on the {side_en}: {mv_en} to get ${e.tex()}$."
                steps.append(dict(mn=dict(do=mn, why=why_mn), en=dict(do=en, why=why_en),
                                  h2=(f"{mv_mn[0].upper() + mv_mn[1:]} {M(e.tex())} болно.",
                                      f"{mv_en[0].upper() + mv_en[1:]}: ${e.tex()}$.")))
            if bc != 0:
                c = abs(bc)
                arith = (etex([K(other_c), K(-bc)], v) + " = " + ntex(rhs_val)) if other_c != 0 else ntex(rhs_val)
                if side == "L":
                    shown = f"{Ax} = {arith}"
                else:
                    shown = f"{etex([K(other_c), K(-bc)] if other_c != 0 else [K(-bc)], v)} = {Ax}"
                self._note(Ax_eq)
                if bc > 0:
                    mv_mn, mv_en = f"Хоёр талаас {W(c, 'acc')} хасъя", f"Subtract ${ntex(c)}$ from both sides"
                    why_mn, why_en = ("Хоёр талаас ижил тоо хасахад тэнцэтгэл алдагдахгүй.",
                                      "Subtracting the same number from both sides keeps the equation balanced.")
                else:
                    mv_mn, mv_en = f"Хоёр талд {W(c, 'acc')} нэмье", f"Add ${ntex(c)}$ to both sides"
                    why_mn, why_en = ("Хоёр талд ижил тоо нэмэхэд тэнцэтгэл алдагдахгүй.",
                                      "Adding the same number to both sides keeps the equation balanced.")
                self.checks.append(f"Eq({npy(other_c)} - {npy(bc)}, {npy(rhs_val)})")
                tail_mn = tail_en = ""
                if side == "R":
                    fin = f"{v} = {ntexd(self.sol, self.dec)}" if A == 1 else Ax_eq.tex()
                    tail_mn = f", өөрөөр хэлбэл {M(fin)}"
                    tail_en = f", that is ${fin}$"
                mn = f"{mv_mn}: {M(shown)}{tail_mn}."
                en = f"{mv_en}: ${shown}${tail_en}."
                hm = (f"Хоёр талаас {W(c, 'acc')} хасвал {M(Ax_eq.tex())} болно." if bc > 0 else
                      f"Хоёр талд {W(c, 'acc')} нэмбэл {M(Ax_eq.tex())} болно.")
                he = f"{mv_en}: ${Ax_eq.tex()}$."
                steps.append(dict(mn=dict(do=mn, why=why_mn), en=dict(do=en, why=why_en), h2=(hm, he)))
        if A != 1 or (side == "R" and bc == 0):
            sol_t = f"{v} = {ntexd(self.sol, self.dec)}"
            if A == 1:
                frac_t = sol_t
            else:
                raw = "\\frac{%s}{%s}" % (ntex(rhs_val), ntex(A))
                # «x = 3/2» is already final when the fraction is in lowest terms with a positive bottom
                final = (A > 0 and Fr(rhs_val).denominator == 1 and self.sol.denominator == A
                         and abs(self.sol.numerator) == abs(rhs_val) and rhs_val >= 0 and not self.dec)
                frac_t = f"{v} = {raw}" + ("" if final else f" = {ntexd(self.sol, self.dec)}")
                self.checks.append(f"Eq({npy(rhs_val)}/{npy(A)}, {npy(self.sol)})")
            self._note(Eqn([V(1)], [P("k", self.sol, dec=self.dec and terminating(self.sol))], v))
            pre_mn = pre_en = ""
            if side == "R":
                pre_mn = f"{M(Eqn([V(A)], [K(rhs_val)], v).tex())} гэж эргүүлж бичээд "
                pre_en = f"Write it as ${Eqn([V(A)], [K(rhs_val)], v).tex()}$ and "
            if A == 1:
                mn = f"Тэгшитгэлийг эргүүлж бичвэл {M(sol_t)}."
                en = f"Read it the other way round: ${sol_t}$."
                why_mn = why_en = None
            else:
                mn = f"{pre_mn}хоёр талыг {W(A, 'dat')} хуваая: {M(frac_t)}."
                en = (f"{pre_en}divide both sides by ${ntex(A)}$: ${frac_t}$." if pre_en else
                      f"Divide both sides by ${ntex(A)}$: ${frac_t}$.")
                mn = mn[0].upper() + mn[1:]
                if A < 0:
                    why_mn = f"{VW(v, v, 'gen')} коэффициент {M(ntex(A))} тул хасах тэмдэгтэй нь хамт {W(A, 'dat')} хуваана."
                    why_en = f"The coefficient of ${v}$ is ${ntex(A)}$, so divide by ${ntex(A)}$, minus sign included."
                else:
                    why_mn = f"{M(v)} нь {W(A, 'ins')} үржигдсэн байгаа тул үржүүлснийг хуваалтаар буцаана."
                    why_en = f"${v}$ is multiplied by ${ntex(A)}$, and division undoes multiplication."
            st = dict(mn=dict(do=mn), en=dict(do=en), h2=(f"{mn}", f"{en}"))
            if why_mn:
                st["mn"]["why"], st["en"]["why"] = why_mn, why_en
            steps.append(st)
        return steps

    def _check_step(self):
        v, x, eq = self.var, self.sol, self.eq0
        xt = ntexd(x, self.dec)
        L = sub_chain(eq.lhs, v, x, self.dec)
        R = sub_chain(eq.rhs, v, x, self.dec)
        self.checks += [f"Eq({epy(eq.lhs, at(x))}, {npy(eval_side(eq.lhs, x))})",
                        f"Eq({epy(eq.rhs, at(x))}, {npy(eval_side(eq.rhs, x))})"]
        self.check_L, self.check_R = L, R
        self.checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        mn = (f"Шалгая: {M(f'{v} = {xt}')} утгыг анхны тэгшитгэлд орлуулъя. Зүүн тал: {M(L)}. "
              f"Баруун тал: {M(R)}. Хоёр тал тэнцүү тул хариу зөв.")
        en = (f"Check: put ${v} = {xt}$ into the original equation. Left side: ${L}$. "
              f"Right side: ${R}$. Both sides are equal, so the answer is right.")
        return dict(mn=dict(do=mn), en=dict(do=en), h2=None)

    # ----- the mistakes ------------------------------------------------
    def rerun(self, mode):
        """Value reached with ONE injected mistake, plus the context its diagnosis needs."""
        cur, ctx = self.eq0, {}
        if mode == "add_dens":
            # x/2 + x/3 read as x/5: the denominators added like numerators
            def merge(ps):
                frs = [p for p in ps if p.kind == "fr" and p.c > 0 and len(p.inner) == 1
                       and p.inner[0].kind == "v" and p.inner[0].c == 1]
                if len(frs) != 2 or "pair" in ctx:
                    return ps
                ctx["pair"] = frs
                out = [p for p in ps if p not in frs]
                return [FR(frs[0].den + frs[1].den, V(1))] + out
            cur = Eqn(merge(cur.lhs), merge(cur.rhs), cur.var)
            if "pair" not in ctx:
                return None
            k, x = cur.solve()
            return (x, ctx, cur) if k == "one" else None
        if any(p.kind == "br" and (p.dec or p.c.denominator != 1) for p in cur.lhs + cur.rhs):
            m = mode if mode in ("first_only", "neg_sign") else None
            cur2, _, target = expand(cur, m, only_dec=True)
            if m and target is not None and (target.dec or target.c.denominator != 1):
                ctx.update(br=target, wrong=expand_piece(target, m), right=expand_piece(target))
                k, x = cur2.solve()
                return (x, ctx, cur2) if k == "one" else None
            cur = cur2
        if has_frac(cur.lhs + cur.rhs) or any(p.dec for p in cur.lhs + cur.rhs if p.kind in "vk"):
            Mx, cur2, _, left = clear(cur, partial=(mode == "partial"))
            if mode == "partial":
                if not left:
                    return None
                ctx.update(Mx=Mx, left=left)
            cur = cur2
        elif mode == "partial":
            return None
        if any(p.kind == "br" for p in cur.lhs + cur.rhs):
            m = mode if mode in ("first_only", "neg_sign") else None
            cur2, _, target = expand(cur, m)
            if m:
                if target is None:
                    return None
                ctx.update(br=target, wrong=expand_piece(target, m), right=expand_piece(target))
            cur = cur2
        elif mode in ("first_only", "neg_sign"):
            return None
        if needs_combine(cur.lhs) or needs_combine(cur.rhs):
            m = mode if mode in ("drop", "abs") else None
            cur2, _, dropped = combine(cur, m)
            if m:
                if dropped is None:
                    return None
                ctx.update(term=dropped, before=cur)
            cur = cur2
        elif mode in ("drop", "abs"):
            return None
        a1, b1 = coeffs(cur.lhs)
        a2, b2 = coeffs(cur.rhs)
        if mode in ("first_only", "neg_sign", "partial", "drop", "abs", "add_dens"):
            k, x = cur.solve()
            return (x, ctx, cur) if k == "one" else None
        A, side, rv, bc, mv = self.A, self.side, self.rhs_val, self.bc, self.moved_v
        if mode == "move_const_sign":
            if bc == 0:
                return None
            return (Fr(rv + 2 * bc) / A, ctx, None)
        if mode == "move_var_sign":
            if mv == 0 or A + 2 * mv == 0:
                return None
            return (Fr(rv) / (A + 2 * mv), ctx, None)
        if mode == "no_divide":
            return (Fr(rv), ctx, None) if A != 1 else None
        if mode == "mul_instead":
            return (Fr(rv) * A, ctx, None) if abs(A) != 1 else None
        if mode == "neg":
            return (-self.sol, ctx, None) if A < 0 else None
        raise ValueError(mode)

    def diagnose(self, mode, x, ctx):
        v, dec = self.var, self.dec
        xt = ntexd(x, dec)
        A, side, rv, bc, mv = getattr(self, "A", None), getattr(self, "side", None), \
            getattr(self, "rhs_val", None), getattr(self, "bc", None), getattr(self, "moved_v", None)
        if mode == "partial":
            Mx, left = ctx["Mx"], ctx["left"]
            bodies = [body(q.copy(c=abs(q.c)), v) for q in left]
            p = left[0]
            pt = bodies[0]
            prod = etex(scale(p.copy(c=abs(p.c)), Mx), v)
            names_mn = " ба ".join(M(b) for b in bodies)
            names_en = " and ".join(M(b) for b in bodies)
            word_mn = "гишүүдийг" if len(bodies) > 1 else "гишүүнийг"
            mn = (f"Хоёр талыг {W(Mx, 'ins')} үржүүлэхдээ {names_mn} {word_mn} үржүүлэхээ мартсан бололтой: "
                  f"тэгвэл {M(f'{v} = {xt}')} гарна. Гишүүн бүрийг үржүүлэх ёстой, жишээ нь {MX(f'{Mx} · {pt} = {prod}')}.")
            en = (f"It looks as if you multiplied by ${Mx}$ but left {names_en} as {'they were' if len(bodies) > 1 else 'it was'}, "
                  f"which leads to ${v} = {xt}$. Every term has to be multiplied, for example {MX(f'{Mx} · {pt} = {prod}')}.")
            return mn, en
        if mode == "add_dens":
            a, b = ctx["pair"]
            pair = etex([a, b], v)
            wrong = body(FR(a.den + b.den, V(1)), v)
            mn = (f"{M(pair)} гэдгийг {M(wrong)} гэж нэмсэн бол {M(f'{v} = {xt}')} гарна. Бутархайг нэмэхэд хуваарийг "
                  f"нэмдэггүй. Хоёр талыг хамгийн бага ерөнхий хуваариар үржүүлбэл бутархай алга болно.")
            en = (f"Adding ${pair}$ as ${wrong}$ gives ${v} = {xt}$, but denominators are never added. Multiply both "
                  f"sides by the least common denominator and the fractions disappear.")
            return mn, en
        if mode in ("first_only", "neg_sign"):
            br, wrong, right = ctx["br"], ctx["wrong"], ctx["right"]
            bt, wt, rt = etex([br], v), etex(wrong, v), etex(right, v)
            if mode == "first_only":
                mn = (f"{M(bt)} гэдгийг {M(wt)} гэж нээсэн бол {M(f'{v} = {xt}')} гарна. Энэ нь хаалтын өмнөх тоогоор "
                      f"зөвхөн эхний гишүүнийг үржүүлсэн алдаа. Хаалтан доторх гишүүн бүрийг үржүүлнэ: {M(f'{bt} = {rt}')}.")
                en = (f"Opening ${bt}$ as ${wt}$ gives ${v} = {xt}$: only the first term inside was multiplied. "
                      f"The number in front multiplies every term: ${bt} = {rt}$.")
            else:
                mn = (f"{M(bt)} гэдгийг {M(wt)} гэж нээсэн бол {M(f'{v} = {xt}')} гарна. Хасах тэмдэгтэй тоогоор "
                      f"үржүүлэхэд хоёр дахь гишүүний тэмдэг ч бас өөрчлөгдөнө: {M(f'{bt} = {rt}')}.")
                en = (f"Opening ${bt}$ as ${wt}$ gives ${v} = {xt}$. Multiplying by a negative number changes the sign "
                      f"of the second term too: ${bt} = {rt}$.")
            return mn, en
        if mode == "drop":
            t = etex([ctx["term"]], v)
            mn = (f"{M(t)} гишүүнийг тооцоогүй бололтой: тэгвэл {M(f'{v} = {xt}')} гарна. Нэгтгэхдээ нэг талын "
                  f"{VW(v, v, 'com')} бүх гишүүнийг оруулах ёстой.")
            en = (f"It looks as if the term ${t}$ was left out, which gives ${v} = {xt}$. When combining, every "
                  f"${v}$-term on that side has to be included.")
            return mn, en
        if mode == "abs":
            t = etex([ctx["term"].copy(c=abs(ctx["term"].c))], v)
            mn = (f"$-{t}$ гишүүний хасах тэмдгийг анзаараагүй бололтой: тэгвэл {M(f'{v} = {xt}')} гарна. Гишүүнийг "
                  f"өмнөх тэмдэгтэй нь хамт авна, иймд {VW(t, v, 'acc')} нэмэхгүй, хасна.")
            en = (f"The minus sign in front of ${t}$ seems to have been dropped, which gives ${v} = {xt}$. A term "
                  f"keeps the sign in front of it, so ${t}$ is subtracted, not added.")
            return mn, en
        Ax = etex([V(A)], v)
        if mode == "move_const_sign":
            c = abs(bc)
            base = [K(rv + bc)] if rv + bc != 0 else []
            wrong_r = etex(base + [K(bc)], v)
            right_r = etex(base + [K(-bc)], v)
            wrong = f"{Ax} = {wrong_r}" if side == "L" else f"{wrong_r} = {Ax}"
            right = f"{Ax} = {right_r}" if side == "L" else f"{right_r} = {Ax}"
            fix_mn = f"Хоёр талаас {W(c, 'acc')} хасах ёстой" if bc > 0 else f"Хоёр талд {W(c, 'acc')} нэмэх ёстой"
            fix_en = f"Subtract ${ntex(c)}$ from both sides instead" if bc > 0 else f"Add ${ntex(c)}$ to both sides instead"
            mn = (f"{W(bc, 'acc')} нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: {M(wrong)} гэж бичвэл "
                  f"ийм хариу гарна. {fix_mn}: {M(right)}.")
            en = (f"It looks as if ${ntex(bc)}$ crossed the equals sign without changing its sign: writing ${wrong}$ "
                  f"leads here. {fix_en}: ${right}$.")
            return mn, en
        if mode == "move_var_sign":
            t = etex([V(abs(mv))], v)
            wrong_l = etex([V(A + 2 * mv)], v)
            fix_mn = f"Хоёр талаас {VW(t, v, 'acc')} хасах ёстой" if mv > 0 else f"Хоёр талд {VW(t, v, 'acc')} нэмэх ёстой"
            fix_en = f"Subtract ${t}$ from both sides" if mv > 0 else f"Add ${t}$ to both sides"
            side_mn = "зүүн" if side == "L" else "баруун"
            ts = etex([V(mv)], v)
            mn = (f"{M(ts)} гишүүнийг нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: тэгвэл {side_mn} талд "
                  f"{M(wrong_l)} гарч, хариу {M(f'{v} = {xt}')} болно. {fix_mn}, тэгвэл {M(Ax)} үлдэнэ.")
            en = (f"It looks as if ${ts}$ crossed to the other side without changing its sign, giving ${wrong_l}$ and "
                  f"then ${v} = {xt}$. {fix_en}, which leaves ${Ax}$.")
            return mn, en
        if mode == "no_divide":
            eqt = f"{Ax} = {ntex(rv)}" if side == "L" else f"{ntex(rv)} = {Ax}"
            mn = (f"{M(eqt)} хүртэл зөв бодсон байна. Гэхдээ {M(ntex(rv))} бол {M(v)} биш, {VW(Ax, v, 'gen')} утга. "
                  f"Сүүлд нь хоёр талыг {W(A, 'dat')} хуваах ёстой.")
            en = (f"Everything up to ${eqt}$ is right. But ${ntex(rv)}$ is the value of ${Ax}$, not of ${v}$: "
                  f"the last step is to divide both sides by ${ntex(A)}$.")
            return mn, en
        if mode == "mul_instead":
            mn = (f"Сүүлийн алхамд {W(A, 'dat')} хуваахын оронд {W(A, 'ins')} үржүүлсэн байна. {M(v)} нь "
                  f"{W(A, 'ins')} үржигдсэн тул буцаахдаа хуваана.")
            en = (f"In the last step ${ntex(A)}$ multiplied instead of dividing. ${v}$ is multiplied by ${ntex(A)}$, "
                  f"so undoing it means dividing.")
            return mn, en
        if mode == "neg":
            mn = (f"Хоёр талыг {W(abs(A), 'dat')} хуваасан бол хасах тэмдэг алга болно. {VW(v, v, 'gen')} коэффициент "
                  f"{M(ntex(A))} тул {W(A, 'dat')} хуваах ёстой.")
            en = (f"Dividing by ${ntex(abs(A))}$ loses the minus sign. The coefficient of ${v}$ is ${ntex(A)}$, "
                  f"so divide by ${ntex(A)}$.")
            return mn, en
        raise ValueError(mode)

    def mistakes(self, order):
        out = []
        for mode in order:
            r = self.rerun(mode)
            if r is None:
                continue
            x, ctx, wrong_eq = r
            mn, en = self.diagnose(mode, x, ctx)
            chk = [f"Ne({epy(self.eq0.lhs, at(x))}, {epy(self.eq0.rhs, at(x))})"]
            if wrong_eq is not None:
                chk.append(wrong_eq.check_at(x))
            out.append(dict(x=x, mn=mn, en=en, mode=mode, checks=chk, tag=MODE_TAG[mode]))
        return out


# ---------------------------------------------------------------------------
# variant assembly
# ---------------------------------------------------------------------------

def hint2_from(step, var):
    mn, en = step["h2"]
    return (f"{mn} Одоо {VW(var, var, 'acc')} олоорой.", f"{en} Now find ${var}$.")


def pick3(answer, cands, dec=False):
    """First three candidate mistakes whose answers differ from the answer and each other."""
    seen = {ntexd(answer, dec)}
    out = []
    for c in cands:
        t = ntexd(c["x"], dec)
        if t in seen:
            continue
        seen.add(t)
        out.append(c)
        if len(out) == 3:
            break
    assert len(out) == 3, (answer, [c["mode"] for c in cands])
    return out


def assemble(vid, i, st_mn, st_en, correct, wrongs, steps, hints, expl, checks, fixed_ci=None):
    """correct = (mn_opt, en_opt); wrongs = [(mn_opt, en_opt, mn_why, en_why)]."""
    if fixed_ci is None:
        ci = i % 4
        opts = list(wrongs)
        opts.insert(ci, None)
    else:
        ci, opts = fixed_ci, wrongs
    om, oe, wm, we, mc = [], [], [], [], []
    for o in opts:
        if o is None:
            om.append(correct[0]); oe.append(correct[1]); wm.append(None); we.append(None); mc.append(None)
        else:
            assert len(o) == 5 and re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", o[4]), (vid, o)
            om.append(o[0]); oe.append(o[1]); wm.append(o[2]); we.append(o[3]); mc.append(o[4])
    assert len(om) == 4 and len(set(om)) == 4 and len(set(oe)) == 4, om
    assert 3 <= len(steps) <= 6, (vid, len(steps))
    assert len(hints) == 2
    en = dict(id=vid, statement=st_en, options=oe, correctIndex=ci, explanation=expl[1],
              check=sorted(set(checks), key=checks.index),
              hints=[h[1] for h in hints], steps=[s["en"] for s in steps], whyWrong=we, misconceptions=mc)
    mn = dict(statement=st_mn, options=om, explanation=expl[0],
              hints=[h[0] for h in hints], steps=[s["mn"] for s in steps], whyWrong=wm)
    return en, mn


def walk_explanation(w):
    v = w.var
    eq0 = w.eq0.tex()
    sol = f"{v} = {ntexd(w.sol, w.dec)}"
    mirror = f"{ntexd(w.sol, w.dec)} = {v}"
    chain = []
    for c in w.chain:
        if c != mirror and (not chain or chain[-1] != c):
            chain.append(c)
    if chain[-1:] != [sol]:
        chain.append(sol)
    mid = ", ".join(M(c) for c in chain)
    Lv = ntexd(eval_side(w.eq0.lhs, w.sol), w.dec)
    mn = (f"{M(eq0)} тэгшитгэлийг алхам алхмаар хялбарчилбал {mid} гарна. "
          f"Орлуулж шалгахад хоёр тал {M(Lv)} болж тэнцүү.")
    en = f"Simplifying ${eq0}$ step by step gives {mid}. Substituting back, both sides equal ${Lv}$."
    return mn, en


def numeric_variant(vid, i, eq, st_mn, st_en, order, hint1, extra_first=None, max_steps=6):
    w = Walk(eq, max_steps=max_steps, extra_steps=1 if extra_first else 0)
    ms = pick3(w.sol, w.mistakes(order), w.dec)
    steps = ([extra_first] if extra_first else []) + w.steps
    first = w.steps[0]
    hints = [hint1, hint2_from(first, eq.var)]
    wrongs = [(M(ntexd(m["x"], w.dec)),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    checks = list(w.checks)
    for m in ms:
        checks += m["checks"]
    ans = M(ntexd(w.sol, w.dec))
    return assemble(vid, i, st_mn, st_en, (ans, ans), wrongs, steps, hints, walk_explanation(w), checks)


def solve_stmt(eq):
    return (f"{M(eq.tex())} тэгшитгэлийг бодоорой.", f"Solve ${eq.tex()}$.")


def two_step_division(vid, i, eq):
    """x/d + b = c, solved the way it is taught: remove b, then multiply by d."""
    v = eq.var
    fr = eq.lhs[0]
    d, b, c = fr.den, eq.lhs[1].c, eq.rhs[0].c
    r = c - b
    sol = r * d
    assert eq.solve() == ("one", sol)
    xd = body(fr, v)
    e1 = Eqn([fr], [K(r)], v)
    e2 = Eqn([V(1)], [K(sol)], v)
    arith = etex([K(c), K(-b)], v) + " = " + ntex(r)
    if b > 0:
        s1_mn = f"Зүүн талд {M(xd)} дээр {M(ntex(b))} нэмэгдсэн байна. Хоёр талаас {W(b, 'acc')} хасъя: {M(f'{xd} = {arith}')}."
        s1_en = f"On the left, ${ntex(b)}$ is added to ${xd}$. Subtract ${ntex(b)}$ from both sides: ${xd} = {arith}$."
        h2_mn, h2_en = f"Хоёр талаас {W(b, 'acc')} хасвал {M(e1.tex())} болно.", f"Subtract ${ntex(b)}$ from both sides: ${e1.tex()}$."
    else:
        s1_mn = f"Зүүн талд {M(xd)}-ээс {M(ntex(-b))} хасагдсан байна. Хоёр талд {W(-b, 'acc')} нэмье: {M(f'{xd} = {arith}')}."
        s1_en = f"On the left, ${ntex(-b)}$ is subtracted from ${xd}$. Add ${ntex(-b)}$ to both sides: ${xd} = {arith}$."
        h2_mn, h2_en = f"Хоёр талд {W(-b, 'acc')} нэмбэл {M(e1.tex())} болно.", f"Add ${ntex(-b)}$ to both sides: ${e1.tex()}$."
    s1_why_mn = (f"{M(xd)} илэрхийлэлд {VW(v, v, 'acc')} эхлээд {W(d, 'dat')} хувааж, дараа нь тоо нэмсэн. Буцаахдаа эсрэг "
                 f"дарааллаар явна: эхлээд тоог арилгана.")
    s1_why_en = f"${xd}$ is built by dividing ${v}$ by ${d}$ first and then adding a number. Undo in reverse order: the number goes first."
    prod = f"{v} = {ntex(r)} \\cdot {d} = {ntex(sol)}" if r >= 0 else f"{v} = ({ntex(r)}) \\cdot {d} = {ntex(sol)}"
    s2_mn = f"{M(v)} нь {W(d, 'dat')} хуваагдсан байна. Хоёр талыг {W(d, 'ins')} үржүүлье: {M(prod)}."
    s2_en = f"${v}$ is divided by ${d}$. Multiply both sides by ${d}$: ${prod}$."
    s2_why_mn, s2_why_en = "Хуваасныг үржүүлэлтээр буцаана.", "Multiplication undoes division."
    Lc = sub_chain(eq.lhs, v, sol)
    s3_mn = (f"Шалгая: {M(f'{v} = {ntex(sol)}')} утгыг анхны тэгшитгэлд орлуулъя. Зүүн тал: {M(Lc)}. "
             f"Баруун тал: {M(ntex(c))}. Хоёр тал тэнцүү тул хариу зөв.")
    s3_en = (f"Check: put ${v} = {ntex(sol)}$ into the original equation. Left side: ${Lc}$. "
             f"Right side: ${ntex(c)}$. Both sides are equal, so the answer is right.")
    steps = [dict(mn=dict(do=s1_mn, why=s1_why_mn), en=dict(do=s1_en, why=s1_why_en)),
             dict(mn=dict(do=s2_mn, why=s2_why_mn), en=dict(do=s2_en, why=s2_why_en)),
             dict(mn=dict(do=s3_mn), en=dict(do=s3_en))]
    hints = [(f"{M(xd)} дээр нэмэгдсэн буюу хасагдсан тоог эхлээд арилгаарай. Дараа нь хуваалтыг юугаар буцаах вэ?",
              f"First remove the number added to or subtracted from ${xd}$. Then what undoes a division?"),
             (h2_mn + f" Одоо {VW(v, v, 'acc')} олоорой.", h2_en + f" Now find ${v}$.")]
    cands = []
    # the number crosses without changing sign
    x1 = (c + b) * d
    wrong = etex([K(c), K(b)], v)
    fix_mn = f"Хоёр талаас {W(b, 'acc')} хасах ёстой" if b > 0 else f"Хоёр талд {W(-b, 'acc')} нэмэх ёстой"
    fix_en = f"Subtract ${ntex(b)}$ from both sides" if b > 0 else f"Add ${ntex(-b)}$ to both sides"
    cands.append(dict(x=x1, mode="move_const_sign", tag="sign-not-changed-moving-term",
                      mn=(f"{W(b, 'acc')} нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: "
                          f"{M(f'{xd} = {wrong}')} гэж бичвэл ийм хариу гарна. {fix_mn}: {M(f'{xd} = {arith}')}."),
                      en=(f"It looks as if ${ntex(b)}$ crossed the equals sign without changing sign, giving "
                          f"${xd} = {wrong}$. {fix_en}: ${xd} = {arith}$.")))
    x2 = Fr(r, d)
    cands.append(dict(x=x2, mode="divide_instead", tag="divided-instead-of-multiplied",
                      mn=(f"{M(e1.tex())} гарсны дараа хоёр талыг {W(d, 'dat')} хуваасан байна. {M(v)} нь "
                          f"{W(d, 'dat')} хуваагдсан тул буцаахдаа {W(d, 'ins')} үржүүлнэ."),
                      en=(f"After ${e1.tex()}$ both sides were divided by ${d}$. Since ${v}$ is divided by ${d}$, "
                          f"undo it by multiplying by ${d}$.")))
    cands.append(dict(x=r, mode="no_multiply", tag="stopped-before-multiplying",
                      mn=(f"{M(e1.tex())} хүртэл зөв бодсон байна. Гэхдээ {M(ntex(r))} бол {M(v)} биш, {M(xd)}-ийн утга. "
                          f"Сүүлд нь хоёр талыг {W(d, 'ins')} үржүүлэх ёстой."),
                      en=(f"Everything up to ${e1.tex()}$ is right. But ${ntex(r)}$ is the value of ${xd}$, not of ${v}$: "
                          f"multiply both sides by ${d}$ to finish.")))
    ms = pick3(sol, cands)
    checks = piece_checks(eq.lhs, sol) + [eq.check_at(sol), e1.check_at(sol), e2.check_at(sol), f"Eq({npy(c)} - {npy(b)}, {npy(r)})",
              f"Eq({npy(r)}*{d}, {npy(sol)})", f"Eq({epy(eq.lhs, at(sol))}, {npy(c)})"]
    for m in ms:
        checks.append(f"Ne({epy(eq.lhs, at(m['x']))}, {npy(c)})")
    expl = (f"Хоёр талаас тоог арилгавал {M(e1.tex())}, дараа нь {W(d, 'ins')} үржүүлбэл {M(e2.tex())} гарна. "
            f"Орлуулж шалгахад зүүн тал {M(ntex(c))} болж баруун талтай тэнцүү.",
            f"Removing the number from both sides gives ${e1.tex()}$, and multiplying by ${d}$ gives ${e2.tex()}$. "
            f"Substituting back, the left side equals ${ntex(c)}$, as it should.")
    wrongs = [(M(ntex(m["x"])),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    st_mn, st_en = solve_stmt(eq)
    return assemble(vid, i, st_mn, st_en, (M(ntex(sol)),) * 2, wrongs, steps, hints, expl, checks)


VERDICT = {
    "yes": ("Тийм, шийд мөн", "Yes, it is a solution"),
    "gt": ("Үгүй, зүүн тал нь баруун талаасаа их гарна", "No, the left side comes out larger"),
    "lt": ("Үгүй, зүүн тал нь баруун талаасаа бага гарна", "No, the left side comes out smaller"),
    "solve": ("Тэгшитгэлийг эхлээд бодохгүйгээр мэдэх боломжгүй", "You cannot tell without solving the equation first"),
}


def verdict(L, R):
    return "yes" if L == R else ("gt" if L > R else "lt")


def find_substitution_cases():
    """Equations p + c(x + q) = a·x + b (bracket on one side) where the two named
    substitution mistakes (adding before multiplying, multiplying the first number
    only) land exactly on the two verdicts that are not the answer. Deterministic
    search, first hit per (target verdict, which side holds the bracket)."""
    plan = [("yes", "L"), ("gt", "R"), ("lt", "L"), ("yes", "R"), ("gt", "L"), ("lt", "R")]
    used, out = set(), []
    for target, side in plan:
        found = None
        for k in (4, 3, 5, 2, 6, -2, -1, 7):
            for p in range(2, 10):
                for c in (2, 3, 4, 5):
                    for q in (3, 1, 2, 4, 5, -1, -2, -3):
                        for a in (3, 2, 4, 5, 6):
                            if (k, p, c, q) in used or k + q == 0 or p == c:
                                continue
                            Lb = p + c * (k + q)
                            orderm = (p + c) * (k + q)
                            first = p + c * k + q
                            for d in (0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 9, -9, 11, -11):
                                b = Lb - a * k + d
                                if b == 0:
                                    continue
                                Ro = a * k + b
                                # verdicts seen from the LEFT side of the printed equation
                                if side == "L":
                                    vt, vo, vf = verdict(Lb, Ro), verdict(orderm, Ro), verdict(first, Ro)
                                else:
                                    vt, vo, vf = verdict(Ro, Lb), verdict(Ro, orderm), verdict(Ro, first)
                                if vt != target:
                                    continue
                                need = {"yes", "gt", "lt"} - {target}
                                if {vo, vf} == need:
                                    found = (k, p, c, q, a, b, vo, vf)
                                    break
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        assert found, (target, side)
        used.add(found[:4])
        out.append((target, side) + found)
    return out


def subst_variant_a(vid, i, var, case):
    target, side, k, p, c, q, a, b, vo, vf = case
    brs = [K(p), BR(c, V(1), K(q))]
    lin = [V(a), K(b)]
    eq = Eqn(brs, lin, var) if side == "L" else Eqn(lin, brs, var)
    x = Fr(k)
    L, R = eval_side(eq.lhs, x), eval_side(eq.rhs, x)
    assert verdict(L, R) == target
    xt = f"{var} = {ntex(x)}"
    Lc, Rc = sub_chain(eq.lhs, var, x), sub_chain(eq.rhs, var, x)
    st_mn = f"{M(xt)} нь {M(eq.tex())} тэгшитгэлийн шийд мөн үү?"
    st_en = f"Is ${xt}$ a solution of ${eq.tex()}$?"
    bside_mn = "Зүүн" if side == "L" else "Баруун"
    bside_en = "left" if side == "L" else "right"
    sub_b = join(sub_parts(brs, var, x, False, 1))
    right_b = sub_chain(brs, var, x)
    bval = eval_side(brs, x)
    lval = eval_side(lin, x)
    om = (p + c) * (k + q)
    fo = p + c * k + q

    def says(vd):
        return {"yes": ("хоёр тал тэнцүү мэт харагдана", "the two sides look equal"),
                "gt": ("зүүн тал баруун талаасаа их мэт харагдана", "the left side looks larger"),
                "lt": ("зүүн тал баруун талаасаа бага мэт харагдана", "the left side looks smaller")}[vd]
    kq = ntex(k + q) if k + q >= 0 else f"({ntex(k + q)})"
    kt = ntex(k) if k >= 0 else f"({ntex(k)})"
    cb = f"{c}({join(sub_parts([V(1), K(q)], var, x, False, 1))})"      # «2(4 + 3)»
    om_t = MX(f"({p} + {c}) · {kq}")
    fo_t = MX(f"{c} · {kt} {'+' if q > 0 else '-'} {abs(q)}")
    diag = {
        vo: ((f"{M(sub_b)} гэдгийг {om_t} гэж бодвол {M(ntex(om))} гарч, {says(vo)[0]}. Энэ нь {M(p)} ба {M(c)} хоёрыг "
              f"түрүүлж нэмсэн алдаа. Үржих үйлдлийг нэмэхээс өмнө хийнэ: {M(right_b)}."),
             (f"Working out ${sub_b}$ as {om_t} gives ${ntex(om)}$, and then {says(vo)[1]}. That adds ${p}$ and ${c}$ "
              f"first. Multiplication comes before addition: ${right_b}$.")),
        vf: ((f"{M(cb)} гэдгийг {fo_t} гэж бодвол {bside_mn.lower()} тал {M(ntex(fo))} гарч, {says(vf)[0]}. "
              f"{M(c)} нь хаалтан доторх хоёр тоог хоёуланг нь үржүүлнэ: {M(right_b)}."),
             (f"Working out ${cb}$ as {fo_t} makes the {bside_en} side ${ntex(fo)}$, and then {says(vf)[1]}. "
              f"The ${c}$ multiplies both numbers inside the bracket: ${right_b}$.")),
    }
    diag["solve"] = ((f"Шийд мөн эсэхийг мэдэхийн тулд тэгшитгэлийг бодох шаардлагагүй. {M(xt)} утгыг хоёр талд орлуулаад "
                      f"гарсан тоонуудыг харьцуулахад хангалттай."),
                     (f"There is no need to solve the equation to check a value. Put ${xt}$ into both sides and compare "
                      f"the two numbers."))
    order = ["yes", "gt", "lt", "solve"]
    rot = i % 4
    order = order[rot:] + order[:rot]
    ci = order.index(target)
    vtag = {vo: "order-of-operations", vf: "distribute-first-term-only", "solve": "thinks-must-solve-to-check"}
    wrongs = [(VERDICT[o][0], VERDICT[o][1], diag[o][0], diag[o][1], vtag[o]) for o in order if o != target]
    opts = []
    wi = iter(wrongs)
    for o in order:
        opts.append(None if o == target else next(wi))
    if target == "yes":
        concl_mn = f"Хоёр тал {M(ntex(L))} болж тэнцүү тул {M(xt)} шийд мөн."
        concl_en = f"Both sides equal ${ntex(L)}$, so ${xt}$ is a solution."
    else:
        rel = ">" if L > R else "<"
        concl_mn = (f"{M(f'{ntex(L)} {rel} {ntex(R)}')} тул {M(xt)} шийд биш: зүүн тал нь баруун талаасаа "
                    f"{'их' if L > R else 'бага'}.")
        concl_en = f"${ntex(L)} {rel} {ntex(R)}$, so ${xt}$ is not a solution: the left side is {'larger' if L > R else 'smaller'}."
    steps = [
        dict(mn=dict(do=f"Тэгшитгэлийг бодох шаардлагагүй. {M(xt)} утгыг хоёр талд орлуулж, гарсан хоёр тоог харьцуулъя.",
                     why="Шийд гэдэг нь тэгшитгэлийг үнэн тэнцэтгэл болгодог утга."),
             en=dict(do=f"There is no need to solve. Put ${xt}$ into both sides and compare the two numbers.",
                     why="A solution is a value that makes the equation a true statement.")),
        dict(mn=dict(do=f"Зүүн тал: {M(Lc)}.",
                     why=("Эхлээд хаалтан доторхыг, дараа нь үржвэрийг, хамгийн сүүлд нэмэх үйлдлийг бодно." if side == "L" else None)),
             en=dict(do=f"Left side: ${Lc}$.",
                     why=("Work out the bracket first, then the product, and add last." if side == "L" else None))),
        dict(mn=dict(do=f"Баруун тал: {M(Rc)}.",
                     why=("Эхлээд хаалтан доторхыг, дараа нь үржвэрийг, хамгийн сүүлд нэмэх үйлдлийг бодно." if side == "R" else None)),
             en=dict(do=f"Right side: ${Rc}$.",
                     why=("Work out the bracket first, then the product, and add last." if side == "R" else None))),
        dict(mn=dict(do=concl_mn), en=dict(do=concl_en)),
    ]
    for s in steps:
        for lang in ("mn", "en"):
            if s[lang].get("why") is None:
                s[lang].pop("why", None)
    hints = [("Өгсөн утгыг үл мэдэгдэхийн оронд тавиад хоёр талыг тус тусад нь бодоорой.",
              "Put the given value in place of the unknown and work out each side separately."),
             (f"Зүүн тал: {M(Lc)}. Одоо баруун талыг бодоод харьцуулаарай.",
              f"Left side: ${Lc}$. Now work out the right side and compare.")]
    if target == "yes":
        expl = (f"{M(xt)} утгыг орлуулбал зүүн тал {M(ntex(L))}, баруун тал {M(ntex(R))} гарна. Тэнцүү тул шийд мөн.",
                f"Substituting ${xt}$ gives ${ntex(L)}$ on the left and ${ntex(R)}$ on the right. They are equal, so it is a solution.")
    else:
        expl = (f"{M(xt)} утгыг орлуулбал зүүн тал {M(ntex(L))}, баруун тал {M(ntex(R))} гарна. Тэнцүү биш тул шийд биш.",
                f"Substituting ${xt}$ gives ${ntex(L)}$ on the left and ${ntex(R)}$ on the right. They differ, so it is not a solution.")
    xs = f"({npy(x)})"
    checks = [f"Eq({epy(eq.lhs, xs)}, {npy(L)})", f"Eq({epy(eq.rhs, xs)}, {npy(R)})",
              (f"Eq({epy(eq.lhs, xs)}, {epy(eq.rhs, xs)})" if target == "yes" else f"Ne({epy(eq.lhs, xs)}, {epy(eq.rhs, xs)})"),
              f"Eq(({p} + {c})*({k} + ({q})), {om})", f"Eq({p} + {c}*({k}) + ({q}), {fo})",
              f"Eq({epy(brs, xs)}, {npy(bval)})", f"Eq({epy(lin, xs)}, {npy(lval)})"] + \
        piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
    return assemble(vid, i, st_mn, st_en, VERDICT[target], opts, steps, hints, expl, checks, fixed_ci=ci)


def subst_variant_b(vid, i, eq):
    v = eq.var
    w = Walk(eq)
    ms = pick3(w.sol, w.mistakes(["first_only", "neg_sign", "partial", "add_dens", "abs", "drop", "move_var_sign", "move_const_sign", "no_divide",
                                  "neg", "mul_instead"]))
    ci = i % 4
    vals = [m["x"] for m in ms]
    vals.insert(ci, w.sol)
    steps = [dict(mn=dict(do=f"Тэгшитгэлийг бодохгүйгээр ч болно. Сонголт бүрийг {VW(v, v, 'gen')} оронд тавьж, хоёр талыг тус тусад нь бодъё.",
                          why="Шийд гэдэг нь тэгшитгэлийг үнэн тэнцэтгэл болгодог утга. Ганцхан утга тохирно."),
                  en=dict(do=f"No need to solve: put each option in place of ${v}$ and work out both sides.",
                          why="A solution is a value that makes the equation true, and only one of the options will."))]
    checks = list(w.checks)
    order_idx = [j for j in range(4) if j != ci] + [ci]       # the solution is checked last
    for j in order_idx:
        x = vals[j]
        Lc, Rc = sub_chain(eq.lhs, v, x), sub_chain(eq.rhs, v, x)
        xt = f"{v} = {ntex(x)}"
        if j == ci:
            mn = f"{M(xt)}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Хоёр тал тэнцүү тул энэ нь шийд."
            en = f"${xt}$: left side ${Lc}$, right side ${Rc}$. The sides are equal, so this is the solution."
        else:
            mn = f"{M(xt)}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Тэнцүү биш."
            en = f"${xt}$: left side ${Lc}$, right side ${Rc}$. Not equal."
        steps.append(dict(mn=dict(do=mn), en=dict(do=en)))
    wrongs = []
    for m in ms:
        x = m["x"]
        Lv, Rv = ntex(eval_side(eq.lhs, x)), ntex(eval_side(eq.rhs, x))
        wrongs.append((M(f"{v} = {ntex(x)}"), M(f"{v} = {ntex(x)}"),
                       m["mn"] + f" Орлуулж шалгавал зүүн тал {M(Lv)}, баруун тал {M(Rv)} гарч тэнцэхгүй.",
                       m["en"] + f" Substituting it gives ${Lv}$ on the left and ${Rv}$ on the right, which are not equal.", m["tag"]))
        checks += m["checks"]
    first_wrong = vals[order_idx[0]]
    hints = [(f"Тэгшитгэлийг бодохгүйгээр ч болно: сонголт бүрийг {VW(v, v, 'gen')} оронд тавиад хоёр тал тэнцүү эсэхийг шалгаарай.",
              f"You do not have to solve it: put each option in place of ${v}$ and see whether the sides match."),
             (f"Жишээ нь {M(f'{v} = {ntex(first_wrong)}')} үед зүүн тал {M(ntex(eval_side(eq.lhs, first_wrong)))}, баруун тал "
              f"{M(ntex(eval_side(eq.rhs, first_wrong)))} гарч тэнцэхгүй. Бусад сонголтыг ингэж шалгаарай.",
              f"For example, ${v} = {ntex(first_wrong)}$ gives ${ntex(eval_side(eq.lhs, first_wrong))}$ on the left and "
              f"${ntex(eval_side(eq.rhs, first_wrong))}$ on the right, which do not match. Test the other options the same way.")]
    for x in vals:
        checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        checks.append(f"Eq({epy(eq.lhs, at(x))}, {npy(eval_side(eq.lhs, x))})")
        checks.append(f"Eq({epy(eq.rhs, at(x))}, {npy(eval_side(eq.rhs, x))})")
    Lv = ntex(eval_side(eq.lhs, w.sol))
    expl = (f"{M(f'{v} = {ntex(w.sol)}')} утгыг орлуулбал хоёр тал {M(Lv)} болж тэнцүү. Бусад утгад хоёр тал тэнцэхгүй.",
            f"Substituting ${v} = {ntex(w.sol)}$ makes both sides ${Lv}$. The other values do not balance the equation.")
    st_mn = f"{VW(v, v, 'gen')} аль утга нь {M(eq.tex())} тэгшитгэлийн шийд вэ?"
    st_en = f"Which value of ${v}$ is a solution of ${eq.tex()}$?"
    return assemble(vid, i, st_mn, st_en, (M(f"{v} = {ntex(w.sol)}"),) * 2, wrongs, steps, hints, expl, checks)



def tg(n):
    return M(ntex(n)) + "₮"


def story_variant(vid, i, s):
    """s: dict(var, eq, st=(mn,en), write=(mn_do, mn_why, en_do, en_why), answer=(mn,en),
               wrongs=[(wrong Eqn or value, mn, en)], hint1=(mn,en))"""
    eq, v = s["eq"], s["var"]
    w = Walk(eq, extra_steps=1)
    write = dict(mn=dict(do=s["write"][0], why=s["write"][1]), en=dict(do=s["write"][2], why=s["write"][3]))
    steps = [write] + w.steps
    chk = steps[-1]
    Lc, Rc = sub_chain(eq.lhs, v, w.sol), sub_chain(eq.rhs, v, w.sol)
    if len(eq.rhs) == 1 and eq.rhs[0].kind == "k":
        chk["mn"]["do"] = f"Шалгая: {M(Lc)}. Бодлогын нөхцөлтэй тохирч байна. {s['answer'][0]}"
        chk["en"]["do"] = f"Check: ${Lc}$, as the story says. {s['answer'][1]}"
    else:
        chk["mn"]["do"] = f"Шалгая: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Хоёр тал тэнцүү. {s['answer'][0]}"
        chk["en"]["do"] = f"Check: left side ${Lc}$, right side ${Rc}$. Both sides are equal. {s['answer'][1]}"
    cands = []
    checks = list(w.checks)
    for k_, item in enumerate(s["wrongs"]):
        wr, mn, en = item[:3]
        tag = item[3] if len(item) > 3 else s["tags"][k_]
        if isinstance(wr, Eqn):
            wr.var = v
            k, x = wr.solve()
            assert k == "one"
            checks.append(wr.check_at(x))
        else:
            x = Fr(wr)
        checks.append(f"Ne({epy(eq.lhs, at(x))}, {epy(eq.rhs, at(x))})")
        cands.append(dict(x=x, mn=mn, en=en, mode="story", tag=tag))
    dec = eq.is_dec()
    ms = pick3(w.sol, cands, dec)
    wrongs = [(M(ntexd(m["x"], dec)),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    hints = [s["hint1"], (f"{s['write'][4]} Одоо тэгшитгэлээ бодоорой.", f"{s['write'][5]} Now solve it.")]
    Lv = ntex(eval_side(eq.lhs, w.sol))
    expl = (f"Тэгшитгэл нь {M(eq.tex())}. Бодвол {M(f'{v} = {ntex(w.sol)}')}, шалгахад хоёр тал {M(Lv)} болно.",
            f"The equation is ${eq.tex()}$. Solving it gives ${v} = {ntex(w.sol)}$, and both sides then equal ${Lv}$.")
    e, m = assemble(vid, i, s["st"][0], s["st"][1], (M(ntexd(w.sol, dec)),) * 2, wrongs, steps, hints, expl, checks)
    return thin_all(e), thin_all(m)


GROUP = re.compile(r"(?<![\d.])(\d{4,})(?![\d.])")


def thin(seg):
    """Thousands inside maths get the thin space the rest of the unit uses: 42000 -> 42\\,000."""
    def g(mo):
        n = mo.group(1)
        out = ""
        while len(n) > 3:
            out = "\\," + n[-3:] + out
            n = n[:-3]
        return n + out
    return GROUP.sub(g, seg)


def thin_all(node):
    if isinstance(node, str):
        return MATH.sub(lambda mo: thin(mo.group(0)), node)
    if isinstance(node, list):
        return [thin_all(x) for x in node]
    if isinstance(node, dict):
        return {k: (v if k in ("check", "id") else thin_all(v)) for k, v in node.items()}
    return node


def stories_v1():
    S = []
    # 1 · notebooks and a pen
    e = Eqn([V(4), K(1500)], [K(11500)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Бат {M(4)} дэвтэр, нэг үзэг худалдаж аваад нийт {tg(11500)} төлсөн. Үзэг {tg(1500)} бол нэг дэвтэр хэдэн төгрөг вэ?",
            f"Bat bought ${4}$ notebooks and one pen and paid {tg(11500)} in total. The pen cost {tg(1500)}. How much is one notebook?"),
        write=(f"Нэг дэвтрийн үнийг {M('x')} төгрөг гэе. {M(4)} дэвтэр {M('4x')} төгрөг, түүн дээр үзэгний {tg(1500)} нэмэгдэж "
               f"нийт {tg(11500)} болсон тул тэгшитгэл нь {M(e.tex())}.",
               "«Нэг бүр нь» гэсэн үнэ ширхгийн тоогоор үржигдэнэ, харин нэг удаа авсан зүйл нэг л удаа нэмэгдэнэ.",
               f"Let one notebook cost $x$ tögrög. Four notebooks cost $4x$, the pen adds {tg(1500)}, and the total is "
               f"{tg(11500)}, so the equation is ${e.tex()}$.",
               "A price «each» is multiplied by how many were bought; something bought once is added once.",
               f"Нэг дэвтрийг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With one notebook as $x$ the equation is ${e.tex()}$."),
        answer=(f"Нэг дэвтэр {tg(2500)}.", f"One notebook costs {tg(2500)}."),
        hint1=("Юуг олох гэж байгааг $x$ гэж тэмдэглээрэй. Дөрвөн дэвтэр хэдэн төгрөг болох вэ?",
               "Call the unknown price $x$. What do four notebooks cost?"),
        wrongs=[(Eqn([BR(4, V(1), K(1500))], [K(11500)]),
                 f"{M('4(x + 1500) = 11500')} гэж бичсэн бол үзгийг дэвтэр бүрт нэг нэгээр тооцсон байна. Үзэг ганцхан тул түүний үнэ нэг л удаа нэмэгдэнэ: {M(e.tex())}.",
                 f"Writing $4(x + 1500) = 11500$ charges the pen once per notebook. There is only one pen, so its price is added once: ${e.tex()}$."),
                (Eqn([V(4), K(-1500)], [K(11500)]),
                 f"{M('4x - 1500 = 11500')} гэж бичсэн бол үзгийн үнийг хассан байна. Үзгийг нэмж худалдаж авсан тул нийт дүнд нэмэгдэнэ.",
                 "Writing $4x - 1500 = 11500$ subtracts the pen. The pen was bought as well, so it adds to the total."),
                (10000, f"{MX('4x = 10_000')} хүртэл зөв. Гэхдээ {MX('10_000')}₮ бол дөрвөн дэвтрийн үнэ. Нэг дэвтрийн үнийг олохын тулд {W(4, 'dat')} хуваана.",
                 "Up to $4x = 10\\,000$ is right, but $10\\,000$₮ is the price of all four notebooks. Divide by $4$ for one."),
                (Eqn([V(1), K(1500)], [K(11500)]),
                 f"{M('x + 1500 = 11500')} гэж бичсэн бол дэвтрийн тоог мартжээ. {M(4)} дэвтэр тул нэгийн үнийг {W(4, 'ins')} үржүүлнэ.",
                 "Writing $x + 1500 = 11500$ forgets how many notebooks there were. There are $4$, so the price of one is multiplied by $4$.")]))
    # 2 · ages: sum and difference
    e = Eqn([V(1), V(1), K(3)], [K(25)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Номин дүүгээсээ {M(3)} насаар ахмад. Хоёулангийнх нь насны нийлбэр {M(25)}. Дүү нь хэдэн настай вэ?",
            f"Nomin is ${3}$ years older than her younger brother. Their ages add up to ${25}$. How old is her brother?"),
        write=(f"Дүүгийн насыг {M('x')} гэе. Номин {M(3)} насаар ахмад тул {M('x + 3')} настай. Нийлбэр нь {M(25)} тул "
               f"{M('x + (x + 3) = 25')}, өөрөөр хэлбэл {M(e.tex())}.",
               "«Насаар ахмад» гэдэг нь дүүгийн насан дээр нэмэх гэсэн үг. «Нийлбэр» нь хоёр насыг нэмэхийг хэлнэ.",
               f"Let the brother be $x$ years old. Nomin is ${3}$ years older, so she is $x + 3$. Their ages add to ${25}$: "
               f"$x + (x + 3) = 25$, that is ${e.tex()}$.",
               "«Older by» means add to the brother's age; «add up to» means the two ages are added.",
               f"Дүүг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With the brother as $x$ the equation is ${e.tex()}$."),
        answer=(f"Дүү нь {M(11)} настай, Номин {M(14)} настай.", f"The brother is ${11}$ and Nomin is ${14}$."),
        hint1=("Дүүгийн насыг $x$ гэвэл Номины насыг $x$-ээр яаж бичих вэ?",
               "If the brother is $x$, how do you write Nomin's age using $x$?"),
        wrongs=[(14, f"{M(14)} бол Номины нас. Асуулт дүүгийн насыг асууж байна: {M('x = 11')}. Хариугаа бичихээсээ өмнө асуултыг дахин уншаарай.",
                 "$14$ is Nomin's age, but the question asks for her brother's: $x = 11$. Read the question again before you answer."),
                (Eqn([V(1), K(3)], [K(25)]),
                 f"{M('x + 3 = 25')} гэж бичсэн бол зөвхөн Номины насыг {M(25)}-тай тэнцүүлжээ. {M(25)} бол хоёр насны нийлбэр тул дүүгийн {M('x')}-ийг ч нэмнэ.",
                 "Writing $x + 3 = 25$ sets Nomin's age alone equal to $25$. $25$ is the sum of both ages, so the brother's $x$ is added too."),
                (Fr(25, 2), f"{W(25, 'acc')} {W(2, 'dat')} хуваасан бол хоёр хүүхдийг ижил настай гэж үзсэн байна. Тэдний нас {W(3, 'ins')} ялгаатай тул эхлээд {W(3, 'acc')} хасна: {M('2x = 22')}.",
                 "Halving $25$ treats the two as the same age. They differ by $3$, so take the $3$ away first: $2x = 22$.")]))
    # 3 · saving money
    e = Eqn([K(12000), V(5000)], [K(47000)], "n")
    S.append(dict(
        var="n", eq=e,
        st=(f"Тэмүүлэнд одоо {tg(12000)} байгаа. Тэр долоо хоног бүр {tg(5000)} хадгалбал хэдэн долоо хоногийн дараа {tg(47000)}-тэй болох вэ?",
            f"Temuulen has {tg(12000)} now. If he saves {tg(5000)} every week, after how many weeks will he have {tg(47000)}?"),
        write=(f"Долоо хоногийн тоог {M('n')} гэе. {M('n')} долоо хоногт {M('5000n')} төгрөг хуримтлагдаж, анхны {tg(12000)} дээр нэмэгдэнэ. "
               f"Нийт нь {tg(47000)} болох тул {M(e.tex())}.",
               "Анхны мөнгө нэг л удаа тоологдоно, харин долоо хоног бүрийн хадгаламж долоо хоногийн тоогоор үржигдэнэ.",
               f"Let $n$ be the number of weeks. In $n$ weeks he saves $5000n$ tögrög on top of the {tg(12000)} he has, "
               f"and the total is {tg(47000)}: ${e.tex()}$.",
               "The starting money counts once; the weekly saving is multiplied by the number of weeks.",
               f"Долоо хоногийг {M('n')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $n$ weeks the equation is ${e.tex()}$."),
        answer=(f"{M(7)} долоо хоногийн дараа.", f"After ${7}$ weeks."),
        hint1=("Долоо хоногийн тоог $n$ гэе. $n$ долоо хоногт хэдэн төгрөг хадгалах вэ? Одоо байгаа мөнгийг хаана нэмэх вэ?",
               "Let $n$ be the number of weeks. How much does he save in $n$ weeks, and where does the money he already has go?"),
        wrongs=[(Eqn([V(5000)], [K(47000)], "n"),
                 f"{M('5000n = 47000')} гэж бичсэн бол одоо байгаа {M(ntex(12000))} төгрөгийг тооцоогүй байна. Тэмүүлэн тэгээс эхлээгүй тул анхны мөнгө нийт дүнд орно.",
                 f"Writing $5000n = 47000$ ignores the {tg(12000)} he already has. He does not start from zero, so that money is part of the total."),
                (Eqn([V(5000)], [K(47000), K(12000)], "n"),
                 f"{M('5000n = 47000 + 12000')} гэж бичсэн бол {W(12000, 'acc')} нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй байна. Хоёр талаас хасах ёстой: {MX('5000n = 35_000')}.",
                 "Writing $5000n = 47000 + 12000$ moves $12\\,000$ across without changing its sign. Subtract it from both sides: $5000n = 35\\,000$."),
                (35000, f"{MX('5000n = 35_000')} хүртэл зөв. Гэхдээ {MX('35_000')} бол хадгалах ёстой мөнгө, долоо хоногийн тоо биш. {W(5000, 'dat')} хуваана.",
                 "Up to $5000n = 35\\,000$ is right, but $35\\,000$ is the money still to save, not the number of weeks. Divide by $5000$.")]))
    # 4 · bus to Darkhan
    e = Eqn([K(40), V(60)], [K(220)], "t")
    S.append(dict(
        var="t", eq=e,
        st=(f"Улаанбаатараас Дархан хүртэл {M(220)} км. Автобус эхний {M(40)} км-ийг явсны дараа цагт {M(60)} км хурдтай явж байна. "
            f"Үлдсэн замыг хэдэн цагт туулах вэ?",
            f"It is ${220}$ km from Ulaanbaatar to Darkhan. After the first ${40}$ km a bus travels at ${60}$ km per hour. "
            f"How many hours does the rest of the journey take?"),
        write=(f"Үлдсэн замыг туулах цагийг {M('t')} гэе. {M('t')} цагт автобус {M('60t')} км явна. Эхний {M(40)} км дээр үүнийг нэмбэл "
               f"нийт {M(220)} км болох тул {M(e.tex())}.",
               "Хурдыг цагаар үржүүлбэл явсан зам гарна. Өмнө нь явсан зам нэг удаа нэмэгдэнэ.",
               f"Let the remaining time be $t$ hours. In $t$ hours the bus covers $60t$ km; add the first ${40}$ km and the "
               f"total is ${220}$ km: ${e.tex()}$.",
               "Speed times time gives distance; the part already driven is added once.",
               f"Цагийг {M('t')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $t$ hours the equation is ${e.tex()}$."),
        answer=(f"Үлдсэн замыг {M(3)} цагт туулна.", f"The rest takes ${3}$ hours."),
        hint1=("Үлдсэн замын цагийг $t$ гэвэл автобус $t$ цагт хэдэн км явах вэ?",
               "If the remaining time is $t$ hours, how far does the bus go in $t$ hours?"),
        wrongs=[(Eqn([V(60)], [K(220)], "t"),
                 f"{M('60t = 220')} гэж бичсэн бол эхний {M(40)} км-ийг тооцоогүй. Тэр хэсгийг өмнө нь явсан тул үлдсэн зам нь {M('220 - 40')} км.",
                 "Writing $60t = 220$ leaves out the first $40$ km. That part is already driven, so what is left is $220 - 40$ km."),
                (Eqn([V(60)], [K(220), K(40)], "t"),
                 f"{M('60t = 220 + 40')} гэж бичсэн бол {W(40, 'acc')} хасахын оронд нэмсэн. Хоёр талаас {W(40, 'acc')} хасна: {M('60t = 180')}.",
                 "Writing $60t = 220 + 40$ adds the $40$ instead of subtracting it. Subtract $40$ from both sides: $60t = 180$."),
                (180, f"{M('60t = 180')} хүртэл зөв. Гэхдээ {M(180)} бол км, цаг биш. Цагийг олохын тулд {W(60, 'dat')} хуваана.",
                 "Up to $60t = 180$ is right, but $180$ is kilometres, not hours. Divide by $60$ to get the time.")]))
    # 5 · cinema tickets for four friends
    e = Eqn([V(4), K(6000)], [K(42000)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Энхжин {M(3)} найзтайгаа кинонд орсон. Тасалбар бүр ижил үнэтэй. Тэд тасалбараас гадна {M(ntex(6000))} төгрөгийн попкорн авч, нийт {tg(42000)} төлжээ. "
            "Нэг тасалбар хэдэн төгрөг вэ?",
            f"Enkhjin went to the cinema with ${3}$ friends. Every ticket costs the same. Besides the tickets they bought popcorn for "
            f"${ntex(6000)}$ tögrög and paid {tg(42000)} in total. How much is one ticket?"),
        write=(f"Нэг тасалбарын үнийг {M('x')} гэе. Энхжинг оруулаад {M(4)} хүн тул тасалбар {M('4x')} төгрөг. Попкорны {tg(6000)} нэмбэл "
               f"нийт {tg(42000)} болох тул {M(e.tex())}.",
               f"«{M(3)} найзтайгаа» гэсэн бол Энхжин өөрөө нэмэгдэж нийт {M(4)} хүн болно. Попкорныг нэг удаа авсан тул нэг л удаа нэмнэ.",
               f"Let one ticket cost $x$. With Enkhjin there are ${4}$ people, so the tickets cost $4x$. Add the popcorn and the "
               f"total is {tg(42000)}: ${e.tex()}$.",
               "«With 3 friends» means Enkhjin herself makes 4 people. The popcorn was bought once, so it is added once.",
               f"Нэг тасалбарыг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With one ticket as $x$ the equation is ${e.tex()}$."),
        answer=(f"Нэг тасалбар {tg(9000)}.", f"One ticket costs {tg(9000)}."),
        hint1=("Кинонд нийт хэдэн хүн орсон бэ? Энхжинг өөрийг нь тоолохоо мартуузай.",
               "How many people went to the cinema? Do not forget to count Enkhjin herself."),
        wrongs=[(Eqn([V(3), K(6000)], [K(42000)]),
                 f"{M('3x + 6000 = 42000')} гэж бичсэн бол Энхжинг өөрийг нь тоолоогүй. «{M(3)} найзтайгаа» гэсэн тул нийт {M(4)} хүн.",
                 "Writing $3x + 6000 = 42000$ leaves Enkhjin out. «With $3$ friends» makes $4$ people in all."),
                (Eqn([BR(4, V(1), K(6000))], [K(42000)]),
                 f"{M('4(x + 6000) = 42000')} гэж бичсэн бол попкорныг хүн бүрт авсан гэж үзжээ. Попкорныг нэг удаа авсан тул нэг л удаа нэмнэ.",
                 "Writing $4(x + 6000) = 42000$ buys popcorn for each person. It was bought once, so it is added once."),
                (36000, f"{MX('4x = 36_000')} хүртэл зөв. Гэхдээ {MX('36_000')} бол дөрвөн тасалбарын үнэ. {W(4, 'dat')} хуваана.",
                 "Up to $4x = 36\\,000$ is right, but that is the price of four tickets. Divide by $4$.")]))
    # 6 · three consecutive integers
    e = Eqn([V(1), V(1), K(1), V(1), K(2)], [K(72)], "n")
    S.append(dict(
        var="n", eq=e,
        st=(f"Дараалсан гурван бүхэл тооны нийлбэр {M(72)}. Эдгээрийн хамгийн бага нь аль вэ?",
            f"Three consecutive integers add up to ${72}$. What is the smallest of them?"),
        write=(f"Хамгийн бага тоог {M('n')} гэе. Дараагийн хоёр нь {M('n + 1')} ба {M('n + 2')}. Нийлбэр нь {M(72)} тул {M(e.tex())}.",
               "Дараалсан бүхэл тоонууд бие биенээсээ нэгээр ялгаатай.",
               f"Let the smallest be $n$. The next two are $n + 1$ and $n + 2$. They add to ${72}$: ${e.tex()}$.",
               "Consecutive integers go up by one each time.",
               f"Хамгийн бага тоог {M('n')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With the smallest as $n$ the equation is ${e.tex()}$."),
        answer=(f"Тоонууд {M('23, 24, 25')}, хамгийн бага нь {M(23)}.", f"The numbers are $23, 24, 25$; the smallest is ${23}$."),
        hint1=("Хамгийн бага тоог $n$ гэвэл дараагийн хоёр тоог $n$-ээр яаж бичих вэ?",
               "If the smallest is $n$, how do you write the next two using $n$?"),
        wrongs=[(24, f"{W(72, 'acc')} {W(3, 'dat')} хуваавал дунд тоо гарна. Асуулт хамгийн бага тоог асууж байна: {M('24 - 1 = 23')}.",
                 "Dividing $72$ by $3$ gives the middle number. The question asks for the smallest: $24 - 1 = 23$."),
                (25, f"{M(25)} бол хамгийн их тоо. Хамгийн бага тоо нь {M(23)}.",
                 "$25$ is the largest of the three. The smallest is $23$."),
                (Eqn([V(1), K(1), K(2)], [K(72)], "n"),
                 f"{M('n + 1 + 2 = 72')} гэж бичсэн бол хоёр, гурав дахь тоонд {M('n')}-ийг оруулахаа мартжээ. Тоо бүр {M('n')}-ийг агуулна: {M('n + (n + 1) + (n + 2)')}.",
                 "Writing $n + 1 + 2 = 72$ forgets the $n$ in the second and third numbers. Each of them contains $n$: $n + (n + 1) + (n + 2)$.")]))
    # 7 · mobile data
    e = Eqn([K(8000), V(1500)], [K(20000)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Сарнай утасныхаа төлбөрт сар бүр {tg(8000)} суурь төлбөр, нэмээд нэг гигабайт тутамд {tg(1500)} төлдөг. "
            f"Энэ сард {tg(20000)} төлсөн бол хэдэн гигабайт хэрэглэсэн бэ?",
            f"Sarnai pays a monthly base fee of {tg(8000)} for her phone, plus {tg(1500)} for each gigabyte. "
            f"This month she paid {tg(20000)}. How many gigabytes did she use?"),
        write=(f"Хэрэглэсэн гигабайтын тоог {M('x')} гэе. Гигабайтын төлбөр {M('1500x')} төгрөг, суурь төлбөр {tg(8000)}. "
               f"Нийлээд {tg(20000)} тул {M(e.tex())}.",
               "«Нэг гигабайт тутамд» гэсэн үнэ гигабайтын тоогоор үржигдэнэ. Суурь төлбөр сард нэг удаа нэмэгдэнэ.",
               f"Let $x$ be the gigabytes used. They cost $1500x$, the base fee is {tg(8000)}, and together that is "
               f"{tg(20000)}: ${e.tex()}$.",
               "A price «per gigabyte» is multiplied by the gigabytes; the base fee is added once a month.",
               f"Гигабайтыг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $x$ gigabytes the equation is ${e.tex()}$."),
        answer=(f"Тэр {M(8)} гигабайт хэрэглэсэн.", f"She used ${8}$ gigabytes."),
        hint1=("Гигабайтын тоог $x$ гэвэл гигабайтын төлбөр хэд болох вэ? Суурь төлбөрийг хэдэн удаа нэмэх вэ?",
               "If she used $x$ gigabytes, what do they cost? How many times is the base fee added?"),
        wrongs=[(Eqn([K(1500), V(8000)], [K(20000)]),
                 f"{M('1500 + 8000x = 20000')} гэж бичсэн бол хоёр үнийг сольсон байна. Гигабайт тутмын үнэ {M('x')}-ийг үржүүлнэ, суурь төлбөр нэг удаа нэмэгдэнэ.",
                 "Writing $1500 + 8000x = 20000$ swaps the two prices. The per-gigabyte price multiplies $x$; the base fee is added once."),
                (Eqn([V(1500)], [K(20000), K(8000)]),
                 f"{M('1500x = 20000 + 8000')} гэж бичсэн бол суурь төлбөрийг хасахын оронд нэмсэн. Хоёр талаас {W(8000, 'acc')} хасна: {MX('1500x = 12_000')}.",
                 "Writing $1500x = 20000 + 8000$ adds the base fee instead of taking it away. Subtract $8000$ from both sides: $1500x = 12\\,000$."),
                (12000, f"{MX('1500x = 12_000')} хүртэл зөв. Гэхдээ {MX('12_000')} бол гигабайтад төлсөн мөнгө. Гигабайтын тоог олохын тулд {W(1500, 'dat')} хуваана.",
                 "Up to $1500x = 12\\,000$ is right, but that is the money paid for data. Divide by $1500$ to get the gigabytes.")]))
    # 8 · buses for a school trip
    e = Eqn([V(40), K(30)], [K(150)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Сургуулийн {M(150)} сурагч Эрдэнэт рүү аялалд явна. {M(30)} сурагч микроавтобусаар, бусад нь том автобусаар явна. "
            f"Нэг том автобусанд {M(40)} сурагч сууна. Хэдэн том автобус хэрэгтэй вэ?",
            f"${150}$ pupils are going on a school trip to Erdenet. ${30}$ pupils go by minibus and the rest by coach. "
            f"Each coach takes ${40}$ pupils. How many coaches are needed?"),
        write=(f"Том автобусны тоог {M('x')} гэе. Тэдгээрт {M('40x')} сурагч сууна. Микроавтобусны {M(30)} сурагчийг нэмбэл "
               f"бүх {M(150)} сурагч болох тул {M(e.tex())}.",
               "Нэг автобусанд суух хүний тоо автобусны тоогоор үржигдэнэ.",
               f"Let $x$ be the number of coaches. They carry $40x$ pupils; add the ${30}$ in the minibus and that is all "
               f"${150}$: ${e.tex()}$.",
               "Pupils per coach are multiplied by the number of coaches.",
               f"Автобусны тоог {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $x$ coaches the equation is ${e.tex()}$."),
        answer=(f"{M(3)} том автобус хэрэгтэй.", f"${3}$ coaches are needed."),
        hint1=("Том автобусны тоог $x$ гэвэл тэдгээрт хэдэн сурагч суух вэ?",
               "If there are $x$ coaches, how many pupils ride in them?"),
        wrongs=[(Eqn([V(40)], [K(150)]),
                 f"{M('40x = 150')} гэж бичсэн бол микроавтобусаар явах {M(30)} сурагчийг тооцоогүй. Тэд том автобусанд суухгүй тул эхлээд хасна.",
                 "Writing $40x = 150$ forgets the $30$ pupils in the minibus. They do not ride in a coach, so take them away first."),
                (Eqn([V(40)], [K(150), K(30)]),
                 f"{M('40x = 150 + 30')} гэж бичсэн бол {W(30, 'acc')} хасахын оронд нэмсэн. Хоёр талаас {W(30, 'acc')} хасна: {M('40x = 120')}.",
                 "Writing $40x = 150 + 30$ adds the $30$ instead of subtracting. Subtract $30$ from both sides: $40x = 120$."),
                (120, f"{M('40x = 120')} хүртэл зөв. Гэхдээ {M(120)} бол том автобусаар явах сурагчдын тоо. {W(40, 'dat')} хуваавал автобусны тоо гарна.",
                 "Up to $40x = 120$ is right, but $120$ is the number of pupils on coaches. Divide by $40$ for the number of coaches.")]))
    # 9 · father three times as old
    e = Eqn([V(3), K(10)], [BR(2, V(1), K(10))], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Доржийн аав одоо Доржоос {M(3)} дахин ахмад. {M(10)} жилийн дараа аав нь Доржоос яг {M(2)} дахин ахмад болно. "
            f"Дорж одоо хэдэн настай вэ?",
            f"Dorj's father is now ${3}$ times as old as Dorj. In ${10}$ years the father will be exactly ${2}$ times as old as Dorj. "
            f"How old is Dorj now?"),
        write=(f"Доржийн одоогийн насыг {M('x')} гэе. Аав нь {M('3x')} настай. {M(10)} жилийн дараа Дорж {M('x + 10')}, аав нь {M('3x + 10')} настай болно. "
               f"Аав нь {M(2)} дахин ахмад тул {M(e.tex())}.",
               f"Арван жил өнгөрөхөд хоёулангийнх нь нас арваар нэмэгдэнэ. «{M(2)} дахин» гэдэг нь Доржийн тэр үеийн насыг бүхлээр нь {W(2, 'ins')} үржүүлэх.",
               f"Let Dorj be $x$ now. His father is $3x$. In ${10}$ years Dorj is $x + 10$ and his father $3x + 10$. The father is "
               f"then ${2}$ times as old: ${e.tex()}$.",
               "In ten years both ages grow by ten. «Twice as old» multiplies Dorj's whole age at that time by 2.",
               f"Доржийг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With Dorj as $x$ the equation is ${e.tex()}$."),
        answer=(f"Дорж одоо {M(10)} настай, аав нь {M(30)} настай.", f"Dorj is ${10}$ now and his father is ${30}$."),
        hint1=("Доржийн одоогийн насыг $x$ гэе. Аав нь одоо хэдэн настай вэ? Арван жилийн дараа хоёулаа хэдэн настай болох вэ?",
               "Let Dorj be $x$ now. How old is his father? How old will each of them be in ten years?"),
        wrongs=[(Eqn([V(3)], [BR(2, V(1), K(10))]),
                 f"{M('3x = 2(x + 10)')} гэж бичсэн бол аавын насанд {W(10, 'acc')} нэмэхээ мартжээ. Арван жилийн дараа аав нь ч бас {M(10)} насаар ахина.",
                 "Writing $3x = 2(x + 10)$ forgets to add $10$ to the father's age. In ten years he is $10$ years older too."),
                (30, f"{M(30)} бол аавын одоогийн нас. Асуулт Доржийн насыг асууж байна: {M('x = 10')}.",
                 "$30$ is the father's age now. The question asks for Dorj's: $x = 10$."),
                (Eqn([V(3), K(10)], [V(2), K(10)]),
                 f"{M('3x + 10 = 2x + 10')} гэж бичсэн бол {W(2, 'ins')} зөвхөн {M('x')}-ийг үржүүлжээ. Доржийн тэр үеийн нас бүхлээрээ {M(2)} дахин нэмэгдэнэ: {M('2(x + 10) = 2x + 20')}.",
                 "Writing $3x + 10 = 2x + 10$ doubles only the $x$. Dorj's whole age then is doubled: $2(x + 10) = 2x + 20$.")]))
    # 10 · fence around a yard at Terelj
    e = Eqn([BR(2, V(1), V(1), K(6))], [K(52)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Тэрэлжид тэгш өнцөгт хашаа барина. Хашааны урт нь өргөнөөсөө {M(6)} м-ээр урт, периметр нь {M(52)} м. Өргөн нь хэдэн метр вэ?",
            f"A rectangular yard is being fenced at Terelj. Its length is ${6}$ m more than its width and its perimeter is ${52}$ m. How wide is it?"),
        write=(f"Өргөнийг {M('x')} м гэе. Урт нь {M('x + 6')} м. Периметр нь урт, өргөний нийлбэрийг {W(2, 'ins')} үржүүлсэнтэй тэнцүү тул {M(e.tex())}.",
               "Тэгш өнцөгт хоёр урт, хоёр өргөнтэй. Иймд периметр нь урт, өргөний нийлбэрийн хоёр дахин.",
               f"Let the width be $x$ m. The length is $x + 6$ m. The perimeter is twice the sum of length and width: ${e.tex()}$.",
               "A rectangle has two lengths and two widths, so the perimeter is twice length plus width.",
               f"Өргөнийг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With the width as $x$ the equation is ${e.tex()}$."),
        answer=(f"Өргөн нь {M(10)} м, урт нь {M(16)} м.", f"The width is ${10}$ m and the length ${16}$ m."),
        hint1=("Өргөнийг $x$ гэвэл уртыг $x$-ээр яаж бичих вэ? Тэгш өнцөгт хэдэн тал байна вэ?",
               "If the width is $x$, how do you write the length? How many sides does a rectangle have?"),
        wrongs=[(Eqn([V(1), V(1), K(6)], [K(52)]),
                 f"{M('x + x + 6 = 52')} гэж бичсэн бол хоёр талыг л нэмжээ. Тэгш өнцөгт дөрвөн талтай: хоёр урт, хоёр өргөн.",
                 "Writing $x + x + 6 = 52$ adds only two sides. A rectangle has four: two lengths and two widths."),
                (16, f"{M(16)} бол урт. Асуулт өргөнийг асууж байна: {M('x = 10')}.",
                 "$16$ is the length. The question asks for the width: $x = 10$."),
                (Eqn([V(2), V(2), K(6)], [K(52)]),
                 f"{M('2x + 2x + 6 = 52')} гэж бичсэн бол {W(6, 'acc')} хоёр дахин авахаа мартжээ. Урт хоёр удаа орох тул {M('2(x + 6) = 2x + 12')}.",
                 "Writing $2x + 2x + 6 = 52$ counts the extra $6$ only once. The length appears twice: $2(x + 6) = 2x + 12$.")]))
    # 11 · temperature rising in the morning
    e = Eqn([K(-12), V(3)], [K(6)], "t")
    S.append(dict(
        var="t", eq=e,
        st=(f"Өвлийн өглөө агаарын температур {M('-12')}°C байв. Цаг тутамд {M(3)}°C-ээр дулаарвал хэдэн цагийн дараа {M(6)}°C болох вэ?",
            f"On a winter morning the temperature was ${'-12'}$°C. If it rises by ${3}$°C every hour, after how many hours will it be ${6}$°C?"),
        write=(f"Өнгөрөх цагийг {M('t')} гэе. {M('t')} цагт температур {M('3t')} градусаар дулаарна. Эхлэл нь {M('-12')}°C тул {M(e.tex())}.",
               "Эхний температур нэг удаа тоологдоно, харин цаг тутмын өөрчлөлт цагийн тоогоор үржигдэнэ.",
               f"Let $t$ be the hours. In $t$ hours it warms by $3t$ degrees, starting from ${'-12'}$°C: ${e.tex()}$.",
               "The starting temperature counts once; the change per hour is multiplied by the hours.",
               f"Цагийг {M('t')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $t$ hours the equation is ${e.tex()}$."),
        answer=(f"{M(6)} цагийн дараа.", f"After ${6}$ hours."),
        hint1=("Цагийн тоог $t$ гэвэл $t$ цагт хэдэн градусаар дулаарах вэ? Эхлэл нь сөрөг гэдгийг мартуузай.",
               "If $t$ hours pass, how many degrees does it warm up? Remember the start is below zero."),
        wrongs=[(Eqn([V(3)], [K(6), K(-12)], "t"),
                 f"{M('3t = 6 - 12')} гэж бичсэн бол {W(-12, 'acc')} нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй. Хоёр талд {W(12, 'acc')} нэмнэ: {M('3t = 6 + 12 = 18')}.",
                 "Writing $3t = 6 - 12$ moves $-12$ across without changing its sign. Add $12$ to both sides: $3t = 6 + 12 = 18$."),
                (2, f"{W(6, 'acc')} {W(3, 'dat')} хуваасан бол температур тэгээс эхэлсэн гэж үзжээ. Эхлэл нь {M('-12')}°C тул эхлээд {M(0)} хүрэхэд ч {M(4)} цаг болно.",
                 "Dividing $6$ by $3$ assumes it started at zero. It started at $-12$°C, so even reaching $0$ takes $4$ hours."),
                (18, f"{M('3t = 18')} хүртэл зөв. Гэхдээ {M(18)} бол градусын өөрчлөлт, цаг биш. {W(3, 'dat')} хуваана.",
                 "Up to $3t = 18$ is right, but $18$ is the change in degrees, not the hours. Divide by $3$.")]))
    # 12 · basketball points
    e = Eqn([V(2), K(15)], [K(23)], "x")
    S.append(dict(
        var="x", eq=e,
        st=(f"Сагсан бөмбөгийн тоглолтод Бат нийт {M(23)} оноо авсан. Үүнээс {M(5)} нь гурван онооны шидэлт, бусад нь хоёр онооны шидэлт байв. "
            f"Бат хоёр онооны хэдэн шидэлт хийсэн бэ?",
            f"In a basketball game Bat scored ${23}$ points. ${5}$ of his baskets were three-pointers and the rest two-pointers. "
            f"How many two-pointers did he score?"),
        write=(f"Хоёр онооны шидэлтийн тоог {M('x')} гэе. Тэдгээр нь {M('2x')} оноо, гурван онооны {M(5)} шидэлт {MX('3 · 5 = 15')} оноо. "
               f"Нийт {M(23)} тул {M(e.tex())}.",
               "Шидэлтийн тоог нэг шидэлтийн оноогоор үржүүлбэл оноо гарна. Гурван онооны шидэлтийг ч мөн гурваар үржүүлнэ.",
               f"Let $x$ be the two-pointers. They give $2x$ points; the ${5}$ three-pointers give $3 \\cdot 5 = 15$. "
               f"The total is ${23}$: ${e.tex()}$.",
               "Baskets times points per basket gives points, and that goes for the three-pointers too.",
               f"Хоёр онооны шидэлтийг {M('x')} гэвэл тэгшитгэл {M(e.tex())} болно.", f"With $x$ two-pointers the equation is ${e.tex()}$."),
        answer=(f"Бат хоёр онооны {M(4)} шидэлт хийсэн.", f"Bat scored ${4}$ two-pointers."),
        hint1=("Хоёр онооны шидэлтийг $x$ гэе. Гурван онооны таван шидэлт нийт хэдэн оноо өгөх вэ?",
               "Let $x$ be the two-pointers. How many points do the five three-pointers give?"),
        wrongs=[(Eqn([V(2), K(5)], [K(23)]),
                 f"{M('2x + 5 = 23')} гэж бичсэн бол шидэлтийн тоог оноо гэж тооцжээ. {M(5)} шидэлт тус бүр {M(3)} оноо тул {MX('3 · 5 = 15')} оноо.",
                 "Writing $2x + 5 = 23$ counts baskets as points. Each of the $5$ baskets is worth $3$: $3 \\cdot 5 = 15$ points."),
                (Eqn([V(2)], [K(23), K(15)]),
                 f"{M('2x = 23 + 15')} гэж бичсэн бол {W(15, 'acc')} хасахын оронд нэмсэн. Хоёр талаас {W(15, 'acc')} хасна: {M('2x = 8')}.",
                 "Writing $2x = 23 + 15$ adds the $15$ instead of subtracting. Subtract $15$ from both sides: $2x = 8$."),
                (8, f"{M('2x = 8')} хүртэл зөв. Гэхдээ {M(8)} бол оноо, шидэлтийн тоо биш. {W(2, 'dat')} хуваана.",
                 "Up to $2x = 8$ is right, but $8$ is points, not baskets. Divide by $2$.")]))
    return S


NAMES = [("Бат", "Bat"), ("Сарнай", "Sarnai"), ("Тэмүүлэн", "Temuulen"), ("Номин", "Nomin"),
         ("Энхжин", "Enkhjin"), ("Дорж", "Dorj")]


def mv_text(mv, var):
    """A correct move between two lines, in both languages."""
    kind = mv[0]
    if kind == "expand":
        return ("хаалтыг зөв нээсэн", "the bracket is opened correctly")
    if kind == "combine":
        return ("төсөөтэй гишүүдийг зөв нэгтгэсэн", "like terms are combined correctly")
    if kind == "subvar":
        return (f"хоёр талаас {VW(mv[1], var, 'acc')} хассан", f"${mv[1]}$ is subtracted from both sides")
    if kind == "addvar":
        return (f"хоёр талд {VW(mv[1], var, 'acc')} нэмсэн", f"${mv[1]}$ is added to both sides")
    if kind == "subc":
        return (f"хоёр талаас {W(mv[1], 'acc')} хассан", f"${mv[1]}$ is subtracted from both sides")
    if kind == "addc":
        return (f"хоёр талд {W(mv[1], 'acc')} нэмсэн", f"${mv[1]}$ is added to both sides")
    if kind == "div":
        return (f"хоёр талыг {W(mv[1], 'dat')} хуваасан", f"both sides are divided by ${ntex(mv[1])}$")
    if kind == "mul":
        return (f"хоёр талыг {W(mv[1], 'ins')} үржүүлсэн", f"both sides are multiplied by ${mv[1]}$")
    if kind == "text":
        return (mv[1], mv[2])
    raise ValueError(kind)


def find_error_cases():
    """Twelve worked solutions, each with exactly one faulty line (4 in each position)."""
    shift = ("Нөгөө тал руу шилжсэн гишүүний тэмдэг эсрэгээрээ солигдоно.",
             "A term that crosses the equals sign changes its sign.")
    every_br = ("Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг үржүүлнэ.",
                "The number in front of a bracket multiplies every term inside.")
    C = []
    C.append(dict(var="x", eq=Eqn([BR(3, V(1), K(-2))], [V(2), K(5)]),
                  lines=[Eqn([V(3), K(-2)], [V(2), K(5)]), Eqn([V(1), K(-2)], [K(5)]), Eqn([V(1)], [K(7)])],
                  err=0, moves=[None, ("subvar", "2x"), ("addc", 2)],
                  why=(f"Хаалтыг нээхдээ {W(3, 'ins')} зөвхөн $x$-ийг үржүүлжээ. $3(x - 2) = 3x - 6$ байх ёстой.",
                       "Only the $x$ was multiplied by $3$. It should be $3(x - 2) = 3x - 6$."),
                  rule=every_br,
                  fix=[Eqn([V(3), K(-6)], [V(2), K(5)]), Eqn([V(1), K(-6)], [K(5)]), Eqn([V(1)], [K(11)])]))
    C.append(dict(var="y", eq=Eqn([V(5), K(-4)], [V(2), K(11)], "y"),
                  lines=[Eqn([V(3), K(-4)], [K(11)], "y"), Eqn([V(3)], [K(7)], "y"), Eqn([V(1)], [K(Fr(7, 3))], "y")],
                  err=1, moves=[("subvar", "2y"), None, ("div", 3)],
                  why=(f"{W(-4, 'acc')} баруун тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй: $11 - 4$ гэж бодсон. "
                       f"Хоёр талд {W(4, 'acc')} нэмэх ёстой: $3y = 11 + 4 = 15$.",
                       "The $-4$ crossed to the right without changing sign, giving $11 - 4$. Add $4$ to both sides: $3y = 11 + 4 = 15$."),
                  rule=shift,
                  fix=[Eqn([V(3)], [K(15)], "y"), Eqn([V(1)], [K(5)], "y")]))
    C.append(dict(var="n", eq=Eqn([V(-4), K(7)], [V(2), K(19)], "n"),
                  lines=[Eqn([V(-6), K(7)], [K(19)], "n"), Eqn([V(-6)], [K(12)], "n"), Eqn([V(1)], [K(2)], "n")],
                  err=2, moves=[("subvar", "2n"), ("subc", 7), None],
                  why=(f"$-6n = 12$ үед хоёр талыг {W(-6, 'dat')} хуваах ёстой. Хасах тэмдгийг орхисон тул $n = 2$ гарсан, зөв нь $n = -2$.",
                       "From $-6n = 12$, divide both sides by $-6$. The minus sign was dropped: it should be $n = -2$."),
                  rule=("Коэффициент сөрөг бол хасах тэмдэгтэй нь хамт хуваана.",
                        "A negative coefficient is divided out together with its minus sign."),
                  fix=[Eqn([V(1)], [K(-2)], "n")]))
    C.append(dict(var="x", eq=Eqn([FR(2, V(1)), K(1)], [FR(3, V(1)), K(2)]),
                  lines=[Eqn([V(3), K(1)], [V(2), K(2)]), Eqn([V(1), K(1)], [K(2)]), Eqn([V(1)], [K(1)])],
                  err=0, moves=[None, ("subvar", "2x"), ("subc", 1)],
                  why=(f"Хоёр талыг {W(6, 'ins')} үржүүлэхдээ бутархайг л үржүүлээд $1$ ба {W(2, 'acc')} үржүүлээгүй. "
                       "$3x + 6 = 2x + 12$ байх ёстой.",
                       "Multiplying by $6$, only the fractions were multiplied, not the $1$ and the $2$. It should be $3x + 6 = 2x + 12$."),
                  rule=("Хоёр талыг үржүүлэхдээ гишүүн бүрийг үржүүлнэ.",
                        "Multiplying both sides means multiplying every term."),
                  fix=[Eqn([V(3), K(6)], [V(2), K(12)]), Eqn([V(1), K(6)], [K(12)]), Eqn([V(1)], [K(6)])]))
    C.append(dict(var="x", eq=Eqn([K(6), BR(-1, V(1), K(-4))], [V(3)]),
                  lines=[Eqn([K(6), V(-1), K(4)], [V(3)]), Eqn([K(10), V(-1)], [V(3)]), Eqn([V(1)], [K(5)])],
                  err=2, moves=[("expand",), ("combine",), None],
                  why=("$-x$-ийг баруун тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй: $10 = 3x - x = 2x$ гэж бодсон. "
                       "Хоёр талд $x$-ийг нэмэх ёстой: $10 = 4x$, иймд $x = \\frac{5}{2}$.",
                       "The $-x$ crossed to the right without changing sign, giving $10 = 3x - x = 2x$. Add $x$ to both sides: "
                       "$10 = 4x$, so $x = \\frac{5}{2}$."),
                  rule=shift,
                  fix=[Eqn([K(10)], [V(4)]), Eqn([V(1)], [K(Fr(5, 2))])]))
    C.append(dict(var="m", eq=Eqn([V(4), K(8)], [V(2), K(20)], "m"),
                  lines=[Eqn([V(2), K(8)], [K(20)], "m"), Eqn([V(1), K(8)], [K(10)], "m"), Eqn([V(1)], [K(2)], "m")],
                  err=1, moves=[("subvar", "2m"), None, ("subc", 8)],
                  why=(f"Хоёр талыг {W(2, 'dat')} хуваахдаа $2m$ ба {W(20, 'acc')} хуваагаад {W(8, 'acc')} хуваахаа мартжээ. "
                       "$m + 4 = 10$ байх ёстой.",
                       "Dividing by $2$, the $2m$ and the $20$ were divided but the $8$ was not. It should be $m + 4 = 10$."),
                  rule=("Хоёр талыг хуваахдаа гишүүн бүрийг хуваана.",
                        "Dividing both sides means dividing every term."),
                  fix=[Eqn([V(1), K(4)], [K(10)], "m"), Eqn([V(1)], [K(6)], "m")]))
    C.append(dict(var="a", eq=Eqn([V(3), K(2), V(1)], [K(14)], "a"),
                  lines=[Eqn([V(5), V(1)], [K(14)], "a"), Eqn([V(6)], [K(14)], "a"), Eqn([V(1)], [K(Fr(7, 3))], "a")],
                  err=0, moves=[None, ("combine",), ("div", 6)],
                  why=(f"$3a$ ба {W(2, 'acc')} нэмж $5a$ гэж бичжээ. $3a$ нь $a$-тай гишүүн, $2$ нь тоо тул тэдгээрийг нэгтгэж болохгүй. "
                       "Зөв нь $3a + a = 4a$ тул $4a + 2 = 14$.",
                       "$3a$ and $2$ were added to make $5a$. One is an $a$-term and the other a number, so they cannot be combined. "
                       "Correctly $3a + a = 4a$, so $4a + 2 = 14$."),
                  rule=("Зөвхөн төсөөтэй гишүүдийг нэгтгэж болно.", "Only like terms can be combined."),
                  fix=[Eqn([V(4), K(2)], [K(14)], "a"), Eqn([V(4)], [K(12)], "a"), Eqn([V(1)], [K(3)], "a")]))
    C.append(dict(var="x", eq=Eqn([V(7), K(-3)], [V(4), K(9)]),
                  lines=[Eqn([V(7)], [V(4), K(12)]), Eqn([V(11)], [K(12)]), Eqn([V(1)], [K(Fr(12, 11))])],
                  err=1, moves=[("addc", 3), None, ("div", 11)],
                  why=("$4x$-ийг зүүн тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй: $7x + 4x = 11x$ гэж бодсон. "
                       "Хоёр талаас $4x$-ийг хасах ёстой: $3x = 12$.",
                       "The $4x$ crossed to the left without changing sign, giving $7x + 4x = 11x$. Subtract $4x$ from both sides: $3x = 12$."),
                  rule=shift,
                  fix=[Eqn([V(3)], [K(12)]), Eqn([V(1)], [K(4)])]))
    C.append(dict(var="y", eq=Eqn([V(5), K(3)], [V(1), K(5)], "y"),
                  lines=[Eqn([V(4), K(3)], [K(5)], "y"), Eqn([V(4)], [K(2)], "y"), Eqn([V(1)], [K(2)], "y")],
                  err=2, moves=[("subvar", "y"), ("subc", 3), None],
                  why=(f"$4y = 2$ үед {W(2, 'acc')} {W(4, 'dat')} хуваах ёстой: $y = \\frac{{2}}{{4}} = \\frac{{1}}{{2}}$. "
                       f"Энд эсрэгээр нь {W(4, 'acc')} {W(2, 'dat')} хуваасан байна.",
                       "From $4y = 2$, divide $2$ by $4$: $y = \\frac{2}{4} = \\frac{1}{2}$. Here $4$ was divided by $2$ instead."),
                  rule=("Хоёр талыг коэффициентэд хуваана: нөгөө талын тоо нь хуваагдах тоо болно.",
                        "Divide both sides by the coefficient: the number on the other side is the one being divided."),
                  fix=[Eqn([V(1)], [K(Fr(1, 2))], "y")]))
    C.append(dict(var="x", eq=Eqn([BR(2, V(1), K(4))], [BR(3, V(1), K(-2))]),
                  lines=[Eqn([V(2), K(8)], [V(3), K(-6)]), Eqn([K(8)], [V(1), K(-6)]), Eqn([V(1)], [K(2)])],
                  err=2, moves=[("expand",), ("subvar", "2x"), None],
                  why=(f"{W(-6, 'acc')} зүүн тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй: $8 - 6 = 2$ гэж бодсон. "
                       f"Хоёр талд {W(6, 'acc')} нэмэх ёстой: $8 + 6 = x$, иймд $x = 14$.",
                       "The $-6$ crossed to the left without changing sign, giving $8 - 6 = 2$. Add $6$ to both sides: $8 + 6 = x$, so $x = 14$."),
                  rule=shift,
                  fix=[Eqn([K(14)], [V(1)]), Eqn([V(1)], [K(14)])]))
    C.append(dict(var="n", eq=Eqn([FR(3, V(1), K(1))], [FR(2, V(1), K(-1))], "n"),
                  lines=[Eqn([BR(2, V(1), K(1))], [BR(3, V(1), K(-1))], "n"), Eqn([V(2), K(1)], [V(3), K(-1)], "n"),
                         Eqn([V(1)], [K(2)], "n")],
                  err=1, moves=[("mul", 6), None, ("text", "$n$-тэй гишүүдийг баруун талд, тоог зүүн талд цуглуулсан",
                                                   "the $n$-terms are gathered on the right and the numbers on the left")],
                  why=("Хаалтуудыг нээхдээ зөвхөн $n$-ийг үржүүлжээ. $2(n + 1) = 2n + 2$, $3(n - 1) = 3n - 3$ байх ёстой.",
                       "Only the $n$ was multiplied when opening the brackets. It should be $2(n + 1) = 2n + 2$ and $3(n - 1) = 3n - 3$."),
                  rule=every_br,
                  fix=[Eqn([V(2), K(2)], [V(3), K(-3)], "n"), Eqn([V(1)], [K(5)], "n")]))
    C.append(dict(var="x", eq=Eqn([V("0.3"), K("1.5")], [V("0.2"), K(2)]),
                  lines=[Eqn([V(3), K(15)], [V(2), K(2)]), Eqn([V(1), K(15)], [K(2)]), Eqn([V(1)], [K(-13)])],
                  err=0, moves=[None, ("subvar", "2x"), ("subc", 15)],
                  why=(f"Хоёр талыг {W(10, 'ins')} үржүүлэхдээ аравтын бутархайг л үржүүлээд {W(2, 'acc')} үржүүлээгүй. "
                       "$3x + 15 = 2x + 20$ байх ёстой.",
                       "Multiplying by $10$, only the decimals were multiplied, not the $2$. It should be $3x + 15 = 2x + 20$."),
                  rule=("Хоёр талыг үржүүлэхдээ бүхэл тоотой гишүүнийг ч бас үржүүлнэ.",
                        "Multiplying both sides means every term, whole numbers included."),
                  fix=[Eqn([V(3), K(15)], [V(2), K(20)]), Eqn([V(1), K(15)], [K(20)]), Eqn([V(1)], [K(5)])]))
    return C



def find_error_variant(vid, i, c):
    v = c["var"]
    for ln in [c["eq"]] + c["lines"] + c["fix"]:
        ln.var = v
    eq, lines, err = c["eq"], c["lines"], c["err"]
    kind, sol = eq.solve()
    assert kind == "one"
    name_mn, name_en = NAMES[i % len(NAMES)]
    # the worked solution: every line before the error is equivalent to the
    # equation, the faulty line is not, and every later line follows from it
    chain = [eq] + lines
    for j, ln in enumerate(lines):
        prev = chain[j]
        if j < err:
            assert ln.solve() == ("one", sol), (vid, j)
        elif j == err:
            assert ln.solve() != ("one", sol), (vid, j)
        else:
            assert ln.solve() == prev.solve(), (vid, j)
    bat = lines[-1].solve()[1]
    assert not eq.holds(bat)
    for f in c["fix"]:
        assert f.solve() == ("one", sol)
    disp = "\\begin{aligned} " + " \\\\ ".join(
        f"({j + 1})\\quad {etex(ln.lhs, v)} &= {etex(ln.rhs, v)}" for j, ln in enumerate(lines)) + " \\end{aligned}"
    st_mn = f"{name_mn} {M(eq.tex())} тэгшитгэлийг дараах байдлаар бодсон: $${disp}$$ Аль алхамд алдсан бэ?"
    st_en = f"{name_en} solved ${eq.tex()}$ like this: $${disp}$$ In which step is the mistake?"
    opts_mn = ["1-р алхам", "2-р алхам", "3-р алхам", "Алдаа байхгүй"]
    opts_en = ["Step 1", "Step 2", "Step 3", "There is no mistake"]
    wrongs = []
    for j in range(3):
        if j == err:
            wrongs.append(None)
            continue
        mmn, men = mv_text(c["moves"][j], v)
        prev = "анхны тэгшитгэлээс" if j == 0 else f"{j}-р мөрөөс"
        prev_en = "the original equation" if j == 0 else f"line {j}"
        if j < err:
            wm = f"{j + 1}-р алхам зөв: {prev} {mmn}. Алдаа үүний дараа гарсан."
            we = f"Step {j + 1} is fine: from {prev_en}, {men}. The mistake comes later."
        else:
            wm = f"{j + 1}-р алхам өмнөх мөрөөсөө зөв гарсан: {mmn}. Гэвч өмнөх мөр нь буруу байсан."
            we = f"Step {j + 1} follows correctly from the line before: {men}. But that line was already wrong."
        wrongs.append((opts_mn[j], opts_en[j], wm, we, "misplaced-error"))
    Lb, Rb = ntexd(eval_side(eq.lhs, bat), eq.is_dec()), ntexd(eval_side(eq.rhs, bat), eq.is_dec())
    bt = f"{v} = {ntex(bat)}"
    wrongs.append((opts_mn[3], opts_en[3],
                   f"{name_mn}-ын хариу {M(bt)} утгыг анхны тэгшитгэлд орлуулбал зүүн тал {M(Lb)}, баруун тал {M(Rb)} гарч тэнцэхгүй. Иймд бодолтод алдаа бий."
                   .replace(f"{name_mn}-ын", {"Бат": "Батын", "Сарнай": "Сарнайн", "Тэмүүлэн": "Тэмүүлэнгийн", "Номин": "Номины",
                                              "Энхжин": "Энхжингийн", "Дорж": "Доржийн"}[name_mn]),
                   f"Putting {name_en}'s answer ${bt}$ into the original equation gives ${Lb}$ on the left and ${Rb}$ on the right. "
                   f"They are not equal, so there is a mistake somewhere.", "skipped-check"))
    opts = wrongs
    steps = []
    if err > 0:
        good = "; ".join(f"{j + 1}-р мөрөнд {mv_text(c['moves'][j], v)[0]}" for j in range(err))
        good_en = "; ".join(f"in line {j + 1} {mv_text(c['moves'][j], v)[1]}" for j in range(err))
        steps.append(dict(mn=dict(do=f"Мөр бүрийг өмнөх мөртэй нь харьцуулъя. {good[0].upper() + good[1:]}. Энд алдаа алга.",
                                  why="Мөр бүрд хоёр талд ижил, зөв үйлдэл хийсэн эсэхийг шалгана."),
                          en=dict(do=f"Compare each line with the one before. {good_en[0].upper() + good_en[1:]}. No mistake so far.",
                                  why="Each line must come from the one before by doing the same correct move to both sides.")))
    steps.append(dict(mn=dict(do=f"{err + 1}-р алхамд алдаа гарсан. {c['why'][0]}", why=c["rule"][0]),
                      en=dict(do=f"The mistake is in step {err + 1}. {c['why'][1]}", why=c["rule"][1])))
    fixes = ", ".join(M(f.tex()) for f in c["fix"])
    before = chain[err].tex()
    from_mn = "Анхны тэгшитгэлээс" if err == 0 else f"Алдаагүй сүүлийн мөр болох {M(before)} тэгшитгэлээс"
    from_en = "From the original equation" if err == 0 else f"From the last correct line ${before}$"
    steps.append(dict(mn=dict(do=f"{from_mn} эхлэн зөв бодъё: {fixes}."),
                      en=dict(do=f"{from_en}, solve it correctly: {fixes}.")))
    Lc, Rc = sub_chain(eq.lhs, v, sol, eq.is_dec()), sub_chain(eq.rhs, v, sol, eq.is_dec())
    pchecks = piece_checks(eq.lhs, sol) + piece_checks(eq.rhs, sol)
    st = f"{v} = {ntexd(sol, eq.is_dec())}"
    steps.append(dict(mn=dict(do=f"Шалгая: {M(st)} утгыг анхны тэгшитгэлд орлуулъя. Зүүн тал: {M(Lc)}. Баруун тал: {M(Rc)}. Хоёр тал тэнцүү."),
                      en=dict(do=f"Check: put ${st}$ into the original equation. Left side: ${Lc}$. Right side: ${Rc}$. Both sides are equal.")))
    hints = [("Мөр бүрийг өмнөх мөртэй нь харьцуулаарай. Хоёр талд ижил үйлдэл хийсэн үү, тэмдэг зөв үү?",
              "Compare each line with the one before it. Was the same move made on both sides, and are the signs right?"),
             (f"Эцсийн хариу {M(bt)} утгыг анхны тэгшитгэлд орлуулбал зүүн тал {M(Lb)}, баруун тал {M(Rb)} гарна. "
              f"Тэгэхээр алдаа бий. Аль мөрөөс эхлэн шийд нь өөрчлөгдсөнийг олоорой.",
              f"Putting the final answer ${bt}$ into the original equation gives ${Lb}$ and ${Rb}$, so there is a mistake. "
              f"Find the first line that no longer has the same solution.")]
    expl = (f"Алдаа {err + 1}-р алхамд байна. Зөв бодвол {M(st)} гарна.",
            f"The mistake is in step {err + 1}. Solved correctly, ${st}$.")
    checks = pchecks + [eq.check_at(sol), f"Ne({epy(eq.lhs, at(bat))}, {epy(eq.rhs, at(bat))})"]
    checks += [f.check_at(sol) for f in c["fix"]]
    for j, ln in enumerate(lines):
        if j < err:
            checks.append(ln.check_at(sol))
        elif j == err:
            checks.append(f"Ne({epy(ln.lhs, at(sol))}, {epy(ln.rhs, at(sol))})")
        checks.append(ln.check_at(bat) if j >= err else ln.check_at(sol))
    checks += [f"Eq({epy(eq.lhs, at(sol))}, {npy(eval_side(eq.lhs, sol))})",
               f"Eq({epy(eq.rhs, at(sol))}, {npy(eval_side(eq.rhs, sol))})",
               f"Eq({epy(eq.lhs, at(bat))}, {npy(eval_side(eq.lhs, bat))})",
               f"Eq({epy(eq.rhs, at(bat))}, {npy(eval_side(eq.rhs, bat))})"]
    return assemble(vid, i, st_mn, st_en, (opts_mn[err], opts_en[err]), opts, steps, hints, expl, checks, fixed_ci=err)


def how_many_variant(vid, i, eq):
    v = eq.var
    kind, sol = eq.solve()
    cat = {"one": "one", "none": "none", "all": "inf"}[kind]
    cur, pre_steps = eq, []
    checks = []
    if any(p.kind == "br" for p in cur.lhs + cur.rhs):
        nxt, shows, _ = expand(cur)
        for p in cur.lhs + cur.rhs:
            if p.kind == "br":
                checks.append(equiv_check([p], expand_piece(p), v))
        cur2, shows2, _ = combine(nxt) if (needs_combine(nxt.lhs) or needs_combine(nxt.rhs)) else (nxt, [], None)
        cur = cur2
        allshow = ", ".join(M(s) for s in shows + shows2)
        pre_steps.append(dict(mn=dict(do=f"Хаалтыг нээж, тал бүрийг хялбарчилъя: {allshow}. Тэгшитгэл {M(cur.tex())} болно.",
                                      why="Хялбарчлахаас өмнө тэгшитгэл хэдэн шийдтэй болохыг харахад хэцүү."),
                              en=dict(do=f"Open the brackets and simplify each side: {allshow}. The equation becomes ${cur.tex()}$.",
                                      why="Before simplifying it is hard to see how many solutions there are.")))
    elif needs_combine(cur.lhs) or needs_combine(cur.rhs):
        cur, shows, _ = combine(cur)
        pre_steps.append(dict(mn=dict(do=f"Тал бүрт төсөөтэй гишүүдийг нэгтгэе: {', '.join(M(s) for s in shows)}. Тэгшитгэл {M(cur.tex())} болно.",
                                      why="Хялбарчлахаас өмнө тэгшитгэл хэдэн шийдтэй болохыг харахад хэцүү."),
                              en=dict(do=f"Combine like terms on each side: {', '.join(M(s) for s in shows)}. The equation becomes ${cur.tex()}$.",
                                      why="Before simplifying it is hard to see how many solutions there are.")))
    checks += [equiv_check(eq.lhs, cur.lhs, v), equiv_check(eq.rhs, cur.rhs, v)]
    a1, b1 = coeffs(cur.lhs)
    a2, b2 = coeffs(cur.rhs)
    simp = cur.tex()
    steps = list(pre_steps)
    if cat == "one":
        w = Walk(cur)
        tail = w.steps[:-1]
        steps.append(dict(mn=dict(do=f"{VW(v, v, 'gen')} коэффициент зүүн талд {M(ntex(a1))}, баруун талд {M(ntex(a2))} байна. Ялгаатай тул {M(v)} хорогдохгүй, тэгшитгэл яг нэг шийдтэй.",
                                  why="Коэффициентууд ялгаатай бол хоёр талаас ижил гишүүн хасахад үл мэдэгдэх үлдэнэ."),
                          en=dict(do=f"The coefficient of ${v}$ is ${ntex(a1)}$ on the left and ${ntex(a2)}$ on the right. They differ, so ${v}$ does not cancel and there is exactly one solution.",
                                  why="With different coefficients the unknown survives when you subtract, so it can be solved for.")))
        # solve it briefly in one step
        st = f"{v} = {ntex(sol)}"
        steps.append(dict(mn=dict(do=f"Бодвол {', '.join(M(c) for c in w.chain)} гарна." if w.chain else f"Бодвол {M(st)}."),
                          en=dict(do=f"Solving gives {', '.join('$' + c + '$' for c in w.chain)}." if w.chain else f"Solving gives ${st}$.")))
        checks += w.checks
        Lc, Rc = sub_chain(eq.lhs, v, sol), sub_chain(eq.rhs, v, sol)
        checks += piece_checks(eq.lhs, sol) + piece_checks(eq.rhs, sol)
        steps.append(dict(mn=dict(do=f"Шалгая: {M(st)} үед зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Хоёр тал тэнцүү."),
                          en=dict(do=f"Check: at ${st}$ the left side is ${Lc}$ and the right side is ${Rc}$. Both sides are equal.")))
        checks.append(eq.check_at(sol))
    else:
        t = etex([V(a1)], v)
        rest = f"{ntex(b1)} = {ntex(b2)}"
        sub_mn = f"Хоёр талаас {VW(t, v, 'acc')} хасъя" if a1 > 0 else f"Хоёр талд {VW(etex([V(-a1)], v), v, 'acc')} нэмье"
        sub_en = f"Subtract ${t}$ from both sides" if a1 > 0 else f"Add ${etex([V(-a1)], v)}$ to both sides"
        steps.append(dict(mn=dict(do=f"Хоёр талын {VW(v, v, 'gen')} коэффициент тэнцүү ({M(ntex(a1))}). {sub_mn}: {M(v)} алга болж {M(rest)} үлдэнэ.",
                                  why=f"Коэффициентууд тэнцүү бол {VW(v, v, 'com')} гишүүд бүрэн хорогдоно. Үлдсэн тэнцэтгэл үнэн эсэхээс хариу шалтгаална."),
                          en=dict(do=f"Both sides have the same coefficient of ${v}$ (${ntex(a1)}$). {sub_en}: ${v}$ disappears and ${rest}$ is left.",
                                  why=f"With equal coefficients the ${v}$-terms cancel completely. The answer depends on whether what is left is true.")))
        checks.append(f"Eq({npy(a1)}, {npy(a2)})")
        if cat == "none":
            steps.append(dict(mn=dict(do=f"{M(rest)} худал. {VW(v, v, 'gen')} ямар ч утгад хоёр тал тэнцэхгүй тул тэгшитгэл шийдгүй."),
                              en=dict(do=f"${rest}$ is false. No value of ${v}$ can make the sides equal, so there is no solution.")))
            checks.append(f"Ne({npy(b1)}, {npy(b2)})")
            tests = [Fr(0), Fr(1)]
        else:
            steps.append(dict(mn=dict(do=f"{M(rest)} үргэлж үнэн. {VW(v, v, 'gen')} дурын утга тохирох тул тэгшитгэл төгсгөлгүй олон шийдтэй. Ийм тэгшитгэлийг адилтгал гэнэ."),
                              en=dict(do=f"${rest}$ is always true. Every value of ${v}$ works, so there are infinitely many solutions. Such an equation is called an identity.")))
            checks.append(f"Eq({npy(b1)}, {npy(b2)})")
            tests = [Fr(0), Fr(2)]
        parts_mn, parts_en = [], []
        for x in tests:
            Lc, Rc = sub_chain(eq.lhs, v, x), sub_chain(eq.rhs, v, x)
            checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
            parts_mn.append(f"{M(f'{v} = {ntex(x)}')} үед зүүн тал {M(Lc)}, баруун тал {M(Rc)}")
            parts_en.append(f"at ${v} = {ntex(x)}$ the left side is ${Lc}$ and the right side ${Rc}$")
            checks.append(f"Eq({epy(eq.lhs, at(x))}, {npy(eval_side(eq.lhs, x))})")
            checks.append(f"Eq({epy(eq.rhs, at(x))}, {npy(eval_side(eq.rhs, x))})")
        if cat == "none":
            steps.append(dict(mn=dict(do=f"Шалгая: {'; '.join(parts_mn)}. Хоёр талын зөрүү үргэлж {M(ntex(abs(b1 - b2)))} хэвээр."),
                              en=dict(do=f"Check: {'; '.join(parts_en)}. The sides always differ by ${ntex(abs(b1 - b2))}$.")))
        else:
            steps.append(dict(mn=dict(do=f"Шалгая: {'; '.join(parts_mn)}. Ямар ч утга авсан хоёр тал тэнцүү."),
                              en=dict(do=f"Check: {'; '.join(parts_en)}. Whatever value you take, the sides are equal.")))
    # options in a fixed order (they read as a scale), the zero trap last
    zero = f"{v} = 0"
    opts_mn = ["Яг нэг шийдтэй", "Шийдгүй", "Төгсгөлгүй олон шийдтэй", f"Ганц шийд нь {M(zero)}"]
    opts_en = ["Exactly one solution", "No solution", "Infinitely many solutions", f"The only solution is ${zero}$"]
    ci = {"one": 0, "none": 1, "inf": 2}[cat]
    assert not (cat == "one" and sol == 0)
    L0, R0 = ntex(eval_side(eq.lhs, Fr(0))), ntex(eval_side(eq.rhs, Fr(0)))
    rest = f"{ntex(b1)} = {ntex(b2)}"
    pre_mn = "Хялбарчлахаас өмнө дүгнэсэн бололтой. "
    pre_en = "It looks as if the decision came before simplifying. "
    D = {}
    if cat == "one":
        D[1] = (pre_mn + f"Хялбарчилбал {M(simp)} болж {VW(v, v, 'gen')} коэффициентууд {M(ntex(a1))} ба {M(ntex(a2))} ялгаатай. Иймд {M(v)} хорогдохгүй, тэгшитгэл яг нэг шийдтэй.",
                pre_en + f"Simplified it reads ${simp}$, and the coefficients ${ntex(a1)}$ and ${ntex(a2)}$ differ, so ${v}$ does not cancel and there is one solution.")
        D[2] = (f"Төгсгөлгүй олон шийд гарахын тулд хялбарчилсны дараа хоёр тал яг ижил болох ёстой. Энд {M(simp)} болж хоёр тал ялгаатай, коэффициентууд ч өөр.",
                f"For infinitely many solutions the two sides must be identical after simplifying. Here ${simp}$: the sides differ, even in the coefficient of ${v}$.")
        D[3] = (f"Нэг шийдтэй гэдэг нь зөв, гэхдээ тэр шийд {M(0)} биш. {M(zero)} үед зүүн тал {M(L0)}, баруун тал {M(R0)} гарч тэнцэхгүй. Бодвол {M(f'{v} = {ntex(sol)}')}.",
                f"One solution is right, but it is not $0$. At ${zero}$ the left side is ${L0}$ and the right side ${R0}$. Solving gives ${v} = {ntex(sol)}$.")
    elif cat == "none":
        D[0] = (pre_mn + f"Хялбарчилбал {M(simp)} болно. Коэффициентууд тэнцүү тул {M(v)} хорогдож, {M(rest)} гэсэн худал тэнцэтгэл үлдэнэ. Нэг ч шийд гарахгүй.",
                pre_en + f"Simplified it reads ${simp}$. The coefficients are equal, so ${v}$ cancels and the false statement ${rest}$ is left: no solution at all.")
        D[2] = (f"{M(v)} алга болсныг хараад төгсгөлгүй олон шийдтэй гэж дүгнэсэн байх. Гэвч үлдсэн {M(rest)} худал тул {VW(v, v, 'gen')} ямар ч утга тохирохгүй.",
                f"Seeing ${v}$ disappear, it is tempting to say «infinitely many». But what is left, ${rest}$, is false, so no value works.")
        D[3] = (f"{M(v)} алга болохыг {M(zero)} гэж ойлгох нь түгээмэл алдаа. {M(zero)} үед зүүн тал {M(L0)}, баруун тал {M(R0)} гарч тэнцэхгүй. Үлдсэн {M(rest)} худал тул шийд байхгүй.",
                f"Reading «${v}$ disappears» as «${zero}$» is a common mistake. At ${zero}$ the sides are ${L0}$ and ${R0}$. What is left, ${rest}$, is false: no solution.")
    else:
        D[0] = (pre_mn + f"Хялбарчилбал {M(simp)} болж хоёр тал яг ижил. {VW(v, v, 'gen')} дурын утга тохирно.",
                pre_en + f"Simplified it reads ${simp}$: the two sides are identical, so every value of ${v}$ works.")
        D[1] = (f"{M(v)} алга болсныг «шийд байхгүй» гэж ойлгосон байх. Үлдсэн {M(rest)} үргэлж үнэн тул {VW(v, v, 'gen')} дурын утга шийд болно.",
                f"${v}$ disappearing was read as «no solution». But what is left, ${rest}$, is always true, so every value is a solution.")
        D[3] = (f"{M(zero)} үнэхээр тохирно, гэхдээ ганцаараа биш. Хоёр тал адилхан {M(etex(cur.lhs, v))} тул {VW(v, v, 'gen')} дурын утга шийд болно.",
                f"${zero}$ does work, but it is not the only one. Both sides are the same ${etex(cur.lhs, v)}$, so every value is a solution.")
    HM_TAG = {("one", 1): "decided-before-simplifying", ("one", 2): "decided-before-simplifying",
              ("one", 3): "one-solution-assumed-zero", ("none", 0): "decided-before-simplifying",
              ("none", 2): "cancelled-means-infinite", ("none", 3): "cancelled-means-x-zero",
              ("inf", 0): "decided-before-simplifying", ("inf", 1): "cancelled-means-no-solution",
              ("inf", 3): "cancelled-means-x-zero"}
    opts = [None if j == ci else (opts_mn[j], opts_en[j], D[j][0], D[j][1], HM_TAG[(cat, j)]) for j in range(4)]
    hints = [(f"Эхлээд хаалтыг нээж, тал бүрийг хялбарчлаарай. Дараа нь хоёр талын {VW(v, v, 'gen')} коэффициентыг харьцуулаарай.",
              f"First open any brackets and simplify each side. Then compare the coefficients of ${v}$ on the two sides."),
             (f"Хялбарчилбал {M(simp)} болно. Хоёр талын {VW(v, v, 'gen')} коэффициент ижил үү, ялгаатай юу?",
              f"Simplified it reads ${simp}$. Are the coefficients of ${v}$ the same or different?")]
    if cat == "one":
        expl = (f"Хялбарчилбал {M(simp)} болж коэффициентууд ялгаатай. Иймд яг нэг шийдтэй: {M(f'{v} = {ntex(sol)}')}.",
                f"Simplified it reads ${simp}$ and the coefficients differ, so there is exactly one solution: ${v} = {ntex(sol)}$.")
    elif cat == "none":
        expl = (f"Хялбарчилбал {M(simp)} болно. {M(v)} хорогдоход {M(rest)} гэсэн худал тэнцэтгэл үлдэх тул шийдгүй.",
                f"Simplified it reads ${simp}$. With ${v}$ cancelled the false statement ${rest}$ is left, so there is no solution.")
    else:
        expl = (f"Хялбарчилбал {M(simp)} болж хоёр тал ижил. Иймд төгсгөлгүй олон шийдтэй.",
                f"Simplified it reads ${simp}$: both sides are identical, so there are infinitely many solutions.")
    st_mn = f"{M(eq.tex())} тэгшитгэл хэдэн шийдтэй вэ?"
    st_en = f"How many solutions does ${eq.tex()}$ have?"
    assert 3 <= len(steps) <= 6, (vid, len(steps))
    return assemble(vid, i, st_mn, st_en, (opts_mn[ci], opts_en[ci]), opts, steps, hints, expl, checks, fixed_ci=ci)


# ---------------------------------------------------------------------------
# WORKSHEET TEMPLATES
#
# Owner feedback (Khas, 9 Nov 2026): "the practice problems are too monotonic
# … the problem bank should have variety of problems, just like how you
# generate it for my students". So a form is a worksheet: twelve problems in
# at least six different SHAPES (a bare equation, a box to fill, a table, a
# picture to read, a story, "which equation", "who is right", "what is the
# next step"…), each shape at most three times and never twice in a row.
# Every template below still carries the full tutoring: two hints, a solution
# step by step, and a diagnosis for each wrong option produced by one named
# mistake.
# ---------------------------------------------------------------------------

VSUF["k"] = {"gen": "гийн", "acc": "г", "com": "тай", "abl": "гаас"}
VSUF["t"] = {"gen": "гийн", "acc": "г", "com": "тэй", "abl": "гээс"}
VSUF["w"] = {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"}
VSUF["g"] = {"gen": "гийн", "acc": "г", "com": "тэй", "abl": "гээс"}
VSUF["d"] = {"gen": "гийн", "acc": "г", "com": "тэй", "abl": "гээс"}
VSUF["h"] = {"gen": "ийн", "acc": "ийг", "com": "тэй", "abl": "ээс"}
VSUF["v"] = {"gen": "гийн", "acc": "г", "com": "тэй", "abl": "гээс"}

GEN = {"Бат": "Батын", "Сарнай": "Сарнайн", "Тэмүүлэн": "Тэмүүлэнгийн", "Номин": "Номины",
       "Энхжин": "Энхжингийн", "Дорж": "Доржийн"}


def with_fig(pair, fig_en, fig_mn):
    e, m = pair
    assert fig_en["mode"] == fig_mn["mode"]
    e["figure"], m["figure"] = fig_en, fig_mn
    return e, m


def walk_wrongs(w, order, extra=()):
    cands = w.mistakes(order) + list(extra)
    ms = pick3(w.sol, cands, w.dec)
    checks = []
    for m in ms:
        checks += m.get("checks", [])
    return ms, checks


# ----- bare equation -------------------------------------------------------

def t_bare(vid, i, eq, order, hint1):
    st_mn, st_en = solve_stmt(eq)
    return numeric_variant(vid, i, eq, st_mn, st_en, order, hint1)


# ----- what goes in the box -----------------------------------------------

def box_tex(eq):
    assert eq.var == "x"
    t = re.sub(r"(\d)x", lambda mo: mo.group(1) + " \\cdot \\square", eq.tex())
    return t.replace("x", "\\square")


def t_box(vid, i, eq, order):
    w = Walk(eq, extra_steps=1)
    ms, mchecks = walk_wrongs(w, order)
    bt = box_tex(eq)
    ans = ntexd(w.sol, w.dec)
    first = dict(mn=dict(do=f"Нүдэнд орох тоог $x$ гэж тэмдэглэе. Тэгвэл {M(eq.tex())} тэгшитгэл гарна.",
                         why="Мэдэгдэхгүй тоог үсгээр тэмдэглэвэл түүнийг тэгшитгэл бодож олно."),
                 en=dict(do=f"Call the number in the box $x$. Then the equation is ${eq.tex()}$.",
                         why="Naming the unknown number with a letter turns the puzzle into an equation to solve."))
    steps = [first] + w.steps
    steps[-1] = dict(mn=dict(do=steps[-1]["mn"]["do"] + f" Нүдэнд {M(ans)} бичнэ."),
                     en=dict(do=steps[-1]["en"]["do"] + f" The box holds ${ans}$."))
    hints = [("Нүдийг үл мэдэгдэх тоо гэж үзээд $x$ гэж тэмдэглээрэй. Тэгвэл энгийн тэгшитгэл болно.",
              "Treat the box as an unknown number and call it $x$: it becomes an ordinary equation."),
             hint2_from(w.steps[0], "x")]
    wrongs = [(M(ntexd(m["x"], w.dec)),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    expl = (f"Нүдийг $x$ гэвэл {M(eq.tex())}. Бодоход {M('x = ' + ans)} тул нүдэнд {M(ans)} бичнэ.",
            f"With the box as $x$ the equation is ${eq.tex()}$. It gives $x = {ans}$, so the box holds ${ans}$.")
    return assemble(vid, i, f"Нүдэнд ямар тоо бичвэл тэнцэтгэл үнэн болох вэ? $${bt}$$",
                    f"Which number in the box makes this true? $${bt}$$",
                    (M(ans),) * 2, wrongs, steps, hints, expl, w.checks + mchecks)


# ----- which equation has this solution (optionally read off a number line) -

def trap(kind, a, b, s, var):
    """An equation that a NAMED mistake would wrongly 'solve' to s."""
    s = Fr(s)
    if kind == "const":       # a·x + b = c, solved by moving b without its sign change
        eq = Eqn([V(a), K(b)], [K(a * s - b)], var)
        ph = (f"{W(b, 'acc')} нөгөө тал руу тэмдгийг нь өөрчлөхгүй шилжүүлбэл",
              f"moving ${ntex(b)}$ across without changing its sign", "sign-not-changed-moving-term")
    elif kind == "nodiv":     # a·x + b = c with c − b = s: forgetting to divide by a
        eq = Eqn([V(a), K(b)], [K(s + b)], var)
        ph = (f"сүүлд нь {W(a, 'dat')} хуваахаа мартвал", f"forgetting the final division by ${a}$", "stopped-before-dividing")
    else:                     # k(x + p) = c with k·x + p = c
        eq = Eqn([BR(a, V(1), K(b))], [K(a * s + b)], var)
        ph = (f"хаалтыг нээхдээ зөвхөн {VW(var, var, 'acc')} {W(a, 'ins')} үржүүлбэл",
              f"multiplying only the ${var}$ in the bracket by ${a}$", "distribute-first-term-only")
    kind_, t = eq.solve()
    assert kind_ == "one" and t != s, (kind, a, b, s)
    return eq, ph, t


def t_which_eq(vid, i, s, var, correct, traps, line=None):
    """Options are equations; exactly one has solution s. `line` = (min, max) draws s on a number line."""
    s = Fr(s)
    assert correct.solve() == ("one", s)
    st = f"{var} = {ntex(s)}"
    eqs = [(correct, None, None)] + [trap(k, a, b, s, var) for k, a, b in traps]
    ci = i % 4
    order = [1, 2, 3]
    order.insert(ci, 0)
    checks, wrongs, opt_steps = [], [], []
    for j in order:
        eq, ph, t = eqs[j]
        L, R = eval_side(eq.lhs, s), eval_side(eq.rhs, s)
        Lc, Rc = sub_chain(eq.lhs, var, s), sub_chain(eq.rhs, var, s)
        checks += piece_checks(eq.lhs, s) + piece_checks(eq.rhs, s)
        if j == 0:
            checks.append(eq.check_at(s))
            last = dict(mn=dict(do=f"{M(eq.tex())}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Тэнцүү тул энэ тэгшитгэлийн шийд нь {M(st)}."),
                        en=dict(do=f"${eq.tex()}$: left side ${Lc}$, right side ${Rc}$. Equal, so this equation has solution ${st}$."))
            wrongs.append(None)
        else:
            checks += [f"Ne({epy(eq.lhs, at(s))}, {epy(eq.rhs, at(s))})", eq.check_at(t)]
            opt_steps.append(dict(mn=dict(do=f"{M(eq.tex())}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Тэнцэхгүй."),
                                  en=dict(do=f"${eq.tex()}$: left side ${Lc}$, right side ${Rc}$. Not equal.")))
            wrongs.append((M(eq.tex()), M(eq.tex()),
                           f"{M(st)} утгыг орлуулбал зүүн тал {M(ntex(L))}, баруун тал {M(ntex(R))} гарч тэнцэхгүй. "
                           f"Энэ тэгшитгэлийг {ph[0]} {M(st)} гэж андуурч гардаг. Жинхэнэ шийд нь {M(f'{var} = {ntex(t)}')}.",
                           f"Substituting ${st}$ gives ${ntex(L)}$ on the left and ${ntex(R)}$ on the right. This equation "
                           f"only seems to give ${st}$ by {ph[1]}; its real solution is ${var} = {ntex(t)}$.", ph[2]))
    intro_mn = (f"Тоон шулуун дээр {M(ntex(s))} тоо тэмдэглэгдсэн байна. " if line else "") + \
        f"Тэгшитгэл бүрийг бодох шаардлагагүй: {M(st)} утгыг орлуулж, хоёр тал тэнцүү эсэхийг шалгая."
    intro_en = (f"The number line marks ${ntex(s)}$. " if line else "") + \
        f"No need to solve each equation: substitute ${st}$ and see which one balances."
    steps = [dict(mn=dict(do=intro_mn, why="Шийд гэдэг нь тэгшитгэлийг үнэн тэнцэтгэл болгодог утга."),
                  en=dict(do=intro_en, why="A solution is the value that makes the equation true."))] + opt_steps + [last]
    first_wrong = eqs[order[0] if order[0] != 0 else order[1]][0]
    hints = [(f"Тэгшитгэл бүрийг бодохын оронд {M(st)} утгыг орлуулаад хоёр тал тэнцэх эсэхийг шалгаарай.",
              f"Instead of solving each one, substitute ${st}$ and check whether the two sides match."),
             (f"Жишээ нь {M(first_wrong.tex())} тэгшитгэлд зүүн тал {M(ntex(eval_side(first_wrong.lhs, s)))}, баруун тал "
              f"{M(ntex(eval_side(first_wrong.rhs, s)))} гарна. Бусдыг ингэж шалгаарай.",
              f"For example ${first_wrong.tex()}$ gives ${ntex(eval_side(first_wrong.lhs, s))}$ and "
              f"${ntex(eval_side(first_wrong.rhs, s))}$. Check the others the same way.")]
    expl = (f"{M(st)} утгыг орлуулахад зөвхөн {M(correct.tex())} тэгшитгэлийн хоёр тал тэнцүү гарна. Бусад тэгшитгэлийн хоёр тал тэнцэхгүй.",
            f"Substituting ${st}$ balances only ${correct.tex()}$. The other equations do not balance.")
    opts = [None if w is None else w for w in wrongs]
    if line:
        st_mn = "Тоон шулуун дээр тэмдэглэсэн тоо аль тэгшитгэлийн шийд вэ?"
        st_en = "The number marked on the number line is the solution of which equation?"
    else:
        st_mn = f"Аль тэгшитгэлийн шийд нь {M(st)} вэ?"
        st_en = f"Which equation has the solution ${st}$?"
    pair = assemble(vid, i, st_mn, st_en, (M(correct.tex()),) * 2, opts, steps, hints, expl, checks, fixed_ci=ci)
    if line:
        lo, hi = line
        assert lo <= s <= hi and s.denominator == 1
        fig = {"mode": "integerLine", "integerLine": {"min": lo, "max": hi, "points": [{"value": int(s), "label": "?"}]}}
        pair = with_fig(pair, fig, json.loads(json.dumps(fig)))
    return pair


# ----- for which k does the equation have solution s ----------------------

def t_param(vid, i, shown, s, keq, order, extra=(), var="x"):
    """shown: (tex, py-template with {x} and {k}) of an equation in x with a parameter k; keq: the k-equation."""
    tex, tpl = shown
    w = Walk(keq, extra_steps=1)
    kv = w.sol
    lhs_t, rhs_t = tpl.split("=")
    for xv, kk in ((s, kv),):
        L = sp.sympify(lhs_t.format(x=f"({npy(xv)})", k=f"({npy(kk)})"))
        R = sp.sympify(rhs_t.format(x=f"({npy(xv)})", k=f"({npy(kk)})"))
        assert L == R, (tex, L, R)
    K_ = sp.Symbol("k")
    d = sp.expand(sp.sympify(lhs_t.format(x=f"({npy(s)})", k="k")) - sp.sympify(rhs_t.format(x=f"({npy(s)})", k="k")))
    A_, B_ = keq.diff()
    assert sp.simplify(d * A_ - sp.expand(sp.Rational(A_) * K_ + B_) * d.coeff(K_, 1)) == 0
    ex = []
    for xv, mn, en, tag_ in extra:
        ex.append(dict(x=Fr(xv), mn=mn, en=en, mode="extra", tag=tag_,
                       checks=[f"Ne({lhs_t.format(x=at(s), k=at(Fr(xv)))}, {rhs_t.format(x=at(s), k=at(Fr(xv)))})"]))
    ms, mchecks = walk_wrongs(w, order, ex)
    xs = f"{var} = {ntex(s)}"
    first = dict(mn=dict(do=f"Шийд нь {M(xs)} гэдэг нь {VW(var, var, 'gen')} оронд {M(ntex(s))} тавихад тэнцэтгэл үнэн болно гэсэн үг. "
                            f"Орлуулбал {M(keq.tex())}.",
                         why=f"Одоо {M(var)} мэдэгдэж байгаа тул үл мэдэгдэх нь ганцхан {M('k')} үлдэнэ."),
                 en=dict(do=f"Having solution ${xs}$ means the equation is true when ${ntex(s)}$ replaces ${var}$. "
                            f"Substituting gives ${keq.tex()}$.",
                         why=f"Now ${var}$ is known, so the only unknown left is $k$."))
    steps = [first] + w.steps
    kt = f"k = {ntex(kv)}"
    steps[-1] = dict(mn=dict(do=steps[-1]["mn"]["do"] + f" Иймд {M(kt)} үед тэгшитгэлийн шийд {M(xs)} болно."),
                     en=dict(do=steps[-1]["en"]["do"] + f" So with ${kt}$ the equation has solution ${xs}$."))
    checks = w.checks + mchecks + [f"Eq({lhs_t.format(x=at(s), k=at(kv))}, {rhs_t.format(x=at(s), k=at(kv))})"]
    hints = [(f"{VW(var, var, 'gen')} оронд {M(ntex(s))} тавиарай. Тэгвэл {M('k')}-тай энгийн тэгшитгэл үлдэнэ.",
              f"Put ${ntex(s)}$ in place of ${var}$. What is left is a simple equation in $k$."),
             (f"Орлуулбал {M(keq.tex())} болно. Одоо {M('k')}-г олоорой.", f"Substituting gives ${keq.tex()}$. Now find $k$.")]
    wrongs = [(M(ntex(m["x"])),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    expl = (f"{M(xs)} утгыг орлуулбал {M(keq.tex())}, эндээс {M(kt)}.",
            f"Substituting ${xs}$ gives ${keq.tex()}$, so ${kt}$.")
    return assemble(vid, i, f"{VW('k', 'k', 'gen')} ямар утгад {M(tex)} тэгшитгэлийн шийд {M(xs)} болох вэ?",
                    f"For which value of $k$ does ${tex}$ have the solution ${xs}$?",
                    (M(ntex(kv)),) * 2, wrongs, steps, hints, expl, checks)


# ----- what is the next step ----------------------------------------------

def t_next(vid, i, eq0, line, name=None, drill=False):
    """Options are moves. The right one is the move the solving walk makes next on `line`."""
    v = eq0.var
    assert line.solve() == eq0.solve()
    w = Walk(line, extra_steps=1)
    nxt = w.stage_eqs[0]
    sides = line.lhs + line.rhs
    if any(p.kind == "fr" for p in sides) or any(p.dec for p in sides if p.kind in "vk"):
        Mx, _, _, _ = clear(line)
        if line.is_dec():
            alt = 10 if Mx == 100 else 100
            alt_d = (f"{W(alt, 'ins')} үржүүлбэл {'бүх тоо бүхэл болохгүй' if alt < Mx else 'тоо шаардлагагүй томорно'}: "
                     f"таслалаас хойш хамгийн олон оронтой тоог харж {W(Mx, 'ins')} үржүүлнэ.",
                     f"Multiplying by ${alt}$ {'leaves some decimals' if alt < Mx else 'makes the numbers needlessly big'}: "
                     f"the number with the most decimal places decides, so multiply by ${Mx}$.")
        else:
            dens = sorted({p.den for p in sides if p.kind == "fr"})
            alt = sum(dens)
            assert alt % Mx != 0 or alt == Mx
            alt = alt if alt != Mx else Mx * 2
            alt_d = (f"{W(alt, 'ins')} үржүүлбэл хуваарь бүр түүнд хуваагдахгүй тул бутархай үлдэнэ. Хуваариудын хамгийн бага "
                     f"ерөнхий хуваарь {M(Mx)}.",
                     f"Not every denominator divides ${alt}$, so fractions would remain. The least common denominator is ${Mx}$.")
        _, part, _, left = clear(line, partial=True)
        if left:
            part_o = (f"Зөвхөн бутархайтай гишүүдийг {W(Mx, 'ins')} үржүүлэх", f"Multiply only the fraction terms by ${Mx}$")
            part_d = (f"Ингэвэл {M(part.tex())} болж тэнцэтгэл алдагдана: хоёр талын гишүүн бүрийг ижил тоогоор үржүүлэх ёстой.",
                      f"That gives ${part.tex()}$, which is no longer balanced: every term on both sides must be multiplied.")
        else:
            part_o = (f"Зөвхөн зүүн талыг {W(Mx, 'ins')} үржүүлэх", f"Multiply only the left side by ${Mx}$")
            part_d = ("Нэг талыг л үржүүлбэл тэнцэтгэл алдагдана. Хоёр талыг ижил тоогоор үржүүлэх ёстой.",
                      "Multiplying one side only breaks the balance. Both sides must be multiplied by the same number.")
        # dropping the denominators / decimal points: each term scaled by its own number
        def own(p):
            if p.kind == "fr":
                inner = [q.copy() for q in p.inner]
                return [q.copy(c=q.c * (1 if p.c > 0 else -1)) for q in inner] if len(inner) > 1 else \
                    [inner[0].copy(c=inner[0].c * p.c)]
            if p.kind in "vk" and p.dec:
                k = 0
                while (p.c * 10 ** k).denominator != 1:
                    k += 1
                return [p.copy(c=p.c * 10 ** k, dec=False)]
            return [p.copy()]
        drop = Eqn([q for p in line.lhs for q in own(p)], [q for p in line.rhs for q in own(p)], v)
        assert drop.solve() != line.solve()
        if line.is_dec():
            drop_o = (f"Таслалыг зүгээр арилгах: {M(drop.tex())}", f"Just delete the decimal points: ${drop.tex()}$")
            drop_d = ("Таслалыг арилгахад гишүүн бүр өөр өөр тоогоор үржигдэнэ, тэгэхээр тэнцэтгэл алдагдана.",
                      "Deleting the points multiplies different terms by different numbers, so the balance is lost.")
        else:
            drop_o = (f"Хуваарийг зүгээр хаях: {M(drop.tex())}", f"Just drop the denominators: ${drop.tex()}$")
            drop_d = ("Хуваарийг хаяхад гишүүн бүр өөр өөр тоогоор үржигдэнэ, тэгэхээр тэнцэтгэл алдагдана.",
                      "Dropping the denominators multiplies different terms by different numbers, so the balance is lost.")
        right = (f"Хоёр талын гишүүн бүрийг {W(Mx, 'ins')} үржүүлэх", f"Multiply every term on both sides by ${Mx}$")
        wrongs = [(f"Хоёр талыг {W(alt, 'ins')} үржүүлэх", f"Multiply both sides by ${alt}$") + alt_d + ("wrong-common-denominator",),
                  part_o + part_d + ("multiplied-some-terms-only",), drop_o + drop_d + ("dropped-denominators",)]
        reason = ("Тэгшитгэлд бутархай байгаа тул эхлээд бутархайгаас салвал бусад алхам хялбар болно."
                  if not line.is_dec() else "Аравтын бутархайгаас эхлээд салвал бүхэл тоотой бодно.",
                  "There are fractions, so getting rid of them first makes every later step easier."
                  if not line.is_dec() else "Clearing the decimals first lets you work with whole numbers.")
        checks = [f"Ne(({epy(part.lhs, at(w.sol))}) - ({epy(part.rhs, at(w.sol))}), 0)" if part.solve() != line.solve() else "True"]
    elif any(p.kind == "br" for p in sides):
        br = next(p for p in sides if p.kind == "br" and p.c != 1 and len(p.inner) > 1)
        good = etex(expand_piece(br), v)
        fo = etex(expand_piece(br, "first_only"), v)
        bt = etex([br], v)
        right = (f"Хаалтыг нээх: {M(bt + ' = ' + good)}", f"Open the bracket: ${bt} = {good}$")
        wrongs = [(f"Хаалтыг нээх: {M(bt + ' = ' + fo)}", f"Open the bracket: ${bt} = {fo}$",
                   f"Энд хаалтын өмнөх {M(ntex(br.c))} зөвхөн эхний гишүүнийг үржүүлжээ. Хаалтан доторх гишүүн бүрийг үржүүлнэ: {M(bt + ' = ' + good)}.",
                   f"Here ${ntex(br.c)}$ multiplies only the first term. It multiplies every term inside: ${bt} = {good}$.",
                   "distribute-first-term-only")]
        if br.c < 0:
            ns = etex(expand_piece(br, "neg_sign"), v)
            wrongs.append((f"Хаалтыг нээх: {M(bt + ' = ' + ns)}", f"Open the bracket: ${bt} = {ns}$",
                           f"Хасах тэмдэгтэй {W(br.c, 'ins')} үржүүлэхэд хоёр дахь гишүүний тэмдэг ч өөрчлөгдөнө: {M(bt + ' = ' + good)}.",
                           f"Multiplying by the negative ${ntex(br.c)}$ changes the second term's sign too: ${bt} = {good}$.",
                           "distribute-sign-second-term"))
        q = br.inner[-1]
        qt = ntex(abs(q.c))
        if q.c > 0:
            q_mn, q_en = f"Хаалтан доторх {W(abs(q.c), 'acc')} хоёр талаас хасах", f"Subtract the ${qt}$ inside the bracket from both sides"
        else:
            q_mn, q_en = f"Хаалтан доторх {W(abs(q.c), 'acc')} хоёр талд нэмэх", f"Add the ${qt}$ inside the bracket to both sides"
        wrongs.append((q_mn, q_en,
                       f"{M(qt)} нь хаалтан дотор байгаа тул {W(br.c, 'ins')} үржигдсэн байна. Түүнийг дангаар нь шилжүүлж болохгүй: эхлээд хаалтыг нээнэ.",
                       f"The ${qt}$ is inside the bracket, so it is multiplied by ${ntex(br.c)}$. It cannot be moved on its own: open the bracket first.",
                       "moved-term-out-of-bracket"))
        if len(wrongs) < 3:
            wrongs.append((f"Хоёр талыг {W(abs(br.c), 'ins')} үржүүлэх", f"Multiply both sides by ${ntex(abs(br.c))}$",
                           "Үржүүлбэл хаалт арилахгүй, харин тоонууд томорно. Хаалтын өмнөх тоог хаалтыг нээж эсвэл хуваалтаар арилгана.",
                           "Multiplying keeps the bracket and makes the numbers bigger. The number in front goes by opening the bracket or by dividing.",
                           "multiplied-instead-of-divided"))
        reason = ("Хаалт байгаа үед доторх тоонуудтай шууд ажиллах боломжгүй. Эхлээд хаалтыг нээнэ.",
                  "With a bracket in the way you cannot work with the numbers inside directly. Open it first.")
        checks = [equiv_check([br], expand_piece(br), v)]
    else:
        a1, b1 = coeffs(line.lhs)
        a2, b2 = coeffs(line.rhs)
        if a1 != 0 and a2 != 0:
            side = w.orientation(a1, a2)
            mv = a2 if side == "L" else a1
            t = etex([V(abs(mv))], v)
            if mv > 0:
                right = (f"Хоёр талаас {VW(t, v, 'acc')} хасах", f"Subtract ${t}$ from both sides")
                opp = (f"Хоёр талд {VW(t, v, 'acc')} нэмэх", f"Add ${t}$ to both sides")
            else:
                right = (f"Хоёр талд {VW(t, v, 'acc')} нэмэх", f"Add ${t}$ to both sides")
                opp = (f"Хоёр талаас {VW(t, v, 'acc')} хасах", f"Subtract ${t}$ from both sides")
            twice = etex([V(a1 + mv) if side == "R" else V(a2 + mv)], v)
            wrongs = [opp + (f"Ингэвэл нөгөө талд {M(twice)} гарч {M(v)} арилахгүй, харин нэмэгдэнэ. {M(etex([V(mv)], v))}-ийг арилгахын тулд эсрэг үйлдэл хийнэ.",
                             f"That leaves ${twice}$ on the other side: the ${v}$-term grows instead of going away. Do the opposite operation to remove ${etex([V(mv)], v)}$.",
                             "opposite-operation"),
                      (f"Зөвхөн {'баруун' if side == 'L' else 'зүүн'} талаас {VW(t, v, 'acc')} {'хасах' if mv > 0 else 'нэмэх'}",
                       f"{'Subtract' if mv > 0 else 'Add'} ${t}$ on the {'right' if side == 'L' else 'left'} side only",
                       "Нэг талд л үйлдэл хийвэл тэнцэтгэл алдагдана. Ижил үйлдлийг хоёр талд хийнэ.",
                       "Doing it on one side only breaks the balance. The same move goes on both sides.", "one-side-only")]
            ks = (line.lhs if b1 != 0 else line.rhs)
            vv = next(p for p in ks if p.kind == "v")
            kk = next(p for p in ks if p.kind == "k")
            comb = etex([V(vv.c + kk.c)], v)
            wrongs.append((f"{M(etex([vv, kk], v))} гэдгийг {M(comb)} болгож нэгтгэх", f"Combine ${etex([vv, kk], v)}$ into ${comb}$",
                           f"{M(etex([vv], v))} нь {VW(v, v, 'com')} гишүүн, {M(ntex(kk.c))} нь тоо: тэд төсөөтэй гишүүд биш тул нэгтгэж болохгүй.",
                           f"${etex([vv], v)}$ is a ${v}$-term and ${ntex(kk.c)}$ is a number: they are not like terms and cannot be combined.",
                           "combined-unlike-terms"))
            reason = (f"{M(v)} хоёр талд байна. Эхлээд {VW(v, v, 'com')} гишүүдийг нэг талд цуглуулна.",
                      f"${v}$ is on both sides. First gather the ${v}$-terms on one side.")
            checks = ["True"]
        else:
            vs = line.lhs if a1 != 0 else line.rhs
            A, B = coeffs(vs)
            assert B != 0 and A != 1
            other = b2 if a1 != 0 else b1
            if B > 0:
                right = (f"Хоёр талаас {W(B, 'acc')} хасах", f"Subtract ${ntex(B)}$ from both sides")
                opp = (f"Хоёр талд {W(B, 'acc')} нэмэх", f"Add ${ntex(B)}$ to both sides")
            else:
                right = (f"Хоёр талд {W(-B, 'acc')} нэмэх", f"Add ${ntex(-B)}$ to both sides")
                opp = (f"Хоёр талаас {W(-B, 'acc')} хасах", f"Subtract ${ntex(-B)}$ from both sides")
            dbl = etex([V(A), K(2 * B)], v)
            dv = etex([V(1), K(B)], v) + " = " + ntex(Fr(other) / A)
            wrongs = [opp + (f"Ингэвэл {M(dbl)} болж тоо арилахгүй, харин хоёр дахин ихэснэ.",
                             f"That gives ${dbl}$: the number does not go away, it doubles.", "opposite-operation"),
                      (f"Зөвхөн {VW(etex([V(A)], v), v, 'acc')} {W(A, 'dat')} хуваах: {M(dv)}",
                       f"Divide only ${etex([V(A)], v)}$ by ${ntex(A)}$: ${dv}$",
                       f"Хоёр талыг хуваахдаа гишүүн бүрийг хуваана: {M(ntex(B))} ч бас {W(A, 'dat')} хуваагдах ёстой. "
                       f"Эхлээд тоог арилгавал бутархай гарахгүй.",
                       f"Dividing a side means dividing every term: ${ntex(B)}$ must be divided by ${ntex(A)}$ too. "
                       f"Removing the number first avoids fractions.", "divided-one-term-only"),
                      (f"Зөвхөн {'зүүн' if a1 != 0 else 'баруун'} талд {'хасах' if B > 0 else 'нэмэх'}",
                       f"{'Subtract' if B > 0 else 'Add'} on the {'left' if a1 != 0 else 'right'} side only",
                       "Нэг талд л үйлдэл хийвэл тэнцэтгэл алдагдана. Ижил үйлдлийг хоёр талд хийнэ.",
                       "Doing it on one side only breaks the balance. The same move goes on both sides.", "one-side-only")]
            reason = (f"{VW(etex([V(A)], v), v, 'com')} хамт {M(ntex(B))} байна. Урвуу дарааллаар эхлээд тоог арилгана.",
                      f"${ntex(B)}$ sits with ${etex([V(A)], v)}$. In reverse order, the number goes first.")
            checks = ["True"]
    wrongs = wrongs[:3]
    assert len(wrongs) == 3
    if line.tex() == eq0.tex():
        st_mn = f"{M(eq0.tex())} тэгшитгэлийг бодох эхний зөв алхам аль вэ?"
        st_en = f"What is the right first step for solving ${eq0.tex()}$?"
        pre_mn = pre_en = ""
    else:
        nm = name or ("Номин", "Nomin")
        st_mn = (f"{nm[0]} {M(eq0.tex())} тэгшитгэлийг бодож байгаад {M(line.tex())} гэж бичсэн. "
                 f"Дараагийн зөв алхам аль вэ?")
        st_en = f"{nm[1]} is solving ${eq0.tex()}$ and has reached ${line.tex()}$. What is the right next step?"
    steps = [dict(mn=dict(do=reason[0]), en=dict(do=reason[1]))] + w.steps
    if drill:
        steps = steps[:3]
    if len(steps) > 6:
        steps = steps[1:]
    hints = [(f"{VW(v, v, 'acc')} ганцааруулахад одоо юу саад болж байна вэ? Түүнийг хоёр талд адилхан үйлдлээр арилгах алхмыг сонгоорой.",
              f"What is in the way of getting ${v}$ alone right now? Pick the move that removes it, done to both sides."),
             (w.steps[0]["h2"][0], w.steps[0]["h2"][1])]
    expl = (f"Дараагийн зөв алхам: {right[0][0].lower() + right[0][1:]}. Ингэвэл {M(nxt.tex())} болно.",
            f"The right next step: {right[1][0].lower() + right[1][1:]}. It gives ${nxt.tex()}$.")
    return assemble(vid, i, st_mn, st_en, right, wrongs, steps, hints, expl, w.checks + checks)


# ----- two friends solved it differently: who is right? --------------------

def verdict_tag(j, truth):
    """Option j of (only A, only B, both, neither) against the truth: did it accept a wrong working?"""
    sets = [{0}, {1}, {0, 1}, set()]
    return "accepted-wrong-working" if sets[j] - sets[truth] else "rejected-valid-method"


def aligned(lines, var):
    return "\\begin{aligned} " + " \\\\ ".join(f"{etex(l.lhs, var)} &= {etex(l.rhs, var)}" for l in lines) + " \\end{aligned}"


def t_friends(vid, i, eq, A, B):
    """A, B: dict(name=(mn, en), lines=[Eqn], how=(mn, en), err=(mn, en) or None)."""
    v = eq.var
    kind, sol = eq.solve()
    assert kind == "one"
    res = {}
    for P_ in (A, B):
        for l in P_["lines"]:
            l.var = v
        bad = next((j for j, l in enumerate(P_["lines"]) if l.solve() != ("one", sol)), None)
        assert (bad is None) == (P_["err"] is None), (vid, P_["name"])
        P_["bad"] = bad
        P_["ans"] = P_["lines"][-1].solve()[1]
    rA, rB = A["bad"] is None, B["bad"] is None
    gen = {n: GEN[n] for n in GEN}
    nA, nB = A["name"], B["name"]

    def fault(P_):
        j = P_["bad"]
        return (f"{gen[P_['name'][0]]} {j + 1}-р мөр буруу: {P_['err'][0]}",
                f"{P_['name'][1]}'s line {j + 1} is wrong: {P_['err'][1]}")

    def fine(P_):
        return (f"{gen[P_['name'][0]]} бодолт ч зөв: {P_['how'][0]}", f"{P_['name'][1]}'s working is right too: {P_['how'][1]}")
    opts = [(f"Зөвхөн {nA[0]} зөв", f"Only {nA[1]} is right"), (f"Зөвхөн {nB[0]} зөв", f"Only {nB[1]} is right"),
            ("Хоёулаа зөв", "Both are right"), ("Хоёулаа буруу", "Both are wrong")]
    truth = 0 if (rA and not rB) else 1 if (rB and not rA) else 2 if (rA and rB) else 3
    diags = {}
    if truth != 0:
        d = fault(A) if not rA else fine(B)
        diags[0] = d
    if truth != 1:
        d = fault(B) if not rB else fine(A)
        diags[1] = d
    if truth != 2:
        d = fault(A) if not rA else fault(B)
        diags[2] = d
    if truth != 3:
        P_ = A if rA else B
        diags[3] = (f"{gen[P_['name'][0]]} бодолт зөв: {P_['how'][0]} Хариу {M(f'{v} = {ntex(sol)}')} шалгалтад тэнцэнэ.",
                    f"{P_['name'][1]}'s working is right: {P_['how'][1]} The answer ${v} = {ntex(sol)}$ checks out.")
    wrongs = [None if j == truth else (opts[j][0], opts[j][1], diags[j][0], diags[j][1], verdict_tag(j, truth)) for j in range(4)]
    steps = []
    checks = [eq.check_at(sol)]
    for P_ in (A, B):
        g = gen[P_["name"][0]]
        if P_["bad"] is None:
            steps.append(dict(mn=dict(do=f"{g} бодолтыг шалгая: {P_['how'][0]} Мөр бүр өмнөх мөрөөсөө зөв гарсан.",
                                      why="Нэг тэгшитгэлийг хэд хэдэн зөв аргаар бодож болно."),
                              en=dict(do=f"Check {P_['name'][1]}'s working: {P_['how'][1]} Every line follows from the one before.",
                                      why="One equation can be solved correctly in more than one way.")))
            checks += [l.check_at(sol) for l in P_["lines"]]
        else:
            steps.append(dict(mn=dict(do=f"{g} бодолтыг шалгая: {P_['how'][0]} {P_['bad'] + 1}-р мөрөнд алдаа бий: {P_['err'][0]}"),
                              en=dict(do=f"Check {P_['name'][1]}'s working: {P_['how'][1]} Line {P_['bad'] + 1} is wrong: {P_['err'][1]}")))
            bl = P_["lines"][P_["bad"]]
            checks.append(f"Ne({epy(bl.lhs, at(sol))}, {epy(bl.rhs, at(sol))})")
    Lc, Rc = sub_chain(eq.lhs, v, sol, eq.is_dec()), sub_chain(eq.rhs, v, sol, eq.is_dec())
    checks += piece_checks(eq.lhs, sol) + piece_checks(eq.rhs, sol)
    steps.append(dict(mn=dict(do=f"Шалгая: {M(f'{v} = {ntex(sol)}')} үед зүүн тал {M(Lc)}, баруун тал {M(Rc)}. Хоёр тал тэнцүү."),
                      en=dict(do=f"Check: at ${v} = {ntex(sol)}$ the left side is ${Lc}$ and the right side is ${Rc}$. Equal.")))
    concl = {0: (f"Иймд зөвхөн {nA[0]} зөв.", f"So only {nA[1]} is right."), 1: (f"Иймд зөвхөн {nB[0]} зөв.", f"So only {nB[1]} is right."),
             2: ("Иймд хоёулаа зөв: арга нь өөр ч хариу нь нэг.", "So both are right: different methods, the same answer."),
             3: ("Иймд хоёулаа буруу.", "So both are wrong.")}[truth]
    steps[-1]["mn"]["do"] += " " + concl[0]
    steps[-1]["en"]["do"] += " " + concl[1]
    ans = "; ".join(gen[P_["name"][0]] + " хариу " + M(v + " = " + ntex(P_["ans"])) for P_ in (A, B))
    ans_en = "; ".join(f"{P_['name'][1]} got ${v} = {ntex(P_['ans'])}$" for P_ in (A, B))
    hints = [("Хоёр бодолтын мөр бүрийг өмнөх мөртэй нь харьцуулаарай. Хоёр өөр арга хоёулаа зөв байж болно.",
              "Compare every line of each working with the line before. Two different methods can both be right."),
             (f"{ans}. Хариу бүрийг анхны тэгшитгэлд орлуулж шалгаарай.", f"{ans_en}. Put each answer into the original equation.")]
    expl = (concl[0] + f" Зөв хариу нь {M(f'{v} = {ntex(sol)}')}.", concl[1] + f" The correct answer is ${v} = {ntex(sol)}$.")
    st_mn = (f"{nA[0]}, {nB[0]} хоёр {M(eq.tex())} тэгшитгэлийг ингэж бодсон. {nA[0]}: $${aligned(A['lines'], v)}$$ "
             f"{nB[0]}: $${aligned(B['lines'], v)}$$ Хэн нь зөв бэ?")
    st_en = (f"{nA[1]} and {nB[1]} solved ${eq.tex()}$ like this. {nA[1]}: $${aligned(A['lines'], v)}$$ "
             f"{nB[1]}: $${aligned(B['lines'], v)}$$ Who is right?")
    return assemble(vid, i, st_mn, st_en, opts[truth], wrongs, steps, hints, expl, checks, fixed_ci=truth)


# ----- a table of values ---------------------------------------------------

def t_table(vid, i, a, b, target, order, xs=range(5), head=None, text=None, answer=None):
    """y = a·x + b tabulated at xs (starting at 0); find x with y = target.
    head = ((mn x, mn y), (en x, en y)) words for the header; text = (mn, en) story lead-in."""
    xs = list(xs)
    assert xs[0] == 0 and all(xs[j + 1] - xs[j] == 1 for j in range(len(xs) - 1))
    eq = Eqn([V(a), K(b)], [K(target)], "x")
    w = Walk(eq, extra_steps=1)
    ys = [a * x + b for x in xs]
    if head:
        hx_mn, hy_mn = (f"\\text{{{head[0][0]}}}", f"\\text{{{head[0][1]}}}")
        hx_en, hy_en = (f"\\text{{{head[1][0]}}}", f"\\text{{{head[1][1]}}}")
    else:
        hx_mn = hx_en = "x"
        hy_mn = hy_en = "y"
    cols = "c|" + "c" * len(xs)

    def tab(hx, hy):
        return (f"\\begin{{array}}{{{cols}}} {hx} & " + " & ".join(ntex(x) for x in xs) + f" \\\\ \\hline {hy} & " +
                " & ".join(ntex(y) for y in ys) + " \\end{array}")
    grow = (f"{W(abs(a), 'ins')} {'нэмэгддэг' if a > 0 else 'хорогддог'}", f"{'goes up' if a > 0 else 'goes down'} by ${ntex(abs(a))}$")
    rule = Eqn([V(1)], [V(a), K(b)], "x")
    rt = f"y = {etex([V(a), K(b)], 'x')}"
    read = dict(mn=dict(do=f"Хүснэгтээс дүрмийг олъё: {M('x')} нэгээр нэмэгдэх бүрт доод мөрийн утга {grow[0]}, "
                           f"{M('x = 0')} үед {M(ntex(b))}. Иймд {M(rt)}. {M('y = ' + ntex(target))} гэж тавибал {M(eq.tex())} тэгшитгэл гарна.",
                        why="Эхний утга нь тогтмол гишүүн, нэг алхам бүрийн өөрчлөлт нь коэффициент болно."),
                en=dict(do=f"Read the rule from the table: each time $x$ goes up by one the bottom row {grow[1]}, and at $x = 0$ it is "
                           f"${ntex(b)}$. So ${rt}$. Setting $y = {ntex(target)}$ gives the equation ${eq.tex()}$.",
                        why="The starting value is the constant term and the change per step is the coefficient."))
    steps = [read] + w.steps
    if answer:
        steps[-1] = dict(mn=dict(do=steps[-1]["mn"]["do"] + " " + answer[0]), en=dict(do=steps[-1]["en"]["do"] + " " + answer[1]))
    ms, mchecks = walk_wrongs(w, ["move_const_sign", "neg", "no_divide", "mul_instead"],
                              [dict(x=Fr(target - ys[-1], a) + xs[-1] + 1, mode="count", tag="skipped-table-step",
                                    mn=f"Хүснэгтийг цааш нь үргэлжлүүлж тоолохдоо нэг алхам алгассан бололтой. {M(eq.tex())} тэгшитгэлийг бодоход хариу шууд гарна.",
                                    en=f"It looks as if one step was skipped when extending the table. Solving ${eq.tex()}$ gives the answer directly.",
                                    checks=[])])
    checks = w.checks + mchecks + [f"Eq({a}*({x}) + ({b}), {y})" for x, y in zip(xs, ys)]
    wrongs = [(M(ntex(m["x"])),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    hints = [("Хүснэгтийн доод мөр нэг алхам бүрт хэдээр өөрчлөгдөж байна вэ? Эхний утга нь юу вэ? Үүнээс дүрмийг бичээрэй.",
              "By how much does the bottom row change at each step, and what is its first value? Write the rule from that."),
             (f"Дүрэм нь {M(rt)}. Иймд {M(eq.tex())} тэгшитгэлийг бодоорой.", f"The rule is ${rt}$, so solve ${eq.tex()}$.")]
    expl = (f"Хүснэгтийн дүрэм {M(rt)} тул {M(eq.tex())}, эндээс {M('x = ' + ntex(w.sol))}.",
            f"The table's rule is ${rt}$, so ${eq.tex()}$ and $x = {ntex(w.sol)}$.")
    checks.append(f"Eq({a}*({npy(w.sol)}) + ({b}), {target})")
    if text:
        st_mn = f"{text[0]} $${tab(hx_mn, hy_mn)}$$"
        st_en = f"{text[1]} $${tab(hx_en, hy_en)}$$"
    else:
        st_mn = (f"Хүснэгтийн доод мөрийн утга дээд мөрөөс нэг дүрмээр хамаарна. $${tab(hx_mn, hy_mn)}$$ "
                 f"Доод мөрөнд {M(ntex(target))} гарах {M('x')}-ийн утга хэд вэ?")
        st_en = (f"The bottom row follows one rule from the top row. $${tab(hx_en, hy_en)}$$ "
                 f"For which $x$ does the bottom row reach ${ntex(target)}$?")
    return assemble(vid, i, st_mn, st_en, (M(ntex(w.sol)),) * 2, wrongs, steps, hints, expl, checks)


# ----- which point on the number line is the solution ----------------------

def t_point(vid, i, eq, lo, hi, order):
    v = eq.var
    w = Walk(eq)
    cands = [c for c in w.mistakes(order) if Fr(c["x"]).denominator == 1 and lo <= c["x"] <= hi]
    ms = pick3(w.sol, cands)
    vals = [m["x"] for m in ms]
    ci = i % 4
    vals.insert(ci, w.sol)
    labels = ["A", "B", "C", "D"]
    pts = sorted(zip(vals, range(4)))
    lab_of = {}
    for (val_, j), L_ in zip(pts, labels):
        lab_of[j] = L_
    checks = list(w.checks)
    steps = [dict(mn=dict(do=f"Тоон шулуунаас цэг бүрийн утгыг уншъя: " +
                          ", ".join(f"{lab_of[j]} = {M(ntex(vals[j]))}" for j in sorted(lab_of, key=lambda j: lab_of[j])) +
                          f". Утга бүрийг {VW(v, v, 'gen')} оронд тавьж шалгая.",
                          why="Шийд гэдэг нь тэгшитгэлийг үнэн тэнцэтгэл болгодог утга."),
                  en=dict(do="Read each point off the number line: " +
                          ", ".join(f"{lab_of[j]} = ${ntex(vals[j])}$" for j in sorted(lab_of, key=lambda j: lab_of[j])) +
                          f". Put each value in place of ${v}$.",
                          why="A solution is the value that makes the equation true."))]
    for j in [j for j in range(4) if j != ci] + [ci]:
        x = vals[j]
        Lc, Rc = sub_chain(eq.lhs, v, x), sub_chain(eq.rhs, v, x)
        checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        tail = ("Хоёр тал тэнцүү тул энэ нь шийд." if j == ci else "Тэнцүү биш.", "Equal: this is the solution." if j == ci else "Not equal.")
        steps.append(dict(mn=dict(do=f"{lab_of[j]} цэг, {M(f'{v} = {ntex(x)}')}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. {tail[0]}"),
                          en=dict(do=f"Point {lab_of[j]}, ${v} = {ntex(x)}$: left side ${Lc}$, right side ${Rc}$. {tail[1]}")))
    steps = steps[:6]
    wrongs = []
    for j in range(4):
        if j == ci:
            wrongs.append(None)
            continue
        m = ms[[k for k in range(4) if k != ci].index(j)]
        x = vals[j]
        wrongs.append((f"{lab_of[j]} цэг", f"Point {lab_of[j]}",
                       m["mn"] + f" {lab_of[j]} цэгийн утгыг орлуулбал зүүн тал {M(ntex(eval_side(eq.lhs, x)))}, баруун тал {M(ntex(eval_side(eq.rhs, x)))} гарч тэнцэхгүй.",
                       m["en"] + f" Point {lab_of[j]} gives ${ntex(eval_side(eq.lhs, x))}$ on the left and ${ntex(eval_side(eq.rhs, x))}$ on the right.",
                       m["tag"]))
        checks += m["checks"]
    hints = [("Цэг бүрийн утгыг тэгшитгэлд орлуулаад хоёр тал тэнцэх эсэхийг шалгаарай.",
              "Put each point's value into the equation and see whether the two sides match."),
             (f"Эсвэл тэгшитгэлийг бодоод гарсан тоог тоон шулуун дээрээс хайгаарай: {w.steps[0]['h2'][0]}",
              f"Or solve the equation and look for the answer on the line: {w.steps[0]['h2'][1]}")]
    expl = (f"{lab_of[ci]} цэг буюу {M(f'{v} = {ntex(w.sol)}')} үед хоёр тал тэнцүү. Бусад цэгт тэнцэхгүй.",
            f"At point {lab_of[ci]}, ${v} = {ntex(w.sol)}$, the two sides are equal; at the others they are not.")
    pair = assemble(vid, i, f"Тоон шулуун дээрх аль цэг {M(eq.tex())} тэгшитгэлийн шийдийг заах вэ?",
                    f"Which point on the number line shows the solution of ${eq.tex()}$?",
                    (f"{lab_of[ci]} цэг", f"Point {lab_of[ci]}"), wrongs, steps, hints, expl, checks, fixed_ci=ci)
    fig = {"mode": "integerLine", "integerLine": {"min": lo, "max": hi,
                                                  "points": [{"value": int(vals[j]), "label": lab_of[j]} for j in range(4)]}}
    return with_fig(pair, fig, json.loads(json.dumps(fig)))


# ----- whose answer is right (two claimed answers, substitution only) -------

def t_whose(vid, i, eq, A, B, order):
    """A, B: (name pair, mode or None for the correct answer)."""
    v = eq.var
    w = Walk(eq)
    ms = {m["mode"]: m for m in w.mistakes(order)}
    people = []
    for nm, mode in (A, B):
        if mode is None:
            people.append((nm, w.sol, None))
        else:
            people.append((nm, ms[mode]["x"], ms[mode]))
    checks = list(w.checks)
    rA, rB = people[0][2] is None, people[1][2] is None
    truth = 0 if (rA and not rB) else 1 if (rB and not rA) else 2 if (rA and rB) else 3
    nA, nB = people[0][0], people[1][0]
    opts = [(f"Зөвхөн {nA[0]} зөв", f"Only {nA[1]} is right"), (f"Зөвхөн {nB[0]} зөв", f"Only {nB[1]} is right"),
            ("Хоёулаа зөв", "Both are right"), ("Хоёулаа буруу", "Both are wrong")]
    steps = [dict(mn=dict(do=f"Хэн зөвийг мэдэхийн тулд тэгшитгэлийг дахин бодох шаардлагагүй. Хариу бүрийг {VW(v, v, 'gen')} оронд тавьж шалгая.",
                          why="Шийд гэдэг нь тэгшитгэлийг үнэн тэнцэтгэл болгодог утга."),
                  en=dict(do=f"No need to solve again: put each answer in place of ${v}$ and check.",
                          why="A solution is the value that makes the equation true."))]
    sub = {}
    for nm, x, m in people:
        Lc, Rc = sub_chain(eq.lhs, v, x), sub_chain(eq.rhs, v, x)
        checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        ok = m is None
        sub[nm[0]] = (ntex(eval_side(eq.lhs, x)), ntex(eval_side(eq.rhs, x)))
        steps.append(dict(mn=dict(do=f"{GEN[nm[0]]} хариу {M(f'{v} = {ntex(x)}')}: зүүн тал {M(Lc)}, баруун тал {M(Rc)}. "
                                     + ("Тэнцүү тул зөв." if ok else "Тэнцүү биш тул буруу.")),
                          en=dict(do=f"{nm[1]}'s answer ${v} = {ntex(x)}$: left side ${Lc}$, right side ${Rc}$. "
                                     + ("Equal, so it is right." if ok else "Not equal, so it is wrong."))))
        if m:
            checks += m["checks"]
    concl = {0: (f"Иймд зөвхөн {nA[0]} зөв.", f"So only {nA[1]} is right."), 1: (f"Иймд зөвхөн {nB[0]} зөв.", f"So only {nB[1]} is right."),
             2: ("Иймд хоёулаа зөв.", "So both are right."), 3: ("Иймд хоёулаа буруу.", "So both are wrong.")}[truth]
    steps.append(dict(mn=dict(do=concl[0] + f" Тэгшитгэлийн шийд нь {M(f'{v} = {ntex(w.sol)}')}."),
                      en=dict(do=concl[1] + f" The solution is ${v} = {ntex(w.sol)}$.")))

    def bad(p):
        nm, x, m = p
        return (f"{GEN[nm[0]]} хариу буруу: орлуулбал {M(sub[nm[0]][0])} ба {M(sub[nm[0]][1])} гарч тэнцэхгүй. {m['mn']}",
                f"{nm[1]}'s answer is wrong: substituting gives ${sub[nm[0]][0]}$ and ${sub[nm[0]][1]}$. {m['en']}")

    def good(p):
        nm, x, m = p
        return (f"{GEN[nm[0]]} хариу ч зөв: орлуулбал хоёр тал {M(sub[nm[0]][0])} болно.",
                f"{nm[1]}'s answer is right too: both sides come to ${sub[nm[0]][0]}$.")
    pA, pB = people
    diags = {0: bad(pA) if not rA else good(pB), 1: bad(pB) if not rB else good(pA),
             2: bad(pA) if not rA else bad(pB), 3: good(pA) if rA else good(pB)}
    wrongs = [None if j == truth else (opts[j][0], opts[j][1], diags[j][0], diags[j][1], verdict_tag(j, truth)) for j in range(4)]
    hints = ["Хоёр хариуг тус бүр тэгшитгэлд орлуулаад хоёр тал тэнцэх эсэхийг шалгаарай.",
             f"{GEN[nA[0]]} хариуг орлуулбал зүүн тал {M(sub[nA[0]][0])}, баруун тал {M(sub[nA[0]][1])} гарна. Одоо {GEN[nB[0]]} хариуг шалгаарай."]
    hints_en = ["Put each answer into the equation and check whether the sides match.",
                f"{nA[1]}'s answer gives ${sub[nA[0]][0]}$ on the left and ${sub[nA[0]][1]}$ on the right. Now check {nB[1]}'s."]
    xa, xb = ntex(pA[1]), ntex(pB[1])
    st_mn = (f"{nA[0]}, {nB[0]} хоёр {M(eq.tex())} тэгшитгэлийг бодсон. {nA[0]} {M(f'{v} = {xa}')}, "
             f"{nB[0]} {M(f'{v} = {xb}')} гэсэн хариу гаргажээ. Хэн нь зөв бэ?")
    st_en = (f"{nA[1]} and {nB[1]} solved ${eq.tex()}$. {nA[1]} got ${v} = {xa}$ and {nB[1]} got ${v} = {xb}$. Who is right?")
    expl = (concl[0] + f" Шийд нь {M(f'{v} = {ntex(w.sol)}')}.", concl[1] + f" The solution is ${v} = {ntex(w.sol)}$.")
    return assemble(vid, i, st_mn, st_en, opts[truth], wrongs, steps, list(zip(hints, hints_en)), expl, checks, fixed_ci=truth)


# ----- which line opens the brackets correctly ----------------------------

def t_correct_line(vid, i, eq, order, drill=False):
    v = eq.var
    good, _, _ = expand(eq)
    bad = []
    for mode, mn, en in (("first_only", "хаалтын өмнөх тоогоор зөвхөн эхний гишүүнийг үржүүлжээ",
                          "the number in front multiplied only the first term"),
                         ("neg_sign", "хасах тэмдэгтэй тоогоор үржүүлэхэд хоёр дахь гишүүний тэмдгийг өөрчлөөгүй",
                          "multiplying by a negative number, the second term's sign was not changed"),
                         ("first_all", "хаалт бүрт зөвхөн эхний гишүүнийг үржүүлжээ",
                          "in every bracket only the first term was multiplied")):
        e2, _, tg_ = expand(eq, mode)
        if tg_ is None and mode != "first_all":
            continue
        if e2.tex() == good.tex() or any(e2.tex() == b[0].tex() for b in bad):
            continue
        bad.append((e2, mn, en, MODE_TAG.get(mode, "distribute-first-term-only")))
    assert len(bad) >= 3, vid
    bad = bad[:3]
    w = Walk(eq)
    checks = list(w.checks)
    wrongs = []
    for e2, mn, en, tag in bad:
        k, x = e2.solve()
        assert eval_side(e2.lhs, w.sol) != eval_side(e2.rhs, w.sol), (vid, e2.tex())
        checks.append(f"Ne({epy(e2.lhs, at(w.sol))}, {epy(e2.rhs, at(w.sol))})")
        wrongs.append((M(e2.tex()), M(e2.tex()),
                       f"Энэ мөрөнд {mn}. Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг тэмдэгтэй нь хамт үржүүлнэ.",
                       f"In this line {en}. The number in front multiplies every term inside, sign included.", tag))
    steps = w.steps[:3] if drill else w.steps
    hints = [("Хаалт бүрийг тусад нь нээгээд, гарсан гишүүдийг сонголтуудтай харьцуулаарай. Хаалтын өмнөх тэмдэгт анхаараарай.",
              "Open each bracket on its own and compare the terms with the options. Watch the sign in front of each bracket."),
             (w.steps[0]["h2"][0], w.steps[0]["h2"][1])]
    expl = (f"Хаалтуудыг зөв нээвэл {M(good.tex())} болно. Цааш бодвол {M(f'{v} = {ntex(w.sol)}')}.",
            f"Opening the brackets correctly gives ${good.tex()}$; solving on gives ${v} = {ntex(w.sol)}$.")
    return assemble(vid, i, f"{M(eq.tex())} тэгшитгэлийн хаалтыг зөв нээсэн мөр аль нь вэ?",
                    f"Which line opens the brackets of ${eq.tex()}$ correctly?",
                    (M(good.tex()),) * 2, wrongs, steps, hints, expl, checks)


# ----- stories: solve, or choose the equation -------------------------------

def t_write(vid, i, s):
    """Options are equations: the story's own equation and three mis-translations of it."""
    eq, v = s["eq"], s["var"]
    eq.var = v
    w = Walk(eq)
    wrongs, checks = [], list(w.checks)
    for k_, item in enumerate(s["wrongs"]):
        wr, mn, en = item[:3]
        tag = item[3] if len(item) > 3 else s["tags"][k_]
        if not isinstance(wr, Eqn):
            continue
        wr.var = v
        assert eval_side(wr.lhs, w.sol) != eval_side(wr.rhs, w.sol), (vid, wr.tex())
        checks.append(f"Ne({epy(wr.lhs, at(w.sol))}, {epy(wr.rhs, at(w.sol))})")
        wrongs.append((M(wr.tex()), M(wr.tex()), mn, en, tag))
    assert len(wrongs) >= 3, vid
    wrongs = wrongs[:3]
    write = dict(mn=dict(do=s["write"][0], why=s["write"][1]), en=dict(do=s["write"][2], why=s["write"][3]))
    sol = ntex(w.sol)
    Lc = sub_chain(eq.lhs, v, w.sol)
    Rc = sub_chain(eq.rhs, v, w.sol)
    steps = [write,
             dict(mn=dict(do="Бусад сонголт яагаад буруу вэ: " + " ".join(f"{w_[0]}: {w_[2]}" for w_ in wrongs)),
                  en=dict(do="Why the other options are wrong: " + " ".join(f"{w_[1]}: {w_[3]}" for w_ in wrongs))),
             dict(mn=dict(do=f"Шалгая: {M(eq.tex())} тэгшитгэлийг бодвол {M(f'{v} = {sol}')}. Зүүн тал {M(Lc)}, баруун тал {M(Rc)}. "
                             f"{s['answer'][0]} Бодлогын нөхцөлд тохирно."),
                  en=dict(do=f"Check: solving ${eq.tex()}$ gives ${v} = {sol}$. Left side ${Lc}$, right side ${Rc}$. "
                             f"{s['answer'][1]} It fits the story."))]
    checks += piece_checks(eq.lhs, w.sol) + piece_checks(eq.rhs, w.sol)
    hints = [s["hint1"], (s["write"][4], s["write"][5])]
    expl = (f"Зөв тэгшитгэл нь {M(eq.tex())}. Түүнийг бодвол {M(f'{v} = {sol}')} гарч бодлогод тохирно.",
            f"The right equation is ${eq.tex()}$. It gives ${v} = {sol}$, which fits the story.")
    e, m = assemble(vid, i, s["st_write"][0], s["st_write"][1], (M(eq.tex()),) * 2, wrongs, steps, hints, expl, checks)
    pair = (thin_all(e), thin_all(m))
    if s.get("fig"):
        pair = with_fig(pair, s["fig"][0], s["fig"][1])
    return pair


def t_story(vid, i, s):
    pair = story_variant(vid, i, s)
    if s.get("fig"):
        pair = with_fig(pair, s["fig"][0], s["fig"][1])
    return pair


# ----- how many solutions: make it so, pick it, story -----------------------

def t_make(vid, i, var, build_eq, shown, kv, target, wrongs_spec):
    """Find the k (or the box) that gives `target` ('none' or 'all'). build_eq(k) -> Eqn."""
    eq = build_eq(Fr(kv))
    assert eq.solve()[0] == target, (vid, eq.tex())
    checks = [f"Eq(expand(({epy(eq.lhs, var)}) - ({epy(eq.rhs, var)})), {npy(Fr(eq.diff()[1]))})"]
    wrongs = []
    for val_, mn, en, tag in wrongs_spec:
        e2 = build_eq(Fr(val_))
        assert e2.solve()[0] != target, (vid, val_)
        k2, x2 = e2.solve()
        if k2 == "one":
            checks.append(e2.check_at(x2))
        wrongs.append((M(ntex(val_)), M(ntex(val_)), mn, en, tag))
    a1, b1 = coeffs(combine(expand(eq)[0])[0].lhs)
    a2, b2 = coeffs(combine(expand(eq)[0])[0].rhs)
    simp = combine(expand(eq)[0])[0].tex()
    if target == "none":
        st_mn = f"{shown[0]} тэгшитгэл шийдгүй байх {VW('k', 'k', 'gen')} утгыг ол." if "k" in shown[0] else \
            f"Нүдэнд ямар тоо бичвэл {shown[0]} тэгшитгэл шийдгүй болох вэ?"
        st_en = f"Find the value of $k$ for which {shown[1]} has no solution." if "k" in shown[1] else \
            f"Which number in the box makes {shown[1]} have no solution?"
        need = ("Шийдгүй байхын тулд хялбарчилсны дараа хоёр талын коэффициент тэнцүү, тогтмол нь ялгаатай байх ёстой.",
                "For no solution, after simplifying the coefficients must be equal and the constants different.")
        ne_t = ntex(b1) + " \\ne " + ntex(b2)
        res = (f"{M(ne_t)} тул {M(var)} хорогдоход худал тэнцэтгэл үлдэж, шийдгүй болно.",
               f"${ntex(b1)} \\ne {ntex(b2)}$, so when ${var}$ cancels a false statement is left: no solution.")
    else:
        if "k" in shown[0]:
            st_mn = f"{VW('k', 'k', 'gen')} ямар утгад {shown[0]} тэгшитгэл төгсгөлгүй олон шийдтэй болох вэ?"
            st_en = f"For which value of $k$ does {shown[1]} have infinitely many solutions?"
        else:
            st_mn = f"Нүдэнд ямар тоо бичвэл {shown[0]} тэгшитгэл төгсгөлгүй олон шийдтэй болох вэ?"
            st_en = f"Which number in the box makes {shown[1]} have infinitely many solutions?"
        need = ("Төгсгөлгүй олон шийдтэй байхын тулд хялбарчилсны дараа хоёр тал яг ижил болох ёстой.",
                "For infinitely many solutions both sides must be identical after simplifying.")
        res = (f"Хоёр тал яг ижил {M(etex(combine(expand(eq)[0])[0].lhs, var))} болж, {M(var)}-ийн дурын утга тохирно. Энэ нь адилтгал.",
               f"Both sides become ${etex(combine(expand(eq)[0])[0].lhs, var)}$, so every value of ${var}$ works: an identity.")
    steps = [dict(mn=dict(do=need[0], why="Хоёр талаас ижил гишүүн хасахад юу үлдэхээс шийдийн тоо хамаарна."),
                  en=dict(do=need[1], why="How many solutions there are depends on what is left after cancelling.")),
             dict(mn=dict(do=f"{M(ntex(kv))} тоог тавиад хялбарчилбал {M(simp)} болно."),
                  en=dict(do=f"With ${ntex(kv)}$ in place and simplified, the equation reads ${simp}$.")),
             dict(mn=dict(do=res[0]), en=dict(do=res[1]))]
    tests = [Fr(0), Fr(1)]
    parts_mn, parts_en = [], []
    for x in tests:
        L, R = ntex(eval_side(eq.lhs, x)), ntex(eval_side(eq.rhs, x))
        checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        parts_mn.append(f"{M(f'{var} = {ntex(x)}')} үед {M(L)} ба {M(R)}")
        parts_en.append(f"at ${var} = {ntex(x)}$: ${L}$ and ${R}$")
    steps.append(dict(mn=dict(do="Шалгая: " + "; ".join(parts_mn) + "."), en=dict(do="Check: " + "; ".join(parts_en) + ".")))
    hints = [(need[0], need[1]),
             (f"Хялбарчилбал {VW(var, var, 'gen')} коэффициентууд ямар болох вэ? Тэдгээрийг тэнцүүлбэл аль тоо гарах вэ?",
              f"After simplifying, what are the coefficients of ${var}$? Which number makes them equal?")]
    expl = (f"{M(ntex(kv))} үед тэгшитгэл {M(simp)} болно. " + res[0], f"With ${ntex(kv)}$ it reads ${simp}$. " + res[1])
    return assemble(vid, i, st_mn, st_en, (M(ntex(kv)),) * 2, wrongs, steps, hints, expl, checks)


def t_which_none(vid, i, correct, others):
    """Options are equations; exactly one has no solution. others: [(Eqn, mn, en)]."""
    assert correct.solve()[0] == "none"
    v = correct.var
    checks = []
    steps = [dict(mn=dict(do="Тэгшитгэл бүрийг хялбарчлаад хоёр талын коэффициент, тогтмолыг харьцуулъя.",
                          why="Коэффициент тэнцүү, тогтмол ялгаатай бол шийдгүй; хоёр тал ижил бол төгсгөлгүй олон шийдтэй."),
                  en=dict(do="Simplify each equation and compare the coefficients and the constants on the two sides.",
                          why="Equal coefficients with different constants: no solution. Identical sides: infinitely many."))]
    wrongs = []
    for e2, mn, en, tag in others:
        e2.var = v
        simp = combine(expand(e2)[0])[0]
        k2 = e2.solve()[0]
        assert k2 != "none"
        word = ("яг нэг шийдтэй", "exactly one solution") if k2 == "one" else ("төгсгөлгүй олон шийдтэй", "infinitely many solutions")
        steps.append(dict(mn=dict(do=f"{M(e2.tex())}: хялбарчилбал {M(simp.tex())}, {word[0]}."),
                          en=dict(do=f"${e2.tex()}$: simplified ${simp.tex()}$, {word[1]}.")))
        checks.append(equiv_check(e2.lhs, simp.lhs, v))
        wrongs.append((M(e2.tex()), M(e2.tex()), mn, en, tag))
    simp = combine(expand(correct)[0])[0]
    a1, b1 = coeffs(simp.lhs)
    a2, b2 = coeffs(simp.rhs)
    checks += [equiv_check(correct.lhs, simp.lhs, v), equiv_check(correct.rhs, simp.rhs, v), f"Ne({npy(b1)}, {npy(b2)})"]
    rest = f"{ntex(b1)} = {ntex(b2)}"
    steps.append(dict(mn=dict(do=f"{M(correct.tex())}: хялбарчилбал {M(simp.tex())}. {M(v)} хорогдоход {M(rest)} гэсэн худал тэнцэтгэл үлдэх тул шийдгүй."),
                      en=dict(do=f"${correct.tex()}$: simplified ${simp.tex()}$. With ${v}$ cancelled, the false ${rest}$ is left: no solution.")))
    hints = [("Тэгшитгэл бүрийн хаалтыг нээж, тал бүрийг хялбарчлаарай. Дараа нь коэффициентуудыг харьцуулаарай.",
              "Open the brackets of each equation and simplify each side. Then compare the coefficients."),
             ("Шийдгүй тэгшитгэлд хялбарчилсны дараа хоёр талын коэффициент тэнцүү, тогтмол нь ялгаатай байна. Ийм нь аль вэ?",
              "In an equation with no solution the coefficients end up equal and the constants different. Which one is that?")]
    expl = (f"{M(correct.tex())} хялбарчилбал {M(simp.tex())}: коэффициент тэнцүү, тогтмол ялгаатай тул шийдгүй.",
            f"${correct.tex()}$ simplifies to ${simp.tex()}$: equal coefficients, different constants, so no solution.")
    return assemble(vid, i, "Аль тэгшитгэл шийдгүй вэ?", "Which equation has no solution?",
                    (M(correct.tex()),) * 2, wrongs, steps, hints, expl, checks)


def t_story_count(vid, i, eq, st, read, cats, concl, fig=None):
    """A story whose question is 'when (if ever) are they equal?'.
    cats: {'one','none','inf','zero'} -> (mn, en) option texts; concl: (mn, en) after the maths."""
    v = eq.var
    kind = eq.solve()[0]
    truth = {"one": "one", "none": "none", "all": "inf"}[kind]
    simp = combine(expand(eq)[0])[0] if any(p.kind == "br" for p in eq.lhs + eq.rhs) else \
        (combine(eq)[0] if (needs_combine(eq.lhs) or needs_combine(eq.rhs)) else eq)
    a1, b1 = coeffs(simp.lhs)
    a2, b2 = coeffs(simp.rhs)
    assert a1 == a2
    rest = f"{ntex(b1)} = {ntex(b2)}"
    order = ["one", "none", "inf", "zero"]
    ci = order.index(truth)
    checks = [equiv_check(eq.lhs, simp.lhs, v), equiv_check(eq.rhs, simp.rhs, v),
              (f"Eq({npy(b1)}, {npy(b2)})" if truth == "inf" else f"Ne({npy(b1)}, {npy(b2)})")]
    t = etex([V(abs(a1))], v)
    mv_mn = f"Хоёр талаас {VW(t, v, 'acc')} хасвал" if a1 > 0 else f"Хоёр талд {VW(t, v, 'acc')} нэмбэл"
    mv_en = f"Subtracting ${t}$ from both sides" if a1 > 0 else f"Adding ${t}$ to both sides"
    steps = [dict(mn=dict(do=read[0], why="Өгөгдлийг тэгшитгэл болгосны дараа шийд хэд байгааг тоолж болно."),
                  en=dict(do=read[1], why="Once the story is an equation, its solutions can be counted.")),
             dict(mn=dict(do=f"Хялбарчилбал {M(simp.tex())}. {mv_mn} {M(rest)} үлдэнэ."),
                  en=dict(do=f"Simplified: ${simp.tex()}$. {mv_en} leaves ${rest}$.")),
             dict(mn=dict(do=concl[0]), en=dict(do=concl[1]))]
    parts_mn, parts_en = [], []
    for x in (Fr(0), Fr(2)):
        L, R = ntex(eval_side(eq.lhs, x)), ntex(eval_side(eq.rhs, x))
        checks += piece_checks(eq.lhs, x) + piece_checks(eq.rhs, x)
        parts_mn.append(f"{M(f'{v} = {ntex(x)}')} үед {M(L)} ба {M(R)}")
        parts_en.append(f"at ${v} = {ntex(x)}$: ${L}$ and ${R}$")
    steps.append(dict(mn=dict(do="Шалгая: " + "; ".join(parts_mn) + "."), en=dict(do="Check: " + "; ".join(parts_en) + ".")))
    D = {
        ("none", "one"): ("Тодорхой нэг утгад тэнцэхийн тулд хоёр талын коэффициент ялгаатай байх ёстой. Энд хоёулаа ижил хурдаар өөрчлөгдөж байгаа тул зөрүү нь хэвээр үлдэнэ.",
                          "To meet at one value the coefficients would have to differ. Here both change at the same rate, so the gap never closes."),
        ("none", "inf"): (f"{M(v)} алга болсныг хараад «үргэлж тэнцүү» гэж дүгнэсэн байх. Гэвч үлдсэн {M(rest)} худал: зөрүү хэзээ ч арилахгүй.",
                          f"${v}$ disappearing was read as «always equal», but what is left, ${rest}$, is false: the gap never closes."),
        ("none", "zero"): (f"{M(v)} хорогдохыг {M(f'{v} = 0')} гэж ойлгох нь түгээмэл алдаа. {M(f'{v} = 0')} үед ч хоёр тал {M(ntex(b1))} ба {M(ntex(b2))} байна.",
                           f"Reading «${v}$ cancels» as «${v} = 0$» is a common mistake. Even at ${v} = 0$ the sides are ${ntex(b1)}$ and ${ntex(b2)}$."),
        ("inf", "one"): ("Хоёр илэрхийлэл хялбарчилсны дараа яг ижил болно. Тиймээс ганц утгад биш, бүх утгад тэнцүү.",
                         "After simplifying the two expressions are identical, so they agree for every value, not just one."),
        ("inf", "none"): (f"{M(v)} алга болсныг «хэзээ ч тэнцэхгүй» гэж ойлгосон байх. Үлдсэн {M(rest)} үргэлж үнэн.",
                          f"${v}$ disappearing was read as «never equal», but what is left, ${rest}$, is always true."),
        ("inf", "zero"): (f"{M(f'{v} = 0')} үед үнэхээр тэнцүү, гэхдээ ганцаараа биш: хоёр тал ямагт ижил.",
                          f"They are equal at ${v} = 0$, but not only there: the two sides are always the same."),
    }
    SC_TAG = {"one": "decided-before-simplifying", "inf": "cancelled-means-infinite", "zero": "cancelled-means-x-zero",
              "none": "cancelled-means-no-solution"}
    wrongs = [None if j == ci else (cats[o][0], cats[o][1]) + D[(truth, o)] + (SC_TAG[o],) for j, o in enumerate(order)]
    hints = [("Өгүүлбэр бүрийг илэрхийлэл болгож, хоёуланг тэнцүүлээрэй. Дараа нь хялбарчлаад коэффициентуудыг харьцуулаарай.",
              "Write each part of the story as an expression and set them equal. Then simplify and compare the coefficients."),
             (f"Тэгшитгэл нь {M(eq.tex())}. {mv_mn} юу үлдэх вэ?",
              f"The equation is ${eq.tex()}$. {mv_en}: what is left?")]
    expl = (f"Тэгшитгэл {M(eq.tex())} хялбарчилбал {M(rest)} үлдэнэ. {concl[0]}", f"The equation ${eq.tex()}$ reduces to ${rest}$. {concl[1]}")
    pair = assemble(vid, i, st[0], st[1], cats[truth], wrongs, steps, hints, expl, checks, fixed_ci=ci)
    if fig:
        pair = with_fig(pair, fig[0], fig[1])
    return pair


# ----- figures ----------------------------------------------------------------

def line_fig(xs, a, b, c, d, labels, unit, xlab):
    """Two lines y = a + b·x and y = c + d·x over xs (both languages share the numbers)."""
    ya = [a + b * x for x in xs]
    yb = [c + d * x for x in xs]
    out = []
    for (la, lb), un, xl in zip(labels, unit, xlab):
        out.append({"mode": "lineGraph", "lineGraph": {
            "points": [{"label": str(x), "value": float(y) if Fr(y).denominator != 1 else int(y)} for x, y in zip(xs, ya)],
            "seriesLabel": la, "series": [{"label": lb, "values": [int(y) for y in yb]}],
            "unit": un, "xLabel": xl, "step": max(1, int((max(ya + yb)) // 8 // 1000 * 1000) or 1)}})
    return out[1], out[0]          # (en, mn)


def one_line_fig(xs, a, b, units, xlabs):
    ys = [a + b * x for x in xs]
    out = []
    for un, xl in zip(units, xlabs):
        out.append({"mode": "lineGraph", "lineGraph": {"points": [{"label": str(x), "value": int(y)} for x, y in zip(xs, ys)],
                                                       "unit": un, "xLabel": xl}})
    return out[1], out[0]


def bars_fig(labels_mn, labels_en, values, unit_mn, unit_en):
    mk = lambda labels, unit: {"mode": "barChart", "barChart": {
        "categories": [{"label": l, "value": int(v)} for l, v in zip(labels, values)], "unit": unit}}
    return mk(labels_en, unit_en), mk(labels_mn, unit_mn)


def geo_poly(coords, side_labels):
    ids = [chr(65 + j) for j in range(len(coords))]
    pts = [{"id": p, "x": float(x), "y": float(y), "label": ""} for p, (x, y) in zip(ids, coords)]
    objs = []
    for j in range(len(ids)):
        o = {"kind": "segment", "from": ids[j], "to": ids[(j + 1) % len(ids)]}
        if side_labels[j]:
            o["label"] = side_labels[j]
        objs.append(o)
    fig = {"mode": "geo", "geo": {"points": pts, "objects": objs, "hidePoints": ids, "height": 170}}
    return fig, json.loads(json.dumps(fig))


def frac_fig(num, den, lab_en, lab_mn):
    return ({"mode": "fractionBar", "fraction": {"num": num, "den": den, "label": lab_en}},
            {"mode": "fractionBar", "fraction": {"num": num, "den": den, "label": lab_mn}})


# ---------------------------------------------------------------------------
# THE TEN WORKSHEETS
# Each form lists its twelve problems as (template, builder). The template
# names are checked by self_check: >= 6 kinds, each <= 3 times, never twice
# in a row, and every story used once in the whole unit.
# ---------------------------------------------------------------------------

STORY_KEYS = []


def S(key, **kw):
    STORY_KEYS.append(key)
    kw["key"] = key
    return kw


def hint_two(eq):
    v = eq.var
    side = eq.lhs if any(p.kind == "v" for p in eq.lhs) else eq.rhs
    t = etex([p for p in side if p.kind == "v"], v)
    return (f"{M(t)} гишүүнтэй хамт байгаа тоог эхлээд арилгах хэрэгтэй. Хоёр талд ямар үйлдэл хийвэл тэр тоо алга болох вэ?",
            f"First get rid of the number that sits with ${t}$. What can you do to both sides to make it disappear?")


def hint_like(v):
    return (f"Тэгшитгэлийн нэг талд {VW(v, v, 'com')} гишүүн хэд хэд байна. Тэдгээрийг эхлээд нэгтгэвэл ямар болох вэ?",
            f"One side has several ${v}$-terms. What do they become when you combine them first?")


def hint_both(v):
    return (f"{VW(v, v, 'com')} гишүүд хоёр талд байна. Аль талынхыг нь хасвал {VW(v, v, 'gen')} коэффициент эерэг үлдэх вэ?",
            f"There are ${v}$-terms on both sides. Removing which one keeps the coefficient of ${v}$ positive?")


HINT_BR = ("Эхлээд хаалтыг нээгээрэй. Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг тэмдэгтэй нь хамт үржүүлнэ.",
           "Open the bracket first. The number in front multiplies every term inside, sign included.")
HINT_FR = ("Бүх хуваарьт хуваагддаг хамгийн бага тоо аль вэ? Хоёр талыг тэр тоогоор үржүүлбэл бутархай алга болно.",
           "What is the smallest number every denominator divides into? Multiplying both sides by it removes the fractions.")
HINT_DEC = ("Хоёр талыг ямар тоогоор үржүүлбэл бүх тоо бүхэл болох вэ? Гишүүн бүрийг үржүүлэхээ мартаж болохгүй.",
            "What number makes every number whole when both sides are multiplied by it? Multiply every term.")
HINT_MS = ("Эхлээд бутархайгаас эсвэл хаалтаас салаарай. Дараа нь тал бүрийг хялбарчлаарай.",
           "First get rid of the fractions or the brackets. Then simplify each side.")

O_TS = ["move_const_sign", "neg", "no_divide", "mul_instead"]
O_SY = ["abs", "drop", "move_const_sign", "neg", "no_divide", "mul_instead"]
O_BS = ["move_var_sign", "move_const_sign", "no_divide", "neg", "mul_instead"]
O_BK = ["first_only", "neg_sign", "abs", "drop", "move_const_sign", "no_divide", "neg", "mul_instead"]
O_FX = ["partial", "add_dens", "first_only", "neg_sign", "abs", "move_var_sign", "move_const_sign", "no_divide", "drop", "mul_instead"]
O_MS = ["neg_sign", "first_only", "partial", "add_dens", "abs", "move_var_sign", "move_const_sign", "no_divide", "neg", "mul_instead"]
O_ALL = O_FX + ["neg"]


def nice_step(mx):
    for s_ in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000):
        if mx / s_ <= 10:
            return s_
    return 10000


def fix_steps(fig):
    for key in ("lineGraph", "barChart"):
        if key in fig:
            vals = [p["value"] for p in fig[key].get("points", [])] + [c["value"] for c in fig[key].get("categories", [])]
            for s_ in fig[key].get("series", []):
                vals += s_["values"]
            fig[key]["step"] = nice_step(max(vals))
    return fig


def lines2(eq, xs, labels_mn, labels_en, unit, xlab):
    """Two-line graph of the two sides of eq (each side = start + rate·x); asserts the numbers agree."""
    v = eq.var
    ya = [eval_side(eq.lhs, Fr(x)) for x in xs]
    yb = [eval_side(eq.rhs, Fr(x)) for x in xs]
    assert all(y.denominator == 1 for y in ya + yb)

    def mk(la, lb, un, xl):
        return fix_steps({"mode": "lineGraph", "lineGraph": {
            "points": [{"label": str(x), "value": int(y)} for x, y in zip(xs, ya)], "seriesLabel": la,
            "series": [{"label": lb, "values": [int(y) for y in yb]}], "unit": un, "xLabel": xl}})
    return mk(labels_en[0], labels_en[1], unit[1], xlab[1]), mk(labels_mn[0], labels_mn[1], unit[0], xlab[0])


def line1(start, rate, xs, unit, xlab):
    ys = [start + rate * x for x in xs]
    mk = lambda un, xl: fix_steps({"mode": "lineGraph", "lineGraph": {
        "points": [{"label": str(x), "value": int(y)} for x, y in zip(xs, ys)], "unit": un, "xLabel": xl}})
    return mk(unit[1], xlab[1]), mk(unit[0], xlab[0])


def bars(start, rate, weeks, lab_mn, lab_en, unit):
    vals = [start + rate * w_ for w_ in weeks]
    mk = lambda lab, un: fix_steps({"mode": "barChart", "barChart": {
        "categories": [{"label": lab(w_), "value": int(v_)} for w_, v_ in zip(weeks, vals)], "unit": un}})
    return mk(lab_en, unit[1]), mk(lab_mn, unit[0])


def wr(eq_or_val, mn, en, tag):
    return (eq_or_val, mn, en, tag)


SUBST = None


def subst_cases():
    global SUBST
    if SUBST is None:
        SUBST = find_substitution_cases()
    return SUBST


def plan_story(key, eq, var, st, write, answer, hint1, wrongs, fig):
    return S(key, var=var, eq=eq, st=st, write=write, answer=answer, hint1=hint1, wrongs=wrongs, fig=fig)


def old_story(n):
    """The original twelve stories, by position."""
    return stories_v1()[n]


DIAG_KINDS = {
    "first_only": ("Хаалтын өмнөх тоогоор зөвхөн эхний гишүүнийг үржүүлсэн", "Multiplied only the first term in the bracket"),
    "sign": ("Гишүүнийг нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй", "Moved a term across without changing its sign"),
    "combine": ("Төсөөтэй биш гишүүдийг нэгтгэсэн", "Combined terms that are not like terms"),
    "partial": ("Хоёр талыг үржүүлэхдээ зарим гишүүнийг үржүүлээгүй", "Did not multiply every term"),
    "div_sign": ("Сөрөг тоонд хуваахдаа хасах тэмдгийг орхисон", "Lost the minus sign when dividing"),
}


def t_diagnose(vid, i, case, kind):
    e, m = find_error_variant(vid, i, case)
    err = case["err"]
    name_mn, name_en = NAMES[i % len(NAMES)]
    others = [k for k in DIAG_KINDS if k != kind][:3]
    ci = i % 4
    keys = list(others)
    keys.insert(ci, kind)
    m["options"] = [DIAG_KINDS[k][0] for k in keys]
    e["options"] = [DIAG_KINDS[k][1] for k in keys]
    e["correctIndex"] = ci
    m["whyWrong"] = [None if k == kind else f"Энэ алдаа энд гараагүй. {err + 1}-р алхамд: {case['why'][0]}" for k in keys]
    e["whyWrong"] = [None if k == kind else f"That is not the mistake here. In step {err + 1}: {case['why'][1]}" for k in keys]
    e["misconceptions"] = [None if k == kind else "misnamed-error" for k in keys]
    disp = re.search(r"\$\$.*\$\$", m["statement"]).group(0)
    m["statement"] = f"{name_mn} {M(case['eq'].tex())} тэгшитгэлийг ингэж бодсон: {disp} {err + 1}-р алхамд ямар алдаа гаргасан бэ?"
    e["statement"] = f"{name_en} solved ${case['eq'].tex()}$ like this: {disp} What mistake was made in step {err + 1}?"
    m["explanation"] = f"{err + 1}-р алхамд: {case['why'][0]}"
    e["explanation"] = f"In step {err + 1}: {case['why'][1]}"
    m["hints"][1] = f"{err + 1}-р мөрийг өмнөх мөртэй нь харьцуулаарай. Тэнд юуг өөрчилсөн бэ, тэр нь хоёр талд зөв хийгдсэн үү?"
    e["hints"][1] = f"Compare line {err + 1} with the line before. What changed, and was it done correctly on both sides?"
    return e, m


def t_claim(vid, i, var, case, who):
    e, m = subst_variant_a(vid, i, var, case)
    xt = re.search(r"\$[a-z] = -?\d+\$", e["statement"]).group(0)
    eqt = re.findall(r"\$[^$]+\$", e["statement"])[1]
    m["statement"] = f"{who[0]} {eqt} тэгшитгэлийг бодоод {xt} гэж хариулсан. Энэ хариу зөв үү?"
    e["statement"] = f"{who[1]} solved {eqt} and answered {xt}. Is that answer right?"
    return e, m


CATS_TIME = {"one": ("Тодорхой нэг цагт тэнцэнэ", "At one particular hour"), "none": ("Хэзээ ч тэнцэхгүй", "Never"),
             "inf": ("Үргэлж тэнцүү", "Always"), "zero": ("Зөвхөн эхлэх үед тэнцүү", "Only at the very start")}




# ----- stripped drill: the least common denominator only -------------------

def t_lcd(vid, i, eq):
    v = eq.var
    dens = sorted({p.den for p in eq.lhs + eq.rhs if p.kind == "fr"})
    Mx = 1
    for d in dens:
        Mx = lcm(Mx, d)
    prod = 1
    for d in dens:
        prod *= d
    big = dens[-1]
    cands = [(sum(dens), "sum-of-denominators",
              lambda x: (f"Хуваариудыг нэмсэн байна. {M(ntex(x))}-д {M(ntex(next(d for d in dens if x % d)))} хуваагдахгүй тул бутархай үлдэнэ.",
                         f"That adds the denominators. ${x}$ is not a multiple of ${next(d for d in dens if x % d)}$, so a fraction is left.")),
             (prod, "not-smallest-multiplier",
              lambda x: (f"{W(x, 'ins')} үржүүлбэл бутархай алга болно, гэхдээ энэ нь хамгийн бага тоо биш: {M(ntex(Mx))} хангалттай, тоонууд жижиг үлдэнэ.",
                         f"Multiplying by ${x}$ does clear the fractions, but it is not the smallest: ${Mx}$ is enough and keeps the numbers small.")),
             (big, "largest-denominator",
              lambda x: (f"Хамгийн их хуваарийг авсан байна. {M(ntex(x))}-д {M(ntex(next(d for d in dens if x % d)))} хуваагдахгүй тул бутархай үлдэнэ.",
                         f"That takes the largest denominator. ${x}$ is not a multiple of ${next(d for d in dens if x % d)}$, so a fraction is left.")),
             (2 * Mx, "not-smallest-multiplier",
              lambda x: (f"{W(x, 'ins')} үржүүлж болно, гэхдээ хамгийн бага нь {M(ntex(Mx))}.",
                         f"${x}$ works, but the smallest is ${Mx}$."))]
    seen, wrongs, checks = {Mx}, [], [f"Eq(ilcm({', '.join(map(str, dens))}), {Mx})"] + [f"Eq(Mod({Mx}, {d}), 0)" for d in dens]
    for x, tag, f in cands:
        if x in seen:
            continue
        seen.add(x)
        mn, en = f(x)
        wrongs.append((M(ntex(x)), M(ntex(x)), mn, en, tag))
        if tag != "not-smallest-multiplier":
            checks.append(f"Ne(Mod({x}, {next(d for d in dens if x % d)}), 0)")
        if len(wrongs) == 3:
            break
    _, nxt, _, _ = clear(eq)
    mult = [big * k for k in range(1, Mx // big + 1)]
    ds = ", ".join(M(ntex(d)) for d in dens)
    steps = [dict(mn=dict(do=f"Хуваариуд нь {ds}. Хамгийн их хуваарь {W(big, 'gen')} үржвэрүүдийг дараалуулъя: "
                             + ", ".join(M(ntex(m_)) for m_ in mult) + ".",
                          why="Хуваарь бүрт хуваагддаг хамгийн бага тоо нь эдгээрийн дотор заавал байна."),
                  en=dict(do=f"The denominators are {ds}. List the multiples of the largest, ${big}$: " + ", ".join(f"${m_}$" for m_ in mult) + ".",
                          why="The smallest number every denominator divides into is somewhere in that list.")),
             dict(mn=dict(do=f"{M(ntex(Mx))} бол хуваарь бүрт хуваагддаг анхны тоо: " +
                             ", ".join(M(f"{Mx} : {d} = {Mx // d}") for d in dens) + ". Иймд хамгийн бага ерөнхий хуваарь нь " + M(ntex(Mx)) + "."),
                  en=dict(do=f"${Mx}$ is the first that every denominator divides: " + ", ".join(f"${Mx} : {d} = {Mx // d}$" for d in dens) +
                             f". So the least common denominator is ${Mx}$.")),
             dict(mn=dict(do=f"Хоёр талыг {W(Mx, 'ins')} үржүүлбэл {M(nxt.tex())} болж бутархай алга болно. Энэ асуултад үүгээр зогсоно."),
                  en=dict(do=f"Multiplying both sides by ${Mx}$ gives ${nxt.tex()}$: no fractions left. For this question, stop here."))]
    checks.append(f"Eq(Mod({Mx}, {big}), 0)")
    hints = [("Хамгийн их хуваарийн үржвэрүүдийг дараалуулаад, бусад хуваарь бүгд хуваагддаг анхных нь аль болохыг хараарай.",
              "List multiples of the largest denominator and find the first one the others all divide."),
             (f"Хамгийн их хуваарь {M(ntex(big))}. Түүний үржвэрүүд: " + ", ".join(M(ntex(big * k)) for k in range(1, 4)) + "…",
              f"The largest denominator is ${big}$. Its multiples: " + ", ".join(f"${big * k}$" for k in range(1, 4)) + "…")]
    expl = (f"Хуваариуд {ds}-ийн хамгийн бага ерөнхий хуваарь нь {M(ntex(Mx))}.", f"The least common denominator of {ds} is ${Mx}$.")
    return assemble(vid, i, f"{M(eq.tex())} тэгшитгэлийн хоёр талыг ямар хамгийн бага натурал тоогоор үржүүлбэл бүх бутархай алга болох вэ? "
                            f"Тэгшитгэлийг бодохгүй.",
                    f"What is the smallest whole number that clears every fraction in ${eq.tex()}$ when both sides are multiplied by it? "
                    f"Do not solve.", (M(ntex(Mx)),) * 2, wrongs, steps, hints, expl, checks)


# ----- explain, as a choice ---------------------------------------------------

def t_explain(vid, i, q, correct, wrongs, steps, hints, expl, checks):
    return assemble(vid, i, q[0], q[1], correct, wrongs, steps, hints, expl, checks)


def t_self(vid, i, q, model, samples, steps, hints, expl, checks):
    """An open or explain item the student marks against a model answer (answerFormat self).
    options = the model answer and three sample answers, each from a named misconception."""
    e, m = assemble(vid, i, q[0], q[1], model, [None] + list(samples), steps, hints, expl, checks, fixed_ci=0)
    e["answerFormat"] = "self"
    e["modelAnswer"], m["modelAnswer"] = model[1], model[0]
    return e, m


# ---------------------------------------------------------------------------
# THE BANK: parts A–H and a Challenge (problem-bank-authoring manual §3)
# ---------------------------------------------------------------------------

UNIT_MASTERY_EN = {
    "skill": "Solve a linear equation in one unknown (two-step; with negatives, fractions and decimals; with brackets and like "
             "terms; with the unknown on both sides), check a solution by substitution, recognise no solution or infinitely "
             "many, and model a situation with an equation.",
    "mistakes": [
        "Moving a term across the equals sign without changing its sign.",
        "Multiplying only the first term of a bracket, or keeping the sign of the second term after a negative number.",
        "Dividing before the constant is removed, or dividing only one term.",
        "Clearing fractions by multiplying only the fractions, not every term; adding the denominators.",
        "Losing the minus sign when dividing by a negative coefficient.",
        "Combining unlike terms, e.g. 3x + 2 = 5x.",
        "Reading «x cancels» as x = 0, or as «no solution», without looking at what is left.",
        "In a story, multiplying a one-off charge by the count, or answering for the wrong quantity.",
    ],
    "canDo": "Solve 3(x − 2)/4 − (x + 1)/6 = x/3 + 1 by hand, say whether an equation has one, no or infinitely many solutions, "
             "and turn a story into an equation, solve it and answer in a sentence with units.",
}
UNIT_MASTERY_MN = {
    "skill": "Нэг үл мэдэгдэхтэй шугаман тэгшитгэл бодох (хоёр алхамт; сөрөг тоо, бутархай, аравтын бутархайтай; хаалт, төсөөтэй "
             "гишүүдтэй; хоёр талдаа үл мэдэгдэхтэй), шийдээ орлуулж шалгах, шийдгүй эсвэл төгсгөлгүй олон шийдтэйг таних, "
             "нөхцөл байдлыг тэгшитгэлээр илэрхийлэх.",
    "mistakes": [
        "Гишүүнийг нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөхгүй байх.",
        "Хаалтын өмнөх тоогоор зөвхөн эхний гишүүнийг үржүүлэх, эсвэл сөрөг тоогоор үржүүлэхэд хоёр дахь гишүүний тэмдгийг өөрчлөхгүй байх.",
        "Тогтмол гишүүнийг арилгахаас өмнө хуваах, эсвэл зөвхөн нэг гишүүнийг хуваах.",
        "Бутархайгаас салахдаа зөвхөн бутархайтай гишүүдийг үржүүлэх; хуваариудыг нэмэх.",
        "Сөрөг коэффициентэд хуваахдаа хасах тэмдгийг алдах.",
        "Төсөөтэй биш гишүүдийг нэгтгэх, жишээ нь 3x + 2-ыг 5x гэх.",
        "Үл мэдэгдэх хорогдохыг x = 0 гэж, эсвэл үлдсэнийг харалгүй «шийдгүй» гэж ойлгох.",
        "Үгэн бодлогод нэг удаагийн төлбөрийг тоогоор үржүүлэх, эсвэл өөр хэмжигдэхүүний хариу өгөх.",
    ],
    "canDo": "3(x − 2)/4 − (x + 1)/6 = x/3 + 1 тэгшитгэлийг гараар бодох, тэгшитгэл нэг шийдтэй, шийдгүй, төгсгөлгүй олон шийдтэйг "
             "тогтоох, үгэн бодлогыг тэгшитгэл болгож бодоод хариуг нэгжтэй нь өгүүлбэрээр бичих.",
}

PREREQ = {
    "A": ["integer-operations", "order-of-operations", "inverse-operations"],
    "B": ["integer-operations", "fraction-arithmetic", "decimal-arithmetic", "lcm"],
    "C": ["inverse-operations", "lcm", "distributive-property"],
    "D": ["distributive-property", "like-terms", "integer-operations"],
    "E": ["like-terms", "integer-operations"],
    "F": ["expressions-from-words", "integer-operations", "percent-of-quantity"],
    "G": ["inverse-operations", "distributive-property", "like-terms"],
    "H": ["distributive-property", "like-terms", "fraction-arithmetic"],
    "Challenge": ["distributive-property", "fraction-arithmetic", "lcm"],
}
SKILL = {
    "A": "g8-le-two-step", "B": "g8-le-fractions-decimals", "C": "g8-le-first-move", "D": "g8-le-brackets-like-terms",
    "E": "g8-le-both-sides", "F": "g8-le-modelling", "G": "g8-le-error-analysis", "H": "g8-le-multi-step",
    "Challenge": "g8-le-multi-step",
}
EXTRA_SKILL = {
    "which_value": "g8-le-substitution-check", "which_eq": "g8-le-substitution-check", "point": "g8-le-substitution-check",
    "whose": "g8-le-substitution-check", "claim": "g8-le-substitution-check", "is_sol": "g8-le-substitution-check",
    "classify": "g8-le-solution-count", "make": "g8-le-solution-count", "which_none": "g8-le-solution-count",
    "count": "g8-le-solution-count", "explain_self": "g8-le-solution-count",
    "graph": "g8-le-read-graph", "bars": "g8-le-read-graph", "table": "g8-le-read-table", "geo": "g8-le-modelling",
    "story": "g8-le-modelling", "write": "g8-le-modelling", "percent": "g8-le-modelling", "frbar": "g8-le-modelling",
    "puzzle": "g8-le-modelling", "recipe": "g8-le-modelling",
}

STORY0_TAGS = ["fee-multiplied-by-count", "added-subtracted-confused", "stopped-before-dividing", "forgot-quantity"]
STORY4_TAGS = ["miscounted-people", "fee-multiplied-by-count", "stopped-before-dividing"]


def part_A():
    I = []
    e1 = Eqn([V(1), K(9)], [K(14)])
    I.append(("box", "direct", 1, lambda vid, i: t_box_extra(vid, i, e1, O_TS, [
        (23, "$9$-ийг хасахын оронд нэмсэн бололтой: $14 + 9$. Нүдэн дээр $9$ нэмэгдсэн тул буцаахдаа хасна.",
         "It looks as if $9$ was added instead of subtracted: $14 + 9$. Nine was added to the box, so take it away.",
         "sign-not-changed-moving-term"),
        (14, "Баруун талын тоог шууд бичсэн байна. Нүдэн дээр $9$ нэмэхэд $14$ гарах ёстой: $14 - 9 = 5$.",
         "That copies the right side. The box plus $9$ must make $14$: $14 - 9 = 5$.", "ignored-constant"),
        (-5, "$9 - 14$ гэж хассан бололтой. Хасах дараалал чухал: $14 - 9 = 5$.",
         "That is $9 - 14$. Order matters in subtraction: $14 - 9 = 5$.", "subtraction-order")])))
    e2 = Eqn([V(4)], [K(28)], "y")
    I.append(("bare", "direct", 1, lambda vid, i: t_bare_extra(vid, i, e2, O_TS, hint_two_one(e2), [
        (24, "$4$-ийг хассан бололтой. $4y$ гэдэг нь $4$ дахин $y$: үржүүлснийг хуваалтаар буцаана.",
         "It looks as if $4$ was subtracted. $4y$ means four times $y$: undo multiplication by dividing.",
         "subtracted-instead-of-divided")])))
    e3 = Eqn([V(3), K(7)], [K(19)])
    I.append(("bare", "direct", 2, lambda vid, i: t_bare(vid, i, e3, O_TS, hint_two(e3))))
    I.append(("explain", "explain", 2, lambda vid, i: t_explain(
        vid, i, ("$3x + 7 = 19$ тэгшитгэлийн хоёр талаас $7$-г хасаж болох нь яагаад вэ?",
                 "Why may we subtract $7$ from both sides of $3x + 7 = 19$?"),
        ("Хоёр талд ижил үйлдэл хийхэд тэнцэтгэл алдагдахгүй", "Doing the same thing to both sides keeps the equation balanced"),
        [("Зөвхөн зүүн талаас хасахад хангалттай, баруун тал өөрчлөгдөхгүй", "Only the left side needs it; the right side stays as it is",
          "Нэг талаас л хасвал тэнцүү байсан хоёр тал тэнцүү байхаа болино: $3x = 19$ гэвэл буруу.",
          "Subtracting on one side only breaks the balance: $3x = 19$ would be wrong.", "one-side-only"),
         ("Нөгөө тал руу шилжсэн тоо тэмдгээ хадгалдаг тул", "Because a number keeps its sign when it moves across",
          "Шилжсэн тоо эсрэг тэмдэгтэй болдог: зүүн талын $+7$ баруун талд $-7$ болно. Энэ нь хоёр талаас $7$-г хассантай адил.",
          "A number that moves across changes sign: $+7$ on the left becomes $-7$ on the right, the same as subtracting $7$ from both sides.",
          "sign-not-changed-moving-term"),
         ("$7$-г хасах нь хоёр талыг $7$-д хуваахтай адил", "Subtracting $7$ is the same as dividing both sides by $7$",
          "Нэмсэн тоог хасалтаар, үржүүлснийг хуваалтаар буцаана. $7$ нэмэгдсэн тул хасна.",
          "Addition is undone by subtraction and multiplication by division. Here $7$ was added, so it is subtracted.",
          "confused-inverse-operations")],
        [dict(mn=dict(do="Тэгшитгэлийг тэнцүү байгаа жинлүүр гэж төсөөлье: хоёр тавган дээр ижил жин байна.",
                      why="Тэнцүүгийн тэмдэг нь хоёр тал ижил хэмжээтэй гэсэн үг."),
              en=dict(do="Picture the equation as a balanced scale: the two pans hold the same weight.",
                      why="The equals sign says the two sides are the same size.")),
         dict(mn=dict(do="Хоёр тавгаас ижил $7$-г авахад жинлүүр тэнцүү хэвээр: $3x + 7 - 7 = 19 - 7$, өөрөөр хэлбэл $3x = 12$."),
              en=dict(do="Taking $7$ off both pans keeps it level: $3x + 7 - 7 = 19 - 7$, that is $3x = 12$.")),
         dict(mn=dict(do="Цааш бодвол $x = 4$. Шалгая: $3 \\cdot 4 + 7 = 19$. Хоёр тал тэнцүү."),
              en=dict(do="Solving on gives $x = 4$. Check: $3 \\cdot 4 + 7 = 19$. Equal."))],
        [("Тэгшитгэлийн хоёр талыг тэнцүү жинтэй хоёр таваг гэж бодоорой.", "Think of the two sides as two pans of equal weight."),
         ("Нэг тавгаас л жин авбал юу болох вэ?", "What happens if you take weight off one pan only?")],
        ("Хоёр талд ижил үйлдэл хийхэд тэнцэтгэл алдагдахгүй, иймд хоёр талаас $7$-г хасаж $3x = 12$ гэж бичнэ.",
         "Doing the same thing to both sides keeps the balance, so subtract $7$ from both: $3x = 12$."),
        ["Eq(19 - 7, 12)", "Eq(3*4 + 7, 19)", "Eq(12/3, 4)"])))
    I.append(("box", "direct", 2, lambda vid, i: t_box(vid, i, Eqn([V(4), K(-9)], [K(15)]), O_TS)))
    I.append(("which_value", "compare", 2, lambda vid, i: subst_variant_b(vid, i, Eqn([V(2), K(-5)], [K(9)], "a"))))
    e7 = Eqn([K(26)], [V(3), K(-4)], "m")
    I.append(("bare", "direct", 3, lambda vid, i: t_bare(vid, i, e7, O_TS, hint_two(e7))))
    I.append(("table", "figure", 3, lambda vid, i: t_table(vid, i, 3, 5, 38, O_TS)))
    I.append(("which_eq", "reverse", 3, lambda vid, i: t_which_eq(vid, i, 5, "x", Eqn([V(4), K(-3)], [K(17)]),
                                                                 [("first", 3, -2), ("const", 2, -6), ("nodiv", 3, 1)], line=(-2, 8))))
    I.append(("point", "figure", 3, lambda vid, i: t_point(vid, i, Eqn([V(2), K(7)], [K(1)], "m"), -13, 5,
                                                          ["move_const_sign", "no_divide", "mul_instead"])))
    I.append(("param", "reverse", 4, lambda vid, i: t_param(vid, i, ("kx - 4 = 10", "{k}*{x} - 4 = 10"), 2,
                                                           Eqn([V(2), K(-4)], [K(10)], "k"), O_TS)))
    I.append(("open", "open", 4, lambda vid, i: t_self(
        vid, i, ("Шийд нь $x = 3$ байх $ax + b = c$ хэлбэрийн нэг тэгшитгэл зохиогоорой ($a \\ne 1$, $b \\ne 0$). "
                 "Зохиосон тэгшитгэлдээ $x = 3$ утгыг орлуулж шалгаарай.",
                 "Write an equation of the form $ax + b = c$ whose solution is $x = 3$ ($a \\ne 1$, $b \\ne 0$). "
                 "Check it by substituting $x = 3$."),
        ("Жишээ нь $2x + 1 = 7$, учир нь $2 \\cdot 3 + 1 = 7$", "For example $2x + 1 = 7$, because $2 \\cdot 3 + 1 = 7$"),
        [("$2x + 1 = 6$", "$2x + 1 = 6$",
          "$x = 3$ үед зүүн тал $7$ болно, $6$ биш. Зохиосон тэгшитгэлээ заавал орлуулж шалгаарай.",
          "At $x = 3$ the left side is $7$, not $6$. Always substitute to check an equation you write.", "did-not-check-solution"),
         ("$x + 3 = 0$", "$x + 3 = 0$",
          "Энэ тэгшитгэлийн шийд нь $x = -3$. Мөн $a = 1$ байна. Шийд $3$ байхын тулд $x - 3 = 0$ гэх мэтээр бичнэ.",
          "This one is solved by $x = -3$, and $a = 1$. For the solution $3$ you would need something like $x - 3 = 0$.",
          "sign-of-solution"),
         ("$3x = 1$", "$3x = 1$",
          "Энд $3$ нь коэффициент болсон тул шийд нь $\\frac{1}{3}$. Мөн $b = 0$ байна. $x$-ийн оронд $3$ тавиад $c$-г тооцоолно.",
          "Here $3$ became the coefficient, so the solution is $\\frac{1}{3}$, and $b = 0$. Put $3$ in for $x$ and work out $c$.",
          "confused-coefficient-solution")],
        [dict(mn=dict(do="Шийдээс эхэлье. Дурын $a$, $b$ сонгоод $c$-г тооцоолно: $a = 2$, $b = 1$ бол $c = 2 \\cdot 3 + 1 = 7$.",
                      why="Шийд нь тэгшитгэлийг үнэн болгодог тул $x = 3$ үед зүүн тал $c$-тэй тэнцүү байх ёстой."),
              en=dict(do="Start from the solution. Choose any $a$ and $b$ and work out $c$: with $a = 2$, $b = 1$, $c = 2 \\cdot 3 + 1 = 7$.",
                      why="The solution makes the equation true, so at $x = 3$ the left side must equal $c$.")),
         dict(mn=dict(do="Тэгшитгэл нь $2x + 1 = 7$. Өөр $a$, $b$ сонговол өөр тэгшитгэл гарна: олон зөв хариу бий."),
              en=dict(do="The equation is $2x + 1 = 7$. Other choices of $a$ and $b$ give other equations: many answers are right.")),
         dict(mn=dict(do="Шалгая: $2x + 1 = 7$ тэгшитгэлийг бодвол $2x = 6$, $x = 3$. Зөв."),
              en=dict(do="Check: solving $2x + 1 = 7$ gives $2x = 6$, $x = 3$. Right."))],
        [("Шийдээс эхлээрэй: $a$, $b$-д дуртай тоогоо өгөөд $x = 3$ үед зүүн тал хэд болохыг бодоорой.",
          "Start from the solution: pick $a$ and $b$, then work out the left side at $x = 3$."),
         ("Жишээ нь $a = 2$, $b = 1$ бол $2 \\cdot 3 + 1 = 7$ тул $c = 7$.", "For example $a = 2$, $b = 1$ gives $2 \\cdot 3 + 1 = 7$, so $c = 7$.")],
        ("Жишээ хариу: $2x + 1 = 7$. Ямар ч тэгшитгэл $x = 3$ үед үнэн бол зөв.", "A sample answer: $2x + 1 = 7$. Any equation true at $x = 3$ is right."),
        ["Eq(2*3 + 1, 7)", "Ne(2*3 + 1, 6)", "Eq(-3 + 3, 0)", "Eq(3*Rational(1,3), 1)", "Ne(3 + 3, 0)"])))
    return I


def hint_two_one(eq):
    v = eq.var
    return (f"{M(etex(eq.lhs, v))} гэдэг нь {M(v)}-ийг хэдээр үржүүлсэн бэ? Үржүүлснийг юугаар буцаах вэ?",
            f"In ${etex(eq.lhs, v)}$, what is ${v}$ multiplied by? What undoes multiplication?")


def extra_cands(eq, extra):
    out = []
    for xv, mn, en, tag in extra:
        out.append(dict(x=Fr(xv), mn=mn, en=en, mode="extra", tag=tag,
                        checks=[f"Ne({epy(eq.lhs, at(Fr(xv)))}, {epy(eq.rhs, at(Fr(xv)))})"]))
    return out


def t_bare_extra(vid, i, eq, order, hint1, extra):
    w = Walk(eq)
    ms = pick3(w.sol, w.mistakes(order) + extra_cands(eq, extra), w.dec)
    wrongs = [(M(ntexd(m["x"], w.dec)),) * 2 + (m["mn"], m["en"], m["tag"]) for m in ms]
    checks = list(w.checks)
    for m in ms:
        checks += m["checks"]
    st_mn, st_en = solve_stmt(eq)
    if len(w.steps) < 3:
        w.steps.insert(0, dict(mn=dict(do=f"{M(eq.tex())} тэгшитгэлд {M(eq.var)}-д нэг л үйлдэл хийгдсэн байна. Түүнийг буцаахад хангалттай."),
                               en=dict(do=f"In ${eq.tex()}$ only one operation was done to ${eq.var}$. Undoing it is enough.")))
    return assemble(vid, i, st_mn, st_en, (M(ntexd(w.sol, w.dec)),) * 2, wrongs, w.steps,
                    [hint1, hint2_from(next(st for st in w.steps if st.get("h2")), eq.var)],
                    walk_explanation(w), checks)


def t_box_extra(vid, i, eq, order, extra):
    w = Walk(eq, extra_steps=1)
    ms = pick3(w.sol, w.mistakes(order) + extra_cands(eq, extra), w.dec)
    bt = box_tex(eq)
    ans = ntexd(w.sol, w.dec)
    first = dict(mn=dict(do=f"Нүдэнд орох тоог $x$ гэж тэмдэглэе. Тэгвэл {M(eq.tex())} тэгшитгэл гарна.",
                         why="Мэдэгдэхгүй тоог үсгээр тэмдэглэвэл түүнийг тэгшитгэл бодож олно."),
                 en=dict(do=f"Call the number in the box $x$. Then the equation is ${eq.tex()}$.",
                         why="Naming the unknown number with a letter turns the puzzle into an equation to solve."))
    steps = [first] + w.steps
    steps[-1] = dict(mn=dict(do=steps[-1]["mn"]["do"] + f" Нүдэнд {M(ans)} бичнэ."),
                     en=dict(do=steps[-1]["en"]["do"] + f" The box holds ${ans}$."))
    hints = [("Нүдийг үл мэдэгдэх тоо гэж үзээд $x$ гэж тэмдэглээрэй. Тэгвэл энгийн тэгшитгэл болно.",
              "Treat the box as an unknown number and call it $x$: it becomes an ordinary equation."),
             hint2_from(w.steps[0], "x")]
    wrongs = [(M(ntexd(m_["x"], w.dec)),) * 2 + (m_["mn"], m_["en"], m_["tag"]) for m_ in ms]
    checks = list(w.checks)
    for m_ in ms:
        checks += m_["checks"]
    expl = (f"Нүдийг $x$ гэвэл {M(eq.tex())}. Бодоход {M('x = ' + ans)} тул нүдэнд {M(ans)} бичнэ.",
            f"With the box as $x$ the equation is ${eq.tex()}$. It gives $x = {ans}$, so the box holds ${ans}$.")
    return assemble(vid, i, f"Нүдэнд ямар тоо бичвэл тэнцэтгэл үнэн болох вэ? $${bt}$$",
                    f"Which number in the box makes this true? $${bt}$$", (M(ans),) * 2, wrongs, steps, hints, expl, checks)


def part_B():
    I = []
    e1 = Eqn([V(-2), K(5)], [K(11)])
    I.append(("bare", "direct", 1, lambda vid, i: t_bare(vid, i, e1, O_TS, hint_two(e1))))
    I.append(("which_value", "compare", 2, lambda vid, i: subst_variant_b(vid, i, Eqn([FR(3, V(2)), K(4)], [K(10)]))))
    bk = Eqn([FR(5, V(3))], [K(120)])
    I.append(("frbar", "figure", 2, lambda vid, i: t_story(vid, i, S(
        "book", var="x", eq=bk, fig=frac_fig(3, 5, "pages read", "уншсан хэсэг"),
        st=(f"Сарнай нэг номын {M(chr(92) + 'frac{3}{5}')} хэсгийг уншжээ. Зурагт уншсан хэсгийг будсан. "
            f"Тэр {M(120)} хуудас уншсан бол ном нийт хэдэн хуудастай вэ?",
            f"Sarnai has read $\\frac{{3}}{{5}}$ of a book; the shaded part of the bar shows it. She has read ${120}$ pages. "
            f"How many pages does the book have?"),
        write=(f"Номын хуудсыг {M('x')} гэе. {VW('x', 'x', 'gen')} {M(chr(92) + 'frac{3}{5}')} хэсэг нь {M(chr(92) + 'frac{3x}{5}')}, "
               f"энэ нь {M(120)} тул {M(bk.tex())}.",
               "«Хэсэг нь» гэдэг нь бүхлийг бутархайгаар үржүүлнэ гэсэн үг.",
               f"Let the book have $x$ pages. $\\frac{{3}}{{5}}$ of $x$ is $\\frac{{3x}}{{5}}$, which is ${120}$: ${bk.tex()}$.",
               "«A fraction of» the whole means the whole times the fraction.",
               f"Хуудсыг {M('x')} гэвэл {M(bk.tex())}.", f"With $x$ pages: ${bk.tex()}$."),
        answer=(f"Ном {M(200)} хуудастай.", f"The book has ${200}$ pages."),
        hint1=("Номын хуудсыг $x$ гэвэл уншсан хэсгийг $x$-ээр яаж бичих вэ? Зурагт хэдэн хэсгийн хэд нь будагдсан бэ?",
               "If the book has $x$ pages, how do you write the part read? How many of the parts are shaded?"),
        wrongs=[(72, "$120$-ийн $\\frac{3}{5}$-ийг олсон байна. Гэхдээ $120$ нь бүхэл ном биш, уншсан хэсэг.",
                 "That is $\\frac{3}{5}$ of $120$, but $120$ is the part read, not the whole book.", "part-whole-swapped"),
                (40, "$120$-ийг $3$-т хуваавал нэг хэсэг гарна. Ном ийм $5$ хэсэгтэй: $40 \\cdot 5$.",
                 "$120$ divided by $3$ is one part. The book has $5$ such parts: $40 \\cdot 5$.", "stopped-before-multiplying"),
                (600, "$3x = 600$ хүртэл зөв. Гэхдээ $600$ нь $3x$: $3$-т хуваана.", "Up to $3x = 600$ is right, but that is $3x$: divide by $3$.",
                 "stopped-before-dividing")]))))
    I.append(("box", "direct", 2, lambda vid, i: t_box(vid, i, Eqn([V("0.5"), K("1.5")], [K(4)]), O_FX)))
    sh = Eqn([V("0.8")], [K(36000)])
    I.append(("percent", "recall", 3, lambda vid, i: t_story(vid, i, S(
        "shirt-sale", var="x", eq=sh,
        st=(f"Дэлгүүрт бүх бараа {M('20' + chr(92) + '%')}-ийн хямдралтай байв. Номин цамцыг {tg(36000)} төлж авсан бол цамцны анхны үнэ хэд вэ?",
            f"Everything in a shop is ${'20' + chr(92) + '%'}$ off. Nomin paid {tg(36000)} for a shirt. What was its original price?"),
        write=(f"Анхны үнийг {M('x')} гэе. {M('20' + chr(92) + '%')} хямдарвал анхны үнийн {M('80' + chr(92) + '%')} буюу {M('0.8x')} төлнө. "
               f"Иймд {M(sh.tex())}.",
               "Хямдралын хувийг хасаад үлдсэн хувийг аравтын бутархайгаар бичнэ.",
               f"Let the original price be $x$. With ${'20' + chr(92) + '%'}$ off you pay ${'80' + chr(92) + '%'}$ of it, $0.8x$. So ${sh.tex()}$.",
               "Take the discount away from $100\\%$ and write what is left as a decimal.",
               f"Анхны үнийг {M('x')} гэвэл {M(sh.tex())}.", f"With the original price $x$: ${sh.tex()}$."),
        answer=(f"Анхны үнэ {tg(45000)}.", f"The original price was {tg(45000)}."),
        hint1=("Хямдралтай үед анхны үнийн хэдэн хувийг төлдөг вэ? Түүнийг аравтын бутархайгаар бичээрэй.",
               "In the sale, what percent of the original price do you pay? Write it as a decimal."),
        wrongs=[(43200, "$36\\,000$ дээр түүний $20\\%$-ийг нэмсэн бололтой. Хямдрал анхны үнээс тооцогддог тул $0.8x = 36\\,000$.",
                 "That adds $20\\%$ of $36\\,000$. The discount is taken from the original price, so $0.8x = 36\\,000$.", "percent-of-wrong-base"),
                (Eqn([V("0.2")], [K(36000)]), "$0.2x = 36\\,000$ гэж бичсэн бол хямдарсан хэсгийг төлсөн мэт үзжээ. Төлсөн нь үлдсэн $80\\%$.",
                 "Writing $0.2x = 36\\,000$ treats the discount as what was paid. What was paid is the remaining $80\\%$.", "discount-as-price"),
                (28800, "$36\\,000$-аас дахин $20\\%$ хассан байна: хямдралтай үнийг дахин хямдруулсан хэрэг.",
                 "That takes $20\\%$ off $36\\,000$ again: the sale price discounted twice.", "percent-of-wrong-base")]))))
    e6 = Eqn([FR(2, V(1)), FR(3, V(1))], [K(10)])
    I.append(("bare", "direct", 3, lambda vid, i: t_bare(vid, i, e6, O_FX, HINT_FR)))
    rd = Eqn([FR(3, V(2))], [K(140)])
    I.append(("frbar", "figure", 3, lambda vid, i: t_story(vid, i, S(
        "darkhan-road", var="x", eq=rd, fig=frac_fig(2, 3, "distance covered", "туулсан зам"),
        st=(f"Дорж Улаанбаатараас Дархан руу явж байна. Замын {M(chr(92) + 'frac{2}{3}')} хэсгийг туулахад {M(140)} км явсан байв (зургийг хар). "
            f"Улаанбаатараас Дархан хүртэл хэдэн км вэ?",
            f"Dorj is travelling from Ulaanbaatar to Darkhan. After covering $\\frac{{2}}{{3}}$ of the way he has gone ${140}$ km (see the bar). "
            f"How far is it from Ulaanbaatar to Darkhan?"),
        write=(f"Нийт замыг {M('x')} км гэе. Түүний {M(chr(92) + 'frac{2}{3}')} хэсэг нь {M(chr(92) + 'frac{2x}{3}')} тул {M(rd.tex())}.",
               "Туулсан хэсэг нь бүх замыг бутархайгаар үржүүлсэнтэй тэнцүү.",
               f"Let the whole way be $x$ km. $\\frac{{2}}{{3}}$ of it is $\\frac{{2x}}{{3}}$, so ${rd.tex()}$.",
               "The distance covered is the whole distance times the fraction.",
               f"Нийт замыг {M('x')} гэвэл {M(rd.tex())}.", f"With the whole way $x$: ${rd.tex()}$."),
        answer=(f"Улаанбаатараас Дархан хүртэл {M(210)} км.", f"It is ${210}$ km."),
        hint1=("Бүх замыг $x$ гэвэл туулсан хэсгийг $x$-ээр яаж бичих вэ?", "If the whole way is $x$, how do you write the part covered?"),
        wrongs=[(Fr(280, 3), "$140$-ийн $\\frac{2}{3}$-ыг олсон байна. $140$ нь туулсан хэсэг, бүх зам биш.",
                 "That is $\\frac{2}{3}$ of $140$, but $140$ is the part covered, not the whole way.", "part-whole-swapped"),
                (70, "$70$ бол замын гуравны нэг. Бүх зам гурван ийм хэсэг: $70 \\cdot 3$.",
                 "$70$ is one third of the way. The whole way is three such parts: $70 \\cdot 3$.", "stopped-before-multiplying"),
                (420, "$2x = 420$ хүртэл зөв. Гэхдээ энэ нь $2x$: $2$-т хуваана.", "Up to $2x = 420$ is right, but that is $2x$: divide by $2$.",
                 "stopped-before-dividing")]))))
    I.append(("whose", "compare", 3, lambda vid, i: t_whose(vid, i, Eqn([V("0.25"), K(-3)], [K("0.5")], "n"),
                                                           (("Тэмүүлэн", "Temuulen"), "partial"), (("Энхжин", "Enkhjin"), None), O_ALL)))
    I.append(("box", "direct", 3, lambda vid, i: t_box(vid, i, Eqn([FR(3, V(2)), K(5)], [K(1)]), ["partial"] + O_TS)))
    I.append(("explain", "explain", 4, lambda vid, i: t_explain(
        vid, i, ("$\\frac{x}{2} + \\frac{x}{3} = 10$ тэгшитгэлийн хоёр талыг $6$-аар үржүүлэхэд $10$-ыг ч бас үржүүлэх ёстой юу? Аль тайлбар зөв бэ?",
                 "When both sides of $\\frac{x}{2} + \\frac{x}{3} = 10$ are multiplied by $6$, must the $10$ be multiplied too? Which explanation is right?"),
        ("Тийм: хоёр тал бүхлээрээ үржигдэх тул гишүүн бүрийг үржүүлнэ, $3x + 2x = 60$",
         "Yes: each side is multiplied as a whole, so every term is, giving $3x + 2x = 60$"),
        [("Үгүй: $10$ бутархай биш тул үржүүлэх шаардлагагүй", "No: $10$ is not a fraction, so it stays",
          "Тэгвэл $3x + 2x = 10$ болж $x = 2$ гарна. $x = 2$ үед $1 + \\frac{2}{3} \\ne 10$: тэнцэтгэл алдагдсан.",
          "Then $3x + 2x = 10$ gives $x = 2$, and $1 + \\frac{2}{3} \\ne 10$: the balance is lost.", "multiplied-some-terms-only"),
         ("Үгүй: зөвхөн бутархайтай зүүн талыг үржүүлнэ", "No: only the left side, which has the fractions",
          "Нэг талыг л үржүүлбэл хоёр тал өөр тоогоор өөрчлөгдөж тэнцэтгэл алдагдана.",
          "Multiplying one side only changes the sides by different amounts and breaks the balance.", "one-side-only"),
         ("Тийм, гэхдээ $6$ биш $5$-аар үржүүлнэ", "Yes, but by $5$, not $6$",
          "$5$ нь хуваариудын нийлбэр: $\\frac{5x}{2}$ бутархай хэвээр үлдэнэ. $2$, $3$ хоёулаа хуваагддаг хамгийн бага тоо нь $6$.",
          "$5$ is the sum of the denominators: $\\frac{5x}{2}$ is still a fraction. The smallest number both $2$ and $3$ divide is $6$.",
          "sum-of-denominators")],
        [dict(mn=dict(do="Хоёр талыг бүхлээр нь үржүүлье: $6 \\cdot (\\frac{x}{2} + \\frac{x}{3}) = 6 \\cdot 10$.",
                      why="Тэнцүү хоёр зүйлийг ижил тоогоор үржүүлэхэд тэнцүү хэвээр үлдэнэ."),
              en=dict(do="Multiply each whole side: $6 \\cdot (\\frac{x}{2} + \\frac{x}{3}) = 6 \\cdot 10$.",
                      why="Equal things multiplied by the same number stay equal.")),
         dict(mn=dict(do="Хаалтыг нээвэл $3x + 2x = 60$: $10$ ч бас $6$ дахин ихэссэн."),
              en=dict(do="Opening the bracket: $3x + 2x = 60$. The $10$ was multiplied by $6$ too.")),
         dict(mn=dict(do="Бодвол $5x = 60$, $x = 12$. Шалгая: $\\frac{12}{2} + \\frac{12}{3} = 6 + 4 = 10$."),
              en=dict(do="Then $5x = 60$, $x = 12$. Check: $\\frac{12}{2} + \\frac{12}{3} = 6 + 4 = 10$."))],
        [("Тал бүрийг бүхэлд нь хаалтанд хийгээд $6$-аар үржүүлж үзээрэй.", "Put each whole side in a bracket and multiply it by $6$."),
         ("$6 \\cdot (\\frac{x}{2} + \\frac{x}{3}) = 6 \\cdot 10$. Баруун тал юу болох вэ?", "$6 \\cdot (\\frac{x}{2} + \\frac{x}{3}) = 6 \\cdot 10$. What does the right side become?")],
        ("Гишүүн бүрийг үржүүлнэ: $3x + 2x = 60$, эндээс $x = 12$.", "Every term is multiplied: $3x + 2x = 60$, so $x = 12$."),
        ["Eq(Rational(12,2) + Rational(12,3), 10)", "Eq(6*10, 60)", "Eq(60/5, 12)", "Ne(Rational(2,2) + Rational(2,3), 10)"])))
    bz = Eqn([V(1), V(1), K("-0.3")], [K("2.7")])
    I.append(("recipe", "modelling", 4, lambda vid, i: t_story(vid, i, S(
        "buuz", var="x", eq=bz,
        st=(f"Номин бууз хийхээр мах, гурил авчээ. Гурил нь махнаас {M('0.3')} кг-аар хөнгөн, хоёулаа нийт {M('2.7')} кг. Хэдэн кг мах авсан бэ?",
            f"Nomin bought meat and flour to make buuz. The flour weighs ${'0.3'}$ kg less than the meat, and together they weigh "
            f"${'2.7'}$ kg. How many kg of meat did she buy?"),
        write=(f"Махны жинг {M('x')} кг гэе. Гурил нь {M('x - 0.3')} кг. Нийт жин {M('2.7')} тул {M(bz.tex())}.",
               "«Хөнгөн» гэдэг нь махны жингээс хасна гэсэн үг. Хоёр жинг нэмбэл нийт жин гарна.",
               f"Let the meat weigh $x$ kg. The flour weighs $x - 0.3$ kg. Together: ${bz.tex()}$.",
               "«Less than» means take it away from the meat's weight; adding both weights gives the total.",
               f"Махыг {M('x')} гэвэл {M(bz.tex())}.", f"With the meat as $x$: ${bz.tex()}$."),
        answer=(f"Мах {M('1.5')} кг, гурил {M('1.2')} кг.", f"The meat weighs ${'1.5'}$ kg and the flour ${'1.2'}$ kg."),
        hint1=("Махны жинг $x$ гэвэл гурлын жинг $x$-ээр яаж бичих вэ?", "If the meat weighs $x$, how do you write the flour's weight?"),
        wrongs=[(Fr(6, 5), "$1.2$ кг бол гурлын жин. Асуулт махны жинг асууж байна.", "$1.2$ kg is the flour. The question asks for the meat.",
                 "answered-wrong-quantity"),
                (Fr(27, 20), "$2.7$-г $2$-т хуваасан бол мах, гурил хоёрыг ижил жинтэй гэж үзжээ. Гурил $0.3$ кг-аар хөнгөн.",
                 "Halving $2.7$ treats meat and flour as equal. The flour is $0.3$ kg lighter.", "ignored-difference"),
                (3, "$2x = 3$ хүртэл зөв. Гэхдээ энэ нь $2x$: $2$-т хуваана.", "Up to $2x = 3$ is right, but that is $2x$: divide by $2$.",
                 "stopped-before-dividing")]))))
    e12 = Eqn([FR(3, V(2), K(1))], [V(1), K(-2)], "a")
    I.append(("bare", "direct", 4, lambda vid, i: t_bare(vid, i, e12, O_FX, HINT_FR)))
    return I


def part_C():
    I = []
    I.append(("next", "stripped-drill", 1, lambda vid, i: t_next(vid, i, Eqn([V(3), K(7)], [K(19)]), Eqn([V(3), K(7)], [K(19)]), drill=True)))
    I.append(("lcd", "stripped-drill", 1, lambda vid, i: t_lcd(vid, i, Eqn([FR(4, V(1)), FR(6, V(1), c=-1)], [K(2)]))))
    I.append(("write", "stripped-drill", 2, lambda vid, i: t_write(vid, i, dict(
        old_story(0), key=S("notebooks")["key"], tags=STORY0_TAGS, st_write=(
            f"Бат {M(4)} дэвтэр, нэг үзэг худалдаж аваад нийт {tg(11500)} төлсөн. Үзэг {tg(1500)}. Нэг дэвтрийн үнийг {M('x')} гэвэл "
            f"аль тэгшитгэл зөв бэ? Бодохгүй.",
            f"Bat bought ${4}$ notebooks and one pen for {tg(11500)} in total. The pen cost {tg(1500)}. With one notebook costing $x$, "
            f"which equation is right? Do not solve.")))))
    I.append(("next", "stripped-drill", 2, lambda vid, i: t_next(vid, i, Eqn([V(3), K(7)], [V(5), K(-9)], "y"), Eqn([V(3), K(7)], [V(5), K(-9)], "y"), drill=True)))
    I.append(("lcd", "stripped-drill", 2, lambda vid, i: t_lcd(vid, i, Eqn([FR(6, V(1), K(1))], [FR(9, V(1), K(-2))]))))
    I.append(("correct_line", "stripped-drill", 3, lambda vid, i: t_correct_line(
        vid, i, Eqn([BR(3, V(1), K(-2)), BR(-2, V(1), K(4))], [K(6)]), O_MS, drill=True)))
    bb = Eqn([V(2), K(15)], [K(23)])
    I.append(("write", "stripped-drill", 3, lambda vid, i: t_write(vid, i, S(
        "basketball", var="x", eq=bb,
        st_write=(f"Сагсан бөмбөгийн тоглолтод Бат нийт {M(23)} оноо авсан. Үүнээс {M(5)} нь гурван онооны шидэлт, бусад нь хоёр онооны "
                  f"шидэлт байв. Хоёр онооны шидэлтийн тоог {M('x')} гэвэл аль тэгшитгэл зөв бэ? Бодохгүй.",
                  f"In a basketball game Bat scored ${23}$ points: ${5}$ three-pointers and the rest two-pointers. With $x$ two-pointers, "
                  f"which equation is right? Do not solve."),
        write=(f"Хоёр онооны {M('x')} шидэлт {M('2x')} оноо, гурван онооны {M(5)} шидэлт {M('3 ' + chr(92) + 'cdot 5 = 15')} оноо. "
               f"Нийлбэр нь {M(23)} тул {M(bb.tex())}.",
               "Шидэлтийн тоог нэг шидэлтийн оноогоор үржүүлбэл оноо гарна.",
               f"$x$ two-pointers give $2x$ points; ${5}$ three-pointers give $3 \\cdot 5 = 15$. The total is ${23}$: ${bb.tex()}$.",
               "Baskets times points per basket gives points.",
               f"Оноог нэмбэл {M(bb.tex())}.", f"Adding the points: ${bb.tex()}$."),
        answer=(f"Бат хоёр онооны {M(4)} шидэлт хийсэн.", f"Bat scored ${4}$ two-pointers."),
        hint1=("Гурван онооны таван шидэлт хэдэн оноо өгөх вэ? Хоёр онооны $x$ шидэлт хэд вэ?",
               "How many points do five three-pointers give? And $x$ two-pointers?"),
        wrongs=[(Eqn([V(2), K(5)], [K(23)]), "Шидэлтийн тоог ($5$) оноо мэт нэмжээ. $5$ шидэлт тус бүр $3$ оноо: $15$.",
                 "This adds the number of baskets ($5$) as if it were points. Each is worth $3$: $15$.", "count-used-as-amount"),
                (Eqn([V(3), K(10)], [K(23)]), "Хоёр, гурван оноог сольсон байна: $x$ шидэлт хоёр оноотой, $5$ шидэлт гурван оноотой.",
                 "The point values are swapped: the $x$ baskets are worth two, the $5$ baskets three.", "rate-and-fee-confused"),
                (Eqn([BR(2, V(1), K(15))], [K(23)]), "$2(x + 15)$ гэвэл гурван онооны шидэлтийн оноог ч хоёроор үржүүлжээ. Тэр оноо нэг удаа нэмэгдэнэ.",
                 "$2(x + 15)$ doubles the three-point score too. It is added once.", "fee-multiplied-by-count")]))))
    I.append(("next", "stripped-drill", 3, lambda vid, i: t_next(vid, i, Eqn([BR(5, V(1), K(-2)), K(3)], [K(18)], "n"),
                                                                Eqn([BR(5, V(1), K(-2)), K(3)], [K(18)], "n"), drill=True)))
    I.append(("lcd", "stripped-drill", 3, lambda vid, i: t_lcd(vid, i, Eqn([FR(2, V(1)), FR(3, V(1))], [FR(4, V(1)), K(7)]))))
    sv = Eqn([K(12), V(5)], [K(47)], "n")
    I.append(("write", "stripped-drill", 4, lambda vid, i: t_write(vid, i, S(
        "savings-bars", var="n", eq=sv, fig=bars(12, 5, [1, 2, 3, 4], lambda w_: f"{w_}-р долоо хоног", lambda w_: f"Week {w_}",
                                                ("мянган ₮", "thousand ₮")),
        st_write=(f"Тэмүүлэн долоо хоног бүр ижил хэмжээний мөнгө хадгалдаг. Графикт эхний дөрвөн долоо хоногийн эцсийн хадгаламжийг "
                  f"мянган төгрөгөөр үзүүлэв. Хэд дэх долоо хоногийн эцэст {M(47)} мянган төгрөгтэй болохыг олох тэгшитгэл аль нь вэ? "
                  f"Долоо хоногийн тоог {M('n')} гэе. Бодохгүй.",
                  f"Temuulen saves the same amount every week. The chart shows his savings, in thousands of tögrög, at the end of the "
                  f"first four weeks. Which equation finds the week when he reaches ${47}$ thousand? Let $n$ be the number of weeks. "
                  f"Do not solve."),
        write=(f"Графикаас: долоо хоног бүр {M('22 - 17 = 5')} мянгаар нэмэгдэж байна. Тэгэхээр эхлэхдээ {M('17 - 5 = 12')} мянгатай байсан. "
               f"Иймд {M(sv.tex())}.",
               "Нэг баганаас дараагийнх хүртэлх өсөлт нь долоо хоногийн хадгаламж; эхний мөнгийг нэг алхам буцааж олно.",
               f"From the chart: the savings grow by $22 - 17 = 5$ thousand a week, so he started with $17 - 5 = 12$ thousand. "
               f"So ${sv.tex()}$.",
               "The rise from bar to bar is the weekly saving; step back once to find the start.",
               f"Графикаас {M(sv.tex())}.", f"From the chart: ${sv.tex()}$."),
        answer=(f"{M(7)} дахь долоо хоногийн эцэст.", f"At the end of week ${7}$."),
        hint1=("Багана бүр өмнөхөөсөө хэдээр өндөр вэ? Тэгвэл эхлэхдээ хэдтэй байсан бэ?",
               "How much taller is each bar than the one before? Then how much did he start with?"),
        wrongs=[(Eqn([K(17), V(5)], [K(47)], "n"), "Эхний баганын $17$-г эхлэл гэж авсан бололтой. $17$ бол $1$-р долоо хоногийн эцсийнх: эхлэл нь $12$.",
                 "The first bar's $17$ was taken as the start. It is the end of week $1$; the start is $12$.", "misread-starting-value"),
                (Eqn([V(5)], [K(47)], "n"), "Эхний мөнгийг тооцоогүй байна: Тэмүүлэн тэгээс эхлээгүй.",
                 "The starting money is left out: Temuulen did not start from zero.", "missed-starting-amount"),
                (Eqn([V(12), K(5)], [K(47)], "n"), "Эхний мөнгө, долоо хоногийн хадгаламжийг сольсон байна: долоо хоног бүр $5$ мянгаар нэмэгддэг.",
                 "The start and the weekly saving are swapped: it grows by $5$ thousand a week.", "rate-and-fee-confused")]))))
    I.append(("correct_line", "stripped-drill", 4, lambda vid, i: t_correct_line(
        vid, i, Eqn([K(7), BR(-3, V(1), K(-2))], [BR(2, V(1), K(5))], "y"), O_MS, drill=True)))
    return I


def part_D():
    I = []
    e1 = Eqn([V(2), V(5), K(-4)], [K(24)])
    I.append(("bare", "direct", 1, lambda vid, i: t_bare(vid, i, e1, O_SY, hint_like("x"))))
    e2 = Eqn([BR(3, V(1), K(-4))], [K(15)])
    I.append(("bare", "direct", 1, lambda vid, i: t_bare(vid, i, e2, O_BK, HINT_BR)))
    I.append(("box", "direct", 2, lambda vid, i: t_box(vid, i, Eqn([V(1), V(1), V(1), K(4)], [K(19)]), O_SY)))
    e4 = Eqn([V(7), V(5)], [K(6000)])
    I.append(("story", "modelling", 2, lambda vid, i: t_story(vid, i, S(
        "bus-tickets", var="x", eq=e4,
        st=(f"Энэ долоо хоногт Бат автобусанд {M(7)} удаа, Номин {M(5)} удаа суусан. Нэг удаагийн тасалбар ижил үнэтэй. "
            f"Хоёулаа нийт {tg(6000)} төлсөн бол нэг удаагийн тасалбар хэдэн төгрөг вэ?",
            f"This week Bat took the bus ${7}$ times and Nomin ${5}$ times. Every ride costs the same. Together they paid "
            f"{tg(6000)}. How much is one ride?"),
        write=(f"Нэг удаагийн үнийг {M('x')} гэе. Бат {M('7x')}, Номин {M('5x')} төгрөг төлсөн тул {M(e4.tex())}.",
               "Хоёр хүний зардлыг тус тусад нь бичээд нэмнэ. Хоёулаа ижил үнэтэй тасалбар авсан тул төсөөтэй гишүүд болно.",
               f"Let one ride cost $x$. Bat paid $7x$ and Nomin $5x$, so ${e4.tex()}$.",
               "Write each person's cost and add. Both used the same fare, so these are like terms.",
               f"Нэг удаагийнхыг {M('x')} гэвэл {M(e4.tex())}.", f"With one ride as $x$: ${e4.tex()}$."),
        answer=(f"Нэг удаагийн тасалбар {tg(500)}.", f"One ride costs {tg(500)}."),
        hint1=("Нэг удаагийн үнийг $x$ гэвэл Бат, Номин хоёр тус бүр хэдэн төгрөг төлсөн бэ?",
               "If one ride costs $x$, how much did Bat and Nomin each pay?"),
        wrongs=[(Eqn([V(7), K(5)], [K(6000)]), "$7x + 5$ гэж бичсэн бол Номины суусан тоог мөнгө мэт нэмжээ. Номин ч мөн $x$ төгрөгөөр $5$ удаа суусан: $5x$.",
                 "Writing $7x + 5$ adds Nomin's number of rides as if it were money. She also paid $x$ each time: $5x$.", "count-used-as-amount"),
                (Fr(6000, 7), "Зөвхөн Батын зорчилтыг тоолсон бололтой. Номины $5$ удааг нэмэхэд $12$ удаа болно.",
                 "Only Bat's rides were counted. With Nomin's $5$ there are $12$ rides.", "missed-part-of-total"),
                (6000, "$12x = 6\\,000$ хүртэл зөв. Гэхдээ $6\\,000$ нь нийт мөнгө: $12$-т хуваавал нэг удаагийнх гарна.",
                 "Up to $12x = 6\\,000$ is right, but that is the total: divide by $12$ for one ride.", "stopped-before-dividing")]))))
    I.append(("friends", "compare", 2, lambda vid, i: t_friends(
        vid, i, Eqn([BR(4, V(1), K(3))], [K(28)]),
        dict(name=("Бат", "Bat"), lines=[Eqn([V(1), K(3)], [K(7)]), Eqn([V(1)], [K(4)])],
             how=(f"эхлээд хоёр талыг {W(4, 'dat')} хуваасан.", "he divided both sides by $4$ first."), err=None),
        dict(name=("Сарнай", "Sarnai"), lines=[Eqn([V(4), K(12)], [K(28)]), Eqn([V(4)], [K(16)]), Eqn([V(1)], [K(4)])],
             how=("эхлээд хаалтыг нээсэн.", "she opened the bracket first."), err=None))))
    e6 = Eqn([BR(-2, V(1), K(5))], [K(8)], "y")
    I.append(("bare", "direct", 3, lambda vid, i: t_bare(vid, i, e6, O_BK, HINT_BR)))
    r1 = Eqn([BR(2, V(1), V(1), K(3))], [K(34)])
    f1 = geo_poly([(0, 0), (5, 0), (5, 3), (0, 3)], ["x + 3", "x", "", ""])
    I.append(("geo", "figure", 3, lambda vid, i: t_story(vid, i, S(
        "flowerbed", var="x", eq=r1, fig=f1,
        st=(f"Сургуулийн цэцгийн мандал тэгш өнцөгт хэлбэртэй. Зурагт талуудын уртыг метрээр үзүүлэв: урт нь {M('x + 3')}, "
            f"өргөн нь {M('x')}. Мандлын периметр {M(34)} м бол өргөн {M('x')} хэдэн метр вэ?",
            f"A school flowerbed is a rectangle. The picture gives its sides in metres: length $x + 3$, width $x$. "
            f"The perimeter is ${34}$ m. What is the width $x$?"),
        write=(f"Тэгш өнцөгт хоёр урт, хоёр өргөнтэй тул периметр нь {M('2(x + x + 3)')}. Энэ нь {M(34)} тул {M(r1.tex())}.",
               "Периметр бол бүх талын уртын нийлбэр. Урт, өргөн тус бүр хоёр удаа орно.",
               f"A rectangle has two lengths and two widths, so the perimeter is $2(x + x + 3)$. It equals ${34}$: ${r1.tex()}$.",
               "The perimeter is the sum of all four sides; length and width each count twice.",
               f"Периметрээс {M(r1.tex())} гарна.", f"The perimeter gives ${r1.tex()}$."),
        answer=(f"Өргөн {M(7)} м, урт {M(10)} м.", f"The width is ${7}$ m and the length ${10}$ m."),
        hint1=("Тэгш өнцөгт хэдэн талтай вэ? Периметрийг $x$-ээр бичээрэй.", "How many sides does a rectangle have? Write the perimeter using $x$."),
        wrongs=[(Eqn([V(1), V(1), K(3)], [K(34)]), "$x + x + 3 = 34$ гэж бичсэн бол хоёр талыг л нэмжээ. Тэгш өнцөгт дөрвөн талтай.",
                 "Writing $x + x + 3 = 34$ adds only two sides. A rectangle has four.", "missed-part-of-total"),
                (10, "$10$ бол урт. Асуулт өргөнийг асууж байна: $x = 7$.", "$10$ is the length. The question asks for the width: $x = 7$.",
                 "answered-wrong-quantity"),
                (Eqn([V(2), V(2), K(3)], [K(34)]), "$2x + 2x + 3 = 34$ гэж бичсэн бол $3$-ыг хоёр удаа авахаа мартжээ: $2(x + 3) = 2x + 6$.",
                 "Writing $2x + 2x + 3 = 34$ counts the extra $3$ only once: $2(x + 3) = 2x + 6$.", "distribute-first-term-only")]))))
    I.append(("next", "compare", 3, lambda vid, i: t_next(vid, i, Eqn([BR(-2, V(1), K(4)), V(3)], [K(1)]), Eqn([BR(-2, V(1), K(4)), V(3)], [K(1)]))))
    I.append(("which_eq", "reverse", 3, lambda vid, i: t_which_eq(vid, i, 4, "x", Eqn([BR(2, V(1), K(3)), V(-1)], [K(10)]),
                                                                 [("first", 3, 2), ("const", 5, -6), ("nodiv", 3, -2)])))
    I.append(("box", "direct", 4, lambda vid, i: t_box(vid, i, Eqn([BR(3, V(2), K(-5)), V(4)], [K(25)]), O_BK)))
    I.append(("friends", "compare", 4, lambda vid, i: t_friends(
        vid, i, Eqn([K(7), BR(-3, V(1), K(-1))], [K(4)], "m"),
        dict(name=("Тэмүүлэн", "Temuulen"), lines=[Eqn([K(7), V(-3), K(-3)], [K(4)]), Eqn([K(4), V(-3)], [K(4)]), Eqn([V(1)], [K(0)])],
             how=("хаалтыг нээгээд нэгтгэсэн.", "he opened the bracket and combined."),
             err=("$-3(m - 1)$ гэдгийг $-3m - 3$ гэж нээжээ. Хасах тэмдэгтэй тоогоор үржүүлэхэд $-1$ нь $+3$ болно.",
                  "$-3(m - 1)$ became $-3m - 3$. Multiplying by a negative number turns $-1$ into $+3$.")),
        dict(name=("Энхжин", "Enkhjin"), lines=[Eqn([K(7), V(-3), K(3)], [K(4)]), Eqn([K(10), V(-3)], [K(4)]), Eqn([V(-3)], [K(-6)]), Eqn([V(1)], [K(2)])],
             how=("хаалтыг нээгээд нэгтгэсэн.", "she opened the bracket and combined."), err=None))))
    r2 = Eqn([BR(2, V(2), K(1), V(1))], [K(50)])
    f2 = geo_poly([(0, 0), (6, 0), (6, 2.5), (0, 2.5)], ["2x + 1", "x", "", ""])
    I.append(("geo", "figure", 4, lambda vid, i: t_story(vid, i, S(
        "volleyball", var="x", eq=r2, fig=f2,
        st=(f"Тэрэлжийн амралтын газарт тэгш өнцөгт волейболын талбай бий. Зурагт талбайн урт {M('2x + 1')} м, өргөн {M('x')} м. "
            f"Талбайн периметр {M(50)} м бол {M('x')} хэд вэ?",
            f"A holiday camp at Terelj has a rectangular volleyball court. In the picture its length is $2x + 1$ m and its width $x$ m. "
            f"The perimeter is ${50}$ m. Find $x$."),
        write=(f"Периметр нь урт, өргөний нийлбэрийн хоёр дахин: {M('2(2x + 1 + x)')}. Энэ нь {M(50)} тул {M(r2.tex())}.",
               "Тэгш өнцөгтийн урт хоёр, өргөн хоёр удаа орно.",
               f"The perimeter is twice length plus width: $2(2x + 1 + x)$. It equals ${50}$: ${r2.tex()}$.",
               "In a rectangle the length and the width each appear twice.",
               f"Периметрээс {M(r2.tex())} гарна.", f"The perimeter gives ${r2.tex()}$."),
        answer=(f"{M('x = 8')}: өргөн {M(8)} м, урт {M(17)} м.", f"$x = 8$: the width is ${8}$ m and the length ${17}$ m."),
        hint1=("Урт, өргөнийг нэмээд хоёр дахин авбал периметр гарна. Тэгшитгэлээ бичээрэй.",
               "Add length and width and double it to get the perimeter. Write the equation."),
        wrongs=[(Eqn([V(2), K(1), V(1)], [K(50)]), "$2x + 1 + x = 50$ гэж бичсэн бол хоёр талыг л нэмжээ. Хоёр дахин авах ёстой.",
                 "Writing $2x + 1 + x = 50$ adds only two sides; it must be doubled.", "missed-part-of-total"),
                (17, "$17$ бол талбайн урт. Асуулт $x$-ийг, өөрөөр хэлбэл өргөнийг асууж байна.", "$17$ is the length. The question asks for $x$, the width.",
                 "answered-wrong-quantity"),
                (Eqn([BR(2, V(2), K(1)), V(1)], [K(50)]), "$2(2x + 1) + x = 50$ гэж бичсэн бол өргөнийг нэг л удаа авчээ. Өргөн ч хоёр удаа орно.",
                 "Writing $2(2x + 1) + x = 50$ counts the width once. It appears twice too.", "missed-part-of-total")]))))
    return I


def part_E():
    I = []
    e1 = Eqn([V(5), K(-3)], [V(2), K(9)])
    I.append(("bare", "direct", 1, lambda vid, i: t_bare(vid, i, e1, O_BS, hint_both("x"))))
    I.append(("box", "direct", 2, lambda vid, i: t_box(vid, i, Eqn([K(7), V(-2)], [V(1), K(1)]), O_BS)))
    e3 = Eqn([V(3), K(7)], [V(5), K(-9)], "y")
    I.append(("bare", "direct", 2, lambda vid, i: t_bare(vid, i, e3, O_BS, hint_both("y"))))
    ph = Eqn([K(4000), V(2000)], [K(8000), V(1000)], "g")
    I.append(("graph", "figure", 2, lambda vid, i: t_story(vid, i, plan_story(
        "phone-plans", ph, "g",
        (f"Номин утасны хоёр багцаас сонгох гэж байна. А багц: сард {tg(4000)}, дээр нь гигабайт тутамд {tg(2000)}. "
         f"Б багц: сард {tg(8000)}, дээр нь гигабайт тутамд {tg(1000)}. Графикт хоёр багцын төлбөрийг үзүүлэв. "
         f"Хэдэн гигабайт хэрэглэвэл хоёр багцын төлбөр тэнцүү вэ?",
         f"Nomin is choosing between two phone plans. Plan A: {tg(4000)} a month plus {tg(2000)} per gigabyte. "
         f"Plan B: {tg(8000)} a month plus {tg(1000)} per gigabyte. The graph shows both costs. "
         f"For how many gigabytes do the two plans cost the same?"),
        (f"Графикийг уншъя: А багцын шулуун {W(4000, 'abl')} эхэлж гигабайт бүрд {W(2000, 'ins')} өсдөг, Б багцынх "
         f"{W(8000, 'abl')} эхэлж {W(1000, 'ins')} өсдөг. Гигабайтыг {M('g')} гэвэл {M(ph.tex())}.",
         "Хоёр шулууны огтлолцох цэг нь хоёр төлбөр тэнцэх үе. Тэнцүү гэдгийг тэгшитгэл болгож бичнэ.",
         f"Read the graph: plan A starts at ${ntex(4000)}$ and rises ${ntex(2000)}$ per gigabyte, plan B starts at "
         f"${ntex(8000)}$ and rises ${ntex(1000)}$. With $g$ gigabytes: ${ph.tex()}$.",
         "Where the two lines cross, the costs are equal; writing «equal» gives the equation.",
         f"Гигабайтыг {M('g')} гэвэл {M(ph.tex())}.", f"With $g$ gigabytes: ${ph.tex()}$."),
        (f"{M(4)} гигабайтад хоёр багц тэнцүү.", f"At ${4}$ gigabytes the plans cost the same."),
        ("Багц бүрийн төлбөрийг $g$ гигабайтаар бичээд хоёуланг тэнцүүлээрэй.", "Write each plan's cost for $g$ gigabytes and set them equal."),
        [(Eqn([K(4000), V(2000)], [K(8000)], "g"), "Б багцын гигабайтын төлбөрийг тооцоогүй бололтой: баруун талд $1\\,000g$ дутуу байна.",
          "Plan B's per-gigabyte charge was left out: the right side is missing $1\\,000g$.", "missed-part-of-total"),
         (12, "$4\\,000$-ыг нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: $1\\,000g = 8\\,000 + 4\\,000$ гэж бичвэл ийм хариу гарна.",
          "It looks as if $4\\,000$ crossed without changing sign: $1\\,000g = 8\\,000 + 4\\,000$ leads here.", "sign-not-changed-moving-term"),
         (Fr(4, 3), "$1\\,000g$-ийг шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: тэгвэл зүүн талд $3\\,000g$ гарна. Хоёр талаас $1\\,000g$-ийг хасах ёстой.",
          "It looks as if $1\\,000g$ crossed without changing sign, giving $3\\,000g$. Subtract $1\\,000g$ from both sides.",
          "sign-not-changed-moving-term")],
        lines2(ph, range(7), ("А багц", "Б багц"), ("Plan A", "Plan B"), ("₮", "₮"), ("гигабайт", "gigabytes"))))))
    I.append(("friends", "compare", 3, lambda vid, i: t_friends(
        vid, i, Eqn([V(8), K(-3)], [V(5), K(12)], "m"),
        dict(name=("Бат", "Bat"), lines=[Eqn([V(3), K(-3)], [K(12)]), Eqn([V(3)], [K(15)]), Eqn([V(1)], [K(5)])],
             how=("$m$-тэй гишүүдийг зүүн талд цуглуулсан.", "he gathered the $m$-terms on the left."), err=None),
        dict(name=("Сарнай", "Sarnai"), lines=[Eqn([K(-3)], [V(-3), K(12)]), Eqn([K(-15)], [V(-3)]), Eqn([V(1)], [K(5)])],
             how=("хоёр талаас $8m$-ийг хасаж, $m$-тэй гишүүдийг баруун талд цуглуулсан.",
                  "she subtracted $8m$ and gathered the $m$-terms on the right."), err=None))))
    I.append(("next", "compare", 3, lambda vid, i: t_next(vid, i, Eqn([V(-2), K(8)], [V(-5), K(-7)], "y"), Eqn([V(-2), K(8)], [V(-5), K(-7)], "y"))))
    e7 = Eqn([V(2), K(11)], [V(-3), K(1)], "n")
    I.append(("bare", "direct", 3, lambda vid, i: t_bare(vid, i, e7, O_BS, hint_both("n"))))
    tx = Eqn([K(2000), V(1000)], [K(4500), V(500)], "d")
    I.append(("graph", "figure", 3, lambda vid, i: t_story(vid, i, plan_story(
        "taxi", tx, "d",
        (f"Дарханд хоёр такси үйлчилдэг. Эхнийх нь суухад {tg(2000)}, километр тутамд {tg(1000)}. Хоёр дахь нь суухад {tg(4500)}, "
         f"километр тутамд {tg(500)}. Графикт хоёр таксины үнийг үзүүлэв. Хэдэн км явахад хоёр такси ижил үнэтэй вэ?",
         f"Two taxi companies work in Darkhan. The first charges {tg(2000)} to get in and {tg(1000)} per km; the second "
         f"{tg(4500)} to get in and {tg(500)} per km. The graph shows both fares. For how many km do they cost the same?"),
        (f"Графикаас: эхний такси {W(2000, 'abl')}, хоёр дахь нь {W(4500, 'abl')} эхэлж, км бүрд {W(1000, 'ins')} ба "
         f"{W(500, 'ins')} нэмэгдэнэ. Км-ийг {M('d')} гэвэл {M(tx.tex())}.",
         "Суух төлбөр нэг л удаа, км тутмын үнэ км-ийн тоогоор үржигдэнэ.",
         f"From the graph: the first fare starts at ${ntex(2000)}$, the second at ${ntex(4500)}$, rising ${ntex(1000)}$ and "
         f"${ntex(500)}$ per km. With $d$ km: ${tx.tex()}$.",
         "The pick-up charge counts once; the price per km is multiplied by the kilometres.",
         f"Км-ийг {M('d')} гэвэл {M(tx.tex())}.", f"With $d$ km: ${tx.tex()}$."),
        (f"{M(5)} км явахад хоёулаа {tg(7000)}.", f"At ${5}$ km both cost {tg(7000)}."),
        ("Такси бүрийн үнийг $d$ км-ээр бичээд тэнцүүлээрэй.", "Write each fare for $d$ km and set them equal."),
        [(Eqn([K(2000), V(1000)], [K(4500)], "d"), "Хоёр дахь таксины км тутмын төлбөрийг мартсан бололтой: баруун талд $500d$ дутуу.",
          "The second taxi's per-km charge is missing: the right side needs $500d$.", "missed-part-of-total"),
         (13, "$2\\,000$-ыг нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: $500d = 4\\,500 + 2\\,000$ гэж бичвэл ийм хариу гарна.",
          "It looks as if $2\\,000$ crossed without changing sign: $500d = 4\\,500 + 2\\,000$ leads here.", "sign-not-changed-moving-term"),
         (Eqn([V(1000)], [V(500)], "d"), "Суух төлбөрийг хоёуланд нь тооцоогүй бололтой. Суух төлбөр нь графикийн эхлэх цэг.",
          "Both pick-up charges were left out; they are where the lines start.", "missed-starting-amount")],
        lines2(tx, range(8), ("1-р такси", "2-р такси"), ("Taxi 1", "Taxi 2"), ("₮", "₮"), ("км", "km"))))))
    I.append(("box", "direct", 3, lambda vid, i: t_box(vid, i, Eqn([V(4), K(5)], [V(1), K(6)]), O_BS)))
    I.append(("param", "reverse", 4, lambda vid, i: t_param(vid, i, ("kx + 4 = 2x + 10", "{k}*{x} + 4 = 2*{x} + 10"), 3,
                                                           Eqn([V(3), K(4)], [K(16)], "k"), O_TS)))
    pl = Eqn([K(20000), V(3000)], [V(8000)], "v")
    I.append(("graph", "figure", 4, lambda vid, i: t_story(vid, i, plan_story(
        "pool", pl, "v",
        (f"Улаанбаатарын усан бассейнд хоёр төрлийн тасалбар бий. Гишүүнчлэлтэй бол сард {tg(20000)}, дээр нь орох бүрд {tg(3000)}. "
         f"Гишүүнчлэлгүй бол орох бүрд {tg(8000)}. Графикт хоёр төрлийн зардлыг үзүүлэв. Сард хэдэн удаа орвол хоёр зардал тэнцүү вэ?",
         f"A swimming pool in Ulaanbaatar has two kinds of ticket. With a membership: {tg(20000)} a month plus {tg(3000)} a visit. "
         f"Without: {tg(8000)} a visit. The graph shows both costs. For how many visits a month are they equal?"),
        (f"Графикаас: гишүүнчлэлтэй зардал {W(20000, 'abl')} эхэлж удаа бүрд {W(3000, 'ins')} өсдөг, гишүүнчлэлгүй нь "
         f"{W(0, 'abl')} эхэлж {W(8000, 'ins')} өсдөг. Удааг {M('v')} гэвэл {M(pl.tex())}.",
         "Сарын төлбөр нэг удаа, нэг удаагийн үнэ орсон тоогоор үржигдэнэ.",
         f"From the graph: with a membership the cost starts at ${ntex(20000)}$ and rises ${ntex(3000)}$ a visit; without, it "
         f"starts at $0$ and rises ${ntex(8000)}$. With $v$ visits: ${pl.tex()}$.",
         "The monthly fee counts once; the price per visit is multiplied by the visits.",
         f"Удааг {M('v')} гэвэл {M(pl.tex())}.", f"With $v$ visits: ${pl.tex()}$."),
        (f"Сард {M(4)} удаа орвол хоёулаа {tg(32000)}.", f"At ${4}$ visits both cost {tg(32000)}."),
        ("Хоёр төрлийн зардлыг $v$ удаагаар бичээд тэнцүүлээрэй.", "Write both costs for $v$ visits and set them equal."),
        [(Eqn([V(3000)], [V(8000)], "v"), "Гишүүнчлэлийн сарын төлбөрийг мартсан бололтой: зүүн талд $20\\,000$ дутуу.",
          "The monthly membership fee is missing on the left: $20\\,000$.", "missed-starting-amount"),
         (Eqn([K(20000)], [V(8000)], "v"), "Гишүүнчлэлтэй үед ч орох бүрд $3\\,000$₮ төлдгийг мартжээ: $20\\,000 + 3\\,000v$.",
          "Members still pay $3\\,000$₮ a visit: $20\\,000 + 3\\,000v$.", "missed-part-of-total"),
         (Fr(20, 11), "$3\\,000v$-ийг шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: тэгвэл $11\\,000v$ гарна. Хоёр талаас $3\\,000v$-ийг хасна.",
          "It looks as if $3\\,000v$ crossed without changing sign, giving $11\\,000v$. Subtract $3\\,000v$ from both sides.",
          "sign-not-changed-moving-term")],
        lines2(pl, range(7), ("Гишүүнчлэлтэй", "Гишүүнчлэлгүй"), ("Member", "No membership"), ("₮", "₮"), ("удаа", "visits"))))))
    I.append(("param", "reverse", 4, lambda vid, i: t_param(
        vid, i, ("x - k = 3x + 1", "{x} - {k} = 3*{x} + 1"), -2, Eqn([K(-2), V(-1)], [K(-5)], "k"), O_TS,
        extra=[(-5, "$x = -2$ утгыг хасах тэмдэггүй, $2$ гэж орлуулсан бололтой: $2 - k = 7$ гарна. Сөрөг тоог хаалтанд хийж орлуулна: $-2 - k = -5$.",
                "It looks as if $2$ was substituted instead of $-2$, giving $2 - k = 7$. Put the negative value in: $-2 - k = -5$.",
                "dropped-negative-substituting")])))
    return I


def part_F():
    I = []
    pz = Eqn([V(4), K(9)], [K(1)])
    I.append(("puzzle", "modelling", 1, lambda vid, i: t_story(vid, i, S(
        "think-of-a-number", var="x", eq=pz,
        st=(f"Энхжин: «Би нэг тоо бодлоо. Түүнийг {W(4, 'ins')} үржүүлээд {W(9, 'acc')} нэмэхэд {M(1)} гарсан.» Энхжин ямар тоо бодсон бэ?",
            f"Enkhjin says: «I thought of a number, multiplied it by ${4}$ and added ${9}$. I got ${1}$.» What was her number?"),
        write=(f"Бодсон тоог {M('x')} гэе. {W(4, 'ins')} үржүүлбэл {M('4x')}, {W(9, 'acc')} нэмбэл {M('4x + 9')}. Энэ нь {M(1)} тул {M(pz.tex())}.",
               "Өгүүлбэрийн үйлдлүүдийг хэлсэн дарааллаар нь бичнэ: эхлээд үржүүлж, дараа нь нэмнэ.",
               f"Call the number $x$. Times ${4}$ is $4x$; adding ${9}$ gives $4x + 9$. That is ${1}$: ${pz.tex()}$.",
               "Write the operations in the order they are said: multiply first, then add.",
               f"Тоог {M('x')} гэвэл {M(pz.tex())}.", f"With the number as $x$: ${pz.tex()}$."),
        answer=(f"Энхжин {M(-2)} бодсон.", f"Her number was ${-2}$."),
        hint1=("Бодсон тоог $x$ гэе. Түүнд юу хийснийг дарааллаар нь бичээрэй.", "Call the number $x$ and write what was done to it, in order."),
        wrongs=[(Eqn([V(4), K(-9)], [K(1)]), "«Нэмэхэд» гэдгийг хасах гэж ойлгосон бололтой: $4x - 9 = 1$.",
                 "«Added» was read as «subtracted»: $4x - 9 = 1$.", "added-subtracted-confused"),
                (Eqn([BR(4, V(1), K(9))], [K(1)]), "$4(x + 9)$ гэж бичвэл эхлээд нэмээд дараа нь үржүүлсэн болно. Энхжин эхлээд үржүүлсэн.",
                 "$4(x + 9)$ adds first and multiplies after. Enkhjin multiplied first.", "order-of-operations"),
                (-8, "$4x = -8$ хүртэл зөв. Гэхдээ $-8$ нь $4x$: $4$-т хуваана.", "Up to $4x = -8$ is right, but that is $4x$: divide by $4$.",
                 "stopped-before-dividing")]))))
    k8 = Eqn([V(4), V(3)], [K(10500)])
    I.append(("story", "modelling", 1, lambda vid, i: t_story(vid, i, S(
        "khuushuur", var="x", eq=k8,
        st=(f"Наадмаар Дорж {M(4)}, Энхжин {M(3)} хуушуур авав. Хуушуур бүр ижил үнэтэй. Тэд нийлээд {tg(10500)} төлсөн бол нэг хуушуур хэдэн төгрөг вэ?",
            f"At Naadam Dorj bought ${4}$ khuushuur and Enkhjin ${3}$. They all cost the same, and together they paid {tg(10500)}. "
            f"How much is one khuushuur?"),
        write=(f"Нэг хуушуурын үнийг {M('x')} гэе. Дорж {M('4x')}, Энхжин {M('3x')} төлсөн тул {M(k8.tex())}.",
               "Ижил үнэтэй зүйлсийн зардлыг төсөөтэй гишүүд болгож нэгтгэнэ.",
               f"Let one khuushuur cost $x$. Dorj paid $4x$ and Enkhjin $3x$, so ${k8.tex()}$.",
               "Costs of identically priced items are like terms and add together.",
               f"Нэг хуушуурыг {M('x')} гэвэл {M(k8.tex())}.", f"With one khuushuur as $x$: ${k8.tex()}$."),
        answer=(f"Нэг хуушуур {tg(1500)}.", f"One khuushuur costs {tg(1500)}."),
        hint1=("Нэг хуушуурын үнийг $x$ гэвэл хоёулаа нийт хэдэн хуушуур авсан бэ?", "If one khuushuur costs $x$, how many did they buy in all?"),
        wrongs=[(Fr(10500, 4), "Зөвхөн Доржийн авсныг тоолсон бололтой. Хоёулаа нийлээд $7$ хуушуур авсан.",
                 "Only Dorj's were counted. Together they bought $7$.", "missed-part-of-total"),
                (Eqn([V(4), K(3)], [K(10500)]), "$4x + 3$ гэж бичсэн бол Энхжины хуушуурын тоог мөнгө мэт нэмжээ. Түүний төлсөн нь $3x$.",
                 "Writing $4x + 3$ adds Enkhjin's count as if it were money. She paid $3x$.", "count-used-as-amount"),
                (10500, "$7x = 10\\,500$ хүртэл зөв. Гэхдээ энэ нь нийт мөнгө: $7$-д хуваана.",
                 "Up to $7x = 10\\,500$ is right, but that is the total: divide by $7$.", "stopped-before-dividing")]))))
    I.append(("story", "modelling", 2, lambda vid, i: t_story(vid, i, dict(old_story(4), key=S("cinema")["key"], tags=STORY4_TAGS))))
    I.append(("table", "figure", 2, lambda vid, i: t_table(
        vid, i, 2, 3, 19, O_TS, head=(("км", "Төлбөр"), ("km", "Fare")),
        text=(f"Улаанбаатарт таксины төлбөр явсан км-ээс хамаарна. Хүснэгтэд төлбөрийг мянган төгрөгөөр үзүүлэв. "
              f"Нийт {M(19)} мянган төгрөг төлсөн бол хэдэн км явсан бэ?",
              f"In Ulaanbaatar a taxi fare depends on the distance. The table gives fares in thousands of tögrög. "
              f"A ride cost ${19}$ thousand. How many km was it?"),
        answer=(f"{M(8)} км явсан.", f"It was ${8}$ km."))))
    pg = Eqn([K(3), V(2)], [K(25)], "w")
    I.append(("bars", "figure", 2, lambda vid, i: t_story(vid, i, S(
        "plant", var="w", eq=pg, fig=bars(3, 2, [1, 2, 3, 4], lambda w_: f"{w_}-р долоо хоног", lambda w_: f"Week {w_}", ("см", "cm")),
        st=(f"Номин цонхныхоо тавцан дээр ногоо ургуулж байна. Графикт ургамлын өндрийг долоо хоног бүрийн эцэст үзүүлэв. "
            f"Ургамал ижил хурдаар ургавал хэд дэх долоо хоногийн эцэст {M(25)} см болох вэ?",
            f"Nomin is growing a plant on her windowsill. The chart shows its height at the end of each week. If it keeps growing "
            f"at the same rate, at the end of which week will it be ${25}$ cm?"),
        write=(f"Графикаас: долоо хоног бүр {M('7 - 5 = 2')} см ургадаг, тэгэхээр тарихад {M('5 - 2 = 3')} см байсан. Долоо хоногийг {M('w')} "
               f"гэвэл {M(pg.tex())}.",
               "Баганын өсөлт нь долоо хоногийн ургалт; эхлэлийг нэг алхам буцааж олно.",
               f"From the chart: it grows $7 - 5 = 2$ cm a week, so it was $5 - 2 = 3$ cm at the start. After $w$ weeks: ${pg.tex()}$.",
               "The rise from bar to bar is the weekly growth; step back once to find the start.",
               f"Долоо хоногийг {M('w')} гэвэл {M(pg.tex())}.", f"With $w$ weeks: ${pg.tex()}$."),
        answer=(f"{M(11)} дэх долоо хоногийн эцэст.", f"At the end of week ${11}$."),
        hint1=("Багана бүр өмнөхөөсөө хэдэн см өндөр вэ? Эхлэхдээ хэдэн см байсан бэ?", "How many cm taller is each bar? How tall was it at the start?"),
        wrongs=[(Eqn([K(5), V(2)], [K(25)], "w"), "Эхний баганын $5$-ыг эхлэл гэж авсан бололтой. $5$ бол $1$-р долоо хоногийн эцсийнх.",
                 "The first bar's $5$ was taken as the start; it is the end of week $1$.", "misread-starting-value"),
                (Fr(25, 2), "Эхний өндрийг тооцоогүй бололтой: $2w = 25$ гэж бичжээ.", "The starting height was left out: $2w = 25$.",
                 "missed-starting-amount"),
                (22, "$2w = 22$ хүртэл зөв. Гэхдээ $22$ нь см: $2$-т хуваавал долоо хоног гарна.",
                 "Up to $2w = 22$ is right, but $22$ is centimetres: divide by $2$ for the weeks.", "stopped-before-dividing")]))))
    bs = Eqn([K(20), V(60)], [K(380)], "t")
    I.append(("graph", "figure", 3, lambda vid, i: t_story(vid, i, S(
        "bus-erdenet", var="t", eq=bs, fig=line1(20, 60, range(5), ("км", "km"), ("цаг", "hours")),
        st=(f"Автобус Улаанбаатараас Эрдэнэт рүү явж байна. Графикт автобус Улаанбаатараас хэдэн км явсныг цаг тутам үзүүлэв. "
            f"Эрдэнэт хүртэл {M(380)} км бол хэдэн цагийн дараа хүрэх вэ?",
            f"A bus is going from Ulaanbaatar to Erdenet. The graph shows how far from Ulaanbaatar it is, hour by hour. "
            f"Erdenet is ${380}$ km away. After how many hours does the bus arrive?"),
        write=(f"Графикаас: {M(0)} цагт автобус {M(20)} км-т байсан, цаг тутам {M('80 - 20 = 60')} км явдаг. Цагийг {M('t')} гэвэл "
               f"{M(bs.tex())}.",
               "Графикийн эхлэх утга нь анхны зай, цаг бүрийн өсөлт нь хурд.",
               f"From the graph: at hour $0$ the bus was at $20$ km and it covers $80 - 20 = 60$ km an hour. With $t$ hours: ${bs.tex()}$.",
               "The graph's starting value is the first distance; the rise each hour is the speed.",
               f"Цагийг {M('t')} гэвэл {M(bs.tex())}.", f"With $t$ hours: ${bs.tex()}$."),
        answer=(f"{M(6)} цагийн дараа хүрнэ.", f"It arrives after ${6}$ hours."),
        hint1=("Графикаас автобусны эхлэх зай болон цагийн хурдыг уншаарай.", "Read the starting distance and the speed per hour off the graph."),
        wrongs=[(Eqn([V(60)], [K(380)], "t"), "Эхний $20$ км-ийг тооцоогүй бололтой. Автобус $0$ цагт $20$ км-т байсан.",
                 "The first $20$ km were left out: at hour $0$ the bus was already at $20$ km.", "missed-starting-amount"),
                (Eqn([V(80)], [K(380)], "t"), "$1$ цагийн дараах $80$ км-ийг хурд гэж авсан байна. Хурд нь цаг бүрийн өсөлт: $60$.",
                 "The $80$ km after one hour was taken as the speed. The speed is the rise per hour: $60$.", "misread-starting-value"),
                (360, "$60t = 360$ хүртэл зөв. Гэхдээ $360$ нь км: $60$-д хуваавал цаг гарна.",
                 "Up to $60t = 360$ is right, but $360$ is kilometres: divide by $60$ for hours.", "stopped-before-dividing")]))))
    I.append(("write", "modelling", 3, lambda vid, i: t_write(vid, i, dict(old_story(7), key=S("school-trip")["key"], st_write=(
        f"Сургуулийн {M(150)} сурагч Эрдэнэт рүү аялалд явна. {M(30)} сурагч микроавтобусаар, бусад нь том автобусаар явна. "
        f"Нэг том автобусанд {M(40)} сурагч сууна. Том автобусны тоог {M('x')} гэвэл аль тэгшитгэл зөв бэ?",
        f"${150}$ pupils are going to Erdenet. ${30}$ go by minibus and the rest by coach; a coach takes ${40}$. "
        f"With $x$ coaches, which equation is right?"),
        wrongs=[(Eqn([V(40)], [K(150)]), "Микроавтобусаар явах $30$ сурагчийг тооцоогүй.", "The $30$ pupils in the minibus are left out.",
                 "missed-part-of-total"),
                (Eqn([V(40)], [K(150), K(30)]), "$30$-ыг хасахын оронд нэмсэн: тэд том автобусанд суухгүй.",
                 "The $30$ are added instead of subtracted: they do not ride in a coach.", "added-subtracted-confused"),
                (Eqn([V(40), K(-30)], [K(150)]), "Микроавтобусны сурагчдыг хассан байна. Тэд нийт $150$-д ордог тул нэмнэ: $40x + 30 = 150$.",
                 "This subtracts the minibus pupils; they are part of the $150$, so they are added: $40x + 30 = 150$.",
                 "added-subtracted-confused")]))))
    I.append(("story", "modelling", 3, lambda vid, i: t_story(vid, i, dict(
        old_story(1), key=S("sister-brother")["key"],
        tags=["answered-wrong-quantity", "missed-part-of-total", "ignored-difference"]))))
    sb = Eqn([V("0.75")], [K(54000)])
    I.append(("percent", "recall", 3, lambda vid, i: t_story(vid, i, S(
        "boots-sale", var="x", eq=sb,
        st=(f"Өвлийн гутал {M('25' + chr(92) + '%')}-ийн хямдралтай {tg(54000)} болжээ. Гутлын хямдралаас өмнөх үнэ хэд байсан бэ?",
            f"Winter boots cost {tg(54000)} after a ${'25' + chr(92) + '%'}$ discount. What did they cost before the discount?"),
        write=(f"Хямдралаас өмнөх үнийг {M('x')} гэе. {M('25' + chr(92) + '%')} хямдарвал {M('75' + chr(92) + '%')} буюу {M('0.75x')} үлдэнэ. "
               f"Иймд {M(sb.tex())}.",
               "Хямдралын дараах үнэ нь анхны үнийн үлдсэн хувь.",
               f"Let the price before be $x$. After ${'25' + chr(92) + '%'}$ off, ${'75' + chr(92) + '%'}$ is left: $0.75x$. So ${sb.tex()}$.",
               "The sale price is the remaining percent of the original price.",
               f"Анхны үнийг {M('x')} гэвэл {M(sb.tex())}.", f"With the original price $x$: ${sb.tex()}$."),
        answer=(f"Хямдралаас өмнө {tg(72000)} байсан.", f"Before the discount they cost {tg(72000)}."),
        hint1=("Хямдралын дараа анхны үнийн хэдэн хувь үлдэх вэ?", "After the discount, what percent of the original price is left?"),
        wrongs=[(67500, "$54\\,000$ дээр түүний $25\\%$-ийг нэмсэн бололтой. Хямдрал анхны үнээс тооцогдоно: $0.75x = 54\\,000$.",
                 "That adds $25\\%$ of $54\\,000$. The discount is taken from the original price: $0.75x = 54\\,000$.", "percent-of-wrong-base"),
                (Eqn([V("0.25")], [K(54000)]), "$0.25x = 54\\,000$ гэж бичсэн бол хямдарсан хэсгийг төлсөн мэт үзжээ.",
                 "Writing $0.25x = 54\\,000$ treats the discount as the price paid.", "discount-as-price"),
                (40500, "$54\\,000$-аас дахин $25\\%$ хассан байна: хямдралтай үнийг дахин хямдруулсан хэрэг.",
                 "That takes $25\\%$ off $54\\,000$ again: the sale price discounted twice.", "percent-of-wrong-base")]))))
    I.append(("table", "figure", 3, lambda vid, i: t_table(
        vid, i, 3, -12, 6, O_TS, head=(("Цаг", "Температур"), ("Hour", "Temperature")),
        text=(f"Өвлийн өглөө агаар цаг тутам ижил хэмжээгээр дулаарч байна. Хүснэгтэд өглөөний {M(8)} цагаас хойш цаг бүрийн "
              f"температурыг градусаар үзүүлэв. Хэдэн цагийн дараа {M(6)} градус болох вэ?",
              f"On a winter morning it warms up by the same amount every hour. The table shows the temperature in degrees each hour "
              f"from ${8}$ o'clock. After how many hours will it be ${6}$ degrees?"),
        answer=(f"{M(6)} цагийн дараа.", f"After ${6}$ hours."))))
    bt = Eqn([K(100), V(-12)], [K(16)], "h")
    I.append(("graph", "figure", 4, lambda vid, i: t_story(vid, i, S(
        "battery", var="h", eq=bt, fig=line1(100, -12, range(5), ("%", "%"), ("цаг", "hours")),
        st=(f"Сарнайн утасны цэнэг цаг тутам ижил хэмжээгээр багасч байна. Графикт цэнэгийг хувиар үзүүлэв. "
            f"Хэдэн цагийн дараа цэнэг {M('16' + chr(92) + '%')} болох вэ?",
            f"Sarnai's phone battery drops by the same amount every hour. The graph shows the charge in percent. "
            f"After how many hours will it be at ${'16' + chr(92) + '%'}$?"),
        write=(f"Графикаас: цэнэг {M('100' + chr(92) + '%')}-иас эхэлж цаг тутам {M('100 - 88 = 12')} хувиар багасдаг. Цагийг {M('h')} "
               f"гэвэл {M(bt.tex())}.",
               "Багасаж байгаа тул цагийн өөрчлөлт хасах тэмдэгтэй.",
               f"From the graph: the charge starts at $100\\%$ and drops $100 - 88 = 12$ points an hour. With $h$ hours: ${bt.tex()}$.",
               "It is going down, so the change per hour carries a minus sign.",
               f"Цагийг {M('h')} гэвэл {M(bt.tex())}.", f"With $h$ hours: ${bt.tex()}$."),
        answer=(f"{M(7)} цагийн дараа.", f"After ${7}$ hours."),
        hint1=("Графикаас эхний цэнэг болон цаг тутмын бууралтыг уншаарай.", "Read the starting charge and the drop per hour off the graph."),
        wrongs=[(-7, "$-12$-т хуваахдаа хасах тэмдгийг алдсан бололтой: хасахыг хасахад хуваавал нэмэх гарна.",
                 "The minus sign was lost dividing by $-12$: a negative divided by a negative is positive.", "lost-sign-dividing-by-negative"),
                (Fr(-29, 3), "$100$-г нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: $-12h = 16 + 100$.",
                 "It looks as if $100$ crossed without changing sign: $-12h = 16 + 100$.", "sign-not-changed-moving-term"),
                (84, "$-12h = -84$ хүртэл зөв. Гэхдээ $84$ нь хувь: $-12$-т хуваавал цаг гарна.",
                 "Up to $-12h = -84$ is right, but $84$ is percent: divide by $-12$ for hours.", "stopped-before-dividing")]))))
    I.append(("write", "modelling", 4, lambda vid, i: t_write(vid, i, dict(old_story(8), key=S("father-son")["key"], st_write=(
        f"Доржийн аав одоо Доржоос {M(3)} дахин ахмад. {M(10)} жилийн дараа аав нь Доржоос яг {M(2)} дахин ахмад болно. "
        f"Доржийн одоогийн насыг {M('x')} гэвэл аль тэгшитгэл зөв бэ?",
        f"Dorj's father is now ${3}$ times as old as Dorj. In ${10}$ years he will be exactly ${2}$ times as old. "
        f"With Dorj's age now as $x$, which equation is right?"),
        wrongs=[(Eqn([V(3)], [BR(2, V(1), K(10))]), "Аавын насанд $10$ нэмээгүй байна: арван жилийн дараа аав ч мөн ахина.",
                 "The father's age is missing the added $10$: he gets ten years older too.", "missed-part-of-total"),
                (Eqn([V(3), K(10)], [V(2), K(10)]), "$2$-оор зөвхөн $x$-ийг үржүүлжээ. Доржийн тэр үеийн нас бүхлээрээ хоёр дахин: $2(x + 10)$.",
                 "Only the $x$ is doubled. Dorj's whole age then is doubled: $2(x + 10)$.", "distribute-first-term-only"),
                (Eqn([V(3), K(10)], [V(2)]), "Доржийн насанд $10$ нэмэхээ мартжээ: арван жилийн дараа Дорж $x + 10$ настай.",
                 "Dorj's age is missing the added $10$: in ten years he is $x + 10$.", "missed-part-of-total")]))))
    return I


def part_G():
    C = find_error_cases()
    I = []
    I.append(("find_error", "find-the-mistake", 2, lambda vid, i: find_error_variant(vid, i, C[5])))
    I.append(("diagnose", "find-the-mistake", 2, lambda vid, i: t_diagnose(vid, i, C[6], "combine")))
    I.append(("claim", "compare", 2, lambda vid, i: t_claim(vid, i, "m", subst_cases()[0], ("Номин", "Nomin"))))
    I.append(("find_error", "find-the-mistake", 3, lambda vid, i: find_error_variant(vid, i, C[0])))
    I.append(("friends", "find-the-mistake", 3, lambda vid, i: t_friends(
        vid, i, Eqn([V(5), K(-4)], [V(2), K(11)], "y"),
        dict(name=("Тэмүүлэн", "Temuulen"), lines=[Eqn([V(3), K(-4)], [K(11)]), Eqn([V(3)], [K(7)]), Eqn([V(1)], [K(Fr(7, 3))])],
             how=("$y$-тэй гишүүдийг зүүн талд цуглуулсан.", "he gathered the $y$-terms on the left."),
             err=(f"{W(-4, 'acc')} шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй: $11 - 4$ гэж бодсон. $3y = 11 + 4 = 15$ байх ёстой.",
                  "the $-4$ crossed without changing sign, giving $11 - 4$. It should be $3y = 11 + 4 = 15$.")),
        dict(name=("Энхжин", "Enkhjin"), lines=[Eqn([K(-4)], [V(-3), K(11)]), Eqn([K(-15)], [V(-3)]), Eqn([V(1)], [K(5)])],
             how=("хоёр талаас $5y$-ийг хасаж, $y$-тэй гишүүдийг баруун талд цуглуулсан.",
                  "she subtracted $5y$ and gathered the $y$-terms on the right."), err=None))))
    I.append(("correct_line", "find-the-mistake", 3, lambda vid, i: t_correct_line(
        vid, i, Eqn([BR(4, V(1), K(3)), BR(-1, V(1), K(-6))], [BR(2, V(1), K(7)), K(1)]), O_MS)))
    I.append(("diagnose", "find-the-mistake", 3, lambda vid, i: t_diagnose(vid, i, C[7], "sign")))
    I.append(("find_error", "find-the-mistake", 4, lambda vid, i: find_error_variant(vid, i, C[3])))
    I.append(("friends", "find-the-mistake", 4, lambda vid, i: t_friends(
        vid, i, Eqn([FR(2, V(1)), K(1)], [FR(3, V(1)), K(2)]),
        dict(name=("Номин", "Nomin"), lines=[Eqn([V(3), K(6)], [V(2), K(12)]), Eqn([V(1), K(6)], [K(12)]), Eqn([V(1)], [K(6)])],
             how=(f"хоёр талыг {W(6, 'ins')} үржүүлсэн.", "she multiplied both sides by $6$."), err=None),
        dict(name=("Дорж", "Dorj"), lines=[Eqn([V(3), K(1)], [V(2), K(2)]), Eqn([V(1), K(1)], [K(2)]), Eqn([V(1)], [K(1)])],
             how=(f"хоёр талыг {W(6, 'ins')} үржүүлсэн.", "he multiplied both sides by $6$."),
             err=(f"$1$ ба {W(2, 'acc')} {W(6, 'ins')} үржүүлээгүй. $3x + 6 = 2x + 12$ байх ёстой.",
                  "the $1$ and the $2$ were not multiplied by $6$. It should be $3x + 6 = 2x + 12$.")))))
    I.append(("whose", "compare", 4, lambda vid, i: t_whose(vid, i, Eqn([BR(-2, V(1), K(3))], [K(4)], "n"),
                                                           (("Сарнай", "Sarnai"), "neg_sign"), (("Дорж", "Dorj"), "neg"), O_ALL)))
    return I


def part_H():
    I = []
    e1 = Eqn([BR(3, V(2), K(-1)), BR(-2, V(1), K(4))], [BR(5, V(1), K(-3))])
    I.append(("bare", "multi-step", 3, lambda vid, i: t_bare(vid, i, e1, O_MS, HINT_MS)))
    I.append(("classify", "explain", 3, lambda vid, i: how_many_variant(vid, i, Eqn([BR(2, V(1), K(-1)), K(4)], [V(2), K(5)]))))
    e3 = Eqn([FR(5, V(2), K(-1))], [FR(3, V(1), K(4))], "m")
    I.append(("bare", "multi-step", 3, lambda vid, i: t_bare(vid, i, e3, O_MS, HINT_MS)))
    cd = Eqn([K(20), V(-2)], [K(16), V(-2)], "t")
    I.append(("graph", "figure", 3, lambda vid, i: t_story_count(
        vid, i, cd,
        (f"Хоёр лааг зэрэг асаав. Эхнийх нь {M(20)} см, хоёр дахь нь {M(16)} см урттай бөгөөд хоёулаа цагт {M(2)} см-ээр богиносно. "
         f"Графикт тэдгээрийн уртыг цаг тутам үзүүлэв. Хоёр лааны урт хэзээ тэнцэх вэ?",
         f"Two candles are lit together: one ${20}$ cm long, the other ${16}$ cm, and both burn ${2}$ cm an hour. The graph shows "
         f"their lengths hour by hour. When are they the same length?"),
        (f"Цагийг {M('t')} гэвэл эхний лаа {M('20 - 2t')}, хоёр дахь нь {M('16 - 2t')} см. Урт тэнцүү гэдгээс {M(cd.tex())}.",
         f"After $t$ hours the candles are $20 - 2t$ and $16 - 2t$ cm long. Equal lengths: ${cd.tex()}$."),
        CATS_TIME,
        ("$20 = 16$ худал: хоёр лааны зөрүү үргэлж $4$ см хэвээр тул тэд хэзээ ч тэнцэхгүй.",
         "$20 = 16$ is false: the difference stays $4$ cm, so they are never the same length."),
        fig=lines2(cd, range(6), ("1-р лаа", "2-р лаа"), ("Candle 1", "Candle 2"), ("см", "cm"), ("цаг", "hours")))))
    I.append(("make", "reverse", 4, lambda vid, i: t_make(
        vid, i, "x", lambda k: Eqn([V(3), K(5)], [V(k), K(2)]), ("$3x + 5 = kx + 2$", "$3x + 5 = kx + 2$"), 3, "none",
        [(-3, "Коэффициентууд эсрэг тэмдэгтэй байх ёстой гэж бодсон бол $k = -3$. Тэгвэл $3x + 5 = -3x + 2$ болж яг нэг шийдтэй.",
          "Thinking the coefficients must be opposite gives $k = -3$, but then $3x + 5 = -3x + 2$ has exactly one solution.", "opposite-coefficients"),
         (0, "$k = 0$ бол баруун талд $x$ алга болох ч зүүн талд $3x$ үлдэж, тэгшитгэл нэг шийдтэй.",
          "$k = 0$ removes $x$ on the right only; $3x$ stays on the left, so there is one solution.", "cancelled-means-no-solution"),
         (5, "$k$-г зүүн талын тогтмол $5$-тай тэнцүүлсэн бололтой. Харьцуулах ёстой нь $x$-ийн коэффициентууд.",
          "$k$ was matched to the constant $5$. It is the coefficients of $x$ that must match.", "coefficient-constant-confused")])))
    tri = Eqn([V(1), V(1), K(4), BR(2, V(1), K(-1))], [K(30)])
    tf = geo_poly([(0, 0), (6, 0), (2, 3)], ["2(x - 1)", "x + 4", "x"])
    I.append(("geo", "figure", 4, lambda vid, i: t_story(vid, i, S(
        "triangle-fence", var="x", eq=tri, fig=tf,
        st=(f"Хөвсгөлийн аялалын баазад гурвалжин хэлбэртэй хашаа бий. Зурагт талуудыг метрээр үзүүлэв: {M('x')}, {M('x + 4')} ба "
            f"{M('2(x - 1)')}. Хашааны периметр {M(30)} м бол {M('x')} хэд вэ?",
            f"A tourist camp at Khövsgöl has a triangular fence. The picture gives the sides in metres: $x$, $x + 4$ and $2(x - 1)$. "
            f"The perimeter is ${30}$ m. Find $x$."),
        write=(f"Периметр нь гурван талын нийлбэр: {M(tri.tex())}.", "Периметр бол бүх талын уртын нийлбэр.",
               f"The perimeter is the sum of the three sides: ${tri.tex()}$.", "The perimeter is the sum of all the sides.",
               f"Талуудыг нэмбэл {M(tri.tex())}.", f"Adding the sides: ${tri.tex()}$."),
        answer=(f"{M('x = 7')}: талууд нь {M(7)}, {M(11)} ба {M(12)} м.", f"$x = 7$: the sides are ${7}$, ${11}$ and ${12}$ m."),
        hint1=("Гурван талын уртыг нэмээд периметртэй тэнцүүлээрэй. Хаалтыг нээхээ мартуузай.",
               "Add the three sides and set them equal to the perimeter. Remember to open the bracket."),
        wrongs=[(Eqn([V(1), V(1), K(4), V(2), K(-1)], [K(30)]), "$2(x - 1)$ гэдгийг $2x - 1$ гэж нээжээ. $2$ нь хоёр гишүүнийг хоёуланг нь үржүүлнэ: $2x - 2$.",
                 "$2(x - 1)$ was opened as $2x - 1$. The $2$ multiplies both terms: $2x - 2$.", "distribute-first-term-only"),
                (12, "$12$ бол хамгийн урт тал $2(x - 1)$. Асуулт $x$-ийг асууж байна.", "$12$ is the longest side, $2(x - 1)$. The question asks for $x$.",
                 "answered-wrong-quantity"),
                (Eqn([V(1), K(4), BR(2, V(1), K(-1))], [K(30)]), "$x$ талыг нэмэхээ мартжээ: гурвалжин гурван талтай.",
                 "The side $x$ was left out: a triangle has three sides.", "missed-part-of-total")]))))
    I.append(("classify", "explain", 4, lambda vid, i: how_many_variant(vid, i, Eqn([BR(3, V(1), K(2))], [V(3), K(6)]))))
    I.append(("explain_self", "explain", 4, lambda vid, i: t_self(
        vid, i, ("$2x + 5 = 2x + 7$ тэгшитгэл яагаад шийдгүй вэ? Тайлбарлаад, өөрийн хариугаа загвар хариутай харьцуулаарай.",
                 "Why does $2x + 5 = 2x + 7$ have no solution? Explain, then compare your answer with the model."),
        ("Хоёр талаас $2x$-ийг хасвал $5 = 7$ үлдэнэ. Энэ нь худал бөгөөд үл мэдэгдэхээс хамаарахгүй тул ямар ч $x$ тохирохгүй",
         "Subtracting $2x$ from both sides leaves $5 = 7$, which is false whatever $x$ is, so no value works"),
        [("$x$ хорогдсон тул $x = 0$", "$x$ cancels, so $x = 0$",
          "$x = 0$ үед зүүн тал $5$, баруун тал $7$: тэнцэхгүй. $x$ хорогдох нь $x = 0$ гэсэн үг биш.",
          "At $x = 0$ the sides are $5$ and $7$: not equal. «$x$ cancels» does not mean $x = 0$.", "cancelled-means-x-zero"),
         ("Хоёр талд $2x$ ижил тул төгсгөлгүй олон шийдтэй", "Both sides have $2x$, so there are infinitely many solutions",
          "Төгсгөлгүй олон шийдтэй байхын тулд хоёр тал бүхэлдээ ижил байх ёстой. Энд тогтмолууд $5$ ба $7$ ялгаатай.",
          "For infinitely many solutions the whole sides must match. Here the constants $5$ and $7$ differ.", "cancelled-means-infinite"),
         ("Хоёр талыг $2$-т хуваавал $x + 5 = x + 7$ болж $x = 2$", "Dividing both sides by $2$ gives $x + 5 = x + 7$, so $x = 2$",
          "Хоёр талыг $2$-т хуваахдаа $5$, $7$-г хуваагаагүй. Мөн $x + 5 = x + 7$-оос ч $5 = 7$ гарна: $x = 2$ гарахгүй.",
          "Dividing by $2$ must divide the $5$ and the $7$ too, and even $x + 5 = x + 7$ leaves $5 = 7$: it never gives $x = 2$.",
          "divided-one-term-only")],
        [dict(mn=dict(do="Хоёр талаас $2x$-ийг хасъя: $5 = 7$.", why="Хоёр талд ижил үйлдэл хийхэд тэнцэтгэл алдагдахгүй."),
              en=dict(do="Subtract $2x$ from both sides: $5 = 7$.", why="Doing the same to both sides keeps the balance.")),
         dict(mn=dict(do="$5 = 7$ худал, мөн $x$ үлдээгүй тул ямар ч утга тэнцэтгэлийг үнэн болгохгүй."),
              en=dict(do="$5 = 7$ is false and no $x$ is left, so no value can make it true.")),
         dict(mn=dict(do="Шалгая: $x = 0$ үед $5$ ба $7$; $x = 1$ үед $7$ ба $9$. Зөрүү үргэлж $2$."),
              en=dict(do="Check: at $x = 0$ the sides are $5$ and $7$; at $x = 1$, $7$ and $9$. They always differ by $2$."))],
        [("Хоёр талаас ижил гишүүн хасвал юу үлдэх вэ?", "What is left if you subtract the same term from both sides?"),
         ("$2x$-ийг хасвал $5 = 7$ үлдэнэ. Энэ үнэн үү?", "Subtracting $2x$ leaves $5 = 7$. Is that true?")],
        ("Хоёр талаас $2x$-ийг хасахад $5 = 7$ гэсэн худал тэнцэтгэл үлддэг тул шийдгүй.",
         "Subtracting $2x$ leaves the false $5 = 7$, so there is no solution."),
        ["Ne(5, 7)", "Eq(2*0 + 5, 5)", "Eq(2*0 + 7, 7)", "Eq((2*1 + 7) - (2*1 + 5), 2)"])))
    b2 = Eqn([K(30), V(60)], [V(60)], "t")
    I.append(("graph", "figure", 4, lambda vid, i: t_story_count(
        vid, i, b2,
        (f"Дархан руу хоёр автобус нэгэн зэрэг хөдөлжээ. Эхнийх нь Улаанбаатараас {M(30)} км-ийн зайнаас, хоёр дахь нь Улаанбаатараас гарсан. "
         f"Хоёулаа цагт {M(60)} км явна. Графикт хоёр автобусны Улаанбаатараас явсан зайг үзүүлэв. Хоёр дахь автобус эхнийхийг хэзээ гүйцэх вэ?",
         f"Two buses set off for Darkhan at the same moment: the first from ${30}$ km outside Ulaanbaatar, the second from the city. "
         f"Both travel ${60}$ km an hour. The graph shows their distances from Ulaanbaatar. When does the second bus catch the first?"),
        (f"Цагийг {M('t')} гэвэл эхний автобус {M('30 + 60t')}, хоёр дахь нь {M('60t')} км-т байна. Гүйцэх үед зай тэнцүү: {M(b2.tex())}.",
         f"After $t$ hours the buses are at $30 + 60t$ and $60t$ km. Catching up means equal distances: ${b2.tex()}$."),
        {"one": ("Тодорхой нэг цагт гүйцнэ", "At one particular hour"), "none": ("Хэзээ ч гүйцэхгүй", "Never"),
         "inf": ("Үргэлж зэрэгцэж явна", "They are always side by side"), "zero": ("Хөдлөх мөчид зэрэгцэнэ", "Only at the start")},
        ("$30 = 0$ худал: хоёр автобусны зай үргэлж $30$ км хэвээр тул хоёр дахь нь хэзээ ч гүйцэхгүй.",
         "$30 = 0$ is false: the gap stays $30$ km, so the second bus never catches up."),
        fig=lines2(b2, range(5), ("1-р автобус", "2-р автобус"), ("Bus 1", "Bus 2"), ("км", "km"), ("цаг", "hours")))))
    I.append(("make", "reverse", 4, lambda vid, i: t_make(
        vid, i, "x", lambda k: Eqn([BR(2, V(1), K(4))], [V(2), K(k)]), ("$2(x + 4) = 2x + \\square$", "$2(x + 4) = 2x + \\square$"), 8, "all",
        [(4, "Хаалтыг нээхдээ зөвхөн $x$-ийг $2$-оор үржүүлсэн бол $2x + 4$ гэж бодно. $2(x + 4) = 2x + 8$.",
          "Multiplying only the $x$ by $2$ gives $2x + 4$. In fact $2(x + 4) = 2x + 8$.", "distribute-first-term-only"),
         (6, "$2 + 4 = 6$ гэж нэмсэн бололтой. Хаалтын өмнөх тоо нэмэгддэггүй, үржүүлнэ: $2 \\cdot 4 = 8$.",
          "That adds $2 + 4$. The number in front multiplies: $2 \\cdot 4 = 8$.", "added-instead-of-multiplied"),
         (0, "Нүдэнд $0$ бичвэл $2x + 8 = 2x$ болж $8 = 0$ худал: шийдгүй болно.",
          "With $0$ the equation is $2x + 8 = 2x$, so $8 = 0$: no solution at all.", "cancelled-means-infinite")])))
    cp = Eqn([BR(2, V(1), K(1), V(Fr(1, 2)))], [K(20)])
    cf = geo_poly([(0, 0), (6, 0), (6, 2.6), (0, 2.6)], ["x + 1", "x/2", "", ""])
    I.append(("geo", "figure", 5, lambda vid, i: t_story(vid, i, S(
        "carpet", var="x", eq=cp, fig=cf,
        st=(f"Гэрийн шалан дээр тэгш өнцөгт хивс дэвсэв. Зурагт хивсний урт {M('x + 1')} м, өргөн {M(chr(92) + 'frac{x}{2}')} м. "
            f"Хивсний периметр {M(20)} м бол {M('x')} хэд вэ?",
            f"A rectangular carpet lies on a ger floor. In the picture its length is $x + 1$ m and its width $\\frac{{x}}{{2}}$ m. "
            f"The perimeter is ${20}$ m. Find $x$."),
        write=(f"Периметр нь урт, өргөний нийлбэрийн хоёр дахин тул {M(cp.tex())}.", "Тэгш өнцөгтийн урт, өргөн тус бүр хоёр удаа орно.",
               f"The perimeter is twice length plus width: ${cp.tex()}$.", "Length and width each appear twice.",
               f"Периметрээс {M(cp.tex())}.", f"The perimeter gives ${cp.tex()}$."),
        answer=(f"{M('x = 6')}: урт {M(7)} м, өргөн {M(3)} м.", f"$x = 6$: the length is ${7}$ m and the width ${3}$ m."),
        hint1=("Урт, өргөнийг нэмээд хоёр дахин авбал периметр. Хаалтыг нээхэд бутархай коэффициент алга болно.",
               "Length plus width, doubled, is the perimeter. The fraction disappears when you open the bracket."),
        wrongs=[(Eqn([V(1), K(1), V(Fr(1, 2))], [K(20)]), "Хоёр талыг л нэмжээ: периметрт урт, өргөн тус бүр хоёр удаа орно.",
                 "Only two sides were added: length and width each appear twice.", "missed-part-of-total"),
                (7, "$7$ бол хивсний урт. Асуулт $x$-ийг асууж байна.", "$7$ is the length. The question asks for $x$.", "answered-wrong-quantity"),
                (3, "$3$ бол хивсний өргөн. Асуулт $x$-ийг асууж байна.", "$3$ is the width. The question asks for $x$.", "answered-wrong-quantity")]))))
    I.append(("friends", "compare", 5, lambda vid, i: t_friends(
        vid, i, Eqn([FR(2, V(1)), FR(4, V(1), K(-2))], [FR(3, V(1), K(1))], "a"),
        dict(name=("Номин", "Nomin"), lines=[Eqn([V(6), BR(3, V(1), K(-2))], [BR(4, V(1), K(1))]), Eqn([V(6), V(3), K(-6)], [V(4), K(4)]),
                                             Eqn([V(5)], [K(10)]), Eqn([V(1)], [K(2)])],
             how=(f"хоёр талыг {W(12, 'ins')} үржүүлсэн.", "she multiplied both sides by $12$."), err=None),
        dict(name=("Тэмүүлэн", "Temuulen"), lines=[Eqn([V(12), BR(6, V(1), K(-2))], [BR(8, V(1), K(1))]), Eqn([V(12), V(6), K(-12)], [V(8), K(8)]),
                                                 Eqn([V(10)], [K(20)]), Eqn([V(1)], [K(2)])],
             how=(f"хоёр талыг {W(24, 'ins')} үржүүлсэн.", "he multiplied both sides by $24$."), err=None))))
    return I


def part_Ch():
    I = []
    I.append(("explain", "explain", 4, lambda vid, i: t_explain(
        vid, i, ("Сарнай: «$2(x + 3) = 2x + 6$ тэгшитгэлийн шийд нь $x = 0$.» Түүний хэлсэн нь зөв үү?",
                 "Sarnai says: «The solution of $2(x + 3) = 2x + 6$ is $x = 0$.» Is she right?"),
        ("Хагас зөв: $x = 0$ шийд мөн, гэвч ямар ч тоо шийд болно", "Partly: $x = 0$ is a solution, but so is every number"),
        [("Бүрэн зөв: ганц шийд нь $x = 0$", "Completely: the only solution is $x = 0$",
          "Хаалтыг нээвэл хоёр тал яг ижил $2x + 6$. Тиймээс $x = 0$ ганцаараа биш: жишээ нь $x = 5$ үед ч хоёр тал $16$.",
          "Opened, both sides are $2x + 6$. So $x = 0$ is not alone: at $x = 5$ both sides are $16$ too.", "cancelled-means-x-zero"),
         ("Буруу: $x$ хорогдох тул шийдгүй", "No: $x$ cancels, so there is no solution",
          "$x$ хорогдоход $6 = 6$ үлдэнэ. Энэ үнэн тул шийдгүй биш, харин төгсгөлгүй олон шийдтэй.",
          "When $x$ cancels, $6 = 6$ is left. That is true, so there are infinitely many solutions, not none.", "cancelled-means-no-solution"),
         ("Буруу: шийд нь $x = -3$", "No: the solution is $x = -3$",
          "Хаалтыг тэгтэй тэнцүүлж $x + 3 = 0$ гэж бодсон бололтой. Тэгшитгэлийн баруун тал $0$ биш, $2x + 6$.",
          "That sets the bracket to zero, $x + 3 = 0$. The right side is $2x + 6$, not $0$.", "set-bracket-to-zero")],
        [dict(mn=dict(do="Хаалтыг нээе: $2(x + 3) = 2x + 6$. Тэгшитгэл $2x + 6 = 2x + 6$ болно.",
                      why="Хялбарчилсны дараа хоёр талыг харьцуулахад шийдийн тоо харагдана."),
              en=dict(do="Open the bracket: $2(x + 3) = 2x + 6$. The equation reads $2x + 6 = 2x + 6$.",
                      why="Comparing the sides after simplifying shows how many solutions there are.")),
         dict(mn=dict(do="Хоёр тал яг ижил тул $x$-ийн дурын утга шийд. $x = 0$ нь тэдний нэг."),
              en=dict(do="The sides are identical, so every value of $x$ is a solution; $x = 0$ is one of them.")),
         dict(mn=dict(do="Шалгая: $x = 0$ үед $2 \\cdot 3 = 6$ ба $6$; $x = 5$ үед $2 \\cdot 8 = 16$ ба $16$."),
              en=dict(do="Check: at $x = 0$, $2 \\cdot 3 = 6$ and $6$; at $x = 5$, $2 \\cdot 8 = 16$ and $16$."))],
        [("Хаалтыг нээгээд хоёр талыг харьцуулаарай.", "Open the bracket and compare the two sides."),
         ("$x = 0$ өөр өөр утгыг ч орлуулж үзээрэй, жишээ нь $x = 5$.", "Try another value besides $x = 0$, for example $x = 5$.")],
        ("Хоёр тал ижил тул бүх тоо шийд: $x = 0$ нь ганц шийд биш.", "The sides are identical, so every number is a solution: $x = 0$ is not the only one."),
        ["Eq(expand(2*(x + 3)), 2*x + 6)", "Eq(2*(0 + 3), 2*0 + 6)", "Eq(2*(5 + 3), 2*5 + 6)", "Ne(2*(-3 + 3), 0) | Eq(2*(-3 + 3), 0)"])))
    I.append(("make", "reverse", 5, lambda vid, i: t_make(
        vid, i, "x", lambda k: Eqn([BR(k, V(1), K(2))], [V(3), K(6)]), ("$k(x + 2) = 3x + 6$", "$k(x + 2) = 3x + 6$"), 3, "all",
        [(6, "$k$-г тогтмол $6$-тай тэнцүүлсэн бололтой. $k = 6$ бол $6x + 12 = 3x + 6$ болж нэг шийдтэй.",
          "$k$ was matched to the constant $6$; with $k = 6$, $6x + 12 = 3x + 6$ has one solution.", "coefficient-constant-confused"),
         (-3, "Эсрэг тэмдэгтэй коэффициент сонгосон бол $-3x - 6 = 3x + 6$ болж нэг шийдтэй.",
          "Choosing the opposite coefficient gives $-3x - 6 = 3x + 6$, which has one solution.", "opposite-coefficients"),
         (1, "Хаалтыг нээхдээ $k$-г зөвхөн $x$-ээр үржүүлж $kx + 2$ гэвэл $k = 1$... гэхдээ $x + 2 = 3x + 6$ нэг шийдтэй.",
          "Multiplying only the $x$ by $k$ suggests $kx + 2$, but $k = 1$ gives $x + 2 = 3x + 6$, which has one solution.",
          "distribute-first-term-only")])))
    ch = Eqn([FR(4, BR(3, V(1), K(-2))), FR(6, V(1), K(1), c=-1)], [FR(3, V(1)), K(1)])
    I.append(("bare", "multi-step", 5, lambda vid, i: t_bare(vid, i, ch, O_MS, HINT_MS)))
    mo = Eqn([K(40), V(-1)], [BR(5, K(10), V(-1))], "t")
    I.append(("story", "modelling", 5, lambda vid, i: t_story(vid, i, S(
        "mother-daughter", var="t", eq=mo,
        st=(f"Ээж нь {M(40)}, охин нь {M(10)} настай. Хэдэн жилийн өмнө ээж нь охиноосоо яг {M(5)} дахин ахмад байсан бэ?",
            f"A mother is ${40}$ and her daughter ${10}$. How many years ago was the mother exactly ${5}$ times as old as her daughter?"),
        write=(f"{M('t')} жилийн өмнөх үеийг авъя. Тэр үед ээж {M('40 - t')}, охин {M('10 - t')} настай байсан. Ээж нь {M(5)} дахин ахмад тул "
               f"{M(mo.tex())}.",
               "«Өмнө» гэдэг тул хоёулангийнх нь наснаас {t} жилийг хасна; «дахин» гэдэг нь охины тэр үеийн насыг бүхлээр нь үржүүлнэ.".replace("{t}", "$t$"),
               f"Go back $t$ years. Then the mother was $40 - t$ and the daughter $10 - t$. The mother was ${5}$ times as old: ${mo.tex()}$.",
               "«Ago» subtracts $t$ from both ages; «times as old» multiplies the daughter's whole age then.",
               f"{M('t')} жилийн өмнөх үеийг авбал {M(mo.tex())}.", f"Going back $t$ years: ${mo.tex()}$."),
        answer=(f"{M(chr(92) + 'frac{5}{2}')} жилийн өмнө: ээж {M(chr(92) + 'frac{75}{2}')}, охин {M(chr(92) + 'frac{15}{2}')} настай байсан.",
                "$\\frac{5}{2}$ years ago: the mother was $\\frac{75}{2}$ and the daughter $\\frac{15}{2}$."),
        hint1=("$t$ жилийн өмнө хоёулаа хэдэн настай байсан бэ? «Дахин» гэдгийг тэгшитгэл болгоорой.",
               "How old was each of them $t$ years ago? Turn «times as old» into an equation."),
        wrongs=[(Eqn([K(40), V(1)], [BR(5, K(10), V(1))], "t"), "Жилийг хасахын оронд нэмсэн байна: энэ нь ирээдүйг асуусан хэрэг. «Өмнө» гэдэг тул хасна.",
                 "The years were added instead of subtracted: that looks forward in time. «Ago» means subtract.", "time-direction-confused"),
                (8, "$40$-ийг $5$-д хуваасан бол одоогийн ээжийн насыг охины тэр үеийн нас гэж үзжээ. Ээжийн нас ч бас өөрчлөгдөнө.",
                 "Dividing $40$ by $5$ keeps the mother's age fixed. Her age changes too.", "missed-part-of-total"),
                (Eqn([K(40)], [BR(5, K(10), V(-1))], "t"), "Зөвхөн охины наснаас жилийг хасжээ. Ээж ч бас $t$ жилийн өмнө залуу байсан: $40 - t$.",
                 "Only the daughter's age went back. The mother was younger too: $40 - t$.", "missed-part-of-total")]))))
    return I


PARTS = [
    dict(part="A", id="g8-two-step-g8", prefix="g8-ts", level=1, build=part_A,
         title=("One- and two-step equations", "Нэг ба хоёр алхамт тэгшитгэл"),
         instruction=("Undo what was done to the unknown, in reverse order, and check by substituting.",
                      "Үл мэдэгдэхэд хийсэн үйлдлийг эсрэг дарааллаар буцааж, орлуулж шалгаарай."),
         skill=("Undo the number first, then the coefficient.", "Эхлээд үл мэдэгдэхтэй хамт байгаа тоог, дараа нь коэффициентыг арилгана."),
         method=(["Find the number added to or subtracted from the term with the unknown.",
                  "Remove it from both sides: subtract what was added, add what was subtracted.",
                  "Divide both sides by the coefficient (or multiply, if the unknown was divided).",
                  "Put the answer back into the original equation and check."],
                 ["Үл мэдэгдэхтэй гишүүн дээр ямар тоо нэмэгдсэн, хасагдсаныг ол.",
                  "Тэр тоог хоёр талаас арилга: нэмэгдсэн бол хас, хасагдсан бол нэм.",
                  "Хоёр талыг коэффициентэд хуваа (үл мэдэгдэх хуваагдсан бол үржүүл).",
                  "Хариугаа анхны тэгшитгэлд орлуулж шалга."])),
    dict(part="B", id="g8-fractions-decimals", prefix="g8-fx", level=1, build=part_B,
         title=("Negatives, fractions and decimals", "Сөрөг тоо, бутархай, аравтын бутархайтай"),
         instruction=("Same moves with messier numbers: clear fractions and decimals by multiplying every term.",
                      "Ижил аргаар, гэхдээ төвөгтэй тоотой: бутархайгаас гишүүн бүрийг үржүүлж салаарай."),
         skill=("Multiply every term by one number to clear the fractions, then solve as usual.",
                "Гишүүн бүрийг нэг тоогоор үржүүлж бутархайгаас салаад, ердийнхөөрөө бодно."),
         method=(["Find the least common denominator (for decimals take $10$ or $100$).",
                  "Multiply every term on both sides by it, whole numbers included.",
                  "Open any brackets that appear.",
                  "Solve the equation without fractions and check in the original."],
                 ["Хуваариудын хамгийн бага ерөнхий хуваарийг ол (аравтын бутархай бол $10$ эсвэл $100$-г ав).",
                  "Хоёр талын гишүүн бүрийг, бүхэл тоог ч мөн, тэр тоогоор үржүүл.",
                  "Хаалт гарвал нээ.",
                  "Бутархайгүй болсон тэгшитгэлийг бодоод анхны тэгшитгэлд орлуулж шалга."])),
    dict(part="C", id="g8-first-move", prefix="g8-fm", level=1, build=part_C,
         title=("Drill: the first move", "Дасгал: эхний алхам"),
         instruction=("Choose only the first move, the common denominator or the equation. Do not solve.",
                      "Зөвхөн эхний алхам, ерөнхий хуваарь эсвэл тэгшитгэлийг сонго. Бодохгүй."),
         skill=("Decide the first move before doing any arithmetic.", "Тооцоо хийхээсээ өмнө эхний алхмаа шийднэ."),
         method=(["Look at what stands between you and the unknown.",
                  "Fractions: find the least common denominator. Brackets: open them. Unknowns on both sides: gather them.",
                  "Otherwise remove the number that sits with the unknown.",
                  "For a story, name the unknown and turn each sentence into part of the equation."],
                 ["Үл мэдэгдэхийг ганцааруулахад юу саад болж байгааг хар.",
                  "Бутархай бол ерөнхий хуваарь ол, хаалт бол нээ, хоёр талд үл мэдэгдэх бол нэг талд цуглуул.",
                  "Бусад тохиолдолд үл мэдэгдэхтэй хамт байгаа тоог арилга.",
                  "Үгэн бодлогод үл мэдэгдэхийг нэрлээд өгүүлбэр бүрийг тэгшитгэлийн хэсэг болго."])),
    dict(part="D", id="g8-brackets", prefix="g8-bk", level=2, build=part_D,
         title=("Brackets and like terms", "Хаалт ба төсөөтэй гишүүд"),
         instruction=("Open brackets with every sign, combine like terms on each side, then solve.",
                      "Хаалтыг тэмдэгтэй нь нээж, тал бүрт төсөөтэй гишүүдийг нэгтгээд бодоорой."),
         skill=("The number in front of a bracket multiplies every term inside it; like terms combine first.",
                "Хаалтын өмнөх тоо доторх гишүүн бүрийг үржүүлнэ; төсөөтэй гишүүдийг эхлээд нэгтгэнэ."),
         method=(["Open the bracket: multiply every term inside by the number in front.",
                  "If that number is negative, every sign inside changes.",
                  "Combine like terms on each side.",
                  "Solve what is left and check in the original equation."],
                 ["Хаалтыг нээ: хаалтын өмнөх тоогоор доторх гишүүн бүрийг үржүүл.",
                  "Тэр тоо сөрөг бол доторх гишүүн бүрийн тэмдэг өөрчлөгдөнө.",
                  "Тал бүрт төсөөтэй гишүүдийг нэгтгэ.",
                  "Үлдсэн тэгшитгэлийг бодоод анхны тэгшитгэлд орлуулж шалга."])),
    dict(part="E", id="g8-both-sides", prefix="g8-bs", level=2, build=part_E,
         title=("Unknown on both sides", "Хоёр талдаа үл мэдэгдэхтэй"),
         instruction=("Gather the unknown on one side and the numbers on the other; read two-line graphs as equations.",
                      "Үл мэдэгдэхийг нэг талд, тоонуудыг нөгөө талд цуглуул; хоёр шулуунтай графикийг тэгшитгэл болгон унш."),
         skill=("Gather the unknowns on one side and the numbers on the other.",
                "Үл мэдэгдэхтэй гишүүдийг нэг талд, тоонуудыг нөгөө талд цуглуулна."),
         method=(["Compare the coefficients of the unknown on the two sides.",
                  "Remove the smaller one from both sides, so a positive coefficient is left.",
                  "Move the number to the other side: its sign changes.",
                  "Divide by the coefficient and check in the original equation."],
                 ["Хоёр талын үл мэдэгдэхийн коэффициентыг харьцуул.",
                  "Бага коэффициенттэй гишүүнийг хоёр талаас хас, тэгвэл эерэг коэффициент үлдэнэ.",
                  "Тоог нөгөө тал руу шилжүүл: тэмдэг нь эсрэгээрээ солигдоно.",
                  "Коэффициентэд хувааж, анхны тэгшитгэлд орлуулж шалга."])),
    dict(part="F", id="g8-words-equation", prefix="g8-we", level=2, build=part_F,
         title=("Word problems", "Үгэн бодлого"),
         instruction=("Define the unknown, write the equation, solve, and answer in a sentence with units.",
                      "Үл мэдэгдэхийг тэмдэглээд тэгшитгэл зохиож бодоод, хариуг нэгжтэй нь өгүүлбэрээр бичээрэй."),
         skill=("Name the unknown, turn each sentence into part of the equation, then solve.",
                "Үл мэдэгдэхийг нэрлээд өгүүлбэр бүрийг тэгшитгэлийн хэсэг болгож, дараа нь бодно."),
         method=(["Decide what you are asked for and call it $x$.",
                  "Write every other quantity using $x$; read starting values and rates off a graph or table.",
                  "Use words like «total» or «sum» to write the equation.",
                  "Solve it and answer in a sentence with units."],
                 ["Юуг олох гэж байгааг тодорхойлж $x$ гэж тэмдэглэ.",
                  "Бусад хэмжигдэхүүнийг $x$-ээр илэрхийл; график, хүснэгтээс эхлэх утга, өөрчлөлтийг унш.",
                  "«Нийт», «нийлбэр» гэх мэт үгийг ашиглан тэгшитгэл зохио.",
                  "Тэгшитгэлээ бодоод хариуг нэгжтэй нь өгүүлбэрээр бич."])),
    dict(part="G", id="g8-find-error", prefix="g8-fe", level=2, build=part_G,
         title=("Find the mistake", "Алдааг олох"),
         instruction=("Name the mistake in a worked solution, then give the correct answer.",
                      "Бодолтын алдааг нэрлээд зөв хариуг гаргаарай."),
         skill=("Compare every line with the one before: was the same correct move made on both sides?",
                "Мөр бүрийг өмнөх мөртэй нь харьцуулж, хоёр талд ижил зөв үйлдэл хийсэн эсэхийг шалгана."),
         method=(["Say what was done to get each line.",
                  "Check that the move was made correctly on both sides.",
                  "Look hardest at opening brackets, moving terms and dividing.",
                  "Put the final answer into the original equation to confirm."],
                 ["Мөр бүрийг гаргахад юу хийснийг тодорхойл.",
                  "Тэр үйлдлийг хоёр талд зөв хийсэн эсэхийг шалга.",
                  "Хаалт нээх, гишүүн шилжүүлэх, хуваах алхамд онцгой анхаар.",
                  "Эцсийн хариуг анхны тэгшитгэлд орлуулж батал."])),
    dict(part="H", id="g8-multi-step", prefix="g8-ms", level=3, build=part_H,
         title=("Mixed multi-step, and special cases", "Олон алхамт ба онцгой тохиолдол"),
         instruction=("Combine every move in the unit, and tell one solution from none or infinitely many.",
                      "Энэ бүлгийн бүх алхмыг хослуулж, нэг шийдтэй, шийдгүй, төгсгөлгүй олон шийдтэйг ялгаарай."),
         skill=("Clear fractions, open brackets, combine like terms, then solve; compare coefficients to count solutions.",
                "Бутархай, хаалт, төсөөтэй гишүүдийг цэгцлээд бодно; шийдийн тоог коэффициентоор тогтооно."),
         method=(["If there are fractions, multiply both sides by the least common denominator.",
                  "Open every bracket, minding the minus signs, and combine like terms.",
                  "Different coefficients of the unknown: exactly one solution; solve it.",
                  "Equal coefficients: no solution if the numbers differ, infinitely many if the sides are identical.",
                  "Check in the original equation."],
                 ["Бутархай байвал хоёр талыг хамгийн бага ерөнхий хуваариар үржүүл.",
                  "Бүх хаалтыг хасах тэмдэгт анхааран нээж, төсөөтэй гишүүдийг нэгтгэ.",
                  "Үл мэдэгдэхийн коэффициентууд ялгаатай бол яг нэг шийдтэй: бод.",
                  "Коэффициентууд тэнцүү бол тоонууд ялгаатай үед шийдгүй, хоёр тал ижил үед төгсгөлгүй олон шийдтэй.",
                  "Анхны тэгшитгэлд орлуулж шалга."])),
    dict(part="Challenge", id="g8-le-challenge", prefix="g8-ch", level=3, build=part_Ch,
         title=("Challenge", "Сорил"),
         instruction=("Stretch: harder problems that use everything in this unit.",
                      "Сорил: энэ бүлгийн бүх мэдлэгийг шаардсан хүндэвтэр бодлогууд."),
         skill=("Use every move in the unit, and think about what the answer means.",
                "Бүлгийн бүх алхмыг хэрэглэж, хариу юу гэсэн үг болохыг бодно."),
         method=(["Read the whole problem and decide which moves it needs.",
                  "Do one move at a time and write each line.",
                  "Check the answer, and ask whether it makes sense in the question."],
                 ["Бодлогыг бүтнээр уншаад ямар алхам хэрэгтэйг шийд.",
                  "Нэг удаад нэг алхам хийж, мөр бүрийг бич.",
                  "Хариугаа шалгаад, асуултад утга учиртай эсэхийг бод."])),
]


def realise_part(spec):
    items = spec["build"]()
    en_vs, mn_vs, kinds = [], [], []
    last = 0
    for j, (kind, typ, diff, fn) in enumerate(items):
        assert diff >= last, (spec["part"], j, diff, last)
        last = diff
        vid = "%s-v%02d" % (spec["prefix"], j + 1)
        e, m = fn(vid, j)
        skills = [SKILL[spec["part"]]]
        if EXTRA_SKILL.get(kind) and EXTRA_SKILL[kind] not in skills:
            skills.append(EXTRA_SKILL[kind])
        e.update(type=typ, difficulty=diff, skills=skills, prerequisites=list(PREREQ[spec["part"]]), examTags=["ЭШ"])
        en_vs.append(e)
        mn_vs.append(m)
        kinds.append(kind)
    out = dict(spec)
    out["variants"] = (en_vs, mn_vs)
    out["kinds"] = kinds
    return out


MATH = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")


def self_check(parts):
    ids, n_fig, n_self = set(), 0, 0
    assert len(STORY_KEYS) == len(set(STORY_KEYS)), [k for k in STORY_KEYS if STORY_KEYS.count(k) > 1]
    for f in parts:
        en_vs, mn_vs = f["variants"]
        n = len(en_vs)
        if f["part"] == "Challenge":
            assert 4 <= n <= 4, n            # 2–3 per the manual; 4 is the bank gate's floor per form
        else:
            assert 8 <= n <= 16, (f["part"], n)
        # variety (manual §9.6): no template more than ~30% of a part
        for k in set(f["kinds"]):
            assert f["kinds"].count(k) <= max(1, round(0.3 * n)), (f["part"], k, f["kinds"].count(k))
        diffs = [e["difficulty"] for e in en_vs]
        assert diffs == sorted(diffs), (f["part"], diffs)
        stmts = set()
        for e, m in zip(en_vs, mn_vs):
            assert e["id"] not in ids
            ids.add(e["id"])
            assert e["statement"] not in stmts, e["id"]
            stmts.add(e["statement"])
            n_fig += "figure" in e
            n_self += e.get("answerFormat") == "self"
            for s in e["check"]:
                assert bool(sp.sympify(s)) is True, (e["id"], s)
            nt = lambda t: [re.sub(r"\\text\{[^{}]*\}", "TEXT", x) for x in MATH.findall(t)]
            assert sorted(nt(e["statement"])) == sorted(nt(m["statement"])), (e["id"], e["statement"], m["statement"])
            assert set(MATH.findall(e["explanation"])) <= set(MATH.findall(m["explanation"])), e["id"]
            for se, sm in zip(e["steps"], m["steps"]):
                lost = set(MATH.findall(se["do"])) - set(MATH.findall(sm["do"]))
                assert not lost, (e["id"], lost, se["do"], sm["do"])
                assert ("why" in se) == ("why" in sm), e["id"]
            assert len(e["hints"]) == 2 and len(m["hints"]) == 2
            mc = e["misconceptions"]
            assert [x is None for x in mc] == [x is None for x in e["whyWrong"]] == [j == e["correctIndex"] for j in range(4)], e["id"]
            for key in ("type", "difficulty", "skills", "prerequisites", "examTags"):
                assert e.get(key), (e["id"], key)
            for s in [m["statement"], m["explanation"], *m["options"], *m["hints"], *[w for w in m["whyWrong"] if w],
                      *[x for st in m["steps"] for x in st.values()]]:
                assert "—" not in s and "гэнэт" not in s, s
                assert s.replace("\\$", "").count("$") % 2 == 0, s
    assert n_fig >= 15, n_fig
    assert n_self <= 6, n_self
    return n_fig, n_self


def build():
    STORY_KEYS.clear()
    parts = [realise_part(p) for p in PARTS]
    stats = self_check(parts)
    return parts, stats


def main():
    parts, (n_fig, n_self) = build()
    bank = json.load(open(BANK, encoding="utf-8"))
    first = next(i for i, f in enumerate(bank["forms"]) if f["unit"] == UNIT)
    keep = [f for f in bank["forms"] if f["unit"] != UNIT]
    other_ids = {v["id"] for f in keep for v in f["variants"]} | {f["id"] for f in keep}
    new_en = []
    table = {"unit": dict(UNIT_MN, mastery=UNIT_MASTERY_MN), "forms": {}}
    for f in parts:
        assert f["id"] not in other_ids, f["id"]
        en_vs, mn_vs = f["variants"]
        for e in en_vs:
            assert e["id"] not in other_ids, e["id"]
        new_en.append({"id": f["id"], "title": f["title"][0], "level": f["level"], "unit": UNIT, "part": f["part"],
                       "instruction": f["instruction"][0], "skill": f["skill"][0], "method": f["method"][0], "variants": en_vs})
        table["forms"][f["id"]] = {
            "title": f["title"][1], "skill": f["skill"][1], "method": f["method"][1], "instruction": f["instruction"][1],
            "variants": {e["id"]: m for e, m in zip(en_vs, mn_vs)}}
    bank["forms"] = keep[:first] + new_en + keep[first:]
    for u in bank["units"]:
        if u["id"] == UNIT:
            u["blurb"] = UNIT_EN["blurb"]
            u["mastery"] = UNIT_MASTERY_EN
            u["calculator"] = False
    with open(BANK, "w", encoding="utf-8") as fh:
        json.dump(bank, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.makedirs(os.path.dirname(TABLE), exist_ok=True)
    with open(TABLE, "w", encoding="utf-8") as fh:
        json.dump(table, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    man = json.load(open(MANIFEST, encoding="utf-8"))
    for t in man:
        if t["slug"] == bank["slug"]:
            t["problemCount"] = sum(len(f["variants"]) for f in bank["forms"])
            t["forms"] = [{"id": f["id"], "unit": f["unit"], "level": f["level"]} for f in bank["forms"]]
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nv = sum(len(f["variants"][0]) for f in parts)
    print(f"{UNIT}: {len(parts)} parts, {nv} problems, {n_fig} with figures, {n_self} self-marked "
          f"-> {os.path.relpath(BANK, ROOT)}, {os.path.relpath(TABLE, ROOT)}")


if __name__ == "__main__":
    main()
