# -*- coding: utf-8 -*-
"""Problem-bank subject: Trigonometry — mirrors the /math/trigonometry course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/trigonometry_course.py` for the self-check.
"""
import importlib.util
import math
import os
import re

from sympy import Integer, Rational, cos, pi, rad, simplify, sin, sqrt

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "trigonometry"
TITLE = "Trigonometry"
TITLE_MN = "Тригонометр"
BLURB = ("Unit-by-unit practice for the Trigonometry course — right triangles to identities and the laws.")

UNITS = [
    {"id": "right-triangle-trigonometry", "title": "Right-Triangle Trigonometry",
     "blurb": "SOH-CAH-TOA: name the sides, pick the ratio, solve for any missing side or angle — then aim it at towers, ramps, and shadows."},
    {"id": "special-triangles-and-exact-values", "title": "Special Triangles & Exact Values",
     "blurb": "Half a square and half an equilateral: the two triangles behind every exact value of 30°, 45°, and 60°."},
    {"id": "radians-and-the-unit-circle", "title": "Radians & the Unit Circle",
     "blurb": "Angles measured by arc, a circle where cosine and sine ARE the coordinates — and exact values in every quadrant."},
    {"id": "graphs-of-trig-functions", "title": "Graphs of Trig Functions",
     "blurb": "The circle unrolled into a wave: amplitude, period, phase, midline — and tangent's wilder portrait."},
    {"id": "identities-and-equations", "title": "Identities & Equations",
     "blurb": "The Pythagorean identity, sum and double-angle formulas — and solving equations whose unknown is an angle."},
    {"id": "laws-of-sines-and-cosines", "title": "Laws of Sines & Cosines",
     "blurb": "Trigonometry for EVERY triangle: the sine area formula, both laws, and the strategy for solving any triangle from any three facts."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "right-triangle-side": "right-triangle-trigonometry",
    "sin-to-cos-tan": "right-triangle-trigonometry",
    "exact-values": "special-triangles-and-exact-values",
    "deg-rad": "radians-and-the-unit-circle",
    "solve-sin": "identities-and-equations",
    "pythagorean-identity": "identities-and-equations",
    "double-angle": "identities-and-equations",
    "law-of-cosines": "laws-of-sines-and-cosines",
}

SOURCES = ['trigonometry']

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
# Shared helpers (house style — copied from scripts/pb/trigonometry.py)
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


# ---------------------------------------------------------------------------
# Form A : arc-length  (unit: radians-and-the-unit-circle)
# ---------------------------------------------------------------------------

# (radius, p, q): central angle p*pi/q with q | r*p  ->  arc = k*pi, k integer
ARC_RAD = [
    (6, 1, 3), (4, 1, 2), (9, 2, 3), (8, 3, 4), (10, 1, 5), (12, 5, 6),
    (6, 2, 3), (8, 1, 4), (10, 2, 5), (12, 1, 6), (15, 1, 3), (14, 1, 2),
    (9, 4, 3), (20, 3, 4), (12, 7, 6), (18, 5, 6), (5, 2, 5), (16, 3, 8),
    (21, 2, 3), (25, 3, 5), (24, 1, 8), (10, 3, 2), (7, 2, 7), (18, 1, 9),
]
# (radius, degrees) with 180 | r*d  ->  arc = k*pi, k integer
ARC_DEG = [
    (6, 60), (9, 80), (12, 30), (10, 90), (18, 40), (12, 120),
    (15, 60), (8, 45), (20, 90), (9, 120), (24, 30), (36, 45),
]


def build_arc_length():
    variants = []
    combos = []
    ri = di = 0
    for i in range(36):
        if i % 3 == 2 and di < len(ARC_DEG):
            combos.append(("deg", ARC_DEG[di]))
            di += 1
        else:
            combos.append(("rad", ARC_RAD[ri]))
            ri += 1
    for i, (kind, data) in enumerate(combos):
        if kind == "rad":
            r, p, q = data
            k = Rational(r * p, q)
            assert k.is_integer, (r, p, q)
            ang = pi_kat(Rational(p, q))
            stmt = (f"A circle has radius ${r}$. Find the length of an arc "
                    f"subtending a central angle of {ang} (radians).")
            cand_c = [Rational(2 * r), Rational(k, 2)]
            inv = Rational(r * q, p)
            if inv <= 60:
                cand_c.append(inv)
            cand_c += [2 * k, Rational(r), k + 2]
            cand = [(pi_kat(c), c * pi) for c in cand_c if c > 0]
            check = [f"{r}*Rational({p},{q})*pi == {int(k)}*pi"]
            expl = (f"Arc length is $s = r\\theta$ with $\\theta$ in radians: "
                    f"$s = {r} \\cdot {ang.strip('$')} = "
                    f"{pi_kat(k).strip('$')}$. Answering "
                    f"${2 * r}\\pi$ — the FULL circumference $2\\pi r$ — is "
                    f"the classic slip.")
        else:
            r, d = data
            k = Rational(r * d, 180)
            assert k.is_integer, (r, d)
            stmt = (f"A circle has radius ${r}$. Find the length of an arc "
                    f"subtending a central angle of ${d}°$.")
            cand = [(pi_kat(Rational(2 * r)), 2 * r * pi),
                    (pi_kat(Rational(k, 2)), Rational(k, 2) * pi),
                    (surd_kat(Integer(k)), Integer(k)),
                    (pi_kat(Rational(2 * k)), 2 * k * pi),
                    (pi_kat(Rational(k + 2)), (k + 2) * pi)]
            check = [f"{r}*rad({d}) == {int(k)}*pi"]
            expl = (f"Convert first: ${d}° = "
                    f"{pi_kat(Rational(d, 180)).strip('$')}$ radians, then "
                    f"$s = r\\theta = {pi_kat(k).strip('$')}$. Dropping the "
                    f"$\\pi$ (answering ${int(k)}$) is the classic slip.")
        correct_val = k * pi
        correct_kat = pi_kat(Rational(k))
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        variants.append({
            "id": f"TRIG-arc-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": check,
        })
    return variants


def _resolve_arc_length(s):
    r = int(re.search(r"radius \$(\d+)\$", s).group(1))
    m = re.search(r"central angle of \$(\d+)°\$", s)
    if m:
        return ("num", Rational(r * int(m.group(1)), 180) * pi)
    m = re.search(r"\\dfrac\{(\d*)\\pi\}\{(\d+)\}", s)
    p = int(m.group(1)) if m.group(1) else 1
    q = int(m.group(2))
    return ("num", r * Rational(p, q) * pi)


# ---------------------------------------------------------------------------
# Forms B & C : amplitude-period / max-min-value  (unit: graphs)
# ---------------------------------------------------------------------------

def wave_kat(fn, A, B, C):
    """KaTeX for y = A fn(Bx) + C with B a positive integer or 1/q."""
    if B == 1:
        inner = "x"
    elif Rational(B).q == 1:
        inner = f"{B}x"
    else:
        inner = f"\\frac{{x}}{{{Rational(B).q}}}"
    tail = f" + {C}" if C > 0 else f" - {-C}"
    return f"y = {A}\\{fn}\\left({inner}\\right){tail}"


_WAVE_RE = re.compile(
    r"y = (-?\d+)\\(sin|cos)\\left\((x|\d+x|\\frac\{x\}\{\d+\})\\right\)"
    r" ([+-]) (\d+)")


def _parse_wave(s):
    m = _WAVE_RE.search(s)
    A = int(m.group(1))
    inner = m.group(3)
    if inner == "x":
        B = Rational(1)
    elif "frac" in inner:
        B = Rational(1, int(re.search(r"\{(\d+)\}$", inner).group(1)))
    else:
        B = Rational(int(inner[:-1]))
    C = int(m.group(5))
    if m.group(4) == "-":
        C = -C
    return A, B, C


AMP_A = [3, -2, 5, -4, 2, -3, 4, -5, 7, -6, 6, -7, 8, -8, 9, -9, 10, -10]
AMP_C = [1, -2, 3, -4, 5, -1, 2, -3, 4]
PER_B = [1, 2, 3, 4, 6, Rational(1, 2), Rational(1, 3)]
PER_A = [2, 3, 4, 5, -3]
PER_C = [1, -2, 3, 2, -1, 4]


def build_amplitude_period():
    variants = []
    for i in range(36):
        j = i // 2
        fn = ("sin", "cos")[j % 2]
        if i % 2 == 0:
            # amplitude question
            A = AMP_A[j % len(AMP_A)]
            B = (1, 2, 3, 4)[j % 4]
            C = AMP_C[j % len(AMP_C)]
            correct_val = Integer(abs(A))
            correct_kat = surd_kat(correct_val)
            cand_v = [Integer(A), Integer(C), Integer(abs(A) + C),
                      Integer(2 * abs(A)), Integer(B), Integer(abs(A) + 2),
                      Integer(abs(A) + 1)]
            cand = [(surd_kat(v), v) for v in cand_v]
            stmt = (f"Find the AMPLITUDE of "
                    f"${wave_kat(fn, A, B, C)}$.")
            if A < 0:
                expl = (f"The amplitude is $|A| = |{A}| = {abs(A)}$ — a "
                        f"negative $A$ only reflects the graph. Answering the "
                        f"signed ${A}$ is the classic slip.")
            else:
                expl = (f"The amplitude is $|A| = {abs(A)}$: the distance "
                        f"from the midline to a peak. Mixing in the vertical "
                        f"shift ${C}$ is the classic slip.")
            check = [f"sqrt(({A})**2) == {abs(A)}"]
        else:
            # period question
            B = Rational(PER_B[j % len(PER_B)])
            A = PER_A[j % len(PER_A)]
            C = PER_C[j % len(PER_C)]
            correct_val = 2 * pi / B
            correct_kat = pi_kat(Rational(2) / B)
            cand = [(surd_kat(B), B),
                    (pi_kat(2 * B), 2 * B * pi),
                    (pi_kat(1 / B), pi / B),
                    (pi_kat(Rational(1, 2)), pi / 2),
                    (pi_kat(Rational(4)), 4 * pi),
                    (pi_kat(Rational(1, 4)), pi / 4)]
            stmt = (f"Find the PERIOD of "
                    f"${wave_kat(fn, A, B, C)}$.")
            if B == 1:
                slip = (f"Answering the coefficient $B$ itself "
                        f"({surd_kat(B)}) is the classic slip.")
            else:
                slip = (f"Multiplying instead — "
                        f"${pi_kat(2 * B).strip('$')}$ — is the classic slip.")
            expl = (f"The period of $\\{fn}(Bx)$ is $\\frac{{2\\pi}}{{B}}$; "
                    f"here it is {correct_kat}. {slip}")
            check = [f"2*pi/Rational({B.p},{B.q}) == {2 * pi / B}"]
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        variants.append({
            "id": f"TRIG-amp-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": check,
        })
    return variants


def _resolve_amplitude_period(s):
    A, B, _C = _parse_wave(s)
    if "AMPLITUDE" in s:
        return ("num", Integer(abs(A)))
    assert "PERIOD" in s
    return ("num", 2 * pi / B)


MM_A = [2, -3, 4, -5, 3, -2, 5, -4, 6, -7, 7, -6, 8, -8, 9, -9, 10, -10]
MM_C = [1, -2, 3, 4, -1, 2, 5]


def build_max_min_value():
    variants = []
    for i in range(36):
        which = "MAXIMUM" if i % 2 == 0 else "MINIMUM"
        A = MM_A[i % len(MM_A)]
        B = (1, 2, 3, 4)[i % 4]
        C = MM_C[i % len(MM_C)]
        fn = ("sin", "cos")[(i // 2) % 2]
        if which == "MAXIMUM":
            correct_val = Integer(C + abs(A))
            sign_kat, val = "+", C + abs(A)
        else:
            correct_val = Integer(C - abs(A))
            sign_kat, val = "-", C - abs(A)
        correct_kat = surd_kat(correct_val)
        cand_v = [Integer(C + A), Integer(C - A), Integer(C), Integer(abs(A)),
                  Integer(C + 2 * abs(A)), Integer(C - 2 * abs(A)),
                  Integer(A), Integer(-A)]
        cand = [(surd_kat(v), v) for v in cand_v]
        distractors = pick_numeric(correct_val, cand)
        opts, ci = place(correct_kat, distractors, i)
        stmt = (f"Find the {which} value of "
                f"${wave_kat(fn, A, B, C)}$.")
        other = "minimum" if which == "MAXIMUM" else "maximum"
        if A < 0:
            expl = (f"$\\{fn}$ swings between $-1$ and $1$, so $y$ ranges "
                    f"over ${C} \\pm |{A}|$ and the {which.lower()} is "
                    f"${C} {sign_kat} {abs(A)} = {val}$. Using the signed "
                    f"$A = {A}$ without absolute value gives the "
                    f"{other} instead — the classic slip.")
        else:
            expl = (f"$\\{fn}$ swings between $-1$ and $1$, so $y$ ranges "
                    f"over ${C} \\pm {abs(A)}$ and the {which.lower()} is "
                    f"${C} {sign_kat} {abs(A)} = {val}$. Forgetting the "
                    f"midline shift and answering $|A| = {abs(A)}$ is the "
                    f"classic slip.")
        variants.append({
            "id": f"TRIG-mm-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"({C}) {sign_kat} sqrt(({A})**2) == {val}"],
        })
    return variants


def _resolve_max_min_value(s):
    A, _B, C = _parse_wave(s)
    if "MAXIMUM" in s:
        return ("num", Integer(C + abs(A)))
    assert "MINIMUM" in s
    return ("num", Integer(C - abs(A)))


# ---------------------------------------------------------------------------
# Form D : triangle-area-sine  (unit: laws-of-sines-and-cosines)
# ---------------------------------------------------------------------------

AREA_CS = [30, 45, 60, 90, 120, 135, 150]
AREA_PAIRS = [(4, 5), (8, 3), (4, 7), (8, 5), (6, 10), (12, 5),
              (4, 9), (8, 7), (4, 3), (12, 7), (16, 3), (8, 9)]


def build_triangle_area_sine():
    variants = []
    for i in range(36):
        Cdeg = AREA_CS[i % len(AREA_CS)]
        a, b = AREA_PAIRS[i % len(AREA_PAIRS)]
        assert (a * b) % 4 == 0, (a, b)
        area = simplify(Rational(a * b, 2) * sin(rad(Cdeg)))
        correct_kat = surd_kat(area)
        cand_v = [simplify(Integer(a * b) * sin(rad(Cdeg))),  # forgot the 1/2
                  Rational(a * b, 2),                         # forgot sin C
                  Rational(a * b, 4),
                  simplify(Rational(a * b, 2) * abs(cos(rad(Cdeg)))),  # cosine
                  Integer(a + b),
                  Integer(a * b)]
        cand = [(surd_kat(v), v) for v in cand_v if v != 0]
        distractors = pick_numeric(area, cand)
        opts, ci = place(correct_kat, distractors, i)
        cx = round(a * math.cos(math.radians(Cdeg)), 4)
        cy = round(a * math.sin(math.radians(Cdeg)), 4)
        fig = {
            "points": [
                {"id": "A", "x": 0, "y": 0, "label": ""},
                {"id": "B", "x": b, "y": 0, "label": ""},
                {"id": "C", "x": cx, "y": cy, "label": ""},
            ],
            "objects": [
                {"kind": "segment", "from": "A", "to": "B", "label": str(b)},
                {"kind": "segment", "from": "A", "to": "C", "label": str(a)},
                {"kind": "segment", "from": "B", "to": "C"},
                {"kind": "angle", "at": "A", "from": "B", "to": "C",
                 "label": "%d°" % Cdeg},
            ],
        }
        forgot_half = surd_kat(2 * area).strip('$')
        variants.append({
            "geoFigure": fig,
            "id": f"TRIG-areas-v{i+1:02d}",
            "statement": (f"A triangle has sides ${a}$ and ${b}$ with an "
                          f"included angle of ${Cdeg}°$. Find its area."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"Area $= \\frac{{1}}{{2}}ab\\sin C = "
                            f"\\frac{{1}}{{2}} \\cdot {a} \\cdot {b} \\cdot "
                            f"\\sin {Cdeg}° = {correct_kat.strip('$')}$. "
                            f"Dropping the $\\frac{{1}}{{2}}$ gives "
                            f"${forgot_half}$ — the classic slip."),
            "check": [f"Rational({a * b},2)*sin(rad({Cdeg})) == {area}"],
        })
    return variants


def _resolve_triangle_area_sine(s):
    m = re.search(r"sides \$(\d+)\$ and \$(\d+)\$ with an included angle "
                  r"of \$(\d+)°\$", s)
    a, b, C = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", Rational(a * b, 2) * sin(rad(C)))


# ---------------------------------------------------------------------------
# Form E : law-of-sines  (unit: laws-of-sines-and-cosines)
# ---------------------------------------------------------------------------

# Curated (angle A, angle B) pairs whose sinB/sinA ratio stays exact and clean.
LOS_PAIRS = [(30, 90), (45, 90), (30, 45), (45, 30), (30, 60),
             (90, 45), (90, 30), (90, 60), (30, 120), (135, 30)]
# pairs whose answers need an even k to keep integer surd coefficients
LOS_EVEN = {(45, 30), (90, 45), (90, 30), (90, 60), (135, 30)}
K_EVEN = [4, 6, 8, 10, 12]
K_ANY = [3, 5, 4, 7, 6]


def _los_apex(Adeg, Bdeg):
    """Apex C of a triangle drawn true with A at (0,0), B at (6,0)."""
    if Adeg == 90:
        return 0.0, round(6 * math.tan(math.radians(Bdeg)), 4)
    if Bdeg == 90:
        return 6.0, round(6 * math.tan(math.radians(Adeg)), 4)
    tA = math.tan(math.radians(Adeg))
    tB = math.tan(math.radians(Bdeg))
    x = 6 * tB / (tA + tB)
    return round(x, 4), round(tA * x, 4)


def build_law_of_sines():
    variants = []
    seen = {}
    for i in range(36):
        Adeg, Bdeg = LOS_PAIRS[i % len(LOS_PAIRS)]
        n = seen.get((Adeg, Bdeg), 0)
        seen[(Adeg, Bdeg)] = n + 1
        k = (K_EVEN if (Adeg, Bdeg) in LOS_EVEN else K_ANY)[n]
        bval = simplify(k * sin(rad(Bdeg)) / sin(rad(Adeg)))
        correct_kat = surd_kat(bval)
        cand_v = [simplify(k * sin(rad(Adeg)) / sin(rad(Bdeg))),  # inverted
                  simplify(k * sin(rad(Bdeg))),                   # no divide
                  Integer(2 * k), Integer(k), Rational(k, 2),
                  simplify(2 * bval),
                  simplify(k * sqrt(2) / 2), simplify(k * sqrt(3) / 2),
                  Integer(3 * k)]
        cand = [(surd_kat(v), v) for v in cand_v]
        distractors = pick_numeric(bval, cand)
        opts, ci = place(correct_kat, distractors, i)
        cx, cy = _los_apex(Adeg, Bdeg)
        fig = {
            "points": [
                {"id": "A", "x": 0, "y": 0, "label": "A"},
                {"id": "B", "x": 6, "y": 0, "label": "B"},
                {"id": "C", "x": cx, "y": cy, "label": "C"},
            ],
            "objects": [
                {"kind": "segment", "from": "A", "to": "B"},
                {"kind": "segment", "from": "B", "to": "C", "label": "a"},
                {"kind": "segment", "from": "A", "to": "C", "label": "?",
                 "color": "accent"},
                {"kind": "angle", "at": "A", "from": "B", "to": "C",
                 "label": "%d°" % Adeg},
                {"kind": "angle", "at": "B", "from": "A", "to": "C",
                 "label": "%d°" % Bdeg},
            ],
        }
        inv_kat = surd_kat(cand_v[0]).strip('$')
        variants.append({
            "geoFigure": fig,
            "id": f"TRIG-los-v{i+1:02d}",
            "statement": (f"In triangle $ABC$, $\\angle A = {Adeg}°$, "
                          f"$\\angle B = {Bdeg}°$, and side $a = {k}$ "
                          f"(opposite $\\angle A$). Find side $b$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": (f"Law of sines: $\\frac{{b}}{{\\sin B}} = "
                            f"\\frac{{a}}{{\\sin A}}$, so $b = \\frac{{{k}"
                            f"\\sin {Bdeg}°}}{{\\sin {Adeg}°}} = "
                            f"{correct_kat.strip('$')}$. Inverting the ratio "
                            f"(giving ${inv_kat}$) is the classic slip."),
            "check": [f"{k}*sin(rad({Bdeg}))/sin(rad({Adeg})) == {bval}"],
        })
    return variants


def _resolve_law_of_sines(s):
    m = re.search(r"\\angle A = (\d+)°\$, \$\\angle B = (\d+)°\$, and side "
                  r"\$a = (\d+)\$", s)
    A, B, k = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("num", k * sin(rad(B)) / sin(rad(A)))


RESOLVERS["arc-length"] = _resolve_arc_length
RESOLVERS["amplitude-period"] = _resolve_amplitude_period
RESOLVERS["max-min-value"] = _resolve_max_min_value
RESOLVERS["triangle-area-sine"] = _resolve_triangle_area_sine
RESOLVERS["law-of-sines"] = _resolve_law_of_sines


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    return [
        {"id": "arc-length", "title": "Arc length from radius and angle",
         "level": 2, "skill": "s = rθ in radians; convert degrees by π/180 first.",
         "unit": "radians-and-the-unit-circle",
         "variants": build_arc_length()},
        {"id": "amplitude-period", "title": "Amplitude and period from the equation",
         "level": 1, "skill": "Amplitude = |A|; period = 2π/B — divide, never multiply.",
         "unit": "graphs-of-trig-functions",
         "variants": build_amplitude_period()},
        {"id": "max-min-value", "title": "Maximum and minimum of a sinusoid",
         "level": 2, "skill": "Max = C + |A|, min = C − |A| — the midline shifted by the amplitude.",
         "unit": "graphs-of-trig-functions",
         "variants": build_max_min_value()},
        {"id": "triangle-area-sine", "title": "Triangle area with the sine formula",
         "level": 2, "skill": "Area = ½ab·sin C for the included angle — don't drop the ½.",
         "unit": "laws-of-sines-and-cosines",
         "variants": build_triangle_area_sine()},
        {"id": "law-of-sines", "title": "The law of sines",
         "level": 3, "skill": "b = a·sin B / sin A — match each side to its opposite angle.",
         "unit": "laws-of-sines-and-cosines",
         "variants": build_law_of_sines()},
    ]


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
