# -*- coding: utf-8 -*-
"""Shared authoring helpers for the Integrated Math problem banks.

scripts/pb/integrated_1.py and integrated_2.py both build their forms from
parameter SWEEPS: a generator yields many raw problems from a grid of
parameters, and one of the assemblers below turns them into bank variants
with rotated answer positions and provably distinct options.

Two assemblers, because bank options come in two flavours:
  mk_num  — options are numbers. Distinctness is checked on the VALUE
            (Rational), so 1/2 and 2/4 count as a collision and the draw is
            discarded rather than shipping an ambiguous item.
  mk_txt  — options are text/expressions (a transformation name, a factored
            form, a congruence criterion). Distinctness is checked on the
            rendered string after whitespace normalisation.

Both cap a form at CAP variants and assert a floor, so a generator whose
parameter grid silently collapses fails the build instead of shipping a thin
form. The gate (scripts/verify-problembank.py) independently re-checks option
distinctness and every sympy check, so nothing here is load-bearing for
correctness — it is load-bearing for VARIETY.
"""
from sympy import Rational

CAP = 36           # variants kept per form
FLOOR = 24         # a form thinner than this is a broken generator, not a form


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

def fmt(v):
    """LaTeX for an integer/rational value, no surrounding $."""
    v = Rational(v)
    if v.q == 1:
        return str(v.p)
    if v.p < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def money(v):
    """Thin-space thousands separator, KaTeX-safe: 15000 -> 15\\,000."""
    n = int(v)
    sign = "-" if n < 0 else ""
    s = str(abs(n))
    parts = []
    while len(s) > 3:
        parts.insert(0, s[-3:])
        s = s[:-3]
    parts.insert(0, s)
    return sign + "\\,".join(parts)


def sgn(b):
    """'+' or '-' for building signed term chains."""
    return "+" if b >= 0 else "-"


def lin(a, b, var="x"):
    """Render `ax + b` cleanly: no '1x', no '+ -5'."""
    if a == 0:
        return str(b)
    s = var if a == 1 else ("-" + var if a == -1 else "%d%s" % (a, var))
    if b > 0:
        s += " + %d" % b
    elif b < 0:
        s += " - %d" % (-b)
    return s


def quad(a, b, c, var="x"):
    """Render `ax^2 + bx + c` cleanly, dropping zero terms."""
    if a == 0:
        return lin(b, c, var)
    s = "%s^2" % var if a == 1 else ("-%s^2" % var if a == -1 else "%d%s^2" % (a, var))
    if b != 0:
        xb = var if abs(b) == 1 else "%d%s" % (abs(b), var)
        s += " %s %s" % (sgn(b), xb)
    if c != 0:
        s += " %s %d" % (sgn(c), abs(c))
    return s


def xpm(p, var="x"):
    """(x + p) with the sign folded in, e.g. (x + 3) / (x - 3) / x."""
    if p == 0:
        return var
    return "(%s + %d)" % (var, p) if p > 0 else "(%s - %d)" % (var, -p)


def pt(x, y):
    """Coordinate pair as LaTeX."""
    return "(%s,\\ %s)" % (fmt(x), fmt(y))


def radical(coef, rad):
    """Render coef*sqrt(rad) cleanly: 1*sqrt(3) -> \\sqrt{3}, k*sqrt(1) -> k."""
    if rad == 1:
        return str(coef)
    if coef == 1:
        return "\\sqrt{%d}" % rad
    if coef == -1:
        return "-\\sqrt{%d}" % rad
    return "%d\\sqrt{%d}" % (coef, rad)


# ---------------------------------------------------------------------------
# assemblers
# ---------------------------------------------------------------------------

def _rotate(options_wo_correct, correct, i):
    """Place `correct` at slot i%4 so the answer key stays balanced."""
    opts = list(options_wo_correct)
    opts.insert(i % 4, correct)
    return opts, i % 4


def mk_num(prefix, raws, cap=CAP, floor=FLOOR):
    """Assemble variants whose four options are NUMBERS.

    Each raw: {statement, correct, dvals (3), explanation, check, [geoFigure]}.
    A draw whose distractors collide with the answer *as values* is skipped —
    that is a bad parameter choice, not a question.
    """
    variants, seen = [], set()
    for raw in raws:
        if len(variants) >= cap:
            break
        vals = [Rational(raw["correct"])] + [Rational(d) for d in raw["dvals"]]
        if len(set(vals)) != 4:
            continue                       # degenerate draw
        if raw["statement"] in seen:
            continue                       # same question twice
        seen.add(raw["statement"])
        i = len(variants)
        opts, ci = _rotate(["$%s$" % fmt(v) for v in vals[1:]], "$%s$" % fmt(vals[0]), i)
        assert len(set(opts)) == 4, "%s: option collision in %r" % (prefix, raw["statement"])
        v = {
            "id": "%s-v%02d" % (prefix, i + 1),
            "statement": raw["statement"],
            "options": opts,
            "correctIndex": ci,
            "explanation": raw["explanation"],
            "check": raw["check"],
        }
        if raw.get("geoFigure"):
            v["geoFigure"] = raw["geoFigure"]
        variants.append(v)
    assert len(variants) >= floor, \
        "%s: only %d variants generated (floor %d)" % (prefix, len(variants), floor)
    return variants


