# -*- coding: utf-8 -*-
"""Problem-bank subject: Vectors & Matrices — mirrors the /math/vectors-matrices course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/vectors_matrices.py` to
self-check.
"""
import re

from sympy import Rational, sympify

SLUG = "vectors-matrices"
TITLE = "Vectors & Matrices"
TITLE_MN = "Вектор ба матриц"
BLURB = ("Unit-by-unit practice for the Vectors & Matrices course — components and magnitudes to determinants and systems.")

UNITS = [
    {"id": "vectors-and-coordinates", "title": "Vectors & Coordinates",
     "blurb": "What a vector is, components and magnitude, equal/opposite/parallel vectors, and unit vectors."},
    {"id": "vector-arithmetic", "title": "Vector Arithmetic",
     "blurb": "Tip-to-tail addition, scaling, subtraction, vectors inside figures, and the section formula."},
    {"id": "the-dot-product", "title": "The Dot Product",
     "blurb": "u\u00b7v two ways, angles from the sign, perpendicularity tests, and the |u+v|\u00b2 toolbox."},
    {"id": "vectors-in-space", "title": "Vectors in Space",
     "blurb": "The third coordinate: 3D magnitudes and dot products, the box diagonal, and normal vectors of planes."},
    {"id": "matrices-and-operations", "title": "Matrices & Operations",
     "blurb": "Grids with an address system: entrywise arithmetic, row-times-column multiplication, identity and powers."},
    {"id": "determinants-and-inverses", "title": "Determinants, Inverses & Systems",
     "blurb": "ad \u2212 bc, the 2\u00d72 inverse, Cramer's rule, and matrices as transformations \u2014 the capstone."},
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
