# -*- coding: utf-8 -*-
"""Problem-bank subject: Precalculus — mirrors the /math/precalculus course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/precalculus.py` to
self-check.
"""
import re

from sympy import Rational, sympify

SLUG = "precalculus"
TITLE = "Precalculus"
TITLE_MN = "Прекалькулюс"
BLURB = ("Unit-by-unit practice for the Precalculus course — functions and transformations through conics.")

UNITS = [
    {"id": "functions-and-their-graphs", "title": "Functions & Their Graphs",
     "blurb": "Domain, range, and graph features; composition; inverse functions; even/odd symmetry."},
    {"id": "transformations-of-graphs", "title": "Transformations of Graphs",
     "blurb": "Shifts, stretches, reflections, the combined form a·f(x−h)+k, and piecewise graphs."},
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behavior, zeros and the Factor Theorem, multiplicity, division and the Remainder Theorem."},
    {"id": "rational-functions", "title": "Rational Functions",
     "blurb": "Vertical asymptotes, holes, horizontal and slant asymptotes, and complete graphs."},
    {"id": "exponentials-and-logarithms", "title": "Exponentials & Logarithms",
     "blurb": "Growth and decay, compound interest and e, logs as inverses, and exponential/log equations."},
    {"id": "the-unit-circle", "title": "The Unit Circle",
     "blurb": "Radians, sine and cosine as coordinates, special angles, and reference angles in all quadrants."},
    {"id": "trigonometric-graphs-and-equations", "title": "Trig Graphs & Equations",
     "blurb": "The sine wave, amplitude/period/shifts, fundamental identities, and solving trig equations."},
    {"id": "conic-sections", "title": "Conic Sections",
     "blurb": "Circles, ellipses, parabolas with foci, hyperbolas, and classifying second-degree equations."},
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
