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

    def side(ps):
        out = []
        for p in ps:
            if p.kind == "br" and (not only_dec or p.dec or p.c.denominator != 1):
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
            out.append(dict(x=x, mn=mn, en=en, mode=mode, checks=chk))
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
    om, oe, wm, we = [], [], [], []
    for o in opts:
        if o is None:
            om.append(correct[0]); oe.append(correct[1]); wm.append(None); we.append(None)
        else:
            om.append(o[0]); oe.append(o[1]); wm.append(o[2]); we.append(o[3])
    assert len(om) == 4 and len(set(om)) == 4 and len(set(oe)) == 4, om
    assert 3 <= len(steps) <= 6, (vid, len(steps))
    assert len(hints) == 2
    en = dict(id=vid, statement=st_en, options=oe, correctIndex=ci, explanation=expl[1],
              check=sorted(set(checks), key=checks.index),
              hints=[h[1] for h in hints], steps=[s["en"] for s in steps], whyWrong=we)
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
    wrongs = [(M(ntexd(m["x"], w.dec)),) * 2 + (m["mn"], m["en"]) for m in ms]
    checks = list(w.checks)
    for m in ms:
        checks += m["checks"]
    ans = M(ntexd(w.sol, w.dec))
    return assemble(vid, i, st_mn, st_en, (ans, ans), wrongs, steps, hints, walk_explanation(w), checks)


def solve_stmt(eq):
    return (f"{M(eq.tex())} тэгшитгэлийг бодоорой.", f"Solve ${eq.tex()}$.")


# ---------------------------------------------------------------------------
# Form 1 · two-step equations
# ---------------------------------------------------------------------------

