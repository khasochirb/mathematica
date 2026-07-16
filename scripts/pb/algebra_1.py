# -*- coding: utf-8 -*-
"""Problem-bank subject: Algebra 1 — mirrors the /math/algebra-1 course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators (algebra.py, functions.py) and (b) new unit-specific forms defined
below. Every form carries a `unit` field matching ALG1's course spine, so the
bank page can group problems exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/algebra_1.py` for the self-check.
"""
import importlib.util
import os

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "algebra-1"
TITLE = "Algebra 1"
TITLE_MN = "Алгебр 1"
BLURB = ("Unit-by-unit practice for the Algebra 1 course — expressions to "
         "quadratics, every unit with its own problem collection.")

UNITS = [
    {"id": "expressions-and-operations", "title": "Expressions & Operations",
     "blurb": "Variables, evaluating and simplifying, exponents, order of operations, and words-to-algebra."},
    {"id": "linear-equations", "title": "Solving Linear Equations",
     "blurb": "One-step to both-sides equations, fractions and special cases, and rearranging formulas."},
    {"id": "inequalities", "title": "Linear Inequalities",
     "blurb": "Solving and graphing, the negative-flip rule, compound and/or, and absolute-value equations."},
    {"id": "functions", "title": "Introduction to Functions",
     "blurb": "The one-output rule, f(x) notation, domain and range, and reading real-world graphs."},
    {"id": "linear-functions", "title": "Linear Functions & Slope",
     "blurb": "Slope as a rate, y = mx + b, point-slope and standard forms, parallel and perpendicular lines."},
    {"id": "systems-of-equations", "title": "Systems of Equations",
     "blurb": "Graphing, substitution, elimination, applications, and the no-solution/infinite cases."},
    {"id": "polynomials-and-factoring", "title": "Polynomials & Factoring",
     "blurb": "Polynomial arithmetic, GCF, factoring trinomials and special patterns."},
    {"id": "quadratic-equations", "title": "Quadratic Equations & Functions",
     "blurb": "Solving by factoring, roots and the discriminant, the vertex, and parabola graphs."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    # from algebra.py
    "exponent-laws": "expressions-and-operations",
    "evaluate-expression": "expressions-and-operations",
    "linear-two-step": "linear-equations",
    "rational-equation": "linear-equations",
    "inequality-flip": "inequalities",
    "absolute-inequality": "inequalities",
    "system-2x2": "systems-of-equations",
    "system-parameter": "systems-of-equations",
    # from functions.py
    "vertex-read": "quadratic-equations",
    "factored-roots": "quadratic-equations",
    "discriminant": "quadratic-equations",
    "complete-square-min": "quadratic-equations",
    "quadratic-inequality": "quadratic-equations",
    "tangency-parameter": "quadratic-equations",
}

SOURCES = ["algebra", "functions"]

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
