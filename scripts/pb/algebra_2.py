# -*- coding: utf-8 -*-
"""Problem-bank subject: Algebra 2 — mirrors the /math/algebra-2 course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/algebra_2.py` for the self-check.
"""
import importlib.util
import os

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "algebra-2"
TITLE = "Algebra 2"
TITLE_MN = "Алгебр 2"
BLURB = ("Unit-by-unit practice for the Algebra 2 course — transformations, complex numbers, polynomials, logs, rationals, and sequences.")

UNITS = [
    {"id": "functions-and-transformations", "title": "Functions & Transformations",
     "blurb": "Function notation, domain and range, the four graph moves, absolute value, and piecewise functions."},
    {"id": "quadratics-and-complex-numbers", "title": "Quadratics & Complex Numbers",
     "blurb": "Vertex form and completing the square, the number i, complex roots, and quadratic inequalities."},
    {"id": "systems-and-nonlinear-models", "title": "Systems & Nonlinear Models",
     "blurb": "2×2 systems at speed, three variables, curves meeting lines, and feasible regions with the corner principle."},
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behavior, division and the remainder/factor theorems, zeros with multiplicity, and cubic+ equations."},
    {"id": "radicals-and-rational-exponents", "title": "Radicals & Rational Exponents",
     "blurb": "Fractional powers, radical arithmetic, equations with phantom solutions, and inverse functions."},
    {"id": "exponentials-and-logarithms", "title": "Exponentials & Logarithms",
     "blurb": "Growth and decay, logs as the reverse gear, the three log laws, and solving both equation families."},
    {"id": "rational-functions", "title": "Rational Functions",
     "blurb": "Variation, asymptotes and holes, rational-expression arithmetic, and equations with work problems."},
    {"id": "sequences-and-series", "title": "Sequences & Series",
     "blurb": "Arithmetic ladders, geometric rockets, infinite sums, sigma notation, and recursion — the capstone."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "composition": "functions-and-transformations",
    "inverse-value": "functions-and-transformations",
    "log-evaluate": "exponentials-and-logarithms",
    "exp-equation": "exponentials-and-logarithms",
    "log-add-rule": "exponentials-and-logarithms",
    "exp-substitution": "exponentials-and-logarithms",
    "log-equation": "exponentials-and-logarithms",
    "log-chain": "exponentials-and-logarithms",
    "log-inequality": "exponentials-and-logarithms",
    "exp-inequality-flip": "exponentials-and-logarithms",
    "arith-nth": "sequences-and-series",
    "geo-nth": "sequences-and-series",
    "arith-find-d": "sequences-and-series",
    "arith-sum": "sequences-and-series",
    "geo-sum": "sequences-and-series",
    "which-term": "sequences-and-series",
    "infinite-geo": "sequences-and-series",
    "geo-two-terms": "sequences-and-series",
}

SOURCES = ['functions', 'logarithms', 'sequences']

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


def new_forms():
    """Unit-specific forms authored for this subject (appended by unit)."""
    return []


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
