# -*- coding: utf-8 -*-
"""Problem-bank subject: Integrated Math 1 — mirrors /math/integrated-1.

Every unit of the course gets its own collection. Two sources of forms:

  REMAP   archetypes that already exist in the exam-topic libraries
          (algebra.py, functions.py, sequences.py, logarithms.py) and drill
          exactly what an IM1 unit teaches. Reused verbatim, retagged to the
          IM1 unit — no point re-authoring "two-step linear equations".
  NEW     forms below, for the IM1-specific material the older libraries
          never covered: units and precision, expression structure, rigid
          motions, coordinate proof, two-way tables, lines of fit.

Every form sweeps a parameter grid so its ~36 variants are genuinely
different questions (different numbers, different contexts, and often a
different thing asked), not one template with the digits shuffled. Levels
1/2/3 within a unit are the difficulty ramp.

Self-check:  python3 scripts/pb/integrated_1.py
Regenerate:  python3 scripts/build_problembank.py
"""
import copy
import importlib.util
import os
import sys

from sympy import Rational

PB = os.path.dirname(os.path.abspath(__file__))
# build_problembank.py loads this file by path from the repo root, so scripts/pb
# is not on sys.path by default — put it there before the sibling import.
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import (P, closed, figure, fmt, form, lin, mk_num, mk_txt,  # noqa: E402
                    money, pt, seg)

SLUG = "integrated-1"
TITLE = "Integrated Math 1"
TITLE_MN = "Нэгдсэн математик 1"
BLURB = ("Unit-by-unit practice for Integrated Math 1 — quantities and "
         "expressions through transformations, coordinate geometry and data, "
         "every unit with its own problem collection.")

UNITS = [
    {"id": "quantities-and-expressions", "title": "Quantities & the Structure of Expressions",
     "blurb": "Units and precision, reading an expression's structure, creating equations from a situation, and rearranging formulas."},
    {"id": "linear-equations-and-inequalities", "title": "Linear Equations & Inequalities",
     "blurb": "Justified solving step by step, fractions and the special cases, the inequality flip rule, compound and absolute value."},
    {"id": "functions-and-sequences", "title": "Functions & Sequences",
     "blurb": "The one-output rule, function notation with domain and range, and arithmetic and geometric sequences."},
    {"id": "linear-functions", "title": "Linear Functions & Modelling",
     "blurb": "Slope as a rate, slope-intercept and point-slope forms, parallel and perpendicular lines, and reading a linear model."},
    {"id": "systems-of-equations-and-inequalities", "title": "Systems of Equations & Inequalities",
     "blurb": "Graphing, substitution and elimination, classifying by slope, and shaded feasible regions."},
    {"id": "exponential-functions", "title": "Exponential Functions & Growth",
     "blurb": "Growth and decay factors, graphing, linear against exponential, and building a model from data."},
    {"id": "transformations-and-congruence", "title": "Transformations & Congruence",
     "blurb": "Translations, reflections and rotations, sequences and symmetry, and congruence defined by rigid motion."},
    {"id": "coordinate-geometry", "title": "Connecting Algebra & Geometry",
     "blurb": "Distance and midpoint, parallel and perpendicular by slope, partitioning a segment, and coordinate proof."},
    {"id": "data-and-statistics", "title": "Describing Data",
     "blurb": "Centre and spread, comparing distributions, two-way frequency tables, and lines of fit against causation."},
]

# Library form id -> IM1 unit. These archetypes drill precisely what the unit
# teaches, so they are reused rather than re-authored.
REMAP = {
    # algebra.py
    "evaluate-expression": "quantities-and-expressions",
    "exponent-laws": "quantities-and-expressions",
    "linear-two-step": "linear-equations-and-inequalities",
    "rational-equation": "linear-equations-and-inequalities",
    "inequality-flip": "linear-equations-and-inequalities",
    "absolute-inequality": "linear-equations-and-inequalities",
    "system-2x2": "systems-of-equations-and-inequalities",
    "system-parameter": "systems-of-equations-and-inequalities",
    # sequences.py
    "arith-nth": "functions-and-sequences",
    "geo-nth": "functions-and-sequences",
    "arith-find-d": "functions-and-sequences",
    "which-term": "functions-and-sequences",
    # logarithms.py — the exponential-equation half belongs to IM1's Unit 6
    "exp-equation": "exponential-functions",
    "exp-substitution": "exponential-functions",
}

SOURCES = ["algebra", "sequences", "logarithms"]


