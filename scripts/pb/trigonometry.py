# -*- coding: utf-8 -*-
"""Problem-bank generator for the Trigonometry topic (ЭЕШ).

Produces ~36 machine-verified variants for each of 8 exam-archetype forms.
Every `check` string sympifies to a Python-bool True.
Run `python3 scripts/pb/trigonometry.py` to self-check.
"""

from sympy import (
    sqrt, Rational, Integer, pi, sin, cos, tan, rad, simplify, sympify, igcd,
)

SLUG = "trigonometry"
TITLE = "Trigonometry"
TITLE_MN = "Тригонометр"
BLURB = ("Exact values, triangles from triples, equations on the circle, and "
         "the laws — trig in every exam costume.")

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def place(correct_kat, distractors, ci):
    """Place the correct KaTeX option at index ci, fill the rest with
    distractor KaTeX strings (already de-duplicated, exactly 3)."""
    assert len(distractors) == 3, distractors
    res = [None, None, None, None]
    ci = ci % 4
    res[ci] = correct_kat
    di = 0
    for i in range(4):
        if res[i] is None:
            res[i] = distractors[di]
            di += 1
    return res, ci


def pick_numeric(correct_val, candidate_pairs, need=3):
    """From (katex, sympy_value) candidates choose `need` whose values are
    numerically distinct from the correct value and from each other."""
    chosen = []
    for kat, val in candidate_pairs:
        if len(chosen) == need:
            break
        if simplify(val - correct_val) == 0:
            continue
        if any(kat == ck for ck, _ in chosen):
            continue
        if any(simplify(val - cv) == 0 for _, cv in chosen):
            continue
        chosen.append((kat, val))
    assert len(chosen) == need, (correct_val, chosen)
    return [k for k, _ in chosen]


def pick_str(correct, candidates, fallback, need=3):
    """Choose `need` distinct string distractors (string distinctness)."""
    chosen = []
    for d in candidates + fallback:
        if len(chosen) == need:
            break
        if d == correct or d in chosen:
            continue
        chosen.append(d)
    assert len(chosen) == need, (correct, chosen)
    return chosen


# ---------------------------------------------------------------------------
# Form 1 : exact-values
# ---------------------------------------------------------------------------

# (sympy value, KaTeX, sympify-string) for every special exact value.
VALS = [
    (Integer(0), "$0$", "0"),
    (Rational(1, 2), "$\\frac{1}{2}$", "1/2"),
    (-Rational(1, 2), "$- \\frac{1}{2}$", "-1/2"),
    (sqrt(2) / 2, "$\\frac{\\sqrt{2}}{2}$", "sqrt(2)/2"),
    (-sqrt(2) / 2, "$- \\frac{\\sqrt{2}}{2}$", "-sqrt(2)/2"),
    (sqrt(3) / 2, "$\\frac{\\sqrt{3}}{2}$", "sqrt(3)/2"),
    (-sqrt(3) / 2, "$- \\frac{\\sqrt{3}}{2}$", "-sqrt(3)/2"),
    (Integer(1), "$1$", "1"),
    (-Integer(1), "$-1$", "-1"),
    (sqrt(3), "$\\sqrt{3}$", "sqrt(3)"),
    (-sqrt(3), "$- \\sqrt{3}$", "-sqrt(3)"),
    (sqrt(3) / 3, "$\\frac{\\sqrt{3}}{3}$", "sqrt(3)/3"),
    (-sqrt(3) / 3, "$- \\frac{\\sqrt{3}}{3}$", "-sqrt(3)/3"),
]


def val_kat(v):
    for vv, kat, _ in VALS:
        if simplify(v - vv) == 0:
            return kat
    return None


def val_sstr(v):
    for vv, _, s in VALS:
        if simplify(v - vv) == 0:
            return s
    return None


FUNMAP = {"sin": sin, "cos": cos, "tan": tan}
FUNNAME = {"sin": "\\sin", "cos": "\\cos", "tan": "\\tan"}


