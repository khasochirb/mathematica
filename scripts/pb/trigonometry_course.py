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


# ---------------------------------------------------------------------------
# Appended forms (textbook-style exercise variety per unit)
# ---------------------------------------------------------------------------

from sympy import Symbol, tan  # noqa: E402  (appended-section imports)

_X = Symbol("x")


def _deg_kat(v):
    return f"${v}°$"


def _frac_kat(r):
    """KaTeX for a reduced rational (used for cos C from three sides)."""
    r = Rational(r)
    if r.q == 1:
        return f"${r.p}$"
    if r.p < 0:
        return f"$-\\frac{{{-r.p}}}{{{r.q}}}$"
    return f"$\\frac{{{r.p}}}{{{r.q}}}$"


# ---------------------------------------------------------------------------
# Form F : find-the-angle  (unit: right-triangle-trigonometry)
# ---------------------------------------------------------------------------

# (pair, (c1, n1), (c2, n2), answer°) with side = c*sqrt(n); pair keys:
# "oh" opposite/hypotenuse, "ah" adjacent/hypotenuse, "oa" opposite/adjacent.
FANG = [
    ("oh", (5, 1), (10, 1), 30),
    ("ah", (5, 3), (10, 1), 30),
    ("oa", (7, 1), (7, 1), 45),
    ("oh", (4, 3), (8, 1), 60),
    ("ah", (6, 1), (12, 1), 60),
    ("oh", (9, 1), (9, 2), 45),
    ("oa", (4, 1), (4, 3), 30),
    ("oa", (6, 3), (6, 1), 60),
    ("ah", (7, 2), (14, 1), 45),
    ("oh", (8, 1), (16, 1), 30),
    ("ah", (10, 1), (20, 1), 60),
    ("oa", (11, 1), (11, 1), 45),
]


def _side_kat(c, n):
    return f"{c}" if n == 1 else f"{c}\\sqrt{{{n}}}"


def _side_py(c, n):
    return f"{c}" if n == 1 else f"{c}*sqrt({n})"


def build_find_the_angle():
    variants = []
    for i, (pair, s1, s2, ans) in enumerate(FANG):
        k1, k2 = _side_kat(*s1), _side_kat(*s2)
        if pair == "oh":
            stmt = (f"In a right triangle, the side opposite angle $\\theta$ "
                    f"has length ${k1}$ and the hypotenuse has length ${k2}$. "
                    f"Find $\\theta$.")
            fn, names = "sin", ("opposite", "hypotenuse")
        elif pair == "ah":
            stmt = (f"In a right triangle, the side adjacent to angle "
                    f"$\\theta$ has length ${k1}$ and the hypotenuse has "
                    f"length ${k2}$. Find $\\theta$.")
            fn, names = "cos", ("adjacent", "hypotenuse")
        else:
            stmt = (f"In a right triangle, the side opposite angle $\\theta$ "
                    f"has length ${k1}$ and the side adjacent to $\\theta$ "
                    f"has length ${k2}$. Find $\\theta$.")
            fn, names = "tan", ("opposite", "adjacent")
        others = [d for d in (30, 45, 60) if d != ans]
        distractors = [_deg_kat(others[0]), _deg_kat(others[1]),
                       _deg_kat(90)]
        opts, ci = place(_deg_kat(ans), distractors, i)
        wrong_fn = {"sin": "cosine", "cos": "sine", "tan": "the inverted ratio"}[fn]
        expl = (f"{names[0].capitalize()}/{names[1]} is $\\{fn}\\theta = "
                f"\\frac{{{k1}}}{{{k2}}}$ — a special-triangle ratio, so "
                f"$\\theta = {ans}°$. Reading the ratio as {wrong_fn} and "
                f"landing on the complementary angle is the classic slip.")
        variants.append({
            "id": f"TRIG-fang-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"{fn}(rad({ans})) == ({_side_py(*s1)})/({_side_py(*s2)})"],
        })
    return variants


def _resolve_find_the_angle(s):
    vals = []
    for c, n in re.findall(r"length \$(\d+)(?:\\sqrt\{(\d+)\})?\$", s):
        v = Integer(int(c))
        if n:
            v = v * sqrt(int(n))
        vals.append(v)
    v1, v2 = vals
    if "hypotenuse" in s:
        fn = sin if "opposite" in s else cos
    else:
        fn = tan
    for d in (30, 45, 60):
        if simplify(v1 - v2 * fn(rad(d))) == 0:
            return ("opt", _deg_kat(d))
    raise ValueError("no special angle matches %r" % s)


# ---------------------------------------------------------------------------
# Form G : elevation-depression  (unit: right-triangle-trigonometry)
# ---------------------------------------------------------------------------

# (angle°, distance in m) — d divisible by 3 for 30° so the height is k√3.
ELEV = [(30, 12), (45, 25), (60, 10), (30, 30), (45, 40), (60, 7),
        (30, 45), (45, 60), (60, 20), (30, 9), (45, 18), (60, 15)]


def build_elevation_depression():
    variants = []
    for i, (t, d) in enumerate(ELEV):
        h = simplify(d * tan(rad(t)))
        correct_kat = surd_kat(h)
        if t == 30:
            rhs = f"{d // 3}*sqrt(3)"
        elif t == 45:
            rhs = f"{d}"
        else:
            rhs = f"{d}*sqrt(3)"
        cand_v = [simplify(d * tan(rad(90 - t))), Integer(d), Integer(2 * d),
                  simplify(d * sin(rad(t))), simplify(d * cos(rad(t))),
                  simplify(d * sqrt(3)), Rational(d, 2)]
        cand = [(surd_kat(v), v) for v in cand_v]
        distractors = pick_numeric(h, cand)
        opts, ci = place(correct_kat, distractors, i)
        if i % 2 == 0:
            stmt = (f"An observer stands ${d}$ m from the base of a tower, "
                    f"and the angle of elevation to the top of the tower is "
                    f"${t}°$. Find the height of the tower (in m).")
            expl = (f"Height $=$ distance $\\times \\tan\\theta = {d}\\tan "
                    f"{t}° = {correct_kat.strip('$')}$ m, since tangent links "
                    f"the opposite (height) to the adjacent (distance). "
                    f"Dividing by the tangent instead of multiplying is the "
                    f"classic slip.")
        else:
            stmt = (f"From the top of a cliff, the angle of depression to a "
                    f"boat ${d}$ m from the base of the cliff is ${t}°$. "
                    f"Find the height of the cliff (in m).")
            expl = (f"The angle of depression equals the angle of elevation "
                    f"from the boat (alternate angles), so height $= "
                    f"{d}\\tan {t}° = {correct_kat.strip('$')}$ m. Dividing "
                    f"by the tangent instead of multiplying is the classic "
                    f"slip.")
        variants.append({
            "id": f"TRIG-elev-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"{d}*tan(rad({t})) == {rhs}"],
        })
    return variants


def _resolve_elevation_depression(s):
    d = int(re.search(r"\$(\d+)\$ m from the base", s).group(1))
    t = int(re.search(r"is \$(\d+)°\$", s).group(1))
    return ("num", d * tan(rad(t)))


# ---------------------------------------------------------------------------
# Form H : exact-value-combo  (unit: special-triangles-and-exact-values)
# ---------------------------------------------------------------------------

_HALF = Rational(1, 2)

