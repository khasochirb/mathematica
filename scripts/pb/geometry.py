# -*- coding: utf-8 -*-
"""Problem-bank generator for the ЭЕШ 'Geometry' topic.

Exposes build() returning ~36 machine-verified variants for each of 8 forms.
Every 'check' string sympifies to boolean True; every variant has exactly 4
distinct options with the correct answer numerically distinct from the
distractors. Run `python3 scripts/pb/geometry.py` for the self-check.
"""

from math import gcd, isqrt
from sympy import sympify, simplify, sqrt, pi, Rational

SLUG = "geometry"
TITLE = "Geometry"
TITLE_MN = "Геометр"
BLURB = ("From Pythagoras to sectors, similarity, and 3D volumes — "
         "the figures the exam always draws.")


# ---------------------------------------------------------------------------
# formatting helpers
# ---------------------------------------------------------------------------

def L(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = sympify(v)
    if getattr(v, "q", 1) == 1:
        return str(v.p if hasattr(v, "p") else int(v))
    if v < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def intL(v):
    return str(int(v))


def piL(k):
    """LaTeX for k*pi."""
    k = sympify(k)
    if k == 0:
        return "0"
    if k == 1:
        return "\\pi"
    if k == -1:
        return "-\\pi"
    return L(k) + "\\pi"


def surd(coef, base):
    """LaTeX for coef*sqrt(base) with integer coef>=1."""
    coef = int(coef)
    if coef == 1:
        return "\\sqrt{%d}" % base
    return "%d\\sqrt{%d}" % (coef, base)


# ---------------------------------------------------------------------------
# option assembly
# ---------------------------------------------------------------------------

def build_latex_options(correct, cands, pos, latex_of=None):
    """correct = (latex, value); cands = list of (latex, value).

    Returns (options[4] wrapped in $...$, correctIndex=pos). Guarantees the
    three chosen distractors are numerically distinct from the correct answer
    and from each other, and have distinct latex.
    """
    clat, cval = correct[0], sympify(correct[1])
    chosen = []  # list of (latex, value)
    for lat, val in cands:
        v = sympify(val)
        if simplify(v - cval) == 0:
            continue
        if lat == clat or any(lat == l for l, _ in chosen):
            continue
        if any(simplify(v - cv) == 0 for _, cv in chosen):
            continue
        chosen.append((lat, v))
        if len(chosen) == 3:
            break
    k = 1
    while len(chosen) < 3 and latex_of is not None:
        for cand in (cval + k, cval - k):
            lat = latex_of(cand)
            if simplify(cand - cval) == 0:
                continue
            if lat == clat or any(lat == l for l, _ in chosen):
                continue
            if any(simplify(cand - cv) == 0 for _, cv in chosen):
                continue
            chosen.append((lat, cand))
            if len(chosen) == 3:
                break
        k += 1
        if k > 60:
            break
    assert len(chosen) == 3, "could not build 3 distractors for %s" % clat
    final = [l for l, _ in chosen]
    final.insert(pos, clat)
    return ["$" + s + "$" for s in final], pos


# ---------------------------------------------------------------------------
# per-form generators.  Each returns a list of variant dicts (without id).
# ---------------------------------------------------------------------------

def gen_pythagoras():
    # collect Pythagorean triples (a odd-ish leg, b even leg, c hyp)
    seen = set()
    triples = []
    for m in range(2, 10):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                a0 = m * m - n * n
                b0 = 2 * m * n
                c0 = m * m + n * n
                for mult in (1, 2, 3):
                    a, b, c = a0 * mult, b0 * mult, c0 * mult
                    key = (min(a, b), max(a, b))
                    if key in seen:
                        continue
                    seen.add(key)
                    triples.append((a, b, c))
    triples.sort(key=lambda t: (t[2], t[0]))
    triples = triples[:36]

    out = []
    for i, (a, b, c) in enumerate(triples):
        pos = i % 4
        correct = (intL(c), c)
        cands = [(intL(a + b), a + b), (intL(c + 1), c + 1),
                 (intL(c - 1), c - 1), (intL(abs(b - a)), abs(b - a))]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=intL)
        scale = 6.0 / max(a, b)
        bx = round(a * scale, 4)
        cy = round(b * scale, 4)
        fig = {
            "points": [
                {"id": "A", "x": 0, "y": 0, "labelDx": -8, "labelDy": 8},
                {"id": "B", "x": bx, "y": 0, "labelDx": 10, "labelDy": 8},
                {"id": "C", "x": bx, "y": cy, "labelDx": 10, "labelDy": -4},
            ],
            "objects": [
                {"kind": "segment", "from": "A", "to": "B", "label": str(a)},
                {"kind": "segment", "from": "B", "to": "C", "label": str(b),
                 "color": "blue"},
                {"kind": "segment", "from": "A", "to": "C", "label": "?",
                 "color": "accent"},
                {"kind": "angle", "at": "B", "from": "A", "to": "C",
                 "right": True},
            ],
        }
        out.append({
            "statement": "A right triangle has legs $%d$ and $%d$. Find the "
                         "hypotenuse." % (a, b),
            "options": opts, "correctIndex": ci,
            "explanation": "$c = \\sqrt{%d^2 + %d^2} = \\sqrt{%d + %d} = "
                           "\\sqrt{%d} = %d$ — the %d-%d-%d triple."
                           % (a, b, a * a, b * b, c * c, c, a, b, c),
            "check": ["sqrt(%d**2 + %d**2) == %d" % (a, b, c)],
            "geoFigure": fig,
        })
    return out