def quadrant_note(angle):
    if 0 < angle < 90:
        return "quadrant I (all positive)"
    if 90 < angle < 180:
        return "quadrant II (only sine positive)"
    if 180 < angle < 270:
        return "quadrant III (only tangent positive)"
    if 270 < angle < 360:
        return "quadrant IV (only cosine positive)"
    return "an axis boundary"


def build_exact_values():
    variants = []
    order = [120, 135, 150, 210, 225, 240, 300, 315, 330,
             0, 90, 180, 270, 30, 45, 60]
    items = []
    for angle in order:
        for f in ("sin", "cos", "tan"):
            if f == "tan" and angle in (90, 270):
                continue
            items.append((f, angle))
    items = items[:36]
    for i, (f, angle) in enumerate(items):
        fn = FUNMAP[f]
        val = simplify(fn(rad(angle)))
        correct_kat = val_kat(val)
        sstr = val_sstr(val)
        # smart distractors: the OTHER co-function value + sign flips
        prefer = []
        if f == "sin":
            other = simplify(cos(rad(angle)))
        elif f == "cos":
            other = simplify(sin(rad(angle)))
        else:
            other = simplify(-val)  # placeholder for tan
        prefer_vals = [(-val), other, (-other)]
        cand = []
        for pv in prefer_vals:
            k = val_kat(pv)
            if k is not None:
                cand.append((k, pv))
        for vv, kat, _ in VALS:      # fill from full pool
            cand.append((kat, vv))
        distractors = pick_numeric(val, cand)
        opts, ci = place(correct_kat, distractors, i)
        expl = (f"${angle}°$ lies in {quadrant_note(angle)}; use the reference "
                f"angle and the ASTC sign rule to get ${FUNNAME[f]} {angle}° = "
                f"{correct_kat.strip('$')}$.")
        variants.append({
            "id": f"TRIG-ev-v{i+1:02d}",
            "statement": f"Evaluate exactly: ${FUNNAME[f]} {angle}°$.",
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"{f}(rad({angle})) == {sstr}"],
        })
    return variants


# ---------------------------------------------------------------------------
# Form 2 : deg-rad
# ---------------------------------------------------------------------------

def pi_kat(r):
    """KaTeX for a positive rational multiple r of pi."""
    p, q = r.p, r.q
    if q == 1:
        if p == 1:
            return "$\\pi$"
        return f"${p}\\pi$"
    if p == 1:
        return f"$\\dfrac{{\\pi}}{{{q}}}$"
    return f"$\\dfrac{{{p}\\pi}}{{{q}}}$"


def build_deg_rad():
    degs = [12, 15, 18, 20, 24, 30, 36, 40, 45, 50, 54, 60, 72, 75, 80, 90,
            100, 105, 108, 120, 135, 144, 150, 160, 180, 210, 216, 225, 240,
            252, 270, 288, 300, 315, 330, 360]
    degs = degs[:36]
    variants = []
    for i, d in enumerate(degs):
        r = Rational(d, 180)
        correct_kat = pi_kat(r)
        # plausible wrong reductions / scalings
        cand_r = [2 * r, r / 2, r * Rational(3, 2), r * Rational(2, 3),
                  r * Rational(3, 4), r * Rational(4, 3), r + Rational(1, 6),
                  r * Rational(5, 6), r * Rational(6, 5)]
        cand = []
        for cr in cand_r:
            if cr <= 0:
                continue
            cand.append((pi_kat(cr), cr))
        distractors = pick_numeric(r, cand)
        opts, ci = place(correct_kat, distractors, i)
        variants.append({
            "id": f"TRIG-dr-v{i+1:02d}",
            "statement": f"Convert ${d}°$ to radians.",
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"Multiply by $\\frac{{\\pi}}{{180}}$: "
                            f"${d}° = \\frac{{{d}\\pi}}{{180}} = "
                            f"{correct_kat.strip('$')}$."),
            "check": [f"Rational({d}, 180) == Rational({r.p}, {r.q})"],
        })
    return variants


# ---------------------------------------------------------------------------
# Form 3 : right-triangle-side
# ---------------------------------------------------------------------------