def mk_txt(prefix, raws, cap=CAP, floor=FLOOR):
    """Assemble variants whose four options are TEXT or expressions.

    Each raw: {statement, correct (str), dvals (3 strs), explanation, check,
    [geoFigure]}. Distinctness is on the normalised string.
    """
    variants, seen = [], set()
    for raw in raws:
        if len(variants) >= cap:
            break
        # A text form may still have a numeric item ("how many terms?"). Coerce
        # to rendered math rather than a bare digit so options look uniform.
        opts_all = [o if isinstance(o, str) else "$%s$" % fmt(o)
                    for o in [raw["correct"]] + list(raw["dvals"])]
        norm = [" ".join(o.split()) for o in opts_all]
        if len(set(norm)) != 4:
            continue                       # degenerate draw
        if raw["statement"] in seen:
            continue
        seen.add(raw["statement"])
        i = len(variants)
        opts, ci = _rotate(opts_all[1:], opts_all[0], i)
        assert len(set(opts)) == 4, "%s: option collision in %r" % (prefix, raw["statement"])
        v = {
            "id": "%s-v%02d" % (prefix, i + 1),
            "statement": raw["statement"],
            "options": opts,
            "correctIndex": ci,
            "explanation": raw["explanation"],
            "check": raw["check"],
        }
        if raw.get("geoFigure"):
            v["geoFigure"] = raw["geoFigure"]
        variants.append(v)
    assert len(variants) >= floor, \
        "%s: only %d variants generated (floor %d)" % (prefix, len(variants), floor)
    return variants


def form(fid, title, level, unit, skill, variants):
    """One bank form. `skill` is the one-line 'what this drills' shown to students."""
    assert level in (1, 2, 3), "%s: level must be 1..3" % fid
    return {"id": fid, "title": title, "level": level, "unit": unit,
            "skill": skill, "variants": variants}


# ---------------------------------------------------------------------------
# figures — GeoDiagramSpec, the same shape lib/genmath-interactive.ts declares
# ---------------------------------------------------------------------------

def P(pid, x, y, label=None):
    return {"id": pid, "x": round(float(x), 4), "y": round(float(y), 4),
            "label": pid if label is None else label}


def seg(a, b, label=None, dashed=False):
    o = {"kind": "segment", "from": a, "to": b}
    if label:
        o["label"] = label
    if dashed:
        o["dashed"] = True
    return o


def ray(a, b, dashed=False):
    o = {"kind": "ray", "from": a, "to": b}
    if dashed:
        o["dashed"] = True
    return o


def ang(at, frm, to, label=None):
    o = {"kind": "angle", "at": at, "from": frm, "to": to}
    if label:
        o["label"] = label
    return o


# NOTE: GeoObjectSpec (lib/genmath-interactive.ts) has exactly four kinds —
# segment, ray, line, angle. There is no polygon and no circle primitive, and
# because widget configs are cast from JSON, an invented kind would type-check
# and then silently draw nothing. Closed shapes are therefore built out of
# segments, and circles out of a fine segment fan.

def closed(ids, labels=None, ticks=None):
    """Close a polygon as a segment cycle. `labels` optionally names each side."""
    out = []
    n = len(ids)
    for i in range(n):
        a, b = ids[i], ids[(i + 1) % n]
        lab = labels[i] if labels and i < len(labels) and labels[i] else None
        tk = ticks[i] if ticks and i < len(ticks) and ticks[i] else None
        o = seg(a, b, lab)
        if tk:
            o["ticks"] = tk
        out.append(o)
    return out


def circle_of(prefix, cx, cy, r, n=48):
    """Approximate a circle as an n-gon of hidden points.

    Returns (points, objects, hidden_ids). n=48 reads as a smooth circle at
    the sizes GeoDiagram renders (<= 200px tall) while staying cheap in JSON.
    """
    import math
    pts, ids = [], []
    for i in range(n):
        th = 2 * math.pi * i / n
        pid = "%s%d" % (prefix, i)
        ids.append(pid)
        pts.append(P(pid, cx + r * math.cos(th), cy + r * math.sin(th), ""))
    objs = [seg(ids[i], ids[(i + 1) % n]) for i in range(n)]
    return pts, objs, ids


def on_circle(pid, cx, cy, r, deg, label=None):
    """A labelled point at `deg` degrees on the circle centred (cx, cy)."""
    import math
    th = math.radians(deg)
    return P(pid, cx + r * math.cos(th), cy + r * math.sin(th),
             pid if label is None else label)


def figure(points, objects, hide=None):
    """Assemble a GeoDiagramSpec. `hide` suppresses point dots for clean line art."""
    spec = {"points": points, "objects": objects}
    if hide:
        spec["hidePoints"] = list(hide)
    return spec