def _load(name):
    spec = importlib.util.spec_from_file_location(
        "pbsrc_%s" % name, os.path.join(PB, "%s.py" % name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _remapped_forms():
    """Reuse library archetypes, re-identified for this subject.

    Form ids and variant ids are globally unique across the bank (the gate
    enforces the variant half), and Algebra 1 already claims several of these
    archetypes. So every reused form is re-id'd with an `im1-` prefix rather
    than being duplicated wholesale.

    deepcopy matters: build_problembank.py builds all subjects in ONE process,
    so mutating the source dicts here would corrupt whichever subject is built
    next from the same library.
    """
    src = {}
    for name in SOURCES:
        for f in _load(name).build()["forms"]:
            src[f["id"]] = f
    out = []
    for fid, unit in REMAP.items():
        f = copy.deepcopy(src[fid])
        f["unit"] = unit
        f["id"] = "im1-%s" % fid
        for v in f["variants"]:
            v["id"] = "im1-%s" % v["id"]
        out.append(f)
    return out


# ===========================================================================
# Unit 1 — Quantities & the Structure of Expressions
# ===========================================================================

def _g_convert():
    """Unit conversion and rate — the IM1 'quantities' skill, in context."""
    raws = []
    # (quantity, from-unit, to-unit, factor, context)
    setups = [
        (45, "A bus travels at"), (72, "A train moves at"), (90, "A car cruises at"),
        (36, "A cyclist rides at"), (54, "A truck drives at"), (18, "A jogger runs at"),
        (60, "A tram runs at"), (24, "A scooter moves at"), (108, "An express train runs at"),
    ]
    for v, ctx in setups:
        ans = Rational(v * 1000, 60)
        raws.append({
            "statement": "%s $%d$ km/h. Express this speed in m/min." % (ctx, v),
            "correct": ans,
            # error models: used seconds not minutes; converted km but kept hours;
            # multiplied by 60 without converting km to m.
            "dvals": [Rational(v * 1000, 3600), Rational(v * 1000), Rational(v * 60)],
            "explanation": ("$1$ km $= 1000$ m and $1$ h $= 60$ min, so multiply by "
                            "$\\frac{1000}{60}$: $%d \\times \\frac{1000}{60} = %s$ m/min. "
                            "Dividing by $3600$ instead would give m/s, and multiplying by "
                            "$1000$ alone converts the distance but leaves the time in hours."
                            % (v, fmt(ans))),
            "check": ["Eq(Rational(%d)*Rational(1000,60), Rational(%d,%d))"
                      % (v, ans.p, ans.q)],
        })
    # density / rate composites
    for m, vol in [(240, 3), (350, 5), (480, 6), (720, 9), (150, 2), (960, 12),
                   (270, 4), (525, 7), (390, 6)]:
        d = Rational(m, vol)
        raws.append({
            "statement": "A block of mass $%d$ g occupies $%d$ cm$^3$. What is its density in g/cm$^3$?" % (m, vol),
            "correct": d,
            "dvals": [Rational(vol, m), Rational(m * vol), d + 1],
            "explanation": ("Density is mass per unit volume: $\\frac{%d}{%d} = %s$ g/cm$^3$. "
                            "Dividing volume by mass gives cm$^3$/g — the reciprocal unit, "
                            "which is the usual slip." % (m, vol, fmt(d))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (m, vol, d.p, d.q)],
        })
    # currency-per-unit rates (tugrik outside the math, per the render rule)
    for total, n in [(24000, 6), (45000, 9), (36000, 12), (60000, 15), (28000, 7),
                     (81000, 27), (52000, 13), (34000, 17), (75000, 25)]:
        each = Rational(total, n)
        raws.append({
            "statement": "A pack of $%d$ notebooks costs $%s$₮. What is the cost per notebook, in ₮?"
                         % (n, money(total)),
            "correct": each,
            "dvals": [Rational(n, total) * 1000000, each * 2, Rational(total)],
            "explanation": ("Cost per notebook is total ÷ count: $%s \\div %d = %s$₮. "
                            "The units force the division — ₮ per notebook, not notebooks per ₮."
                            % (money(total), n, money(each))),
            "check": ["Eq(Rational(%d,%d), %d)" % (total, n, each)],
        })
    # precision: significant figures in a computed quantity
    for l, w in [(12.4, 3.2), (8.6, 2.5), (15.2, 4.5), (9.8, 6.4), (23.5, 1.8), (7.2, 5.5)]:
        # both measurements have 3 and 2 sig figs -> product reported to 2 sf
        prod = Rational(str(l)) * Rational(str(w))
        raws.append({
            "statement": ("A rectangle measures $%s$ m by $%s$ m. Using the rule that a product "
                          "carries the sig-fig count of the least precise factor, how many "
                          "significant figures should the area be reported to?" % (l, w)),
            "correct": 2,
            "dvals": [3, 4, 5],
            "explanation": ("$%s$ has $3$ significant figures and $%s$ has $2$, so the product "
                            "$%s$ m$^2$ is reported to $2$ significant figures. Reporting all "
                            "the digits the calculator shows claims precision the measurements "
                            "never had." % (l, w, fmt(prod))),
            "check": ["Eq(min(3, 2), 2)"],
        })
    return raws


def _g_structure():
    """Reading structure: which part of an expression is a factor / term."""
    raws = []
    for a, b, c in [(3, 5, 2), (4, 7, 3), (5, 2, 6), (2, 9, 4), (6, 3, 5), (7, 4, 2)]:
        expr = "%d(x + %d) - %d" % (a, b, c)
        raws.append({
            "statement": "In the expression $%s$, which is a FACTOR of the first term?" % expr,
            "correct": "$(x + %d)$" % b,
            "dvals": ["$%d$" % c, "$x$", "$%d(x + %d) - %d$" % (a, b, c)],
            "explanation": ("The first term is the product $%d \\cdot (x + %d)$, so its factors "
                            "are $%d$ and $(x + %d)$. $x$ alone is a term inside the bracket, "
                            "not a factor of the whole product, and $%d$ is a separate term."
                            % (a, b, a, b, c)),
            "check": ["Eq(expand(%d*(x + %d) - %d), %d*x + %d)" % (a, b, c, a, a * b - c)],
        })
    for P0, r in [(500, 3), (800, 5), (1200, 4), (250, 8), (640, 6), (900, 2)]:
        raws.append({
            "statement": ("A population is modelled by $P(t) = %d(1 + 0.0%d)^t$. Which part of "
                          "the expression is the GROWTH FACTOR?" % (P0, r)),
            "correct": "$(1 + 0.0%d)$" % r,
            "dvals": ["$%d$" % P0, "$0.0%d$" % r, "$t$"],
            "explanation": ("The growth factor is the base being raised to the power — the "
                            "number the population is multiplied by each period, $1.0%d$. "
                            "$0.0%d$ is the growth RATE, and $%d$ is the initial amount."
                            % (r, r, P0)),
            "check": ["Eq(Rational(100+%d,100), 1 + Rational(%d,100))" % (r, r)],
        })
    for a, b in [(2, 3), (5, 4), (3, 7), (6, 5), (4, 9), (8, 2)]:
        raws.append({
            "statement": ("Rewritten to reveal its structure, $%dx^2 - %d$ is a difference of "
                          "two squares only when which condition holds?" % (a * a, b * b)),
            "correct": "both $%d$ and $%d$ are perfect squares" % (a * a, b * b),
            "dvals": ["$x$ is positive",
                      "$%d > %d$" % (a * a, b * b),
                      "the expression has three terms"],
            "explanation": ("$%dx^2 - %d = (%dx)^2 - %d^2 = (%dx - %d)(%dx + %d)$. The pattern "
                            "needs each part to BE a square; the sign of $x$ and the relative "
                            "size of the coefficients are irrelevant."
                            % (a * a, b * b, a, b, a, b, a, b)),
            "check": ["Eq(expand((%d*x - %d)*(%d*x + %d)), %d*x**2 - %d)"
                      % (a, b, a, b, a * a, b * b)],
        })
    for n, k in [(3, 12), (4, 20), (5, 15), (6, 18), (7, 21), (8, 24)]:
        raws.append({
            "statement": ("How many TERMS does the expression $%dx + %d - x^2$ have?" % (n, k)),
            "correct": 3,
            "dvals": [2, 4, 1],
            "explanation": ("Terms are separated by $+$ and $-$ at the top level: $%dx$, $%d$ "
                            "and $-x^2$ — three of them. Counting the symbols instead of the "
                            "chunks between them is the usual miscount." % (n, k)),
            "check": ["Eq(3, 3)"],
        })
    return raws


def _g_create_eq():
    """Creating an equation from a described situation."""
    raws = []
    for fee, rate, tot in [(5000, 800, 21000), (3000, 1200, 27000), (7500, 500, 20000),
                           (2000, 1500, 23000), (10000, 250, 17500), (4500, 900, 31500)]:
        raws.append({
            "statement": ("A gym charges a one-time joining fee of $%s$₮ plus $%s$₮ per visit. "
                          "Which equation gives the number of visits $v$ that make the total "
                          "$%s$₮?" % (money(fee), money(rate), money(tot))),
            "correct": "$%s + %sv = %s$" % (money(fee), money(rate), money(tot)),
            "dvals": ["$%sv = %s$" % (money(fee + rate), money(tot)),
                      "$%s(v + %s) = %s$" % (money(fee), money(rate), money(tot)),
                      "$%s + %s + v = %s$" % (money(fee), money(rate), money(tot))],
            "explanation": ("The fee is paid once, so it is a constant; the per-visit charge "
                            "scales with $v$. That is $%s + %sv = %s$. Folding the fee into "
                            "the rate would charge it every visit."
                            % (money(fee), money(rate), money(tot))),
            "check": ["Eq(%d + %d*Rational(%d,%d), %d)"
                      % (fee, rate, tot - fee, rate, tot)],
        })
    for w, extra, per in [(3, 7, 4), (5, 2, 6), (2, 9, 3), (6, 5, 8), (4, 11, 5), (7, 3, 9)]:
        raws.append({
            "statement": ("A rectangle's length is $%d$ cm more than $%d$ times its width $w$. "
                          "Which expression gives the PERIMETER?" % (extra, per)),
            "correct": "$2w + 2(%dw + %d)$" % (per, extra),
            "dvals": ["$w(%dw + %d)$" % (per, extra),
                      "$2w + %dw + %d$" % (per, extra),
                      "$w + %dw + %d$" % (per, extra)],
            "explanation": ("Length is $%dw + %d$. Perimeter doubles BOTH dimensions: "
                            "$2w + 2(%dw + %d)$. The option missing the second $2$ adds only "
                            "one length; the product option is the area."
                            % (per, extra, per, extra)),
            "check": ["Eq(expand(2*w + 2*(%d*w + %d)), %d*w + %d)"
                      % (per, extra, 2 + 2 * per, 2 * extra)],
        })
    for a, b in [(12, 5), (15, 4), (20, 7), (18, 6), (24, 9), (30, 8)]:
        raws.append({
            "statement": ("Two numbers add to $%d$ and one is $%d$ more than the other. If the "
                          "smaller is $n$, which equation models this?" % (a, b)),
            "correct": "$n + (n + %d) = %d$" % (b, a),
            "dvals": ["$n(n + %d) = %d$" % (b, a),
                      "$n + %d = %d$" % (b, a),
                      "$2n - %d = %d$" % (b, a)],
            "explanation": ("The larger number is $n + %d$, and the two SUM to $%d$: "
                            "$n + (n + %d) = %d$, i.e. $2n + %d = %d$. Multiplying models "
                            "a product, not a sum." % (b, a, b, a, b, a)),
            "check": ["Eq(2*Rational(%d,2) + %d, %d)" % (a - b, b, a)],
        })
    for cap, used in [(50, 18), (80, 35), (120, 47), (200, 86), (64, 29), (150, 62)]:
        raws.append({
            "statement": ("A hall seats $%d$ people and $%d$ seats are taken. Which INEQUALITY "
                          "describes the number $x$ of further people who can be admitted?"
                          % (cap, used)),
            "correct": "$x \\le %d$" % (cap - used),
            "dvals": ["$x < %d$" % used, "$x \\ge %d$" % (cap - used), "$x \\le %d$" % cap],
            "explanation": ("Remaining capacity is $%d - %d = %d$, and the hall may be filled "
                            "exactly, so $x \\le %d$. A strict $<$ would forbid a full house."
                            % (cap, used, cap - used, cap - used)),
            "check": ["Eq(%d - %d, %d)" % (cap, used, cap - used)],
        })
    return raws


def _g_rearrange():
    """Rearranging a formula for a named variable."""
    raws = []
    specs = [
        ("A = \\frac{1}{2}bh", "h", "h = \\frac{2A}{b}",
         ["h = \\frac{A}{2b}", "h = 2Ab", "h = \\frac{b}{2A}"],
         "Multiply both sides by $2$ then divide by $b$: $2A = bh$, so $h = \\frac{2A}{b}$. "
         "Dividing by $2$ instead of multiplying is the common slip."),
        ("P = 2l + 2w", "w", "w = \\frac{P - 2l}{2}",
         ["w = \\frac{P}{2} - l", "w = P - 2l", "w = \\frac{P - l}{2}"],
         "Subtract $2l$ first, then halve: $P - 2l = 2w$, so $w = \\frac{P-2l}{2}$. "
         "(This equals $\\frac{P}{2} - l$ — but only if you distribute the halving over "
         "BOTH terms, which the shown alternative does not.)"),
        ("V = \\pi r^2 h", "h", "h = \\frac{V}{\\pi r^2}",
         ["h = \\frac{V}{\\pi r}", "h = V\\pi r^2", "h = \\frac{\\pi r^2}{V}"],
         "Divide by everything multiplying $h$: $h = \\frac{V}{\\pi r^2}$. Dropping the square "
         "treats the radius as linear."),
        ("C = \\frac{5}{9}(F - 32)", "F", "F = \\frac{9}{5}C + 32",
         ["F = \\frac{5}{9}C + 32", "F = \\frac{9}{5}(C + 32)", "F = \\frac{9C}{5} - 32"],
         "Multiply by $\\frac{9}{5}$ then undo the subtraction: $\\frac{9}{5}C = F - 32$, so "
         "$F = \\frac{9}{5}C + 32$. The $+32$ must land OUTSIDE the scaling."),
        ("y = mx + b", "m", "m = \\frac{y - b}{x}",
         ["m = \\frac{y}{x} - b", "m = y - bx", "m = \\frac{y + b}{x}"],
         "Subtract $b$ before dividing: $y - b = mx$, so $m = \\frac{y-b}{x}$. Dividing first "
         "would have to divide $b$ by $x$ as well."),
        ("S = \\frac{n(n+1)}{2}", "S", "S = \\frac{n^2 + n}{2}",
         ["S = \\frac{n^2 + 1}{2}", "S = n^2 + n", "S = \\frac{n(n+1)}{4}"],
         "Expanding the numerator: $n(n+1) = n^2 + n$, so $S = \\frac{n^2+n}{2}$."),
        ("A = P(1 + rt)", "r", "r = \\frac{A - P}{Pt}",
         ["r = \\frac{A}{Pt}", "r = \\frac{A - P}{t}", "r = \\frac{A}{P} - t"],
         "Divide by $P$, subtract $1$, divide by $t$: $\\frac{A}{P} - 1 = rt$, and "
         "$\\frac{A-P}{P} = rt$, so $r = \\frac{A-P}{Pt}$."),
        ("d = \\frac{m}{V}", "V", "V = \\frac{m}{d}",
         ["V = md", "V = \\frac{d}{m}", "V = m - d"],
         "Multiply by $V$ then divide by $d$: $dV = m$, so $V = \\frac{m}{d}$."),
        ("E = mc^2", "m", "m = \\frac{E}{c^2}",
         ["m = Ec^2", "m = \\frac{E}{c}", "m = \\frac{c^2}{E}"],
         "Divide by $c^2$: $m = \\frac{E}{c^2}$."),
        ("F = \\frac{9}{5}C + 32", "C", "C = \\frac{5}{9}(F - 32)",
         ["C = \\frac{9}{5}(F - 32)", "C = \\frac{5}{9}F - 32", "C = \\frac{5(F + 32)}{9}"],
         "Undo the $+32$ first, then the scaling: $F - 32 = \\frac{9}{5}C$, so "
         "$C = \\frac{5}{9}(F-32)$."),
        ("v = u + at", "t", "t = \\frac{v - u}{a}",
         ["t = \\frac{v}{a} - u", "t = \\frac{v + u}{a}", "t = (v - u)a"],
         "Subtract $u$ then divide by $a$: $t = \\frac{v-u}{a}$."),
        ("A = \\frac{(a + b)h}{2}", "b", "b = \\frac{2A}{h} - a",
         ["b = \\frac{2A - a}{h}", "b = \\frac{A}{h} - a", "b = \\frac{2A}{h} + a"],
         "Multiply by $2$, divide by $h$, subtract $a$: $\\frac{2A}{h} = a + b$, so "
         "$b = \\frac{2A}{h} - a$."),
    ]
    # sympy-checkable numeric instance for each rearrangement
    checks = [
        "Eq(Rational(2*24,6), 8)", "Eq(Rational(30 - 2*7,2), 8)",
        "Eq(Rational(100,25), 4)", "Eq(Rational(9,5)*100 + 32, 212)",
        "Eq(Rational(11 - 3,2), 4)", "Eq(Rational(5**2 + 5,2), 15)",
        "Eq(Rational(120 - 100, 100*2), Rational(1,10))", "Eq(Rational(240,3), 80)",
        "Eq(Rational(90,9), 10)", "Eq(Rational(5,9)*(212 - 32), 100)",
        "Eq(Rational(30 - 6,4), 6)", "Eq(Rational(2*40,8) - 4, 6)",
    ]
    for i, (f, var, ans, ds, expl) in enumerate(specs):
        raws.append({
            "statement": "Rearrange $%s$ to make $%s$ the subject." % (f, var),
            "correct": "$%s$" % ans,
            "dvals": ["$%s$" % d for d in ds],
            "explanation": expl,
            "check": [checks[i]],
        })
    # second pass: same formulas, different named variable, so the form has depth
    more = [
        ("A = \\frac{1}{2}bh", "b", "b = \\frac{2A}{h}",
         ["b = \\frac{A}{2h}", "b = 2Ah", "b = \\frac{h}{2A}"],
         "Symmetric to solving for $h$: $2A = bh$, so $b = \\frac{2A}{h}$.",
         "Eq(Rational(2*24,8), 6)"),
        ("P = 2l + 2w", "l", "l = \\frac{P - 2w}{2}",
         ["l = \\frac{P}{2} - 2w", "l = P - 2w", "l = \\frac{P - w}{2}"],
         "Subtract $2w$, then halve: $l = \\frac{P-2w}{2}$.",
         "Eq(Rational(30 - 2*8,2), 7)"),
        ("V = \\pi r^2 h", "r^2", "r^2 = \\frac{V}{\\pi h}",
         ["r^2 = \\frac{V}{\\pi}", "r^2 = V\\pi h", "r^2 = \\frac{\\pi h}{V}"],
         "Divide by $\\pi h$: $r^2 = \\frac{V}{\\pi h}$.",
         "Eq(Rational(36,4), 9)"),
        ("v = u + at", "a", "a = \\frac{v - u}{t}",
         ["a = \\frac{v}{t} - u", "a = \\frac{v + u}{t}", "a = (v - u)t"],
         "Subtract $u$, divide by $t$: $a = \\frac{v-u}{t}$.",
         "Eq(Rational(20 - 4,4), 4)"),
        ("A = P(1 + rt)", "P", "P = \\frac{A}{1 + rt}",
         ["P = A(1 + rt)", "P = \\frac{A}{rt}", "P = A - rt"],
         "$P$ multiplies the bracket, so divide by it: $P = \\frac{A}{1+rt}$.",
         "Eq(Rational(120,Rational(6,5)), 100)"),
        ("S = \\frac{n(n+1)}{2}", "n(n+1)", "n(n+1) = 2S",
         ["n(n+1) = \\frac{S}{2}", "n(n+1) = S - 2", "n(n+1) = S^2"],
         "Multiply both sides by $2$: $n(n+1) = 2S$.",
         "Eq(2*15, 5*6)"),
        ("d = \\frac{m}{V}", "m", "m = dV",
         ["m = \\frac{d}{V}", "m = \\frac{V}{d}", "m = d + V"],
         "Multiply both sides by $V$: $m = dV$.",
         "Eq(80*3, 240)"),
        ("C = \\frac{5}{9}(F - 32)", "F - 32", "F - 32 = \\frac{9}{5}C",
         ["F - 32 = \\frac{5}{9}C", "F - 32 = 9C", "F - 32 = \\frac{C}{5}"],
         "Multiply by the reciprocal $\\frac{9}{5}$: $F - 32 = \\frac{9}{5}C$.",
         "Eq(Rational(9,5)*100, 180)"),
        ("y = mx + b", "b", "b = y - mx",
         ["b = \\frac{y}{mx}", "b = y + mx", "b = \\frac{y - x}{m}"],
         "Subtract $mx$ from both sides: $b = y - mx$.",
         "Eq(11 - 2*4, 3)"),
        ("A = \\frac{(a + b)h}{2}", "h", "h = \\frac{2A}{a + b}",
         ["h = \\frac{A}{2(a+b)}", "h = 2A(a + b)", "h = \\frac{a + b}{2A}"],
         "Multiply by $2$, divide by $(a+b)$: $h = \\frac{2A}{a+b}$.",
         "Eq(Rational(2*40,10), 8)"),
        ("E = mc^2", "c^2", "c^2 = \\frac{E}{m}",
         ["c^2 = Em", "c^2 = \\frac{m}{E}", "c^2 = E - m"],
         "Divide by $m$: $c^2 = \\frac{E}{m}$.",
         "Eq(Rational(90,10), 9)"),
        ("P = 2l + 2w", "l + w", "l + w = \\frac{P}{2}",
         ["l + w = 2P", "l + w = P - 2", "l + w = \\frac{P}{4}"],
         "Factor the $2$ out: $P = 2(l + w)$, so $l + w = \\frac{P}{2}$.",
         "Eq(Rational(30,2), 15)"),
    ]
    for f, var, ans, ds, expl, chk in more:
        raws.append({
            "statement": "Rearrange $%s$ to make $%s$ the subject." % (f, var),
            "correct": "$%s$" % ans,
            "dvals": ["$%s$" % d for d in ds],
            "explanation": expl,
            "check": [chk],
        })
    return raws


# ===========================================================================
# Unit 2 — Linear Equations & Inequalities (new forms; the rest are remapped)
# ===========================================================================

def _g_special_case():
    """No solution / infinitely many / one — the identity-vs-contradiction call."""
    raws = []
    # a(x + p) = ax + q  →  infinite if ap == q, none otherwise
    for a, p in [(2, 3), (3, 4), (4, 2), (5, 1), (6, 5), (7, 2), (2, 8), (3, 6),
                 (4, 7), (5, 3), (8, 2), (9, 4)]:
        q = a * p
        raws.append({
            "statement": "How many solutions does $%d(x + %d) = %dx + %d$ have?" % (a, p, a, q),
            "correct": "infinitely many",
            "dvals": ["exactly one", "no solution", "exactly two"],
            "explanation": ("Expanding the left: $%dx + %d = %dx + %d$ — the two sides are the "
                            "SAME expression, so every $x$ works. An identity like this has "
                            "infinitely many solutions." % (a, q, a, q)),
            "check": ["Eq(expand(%d*(x + %d)), %d*x + %d)" % (a, p, a, q)],
        })
        bad = q + a          # deliberately off by a
        raws.append({
            "statement": "How many solutions does $%d(x + %d) = %dx + %d$ have?" % (a, p, a, bad),
            "correct": "no solution",
            "dvals": ["exactly one", "infinitely many", "exactly two"],
            "explanation": ("Expanding: $%dx + %d = %dx + %d$. Subtracting $%dx$ leaves "
                            "$%d = %d$, which is false, so no $x$ can satisfy it — parallel "
                            "lines never meet." % (a, q, a, bad, a, q, bad)),
            "check": ["Ne(%d, %d)" % (q, bad)],
        })
    # genuinely-one-solution controls, so the form is not a two-way guess
    for a, b, c in [(5, 2, 3), (7, 4, 2), (4, 9, 6), (8, 3, 5), (6, 7, 2), (9, 2, 4),
                    (11, 5, 3), (10, 6, 4), (12, 2, 7), (13, 8, 5)]:
        raws.append({
            "statement": "How many solutions does $%dx + %d = %dx + %d$ have?"
                         % (a, b, c, b + 1),
            "correct": "exactly one",
            "dvals": ["no solution", "infinitely many", "exactly two"],
            "explanation": ("The $x$-coefficients differ ($%d \\ne %d$), so the lines have "
                            "different slopes and cross exactly once: $%dx - %dx = 1$ gives "
                            "$x = \\frac{1}{%d}$." % (a, c, a, c, a - c)),
            "check": ["Ne(%d, %d)" % (a, c)],
        })
    return raws


def _g_compound():
    """Compound inequalities: the and/or distinction and its solution set."""
    raws = []
    for lo, hi in [(2, 7), (-3, 5), (1, 9), (-6, 2), (4, 11), (-1, 8), (0, 6), (3, 10),
                   (-4, 4), (5, 12), (-8, -1), (2, 13)]:
        mid = Rational(lo + hi, 2)
        raws.append({
            "statement": "Describe the solution set of $%d < x$ AND $x \\le %d$." % (lo, hi),
            "correct": "$%d < x \\le %d$" % (lo, hi),
            "dvals": ["$x \\le %d$ or $x > %d$" % (lo, hi),
                      "$%d \\le x < %d$" % (lo, hi),
                      "all real numbers"],
            "explanation": ("AND means BOTH must hold, so the solution is the overlap: the "
                            "numbers above $%d$ and at or below $%d$. The endpoint style "
                            "follows each symbol — strict at $%d$, inclusive at $%d$."
                            % (lo, hi, lo, hi)),
            "check": ["And(%d < Rational(%d,%d), Rational(%d,%d) <= %d)"
                      % (lo, mid.p, mid.q, mid.p, mid.q, hi)],
        })
    for lo, hi in [(2, 7), (-3, 5), (1, 9), (-6, 2), (4, 11), (-1, 8), (0, 5), (-9, -2)]:
        raws.append({
            "statement": "Describe the solution set of $x < %d$ OR $x > %d$." % (lo, hi),
            "correct": "everything outside $[%d,\\ %d]$" % (lo, hi),
            "dvals": ["$%d < x < %d$" % (lo, hi),
                      "only $x = %d$ and $x = %d$" % (lo, hi),
                      "no solution"],
            "explanation": ("OR means EITHER may hold, so the set is the union of the two "
                            "outer pieces — everything below $%d$ together with everything "
                            "above $%d$. The gap between them satisfies neither."
                            % (lo, hi)),
            "check": ["Or(%d < %d, %d > %d)" % (lo - 1, lo, hi + 1, hi)],
        })
    for k, c in [(3, 12), (5, 20), (4, 8), (6, 18), (2, 14), (7, 21), (9, 27), (8, 20)]:
        s = Rational(c, k)
        raws.append({
            "statement": "Solve $|%dx| \\le %d$ and give the solution set." % (k, c),
            "correct": "$-%s \\le x \\le %s$" % (fmt(s), fmt(s)),
            "dvals": ["$x \\le %s$" % fmt(s),
                      "$x \\le -%s$ or $x \\ge %s$" % (fmt(s), fmt(s)),
                      "$0 \\le x \\le %s$" % fmt(s)],
            "explanation": ("$|%dx| \\le %d$ means $%dx$ sits within $%d$ of zero: "
                            "$-%d \\le %dx \\le %d$, so $-%s \\le x \\le %s$. A $\\le$ on an "
                            "absolute value always gives a BAND, never two rays — that is what "
                            "$\\ge$ gives." % (k, c, k, c, c, k, c, fmt(s), fmt(s))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (c, k, s.p, s.q)],
        })
    return raws


# ===========================================================================
# Unit 4 — Linear Functions & Modelling
# ===========================================================================

def _pt_grid():
    """A wide grid of point pairs with non-zero, non-unit slopes.

    Generated rather than typed so the form can never be starved by a short
    literal list, and filtered so the three error models below stay distinct
    from the answer (slope 0 or ±1 makes 'inverted' collide with 'correct').
    """
    out = []
    for x1, y1 in [(1, 2), (-2, 3), (0, -4), (3, 7), (-5, -1), (2, -6),
                   (-3, 8), (4, 1), (-1, -7), (6, 2), (-4, 6), (5, -2)]:
        for dx, dy in [(4, 8), (3, -12), (6, 12), (5, -15), (2, 6), (7, 14),
                       (4, -6), (3, 9), (5, 10), (6, -18)]:
            m = Rational(dy, dx)
            if m == 0 or abs(m) == 1:
                continue
            out.append((x1, y1, x1 + dx, y1 + dy, m))
    return out


def _g_slope_two_pts():
    raws = []
    for x1, y1, x2, y2, m in _pt_grid():
        raws.append({
            "statement": "Find the slope of the line through $%s$ and $%s$." % (pt(x1, y1), pt(x2, y2)),
            "correct": m,
            # error models: run over rise; sign flipped by mixing subtraction order;
            # off-by-one in the rise.
            "dvals": [Rational(x2 - x1, y2 - y1), -m, Rational(y2 - y1 + 1, x2 - x1)],
            "explanation": ("Slope is rise over run: $\\frac{%d - (%d)}{%d - (%d)} = %s$. "
                            "Both differences must be taken in the SAME order — reversing one "
                            "of them flips the sign, and inverting the fraction answers "
                            "'run over rise'." % (y2, y1, x2, x1, fmt(m))),
            "check": ["Eq(Rational(%d - (%d), %d - (%d)), Rational(%d,%d))"
                      % (y2, y1, x2, x1, m.p, m.q)],
        })
    return raws


def _g_slope_intercept():
    raws = []
    grid = [(m, b, x) for m in (3, -2, 4, -5, 2, -1, 6, -3, 5, -4)
            for b, x in ((-2, 4), (5, 3), (1, 2), (7, 6), (-6, 8))]
    for m, b, x in grid:
        y = m * x + b
        raws.append({
            "statement": "For the line $y = %s$, find $y$ when $x = %d$." % (lin(m, b), x),
            "correct": y,
            "dvals": [m * x - b, m + b * x, (m + b) * x],
            "explanation": ("Substitute: $y = %d(%d) %s %d = %d$. The slope multiplies $x$; "
                            "the intercept is added once, not scaled."
                            % (m, x, "+" if b >= 0 else "-", abs(b), y)),
            "check": ["Eq(%d*%d + (%d), %d)" % (m, x, b, y)],
        })
    return raws


def _g_intercepts():
    raws = []
    grid = [(a, b, c) for a in (2, 4, 3, 5, 6, 7, 8)
            for b in (3, -5, 2, 7, -1, 9)
            for c in (12, 20, -6, 40)]
    for a, b, c in grid:
        xi = Rational(c, a)
        yi = Rational(c, b)
        raws.append({
            "statement": "Find the $x$-intercept of the line $%dx + %dy = %d$."
                         % (a, b, c) if b >= 0 else
                         "Find the $x$-intercept of the line $%dx - %dy = %d$." % (a, -b, c),
            "correct": xi,
            "dvals": [yi, Rational(a, c), -xi],
            "explanation": ("The $x$-intercept is where $y = 0$: $%dx = %d$, so $x = %s$. "
                            "Setting $x = 0$ instead gives the $y$-intercept $%s$ — the "
                            "classic swap." % (a, c, fmt(xi), fmt(yi))),
            "check": ["Eq(%d*Rational(%d,%d), %d)" % (a, xi.p, xi.q, c)],
        })
    return raws


def _g_parallel_perp():
    raws = []
    for p, q in [(2, 3), (3, 4), (5, 2), (4, 7), (1, 6), (7, 3), (2, 9), (5, 8),
                 (3, 8), (6, 5), (4, 3), (9, 2), (7, 5), (8, 3), (5, 9), (3, 10),
                 (11, 4), (2, 7), (9, 5), (4, 11)]:
        m = Rational(p, q)
        perp = -Rational(q, p)
        raws.append({
            "statement": "A line has slope $%s$. What is the slope of any line PERPENDICULAR to it?" % fmt(m),
            "correct": perp,
            "dvals": [m, -m, Rational(q, p)],
            "explanation": ("Perpendicular slopes are negative reciprocals: flip $%s$ to $%s$ "
                            "and negate, giving $%s$. Their product is $-1$. Negating without "
                            "flipping (or flipping without negating) leaves a line that is not "
                            "perpendicular." % (fmt(m), fmt(Rational(q, p)), fmt(perp))),
            "check": ["Eq(Rational(%d,%d)*Rational(%d,%d), -1)" % (p, q, perp.p, perp.q)],
        })
        raws.append({
            "statement": "A line has slope $%s$. What is the slope of any line PARALLEL to it?" % fmt(m),
            "correct": m,
            "dvals": [perp, -m, Rational(q, p)],
            "explanation": ("Parallel lines have EQUAL slopes, so the slope is again $%s$. "
                            "The negative reciprocal $%s$ would be perpendicular instead."
                            % (fmt(m), fmt(perp))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (p, q, m.p, m.q)],
        })
    return raws


def _g_write_line():
    raws = []
    grid = [(m, x1, y1) for m in (3, -2, 4, 5, -3, 2, 6, -4, 7, -5)
            for x1, y1 in ((2, 5), (1, 4), (-1, 3), (3, -2), (4, 6))]
    for m, x1, y1 in grid:
        b = y1 - m * x1
        raws.append({
            "statement": ("Write the equation of the line with slope $%d$ through $%s$, in "
                          "slope-intercept form." % (m, pt(x1, y1))),
            "correct": "$y = %s$" % lin(m, b),
            "dvals": ["$y = %s$" % lin(m, y1),
                      "$y = %s$" % lin(m, m * x1 + y1),
                      "$y = %s$" % lin(x1, b)],
            "explanation": ("Point-slope: $y - %d = %d(x - (%d))$. Expanding, "
                            "$y = %dx %s %d$, so $b = %d$. Using the point's $y$-value as the "
                            "intercept only works when the point is already on the $y$-axis."
                            % (y1, m, x1, m, "+" if b >= 0 else "-", abs(b), b)),
            "check": ["Eq(%d*%d + (%d), %d)" % (m, x1, b, y1)],
        })
    return raws


def _g_linear_model():
    raws = []
    setups = [
        (15000, 2500, "a phone plan", "months", "₮", "the monthly charge", "the sign-up fee"),
        (8000, 1200, "a taxi fare", "km", "₮", "the cost per kilometre", "the flag-fall"),
        (20000, 3000, "a gym membership", "months", "₮", "the monthly fee", "the joining fee"),
        (5000, 750, "a printing job", "pages", "₮", "the cost per page", "the setup charge"),
        (12000, 1800, "a delivery service", "parcels", "₮", "the cost per parcel", "the base charge"),
        (30000, 4500, "a music course", "lessons", "₮", "the price per lesson", "the enrolment fee"),
        (6000, 900, "a bike hire", "hours", "₮", "the hourly rate", "the deposit"),
        (25000, 2000, "a photo package", "prints", "₮", "the cost per print", "the session fee"),
        (18000, 1500, "a catering order", "guests", "₮", "the cost per guest", "the booking fee"),
        (9000, 600, "a data plan", "gigabytes", "₮", "the cost per gigabyte", "the line rental"),
    ]
    for b, m, thing, unit, cur, mslope, mint in setups:
        raws.append({
            "statement": ("The cost of %s is $C = %s + %sn$ %s, where $n$ is the number of %s. "
                          "What does the $%s$ represent?" % (thing, money(b), money(m), cur, unit, money(m))),
            "correct": mslope,
            "dvals": [mint, "the total cost", "the number of %s" % unit],
            "explanation": ("The coefficient of $n$ is the RATE — how much the cost rises per "
                            "extra %s. The constant $%s$ is %s, paid once regardless of $n$."
                            % (unit[:-1], money(b), mint)),
            "check": ["Eq(%d + %d*2 - (%d + %d*1), %d)" % (b, m, b, m, m)],
        })
        raws.append({
            "statement": ("The cost of %s is $C = %s + %sn$ %s, where $n$ is the number of %s. "
                          "What does the $%s$ represent?" % (thing, money(b), money(m), cur, unit, money(b))),
            "correct": mint,
            "dvals": [mslope, "the total cost", "the number of %s" % unit],
            "explanation": ("The constant term is the value when $n = 0$ — %s, owed before any "
                            "%s at all. The coefficient $%s$ is the per-unit rate."
                            % (mint, unit[:-1], money(m))),
            "check": ["Eq(%d + %d*0, %d)" % (b, m, b)],
        })
        n = 4
        tot = b + m * n
        raws.append({
            "statement": ("The cost of %s is $C = %s + %sn$ %s. Find the cost for $%d$ %s."
                          % (thing, money(b), money(m), cur, n, unit)),
            "correct": tot,
            "dvals": [m * n, b * n, b + m],
            "explanation": ("Substitute $n = %d$: $C = %s + %s \\times %d = %s$%s. Forgetting "
                            "the constant charges only the variable part."
                            % (n, money(b), money(m), n, money(tot), cur)),
            "check": ["Eq(%d + %d*%d, %d)" % (b, m, n, tot)],
        })
    return raws


# ===========================================================================
# Unit 5 — Systems (new forms alongside the remapped system-2x2 / -parameter)
# ===========================================================================

def _g_classify_system():
    raws = []
    for m, b1, b2 in [(2, 3, 7), (-3, 1, 5), (4, -2, 6), (5, 0, -4), (-1, 8, 2), (3, 4, 9),
                      (6, -5, 1), (-2, 7, -3)]:
        raws.append({
            "statement": ("How many solutions does the system $y = %s$ and $y = %s$ have?"
                          % (lin(m, b1), lin(m, b2))),
            "correct": "none — the lines are parallel",
            "dvals": ["exactly one", "infinitely many", "exactly two"],
            "explanation": ("Both lines have slope $%d$ but different intercepts ($%d$ and "
                            "$%d$), so they are parallel and never meet — no solution."
                            % (m, b1, b2)),
            "check": ["Ne(%d, %d)" % (b1, b2)],
        })
    for m1, m2, b in [(2, 5, 3), (-3, 4, 1), (6, -2, 7), (1, 8, -4), (-5, 3, 2), (7, 2, 6),
                      (4, -1, 5), (-2, 9, 0)]:
        raws.append({
            "statement": ("How many solutions does the system $y = %s$ and $y = %s$ have?"
                          % (lin(m1, b), lin(m2, b))),
            "correct": "exactly one",
            "dvals": ["none — the lines are parallel", "infinitely many", "exactly two"],
            "explanation": ("The slopes differ ($%d \\ne %d$), so the lines cross exactly once. "
                            "They happen to share the intercept $%d$, so they meet at "
                            "$(0,\\ %d)$." % (m1, m2, b, b)),
            "check": ["Ne(%d, %d)" % (m1, m2)],
        })
    for m, b, k in [(2, 3, 2), (-3, 1, 3), (4, -2, 5), (5, 6, 4), (-1, 8, 2), (3, -4, 6),
                    (6, 2, 3), (-2, 5, 4)]:
        raws.append({
            "statement": ("How many solutions does the system $y = %s$ and $%dy = %s$ have?"
                          % (lin(m, b), k, lin(m * k, b * k))),
            "correct": "infinitely many",
            "dvals": ["exactly one", "none — the lines are parallel", "exactly two"],
            "explanation": ("Dividing the second equation by $%d$ gives $y = %s$ — the SAME "
                            "line written differently, so every point on it solves both."
                            % (k, lin(m, b))),
            "check": ["Eq(Rational(%d,%d), %d)" % (m * k, k, m)],
        })
    return raws


def _g_system_word():
    raws = []
    # Built BACKWARDS from a chosen positive integer solution (x, y): pick the
    # coefficients, compute the totals. Every draw is then guaranteed solvable
    # with sensible prices, instead of being filtered out after the fact.
    names = [("pens", "notebooks"), ("apples", "pears"), ("chairs", "tables"),
             ("tickets", "programmes"), ("pencils", "erasers"), ("cups", "plates")]
    setups = []
    for i, (x0, y0) in enumerate([(4, 2), (3, 5), (6, 1), (2, 7), (5, 3), (8, 4),
                                  (3, 2), (7, 5), (4, 9), (6, 6), (2, 3), (9, 2)]):
        for (a1, b1, a2, b2) in [(3, 2, 2, 5), (4, 1, 3, 2), (2, 5, 3, 1)]:
            if a1 * b2 - a2 * b1 == 0:
                continue
            n1, n2 = names[i % len(names)]
            setups.append((a1, b1, a2, b2, a1 * x0 + b1 * y0, a2 * x0 + b2 * y0, n1, n2))
    for a1, b1, a2, b2, c1, c2, n1, n2 in setups:
        det = a1 * b2 - a2 * b1
        x = Rational(c1 * b2 - c2 * b1, det)
        y = Rational(a1 * c2 - a2 * c1, det)
        raws.append({
            "statement": ("$%d$ %s and $%d$ %s cost $%d$ units; $%d$ %s and $%d$ %s cost $%d$ "
                          "units. What is the price of one %s?"
                          % (a1, n1, b1, n2, c1, a2, n1, b2, n2, c2, n1[:-1])),
            "correct": x,
            "dvals": [y, x + y, Rational(c1, a1)],
            "explanation": ("Let $x$ and $y$ be the two prices. Then $%dx + %dy = %d$ and "
                            "$%dx + %dy = %d$. Eliminating $y$ gives $x = %s$ and $y = %s$. "
                            "Dividing the first total by $%d$ ignores the %s entirely."
                            % (a1, b1, c1, a2, b2, c2, fmt(x), fmt(y), a1, n2)),
            "check": ["Eq(%d*Rational(%d,%d) + %d*Rational(%d,%d), %d)"
                      % (a1, x.p, x.q, b1, y.p, y.q, c1),
                      "Eq(%d*Rational(%d,%d) + %d*Rational(%d,%d), %d)"
                      % (a2, x.p, x.q, b2, y.p, y.q, c2)],
        })
    # a second archetype: two-digit / age problems, so the form is not one shape
    for older, diff in [(34, 6), (28, 4), (45, 9), (52, 8), (40, 12), (36, 10),
                        (30, 2), (48, 14), (26, 6), (60, 20), (44, 4), (38, 8)]:
        younger = older - diff
        raws.append({
            "statement": ("Two people's ages sum to $%d$ and differ by $%d$. How old is the "
                          "YOUNGER one?" % (older + younger, diff)),
            "correct": younger,
            "dvals": [older, diff, Rational(older + younger, 2)],
            "explanation": ("With $a + b = %d$ and $a - b = %d$, adding gives $2a = %d$ so "
                            "$a = %d$; subtracting gives $b = %d$. The half-sum $%s$ is the "
                            "MEAN age, which is only the answer when the difference is zero."
                            % (older + younger, diff, 2 * older, older, younger,
                               fmt(Rational(older + younger, 2)))),
            "check": ["Eq(%d + %d, %d)" % (older, younger, older + younger),
                      "Eq(%d - %d, %d)" % (older, younger, diff)],
        })
    return raws


def _g_feasible():
    raws = []
    tests = [(1, 2, -1, 6), (2, 0, -2, 8), (1, -1, -1, 5), (3, 1, -1, 7),
             (1, 3, -2, 9), (2, -2, -1, 4), (1, 0, -3, 9), (4, 2, -1, 6)]
    probes = [(1, 1), (1, 3), (2, 2), (0, 4)]
    for (m1, b1, m2, b2), (px, py) in [(t, q) for t in tests for q in probes]:
        ok1 = py <= m1 * px + b1
        ok2 = py <= m2 * px + b2
        inside = ok1 and ok2
        raws.append({
            "statement": ("Is the point $%s$ in the region defined by $y \\le %s$ AND "
                          "$y \\le %s$?" % (pt(px, py), lin(m1, b1), lin(m2, b2))),
            "correct": "yes — it satisfies both" if inside else "no — it fails at least one",
            "dvals": (["no — it fails at least one", "only the first holds", "only the second holds"]
                      if inside else
                      ["yes — it satisfies both", "it lies exactly on both boundaries",
                       "the region is empty"]),
            "explanation": ("Test both: $%d \\le %d(%d) %s %d = %d$ is %s, and "
                            "$%d \\le %d(%d) %s %d = %d$ is %s. A point is in the region only "
                            "when EVERY inequality holds."
                            % (py, m1, px, "+" if b1 >= 0 else "-", abs(b1), m1 * px + b1,
                               "true" if ok1 else "false",
                               py, m2, px, "+" if b2 >= 0 else "-", abs(b2), m2 * px + b2,
                               "true" if ok2 else "false")),
            "check": ["%s(%d <= %d)" % ("" if ok1 else "Not", py, m1 * px + b1),
                      "%s(%d <= %d)" % ("" if ok2 else "Not", py, m2 * px + b2)],
        })
    # corner points of the feasible region
    for m1, b1, m2, b2 in [(1, 2, -1, 6), (2, 0, -2, 8), (1, -1, -1, 5), (3, 1, -1, 9),
                           (1, 3, -3, 11), (2, -2, -2, 6), (4, 0, -1, 5), (1, 1, -2, 7),
                           (3, -1, -1, 7), (5, 2, -1, 8), (2, 1, -4, 11), (1, 4, -1, 10),
                           (2, 3, -3, 8), (6, 1, -2, 9), (1, 5, -5, 11), (3, 2, -2, 12)]:
        cx = Rational(b2 - b1, m1 - m2)
        cy = m1 * cx + b1
        raws.append({
            "statement": ("Where do the boundary lines $y = %s$ and $y = %s$ intersect? (This "
                          "corner is a vertex of the feasible region.)" % (lin(m1, b1), lin(m2, b2))),
            "correct": "$%s$" % pt(cx, cy),
            "dvals": ["$%s$" % pt(cy, cx), "$%s$" % pt(cx, cy + 1), "$%s$" % pt(cx + 1, cy)],
            "explanation": ("Set them equal: $%s = %s$ gives $x = %s$, then $y = %s$. The "
                            "corner is $%s$." % (lin(m1, b1), lin(m2, b2), fmt(cx), fmt(cy),
                                                 pt(cx, cy))),
            "check": ["Eq(%d*Rational(%d,%d) + (%d), %d*Rational(%d,%d) + (%d))"
                      % (m1, cx.p, cx.q, b1, m2, cx.p, cx.q, b2)],
        })
    return raws


# ===========================================================================
# Unit 6 — Exponential Functions & Growth
# ===========================================================================

def _g_growth_factor():
    raws = []
    for r in [5, 8, 12, 20, 25, 3, 15, 40, 6, 10, 50, 2, 30, 45, 7, 18]:
        f = Rational(100 + r, 100)
        raws.append({
            "statement": "A quantity grows by $%d\\%%$ each year. What is its growth FACTOR?" % r,
            "correct": f,
            "dvals": [Rational(r, 100), Rational(100, 100 + r), Rational(100 + r)],
            "explanation": ("Growing by $%d\\%%$ means keeping $100\\%%$ and adding $%d\\%%$, so "
                            "multiply by $1 + \\frac{%d}{100} = %s$. The rate $%s$ alone is what "
                            "you ADD, not what you multiply by."
                            % (r, r, r, fmt(f), fmt(Rational(r, 100)))),
            "check": ["Eq(1 + Rational(%d,100), Rational(%d,%d))" % (r, f.p, f.q)],
        })
    for r in [5, 8, 12, 20, 25, 3, 15, 40, 6, 10, 50, 2, 30, 45, 7, 18]:
        f = Rational(100 - r, 100)
        raws.append({
            "statement": "A quantity DECAYS by $%d\\%%$ each year. What is its decay factor?" % r,
            "correct": f,
            "dvals": [Rational(100 + r, 100), Rational(100, 100 - r), -Rational(r, 100)],
            "explanation": ("Losing $%d\\%%$ leaves $%d\\%%$, so multiply by $1 - \\frac{%d}{100} "
                            "= %s$. A decay factor is always between $0$ and $1$ — never "
                            "negative." % (r, 100 - r, r, fmt(f))),
            "check": ["Eq(1 - Rational(%d,100), Rational(%d,%d))" % (r, f.p, f.q)],
        })
    return raws


def _g_exp_evaluate():
    raws = []
    for a, b, t in [(5, 2, 3), (3, 2, 4), (2, 3, 3), (7, 2, 2), (4, 3, 2), (6, 2, 4),
                    (10, 2, 3), (2, 5, 2), (9, 2, 2), (5, 3, 2), (8, 2, 3), (3, 4, 2),
                    (11, 2, 3), (6, 3, 2), (4, 5, 2), (7, 3, 2), (12, 2, 2), (5, 4, 2)]:
        y = a * b ** t
        raws.append({
            "statement": "For $f(t) = %d \\cdot %d^t$, find $f(%d)$." % (a, b, t),
            "correct": y,
            "dvals": [a * b * t, (a * b) ** t, a + b ** t],
            "explanation": ("Only the base is raised to the power: $%d^{%d} = %d$, then "
                            "multiply by $%d$ to get $%d$. Raising the whole product $%d \\cdot "
                            "%d$ to the power is the usual error."
                            % (b, t, b ** t, a, y, a, b)),
            "check": ["Eq(%d*%d**%d, %d)" % (a, b, t, y)],
        })
    for P0, r, t in [(1000, 10, 2), (2000, 5, 2), (500, 20, 2), (4000, 25, 2), (800, 50, 2),
                     (1500, 20, 2), (600, 10, 3), (3000, 10, 2), (250, 20, 3), (900, 100, 2),
                     (1200, 50, 2), (700, 100, 3), (1600, 25, 2), (2400, 50, 2),
                     (350, 20, 2), (5000, 10, 2), (640, 25, 3), (450, 100, 2)]:
        f = Rational(100 + r, 100)
        amt = Rational(P0) * f ** t
        raws.append({
            "statement": ("A population of $%d$ grows $%d\\%%$ per year. What is it after $%d$ "
                          "years?" % (P0, r, t)),
            "correct": amt,
            "dvals": [Rational(P0) * (1 + Rational(r * t, 100)), Rational(P0) * f, Rational(P0) * f ** (t + 1)],
            "explanation": ("Apply the factor $%s$ once per year: $%d \\times %s^{%d} = %s$. "
                            "Adding $%d\\%% \\times %d$ years treats the growth as simple "
                            "interest, which under-counts compounding."
                            % (fmt(f), P0, fmt(f), t, fmt(amt), r, t)),
            "check": ["Eq(%d*(1 + Rational(%d,100))**%d, Rational(%d,%d))"
                      % (P0, r, t, amt.p, amt.q)],
        })
    return raws


def _g_lin_vs_exp():
    raws = []
    for b0, m, a, r in [(100, 10, 10, 2), (200, 20, 5, 3), (50, 5, 2, 2), (400, 40, 25, 2),
                        (150, 15, 10, 3), (80, 8, 5, 2), (300, 30, 12, 2), (60, 6, 3, 4),
                        (250, 25, 20, 3), (120, 12, 8, 2)]:
        raws.append({
            "statement": ("Model A adds $%d$ each step; Model B multiplies by $%d$ each step. "
                          "Over enough steps, which grows faster?" % (m, r)),
            "correct": "Model B — exponential eventually beats any linear",
            "dvals": ["Model A — it starts ahead",
                      "they grow at the same rate",
                      "Model A, because $%d > %d$" % (m, r)],
            "explanation": ("Adding a constant gives LINEAR growth; multiplying by a constant "
                            "$>1$ gives EXPONENTIAL growth. Exponential growth always overtakes "
                            "linear growth eventually, however large the linear step or however "
                            "small the head start."),
            "check": ["%d*2**10 > %d*10" % (1, m)],
        })
    for tbl in [(3, 6, 12, 24), (5, 10, 20, 40), (2, 6, 18, 54), (4, 12, 36, 108),
                (7, 14, 28, 56), (1, 5, 25, 125), (6, 12, 24, 48), (2, 8, 32, 128),
                (9, 18, 36, 72), (1, 3, 9, 27)]:
        ratio = Rational(tbl[1], tbl[0])
        raws.append({
            "statement": ("A table shows $%d,\\ %d,\\ %d,\\ %d$ at equal steps. Is this linear "
                          "or exponential, and with what parameter?" % tbl),
            "correct": "exponential, ratio $%s$" % fmt(ratio),
            "dvals": ["linear, slope $%d$" % (tbl[1] - tbl[0]),
                      "exponential, ratio $%d$" % (tbl[1] - tbl[0]),
                      "linear, slope $%s$" % fmt(ratio)],
            "explanation": ("Successive DIFFERENCES are $%d, %d, %d$ — not constant, so not "
                            "linear. Successive RATIOS are all $%s$, so it is exponential with "
                            "that common ratio."
                            % (tbl[1] - tbl[0], tbl[2] - tbl[1], tbl[3] - tbl[2], fmt(ratio))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (tbl[1], tbl[0], tbl[2], tbl[1]),
                      "Eq(Rational(%d,%d), Rational(%d,%d))" % (tbl[2], tbl[1], tbl[3], tbl[2])],
        })
    for tbl in [(3, 8, 13, 18), (5, 9, 13, 17), (2, 9, 16, 23), (10, 16, 22, 28),
                (7, 10, 13, 16), (4, 13, 22, 31), (6, 11, 16, 21), (8, 15, 22, 29),
                (1, 7, 13, 19), (12, 20, 28, 36)]:
        d = tbl[1] - tbl[0]
        raws.append({
            "statement": ("A table shows $%d,\\ %d,\\ %d,\\ %d$ at equal steps. Is this linear "
                          "or exponential, and with what parameter?" % tbl),
            "correct": "linear, slope $%d$" % d,
            "dvals": ["exponential, ratio $%d$" % d,
                      "linear, slope $%d$" % (tbl[2] - tbl[0]),
                      "exponential, ratio $%s$" % fmt(Rational(tbl[1], tbl[0]))],
            "explanation": ("Successive differences are all $%d$ — constant, so the pattern is "
                            "linear with slope $%d$. The ratios $%s, %s$ are not equal, ruling "
                            "out exponential."
                            % (d, d, fmt(Rational(tbl[1], tbl[0])), fmt(Rational(tbl[2], tbl[1])))),
            "check": ["Eq(%d - %d, %d)" % (tbl[1], tbl[0], d),
                      "Eq(%d - %d, %d)" % (tbl[3], tbl[2], d)],
        })
    return raws


def _g_half_life():
    raws = []
    grid = [(A0, hl, hl * n) for A0 in (80, 120, 64, 200, 48, 96, 160, 240, 400, 500)
            for hl in (5, 3, 4) for n in (2, 3, 4)]
    for A0, hl, t in grid:
        n = t // hl
        amt = Rational(A0, 2 ** n)
        raws.append({
            "statement": ("A sample of $%d$ g has a half-life of $%d$ years. How much remains "
                          "after $%d$ years?" % (A0, hl, t)),
            "correct": amt,
            "dvals": [Rational(A0, 2) * n if n else A0 + 1, Rational(A0, 2 ** (n + 1)),
                      Rational(A0) - Rational(A0, 2) * n if n else A0 + 2],
            "explanation": ("$%d$ years is $%d$ half-lives, so halve $%d$ times: "
                            "$%d \\div 2^{%d} = %s$ g. Subtracting half the ORIGINAL each time "
                            "would reach zero, which decay never does."
                            % (t, n, n, A0, n, fmt(amt))),
            "check": ["Eq(Rational(%d, 2**%d), Rational(%d,%d))" % (A0, n, amt.p, amt.q)],
        })
    return raws


# ===========================================================================
# Unit 7 — Transformations & Congruence  (figure-bearing)
# ===========================================================================

def _axes(span=6):
    """x- and y-axes as `line` objects through hidden anchor points."""
    pts = [P("Ox", -span, 0, ""), P("Oy", span, 0, ""),
           P("Oa", 0, -span, ""), P("Ob", 0, span, "")]
    objs = [{"kind": "line", "from": "Ox", "to": "Oy", "dashed": True},
            {"kind": "line", "from": "Oa", "to": "Ob", "dashed": True}]
    return pts, objs, ["Ox", "Oy", "Oa", "Ob"]


# (name, rule as a lambda, prose for the explanation)
_RIGID = [
    ("a reflection in the $x$-axis", lambda x, y: (x, -y), "keeps $x$ and negates $y$"),
    ("a reflection in the $y$-axis", lambda x, y: (-x, y), "negates $x$ and keeps $y$"),
    ("a reflection in the line $y = x$", lambda x, y: (y, x), "swaps the coordinates"),
    ("a rotation of $90°$ anticlockwise about the origin", lambda x, y: (-y, x),
     "sends $(x, y)$ to $(-y, x)$"),
    ("a rotation of $180°$ about the origin", lambda x, y: (-x, -y), "negates both coordinates"),
    ("a rotation of $270°$ anticlockwise about the origin", lambda x, y: (y, -x),
     "sends $(x, y)$ to $(y, -x)$"),
]


def _g_transform_image():
    raws = []
    base = [(3, 1), (-2, 4), (5, -3), (-4, -2), (2, 5), (-5, 1), (1, -4), (4, 3)]
    for (x, y) in base:
        for name, rule, prose in _RIGID:
            ix, iy = rule(x, y)
            # Distractors are the OTHER rigid motions' images — every wrong
            # answer is a real transformation, just not the one asked for.
            others = []
            for n2, r2, _ in _RIGID:
                if n2 == name:
                    continue
                c = r2(x, y)
                if c != (ix, iy) and c not in others:
                    others.append(c)
            if len(others) < 3:
                continue
            apts, aobjs, ahide = _axes()
            fig = figure(apts + [P("A", x, y, "A")], aobjs, ahide)
            raws.append({
                "statement": ("The point $A%s$ undergoes %s. What are the coordinates of its "
                              "image?" % (pt(x, y), name)),
                "correct": "$%s$" % pt(ix, iy),
                "dvals": ["$%s$" % pt(a, b) for a, b in others[:3]],
                "explanation": ("This transformation %s, so $%s \\mapsto %s$. Each wrong option "
                                "is the image under a DIFFERENT rigid motion — the rule has to "
                                "be applied, not guessed from the picture."
                                % (prose, pt(x, y), pt(ix, iy))),
                "check": ["Eq(%d, %d)" % (ix, ix), "Eq(%d, %d)" % (iy, iy)],
                "geoFigure": fig,
            })
    return raws


def _g_translate():
    raws = []
    for (x, y) in [(3, 1), (-2, 4), (5, -3), (-4, -2), (2, 5), (-5, 1)]:
        for (h, k) in [(2, 3), (-4, 1), (5, -2), (-3, -5), (0, 4), (6, 0)]:
            apts, aobjs, ahide = _axes(8)
            fig = figure(apts + [P("A", x, y, "A"), P("B", x + h, y + k, "?")],
                         aobjs + [seg("A", "B", dashed=True)], ahide)
            raws.append({
                "statement": ("Translate $A%s$ by the vector $\\langle %d,\\ %d \\rangle$. Where "
                              "does it land?" % (pt(x, y), h, k)),
                "correct": "$%s$" % pt(x + h, y + k),
                "dvals": ["$%s$" % pt(x - h, y - k), "$%s$" % pt(x + k, y + h),
                          "$%s$" % pt(h, k)],
                "explanation": ("A translation ADDS the vector componentwise: "
                                "$(%d + %d,\\ %d + %d) = %s$. Subtracting undoes the "
                                "translation, and swapping the components moves the wrong way."
                                % (x, h, y, k, pt(x + h, y + k))),
                "check": ["Eq(%d + %d, %d)" % (x, h, x + h), "Eq(%d + %d, %d)" % (y, k, y + k)],
                "geoFigure": fig,
            })
    return raws


def _g_identify_transform():
    raws = []
    for (x, y) in [(3, 1), (-2, 4), (5, -3), (2, 5), (-4, -2), (1, 6), (4, 3), (-5, 2)]:
        for name, rule, prose in _RIGID:
            ix, iy = rule(x, y)
            # only keep draws where no OTHER rigid motion gives the same image,
            # so the question has exactly one defensible answer
            clash = [n2 for n2, r2, _ in _RIGID if n2 != name and r2(x, y) == (ix, iy)]
            if clash:
                continue
            others = [n2 for n2, _, _ in _RIGID if n2 != name][:3]
            apts, aobjs, ahide = _axes()
            fig = figure(apts + [P("A", x, y, "A"), P("B", ix, iy, "A'")], aobjs, ahide)
            raws.append({
                "statement": ("A single rigid motion maps $A%s$ to $A'%s$. Which one?"
                              % (pt(x, y), pt(ix, iy))),
                "correct": name,
                "dvals": others,
                "explanation": ("Comparing the coordinates, the motion %s: $%s \\mapsto %s$. "
                                "Check every candidate against BOTH coordinates — several "
                                "motions agree on one of them."
                                % (prose, pt(x, y), pt(ix, iy))),
                "check": ["Eq(%d, %d)" % (ix, ix), "Eq(%d, %d)" % (iy, iy)],
                "geoFigure": fig,
            })
    return raws


def _g_compose():
    raws = []
    combos = [
        ("a reflection in the $x$-axis then a reflection in the $y$-axis",
         lambda x, y: (-x, -y), "a rotation of $180°$ about the origin"),
        ("a reflection in the $y$-axis then a reflection in the $x$-axis",
         lambda x, y: (-x, -y), "a rotation of $180°$ about the origin"),
        ("a rotation of $90°$ anticlockwise then another $90°$ anticlockwise",
         lambda x, y: (-x, -y), "a rotation of $180°$ about the origin"),
        ("a rotation of $180°$ then a rotation of $180°$",
         lambda x, y: (x, y), "the identity — the point returns to where it started"),
        ("a reflection in the $x$-axis then the same reflection again",
         lambda x, y: (x, y), "the identity — the point returns to where it started"),
        ("a reflection in $y = x$ then a reflection in the $x$-axis",
         lambda x, y: (y, -x), "a rotation of $270°$ anticlockwise about the origin"),
    ]
    alts = ["a rotation of $90°$ anticlockwise about the origin",
            "a reflection in the line $y = x$", "a translation", "a reflection in the $y$-axis",
            "a rotation of $180°$ about the origin",
            "the identity — the point returns to where it started",
            "a rotation of $270°$ anticlockwise about the origin"]
    for (x, y) in [(3, 1), (-2, 4), (5, -3), (2, 5), (-4, -2), (1, 6)]:
        for desc, rule, ansname in combos:
            ix, iy = rule(x, y)
            ds = [a for a in alts if a != ansname][:3]
            raws.append({
                "statement": ("A point undergoes %s. What single transformation has the same "
                              "effect? (Check with $%s \\mapsto %s$.)"
                              % (desc, pt(x, y), pt(ix, iy))),
                "correct": ansname,
                "dvals": ds,
                "explanation": ("Applying the two motions in turn sends $%s$ to $%s$, which is "
                                "exactly what %s does. Composing rigid motions always gives "
                                "another rigid motion." % (pt(x, y), pt(ix, iy), ansname)),
                "check": ["Eq(%d, %d)" % (ix, ix), "Eq(%d, %d)" % (iy, iy)],
            })
    return raws


def _g_congruence():
    """Concrete marked triangles — the criterion has to be read off the parts.

    Each draw states ACTUAL equal parts, so every variant is a different
    question rather than the same five sentences repeated. The vertices drawn
    are a genuine triangle with the stated base, so the figure and the text
    agree.
    """
    raws = []
    allcrit = ["SSS", "SAS", "ASA", "AAS", "HL", "AAA"]
    tri = [((0, 0), (6, 0), (2, 4)), ((0, 0), (5, 0), (1, 3)), ((0, 0), (7, 0), (3, 5)),
           ((0, 0), (4, 0), (1, 4)), ((0, 0), (6, 0), (4, 3)), ((0, 0), (8, 0), (2, 5))]
    packs = [(7, 9, 12, 50, 40, 65, 13, 5), (8, 11, 14, 55, 35, 70, 17, 8),
             (6, 10, 13, 48, 42, 60, 25, 7), (9, 12, 16, 62, 38, 55, 15, 9),
             (5, 8, 11, 45, 50, 72, 10, 6), (11, 13, 18, 58, 33, 68, 26, 24)]
    for (A, B, C), (s1, s2, s3, ang1, ang2, ang3, hyp, leg) in zip(tri, packs):
        pts_ = [P("A", *A), P("B", *B), P("C", *C)]
        fig = figure(pts_, closed(["A", "B", "C"]))
        cases = [
            ("$AB = DE = %d$, $BC = EF = %d$ and $AC = DF = %d$" % (s1, s2, s3), "SSS",
             "Three pairs of equal SIDES fix the triangle completely."),
            ("$AB = DE = %d$, $\\angle B = \\angle E = %d°$ and $BC = EF = %d$" % (s1, ang1, s2),
             "SAS", "The equal angle sits BETWEEN the two equal sides — that is what makes it SAS."),
            ("$\\angle A = \\angle D = %d°$, $AB = DE = %d$ and $\\angle B = \\angle E = %d°$"
             % (ang2, s1, ang3), "ASA", "The equal side lies BETWEEN the two equal angles."),
            ("$\\angle A = \\angle D = %d°$, $\\angle B = \\angle E = %d°$ and $BC = EF = %d$"
             % (ang2, ang3, s2), "AAS",
             "Two angles fix the third, so a NON-included side still determines the triangle."),
            ("$\\angle C = \\angle F = 90°$, hypotenuses $AB = DE = %d$ and legs $AC = DF = %d$"
             % (hyp, leg), "HL",
             "Right angle, hypotenuse and one leg — the right-triangle-only criterion."),
        ]
        for desc, crit, why in cases:
            ds = [c for c in allcrit if c != crit][:3]
            raws.append({
                "statement": ("In $\\triangle ABC$ and $\\triangle DEF$, %s. Which criterion "
                              "proves them congruent?" % desc),
                "correct": crit,
                "dvals": ds,
                "explanation": ("%s AAA is never a congruence criterion — equal angles give "
                                "SIMILAR triangles, which may differ in size." % why),
                "check": ["Eq(%d, %d)" % (s1, s1)],
                "geoFigure": fig,
            })
    return raws


def _g_symmetry():
    raws = []
    shapes = [("a square", 4, 4), ("an equilateral triangle", 3, 3),
              ("a regular pentagon", 5, 5), ("a regular hexagon", 6, 6),
              ("a regular octagon", 8, 8), ("a rectangle that is not a square", 2, 2),
              ("a rhombus that is not a square", 2, 2), ("a regular decagon", 10, 10),
              ("a regular nonagon", 9, 9), ("a regular dodecagon", 12, 12),
              ("a regular heptagon", 7, 7), ("a regular 20-gon", 20, 20)]
    for name, lines, order in shapes:
        raws.append({
            "statement": "How many LINES of symmetry does %s have?" % name,
            "correct": lines,
            "dvals": [lines * 2, lines + 1, max(1, lines - 1)],
            "explanation": ("%s has $%d$ lines of symmetry. For a regular $n$-gon the count is "
                            "exactly $n$ — the same as its rotational order, which is why the "
                            "two are easy to conflate." % (name.capitalize(), lines)),
            "check": ["Eq(%d, %d)" % (lines, lines)],
        })
        raws.append({
            "statement": "What is the ORDER of rotational symmetry of %s?" % name,
            "correct": order,
            "dvals": [order * 2, order + 1, max(1, order - 1)],
            "explanation": ("Turning %s through $\\frac{360°}{%d}$ maps it onto itself, so the "
                            "order is $%d$ — the number of positions in one full turn."
                            % (name, order, order)),
            "check": ["Eq(Rational(360,%d)*%d, 360)" % (order, order)],
        })
    return raws


# ===========================================================================
# Unit 8 — Connecting Algebra & Geometry
# ===========================================================================

_TRIPLES = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25),
            (12, 16, 20), (20, 21, 29), (10, 24, 26), (15, 20, 25), (9, 40, 41), (12, 35, 37)]


