# -*- coding: utf-8 -*-
"""Problem-bank subject: Calculus — mirrors the /math/calculus course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/calculus.py` to
self-check.
"""
import re

from sympy import Rational, sympify

SLUG = "calculus"
TITLE = "Calculus"
TITLE_MN = "Калькулюс"
BLURB = ("Unit-by-unit practice for the Calculus course — limits, derivatives, and integrals, exam-style.")

UNITS = [
    {"id": "limits-and-continuity", "title": "Limits & Continuity",
     "blurb": "What a function is heading toward: limits from graphs and algebra, limits at infinity, and the definition of an unbroken graph."},
    {"id": "the-derivative", "title": "The Derivative",
     "blurb": "Secants collapse onto tangents: the difference quotient, the derivative function, the power rule, and the four library derivatives."},
    {"id": "differentiation-techniques", "title": "Differentiation Techniques",
     "blurb": "Product, quotient, and chain rules; combining them, and second derivatives — the whole differentiable world unlocked."},
    {"id": "applications-of-derivatives", "title": "Applications of Derivatives",
     "blurb": "Tangent and normal lines, rise and fall, peaks and valleys certified two ways, concavity — and optimization, the art of the best."},
    {"id": "integrals", "title": "Integrals",
     "blurb": "Differentiation reversed, areas by slicing, and the Fundamental Theorem that collapses infinite sums into one subtraction."},
    {"id": "applications-of-integrals", "title": "Applications of Integrals",
     "blurb": "Areas between curves, motion recovered from velocity, average values — and a capstone running the whole course in one arc."},
]

# No legacy forms: this subject is authored fresh.
REMAP = {}
SOURCES = []

# form id -> fn(statement) -> ("num", sympy value) | ("opt", exact option str)
RESOLVERS = {}


def new_forms():
    """Unit-specific forms (filled by the authoring pass)."""
    return []


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = new_forms()
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