def gen_triangle_area():
    pairs = []
    for base in range(3, 22):
        for h in range(2, 14):
            if (base * h) % 2 == 0:
                pairs.append((base, h, base * h // 2))
    # spread across the range for size variety
    step = max(1, len(pairs) // 36)
    picked, used = [], set()
    for j in range(0, len(pairs), step):
        b, h, ar = pairs[j]
        if (b, h) in used:
            continue
        used.add((b, h))
        picked.append(pairs[j])
        if len(picked) == 36:
            break
    for b, h, ar in pairs:
        if len(picked) == 36:
            break
        if (b, h) not in used:
            used.add((b, h))
            picked.append((b, h, ar))

    out = []
    for i, (b, h, ar) in enumerate(picked):
        pos = i % 4
        correct = (intL(ar), ar)
        cands = [(intL(b * h), b * h), (intL(b + h), b + h),
                 (intL(ar + h), ar + h), (intL(ar + b), ar + b)]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=intL)
        # True-to-scale triangle: apex over 0.38·base, dashed height with a
        # right-angle mark at its foot. World units = the actual lengths.
        fx = round(0.38 * b, 4)
        fig = {
            "points": [
                {"id": "A", "x": 0, "y": 0, "label": ""},
                {"id": "B", "x": b, "y": 0, "label": ""},
                {"id": "T", "x": fx, "y": h, "label": ""},
                {"id": "F", "x": fx, "y": 0, "label": ""},
            ],
            "objects": [
                {"kind": "segment", "from": "A", "to": "B", "label": str(b)},
                {"kind": "segment", "from": "A", "to": "T"},
                {"kind": "segment", "from": "B", "to": "T"},
                {"kind": "segment", "from": "F", "to": "T", "label": str(h),
                 "color": "blue", "dashed": True},
                {"kind": "angle", "at": "F", "from": "B", "to": "T",
                 "right": True},
            ],
        }
        out.append({
            "statement": "A triangle has base $%d$ and height $%d$. Find its "
                         "area." % (b, h),
            "options": opts, "correctIndex": ci,
            "explanation": "$A = \\tfrac{1}{2}bh = \\tfrac{1}{2}\\cdot %d \\cdot "
                           "%d = %d$. Dropping the $\\tfrac12$ gives the "
                           "rectangle $%d$." % (b, h, ar, b * h),
            "check": ["Rational(1,2)*%d*%d == %d" % (b, h, ar)],
            "geoFigure": fig,
        })
    return out


def gen_circle_basics():
    items = []
    # area from radius
    for r in range(2, 13):
        items.append(("ar", r, r * r,
                      [(2 * r), (r), (2 * r * r), (r * r + r), (r * r - r)]))
    # circumference from radius
    for r in range(2, 13):
        items.append(("cr", r, 2 * r,
                      [(r * r), (r), (4 * r), (r + 1), (2 * r + 2)]))
    # area from diameter (even d)
    for d in range(4, 26, 2):
        items.append(("ad", d, d * d // 4,
                      [(d * d), (d * d // 2), (d), (2 * d), (d * d // 4 + d)]))
    # circumference from diameter
    for d in range(3, 16):
        items.append(("cd", d, d,
                      [(2 * d), (d * d // 4 if d % 2 == 0 else d * d),
                       (d * d), (d + 2), (d + 1)]))

    step = max(1, len(items) // 36)
    picked, used = [], set()
    for j in range(0, len(items), step):
        key = (items[j][0], items[j][1])
        if key in used:
            continue
        used.add(key)
        picked.append(items[j])
        if len(picked) == 36:
            break
    for it in items:
        if len(picked) == 36:
            break
        key = (it[0], it[1])
        if key not in used:
            used.add(key)
            picked.append(it)

    out = []
    for i, (kind, val, k, distk) in enumerate(picked[:36]):
        pos = i % 4
        correct = (piL(k), k * pi)
        cands = [(piL(d), d * pi) for d in distk]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=piL)
        if kind == "ar":
            st = "A circle has radius $%d$. Find its area, exactly." % val
            ex = ("$A = \\pi r^2 = \\pi\\cdot %d^2 = %s$. "
                  "($2\\pi r = %s$ is the circumference, not the area.)"
                  % (val, piL(k), piL(2 * val)))
            chk = "pi*%d**2 == %s*pi" % (val, k)
        elif kind == "cr":
            st = "A circle has radius $%d$. Find its circumference, exactly." % val
            ex = ("$C = 2\\pi r = 2\\pi\\cdot %d = %s$. "
                  "($\\pi r^2 = %s$ is the area, not the length.)"
                  % (val, piL(k), piL(val * val)))
            chk = "2*pi*%d == %s*pi" % (val, k)
        elif kind == "ad":
            st = "A circle has diameter $%d$. Find its area, exactly." % val
            ex = ("Radius is half the diameter: $r = %d$, so "
                  "$A = \\pi r^2 = %s$. Using the diameter as the radius "
                  "gives $%s$." % (val // 2, piL(k), piL(val * val)))
            chk = "pi*(%d/2)**2 == %s*pi" % (val, k)
        else:  # cd
            st = ("A circle has diameter $%d$. Find its circumference, "
                  "exactly." % val)
            ex = ("$C = \\pi d = %s$. "
                  "Doubling to $%s$ double-counts the radius." % (piL(k),
                                                                  piL(2 * val)))
            chk = "2*pi*Rational(%d,2) == %s*pi" % (val, k)
        out.append({"statement": st, "options": opts, "correctIndex": ci,
                    "explanation": ex, "check": [chk]})
    return out


def rt_fig(w, hgt, lab_bottom, lab_left, lab_hyp, ang_at, ang_label,
           tick_legs=False):
    """Right triangle drawn true to scale: right angle at the origin,
    horizontal leg w, vertical leg hgt. Side labels may be None; the '?' side
    is drawn in the accent color. ang_at ('B'|'C') carries the acute-angle
    label (the drawn angle really is that size)."""
    def seg(frm, to, lab):
        o = {"kind": "segment", "from": frm, "to": to}
        if lab is not None:
            o["label"] = lab
            if lab == "?":
                o["color"] = "accent"
        if tick_legs and frm == "A":  # both legs leave the right-angle vertex
            o["ticks"] = 1
        return o
    objs = [
        seg("A", "B", lab_bottom),
        seg("A", "C", lab_left),
        seg("B", "C", lab_hyp),
        {"kind": "angle", "at": "A", "from": "B", "to": "C", "right": True},
        {"kind": "angle", "at": ang_at,
         "from": "A" if ang_at == "B" else "A",
         "to": "C" if ang_at == "B" else "B",
         "label": ang_label},
    ]
    return {
        "points": [
            {"id": "A", "x": 0, "y": 0, "label": ""},
            {"id": "B", "x": round(w, 4), "y": 0, "label": ""},
            {"id": "C", "x": 0, "y": round(hgt, 4), "label": ""},
        ],
        "objects": objs,
    }


def gen_special_triangles():
    bases = [3, 4, 5, 6, 7, 8]
    out = []
    idx = 0
    SQ3 = 3 ** 0.5

    def emit(st, correct, cands, ex, chk, fig=None):
        nonlocal idx
        pos = idx % 4
        opts, ci = build_latex_options(correct, cands, pos)
        v = {"statement": st, "options": opts, "correctIndex": ci,
             "explanation": ex, "check": [chk]}
        if fig is not None:
            v["geoFigure"] = fig
        out.append(v)
        idx += 1

    # template 1: 45-45-90, legs x -> hypotenuse x*sqrt(2)
    for x in bases:
        emit("A 45-45-90 triangle has legs $%d$. Find the hypotenuse." % x,
             (surd(x, 2), x * sqrt(2)),
             [(intL(x), x), (intL(2 * x), 2 * x), (surd(x, 3), x * sqrt(3))],
             "In a 45-45-90 triangle the hypotenuse is a leg times $\\sqrt2$: "
             "$%d\\sqrt2 = %s$." % (x, surd(x, 2)),
             "sqrt(2*%d**2) == %d*sqrt(2)" % (x, x),
             rt_fig(x, x, str(x), str(x), "?", "B", "45°"))
    # template 2: 30-60-90, short leg x -> long leg x*sqrt(3)
    for x in bases:
        emit("In a 30-60-90 triangle the shorter leg (opposite $30°$) is $%d$. "
             "Find the longer leg." % x,
             (surd(x, 3), x * sqrt(3)),
             [(surd(x, 2), x * sqrt(2)), (intL(2 * x), 2 * x), (intL(x), x)],
             "The longer leg is the shorter leg times $\\sqrt3$: "
             "$%d\\sqrt3 = %s$." % (x, surd(x, 3)),
             "sqrt((2*%d)**2 - %d**2) == %d*sqrt(3)" % (x, x, x),
             rt_fig(x * SQ3, x, "?", str(x), None, "B", "30°"))
    # template 3: 30-60-90, short leg x -> hypotenuse 2x
    for x in bases:
        emit("In a 30-60-90 triangle the shorter leg (opposite $30°$) is $%d$. "
             "Find the hypotenuse." % x,
             (intL(2 * x), 2 * x),
             [(surd(x, 3), x * sqrt(3)), (intL(x), x), (surd(x, 2), x * sqrt(2))],
             "The hypotenuse is twice the shorter leg: $2\\cdot %d = %d$."
             % (x, 2 * x),
             "%d/sin(rad(30)) == 2*%d" % (x, x),
             rt_fig(x * SQ3, x, None, str(x), "?", "B", "30°"))
    # template 4: 30-60-90, hypotenuse H=2x -> shorter leg x
    for x in bases:
        H = 2 * x
        emit("In a 30-60-90 triangle the hypotenuse is $%d$. Find the shorter "
             "leg (opposite $30°$)." % H,
             (intL(x), x),
             [(intL(H), H), (surd(x, 3), x * sqrt(3)), (surd(x, 2), x * sqrt(2))],
             "The shorter leg is half the hypotenuse: $\\tfrac{%d}{2} = %d$."
             % (H, x),
             "%d*sin(rad(30)) == %d" % (H, x),
             rt_fig(x * SQ3, x, None, "?", str(H), "B", "30°"))
    # template 5: 30-60-90, hypotenuse H=2x -> longer leg x*sqrt(3)
    for x in bases:
        H = 2 * x
        emit("In a 30-60-90 triangle the hypotenuse is $%d$. Find the longer "
             "leg (opposite $60°$)." % H,
             (surd(x, 3), x * sqrt(3)),
             [(intL(x), x), (intL(H), H), (surd(x, 2), x * sqrt(2))],
             "Longer leg $= \\tfrac{H}{2}\\sqrt3 = %d\\sqrt3 = %s$."
             % (x, surd(x, 3)),
             "%d*sin(rad(60)) == %d*sqrt(3)" % (H, x),
             rt_fig(x * SQ3, x, "?", None, str(H), "C", "60°"))
    # template 6: 45-45-90, hypotenuse n*sqrt(2) -> leg n
    for n in bases:
        emit("A 45-45-90 triangle has hypotenuse $%s$. Find each leg."
             % surd(n, 2),
             (intL(n), n),
             [(surd(n, 2), n * sqrt(2)), (intL(2 * n), 2 * n),
              (surd(n, 3), n * sqrt(3))],
             "Each leg is the hypotenuse over $\\sqrt2$: "
             "$\\tfrac{%d\\sqrt2}{\\sqrt2} = %d$." % (n, n),
             "%d*sqrt(2)*sin(rad(45)) == %d" % (n, n),
             rt_fig(n, n, "?", None, "%d√2" % n, "B", "45°",
                    tick_legs=True))
    return out


def gen_sector_area():
    angles = [30, 45, 60, 90, 120, 135, 150, 180, 270]
    items = []
    for ang in angles:
        for r in range(2, 16):
            k = Rational(ang, 360) * r * r
            if k.q == 1:  # integer coefficient of pi
                items.append((ang, r, int(k)))
    # spread for variety across angles and radii
    step = max(1, len(items) // 36)
    picked, used = [], set()
    for j in range(0, len(items), step):
        key = (items[j][0], items[j][1])
        if key in used:
            continue
        used.add(key)
        picked.append(items[j])
        if len(picked) == 36:
            break
    for it in items:
        if len(picked) == 36:
            break
        key = (it[0], it[1])
        if key not in used:
            used.add(key)
            picked.append(it)

    out = []
    for i, (ang, r, k) in enumerate(picked[:36]):
        pos = i % 4
        correct = (piL(k), k * pi)
        cands = [(piL(r * r), r * r * pi), (piL(2 * k), 2 * k * pi),
                 (piL(4 * k), 4 * k * pi), (piL(r * r - k), (r * r - k) * pi),
                 (piL(k + r), (k + r) * pi)]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=piL)
        out.append({
            "statement": "Find the area of a $%d°$ sector of a circle with "
                         "radius $%d$." % (ang, r),
            "options": opts, "correctIndex": ci,
            "explanation": "A sector is a fraction of the disk: "
                           "$\\frac{%d}{360}\\cdot\\pi\\cdot %d^2 = %s$. "
                           "The full disk is $%s$." % (ang, r, piL(k),
                                                       piL(r * r)),
            "check": ["Rational(%d,360)*pi*%d**2 == %d*pi" % (ang, r, k)],
        })
    return out


def gen_similar_triangles():
    combos = []
    for k in (2, 3, 4, 5):
        for a in (2, 3, 4, 5, 6):
            for b in (a + 1, a + 3):
                A = a * k
                ans = b * k
                combos.append((a, b, A, ans))
    step = max(1, len(combos) // 36)
    picked = []
    for j in range(0, len(combos), step):
        picked.append(combos[j])
        if len(picked) == 36:
            break
    for c in combos:
        if len(picked) == 36:
            break
        if c not in picked:
            picked.append(c)

    out = []
    for i, (a, b, A, ans) in enumerate(picked[:36]):
        pos = i % 4
        added = b + (A - a)
        correct = (intL(ans), ans)
        cands = [(intL(added), added), (intL(A), A), (intL(b + A), b + A),
                 (intL(b * a), b * a)]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=intL)
        # Both triangles share ONE world scale, so the second really is k
        # times the first. Right triangles with legs (a, b) and (A, ans);
        # the correspondence a↔A (vertical), b↔ans (horizontal) matches the
        # statement.
        gap = round(0.15 * (b + ans) + 1.5, 4)
        dx = round(b + gap, 4)
        fig = {
            "points": [
                {"id": "P", "x": 0, "y": 0, "label": ""},
                {"id": "Q", "x": b, "y": 0, "label": ""},
                {"id": "R", "x": 0, "y": a, "label": ""},
                {"id": "P2", "x": dx, "y": 0, "label": ""},
                {"id": "Q2", "x": round(dx + ans, 4), "y": 0, "label": ""},
                {"id": "R2", "x": dx, "y": A, "label": ""},
            ],
            "objects": [
                {"kind": "segment", "from": "P", "to": "Q", "label": str(b)},
                {"kind": "segment", "from": "P", "to": "R", "label": str(a)},
                {"kind": "segment", "from": "Q", "to": "R"},
                {"kind": "angle", "at": "P", "from": "Q", "to": "R",
                 "right": True},
                {"kind": "segment", "from": "P2", "to": "Q2", "label": "?",
                 "color": "accent"},
                {"kind": "segment", "from": "P2", "to": "R2", "label": str(A)},
                {"kind": "segment", "from": "Q2", "to": "R2"},
                {"kind": "angle", "at": "P2", "from": "Q2", "to": "R2",
                 "right": True},
            ],
        }
        out.append({
            "geoFigure": fig,
            "statement": "Two similar triangles: the first has sides $%d$ and "
                         "$%d$; the side of the second corresponding to $%d$ is "
                         "$%d$. Find the side corresponding to $%d$."
                         % (a, b, a, A, b),
            "options": opts, "correctIndex": ci,
            "explanation": "Scale factor $k = \\frac{%d}{%d}$. Corresponding "
                           "sides multiply: $%d\\cdot\\frac{%d}{%d} = %d$. "
                           "Adding $%d$ (the difference) is the classic wrong "
                           "move — similarity multiplies, never adds."
                           % (A, a, b, A, a, ans, A - a),
            "check": ["Rational(%d,%d)*%d == %d" % (A, a, b, ans)],
        })
    return out


def gen_solid_volumes():
    out = []
    idx = 0

    def emit(st, correct, cands, ex, chk):
        nonlocal idx
        pos = idx % 4
        opts, ci = build_latex_options(correct, cands, pos, latex_of=piL)
        out.append({"statement": st, "options": opts, "correctIndex": ci,
                    "explanation": ex, "check": [chk]})
        idx += 1

    # cylinders: k = r^2 h
    cyl = [(2, 3), (2, 5), (3, 2), (3, 4), (3, 7), (4, 3),
           (4, 5), (5, 2), (5, 6), (6, 4), (7, 2), (2, 9)]
    for r, h in cyl:
        k = r * r * h
        emit("Find the volume of a cylinder with radius $%d$ and height $%d$, "
             "exactly." % (r, h),
             (piL(k), k * pi),
             [(piL(2 * r * h), 2 * r * h * pi), (piL(r * h), r * h * pi),
              (piL(2 * r * r * h), 2 * r * r * h * pi),
              (piL(3 * r * r * h), 3 * r * r * h * pi)],
             "Cylinder: $V = \\pi r^2 h = \\pi\\cdot %d\\cdot %d = %s$."
             % (r * r, h, piL(k)),
             "pi*%d**2*%d == %d*pi" % (r, h, k))

    # cones: k = r^2 h / 3  (kept integer)
    cone = [(3, 4), (3, 5), (3, 7), (6, 2), (6, 5), (2, 6),
            (4, 6), (5, 6), (6, 4), (3, 8), (9, 2), (6, 7)]
    for r, h in cone:
        assert (r * r * h) % 3 == 0
        k = r * r * h // 3
        emit("Find the volume of a cone with radius $%d$ and height $%d$, "
             "exactly." % (r, h),
             (piL(k), k * pi),
             [(piL(3 * k), 3 * k * pi), (piL(2 * k), 2 * k * pi),
              (piL(4 * k), 4 * k * pi)],
             "Cone: $V = \\tfrac13\\pi r^2 h = \\tfrac13\\pi\\cdot %d\\cdot %d "
             "= %s$. Dropping the $\\tfrac13$ gives the cylinder $%s$."
             % (r * r, h, piL(k), piL(3 * k)),
             "Rational(1,3)*pi*%d**2*%d == %d*pi" % (r, h, k))

    # spheres: k = 4 R^3 / 3
    for R in range(1, 13):
        k = Rational(4 * R ** 3, 3)
        emit("Find the volume of a sphere with radius $%d$, exactly." % R,
             (piL(k), k * pi),
             [(piL(4 * R * R), 4 * R * R * pi), (piL(R ** 3), R ** 3 * pi),
              (piL(4 * R ** 3), 4 * R ** 3 * pi), (piL(2 * k), 2 * k * pi)],
             "Sphere: $V = \\tfrac43\\pi R^3 = \\tfrac43\\pi\\cdot %d = %s$. "
             "Using $4\\pi R^2$ (the surface area) gives $%s$."
             % (R ** 3, piL(k), piL(4 * R * R)),
             "Rational(4,3)*pi*%d**3 == Rational(%d,%d)*pi"
             % (R, k.p, k.q))
    return out


def gen_space_diagonal():
    quads = []
    seen = set()
    for l in range(1, 17):
        for w in range(l, 20):
            for h in range(w, 26):
                s = l * l + w * w + h * h
                d = isqrt(s)
                if d * d == s:
                    if (l, w, h) in seen:
                        continue
                    seen.add((l, w, h))
                    quads.append((l, w, h, d))
    quads.sort(key=lambda q: (q[3], q[0], q[1], q[2]))
    step = max(1, len(quads) // 36)
    picked = []
    for j in range(0, len(quads), step):
        picked.append(quads[j])
        if len(picked) == 36:
            break
    for q in quads:
        if len(picked) == 36:
            break
        if q not in picked:
            picked.append(q)

    out = []
    for i, (l, w, h, d) in enumerate(picked[:36]):
        pos = i % 4
        correct = (intL(d), d)
        cands = [(intL(l + w + h), l + w + h), (intL(d + 1), d + 1),
                 (intL(d - 1), d - 1), (intL(l + w + h - 1), l + w + h - 1)]
        opts, ci = build_latex_options(correct, cands, pos, latex_of=intL)
        out.append({
            "statement": "Find the space diagonal of a $%d \\times %d \\times "
                         "%d$ box." % (l, w, h),
            "options": opts, "correctIndex": ci,
            "explanation": "$d = \\sqrt{l^2 + w^2 + h^2} = \\sqrt{%d + %d + %d} "
                           "= \\sqrt{%d} = %d$ — Pythagoras across the floor, "
                           "then up." % (l * l, w * w, h * h, d * d, d),
            "check": ["sqrt(%d**2 + %d**2 + %d**2) == %d" % (l, w, h, d)],
        })
    return out


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

FORMS_META = [
    ("pythagoras", "The Pythagorean theorem", 1,
     "c² = a² + b² — hypotenuse from the legs.", "pyth", gen_pythagoras),
    ("triangle-area", "Triangle area", 1,
     "A = ½ · base · height.", "tri", gen_triangle_area),
    ("circle-basics", "Circle area & circumference", 1,
     "A = πr² (fills), C = 2πr (wraps) — don't swap them.", "circ",
     gen_circle_basics),
    ("special-triangles", "Special right triangles", 2,
     "45-45-90: x, x, x√2. 30-60-90: x, x√3, 2x.", "spec",
     gen_special_triangles),
    ("sector-area", "Sector area", 2,
     "Sector = (angle/360) × πr².", "sect", gen_sector_area),
    ("similar-triangles", "Similar triangles", 2,
     "Corresponding sides share one multiplier k — never an added amount.",
     "sim", gen_similar_triangles),
    ("solid-volumes", "Volumes of solids", 3,
     "Cylinder πr²h; cone adds ⅓; sphere ⁴⁄₃πR³.", "vol", gen_solid_volumes),
    ("space-diagonal", "The space diagonal", 3,
     "d² = l² + w² + h² — all three dimensions enter.", "diag",
     gen_space_diagonal),
]


def _finalize(form_id, title, level, skill, abbrev, raw):
    variants = []
    for i, v in enumerate(raw):
        vd = {"id": "GEO-%s-v%02d" % (abbrev, i + 1)}
        vd.update(v)
        variants.append(vd)
    return {"id": form_id, "title": title, "level": level, "skill": skill,
            "variants": variants}


def build():
    forms = []
    for form_id, title, level, skill, abbrev, gen in FORMS_META:
        forms.append(_finalize(form_id, title, level, skill, abbrev, gen()))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN,
            "blurb": BLURB, "forms": forms}


# ---------------------------------------------------------------------------
# self-check
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    data = build()
    expected_ids = [m[0] for m in FORMS_META]
    assert len(data["forms"]) == 8, "expected 8 forms, got %d" % len(data["forms"])
    assert [f["id"] for f in data["forms"]] == expected_ids, "form id/order mismatch"

    all_ids = []
    total = 0
    min_per_form = 10 ** 9
    for meta, form in zip(FORMS_META, data["forms"]):
        assert form["id"] == meta[0]
        assert form["title"] == meta[1]
        assert form["level"] == meta[2]
        assert form["skill"] == meta[3]
        vs = form["variants"]
        assert len(vs) >= 32, "%s has only %d variants" % (form["id"], len(vs))
        min_per_form = min(min_per_form, len(vs))
        total += len(vs)
        for v in vs:
            all_ids.append(v["id"])
            opts = v["options"]
            assert len(opts) == 4, "%s: need 4 options" % v["id"]
            assert len(set(opts)) == 4, "%s: options not distinct" % v["id"]
            assert 0 <= v["correctIndex"] <= 3, "%s: bad correctIndex" % v["id"]
            for c in v["check"]:
                res = sympify(c)
                assert bool(res) is True, "%s: check failed -> %s" % (v["id"], c)
            correct = opts[v["correctIndex"]]
            for j, o in enumerate(opts):
                if j == v["correctIndex"]:
                    continue
                try:
                    cv = sympify(correct.strip("$"))
                    ov = sympify(o.strip("$"))
                    assert simplify(cv - ov) != 0, "%s: distractor == correct" % v["id"]
                except AssertionError:
                    raise
                except Exception:
                    assert correct != o, "%s: duplicate option string" % v["id"]
            if form["id"] == "pythagoras":
                assert "geoFigure" in v, "%s: pythagoras needs geoFigure" % v["id"]

    assert len(all_ids) == len(set(all_ids)), "variant ids not globally unique"
    print("SELFCHECK OK  forms=8  total=%d  min_per_form=%d" % (total, min_per_form))