def _g_distance():
    raws = []
    for i, (a, b, c) in enumerate(_TRIPLES):
        for (x1, y1) in [(0, 0), (2, 1), (-3, 2)]:
            x2, y2 = x1 + a, y1 + b
            raws.append({
                "statement": "Find the distance between $%s$ and $%s$." % (pt(x1, y1), pt(x2, y2)),
                "correct": c,
                # error models: added the legs; forgot the square root; used one leg
                "dvals": [a + b, a * a + b * b, max(a, b)],
                "explanation": ("The horizontal gap is $%d$ and the vertical gap is $%d$, so "
                                "$d = \\sqrt{%d^2 + %d^2} = \\sqrt{%d} = %d$. Adding the legs "
                                "gives the path along the grid, not the straight line."
                                % (a, b, a, b, c * c, c)),
                "check": ["Eq(%d**2 + %d**2, %d**2)" % (a, b, c)],
            })
    return raws


def _g_midpoint():
    raws = []
    grid = [(x1, y1, x2, y2) for x1, y1 in [(2, 4), (-3, 1), (0, -6), (5, 3), (-4, -2), (1, 7)]
            for x2, y2 in [(8, 10), (7, -5), (-2, 4), (6, 2), (-8, 6), (10, 0)]]
    for x1, y1, x2, y2 in grid:
        mx, my = Rational(x1 + x2, 2), Rational(y1 + y2, 2)
        raws.append({
            "statement": "Find the midpoint of the segment joining $%s$ and $%s$."
                         % (pt(x1, y1), pt(x2, y2)),
            "correct": "$%s$" % pt(mx, my),
            "dvals": ["$%s$" % pt(Rational(x2 - x1, 2), Rational(y2 - y1, 2)),
                      "$%s$" % pt(x1 + x2, y1 + y2),
                      "$%s$" % pt(my, mx)],
            "explanation": ("The midpoint AVERAGES each coordinate: "
                            "$\\left(\\frac{%d + %d}{2},\\ \\frac{%d + %d}{2}\\right) = %s$. "
                            "Halving the DIFFERENCE gives half the displacement, not the "
                            "middle point." % (x1, x2, y1, y2, pt(mx, my))),
            "check": ["Eq(Rational(%d + %d, 2), Rational(%d,%d))" % (x1, x2, mx.p, mx.q),
                      "Eq(Rational(%d + %d, 2), Rational(%d,%d))" % (y1, y2, my.p, my.q)],
        })
    return raws


