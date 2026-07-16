# -*- coding: utf-8 -*-
"""Problem-bank subject: Geometry — mirrors the /math/geometry course units.

Assembles the subject from (a) forms remapped out of the original exam-topic
generators and (b) new unit-specific forms defined below. Every form carries a
`unit` field matching the course spine, so the bank page groups problems
exactly the way the course teaches them.

RESOLVERS maps NEW form ids to independent re-solvers used by
scripts/audit_problembank.py (existing form ids keep their built-in resolvers).
Run `python3 scripts/pb/geometry_course.py` for the self-check.
"""
import importlib.util
import os

PB = os.path.dirname(os.path.abspath(__file__))

SLUG = "geometry"
TITLE = "Geometry"
TITLE_MN = "Геометр"
BLURB = ("Unit-by-unit practice for the Geometry course — from points and angles to circles, area, and coordinates.")

UNITS = [
    {"id": "foundations", "title": "Foundations: Points, Lines & Angles",
     "blurb": "Points, lines, rays, segments and planes; measuring segments and angles; angle types, angle pairs, and bisectors."},
    {"id": "reasoning-and-proof", "title": "Reasoning & Proof",
     "blurb": "From noticing patterns to proving facts: conjectures, if-then statements, and your first two-column proofs."},
    {"id": "parallel-and-perpendicular", "title": "Parallel & Perpendicular Lines",
     "blurb": "Transversals and the angle pairs they create — which are congruent, which are supplementary — and proving lines parallel."},
    {"id": "triangles-and-congruence", "title": "Triangles & Congruence",
     "blurb": "Triangle types, the angle sum, the triangle inequality, and the congruence shortcuts SSS · SAS · ASA · AAS · HL."},
    {"id": "relationships-in-triangles", "title": "Relationships in Triangles",
     "blurb": "Bisectors, medians, altitudes, the midsegment theorem, and inequalities inside a triangle."},
    {"id": "quadrilaterals-and-polygons", "title": "Quadrilaterals & Polygons",
     "blurb": "Angle sums for any polygon; parallelograms, rectangles, rhombi, squares, trapezoids, and kites — with proofs."},
    {"id": "similarity", "title": "Similarity",
     "blurb": "Ratio and proportion, similar polygons, the AA · SSS · SAS similarity shortcuts, and the side-splitter theorem."},
    {"id": "right-triangles-and-trig", "title": "Right Triangles & Trigonometry",
     "blurb": "The Pythagorean theorem, special right triangles, and sine · cosine · tangent with elevation and depression."},
    {"id": "circles", "title": "Circles",
     "blurb": "Radius, chord, tangent, secant; central and inscribed angles; arcs; and the circle relationships."},
    {"id": "area-and-perimeter", "title": "Area & Perimeter",
     "blurb": "Areas of triangles, quadrilaterals and regular polygons; circumference, circle area, sectors, and composite figures."},
    {"id": "surface-area-and-volume", "title": "Surface Area & Volume",
     "blurb": "Prisms, cylinders, pyramids, cones, and spheres — wrapping and filling 3-D solids."},
    {"id": "transformations", "title": "Transformations",
     "blurb": "Translations, reflections, rotations, and dilations; symmetry; congruence and similarity re-seen through motion."},
    {"id": "coordinate-geometry", "title": "Coordinate Geometry",
     "blurb": "Distance, midpoint, and slope; equations of lines and circles; proofs with coordinates — the course capstone."},
]

# original form id -> unit id (forms pulled from the old exam-topic builders)
REMAP = {
    "similar-triangles": "similarity",
    "pythagoras": "right-triangles-and-trig",
    "special-triangles": "right-triangles-and-trig",
    "circle-basics": "circles",
    "sector-area": "circles",
    "triangle-area": "area-and-perimeter",
    "solid-volumes": "surface-area-and-volume",
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
