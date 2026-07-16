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
import os

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