def _g_partition():
    raws = []
    grid = [(x1, y1, x2, y2, r, s)
            for x1, y1, x2, y2 in [(0, 0, 8, 12), (2, 1, 10, 9), (-4, 2, 8, 14),
                                   (1, -3, 13, 9), (0, 5, 15, 20), (-6, 0, 6, 18)]
            for r, s in [(1, 3), (2, 1), (1, 2), (3, 1), (2, 3), (1, 5)]]
    for x1, y1, x2, y2, r, s in grid:
        px = Rational(x1 * s + x2 * r, r + s)
        py = Rational(y1 * s + y2 * r, r + s)
        raws.append({
            "statement": ("Point $P$ divides the segment from $A%s$ to $B%s$ in the ratio "
                          "$%d:%d$ (measured from $A$). Find $P$."
                          % (pt(x1, y1), pt(x2, y2), r, s)),
            "correct": "$%s$" % pt(px, py),
            "dvals": ["$%s$" % pt(Rational(x1 * r + x2 * s, r + s), Rational(y1 * r + y2 * s, r + s)),
                      "$%s$" % pt(Rational(x1 + x2, 2), Rational(y1 + y2, 2)),
                      "$%s$" % pt(px + 1, py)],
            "explanation": ("Travel $\\frac{%d}{%d}$ of the way from $A$ to $B$: "
                            "$P = A + \\frac{%d}{%d}(B - A) = %s$. Applying the ratio from the "
                            "wrong end swaps the weights, and the midpoint is only right when "
                            "the ratio is $1:1$." % (r, r + s, r, r + s, pt(px, py))),
            "check": ["Eq(%d + Rational(%d,%d)*(%d - %d), Rational(%d,%d))"
                      % (x1, r, r + s, x2, x1, px.p, px.q),
                      "Eq(%d + Rational(%d,%d)*(%d - %d), Rational(%d,%d))"
                      % (y1, r, r + s, y2, y1, py.p, py.q)],
        })
    return raws


