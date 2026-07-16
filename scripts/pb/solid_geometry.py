# -*- coding: utf-8 -*-
"""Problem-bank subject: Solid Geometry — mirrors the /math/solid-geometry course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/solid_geometry.py` for the self-check.
"""
import importlib.util
import os

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "solid-geometry"
TITLE = "Solid Geometry"
TITLE_MN = "Огторгуйн геометр"
BLURB = ("Unit-by-unit practice for the Solid Geometry course — lines and planes in space through spheres and similar solids.")

UNITS = [
    {"id": "lines-and-planes-in-space", "title": "Lines & Planes in Space",
     "blurb": "The rules of 3D: what determines a plane, skew lines, perpendicularity, and the two angles every exam measures."},
    {"id": "prisms-and-the-cube", "title": "Prisms & the Cube",
     "blurb": "The box family: prism anatomy, the cube's √2 and √3 diagonals, and surface & volume you can see face by face."},
    {"id": "pyramids", "title": "Pyramids",
     "blurb": "Height, apothem, slant, edge — the two Pythagorean triangles inside every pyramid, the ⅓ in the volume, and the frustum."},
    {"id": "cylinders-and-cones", "title": "Cylinders & Cones",
     "blurb": "The round solids you can unroll: the cylinder's rectangle label, the cone's pie-slice development, and both volumes."},
    {"id": "spheres", "title": "Spheres",
     "blurb": "Every slice a circle (r² = R² − d²), the surface of exactly four great circles, and Archimedes' tombstone 2:3."},
    {"id": "cross-sections-and-similar-solids", "title": "Cross-Sections & Similar Solids",
     "blurb": "Predict any cut, scale with k / k² / k³, glue and drill combined solids — and the five-triangle exam strategy."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "space-diagonal": "prisms-and-the-cube",
}

SOURCES = ['geometry']

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