def surd_kat(v):
    v = simplify(v)
    if v.is_rational:
        if v.is_integer:
            return f"${int(v)}$"
        return f"$\\frac{{{v.p}}}{{{v.q}}}$"
    for n in (2, 3, 5, 6, 7):
        c = simplify(v / sqrt(n))
        if c.is_rational:
            if c == 1:
                return f"$\\sqrt{{{n}}}$"
            if c.is_integer:
                return f"${int(c)} \\sqrt{{{n}}}$"
            return f"$\\frac{{{c.p}}}{{{c.q}}} \\sqrt{{{n}}}$"
    return f"${v}$"


def build_right_triangle_side():
    variants = []
    combos = []
    for h in (4, 6, 8, 10, 12, 20):
        for angle in (30, 45, 60):
            for which in ("opposite", "adjacent"):
                combos.append((h, angle, which))
    combos = combos[:36]
    for i, (h, angle, which) in enumerate(combos):
        if which == "opposite":
            trig = "sin"
            correct = simplify(h * sin(rad(angle)))
            other = simplify(h * cos(rad(angle)))
        else:
            trig = "cos"
            correct = simplify(h * cos(rad(angle)))
            other = simplify(h * sin(rad(angle)))
        correct_kat = surd_kat(correct)
        cand_vals = [other, Integer(h), 2 * correct, 2 * other,
                     Rational(h, 2), 3 * correct, 3 * other]
        cand = [(surd_kat(cv), cv) for cv in cand_vals]
        distractors = pick_numeric(correct, cand)
        opts, ci = place(correct_kat, distractors, i)
        ratio = "sine" if which == "opposite" else "cosine"
        variants.append({
            "id": f"TRIG-rt-v{i+1:02d}",
            "statement": (f"A right triangle has hypotenuse ${h}$ and an acute "
                          f"angle of ${angle}°$. Find the side {which.upper()} "
                          f"the ${angle}°$ angle."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"The {which} side over the hypotenuse is the "
                            f"{ratio}: side $= {h}\\{trig} {angle}° = "
                            f"{correct_kat.strip('$')}$."),
            "check": [f"{h}*{trig}(rad({angle})) == {correct}"],
        })
    return variants


# ---------------------------------------------------------------------------
# Pythagorean triples used by several forms  (a < b < c, primitive)
# ---------------------------------------------------------------------------