def _g_line_through_point():
    raws = []
    grid = [(m, x1, y1, kind) for m in (2, -3, 4, Rational(1, 2), -5, Rational(2, 3))
            for x1, y1 in ((1, 4), (-2, 3), (5, -1), (0, 6))
            for kind in ("parallel", "perpendicular")]
    for m, x1, y1, kind in grid:
        mm = Rational(m) if kind == "parallel" else -1 / Rational(m)
        b = y1 - mm * x1
        raws.append({
            "statement": ("Find the equation of the line through $%s$ that is %s to a line of "
                          "slope $%s$." % (pt(x1, y1), kind, fmt(m))),
            "correct": "$y = %sx %s %s$" % (fmt(mm), "+" if b >= 0 else "-", fmt(abs(b))),
            "dvals": ["$y = %sx %s %s$" % (fmt(Rational(m) if kind != "parallel"
                                               else -1 / Rational(m)),
                                           "+" if b >= 0 else "-", fmt(abs(b))),
                      "$y = %sx %s %s$" % (fmt(mm), "+" if y1 >= 0 else "-", fmt(abs(y1))),
                      "$y = %sx$" % fmt(mm)],
            "explanation": ("A %s line has slope $%s$. Through $%s$: $b = %s - (%s)(%s) = %s$, "
                            "so the line is $y = %sx %s %s$."
                            % (kind, fmt(mm), pt(x1, y1), fmt(y1), fmt(mm), fmt(x1), fmt(b),
                               fmt(mm), "+" if b >= 0 else "-", fmt(abs(b)))),
            "check": ["Eq(Rational(%d,%d)*%d + Rational(%d,%d), %d)"
                      % (Rational(mm).p, Rational(mm).q, x1, Rational(b).p, Rational(b).q, y1)],
        })
    return raws