def form_two_step():
    cases = [
        Eqn([V(3), K(7)], [K(19)], "x"),
        Eqn([V(2), K(-11)], [K(-25)], "x"),
        Eqn([V(-4), K(5)], [K(29)], "y"),
        Eqn([K(5), V(2)], [K(17)], "n"),
        Eqn([K(26)], [V(3), K(-4)], "m"),
        Eqn([FR(3, V(1)), K(4)], [K(9)], "x"),
        Eqn([FR(4, V(1)), K(-6)], [K(-2)], "a"),
        Eqn([K(7), V(-2)], [K(15)], "x"),
        Eqn([V(6), K(9)], [K(6)], "y"),
        Eqn([K(-15)], [V(4), K(1)], "n"),
        Eqn([K(8), V(-5)], [K(-12)], "m"),
        Eqn([V(4), K(-3)], [K(7)], "x"),
    ]
    order = ["move_const_sign", "neg", "no_divide", "mul_instead"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        vid = "g8-ts-v%02d" % (i + 1)
        v = eq.var
        st_mn, st_en = solve_stmt(eq)
        if any(p.kind == "fr" for p in eq.lhs):
            e, m = two_step_division(vid, i, eq)
        else:
            side = eq.lhs if any(p.kind == "v" for p in eq.lhs) else eq.rhs
            t = etex([p for p in side if p.kind == "v"], v)
            hint1 = (f"{M(t)} гишүүнтэй хамт байгаа тоог эхлээд арилгах хэрэгтэй. Хоёр талд ямар үйлдэл хийвэл тэр тоо алга болох вэ?",
                     f"First get rid of the number that sits with ${t}$. What can you do to both sides to make it disappear?")
            e, m = numeric_variant(vid, i, eq, st_mn, st_en, order, hint1)
            # the first move of a two-step equation deserves the reverse-order reason
            k = next(p for p in side if p.kind == "k")
            a = next(p for p in side if p.kind == "v").c
            op_mn = "нэмсэн" if k.c > 0 else "хассан"
            op_en = "added" if k.c > 0 else "subtracted"
            st_t = etex(side, v)
            e["steps"][0]["why"] = (f"${st_t}$ is built by multiplying ${v}$ by ${ntex(a)}$ first and then {op_en} "
                                    f"${ntex(abs(k.c))}$. Undo in the reverse order: the number first, the coefficient second.")
            m["steps"][0]["why"] = (f"{M(st_t)} илэрхийлэлд {VW(v, v, 'acc')} эхлээд {W(a, 'ins')} үржүүлж, дараа нь "
                                    f"{W(abs(k.c), 'acc')} {op_mn}. Буцаахдаа эсрэг дарааллаар явна: эхлээд тоог, дараа нь коэффициентыг арилгана.")
            if side is eq.rhs:
                m["steps"][0]["why"] = "Үл мэдэгдэх баруун талд байгаа ч бодох арга өөрчлөгдөхгүй. " + m["steps"][0]["why"]
                e["steps"][0]["why"] = "The unknown is on the right this time, but the method is the same. " + e["steps"][0]["why"]
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-two-step-g8", level=1,
        title=("Two-step equations", "Хоёр алхамт тэгшитгэл"),
        skill=("Undo the number first, then the coefficient.",
               "Эхлээд үл мэдэгдэхтэй хамт байгаа тоог, дараа нь коэффициентыг арилгана."),
        method=(["Find the number added to or subtracted from the term with the unknown.",
                 "Remove it from both sides: subtract what was added, add what was subtracted.",
                 "Divide both sides by the coefficient (or multiply, if the unknown was divided).",
                 "Put the answer back into the original equation and check."],
                ["Үл мэдэгдэхтэй гишүүн дээр ямар тоо нэмэгдсэн, хасагдсаныг ол.",
                 "Тэр тоог хоёр талаас арилга: нэмэгдсэн бол хас, хасагдсан бол нэм.",
                 "Хоёр талыг коэффициентэд хуваа (үл мэдэгдэх хуваагдсан бол үржүүл).",
                 "Хариугаа анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


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
    cands.append(dict(x=x1, mode="move_const_sign",
                      mn=(f"{W(b, 'acc')} нөгөө тал руу шилжүүлэхдээ тэмдгийг нь өөрчлөөгүй бололтой: "
                          f"{M(f'{xd} = {wrong}')} гэж бичвэл ийм хариу гарна. {fix_mn}: {M(f'{xd} = {arith}')}."),
                      en=(f"It looks as if ${ntex(b)}$ crossed the equals sign without changing sign, giving "
                          f"${xd} = {wrong}$. {fix_en}: ${xd} = {arith}$.")))
    x2 = Fr(r, d)
    cands.append(dict(x=x2, mode="divide_instead",
                      mn=(f"{M(e1.tex())} гарсны дараа хоёр талыг {W(d, 'dat')} хуваасан байна. {M(v)} нь "
                          f"{W(d, 'dat')} хуваагдсан тул буцаахдаа {W(d, 'ins')} үржүүлнэ."),
                      en=(f"After ${e1.tex()}$ both sides were divided by ${d}$. Since ${v}$ is divided by ${d}$, "
                          f"undo it by multiplying by ${d}$.")))
    cands.append(dict(x=r, mode="no_multiply",
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
    wrongs = [(M(ntex(m["x"])),) * 2 + (m["mn"], m["en"]) for m in ms]
    st_mn, st_en = solve_stmt(eq)
    return assemble(vid, i, st_mn, st_en, (M(ntex(sol)),) * 2, wrongs, steps, hints, expl, checks)


# ---------------------------------------------------------------------------
# Form 2 · simplify before solving
# ---------------------------------------------------------------------------

def form_simplify():
    cases = [
        Eqn([V(2), V(5), K(-4)], [K(24)], "x"),
        Eqn([V(3), K(8), V(-1)], [K(2)], "x"),
        Eqn([K(7), V(4), K(-2), V(-1)], [K(20)], "y"),
        Eqn([V(-3), V(5), K(6)], [K(-4)], "n"),
        Eqn([V(6), V(-2), V(-1)], [K(21)], "m"),
        Eqn([V(1), V(1), V(1), K(4)], [K(19)], "x"),
        Eqn([V(5), K(-9), K(3), V(-2)], [K(3)], "a"),
        Eqn([K(30)], [V(4), V(2), K(-6)], "x"),
        Eqn([V(4), V(2), K(1)], [K(10)], "y"),
        Eqn([K(9), V(-4), K(-3), V(-2)], [K(18)], "n"),
        Eqn([V(2), V(-7), K(4)], [K(29)], "m"),
        Eqn([V(8), K(-3), V(-5), K(10)], [K(-14)], "x"),
    ]
    order = ["abs", "drop", "move_const_sign", "neg", "no_divide", "mul_instead"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        v = eq.var
        hint1 = (f"Тэгшитгэлийн нэг талд {VW(v, v, 'com')} гишүүн хэд хэд байна. Тэдгээрийг эхлээд нэгтгэвэл ямар болох вэ?",
                 f"One side has several ${v}$-terms. What do they become when you combine them first?")
        st_mn, st_en = solve_stmt(eq)
        e, m = numeric_variant("g8-sy-v%02d" % (i + 1), i, eq, st_mn, st_en, order, hint1)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-simplify-solve", level=1,
        title=("Simplify before solving", "Эхлээд хялбарчлаад бодох"),
        skill=("Combine like terms on each side before you solve.",
               "Бодохоосоо өмнө тал бүрийн төсөөтэй гишүүдийг нэгтгэнэ."),
        method=(["On each side, add the terms with the unknown together, each with its own sign.",
                 "Add the plain numbers together.",
                 "Solve the two-step equation that is left.",
                 "Check the answer in the original equation."],
                ["Тал бүрт үл мэдэгдэхтэй гишүүдийг өөрсдийнх нь тэмдэгтэй нь хамт нэгтгэ.",
                 "Тоонуудыг хооронд нь нэгтгэ.",
                 "Үлдсэн хоёр алхамт тэгшитгэлийг бод.",
                 "Хариугаа анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 3 · is it a solution?  (substitution as a skill)
# ---------------------------------------------------------------------------

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
    wrongs = [(VERDICT[o][0], VERDICT[o][1], diag[o][0], diag[o][1]) for o in order if o != target]
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
    ms = pick3(w.sol, w.mistakes(["first_only", "neg_sign", "move_var_sign", "move_const_sign", "no_divide", "neg"]))
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
                       m["en"] + f" Substituting it gives ${Lv}$ on the left and ${Rv}$ on the right, which are not equal."))
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


def form_is_solution():
    a_cases = find_substitution_cases()
    a_vars = ["x", "y", "n", "x", "m", "a"]
    b_cases = [
        Eqn([V(4), K(-9)], [V(2), K(5)], "x"),
        Eqn([BR(3, V(1), K(-2))], [V(1), K(4)], "y"),
        Eqn([K(5), V(-2)], [V(1), K(17)], "n"),
        Eqn([V(6), K(1)], [V(2), K(-7)], "m"),
        Eqn([BR(2, V(1), K(3))], [V(5), K(-9)], "a"),
        Eqn([K(9), V(-3)], [V(1), K(21)], "x"),
    ]
    en_vs, mn_vs = [], []
    for j in range(12):
        vid = "g8-is-v%02d" % (j + 1)
        if j % 2 == 0:
            e, m = subst_variant_a(vid, j, a_vars[j // 2], a_cases[j // 2])
        else:
            e, m = subst_variant_b(vid, j, b_cases[j // 2])
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-is-solution", level=1,
        title=("Is it a solution?", "Шийд мөн эсэхийг шалгах"),
        skill=("Substitute the value: if both sides come out equal, it is a solution.",
               "Утгыг орлуулаад хоёр тал тэнцүү гарвал тэр нь шийд."),
        method=(["Put the value in place of the unknown, in brackets if it is negative.",
                 "Work out the left side in the right order: brackets, multiplication, addition.",
                 "Work out the right side separately.",
                 "Equal sides mean a solution; different sides mean it is not."],
                ["Үл мэдэгдэхийн оронд өгсөн утгыг тавь, сөрөг бол хаалтанд хий.",
                 "Зүүн талыг дарааллаар нь бод: хаалт, үржих, нэмэх.",
                 "Баруун талыг тусад нь бод.",
                 "Хоёр тал тэнцүү бол шийд, тэнцүү биш бол шийд биш."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 4 · variables on both sides
# ---------------------------------------------------------------------------

def form_both_sides():
    cases = [
        Eqn([V(5), K(-3)], [V(2), K(9)], "x"),
        Eqn([V(3), K(7)], [V(5), K(-9)], "y"),
        Eqn([V(1), K(-6)], [V(4), K(9)], "x"),
        Eqn([V(2), K(11)], [V(-3), K(1)], "n"),
        Eqn([K(7), V(-2)], [V(1), K(1)], "m"),
        Eqn([V(4), K(5)], [V(1), K(6)], "x"),
        Eqn([K(10), V(-1)], [V(3), K(-6)], "a"),
        Eqn([V(-2), K(8)], [V(-5), K(-7)], "y"),
        Eqn([V(6), K(-4)], [V(2), K(-14)], "x"),
        Eqn([K(9), V(4)], [V(6), K(4)], "n"),
        Eqn([V(8), K(-3)], [V(5), K(12)], "m"),
        Eqn([V(-1), K(4)], [V(2), K(13)], "x"),
    ]
    order = ["move_var_sign", "move_const_sign", "no_divide", "neg", "mul_instead"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        v = eq.var
        hint1 = (f"{VW(v, v, 'com')} гишүүд хоёр талд байна. Аль талынхыг нь хасвал {VW(v, v, 'gen')} коэффициент эерэг үлдэх вэ?",
                 f"There are ${v}$-terms on both sides. Removing which one keeps the coefficient of ${v}$ positive?")
        st_mn, st_en = solve_stmt(eq)
        e, m = numeric_variant("g8-bs-v%02d" % (i + 1), i, eq, st_mn, st_en, order, hint1)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-both-sides", level=2,
        title=("Variables on both sides", "Хоёр талдаа хувьсагчтай тэгшитгэл"),
        skill=("Gather the unknowns on one side and the numbers on the other.",
               "Үл мэдэгдэхтэй гишүүдийг нэг талд, тоонуудыг нөгөө талд цуглуулна."),
        method=(["Compare the coefficients of the unknown on the two sides.",
                 "Remove the smaller one from both sides, so a positive coefficient is left.",
                 "Move the number to the other side: its sign changes.",
                 "Divide by the coefficient and check in the original equation."],
                ["Хоёр талын үл мэдэгдэхийн коэффициентыг харьцуул.",
                 "Бага коэффициенттэй гишүүнийг хоёр талаас хас, тэгвэл эерэг коэффициент үлдэнэ.",
                 "Тоог нөгөө тал руу шилжүүл: тэмдэг нь эсрэгээрээ солигдоно.",
                 "Коэффициентэд хувааж, анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 5 · brackets
# ---------------------------------------------------------------------------

def form_brackets():
    cases = [
        Eqn([BR(3, V(1), K(-4))], [K(15)], "x"),
        Eqn([BR(-2, V(1), K(5))], [K(8)], "y"),
        Eqn([BR(4, V(2), K(1))], [K(28)], "x"),
        Eqn([BR(5, V(1), K(-2)), K(3)], [K(18)], "n"),
        Eqn([BR(2, V(1), K(3)), V(-1)], [K(10)], "x"),
        Eqn([K(7), BR(-3, V(1), K(-1))], [K(4)], "m"),
        Eqn([BR(6, V(1), K(-1))], [K(9)], "x"),
        Eqn([K(10), BR(-1, V(1), K(-8))], [K(3)], "a"),
        Eqn([BR(3, V(2), K(-5)), V(4)], [K(25)], "y"),
        Eqn([K(20)], [BR(4, K(3), V(-1))], "x"),
        Eqn([BR(2, V(3), K(-1)), K(-5)], [K(-19)], "n"),
        Eqn([K(8), BR(-2, V(1), K(4))], [K(-14)], "m"),
    ]
    order = ["first_only", "neg_sign", "abs", "drop", "move_const_sign", "no_divide", "neg", "mul_instead"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        neg = any(p.kind == "br" and p.c < 0 for p in eq.lhs + eq.rhs)
        hint1 = ("Эхлээд хаалтыг нээгээрэй. Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг үржүүлнэ."
                 + (" Хаалтын өмнөх тэмдэгт анхаараарай." if neg else ""),
                 "Open the bracket first. The number in front multiplies every term inside."
                 + (" Watch the sign in front of the bracket." if neg else ""))
        st_mn, st_en = solve_stmt(eq)
        e, m = numeric_variant("g8-bk-v%02d" % (i + 1), i, eq, st_mn, st_en, order, hint1)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-brackets", level=2,
        title=("Equations with brackets", "Хаалттай тэгшитгэл"),
        skill=("The number in front of a bracket multiplies every term inside it.",
               "Хаалтын өмнөх тоо хаалтан доторх гишүүн бүрийг үржүүлнэ."),
        method=(["Open the bracket: multiply every term inside by the number in front.",
                 "If that number is negative, every sign inside changes.",
                 "Combine like terms on each side.",
                 "Solve what is left and check in the original equation."],
                ["Хаалтыг нээ: хаалтын өмнөх тоогоор доторх гишүүн бүрийг үржүүл.",
                 "Тэр тоо сөрөг бол доторх гишүүн бүрийн тэмдэг өөрчлөгдөнө.",
                 "Тал бүрт төсөөтэй гишүүдийг нэгтгэ.",
                 "Үлдсэн тэгшитгэлийг бодоод анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 6 · fractions and decimals
# ---------------------------------------------------------------------------

def form_fractions():
    cases = [
        Eqn([FR(2, V(1)), FR(3, V(1))], [K(10)], "x"),
        Eqn([FR(4, V(1), K(1))], [FR(3, V(1), K(-2))], "x"),
        Eqn([FR(5, V(1)), K(-2)], [FR(10, V(1))], "y"),
        Eqn([FR(3, V(2)), K(-1)], [K(-5)], "x"),
        Eqn([V("0.4"), K("1.2")], [K("-0.4")], "x"),
        Eqn([V("0.25"), K(-3)], [K("0.5")], "n"),
        Eqn([FR(2, V(1), K(-3))], [FR(5, V(1))], "m"),
        Eqn([V("1.5"), K("-0.5")], [V(1), K(3)], "m"),
        Eqn([FR(4, V(1)), FR(6, V(1), c=-1)], [K(2)], "x"),
        Eqn([FR(3, V(2), K(1))], [V(1), K(-2)], "a"),
        Eqn([V("0.3"), K("-0.12")], [V("0.06")], "x"),
        Eqn([FR(3, V(1)), K(4)], [FR(2, V(1)), K(-1)], "y"),
    ]
    order = ["partial", "add_dens", "first_only", "neg_sign", "abs", "move_var_sign", "move_const_sign",
             "no_divide", "drop", "mul_instead"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        if eq.is_dec():
            hint1 = ("Хоёр талыг ямар тоогоор үржүүлбэл бүх тоо бүхэл болох вэ? Гишүүн бүрийг үржүүлэхээ мартаж болохгүй.",
                     "What number can you multiply both sides by so that every number becomes whole? Remember to multiply every term.")
        else:
            hint1 = ("Бүх хуваарьт хуваагддаг хамгийн бага тоо аль вэ? Хоёр талыг тэр тоогоор үржүүлбэл бутархай алга болно.",
                     "What is the smallest number every denominator divides into? Multiplying both sides by it removes the fractions.")
        st_mn, st_en = solve_stmt(eq)
        e, m = numeric_variant("g8-fx-v%02d" % (i + 1), i, eq, st_mn, st_en, order, hint1)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-fractions-decimals", level=2,
        title=("Fractions and decimals", "Бутархай ба аравтын бутархайтай тэгшитгэл"),
        skill=("Multiply every term by one number to clear the fractions, then solve as usual.",
               "Гишүүн бүрийг нэг тоогоор үржүүлж бутархайгаас салаад, ердийнхөөрөө бодно."),
        method=(["Find the least common denominator (for decimals take $10$ or $100$).",
                 "Multiply every term on both sides by it, whole numbers included.",
                 "Open any brackets that appear.",
                 "Solve the equation without fractions and check in the original."],
                ["Хуваариудын хамгийн бага ерөнхий хуваарийг ол (аравтын бутархай бол $10$ эсвэл $100$-г ав).",
                 "Хоёр талын гишүүн бүрийг, бүхэл тоог ч мөн, тэр тоогоор үржүүл.",
                 "Хаалт гарвал нээ.",
                 "Бутархайгүй болсон тэгшитгэлийг бодоод анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 7 · word problems: write AND solve
# ---------------------------------------------------------------------------

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
    for wr, mn, en in s["wrongs"]:
        if isinstance(wr, Eqn):
            k, x = wr.solve()
            assert k == "one"
            checks.append(wr.check_at(x))
        else:
            x = Fr(wr)
        checks.append(f"Ne({epy(eq.lhs, at(x))}, {epy(eq.rhs, at(x))})")
        cands.append(dict(x=x, mn=mn, en=en, mode="story"))
    ms = pick3(w.sol, cands)
    wrongs = [(M(ntex(m["x"])),) * 2 + (m["mn"], m["en"]) for m in ms]
    hints = [s["hint1"], (f"{s['write'][4]} Одоо тэгшитгэлээ бодоорой.", f"{s['write'][5]} Now solve it.")]
    Lv = ntex(eval_side(eq.lhs, w.sol))
    expl = (f"Тэгшитгэл нь {M(eq.tex())}. Бодвол {M(f'{v} = {ntex(w.sol)}')}, шалгахад хоёр тал {M(Lv)} болно.",
            f"The equation is ${eq.tex()}$. Solving it gives ${v} = {ntex(w.sol)}$, and both sides then equal ${Lv}$.")
    e, m = assemble(vid, i, s["st"][0], s["st"][1], (M(ntex(w.sol)),) * 2, wrongs, steps, hints, expl, checks)
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


def stories():
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


def form_words():
    en_vs, mn_vs = [], []
    for i, s in enumerate(stories()):
        e, m = story_variant("g8-we-v%02d" % (i + 1), i, s)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-words-equation", level=2,
        title=("From words to equations", "Үгэн бодлогоос тэгшитгэл зохиох"),
        skill=("Name the unknown, turn each sentence into part of the equation, then solve.",
               "Үл мэдэгдэхийг нэрлээд өгүүлбэр бүрийг тэгшитгэлийн хэсэг болгож, дараа нь бодно."),
        method=(["Decide what you are asked for and call it $x$.",
                 "Write every other quantity using $x$.",
                 "Use words like «total» or «sum» to write the equation.",
                 "Solve it and check that the answer fits the story."],
                ["Юуг олох гэж байгааг тодорхойлж $x$ гэж тэмдэглэ.",
                 "Бусад хэмжигдэхүүнийг $x$-ээр илэрхийл.",
                 "«Нийт», «нийлбэр» гэх мэт үгийг ашиглан тэгшитгэл зохио.",
                 "Тэгшитгэлээ бодоод хариу нь бодлогын нөхцөлд тохирох эсэхийг шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 8 · find the mistake in a worked solution
# ---------------------------------------------------------------------------

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
        wrongs.append((opts_mn[j], opts_en[j], wm, we))
    Lb, Rb = ntexd(eval_side(eq.lhs, bat), eq.is_dec()), ntexd(eval_side(eq.rhs, bat), eq.is_dec())
    bt = f"{v} = {ntex(bat)}"
    wrongs.append((opts_mn[3], opts_en[3],
                   f"{name_mn}-ын хариу {M(bt)} утгыг анхны тэгшитгэлд орлуулбал зүүн тал {M(Lb)}, баруун тал {M(Rb)} гарч тэнцэхгүй. Иймд бодолтод алдаа бий."
                   .replace(f"{name_mn}-ын", {"Бат": "Батын", "Сарнай": "Сарнайн", "Тэмүүлэн": "Тэмүүлэнгийн", "Номин": "Номины",
                                              "Энхжин": "Энхжингийн", "Дорж": "Доржийн"}[name_mn]),
                   f"Putting {name_en}'s answer ${bt}$ into the original equation gives ${Lb}$ on the left and ${Rb}$ on the right. "
                   f"They are not equal, so there is a mistake somewhere."))
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


def form_find_error():
    en_vs, mn_vs = [], []
    for i, c in enumerate(find_error_cases()):
        e, m = find_error_variant("g8-fe-v%02d" % (i + 1), i, c)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-find-error", level=2,
        title=("Find the mistake", "Алдааг олох"),
        skill=("Compare every line with the one before: was the same correct move made on both sides?",
               "Мөр бүрийг өмнөх мөртэй нь харьцуулж, хоёр талд ижил зөв үйлдэл хийсэн эсэхийг шалгана."),
        method=(["Say what was done to get each line.",
                 "Check that the move was made correctly on both sides.",
                 "Look hardest at opening brackets, moving terms and dividing.",
                 "Put the final answer into the original equation to confirm."],
                ["Мөр бүрийг гаргахад юу хийснийг тодорхойл.",
                 "Тэр үйлдлийг хоёр талд зөв хийсэн эсэхийг шалга.",
                 "Хаалт нээх, гишүүн шилжүүлэх, хуваах алхамд онцгой анхаар.",
                 "Эцсийн хариуг анхны тэгшитгэлд орлуулж батал."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 9 · one, none or infinitely many
# ---------------------------------------------------------------------------

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
    opts = [None if j == ci else (opts_mn[j], opts_en[j], D[j][0], D[j][1]) for j in range(4)]
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


def form_how_many():
    cases = [
        Eqn([BR(4, V(1), K(-1))], [V(4), V(-1), K(2)], "x"),
        Eqn([BR(2, V(1), K(-1)), K(4)], [V(2), K(5)], "x"),
        Eqn([BR(3, V(1), K(2))], [V(3), K(6)], "x"),
        Eqn([BR(2, V(1), K(5))], [V(3), K(4), V(-2)], "n"),
        Eqn([BR(3, V(1), K(2))], [V(3), K(2)], "a"),
        Eqn([V(4), BR(-1, V(1), K(-5))], [V(3), K(5)], "m"),
        Eqn([V(5), K(-3)], [BR(2, V(1), K(3))], "m"),
        Eqn([V(5), BR(-2, V(1), K(-1))], [V(3), K(-7)], "y"),
        Eqn([BR(2, V(1), K(-3)), V(1)], [BR(3, V(1), K(-2))], "y"),
        Eqn([K(6), BR(-1, V(1), K(-4))], [V(2), K(1)], "y"),
        Eqn([BR(-1, V(1), K(4))], [K(6), V(-1)], "n"),
        Eqn([BR(5, V(1), K(-1)), V(-2)], [V(3), K(-5)], "a"),
    ]
    cats = [c.solve()[0] for c in cases]
    assert cats.count("one") == 4 and cats.count("none") == 4 and cats.count("all") == 4, cats
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        e, m = how_many_variant("g8-hm-v%02d" % (i + 1), i, eq)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-how-many", level=3,
        title=("One, none, or infinitely many", "Нэг шийдтэй, шийдгүй, төгсгөлгүй олон шийдтэй"),
        skill=("Simplify first, then compare the coefficients, then the numbers.",
               "Эхлээд хялбарчилж, дараа нь коэффициентуудыг, тэгээд тогтмолуудыг жишнэ."),
        method=(["Open the brackets and simplify each side.",
                 "Different coefficients of the unknown: exactly one solution.",
                 "Equal coefficients and different numbers: no solution.",
                 "Both sides identical: infinitely many solutions (an identity)."],
                ["Хаалтыг нээж, тал бүрийг хялбарчил.",
                 "Үл мэдэгдэхийн коэффициентууд ялгаатай бол яг нэг шийдтэй.",
                 "Коэффициентууд тэнцүү, тогтмолууд ялгаатай бол шийдгүй.",
                 "Хоёр тал яг ижил бол төгсгөлгүй олон шийдтэй (адилтгал)."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# Form 10 · multi-step
# ---------------------------------------------------------------------------

def form_multi_step():
    cases = [
        Eqn([BR(3, V(2), K(-1)), BR(-2, V(1), K(4))], [BR(5, V(1), K(-3))], "x"),
        Eqn([FR(3, V(1), K(2)), FR(4, V(1), K(-1), c=-1)], [K(2)], "x"),
        Eqn([BR(2, V(3), K(5))], [BR(4, V(1), K(-1)), V(3)], "y"),
        Eqn([BR(-3, V(1), K(-2)), K(4)], [BR(2, V(1), K(8))], "n"),
        Eqn([FR(5, V(2), K(-1))], [FR(3, V(1), K(4))], "m"),
        Eqn([BR("0.5", V(4), K(-6))], [BR("0.2", V(5), K(10))], "x"),
        Eqn([BR(4, V(1), K(3)), BR(-1, V(1), K(-6))], [BR(2, V(1), K(7)), K(1)], "x"),
        Eqn([FR(2, V(1)), FR(4, V(1), K(-2))], [FR(3, V(1), K(1))], "a"),
        Eqn([K(5), BR(-2, K(3), V(-1))], [BR(3, V(1), K(-4)), K(1)], "x"),
        Eqn([FR(2, BR(3, V(1), K(-1)))], [V(1), K(4)], "x"),
        Eqn([BR(2, V(1), K(-3)), BR(-3, V(1), K(1))], [BR(-2, V(1), K(1))], "y"),
        Eqn([FR(6, V(1), K(-4)), K(1)], [FR(3, V(1)), FR(2, K(1), c=-1)], "x"),
    ]
    order = ["neg_sign", "first_only", "partial", "move_var_sign", "move_const_sign", "no_divide", "neg"]
    en_vs, mn_vs = [], []
    for i, eq in enumerate(cases):
        hint1 = ("Эхлээд бутархайгаас эсвэл хаалтаас салаарай. Дараа нь тал бүрийг хялбарчлаарай.",
                 "First get rid of the fractions or the brackets. Then simplify each side.")
        st_mn, st_en = solve_stmt(eq)
        e, m = numeric_variant("g8-ms-v%02d" % (i + 1), i, eq, st_mn, st_en, order, hint1)
        en_vs.append(e)
        mn_vs.append(m)
    return dict(
        id="g8-multi-step", level=3,
        title=("Multi-step equations", "Олон алхамт тэгшитгэл"),
        skill=("Clear fractions, open brackets, combine like terms, then solve: one move at a time.",
               "Бутархай, хаалт, төсөөтэй гишүүдийг дарааллаар нь цэгцлээд бодно. Нэг алхамд нэг л үйлдэл хийнэ."),
        method=(["If there are fractions, multiply both sides by the least common denominator.",
                 "Open every bracket, minding the minus signs.",
                 "Combine like terms on each side.",
                 "Gather the unknowns on one side and the numbers on the other, then divide.",
                 "Check in the original equation."],
                ["Бутархай байвал хоёр талыг хамгийн бага ерөнхий хуваариар үржүүл.",
                 "Бүх хаалтыг нээ, хасах тэмдэгт анхаар.",
                 "Тал бүрт төсөөтэй гишүүдийг нэгтгэ.",
                 "Үл мэдэгдэхтэй гишүүдийг нэг талд, тоонуудыг нөгөө талд цуглуулж, коэффициентэд хуваа.",
                 "Анхны тэгшитгэлд орлуулж шалга."]),
        variants=(en_vs, mn_vs))


# ---------------------------------------------------------------------------
# build, gate locally, write
# ---------------------------------------------------------------------------

MATH = re.compile(r"\$\$[^$]+\$\$|\$[^$]+\$")


def self_check(forms):
    ids = set()
    for f in forms:
        en_vs, mn_vs = f["variants"]
        assert len(en_vs) == 12, f["id"]
        stmts = set()
        for e, m in zip(en_vs, mn_vs):
            assert e["id"] not in ids
            ids.add(e["id"])
            assert e["statement"] not in stmts, e["id"]
            stmts.add(e["statement"])
            for s in e["check"]:
                assert bool(sp.sympify(s)) is True, (e["id"], s)
            assert sorted(MATH.findall(e["statement"])) == sorted(MATH.findall(m["statement"])), (e["id"], e["statement"], m["statement"])
            assert set(MATH.findall(e["explanation"])) <= set(MATH.findall(m["explanation"])), e["id"]
            for se, sm in zip(e["steps"], m["steps"]):
                lost = set(MATH.findall(se["do"])) - set(MATH.findall(sm["do"]))
                assert not lost, (e["id"], lost, se["do"], sm["do"])
                assert ("why" in se) == ("why" in sm), e["id"]
            assert len(e["hints"]) == 2 and len(m["hints"]) == 2
            assert e["whyWrong"][e["correctIndex"]] is None and m["whyWrong"][e["correctIndex"]] is None
            assert sum(w is None for w in e["whyWrong"]) == 1
            for s in [m["statement"], m["explanation"], *m["options"], *m["hints"], *[w for w in m["whyWrong"] if w],
                      *[x for st in m["steps"] for x in st.values()]]:
                assert "—" not in s and "гэнэт" not in s, s
                assert s.replace("\\$", "").count("$") % 2 == 0, s
        assert len({e["correctIndex"] for e in en_vs}) >= 2, f["id"]


def build():
    forms = [form_two_step(), form_simplify(), form_is_solution(), form_both_sides(), form_brackets(),
             form_fractions(), form_words(), form_find_error(), form_how_many(), form_multi_step()]
    self_check(forms)
    return forms


def main():
    forms = build()
    bank = json.load(open(BANK, encoding="utf-8"))
    first = next(i for i, f in enumerate(bank["forms"]) if f["unit"] == UNIT)
    keep = [f for f in bank["forms"] if f["unit"] != UNIT]
    other_ids = {v["id"] for f in keep for v in f["variants"]} | {f["id"] for f in keep}
    new_en = []
    table = {"unit": UNIT_MN, "forms": {}}
    for f in forms:
        assert f["id"] not in other_ids, f["id"]
        en_vs, mn_vs = f["variants"]
        for e in en_vs:
            assert e["id"] not in other_ids, e["id"]
        new_en.append({"id": f["id"], "title": f["title"][0], "level": f["level"], "unit": UNIT,
                       "skill": f["skill"][0], "method": f["method"][0], "variants": en_vs})
        table["forms"][f["id"]] = {
            "title": f["title"][1], "skill": f["skill"][1], "method": f["method"][1],
            "variants": {e["id"]: m for e, m in zip(en_vs, mn_vs)}}
    bank["forms"] = keep[:first] + new_en + keep[first:]
    for u in bank["units"]:
        if u["id"] == UNIT:
            u["blurb"] = UNIT_EN["blurb"]
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
    nv = sum(len(f["variants"][0]) for f in forms)
    print(f"{UNIT}: {len(forms)} forms, {nv} variants -> {os.path.relpath(BANK, ROOT)}, {os.path.relpath(TABLE, ROOT)}")


if __name__ == "__main__":
    main()