TRIPLES = [
    (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
    (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (13, 84, 85),
    (33, 56, 65), (16, 63, 65), (48, 55, 73), (36, 77, 85), (39, 80, 89),
    (65, 72, 97), (20, 99, 101), (60, 91, 109),
]


def frac(p, q):
    return f"$\\frac{{{p}}}{{{q}}}$"


# ---------------------------------------------------------------------------
# Form 4 : sin-to-cos-tan
# ---------------------------------------------------------------------------

def build_sin_to_cos_tan():
    variants = []
    types = [("sin", "cos"), ("sin", "tan"), ("cos", "sin"), ("cos", "tan")]
    combos = []
    seen = set()
    ti = 0
    idx = 0
    # cycle types across triples for numeric variety
    for rep in range(4):
        for t in TRIPLES:
            g, f = types[idx % 4]
            idx += 1
            key = (t, g, f)
            if key in seen:
                continue
            seen.add(key)
            combos.append(key)
            if len(combos) == 36:
                break
        if len(combos) == 36:
            break
    for i, ((a, b, c), g, f) in enumerate(combos):
        given_val = frac(a, c) if g == "sin" else frac(b, c)
        if f == "cos":
            correct, cval = frac(b, c), Rational(b, c)
            cand = [(frac(a, c), Rational(a, c)), (frac(a, b), Rational(a, b)),
                    (frac(b, a), Rational(b, a))]
        elif f == "sin":
            correct, cval = frac(a, c), Rational(a, c)
            cand = [(frac(b, c), Rational(b, c)), (frac(a, b), Rational(a, b)),
                    (frac(b, a), Rational(b, a))]
        else:  # tan
            correct, cval = frac(a, b), Rational(a, b)
            cand = [(frac(b, a), Rational(b, a)), (frac(a, c), Rational(a, c)),
                    (frac(b, c), Rational(b, c))]
        distractors = pick_numeric(cval, cand)
        opts, ci = place(correct, distractors, i)
        variants.append({
            "id": f"TRIG-sc-v{i+1:02d}",
            "statement": (f"An acute angle $\\alpha$ has $\\{g}\\alpha = "
                          f"\\dfrac{{{a if g=='sin' else b}}}{{{c}}}$. "
                          f"Find $\\{f}\\alpha$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"Use the ${a}\\text{{-}}{b}\\text{{-}}{c}$ right "
                            f"triangle (legs ${a}$, ${b}$, hypotenuse ${c}$); "
                            f"read off $\\{f}\\alpha = {correct.strip('$')}$."),
            "check": [f"{a}**2 + {b}**2 == {c}**2",
                      f"Rational({a},{c})**2 + Rational({b},{c})**2 == 1"],
        })
    return variants


# ---------------------------------------------------------------------------
# Form 5 : solve-sin  (sin & cos, one turn)
# ---------------------------------------------------------------------------

SOLVE = [
    ("sin", "\\frac{1}{2}", "1/2", [30, 150]),
    ("sin", "\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", [60, 120]),
    ("sin", "\\frac{\\sqrt{2}}{2}", "sqrt(2)/2", [45, 135]),
    ("sin", "-\\frac{1}{2}", "-1/2", [210, 330]),
    ("sin", "-\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2", [240, 300]),
    ("sin", "-\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2", [225, 315]),
    ("sin", "0", "0", [0, 180]),
    ("sin", "1", "1", [90]),
    ("sin", "-1", "-1", [270]),
    ("cos", "\\frac{1}{2}", "1/2", [60, 300]),
    ("cos", "\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", [30, 330]),
    ("cos", "\\frac{\\sqrt{2}}{2}", "sqrt(2)/2", [45, 315]),
    ("cos", "-\\frac{1}{2}", "-1/2", [120, 240]),
    ("cos", "-\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2", [150, 210]),
    ("cos", "-\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2", [135, 225]),
    ("cos", "0", "0", [90, 270]),
    ("cos", "1", "1", [0]),
    ("cos", "-1", "-1", [180]),
]

SUM_FALLBACK = ["$45°$", "$90°$", "$120°$", "$180°$", "$210°$", "$270°$",
                "$300°$", "$360°$", "$450°$", "$540°$", "$720°$", "$0°$"]
CS_FALLBACK = ["$0 \\text{ solutions, sum } 0°$",
               "$3 \\text{ solutions, sum } 180°$",
               "$4 \\text{ solutions, sum } 360°$",
               "$2 \\text{ solutions, sum } 90°$",
               "$1 \\text{ solution, sum } 360°$"]


def build_solve_sin():
    variants = []
    vi = 0
    # Style A: count + sum
    for j, (f, kkat, kstr, sols) in enumerate(SOLVE):
        n = len(sols)
        S = sum(sols)
        if n == 2:
            correct = f"$2 \\text{{ solutions, sum }} {S}°$"
            cands = [f"$1 \\text{{ solution, sum }} {sols[0]}°$",
                     f"$2 \\text{{ solutions, sum }} {2*S}°$",
                     f"$4 \\text{{ solutions, sum }} {S}°$"]
        else:
            correct = f"$1 \\text{{ solution, sum }} {S}°$"
            cands = [f"$2 \\text{{ solutions, sum }} {2*S if S else 360}°$",
                     f"$2 \\text{{ solutions, sum }} 180°$",
                     f"$0 \\text{{ solutions, sum }} 0°$"]
        distractors = pick_str(correct, cands, CS_FALLBACK)
        opts, ci = place(correct, distractors, vi)
        checks = [f"{f}(rad({s})) == {kstr}" for s in sols]
        checks.append(f"{' + '.join(str(s) for s in sols)} == {S}")
        variants.append({
            "id": f"TRIG-ss-v{vi+1:02d}",
            "statement": (f"How many solutions does $\\{f} x = {kkat}$ have on "
                          f"$[0°; 360°)$ — and what is their SUM?"),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"On one turn the solutions are "
                            f"${', '.join(str(s)+'°' for s in sols)}$, so there "
                            f"{'are '+str(n)+' of them' if n>1 else 'is 1'} with "
                            f"sum ${S}°$."),
            "check": checks,
        })
        vi += 1
    # Style B: sum only
    for j, (f, kkat, kstr, sols) in enumerate(SOLVE):
        n = len(sols)
        S = sum(sols)
        correct = f"${S}°$"
        if n == 2:
            cands = [f"${sols[0]}°$", f"${2*S}°$",
                     f"${(360 if S != 360 else 180)}°$"]
        else:
            cands = [f"${(2*S if S else 90)}°$", f"$180°$", f"$360°$"]
        distractors = pick_str(correct, cands, SUM_FALLBACK)
        opts, ci = place(correct, distractors, vi)
        checks = [f"{f}(rad({s})) == {kstr}" for s in sols]
        checks.append(f"{' + '.join(str(s) for s in sols)} == {S}")
        variants.append({
            "id": f"TRIG-ss-v{vi+1:02d}",
            "statement": (f"Find the SUM of all solutions of $\\{f} x = {kkat}$ "
                          f"on $[0°; 360°)$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"The solutions are "
                            f"${', '.join(str(s)+'°' for s in sols)}$; their sum "
                            f"is ${S}°$."),
            "check": checks,
        })
        vi += 1
    return variants


# ---------------------------------------------------------------------------
# Form 6 : pythagorean-identity
# ---------------------------------------------------------------------------

def build_pythagorean_identity():
    variants = []
    combos = []
    for t in TRIPLES:
        combos.append((t, "cos"))
        combos.append((t, "sin"))
    combos = combos[:36]
    for i, ((a, b, c), given) in enumerate(combos):
        if given == "cos":
            # cos = b/c ; 1 - cos^2 = a^2/c^2
            gnum, gden = b, c
            ans_num, ans_den = a * a, c * c
            cos2_num = b * b            # forgot to subtract -> reports cos^2
            unsq_num, unsq_den = a, c   # took sin, not squared
        else:
            # sin = a/c ; 1 - sin^2 = b^2/c^2
            gnum, gden = a, c
            ans_num, ans_den = b * b, c * c
            cos2_num = a * a
            unsq_num, unsq_den = b, c
        correct_val = Rational(ans_num, ans_den)
        correct_kat = f"$\\frac{{{ans_num}}}{{{ans_den}}}$"
        cand = [
            (f"$\\frac{{{cos2_num}}}{{{c*c}}}$", Rational(cos2_num, c * c)),
            (f"$\\frac{{{unsq_num}}}{{{unsq_den}}}$", Rational(unsq_num, unsq_den)),
            ("$1$", Integer(1)),
        ]
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        variants.append({
            "id": f"TRIG-id-v{i+1:02d}",
            "statement": (f"If $\\{given}\\alpha = \\dfrac{{{gnum}}}{{{gden}}}$, "
                          f"evaluate $1 - \\{given}^2\\alpha$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"By the Pythagorean identity $1 - \\{given}^2\\alpha "
                            f"= \\{'sin' if given=='cos' else 'cos'}^2\\alpha "
                            f"= \\frac{{{ans_num}}}{{{ans_den}}}$."),
            "check": [f"1 - Rational({gnum},{gden})**2 == "
                      f"Rational({ans_num},{ans_den})"],
        })
    return variants


# ---------------------------------------------------------------------------
# Form 7 : double-angle
# ---------------------------------------------------------------------------

def build_double_angle():
    variants = []
    combos = []
    for t in TRIPLES:
        combos.append((t, "sin2"))
        combos.append((t, "cos2"))
    combos = combos[:36]
    for i, ((a, b, c), which) in enumerate(combos):
        if which == "sin2":
            num = 2 * a * b
            den = c * c
            correct_val = Rational(num, den)
            correct_kat = f"$\\frac{{{num}}}{{{den}}}$"
            cand = [
                (f"$\\frac{{{a*b}}}{{{c*c}}}$", Rational(a * b, c * c)),   # forgot 2
                (f"$\\frac{{{2*a}}}{{{c}}}$", Rational(2 * a, c)),        # 2 sin only
                (f"$\\frac{{{b*b-a*a}}}{{{c*c}}}$", Rational(b*b-a*a, c*c)),  # cos2a
            ]
            expl = (f"$\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = "
                    f"2\\cdot\\frac{{{a}}}{{{c}}}\\cdot\\frac{{{b}}}{{{c}}} = "
                    f"\\frac{{{num}}}{{{den}}}$.")
            check = [f"2*Rational({a},{c})*Rational({b},{c}) == "
                     f"Rational({num},{den})"]
        else:
            num = b * b - a * a
            den = c * c
            correct_val = Rational(num, den)
            correct_kat = f"$\\frac{{{num}}}{{{den}}}$"
            cand = [
                (f"$\\frac{{{a*a-b*b}}}{{{c*c}}}$", Rational(a*a-b*b, c*c)),  # sign flip
                (f"$\\frac{{{2*a*b}}}{{{c*c}}}$", Rational(2*a*b, c*c)),      # sin2a
                ("$1$", Integer(1)),                                          # b^2+a^2
            ]
            expl = (f"$\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha = "
                    f"\\frac{{{b*b}}}{{{c*c}}} - \\frac{{{a*a}}}{{{c*c}}} = "
                    f"\\frac{{{num}}}{{{den}}}$.")
            check = [f"Rational({b},{c})**2 - Rational({a},{c})**2 == "
                     f"Rational({num},{den})"]
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        ask = "\\sin 2\\alpha" if which == "sin2" else "\\cos 2\\alpha"
        variants.append({
            "id": f"TRIG-da-v{i+1:02d}",
            "statement": (f"An acute angle has $\\sin\\alpha = "
                          f"\\dfrac{{{a}}}{{{c}}}$ and $\\cos\\alpha = "
                          f"\\dfrac{{{b}}}{{{c}}}$. Find ${ask}$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": check,
        })
    return variants


# ---------------------------------------------------------------------------
# Form 8 : law-of-cosines
# ---------------------------------------------------------------------------

def isqrt_exact(n):
    r = int(round(n ** 0.5))
    for cand in (r - 1, r, r + 1):
        if cand >= 0 and cand * cand == n:
            return cand
    return None


def root_repr(n):
    """Return (katex, sympy_value, sstr) for sqrt(n)."""
    s = isqrt_exact(n)
    if s is not None:
        return f"${s}$", Integer(s), str(s)
    return f"$\\sqrt{{{n}}}$", sqrt(n), f"sqrt({n})"


def build_law_of_cosines():
    variants = []
    combos = []
    q = 3
    while len(combos) < 36:
        for p in range(2, q):
            for angle in (60, 120):
                combos.append((p, q, angle))
                if len(combos) == 36:
                    break
            if len(combos) == 36:
                break
        q += 1
    for i, (p, qq, angle) in enumerate(combos):
        cross = -p * qq if angle == 60 else p * qq
        N = p * p + qq * qq + cross           # correct third-side squared
        Nwrong = p * p + qq * qq - cross      # wrong sign on the cross term
        Nnocross = p * p + qq * qq            # forgot the 2ab cos term
        correct_kat, correct_val, correct_sstr = root_repr(N)
        cand = [root_repr(Nwrong)[:2], root_repr(Nnocross)[:2],
                (f"${p+qq}$", Integer(p + qq))]
        cand = [(k, v) for (k, v) in cand]
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        sign = "-" if angle == 60 else "+"
        cosval = "\\tfrac{1}{2}" if angle == 60 else "-\\tfrac{1}{2}"
        variants.append({
            "id": f"TRIG-lc-v{i+1:02d}",
            "statement": (f"A triangle has sides ${p}$ and ${qq}$ with a "
                          f"${angle}°$ angle between them. Find the third side."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"Law of cosines: $c^2 = {p}^2 + {qq}^2 - "
                            f"2\\cdot{p}\\cdot{qq}\\cos {angle}° = {p*p}+{qq*qq}"
                            f"{sign}{p*qq} = {N}$, so $c = {correct_kat.strip('$')}$."),
            "check": [f"sqrt({p}**2 + {qq}**2 - 2*{p}*{qq}*cos(rad({angle}))) "
                      f"== {correct_sstr}"],
        })
    return variants


# ---------------------------------------------------------------------------
# Assemble
# ---------------------------------------------------------------------------

def build():
    return {
        "slug": SLUG,
        "title": TITLE,
        "titleMn": TITLE_MN,
        "blurb": BLURB,
        "forms": [
            {"id": "exact-values", "title": "Exact values beyond 90°",
             "level": 1, "skill": "Reference angle + quadrant sign (ASTC).",
             "variants": build_exact_values()},
            {"id": "deg-rad", "title": "Degrees ↔ radians", "level": 1,
             "skill": "Multiply degrees by π/180; reduce the fraction.",
             "variants": build_deg_rad()},
            {"id": "right-triangle-side", "title": "Finding a side with sine",
             "level": 1, "skill": "SOH: opposite = hypotenuse × sin(angle).",
             "variants": build_right_triangle_side()},
            {"id": "sin-to-cos-tan", "title": "From sin to cos and tan",
             "level": 2,
             "skill": "Build the triangle from the triple; read the other ratios.",
             "variants": build_sin_to_cos_tan()},
            {"id": "solve-sin", "title": "Solving sin x = k on one turn",
             "level": 2,
             "skill": "Two mirror solutions per turn; supplementary for positive k.",
             "variants": build_solve_sin()},
            {"id": "pythagorean-identity", "title": "The Pythagorean identity",
             "level": 2, "skill": "sin² + cos² = 1, so 1 − cos² is sin².",
             "variants": build_pythagorean_identity()},
            {"id": "double-angle", "title": "The double-angle formula",
             "level": 3, "skill": "sin 2α = 2 sin α cos α — never just double.",
             "variants": build_double_angle()},
            {"id": "law-of-cosines", "title": "The law of cosines", "level": 3,
             "skill": "c² = a² + b² − 2ab·cos C; 60° and 120° keep it exact.",
             "variants": build_law_of_cosines()},
        ],
    }


# ---------------------------------------------------------------------------
# Self-check
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    data = build()
    expected_ids = ["exact-values", "deg-rad", "right-triangle-side",
                    "sin-to-cos-tan", "solve-sin", "pythagorean-identity",
                    "double-angle", "law-of-cosines"]
    forms = data["forms"]
    assert len(forms) == 8, f"expected 8 forms, got {len(forms)}"
    assert [f["id"] for f in forms] == expected_ids, [f["id"] for f in forms]

    all_ids = []
    total = 0
    min_per_form = 10 ** 9
    for form in forms:
        vs = form["variants"]
        assert len(vs) >= 32, f"{form['id']} has only {len(vs)} variants"
        min_per_form = min(min_per_form, len(vs))
        total += len(vs)
        for v in vs:
            all_ids.append(v["id"])
            opts = v["options"]
            assert len(opts) == 4, f"{v['id']} options != 4"
            assert len(set(opts)) == 4, f"{v['id']} options not distinct: {opts}"
            assert 0 <= v["correctIndex"] <= 3, v["id"]
            # every check string must be boolean True
            for cs in v["check"]:
                res = sympify(cs)
                assert bool(res) is True, f"{v['id']} check failed: {cs} -> {res}"
            # numeric distinctness of correct vs each distractor
            correct = opts[v["correctIndex"]]
            try:
                cval = sympify(correct)
                cnum = cval.is_number
            except Exception:
                cnum = False
            for k, o in enumerate(opts):
                if k == v["correctIndex"]:
                    continue
                if cnum:
                    try:
                        oval = sympify(o)
                        if oval.is_number:
                            assert simplify(cval - oval) != 0, \
                                f"{v['id']} distractor equals correct: {o}"
                    except AssertionError:
                        raise
                    except Exception:
                        assert o != correct
                else:
                    assert o != correct
    assert len(all_ids) == len(set(all_ids)), "duplicate variant ids"

    print(f"SELFCHECK OK  forms=8  total={total}  min_per_form={min_per_form}")