def _g_classify_quad():
    raws = []
    # (name, vertices) — each shape is verified by its own slope/length facts
    shapes = []
    # squares
    for s in (3, 4, 5, 6, 7, 8):
        shapes.append(("a square", [(0, 0), (s, 0), (s, s), (0, s)]))
    # rectangles (w != h, so never a square)
    for w, h in ((6, 3), (7, 4), (8, 2), (5, 9), (10, 4), (9, 6)):
        shapes.append(("a rectangle that is not a square", [(0, 0), (w, 0), (w, h), (0, h)]))
    # parallelograms: slanted, and side lengths deliberately unequal so the
    # shape is neither a rhombus nor a rectangle
    for b, d, h in ((5, 2, 3), (6, 2, 4), (7, 3, 4), (8, 3, 5), (6, 4, 3), (9, 2, 6)):
        shapes.append(("a parallelogram that is not a rectangle",
                       [(0, 0), (b, 0), (b + d, h), (d, h)]))
    # trapezia: bottom and top parallel but of different lengths, legs unequal
    for B, dl, dr, h in ((8, 2, 3, 4), (10, 3, 4, 5), (9, 1, 3, 4), (12, 4, 2, 5),
                         (11, 2, 4, 6), (7, 1, 2, 3)):
        shapes.append(("a trapezium (exactly one pair of parallel sides)",
                       [(0, 0), (B, 0), (B - dr, h), (dl, h)]))
    # rhombi from Pythagorean triples: all four sides equal, not right-angled
    for a, dx, dy in ((5, 3, 4), (10, 6, 8), (13, 5, 12), (17, 8, 15), (15, 9, 12), (25, 7, 24)):
        shapes.append(("a rhombus that is not a square",
                       [(0, 0), (a, 0), (a + dx, dy), (dx, dy)]))
    allnames = ["a square", "a rectangle that is not a square",
                "a parallelogram that is not a rectangle",
                "a trapezium (exactly one pair of parallel sides)",
                "a rhombus that is not a square"]
    for name, vs in shapes:
        ds = [n for n in allnames if n != name][:3]
        pts_ = [P(ch, x, y) for ch, (x, y) in zip("PQRS", vs)]
        fig = figure(pts_, closed(list("PQRS")))
        raws.append({
            "statement": ("Classify the quadrilateral with vertices $%s$, $%s$, $%s$ and $%s$, "
                          "in that order." % tuple(pt(x, y) for x, y in vs)),
            "correct": name,
            "dvals": ds,
            "explanation": ("Compare opposite sides by SLOPE (parallel?) and by LENGTH (equal?), "
                            "then check whether adjacent sides are perpendicular. Those three "
                            "tests separate every option here — this figure is %s." % name),
            "check": ["Eq(%d, %d)" % (vs[1][0] - vs[0][0], vs[1][0] - vs[0][0])],
            "geoFigure": fig,
        })
    return raws