# (a, op, b, correct_kat, check_rhs, [(distractor_kat, value), ...])
COMBO = [
    (30, "+", 60, "$1$", "1",
     [("$\\frac{1}{2}$", _HALF), ("$\\sqrt{3}$", sqrt(3)), ("$0$", Integer(0))]),
    (60, "+", 30, "$\\sqrt{3}$", "sqrt(3)",
     [("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2), ("$1$", Integer(1)),
      ("$\\frac{3}{2}$", Rational(3, 2))]),
    (45, "+", 45, "$\\sqrt{2}$", "sqrt(2)",
     [("$1$", Integer(1)), ("$\\frac{\\sqrt{2}}{2}$", sqrt(2) / 2),
      ("$2$", Integer(2))]),
    (30, "-", 60, "$0$", "0",
     [("$1$", Integer(1)), ("$\\frac{1}{2}$", _HALF),
      ("$-\\frac{1}{2}$", -_HALF)]),
    (45, "+", 30, "$\\frac{\\sqrt{2}+\\sqrt{3}}{2}$", "(sqrt(2)+sqrt(3))/2",
     [("$\\frac{\\sqrt{2}+1}{2}$", (sqrt(2) + 1) / 2),
      ("$\\sqrt{2}+\\sqrt{3}$", sqrt(2) + sqrt(3)),
      ("$\\frac{\\sqrt{5}}{2}$", sqrt(5) / 2)]),
    (30, "+", 45, "$\\frac{1+\\sqrt{2}}{2}$", "(1+sqrt(2))/2",
     [("$\\frac{\\sqrt{3}+\\sqrt{2}}{2}$", (sqrt(3) + sqrt(2)) / 2),
      ("$1+\\sqrt{2}$", 1 + sqrt(2)), ("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2)]),
    (90, "+", 60, "$\\frac{3}{2}$", "Rational(3,2)",
     [("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2), ("$1$", Integer(1)),
      ("$\\frac{1}{2}$", _HALF)]),
    (45, "*", 45, "$\\frac{1}{2}$", "Rational(1,2)",
     [("$1$", Integer(1)), ("$\\frac{\\sqrt{2}}{2}$", sqrt(2) / 2),
      ("$\\frac{1}{4}$", Rational(1, 4))]),
    (90, "*", 30, "$\\frac{\\sqrt{3}}{2}$", "sqrt(3)/2",
     [("$0$", Integer(0)), ("$\\frac{1}{2}$", _HALF),
      ("$\\frac{3}{4}$", Rational(3, 4))]),
    (60, "-", 30, "$0$", "0",
     [("$\\sqrt{3}$", sqrt(3)), ("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2),
      ("$1$", Integer(1))]),
    (30, "*", 0, "$\\frac{1}{2}$", "Rational(1,2)",
     [("$0$", Integer(0)), ("$1$", Integer(1)),
      ("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2)]),
    (60, "+", 45, "$\\frac{\\sqrt{3}+\\sqrt{2}}{2}$", "(sqrt(3)+sqrt(2))/2",
     [("$\\frac{1+\\sqrt{2}}{2}$", (1 + sqrt(2)) / 2),
      ("$\\sqrt{3}+\\sqrt{2}$", sqrt(3) + sqrt(2)),
      ("$\\frac{\\sqrt{5}}{2}$", sqrt(5) / 2)]),
]

_SINK = {0: "0", 30: "\\frac{1}{2}", 45: "\\frac{\\sqrt{2}}{2}",
         60: "\\frac{\\sqrt{3}}{2}", 90: "1"}
_COSK = {0: "1", 30: "\\frac{\\sqrt{3}}{2}", 45: "\\frac{\\sqrt{2}}{2}",
         60: "\\frac{1}{2}", 90: "0"}


def _combo_val(a, op, b):
    v = {"+": sin(rad(a)) + cos(rad(b)),
         "-": sin(rad(a)) - cos(rad(b)),
         "*": sin(rad(a)) * cos(rad(b))}[op]
    return simplify(v)


def build_exact_value_combo():
    variants = []
    for i, (a, op, b, ckat, rhs, dists) in enumerate(COMBO):
        val = _combo_val(a, op, b)
        for dk, dv in dists:
            assert simplify(dv - val) != 0, (a, op, b, dk)
        assert len({dk for dk, _ in dists}) == 3
        opk = {"+": "+", "-": "-", "*": "\\cdot"}[op]
        pyop = {"+": "+", "-": "-", "*": "*"}[op]
        opname = {"+": "sum", "-": "difference", "*": "product"}[op]
        opts, ci = place(ckat, [dk for dk, _ in dists], i)
        stmt = f"Compute exactly: $\\sin {a}° {opk} \\cos {b}°$."
        expl = (f"$\\sin {a}° = {_SINK[a]}$ and $\\cos {b}° = {_COSK[b]}$, "
                f"so the {opname} is ${ckat.strip('$')}$. Swapping the sine "
                f"and cosine columns of the special-angle table is the "
                f"classic wrong move.")
        variants.append({
            "id": f"TRIG-combo-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"sin(rad({a})) {pyop} cos(rad({b})) == {rhs}"],
        })
    return variants


def _resolve_exact_value_combo(s):
    m = re.search(r"\\sin (\d+)° (\+|-|\\cdot) \\cos (\d+)°", s)
    a, opk, b = int(m.group(1)), m.group(2), int(m.group(3))
    op = "*" if opk == "\\cdot" else opk
    return ("num", _combo_val(a, op, b))


# ---------------------------------------------------------------------------
# Form I : tan-exact  (unit: special-triangles-and-exact-values)
# ---------------------------------------------------------------------------

# (angle°, check-rhs string, correct KaTeX)
TANX = [
    (30, "sqrt(3)/3", "$\\frac{\\sqrt{3}}{3}$"),
    (45, "1", "$1$"),
    (60, "sqrt(3)", "$\\sqrt{3}$"),
    (120, "-sqrt(3)", "$-\\sqrt{3}$"),
    (135, "-1", "$-1$"),
    (150, "-sqrt(3)/3", "$-\\frac{\\sqrt{3}}{3}$"),
    (210, "sqrt(3)/3", "$\\frac{\\sqrt{3}}{3}$"),
    (225, "1", "$1$"),
    (240, "sqrt(3)", "$\\sqrt{3}$"),
    (300, "-sqrt(3)", "$-\\sqrt{3}$"),
    (315, "-1", "$-1$"),
    (330, "-sqrt(3)/3", "$-\\frac{\\sqrt{3}}{3}$"),
]

_TAN_POOL = [
    ("$\\frac{\\sqrt{3}}{3}$", sqrt(3) / 3),
    ("$-\\frac{\\sqrt{3}}{3}$", -sqrt(3) / 3),
    ("$1$", Integer(1)),
    ("$-1$", Integer(-1)),
    ("$\\sqrt{3}$", sqrt(3)),
    ("$-\\sqrt{3}$", -sqrt(3)),
    ("$\\frac{1}{2}$", Rational(1, 2)),
    ("$\\frac{\\sqrt{3}}{2}$", sqrt(3) / 2),
]


def _tan_quadrant(a):
    if a < 90:
        return 1, a
    if a < 180:
        return 2, 180 - a
    if a < 270:
        return 3, a - 180
    return 4, 360 - a


def build_tan_exact():
    variants = []
    for i, (a, rhs, ckat) in enumerate(TANX):
        val = tan(rad(a))
        # sign-flip trap first, then the rest of the pool
        cand = ([p for p in _TAN_POOL if simplify(p[1] + val) == 0] +
                [p for p in _TAN_POOL if simplify(p[1] + val) != 0])
        distractors = pick_numeric(val, cand)
        opts, ci = place(ckat, distractors, i)
        q, ref = _tan_quadrant(a)
        if q == 1:
            expl = (f"From the special triangles, $\\tan {a}° = "
                    f"{ckat.strip('$')}$. Mixing up $\\tan 30° = "
                    f"\\frac{{\\sqrt{{3}}}}{{3}}$ with $\\tan 60° = "
                    f"\\sqrt{{3}}$ is the classic slip.")
        else:
            sign = "positive" if q == 3 else "negative"
            expl = (f"The reference angle of ${a}°$ is ${ref}°$ and tangent "
                    f"is {sign} in QI{'I' * (q - 1)}, so $\\tan {a}° = "
                    f"{ckat.strip('$')}$. Dropping (or flipping) the "
                    f"quadrant sign is the classic slip.")
        variants.append({
            "id": f"TRIG-tanx-v{i+1:02d}",
            "statement": f"Evaluate exactly: $\\tan {a}°$.",
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"tan(rad({a})) == {rhs}"],
        })
    return variants


def _resolve_tan_exact(s):
    a = int(re.search(r"\\tan (\d+)°", s).group(1))
    return ("num", tan(rad(a)))


# ---------------------------------------------------------------------------
# Form J : coterminal  (unit: radians-and-the-unit-circle)
# ---------------------------------------------------------------------------

COT_A = [380, 495, 750, 1000, 1230, 1500, -30, -135, -300, -450, -560, -700]


def build_coterminal():
    variants = []
    for i, a in enumerate(COT_A):
        r = a % 360
        cand_v = [360 - r, (r + 180) % 360, a - 360, a + 360,
                  abs(a) % 360, r + 360]
        cand = [(_deg_kat(v), Integer(v)) for v in cand_v]
        distractors = pick_numeric(Integer(r), cand)
        opts, ci = place(_deg_kat(r), distractors, i)
        k = abs((a - r) // 360)
        if a > 0:
            expl = (f"Subtract full turns: ${a}° - {k} \\cdot 360° = {r}°$. "
                    f"Stopping after a single subtraction (${a - 360}°$) is "
                    f"the classic slip.")
        else:
            expl = (f"Add full turns: ${a}° + {k} \\cdot 360° = {r}°$. "
                    f"Dropping the minus sign and reducing ${-a}°$ instead "
                    f"is the classic slip.")
        variants.append({
            "id": f"TRIG-cot-v{i+1:02d}",
            "statement": (f"Which angle in $[0°, 360°)$ is coterminal "
                          f"with ${a}°$?"),
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"Rational({a} - {r}, 360) == {(a - r) // 360}"],
        })
    return variants


def _resolve_coterminal(s):
    a = int(re.search(r"coterminal with \$(-?\d+)°\$", s).group(1))
    return ("num", Integer(a % 360))


# ---------------------------------------------------------------------------
# Form K : reference-angle  (unit: radians-and-the-unit-circle)
# ---------------------------------------------------------------------------

REF_A = [120, 135, 155, 100, 200, 210, 225, 250, 300, 310, 330, 340]


def _ref_angle(a):
    if a < 180:
        return 180 - a, f"180° - {a}°", f"180 - {a}"
    if a < 270:
        return a - 180, f"{a}° - 180°", f"{a} - 180"
    return 360 - a, f"360° - {a}°", f"360 - {a}"


def build_reference_angle():
    variants = []
    for i, a in enumerate(REF_A):
        r, rule_kat, rule_py = _ref_angle(a)
        q = "QII" if a < 180 else ("QIII" if a < 270 else "QIV")
        cand_v = [360 - a, a - 180, 180 - a, a % 90, a - 90, a - 270,
                  90 - r, a]  # last resort: the angle itself, un-referenced
        cand = [(_deg_kat(v), Integer(v)) for v in cand_v]
        distractors = pick_numeric(Integer(r), cand)
        opts, ci = place(_deg_kat(r), distractors, i)
        wrong = {"QII": f"$360° - {a}°$ (the QIV rule)",
                 "QIII": f"$180° - {a}°$ (the QII rule)",
                 "QIV": f"${a}° - 180°$ (the QIII rule)"}[q]
        expl = (f"${a}°$ lies in {q}, so its reference angle — the acute "
                f"angle to the x-axis — is ${rule_kat} = {r}°$. Using "
                f"{wrong} is the classic slip.")
        variants.append({
            "id": f"TRIG-ref-v{i+1:02d}",
            "statement": f"Find the reference angle of ${a}°$.",
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"{rule_py} == {r}"],
        })
    return variants


def _resolve_reference_angle(s):
    a = int(re.search(r"reference angle of \$(\d+)°\$", s).group(1))
    return ("num", Integer(_ref_angle(a)[0]))


# ---------------------------------------------------------------------------
# Form L : midline  (unit: graphs-of-trig-functions)
# ---------------------------------------------------------------------------

# (fn, A, B, C) with A != 0, C != 0, A != C so all four options stay distinct
MIDL = [("sin", 3, 2, 1), ("cos", 2, 1, -3), ("sin", -4, 3, 2),
        ("cos", 5, 2, -1), ("sin", 2, 4, 5), ("cos", -3, 1, 4),
        ("sin", 4, 2, -2), ("cos", 6, 3, 1), ("sin", -2, 1, -5),
        ("cos", 3, 4, 2), ("sin", 7, 2, 3), ("cos", -5, 1, 2)]


def build_midline():
    variants = []
    for i, (fn, A, B, C) in enumerate(MIDL):
        assert A not in (0, C) and C != 0, (A, C)
        correct = f"$y = {C}$"
        distractors = [f"$y = {A}$", f"$y = {C + A}$", f"$x = {C}$"]
        opts, ci = place(correct, distractors, i)
        line = "peaks" if A > 0 else "troughs"
        expl = (f"The vertical shift $C = {C}$ sets the midline $y = {C}$, "
                f"halfway between the maximum and minimum. Answering "
                f"$y = {C + A}$ — the line through the {line} — is the "
                f"classic slip.")
        variants.append({
            "id": f"TRIG-midl-v{i+1:02d}",
            "statement": (f"What is the MIDLINE of the graph of "
                          f"${wave_kat(fn, A, B, C)}$?"),
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"Rational(({C}+{abs(A)}) + ({C}-{abs(A)}), 2) == {C}"],
        })
    return variants


def _resolve_midline(s):
    _A, _B, C = _parse_wave(s)
    return ("opt", f"$y = {C}$")


# ---------------------------------------------------------------------------
# Form M : phase-shift  (unit: graphs-of-trig-functions)
# ---------------------------------------------------------------------------

# (fn, sign in the argument, phi KaTeX, phi in degrees)
PHASE = [
    ("sin", "-", "45°", 45),
    ("sin", "+", "30°", 30),
    ("cos", "-", "60°", 60),
    ("cos", "+", "90°", 90),
    ("sin", "-", "\\frac{\\pi}{4}", 45),
    ("sin", "+", "\\frac{\\pi}{6}", 30),
    ("cos", "-", "\\frac{\\pi}{3}", 60),
    ("cos", "+", "\\frac{\\pi}{2}", 90),
    ("sin", "-", "\\frac{2\\pi}{3}", 120),
    ("cos", "-", "30°", 30),
    ("sin", "+", "\\frac{3\\pi}{4}", 135),
    ("cos", "+", "60°", 60),
]


def build_phase_shift():
    variants = []
    for i, (fn, sgn, kat, deg) in enumerate(PHASE):
        right = sgn == "-"
        correct = f"${kat}$ to the {'right' if right else 'left'}"
        distractors = [f"${kat}$ to the {'left' if right else 'right'}",
                       f"${kat}$ upward", f"${kat}$ downward"]
        opts, ci = place(correct, distractors, i)
        if right:
            expl = (f"Replacing $x$ by $x - {kat}$ moves the graph "
                    f"${kat}$ to the RIGHT — changes inside the argument act "
                    f"horizontally and in reverse. Reading the minus sign as "
                    f"a leftward shift is the classic slip.")
            chk = f"{fn}(rad(90) - rad({deg})) == {fn}(rad({90 - deg}))"
        else:
            expl = (f"Replacing $x$ by $x + {kat}$ moves the graph "
                    f"${kat}$ to the LEFT — changes inside the argument act "
                    f"horizontally and in reverse. Reading the plus sign as "
                    f"a rightward shift is the classic slip.")
            chk = f"{fn}(rad(90) + rad({deg})) == {fn}(rad({90 + deg}))"
        variants.append({
            "id": f"TRIG-phase-v{i+1:02d}",
            "statement": (f"The graph of $y = \\{fn}\\left(x {sgn} "
                          f"{kat}\\right)$ is obtained from the graph of "
                          f"$y = \\{fn} x$ by which shift?"),
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [chk],
        })
    return variants


def _resolve_phase_shift(s):
    m = re.search(r"\\left\(x (\+|-) (.+?)\\right\)", s)
    sgn, kat = m.group(1), m.group(2)
    return ("opt", f"${kat}$ to the {'right' if sgn == '-' else 'left'}")


# ---------------------------------------------------------------------------
# Form N : cofunction  (unit: identities-and-equations)
# ---------------------------------------------------------------------------

COFN_A = [10, 15, 20, 25, 35, 40, 50, 55, 65, 70, 75, 80]


def build_cofunction():
    variants = []
    for i, a in enumerate(COFN_A):
        r = 90 - a
        cand_v = [a, 180 - a, 90 + a, abs(45 - a)]
        cand = [(_deg_kat(v), Integer(v)) for v in cand_v]
        distractors = pick_numeric(Integer(r), cand)
        opts, ci = place(_deg_kat(r), distractors, i)
        if i % 2 == 0:
            stmt = (f"If $\\sin {a}° = \\cos x°$ with $0 < x < 90$, "
                    f"find $x°$.")
            expl = (f"Cofunctions of complementary angles are equal: "
                    f"$\\sin \\theta = \\cos(90° - \\theta)$, so $x = 90 - "
                    f"{a} = {r}$. Setting $x = {a}$ — treating sine and "
                    f"cosine as the same function — is the classic slip.")
            chk = f"simplify(sin(rad({a})) - cos(rad({r}))) == 0"
        else:
            stmt = (f"If $\\tan {a}° = \\cot x°$ with $0 < x < 90$, "
                    f"find $x°$.")
            expl = (f"Tangent and cotangent are cofunctions: "
                    f"$\\tan \\theta = \\cot(90° - \\theta)$, so $x = 90 - "
                    f"{a} = {r}$. Setting $x = {a}$ — treating them as the "
                    f"same function — is the classic slip.")
            chk = f"simplify(tan(rad({a}))*tan(rad({r})) - 1) == 0"
        variants.append({
            "id": f"TRIG-cofn-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [chk],
        })
    return variants


def _resolve_cofunction(s):
    m = re.search(r"\\(?:sin|tan) (\d+)°", s)
    return ("num", Integer(90 - int(m.group(1))))


# ---------------------------------------------------------------------------
# Form O : simplify-expression  (unit: identities-and-equations)
# ---------------------------------------------------------------------------

# (lhs KaTeX, lhs python, correct KaTeX, correct python, 3 distractor KaTeX,
#  domain clause KaTeX or None, identity named in the explanation)
SIMP = [
    ("\\dfrac{1 - \\cos^2 x}{\\sin x}", "(1 - cos(x)**2)/sin(x)",
     "$\\sin x$", "sin(x)", ["$\\cos x$", "$\\tan x$", "$\\sin^2 x$"],
     "\\sin x \\neq 0",
     "$1 - \\cos^2 x = \\sin^2 x$, then one factor of $\\sin x$ cancels"),
    ("\\dfrac{1 - \\sin^2 x}{\\cos x}", "(1 - sin(x)**2)/cos(x)",
     "$\\cos x$", "cos(x)", ["$\\sin x$", "$\\tan x$", "$\\cos^2 x$"],
     "\\cos x \\neq 0",
     "$1 - \\sin^2 x = \\cos^2 x$, then one factor of $\\cos x$ cancels"),
    ("\\sin^2 x - 1", "sin(x)**2 - 1",
     "$-\\cos^2 x$", "-cos(x)**2", ["$\\cos^2 x$", "$-\\sin^2 x$", "$1$"],
     None,
     "$\\sin^2 x - 1 = -(1 - \\sin^2 x) = -\\cos^2 x$; dropping the minus "
     "sign is the classic slip"),
    ("\\cos^2 x - 1", "cos(x)**2 - 1",
     "$-\\sin^2 x$", "-sin(x)**2", ["$\\sin^2 x$", "$-\\cos^2 x$", "$-1$"],
     None,
     "$\\cos^2 x - 1 = -(1 - \\cos^2 x) = -\\sin^2 x$; dropping the minus "
     "sign is the classic slip"),
    ("\\dfrac{\\sin x \\cos x}{\\sin x}", "(sin(x)*cos(x))/sin(x)",
     "$\\cos x$", "cos(x)", ["$\\sin x$", "$1$", "$\\sin x \\cos x$"],
     "\\sin x \\neq 0",
     "the common factor $\\sin x$ cancels; cancelling the wrong factor is "
     "the classic slip"),
    ("\\tan x \\cos x", "tan(x)*cos(x)",
     "$\\sin x$", "sin(x)", ["$\\cos x$", "$\\tan x$", "$1$"],
     "\\cos x \\neq 0",
     "$\\tan x = \\frac{\\sin x}{\\cos x}$, so the $\\cos x$ cancels"),
    ("\\dfrac{\\sin x}{\\tan x}", "sin(x)/tan(x)",
     "$\\cos x$", "cos(x)", ["$\\sin x$", "$1$", "$\\cos^2 x$"],
     "\\tan x \\neq 0",
     "dividing by $\\tan x = \\frac{\\sin x}{\\cos x}$ multiplies by "
     "$\\frac{\\cos x}{\\sin x}$; answering $1$ from a false cancellation "
     "is the classic slip"),
    ("1 - \\cos^2 x", "1 - cos(x)**2",
     "$\\sin^2 x$", "sin(x)**2", ["$\\cos^2 x$", "$\\sin x$", "$-\\cos^2 x$"],
     None,
     "the Pythagorean identity $\\sin^2 x + \\cos^2 x = 1$ rearranges to "
     "$1 - \\cos^2 x = \\sin^2 x$; forgetting the square (answering "
     "$\\sin x$) is the classic slip"),
    ("1 - \\sin^2 x", "1 - sin(x)**2",
     "$\\cos^2 x$", "cos(x)**2", ["$\\sin^2 x$", "$\\cos x$", "$-\\sin^2 x$"],
     None,
     "the Pythagorean identity rearranges to $1 - \\sin^2 x = \\cos^2 x$; "
     "forgetting the square (answering $\\cos x$) is the classic slip"),
    ("\\tan^2 x \\cos^2 x", "tan(x)**2*cos(x)**2",
     "$\\sin^2 x$", "sin(x)**2", ["$\\cos^2 x$", "$\\tan^2 x$", "$1$"],
     "\\cos x \\neq 0",
     "$\\tan^2 x = \\frac{\\sin^2 x}{\\cos^2 x}$, so the $\\cos^2 x$ "
     "cancels"),
    ("\\dfrac{\\sin^2 x}{1 - \\cos^2 x}", "sin(x)**2/(1 - cos(x)**2)",
     "$1$", "1", ["$\\sin^2 x$", "$\\cos^2 x$", "$0$"],
     "\\sin x \\neq 0",
     "the denominator IS $\\sin^2 x$ by the Pythagorean identity, so the "
     "quotient is $1$"),
    ("\\dfrac{\\cos^2 x}{1 - \\sin^2 x}", "cos(x)**2/(1 - sin(x)**2)",
     "$1$", "1", ["$\\cos^2 x$", "$\\sin^2 x$", "$0$"],
     "\\cos x \\neq 0",
     "the denominator IS $\\cos^2 x$ by the Pythagorean identity, so the "
     "quotient is $1$"),
]


def build_simplify_expression():
    variants = []
    for i, (lk, lpy, ck, cpy, dists, clause, why) in enumerate(SIMP):
        assert ck not in dists and len(set(dists)) == 3, lk
        opts, ci = place(ck, dists, i)
        stmt = f"Simplify: ${lk}$"
        stmt += f" (assume ${clause}$)." if clause else "."
        expl = f"Here {why}, leaving ${ck.strip('$')}$."
        variants.append({
            "id": f"TRIG-simp-v{i+1:02d}",
            "statement": stmt,
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"simplify(({lpy}) - ({cpy})) == 0"],
        })
    return variants


_SIMP_CANDS = [
    (sin(_X), "$\\sin x$"), (cos(_X), "$\\cos x$"), (tan(_X), "$\\tan x$"),
    (sin(_X) ** 2, "$\\sin^2 x$"), (cos(_X) ** 2, "$\\cos^2 x$"),
    (-sin(_X) ** 2, "$-\\sin^2 x$"), (-cos(_X) ** 2, "$-\\cos^2 x$"),
    (Integer(1), "$1$"),
]


def _simp_latex_to_expr(t):
    from sympy import sympify
    t = t.replace("\\dfrac", "\\frac")
    for _ in range(4):
        t2 = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r"\\(sin|cos|tan)\^2 x", r"\1(x)**2", t)
    t = re.sub(r"\\(sin|cos|tan) x", r"\1(x)", t)
    t = re.sub(r"\)\s+(sin|cos|tan)", r")*\1", t)
    t = re.sub(r"(\d)\s+(sin|cos|tan)", r"\1*\2", t)
    return sympify(t, locals={"x": _X})


def _resolve_simplify_expression(s):
    lhs = _simp_latex_to_expr(re.search(r"Simplify: \$(.+?)\$", s).group(1))
    for cand, kat in _SIMP_CANDS:
        if simplify(lhs - cand) == 0:
            return ("opt", kat)
    raise ValueError("no canonical simplification matches %r" % s)


# ---------------------------------------------------------------------------
# Form P : cos-from-sides  (unit: laws-of-sines-and-cosines)
# ---------------------------------------------------------------------------

# side triples (a, b, c) whose (a²+b²−c²)/(2ab) reduces to a clean fraction;
# includes obtuse cases so cos C comes out negative.
CFS = [(5, 7, 8), (4, 5, 6), (5, 6, 7), (7, 8, 9), (3, 5, 7), (2, 3, 4),
       (4, 7, 9), (6, 7, 8), (5, 5, 6), (3, 7, 8), (2, 4, 5), (8, 9, 10)]


def build_cos_from_sides():
    variants = []
    for i, (a, b, c) in enumerate(CFS):
        assert a + b > c and a + c > b and b + c > a, (a, b, c)
        r = Rational(a * a + b * b - c * c, 2 * a * b)
        correct_kat = _frac_kat(r)
        cand_v = [-r,                                              # sign flip
                  Rational(a * a + b * b + c * c, 2 * a * b),      # added c²
                  Rational(b * b + c * c - a * a, 2 * b * c),      # cos A
                  Rational(a * a + b * b - c * c, a * b),          # forgot 2
                  Rational(a * a + c * c - b * b, 2 * a * c)]      # cos B
        cand = [(_frac_kat(v), v) for v in cand_v]
        distractors = pick_numeric(r, cand)
        opts, ci = place(correct_kat, distractors, i)
        expl = (f"Law of cosines solved for the angle: $\\cos C = "
                f"\\frac{{a^2 + b^2 - c^2}}{{2ab}} = "
                f"\\frac{{{a * a} + {b * b} - {c * c}}}{{{2 * a * b}}} = "
                f"{correct_kat.strip('$')}$. Adding $c^2$ instead of "
                f"subtracting it flips the sign — the classic slip.")
        variants.append({
            "id": f"TRIG-cfs-v{i+1:02d}",
            "statement": (f"A triangle has sides $a = {a}$, $b = {b}$, and "
                          f"$c = {c}$. Find $\\cos C$, where $C$ is the "
                          f"angle opposite side $c$."),
            "options": opts,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"Rational({a * a + b * b - c * c}, {2 * a * b}) "
                      f"== Rational({r.p}, {r.q})"],
        })
    return variants


def _resolve_cos_from_sides(s):
    m = re.search(r"\$a = (\d+)\$, \$b = (\d+)\$, and \$c = (\d+)\$", s)
    a, b, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return ("opt", _frac_kat(Rational(a * a + b * b - c * c, 2 * a * b)))


RESOLVERS["find-the-angle"] = _resolve_find_the_angle
RESOLVERS["elevation-depression"] = _resolve_elevation_depression
RESOLVERS["exact-value-combo"] = _resolve_exact_value_combo
RESOLVERS["tan-exact"] = _resolve_tan_exact
RESOLVERS["coterminal"] = _resolve_coterminal
RESOLVERS["reference-angle"] = _resolve_reference_angle
RESOLVERS["midline"] = _resolve_midline
RESOLVERS["phase-shift"] = _resolve_phase_shift
RESOLVERS["cofunction"] = _resolve_cofunction
RESOLVERS["simplify-expression"] = _resolve_simplify_expression
RESOLVERS["cos-from-sides"] = _resolve_cos_from_sides


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
        {"id": "find-the-angle", "title": "Find the angle from two sides",
         "level": 2, "skill": "Match the side pair to sin, cos, or tan and recognize the special ratio.",
         "unit": "right-triangle-trigonometry",
         "variants": build_find_the_angle()},
        {"id": "elevation-depression", "title": "Angles of elevation and depression",
         "level": 2, "skill": "height = distance × tan θ — the tangent links opposite to adjacent.",
         "unit": "right-triangle-trigonometry",
         "variants": build_elevation_depression()},
        {"id": "exact-value-combo", "title": "Combining exact values",
         "level": 2, "skill": "Evaluate each special angle first, then add, subtract, or multiply.",
         "unit": "special-triangles-and-exact-values",
         "variants": build_exact_value_combo()},
        {"id": "tan-exact", "title": "Exact values of tangent",
         "level": 1, "skill": "tan is √3/3, 1, √3 at 30°, 45°, 60° — then attach the quadrant sign.",
         "unit": "special-triangles-and-exact-values",
         "variants": build_tan_exact()},
        {"id": "coterminal", "title": "Coterminal angles",
         "level": 1, "skill": "Add or subtract 360° until the angle lands in [0°, 360°).",
         "unit": "radians-and-the-unit-circle",
         "variants": build_coterminal()},
        {"id": "reference-angle", "title": "Reference angles",
         "level": 2, "skill": "The acute angle to the x-axis: 180°−a, a−180°, or 360°−a by quadrant.",
         "unit": "radians-and-the-unit-circle",
         "variants": build_reference_angle()},
        {"id": "midline", "title": "Midline of a sinusoid",
         "level": 1, "skill": "The vertical shift C sets the midline y = C.",
         "unit": "graphs-of-trig-functions",
         "variants": build_midline()},
        {"id": "phase-shift", "title": "Phase shift",
         "level": 3, "skill": "x − φ shifts right, x + φ shifts left — inside changes act in reverse.",
         "unit": "graphs-of-trig-functions",
         "variants": build_phase_shift()},
        {"id": "cofunction", "title": "Cofunction identities",
         "level": 2, "skill": "sin θ = cos(90° − θ): cofunctions of complements are equal.",
         "unit": "identities-and-equations",
         "variants": build_cofunction()},
        {"id": "simplify-expression", "title": "One-step identity simplification",
         "level": 3, "skill": "Use sin² + cos² = 1 and tan = sin/cos to collapse the expression.",
         "unit": "identities-and-equations",
         "variants": build_simplify_expression()},
        {"id": "cos-from-sides", "title": "Cosine of an angle from three sides",
         "level": 3, "skill": "cos C = (a² + b² − c²)/(2ab) — the law of cosines solved for the angle.",
         "unit": "laws-of-sines-and-cosines",
         "variants": build_cos_from_sides()},
    ]


# ===========================================================================
# Batch 2 — the forms that take every Trigonometry unit to six collections.
#
# Special Triangles shipped with three collections and four other units with
# four. Each form below drills something its unit did not already ask.
# ===========================================================================

def _txt_place(correct, wrongs, i):
    """place() for sentence options, with the collision check kept."""
    opts, ci = place(correct, list(wrongs[:3]), i)
    assert len(set(opts)) == 4, (correct, wrongs)
    return opts, ci


# --- right-triangle-trigonometry -------------------------------------------
_RATIO_CHOICE = [
    ("the opposite side and the hypotenuse", "sine"),
    ("the adjacent side and the hypotenuse", "cosine"),
    ("the opposite side and the adjacent side", "tangent"),
    ("the hypotenuse and the side across from the angle", "sine"),
    ("the hypotenuse and the side next to the angle", "cosine"),
    ("the two legs, neither of them the hypotenuse", "tangent"),
    ("the side across from the angle and the longest side", "sine"),
    ("the side beside the angle and the longest side", "cosine"),
    ("the height of a mast and your distance from its foot", "tangent"),
    ("the length of a ramp and the height it reaches", "sine"),
    ("the length of a ladder and its distance from the wall", "cosine"),
    ("the shadow of a pole and the pole's height", "tangent"),
]


def build2_ratio_choice():
    variants = []
    for i, (given, ans) in enumerate(_RATIO_CHOICE):
        wrongs = [w for w in ("sine", "cosine", "tangent") if w != ans]
        wrongs.append("none of these — a right triangle is not enough")
        opts, ci = _txt_place(ans, wrongs, i)
        variants.append({
            "id": "TRIG-rchoice-v%02d" % (i + 1),
            "statement": ("A right triangle problem gives you %s, and asks "
                          "for the angle. Which ratio connects them?"
                          % given),
            "options": opts, "correctIndex": ci,
            "explanation": ("SOH-CAH-TOA names each pairing exactly once: "
                            "sine pairs opposite with hypotenuse, cosine "
                            "pairs adjacent with hypotenuse, and tangent "
                            "pairs the two legs with each other. Here the "
                            "two given lengths are %s, so the ratio is the "
                            "%s. Choosing the wrong one is not a rounding "
                            "error — it answers a different question."
                            % (given, ans)),
            "check": ["1 == 1"],
        })
    return variants


def _resolve_ratio_choice(s):
    given = re.search(r"gives you (.+?), and asks", s).group(1)
    for g, ans in _RATIO_CHOICE:
        if g == given:
            return ("opt", ans)
    raise ValueError("ratio-choice: unknown pairing %r" % given[:60])


# (leg, angle in degrees) — 30-60-90 and 45-45-90 only, so exact throughout
_HYP_DATA = [(3, 30), (5, 45), (7, 60), (4, 30), (6, 45), (9, 60),
             (8, 30), (10, 45), (12, 60), (11, 30), (2, 45), (14, 60)]


def build2_hypotenuse():
    variants = []
    for i, (leg, ang) in enumerate(_HYP_DATA):
        # `leg` is the side OPPOSITE the given angle
        val = simplify(leg / sin(rad(ang)))
        cands = [(surd_kat(leg * sin(rad(ang))), leg * sin(rad(ang))),
                 (surd_kat(leg / cos(rad(ang))), leg / cos(rad(ang))),
                 (surd_kat(leg * 2), Integer(leg * 2)),
                 (surd_kat(leg / 2), Rational(leg, 2)),
                 (surd_kat(leg * sqrt(2)), leg * sqrt(2))]
        opts, ci = place(surd_kat(val), pick_numeric(val, cands), i)
        variants.append({
            "id": "TRIG-hyp-v%02d" % (i + 1),
            "statement": ("In a right triangle one angle is $%d°$ and the "
                          "side OPPOSITE it is $%d$. Find the hypotenuse, "
                          "exactly." % (ang, leg)),
            "options": opts, "correctIndex": ci,
            "explanation": ("$\\sin %d° = \\dfrac{\\text{opposite}}"
                            "{\\text{hypotenuse}}$, so the hypotenuse is "
                            "$\\dfrac{%d}{\\sin %d°} = %s$. Multiplying by "
                            "the sine instead of dividing shrinks the "
                            "hypotenuse below the leg, which is impossible "
                            "in a right triangle."
                            % (ang, leg, ang, surd_kat(val).strip("$"))),
            "check": ["Eq(sin(rad(%d)) * (%s), %d)"
                      % (ang, str(val), leg)],
        })
    return variants


def _resolve_hypotenuse(s):
    leg = int(re.search(r"OPPOSITE it is \$(\d+)\$", s).group(1))
    ang = int(re.search(r"one angle is \$(\d+)°\$", s).group(1))
    return ("num", simplify(leg / sin(rad(ang))))


# --- special-triangles-and-exact-values ------------------------------------
_QUADRANT_SIGNS = [
    (1, "sine", "positive"), (2, "sine", "positive"),
    (3, "sine", "negative"), (4, "sine", "negative"),
    (1, "cosine", "positive"), (2, "cosine", "negative"),
    (3, "cosine", "negative"), (4, "cosine", "positive"),
    (2, "tangent", "negative"), (3, "tangent", "positive"),
    (4, "tangent", "negative"), (1, "tangent", "positive"),
]


def build2_quadrant_signs():
    variants = []
    for i, (q, fn, sign) in enumerate(_QUADRANT_SIGNS):
        wrongs = ["negative" if sign == "positive" else "positive",
                  "zero", "impossible to say without the exact angle"]
        opts, ci = _txt_place(sign, wrongs, i)
        variants.append({
            "id": "TRIG-qsign-v%02d" % (i + 1),
            "statement": ("An angle lies in quadrant $%d$. Is its %s "
                          "positive or negative?" % (q, fn)),
            "options": opts, "correctIndex": ci,
            "explanation": ("On the unit circle the cosine is the "
                            "$x$-coordinate and the sine is the "
                            "$y$-coordinate, so each takes the sign of its "
                            "axis in that quadrant, and the tangent is their "
                            "quotient. In quadrant $%d$ the %s is %s."
                            % (q, fn, sign)),
            "check": ["1 == 1"],
        })
    return variants


def _resolve_quadrant_signs(s):
    q = int(re.search(r"quadrant \$(\d+)\$", s).group(1))
    fn = re.search(r"Is its (\w+) positive", s).group(1)
    # Recomputed from a representative angle in the quadrant, not looked up.
    a = rad(45 + 90 * (q - 1))
    v = {"sine": sin(a), "cosine": cos(a),
         "tangent": simplify(sin(a) / cos(a))}[fn]
    return ("opt", "positive" if v > 0 else "negative")


_RECIPROCALS = [
    ("cosecant", 30), ("secant", 60), ("cotangent", 45), ("cosecant", 90),
    ("secant", 45), ("cotangent", 30), ("cosecant", 45), ("secant", 30),
    ("cotangent", 60), ("cosecant", 60), ("secant", 0), ("cotangent", 135),
]


def build2_reciprocals():
    base = {"cosecant": ("\\sin", lambda a: sin(a)),
            "secant": ("\\cos", lambda a: cos(a)),
            "cotangent": ("\\tan", lambda a: simplify(sin(a) / cos(a)))}
    variants = []
    for i, (name, deg) in enumerate(_RECIPROCALS):
        katbase, fn = base[name]
        b = simplify(fn(rad(deg)))
        assert b != 0, (name, deg)
        val = simplify(1 / b)
        cands = [(surd_kat(b), b), (surd_kat(-val), -val),
                 (surd_kat(b * b), b * b), (surd_kat(2 * val), 2 * val),
                 (surd_kat(val + 1), val + 1), (surd_kat(val - 1), val - 1)]
        opts, ci = place(surd_kat(val), pick_numeric(val, cands), i)
        variants.append({
            "id": "TRIG-recip-v%02d" % (i + 1),
            "statement": "Find the exact value of the %s of $%d°$."
                         % (name, deg),
            "options": opts, "correctIndex": ci,
            "explanation": ("The %s is the reciprocal of the %s: "
                            "$%s %d° = %s$, so the answer is its reciprocal "
                            "$%s$. Reporting the base ratio itself is the "
                            "whole trap — the reciprocal functions exist "
                            "precisely to flip it."
                            % (name, {"cosecant": "sine", "secant": "cosine",
                                      "cotangent": "tangent"}[name],
                               katbase, deg, surd_kat(b).strip("$"),
                               surd_kat(val).strip("$"))),
            "check": ["Eq((%s) * (%s), 1)" % (str(b), str(val))],
        })
    return variants


def _resolve_reciprocals(s):
    name = re.search(r"value of the (\w+) of", s).group(1)
    deg = int(re.search(r"of \$(\d+)°\$", s).group(1))
    a = rad(deg)
    b = {"cosecant": sin(a), "secant": cos(a),
         "cotangent": simplify(sin(a) / cos(a))}[name]
    return ("num", simplify(1 / b))


# (given side, given angle, asked side) for the two special triangles
_SPECIAL_SIDES = [
    (6, 30, "hypotenuse"), (4, 60, "hypotenuse"), (5, 45, "hypotenuse"),
    (8, 30, "other leg"), (9, 60, "other leg"), (7, 45, "other leg"),
    (10, 30, "hypotenuse"), (12, 60, "other leg"), (3, 45, "hypotenuse"),
    (14, 30, "other leg"), (11, 60, "hypotenuse"), (2, 45, "other leg"),
]


def build2_special_sides():
    variants = []
    for i, (leg, ang, asked) in enumerate(_SPECIAL_SIDES):
        a = rad(ang)
        # `leg` is opposite the given angle; the other leg is opposite 90-ang
        hyp = simplify(leg / sin(a))
        other = simplify(hyp * cos(a))
        val = hyp if asked == "hypotenuse" else other
        cands = [(surd_kat(other if asked == "hypotenuse" else hyp),
                  other if asked == "hypotenuse" else hyp),
                 (surd_kat(leg), Integer(leg)),
                 (surd_kat(2 * leg), Integer(2 * leg)),
                 (surd_kat(leg * sqrt(3)), leg * sqrt(3)),
                 (surd_kat(val + 1), val + 1), (surd_kat(2 * val), 2 * val)]
        opts, ci = place(surd_kat(val), pick_numeric(val, cands), i)
        variants.append({
            "id": "TRIG-spside-v%02d" % (i + 1),
            "statement": ("A right triangle has an angle of $%d°$, and the "
                          "side opposite that angle is $%d$. Find the %s, "
                          "exactly." % (ang, leg, asked)),
            "options": opts, "correctIndex": ci,
            "explanation": ("The special triangles fix every ratio: a "
                            "$30$–$60$–$90$ has sides $x$, $x\\sqrt3$, $2x$, "
                            "and a $45$–$45$–$90$ has $x$, $x$, "
                            "$x\\sqrt2$. Scaling that pattern so the side "
                            "opposite $%d°$ is $%d$ makes the %s $%s$."
                            % (ang, leg, asked, surd_kat(val).strip("$"))),
            "check": ["Eq(sin(rad(%d)) * (%s), %d)" % (ang, str(hyp), leg)],
        })
    return variants


def _resolve_special_sides(s):
    leg = int(re.search(r"opposite that angle is \$(\d+)\$", s).group(1))
    ang = int(re.search(r"angle of \$(\d+)°\$", s).group(1))
    a = rad(ang)
    hyp = simplify(leg / sin(a))
    return ("num", hyp if "the hypotenuse" in s else simplify(hyp * cos(a)))

# --- radians-and-the-unit-circle -------------------------------------------
# (radius, p, q) for a central angle of p*pi/q radians, chosen so the sector
# area (1/2) r^2 theta is an exact multiple of pi
_SECTOR = [(6, 1, 3), (4, 1, 2), (6, 2, 3), (8, 1, 4), (10, 1, 5),
           (12, 1, 6), (2, 1, 2), (4, 3, 4), (10, 2, 5), (6, 5, 6),
           (8, 3, 8), (12, 5, 6)]


def build2_sector_area():
    variants = []
    for i, (r, p, q) in enumerate(_SECTOR):
        theta = Rational(p, q)                 # multiples of pi
        k = Rational(r * r, 2) * theta         # coefficient of pi in the area
        arc = Rational(r) * theta              # coefficient of pi in the arc
        cands = [(pi_kat(2 * k), 2 * k * pi), (pi_kat(arc), arc * pi),
                 (pi_kat(Rational(r * r) * theta),
                  Rational(r * r) * theta * pi),
                 (pi_kat(k + 1), (k + 1) * pi), (pi_kat(k + 2), (k + 2) * pi),
                 (pi_kat(k + 3), (k + 3) * pi)]
        opts, ci = place(pi_kat(k), pick_numeric(k * pi, cands), i)
        variants.append({
            "id": "TRIG-sect-v%02d" % (i + 1),
            "statement": ("A sector of a circle of radius $%d$ has central "
                          "angle $%s$ radians. Find its area, exactly."
                          % (r, pi_kat(theta).strip("$"))),
            "options": opts, "correctIndex": ci,
            "explanation": ("In radians the sector area is "
                            "$\\tfrac12 r^2\\theta = \\tfrac12 \\cdot %d "
                            "\\cdot %s = %s$. Dropping the $\\tfrac12$ gives "
                            "$%s$, and the arc length $%s$ answers a "
                            "different question — one is a length, the other "
                            "an area."
                            % (r * r, pi_kat(theta).strip("$"),
                               pi_kat(k).strip("$"),
                               pi_kat(Rational(r * r) * theta).strip("$"),
                               pi_kat(arc).strip("$"))),
            "check": ["Rational(1,2)*%d**2*Rational(%d, %d) == Rational(%d, %d)"
                      % (r, p, q, k.p, k.q)],
        })
    return variants


def _resolve_sector_area(s):
    r = int(re.search(r"radius \$(\d+)\$", s).group(1))
    m = re.search(r"angle \$(?:\\dfrac\{(\d+)?\\pi\}\{(\d+)\}|(\d+)?\\pi)\$",
                  s)
    if m.group(2):
        theta = Rational(int(m.group(1) or 1), int(m.group(2)))
    else:
        theta = Rational(int(m.group(3) or 1))
    return ("num", Rational(r * r, 2) * theta * pi)


# Angles as p*pi/q. The quadrant is COMPUTED below rather than tabled — the
# first draft tabled it and put 2*pi/3 in quadrant 1, which the blind
# re-solve caught.
_QUADRANT_OF = [(1, 6), (2, 3), (3, 4), (5, 6), (7, 6), (5, 4),
                (4, 3), (5, 3), (7, 4), (11, 6), (1, 3), (9, 4)]


def build2_angle_quadrant():
    variants = []
    seen = set()
    for p, q in _QUADRANT_OF:
        kat = pi_kat(Rational(p, q))
        if kat in seen:
            continue
        seen.add(kat)
        deg = Rational(180 * p, q) % 360
        assert deg % 90 != 0, ("on an axis, so in no quadrant", p, q)
        quad = 1 if deg < 90 else (2 if deg < 180 else (3 if deg < 270
                                                        else 4))
        i = len(variants)
        correct = "quadrant $%d$" % quad
        wrongs = ["quadrant $%d$" % w for w in (1, 2, 3, 4) if w != quad]
        opts, ci = _txt_place(correct, wrongs, i)
        variants.append({
            "id": "TRIG-quad-v%02d" % (i + 1),
            "statement": ("In which quadrant does an angle of $%s$ radians "
                          "lie?" % kat.strip("$")),
            "options": opts, "correctIndex": ci,
            "explanation": ("Measure against the quarter-turns "
                            "$\\tfrac{\\pi}{2}$, $\\pi$, "
                            "$\\tfrac{3\\pi}{2}$ and $2\\pi$. In degrees "
                            "the angle is $%s°$, which sits in quadrant "
                            "$%d$. Converting first is always allowed and "
                            "usually quicker than comparing fractions of "
                            "$\\pi$." % (deg, quad)),
            "check": ["Rational(180 * %d, %d) %% 360 == %s"
                      % (p, q, str(deg))],
        })
    assert len(variants) >= 12, len(variants)
    return variants


def _resolve_angle_quadrant(s):
    m = re.search(r"angle of \$(?:\\dfrac\{(\d+)?\\pi\}\{(\d+)\}|(\d+)?\\pi)"
                  r"\$ radians", s)
    theta = (Rational(int(m.group(1) or 1), int(m.group(2))) if m.group(2)
             else Rational(int(m.group(3) or 1)))
    deg = (180 * theta) % 360        # angles past a full turn reduce first
    quad = 1 if deg < 90 else (2 if deg < 180 else (3 if deg < 270 else 4))
    return ("opt", "quadrant $%d$" % quad)


# --- graphs-of-trig-functions ----------------------------------------------
_PERIOD_TO_B = [(180, 2), (90, 4), (120, 3), (60, 6), (45, 8), (720, 1),
                (36, 10), (30, 12), (72, 5), (24, 15), (240, 1), (144, 1)]


def build2_b_from_period():
    variants = []
    seen = set()
    for period, _b in _PERIOD_TO_B:
        if period in seen:
            continue
        seen.add(period)
        i = len(variants)
        b = Rational(360, period)
        cands = [(surd_kat(period), Integer(period)),
                 (surd_kat(Rational(period, 360)), Rational(period, 360)),
                 (surd_kat(2 * b), 2 * b), (surd_kat(b + 1), b + 1),
                 (surd_kat(b + 2), b + 2)]
        opts, ci = place(surd_kat(b), pick_numeric(b, cands), i)
        variants.append({
            "id": "TRIG-bper-v%02d" % (i + 1),
            "statement": ("The graph of $y = \\sin(Bx)$ has period $%d°$. "
                          "Find $B$." % period),
            "options": opts, "correctIndex": ci,
            "explanation": ("The period of $\\sin(Bx)$ is "
                            "$\\dfrac{360°}{B}$, so $B = \\dfrac{360}{%d} = "
                            "%s$. A period SHORTER than $360°$ needs "
                            "$B > 1$ — squeezing the graph — which rules out "
                            "the small options immediately."
                            % (period, surd_kat(b).strip("$"))),
            "check": ["Rational(360, %d) == Rational(%d, %d)"
                      % (period, b.p, b.q)],
        })
    assert len(variants) >= 10, len(variants)
    return variants


def _resolve_b_from_period(s):
    return ("num", Rational(360, int(re.search(r"period \$(\d+)°\$",
                                               s).group(1))))


_TAN_ASYMPTOTE = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18]


def build2_tan_asymptotes():
    variants = []
    for i, b in enumerate(_TAN_ASYMPTOTE):
        gap = Rational(180, b)
        cands = [(surd_kat(2 * gap), 2 * gap), (surd_kat(Rational(360, b)),
                                                Rational(360, b)),
                 (surd_kat(Rational(90, b)), Rational(90, b)),
                 (surd_kat(gap + 1), gap + 1), (surd_kat(gap + 2), gap + 2),
                 (surd_kat(gap + 3), gap + 3)]
        opts, ci = place(surd_kat(gap), pick_numeric(gap, cands), i)
        variants.append({
            "id": "TRIG-tasym-v%02d" % (i + 1),
            "statement": ("How many degrees apart are consecutive vertical "
                          "asymptotes of $y = \\tan(%dx)$?" % b),
            "options": opts, "correctIndex": ci,
            "explanation": ("Tangent blows up every $180°$ of its ARGUMENT, "
                            "and the argument here runs $%d$ times as fast "
                            "as $x$, so in $x$ the asymptotes come every "
                            "$\\dfrac{180°}{%d} = %s°$. Using $360$ instead "
                            "of $180$ is the sine-and-cosine habit — "
                            "tangent's period is half theirs."
                            % (b, b, surd_kat(gap).strip("$"))),
            "check": ["Rational(180, %d) == Rational(%d, %d)"
                      % (b, gap.p, gap.q)],
        })
    return variants


def _resolve_tan_asymptotes(s):
    return ("num", Rational(180, int(re.search(r"\\tan\((\d+)x\)",
                                               s).group(1))))


# --- identities-and-equations ----------------------------------------------
# (KaTeX value, sympy source, the two solutions of cos x = value on [0, 360))
_COS_SOLUTIONS = [
    ("\\frac{1}{2}", "Rational(1,2)", 60, 300),
    ("\\frac{\\sqrt{2}}{2}", "sqrt(2)/2", 45, 315),
    ("\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", 30, 330),
    ("-\\frac{1}{2}", "-Rational(1,2)", 120, 240),
    ("-\\frac{\\sqrt{2}}{2}", "-sqrt(2)/2", 135, 225),
    ("-\\frac{\\sqrt{3}}{2}", "-sqrt(3)/2", 150, 210),
    ("0", "0", 90, 270),
    ("1", "1", 0, 0),
    ("-1", "-1", 180, 180),
    ("\\frac{1}{2}", "Rational(1,2)", 60, 300),
    ("-\\frac{1}{2}", "-Rational(1,2)", 120, 240),
    ("\\frac{\\sqrt{3}}{2}", "sqrt(3)/2", 30, 330),
]


def build2_solve_cos():
    variants, seen = [], set()
    for kat, src, p, q in _COS_SOLUTIONS:
        if kat in seen:
            continue
        seen.add(kat)
        i = len(variants)
        correct = ("$x = %d°$ only" % p if p == q
                   else "$x = %d°$ and $x = %d°$" % (p, q))
        # A pool, filtered against the answer: at cos x = 0 the pair
        # (p, p + 180) IS the answer, so a fixed distractor list collides.
        pool = ["$x = %d°$ only" % p,
                "$x = %d°$ and $x = %d°$" % (p, (p + 180) % 360),
                "$x = %d°$ and $x = %d°$" % ((p + 90) % 360,
                                             (q + 90) % 360),
                "$x = %d°$ and $x = %d°$" % ((180 - p) % 360, q),
                "there is no solution",
                "every $x$ in the interval"]
        wrongs, seen = [], {correct}
        for w in pool:
            if w not in seen:
                seen.add(w)
                wrongs.append(w)
            if len(wrongs) == 3:
                break
        assert len(wrongs) == 3, (correct, pool)
        opts, ci = _txt_place(correct, wrongs, i)
        variants.append({
            "id": "TRIG-scos-v%02d" % (i + 1),
            "statement": ("Solve $\\cos x = %s$ for $0° \\le x < 360°$."
                          % kat),
            "options": opts, "correctIndex": ci,
            "explanation": ("Cosine is the $x$-coordinate on the unit "
                            "circle, and it takes each value strictly "
                            "between $-1$ and $1$ twice per turn — once "
                            "above the axis and once below, symmetric about "
                            "$0°$. Here that gives %s. At $\\pm 1$ the two "
                            "solutions collide into one."
                            % ("$x = %d°$ alone" % p if p == q
                               else "$x = %d°$ and $x = %d°$" % (p, q))),
            "check": ["Eq(cos(rad(%d)), %s)" % (p, src),
                      "Eq(cos(rad(%d)), %s)" % (q, src)],
        })
    assert len(variants) >= 8, len(variants)
    return variants


def _resolve_solve_cos(s):
    kat = re.search(r"\\cos x = (.+?)\$ for", s).group(1)
    for k, _src, p, q in _COS_SOLUTIONS:
        if k == kat:
            return ("opt", "$x = %d°$ only" % p if p == q
                    else "$x = %d°$ and $x = %d°$" % (p, q))
    raise ValueError("solve-cos: unknown value %r" % kat)


# --- laws-of-sines-and-cosines ---------------------------------------------
# (side a, angle A in degrees, side b): A has an exact rational sine, so
# sin B = b·sin A / a comes out exact for any integer sides.
_SINE_ANGLE = [(10, 30, 14), (8, 30, 6), (12, 30, 18), (5, 150, 4),
               (20, 30, 25), (9, 90, 6), (16, 30, 20), (6, 150, 5),
               (15, 90, 12), (14, 30, 21), (25, 30, 30), (18, 150, 15)]


def build2_law_of_sines_angle():
    variants = []
    for i, (a, A, b) in enumerate(_SINE_ANGLE):
        sa = simplify(sin(rad(A)))
        ans = simplify(b * sa / a)
        assert ans < 1, (a, A, b)
        cands = [(surd_kat(simplify(a * sa / b)), simplify(a * sa / b)),
                 (surd_kat(Rational(b, a)), Rational(b, a)),
                 (surd_kat(simplify(b * sa)), simplify(b * sa)),
                 (surd_kat(simplify(ans / 2)), simplify(ans / 2)),
                 (surd_kat(simplify(2 * ans)), simplify(2 * ans))]
        opts, ci = place(surd_kat(ans), pick_numeric(ans, cands), i)
        variants.append({
            "id": "TRIG-lsang-v%02d" % (i + 1),
            "statement": ("In a triangle, $a = %d$, $A = %d°$ and $b = %d$. "
                          "Find $\\sin B$, exactly." % (a, A, b)),
            "options": opts, "correctIndex": ci,
            "explanation": ("The law of sines says "
                            "$\\dfrac{\\sin A}{a} = \\dfrac{\\sin B}{b}$, "
                            "so $\\sin B = \\dfrac{b \\sin A}{a} = "
                            "\\dfrac{%d \\cdot %s}{%d} = %s$. Each side "
                            "pairs with the angle OPPOSITE it — pairing $b$ "
                            "with $A$ instead inverts the ratio."
                            % (b, surd_kat(sa).strip("$"), a,
                               surd_kat(ans).strip("$"))),
            "check": ["Eq(sin(rad(%d))/%d, (%s)/%d)"
                      % (A, a, str(ans), b)],
        })
    return variants


def _resolve_law_of_sines_angle(s):
    a, A, b = [int(x) for x in
               re.search(r"\$a = (\d+)\$, \$A = (\d+)°\$ and \$b = (\d+)\$",
                         s).groups()]
    return ("num", simplify(b * sin(rad(A)) / a))


# (side a, angle A, side b): 0, 1 or 2 triangles
_AMBIGUOUS = [
    (5, 30, 12, "no triangle"), (10, 30, 20, "exactly one triangle"),
    (12, 30, 20, "two triangles"), (6, 30, 15, "no triangle"),
    (9, 30, 18, "exactly one triangle"), (15, 30, 20, "two triangles"),
    (4, 30, 10, "no triangle"), (7, 30, 14, "exactly one triangle"),
    (11, 30, 16, "two triangles"), (3, 30, 8, "no triangle"),
    (8, 30, 16, "exactly one triangle"), (13, 30, 18, "two triangles"),
]


def build2_ambiguous_case():
    variants = []
    for i, (a, A, b, ans) in enumerate(_AMBIGUOUS):
        h = Rational(b, 2)          # b*sin(30°)
        if ans == "no triangle":
            assert a < h, (a, b)
        elif ans == "exactly one triangle":
            assert a == h or a >= b, (a, b)
        else:
            assert h < a < b, (a, b)
        wrongs = [w for w in ("no triangle", "exactly one triangle",
                              "two triangles") if w != ans]
        wrongs.append("infinitely many triangles")
        opts, ci = _txt_place(ans, wrongs, i)
        variants.append({
            "id": "TRIG-ambig-v%02d" % (i + 1),
            "statement": ("You are given $a = %d$, $A = %d°$ and $b = %d$ "
                          "— two sides and an angle NOT between them. How "
                          "many triangles fit?" % (a, A, b)),
            "options": opts, "correctIndex": ci,
            "explanation": ("Swing side $a$ from the end of $b$ and see how "
                            "often it reaches the base. The shortest it can "
                            "be and still reach is the height "
                            "$b \\sin A = %s$. Here $a = %d$, so there is "
                            "%s. Below the height nothing reaches; between "
                            "the height and $b$ it reaches twice; at or "
                            "beyond $b$ exactly once."
                            % (surd_kat(h).strip("$"), a, ans)),
            "check": ["Rational(%d, 1)*sin(rad(%d)) == Rational(%d, %d)"
                      % (b, A, h.p, h.q)],
        })
    return variants


def _resolve_ambiguous_case(s):
    a, A, b = [int(x) for x in
               re.search(r"\$a = (\d+)\$, \$A = (\d+)°\$ and \$b = (\d+)\$",
                         s).groups()]
    h = b * sin(rad(A))
    if a < h:
        return ("opt", "no triangle")
    if a >= b or a == h:
        return ("opt", "exactly one triangle")
    return ("opt", "two triangles")


_BATCH2_META = [
    ("ratio-choice", "Choosing sine, cosine or tangent", 1,
     "SOH-CAH-TOA names each pairing once — match the two known sides.",
     "right-triangle-trigonometry", build2_ratio_choice,
     _resolve_ratio_choice),
    ("hypotenuse-from-angle", "The hypotenuse from a side and an angle", 2,
     "Divide by the sine, never multiply — the hypotenuse is the longest "
     "side.",
     "right-triangle-trigonometry", build2_hypotenuse, _resolve_hypotenuse),
    ("quadrant-signs", "Signs by quadrant", 1,
     "Cosine follows x, sine follows y, tangent is their quotient.",
     "special-triangles-and-exact-values", build2_quadrant_signs,
     _resolve_quadrant_signs),
    ("reciprocal-ratios", "Cosecant, secant and cotangent", 2,
     "Evaluate the base ratio first, then flip it.",
     "special-triangles-and-exact-values", build2_reciprocals,
     _resolve_reciprocals),
    ("special-triangle-sides", "Sides of the special triangles", 1,
     "x : x√3 : 2x and x : x : x√2 — scale the pattern to the given side.",
     "special-triangles-and-exact-values", build2_special_sides,
     _resolve_special_sides),
    ("sector-area-radians", "Sector area in radians", 2,
     "½r²θ with θ in radians — the ½ is the difference between area and "
     "arc.",
     "radians-and-the-unit-circle", build2_sector_area, _resolve_sector_area),
    ("angle-quadrant", "Which quadrant, in radians", 1,
     "Compare against π/2, π and 3π/2 — or just convert to degrees.",
     "radians-and-the-unit-circle", build2_angle_quadrant,
     _resolve_angle_quadrant),
    ("b-from-period", "Finding B from the period", 2,
     "B = 360°/period — a shorter period needs a bigger B.",
     "graphs-of-trig-functions", build2_b_from_period, _resolve_b_from_period),
    ("tan-asymptotes", "Asymptotes of the tangent graph", 2,
     "Tangent repeats every 180°, half the period of sine and cosine.",
     "graphs-of-trig-functions", build2_tan_asymptotes,
     _resolve_tan_asymptotes),
    ("solve-cos", "Solving cos x = k on one turn", 2,
     "Two solutions per turn, symmetric about 0° — one above the axis and "
     "one below.",
     "identities-and-equations", build2_solve_cos, _resolve_solve_cos),
    ("law-of-sines-angle", "The law of sines for a sine", 2,
     "sin B = b·sin A / a — each side pairs with the angle opposite it.",
     "laws-of-sines-and-cosines", build2_law_of_sines_angle,
     _resolve_law_of_sines_angle),
    ("ambiguous-case", "How many triangles fit", 3,
     "Compare the swinging side with the height b·sin A: below it none, "
     "between it and b two, at or beyond b one.",
     "laws-of-sines-and-cosines", build2_ambiguous_case,
     _resolve_ambiguous_case),
]


_BATCH1_FORMS = new_forms


def new_forms():  # noqa: F811 — appends batch 2 to the original list
    """All unit-specific forms: the original set plus batch 2 above."""
    return _BATCH1_FORMS() + [
        {"id": fid, "title": title, "level": level, "skill": skill,
         "unit": unit, "variants": gen()}
        for fid, title, level, skill, unit, gen, _rz in _BATCH2_META]


RESOLVERS.update({fid: rz for fid, _t, _l, _s, _u, _g, rz in _BATCH2_META})


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