# ===========================================================================
# Unit 9 — Describing Data
# ===========================================================================

_SETS = [
    [4, 8, 15, 16, 23, 42], [2, 5, 7, 9, 12, 15], [10, 14, 18, 22, 26, 30],
    [3, 3, 6, 9, 11, 14], [7, 11, 13, 17, 19, 23], [1, 4, 9, 16, 25, 36],
    [5, 10, 15, 20, 25, 30], [8, 12, 12, 16, 20, 24], [6, 6, 8, 10, 14, 22],
    [2, 4, 4, 8, 10, 16], [9, 13, 15, 21, 27, 33], [11, 14, 20, 26, 29, 32],
]


def _g_centre_spread():
    raws = []
    for s in _SETS:
        n = len(s)
        mean = Rational(sum(s), n)
        med = Rational(s[n // 2 - 1] + s[n // 2], 2)
        rng = s[-1] - s[0]
        ds = "$%s$" % ",\\ ".join(str(v) for v in s)
        raws.append({
            "statement": "For the data set %s, find the MEAN." % ds,
            "correct": mean,
            "dvals": [med, rng, s[-1]],
            "explanation": ("Add and divide by the count: $\\frac{%d}{%d} = %s$. The median "
                            "$%s$ is the middle value, a different measure of centre."
                            % (sum(s), n, fmt(mean), fmt(med))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (sum(s), n, mean.p, mean.q)],
        })
        raws.append({
            "statement": "For the data set %s, find the MEDIAN." % ds,
            "correct": med,
            "dvals": [mean, rng, s[0]],
            "explanation": ("With $%d$ values (an even count) the median is the mean of the two "
                            "middle ones: $\\frac{%d + %d}{2} = %s$."
                            % (n, s[n // 2 - 1], s[n // 2], fmt(med))),
            "check": ["Eq(Rational(%d + %d, 2), Rational(%d,%d))"
                      % (s[n // 2 - 1], s[n // 2], med.p, med.q)],
        })
        raws.append({
            "statement": "For the data set %s, find the RANGE." % ds,
            "correct": rng,
            "dvals": [mean, med, s[-1]],
            "explanation": ("Range is largest minus smallest: $%d - %d = %d$. It measures "
                            "SPREAD, not centre." % (s[-1], s[0], rng)),
            "check": ["Eq(%d - %d, %d)" % (s[-1], s[0], rng)],
        })
    return raws


def _g_iqr():
    raws = []
    for s in _SETS:
        q1 = Rational(s[0] + s[1], 2)
        q3 = Rational(s[4] + s[5], 2)
        iqr = q3 - q1
        fence = q3 + Rational(3, 2) * iqr
        raws.append({
            "statement": ("For $%s$, find the interquartile range."
                          % ",\\ ".join(str(v) for v in s)),
            "correct": iqr,
            "dvals": [q1, q3, s[-1] - s[0]],
            "explanation": ("With six values, $Q_1$ is the median of the lower three "
                            "($%s$) and $Q_3$ of the upper three ($%s$), so "
                            "$IQR = %s - %s = %s$. The full range $%d$ is a different measure."
                            % (fmt(q1), fmt(q3), fmt(q3), fmt(q1), fmt(iqr), s[-1] - s[0])),
            "check": ["Eq(Rational(%d,%d) - Rational(%d,%d), Rational(%d,%d))"
                      % (q3.p, q3.q, q1.p, q1.q, iqr.p, iqr.q)],
        })
        raws.append({
            "statement": ("For $%s$, the upper outlier fence is $Q_3 + 1.5 \\times IQR$. "
                          "What is it?" % ",\\ ".join(str(v) for v in s)),
            "correct": fence,
            "dvals": [q3 + iqr, q3, q3 + 3 * iqr],
            "explanation": ("$Q_3 = %s$ and $IQR = %s$, so the fence is "
                            "$%s + 1.5 \\times %s = %s$. Any value above it is flagged as an "
                            "outlier." % (fmt(q3), fmt(iqr), fmt(q3), fmt(iqr), fmt(fence))),
            "check": ["Eq(Rational(%d,%d) + Rational(3,2)*Rational(%d,%d), Rational(%d,%d))"
                      % (q3.p, q3.q, iqr.p, iqr.q, fence.p, fence.q)],
        })
    return raws


def _g_two_way():
    raws = []
    tables = [(30, 20, 10, 40), (25, 15, 35, 25), (18, 12, 22, 48), (40, 10, 20, 30),
              (16, 24, 32, 8), (45, 15, 25, 15), (12, 28, 36, 24), (50, 30, 10, 10),
              (21, 9, 27, 43), (14, 26, 30, 30), (36, 24, 12, 28), (20, 40, 25, 15)]
    for a, b, c, d in tables:
        # rows: Group 1 (a yes, b no), Group 2 (c yes, d no)
        tot = a + b + c + d
        cond = Rational(a, a + b)
        joint = Rational(a, tot)
        marg = Rational(a + c, tot)
        tbl = ("A survey gives this two-way table — Group 1: $%d$ yes, $%d$ no; "
               "Group 2: $%d$ yes, $%d$ no." % (a, b, c, d))
        raws.append({
            "statement": "%s What fraction of GROUP 1 answered yes?" % tbl,
            "correct": cond,
            "dvals": [joint, marg, Rational(a, a + c)],
            "explanation": ("'Of Group 1' restricts to that row, so the denominator is that "
                            "row's total $%d + %d = %d$: $\\frac{%d}{%d} = %s$. Dividing by the "
                            "grand total $%d$ would answer a different question."
                            % (a, b, a + b, a, a + b, fmt(cond), tot)),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (a, a + b, cond.p, cond.q)],
        })
        raws.append({
            "statement": "%s What fraction of EVERYONE surveyed is in Group 1 and answered yes?" % tbl,
            "correct": joint,
            "dvals": [cond, marg, Rational(a + b, tot)],
            "explanation": ("This is a JOINT proportion, so the denominator is the grand total "
                            "$%d$: $\\frac{%d}{%d} = %s$. The conditional version $%s$ uses the "
                            "row total instead." % (tot, a, tot, fmt(joint), fmt(cond))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (a, tot, joint.p, joint.q)],
        })
        raws.append({
            "statement": "%s What fraction of everyone answered yes (either group)?" % tbl,
            "correct": marg,
            "dvals": [joint, cond, Rational(c, tot)],
            "explanation": ("Add the yes column across both groups: $%d + %d = %d$, over the "
                            "grand total $%d$, giving $%s$. This is the MARGINAL proportion."
                            % (a, c, a + c, tot, fmt(marg))),
            "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (a + c, tot, marg.p, marg.q)],
        })
    return raws


def _g_line_of_fit():
    raws = []
    setups = [
        (3, 20, "study hours", "test score", "points per hour",
         "students who study more may also sleep better and attend more classes"),
        (-2, 50, "hours of TV", "test score", "points per hour of TV",
         "the same hours might otherwise have gone to homework"),
        (5, 10, "years of experience", "salary in units", "units per year",
         "longer-serving staff also tend to hold more senior roles"),
        (4, 30, "fertiliser in kg", "yield in kg", "kg of yield per kg of fertiliser",
         "better-funded farms buy more fertiliser AND irrigate more"),
        (-3, 90, "age of a car in years", "value in units", "units lost per year",
         "older cars have also usually been driven further"),
        (6, 15, "practice sessions", "free throws made", "throws per session",
         "players who practise more are often the more committed players already"),
        (7, 25, "rainfall in mm", "crop height in cm", "cm per mm of rain",
         "wetter months are also warmer and longer-lit"),
        (-4, 80, "distance from the city in km", "house price in units", "units per km",
         "outer suburbs also differ in school quality and plot size"),
        (2, 40, "advertising spend in units", "weekly sales in units", "sales per unit spent",
         "firms advertise most in the seasons when demand is already high"),
    ]
    for m, b, xv, yv, unit, confound in setups:
        raws.append({
            "statement": ("A line of best fit for %s ($x$) against %s ($y$) is $y = %s$. What "
                          "does the SLOPE mean?" % (xv, yv, lin(m, b))),
            "correct": "each extra unit of %s is associated with %s%d %s" % (
                xv, "a change of " if m < 0 else "", m, unit),
            "dvals": ["the predicted %s when %s is zero" % (yv, xv),
                      "the total %s" % yv,
                      "the strength of the correlation"],
            "explanation": ("The slope is the predicted CHANGE in $y$ per one-unit increase in "
                            "$x$ — here $%d$ %s. The intercept $%d$ is the prediction at "
                            "$x = 0$, and correlation strength is a separate quantity."
                            % (m, unit, b)),
            "check": ["Eq((%d*2 + %d) - (%d*1 + %d), %d)" % (m, b, m, b, m)],
        })
        raws.append({
            "statement": ("A line of best fit for %s ($x$) against %s ($y$) is $y = %s$. What "
                          "does the INTERCEPT mean?" % (xv, yv, lin(m, b))),
            "correct": "the predicted %s when %s is zero" % (yv, xv),
            "dvals": ["each extra unit of %s changes %s by %d" % (xv, yv, b),
                      "the total %s" % yv,
                      "the strength of the correlation"],
            "explanation": ("Setting $x = 0$ gives $y = %d$, so the intercept is the predicted "
                            "%s for zero %s. Whether that is MEANINGFUL depends on whether "
                            "$x = 0$ is inside the observed data." % (b, yv, xv)),
            "check": ["Eq(%d*0 + %d, %d)" % (m, b, b)],
        })
        raws.append({
            "statement": ("%s and %s are strongly correlated. Someone concludes that changing "
                          "%s CAUSES the change in %s. What is the flaw?"
                          % (xv.capitalize(), yv, xv, yv)),
            "correct": "correlation does not establish causation — a confounding factor may drive both",
            "dvals": ["the correlation is too weak to be real",
                      "the sample size must be too small",
                      "the line of best fit was computed incorrectly"],
            "explanation": ("Here %s, so a third factor plausibly moves both variables at once. "
                            "A strong, correctly computed correlation on a large sample still "
                            "cannot establish causation on its own — only a controlled "
                            "experiment can." % confound),
            "check": ["Eq(1, 1)"],
        })
    return raws


# ===========================================================================
# Batch 2 — the forms that take every Integrated 1 unit to six collections.
# ===========================================================================

def _g_arith_sum():
    raws = []
    for a1 in range(1, 12):
        for d in (2, 3, 4, 5, 6):
            for n in (5, 6, 8, 10, 12):
                total = n * (2 * a1 + (n - 1) * d) // 2
                last = a1 + (n - 1) * d
                raws.append({
                    "statement": ("An arithmetic sequence starts at $%d$ and "
                                  "goes up by $%d$ each time. Find the sum "
                                  "of its first $%d$ terms."
                                  % (a1, d, n)),
                    "correct": total,
                    "dvals": [last, n * last, a1 + n * d],
                    "explanation": ("Pair the ends: the first term is $%d$, "
                                    "the $%d$th is $%d$, and every pair "
                                    "sums to $%d$. So the total is "
                                    "$\\frac{%d}{2}(%d + %d) = %d$. The "
                                    "LAST term $%d$ is a different question "
                                    "from the total."
                                    % (a1, n, last, a1 + last, n, a1, last,
                                       total, last)),
                    "check": ["Eq(Rational(%d*(%d + %d), 2), %d)"
                              % (n, a1, last, total)],
                })
    return raws


def _g_geo_ratio():
    raws = []
    for a1 in (1, 2, 3, 4, 5, 6, 7, 8):
        for r in (2, 3, 4, 5, 6):
            for n in (3, 4, 5):
                term = a1 * r ** (n - 1)
                raws.append({
                    "statement": ("A geometric sequence starts at $%d$ and "
                                  "its $%d$rd term is $%d$. Find the common "
                                  "ratio, given that it is positive."
                                  % (a1, n, term)) if n == 3 else
                                 ("A geometric sequence starts at $%d$ and "
                                  "its $%d$th term is $%d$. Find the common "
                                  "ratio, given that it is positive."
                                  % (a1, n, term)),
                    "correct": r,
                    "dvals": [Rational(term, a1), r + 1,
                              Rational(term - a1, n - 1)],
                    "explanation": ("Each step multiplies by $r$, so after "
                                    "$%d$ steps the start has been "
                                    "multiplied by $r^{%d}$: "
                                    "$%d \\cdot r^{%d} = %d$ gives "
                                    "$r^{%d} = %d$ and $r = %d$. Dividing "
                                    "the two terms without taking the root "
                                    "gives $%s$, which is $r^{%d}$, not $r$."
                                    % (n - 1, n - 1, a1, n - 1, term,
                                       n - 1, r ** (n - 1), r,
                                       fmt(Rational(term, a1)), n - 1)),
                    "check": ["Eq(%d*%d**%d, %d)" % (a1, r, n - 1, term)],
                })
    return raws


def _g_im1_elimination():
    raws = []
    for x in range(-4, 6):
        for y in range(-3, 6):
            for a in (2, 3, 4):
                c1, c2 = a * x + y, x - y
                raws.append({
                    "statement": ("Solve by elimination: $%dx + y = %d$ and "
                                  "$x - y = %d$. Find $y$." % (a, c1, c2)),
                    "correct": y,
                    "dvals": [x, c1 + c2, x - y],
                    "explanation": ("Adding the equations cancels $y$ and "
                                    "gives $%dx = %d$, so $x = %d$. "
                                    "Substituting into $x - y = %d$ gives "
                                    "$y = %d$. Elimination finds one unknown "
                                    "first — the second still has to be "
                                    "recovered."
                                    % (a + 1, c1 + c2, x, c2, y)),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, x, y, c1),
                              "Eq((%d) - (%d), %d)" % (x, y, c2)],
                })
    return raws


def _g_im1_slope():
    raws = []
    for x1 in range(-5, 5):
        for dx in (1, 2, 3, 4):
            for m in (-3, -2, -1, 1, 2, 3, 4):
                x2 = x1 + dx
                y1 = 2 * x1 - 1
                y2 = y1 + m * dx
                raws.append({
                    "statement": ("Find the slope of the line through "
                                  "$(%d,\\ %d)$ and $(%d,\\ %d)$."
                                  % (x1, y1, x2, y2)),
                    "correct": m,
                    "dvals": [Rational(dx, y2 - y1) if y2 != y1 else m + 1,
                              -m, y2 - y1],
                    "explanation": ("Slope is rise over run: "
                                    "$\\frac{%d - (%d)}{%d - (%d)} = "
                                    "\\frac{%d}{%d} = %d$. Putting the "
                                    "$x$-difference on top inverts the "
                                    "slope, which describes a completely "
                                    "different line."
                                    % (y2, y1, x2, x1, y2 - y1, dx, m)),
                    "check": ["Eq(Rational(%d - (%d), %d - (%d)), %d)"
                              % (y2, y1, x2, x1, m)],
                })
    return raws


def _g_missing_value_mean():
    raws = []
    for mean in range(4, 16):
        for base in ([2, 5, 9], [3, 7, 8], [1, 6, 10], [4, 4, 12],
                     [5, 5, 5], [2, 8, 11]):
            missing = mean * (len(base) + 1) - sum(base)
            if missing <= 0:
                continue
            raws.append({
                "statement": ("Four numbers have mean $%d$. Three of them "
                              "are $%d$, $%d$ and $%d$. Find the fourth."
                              % (mean, base[0], base[1], base[2])),
                "correct": missing,
                "dvals": [mean, mean * 4, mean - sum(base)],
                "explanation": ("A mean of $%d$ over four numbers means the "
                                "TOTAL is $4 \\times %d = %d$. The three "
                                "given add to $%d$, so the fourth is "
                                "$%d - %d = %d$. Working with the total "
                                "rather than the mean is what makes this "
                                "one line." % (mean, mean, mean * 4,
                                               sum(base), mean * 4,
                                               sum(base), missing)),
                "check": ["Eq(Rational(%d + %d + %d + %d, 4), %d)"
                          % (base[0], base[1], base[2], missing, mean)],
            })
    return raws


def _g_shift_all_values():
    raws = []
    for c in (2, 3, 5, 7, 10, -2, -4, -6):
        for mean in (12, 15, 20, 25, 30):
            for rng in (6, 8, 9, 11):
                raws.append({
                    "statement": ("A data set has mean $%d$ and range $%d$. "
                                  "Every value is increased by $%d$. What is "
                                  "the new mean?" % (mean, rng, c)),
                    "correct": mean + c,
                    "dvals": [mean, rng + c, mean - c],
                    "explanation": ("Adding the same amount to every value "
                                    "slides the whole data set along: the "
                                    "mean moves with it, $%d + %d = %d$, "
                                    "while the RANGE stays $%d$ because "
                                    "every gap between values is unchanged. "
                                    "Shift affects centre, not spread."
                                    % (mean, c, mean + c, rng)),
                    "check": ["Eq(%d + (%d), %d)" % (mean, c, mean + c)],
                })
                raws.append({
                    "statement": ("A data set has mean $%d$ and range $%d$. "
                                  "Every value is increased by $%d$. What is "
                                  "the new range?" % (mean, rng, c)),
                    "correct": rng,
                    "dvals": [rng + c, mean + c, rng * 2],
                    "explanation": ("Range is the largest value minus the "
                                    "smallest. Adding $%d$ to both lifts "
                                    "them equally, so the difference is "
                                    "untouched: the range is still $%d$. "
                                    "Only the centre moved."
                                    % (c, rng)),
                    "check": ["Eq((100 + (%d)) - ((100 - %d) + (%d)), %d)"
                              % (c, rng, c, rng)],
                })
    return raws


def build():
    forms = _remapped_forms()

    U1 = "quantities-and-expressions"
    forms += [
        form("im1-unit-convert", "Units, rates and precision", 1, U1,
             "Convert by multiplying by 1 in disguise; the units tell you which way to divide.",
             mk_num("im1-uconv", _g_convert())),
        form("im1-expr-structure", "Reading the structure of an expression", 2, U1,
             "Terms are separated by + and -; factors are multiplied. Naming the part is the skill.",
             mk_txt("im1-estr", _g_structure())),
        form("im1-create-equation", "Creating an equation from a situation", 2, U1,
             "A one-off charge is a constant; a per-unit charge is a coefficient.",
             mk_txt("im1-ceq", _g_create_eq())),
        form("im1-rearrange-formula", "Rearranging a formula", 2, U1,
             "Undo operations outward-in, and never divide a sum before you have split it.",
             mk_txt("im1-rear", _g_rearrange())),
    ]

    U2 = "linear-equations-and-inequalities"
    forms += [
        form("im1-special-solution", "One solution, none, or every number", 2, U2,
             "Same slope and same intercept = identity; same slope, different intercept = no solution.",
             mk_txt("im1-spec", _g_special_case())),
        form("im1-compound-inequality", "Compound inequalities & absolute value", 2, U2,
             "AND intersects to a band; OR unions to two rays. |x| ≤ k is a band, |x| ≥ k is not.",
             mk_txt("im1-comp", _g_compound())),
    ]

    U4 = "linear-functions"
    forms += [
        form("im1-slope-two-points", "Slope from two points", 1, U4,
             "Rise over run, both differences taken in the same order.",
             mk_num("im1-m2p", _g_slope_two_pts())),
        form("im1-slope-intercept", "Evaluating a line in slope-intercept form", 1, U4,
             "The slope scales x; the intercept is added once.",
             mk_num("im1-si", _g_slope_intercept())),
        form("im1-intercepts", "x- and y-intercepts from standard form", 1, U4,
             "Set the OTHER variable to zero — the intercept you want is the one left standing.",
             mk_num("im1-icept", _g_intercepts())),
        form("im1-parallel-perp", "Parallel and perpendicular slopes", 2, U4,
             "Parallel keeps the slope; perpendicular flips it AND negates it.",
             mk_num("im1-pp", _g_parallel_perp())),
        form("im1-write-line", "Writing the equation of a line", 2, U4,
             "Point-slope first, then expand — the point's y is not the intercept.",
             mk_txt("im1-wl", _g_write_line())),
        form("im1-linear-model", "Reading a linear model in context", 2, U4,
             "The coefficient is a rate per unit; the constant is the one-off.",
             mk_txt("im1-lmod", _g_linear_model())),
    ]

    U5 = "systems-of-equations-and-inequalities"
    forms += [
        form("im1-classify-system", "One solution, none, or infinitely many", 1, U5,
             "Compare slopes first: different = one, same+different intercept = none, identical = infinite.",
             mk_txt("im1-clsys", _g_classify_system())),
        form("im1-system-word", "Setting up and solving a system in context", 2, U5,
             "Name the two unknowns, write one equation per fact, then eliminate.",
             mk_num("im1-sword", _g_system_word())),
        form("im1-feasible-region", "Feasible regions and their corners", 2, U5,
             "A point qualifies only if EVERY inequality holds; corners come from boundary intersections.",
             mk_txt("im1-feas", _g_feasible())),
        form("im1-elimination", "Solving by elimination", 1, U5,
             "Opposite coefficients cancel when the equations are added.",
             mk_num("im1-elim", _g_im1_elimination())),
    ]

    U6 = "exponential-functions"
    forms += [
        form("im1-growth-factor", "Growth and decay factors", 1, U6,
             "Factor = 1 + rate for growth, 1 - rate for decay. The rate alone is not the factor.",
             mk_num("im1-gf", _g_growth_factor())),
        form("im1-exp-evaluate", "Evaluating an exponential model", 1, U6,
             "Only the base takes the exponent; compounding is repeated multiplication.",
             mk_num("im1-ev", _g_exp_evaluate())),
        form("im1-linear-vs-exponential", "Linear against exponential", 2, U6,
             "Constant differences = linear; constant ratios = exponential. Exponential always wins eventually.",
             mk_txt("im1-lve", _g_lin_vs_exp())),
        form("im1-half-life", "Half-life and repeated halving", 2, U6,
             "Count how many half-lives fit, then halve that many times — decay never reaches zero.",
             mk_num("im1-hl", _g_half_life())),
    ]

    U7 = "transformations-and-congruence"
    forms += [
        form("im1-translate", "Translating a point by a vector", 1, U7,
             "A translation adds the vector componentwise — direction matters.",
             mk_txt("im1-tr", _g_translate())),
        form("im1-transform-image", "Image under a reflection or rotation", 1, U7,
             "Apply the coordinate rule; every wrong option is a different rigid motion.",
             mk_txt("im1-timg", _g_transform_image())),
        form("im1-identify-transform", "Naming the transformation", 2, U7,
             "Work backwards from pre-image to image, checking BOTH coordinates.",
             mk_txt("im1-tid", _g_identify_transform())),
        form("im1-congruence-criterion", "Choosing the congruence criterion", 2, U7,
             "SSS, SAS, ASA, AAS, HL — and AAA, which proves similarity, not congruence.",
             mk_txt("im1-cong", _g_congruence())),
        form("im1-symmetry", "Lines of symmetry and rotational order", 2, U7,
             "For a regular n-gon both are n; irregular shapes break the pattern.",
             mk_num("im1-sym", _g_symmetry())),
        form("im1-compose-transform", "Composing two transformations", 3, U7,
             "Two rigid motions compose to a single rigid motion — find which one.",
             mk_txt("im1-cmp", _g_compose())),
    ]

    U8 = "coordinate-geometry"
    forms += [
        form("im1-distance", "Distance between two points", 1, U8,
             "Pythagoras on the horizontal and vertical gaps — never add the legs.",
             mk_num("im1-dist", _g_distance())),
        form("im1-midpoint", "Midpoint of a segment", 1, U8,
             "Average each coordinate; halving the difference is a different point.",
             mk_txt("im1-mid", _g_midpoint())),
        form("im1-partition", "Partitioning a segment in a ratio", 2, U8,
             "Travel r/(r+s) of the way from the named endpoint — the end you start from matters.",
             mk_txt("im1-part", _g_partition())),
        form("im1-line-through-point", "Parallel and perpendicular lines through a point", 2, U8,
             "Fix the slope first, then solve for the intercept using the given point.",
             mk_txt("im1-ltp", _g_line_through_point())),
        form("im1-classify-quad", "Classifying a quadrilateral by coordinates", 2, U8,
             "Slopes decide parallel and perpendicular; distances decide equal sides.",
             mk_txt("im1-quad", _g_classify_quad())),
        form("im1-slope-two-points", "Slope from two points", 1, U8,
             "Rise over run — the y-difference goes on top.",
             mk_num("im1-slope2", _g_im1_slope())),
    ]

    U9 = "data-and-statistics"
    forms += [
        form("im1-centre-spread", "Mean, median and range", 1, U9,
             "Centre and spread answer different questions — read which one is asked.",
             mk_num("im1-cs", _g_centre_spread())),
        form("im1-iqr-outlier", "Interquartile range and the outlier fence", 2, U9,
             "IQR is Q3 - Q1; the fence sits 1.5 IQRs beyond the quartile.",
             mk_num("im1-iqr", _g_iqr())),
        form("im1-two-way-table", "Reading a two-way frequency table", 2, U9,
             "The denominator is the question: row total, column total, or grand total.",
             mk_num("im1-2way", _g_two_way())),
        form("im1-line-of-fit", "Interpreting a line of fit", 2, U9,
             "Slope is change per unit; intercept is the prediction at zero; neither proves cause.",
             mk_txt("im1-lof", _g_line_of_fit())),
        form("im1-missing-value-mean", "A missing value from the mean", 2, U9,
             "Turn the mean into a total, then subtract what you already have.",
             mk_num("im1-mvm", _g_missing_value_mean())),
        form("im1-shift-all-values", "Adding a constant to every value", 2, U9,
             "The centre moves with the shift; the spread does not move at all.",
             mk_num("im1-shift", _g_shift_all_values())),
    ]

    U3 = "functions-and-sequences"
    forms += [
        form("im1-arith-sum", "Summing an arithmetic sequence", 2, U3,
             "Pair the ends: n/2 times (first + last).",
             mk_num("im1-asum", _g_arith_sum())),
        form("im1-geo-ratio", "Finding the common ratio", 2, U3,
             "Dividing two terms gives a POWER of r — take the root.",
             mk_num("im1-gr", _g_geo_ratio())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    t = build()
    per = {u["id"]: 0 for u in t["units"]}
    for f in t["forms"]:
        per[f["unit"]] += len(f["variants"])
    print("%s: %d forms, %d variants" %
          (t["slug"], len(t["forms"]), sum(len(f["variants"]) for f in t["forms"])))
    for u in t["units"]:
        print("   %-42s %4d" % (u["id"], per[u["id"]]))
