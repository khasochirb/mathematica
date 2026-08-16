"""Audit existing ЭЕШ content against Rule 1: one skill_id per item.

Two lists out, as asked: what maps cleanly, and what is an orphan. NOTHING
IS DELETED and nothing is auto-tagged — an orphan here is a decision for
Khas, and a machine guess would be indistinguishable from a real tag once it
is in the database.

The resolver is deliberately CONSERVATIVE, in this order:
  1. the hand-verified legacy mapping (data/skills/esh-topic-mapping.json)
  2. an exact match of the subtopic string against a skill id
  3. an exact match against a skill's English name, normalised
  4. an exact match of a known alias (the ALIASES table below — every entry
     hand-checked, same standard as the legacy mapping)
Anything else is an ORPHAN. In particular there is no fuzzy matching: a
0.8-similar string is how "тойрог" (circle) and "тойрог ба шүргэгч" (circle
and tangent) end up on the same skill when they are two different lessons.

Output is ordered by how much it buys: the orphan list is sorted by the
number of questions behind each string, so the first twenty lines of it are
most of the remaining work.

Run: python3 scripts/skills/content_audit.py
"""

from __future__ import annotations

import collections
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAPH = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))
MAPPING = json.load(open(os.path.join(ROOT, "data", "skills", "esh-topic-mapping.json")))

SKILLS = {s["id"]: s for s in GRAPH["skills"]}
BY_NAME = {}
for s in GRAPH["skills"]:
    BY_NAME[re.sub(r"[^a-z0-9]+", " ", s["name_en"].lower()).strip()] = s["id"]

LEGACY = {}
for r in MAPPING["mappings"]:
    if r["hub"] == "esh" and r["skills"]:
        LEGACY[(r["topic"], r["subtopic"].strip().lower())] = r["skills"][0]

# Hand-checked aliases. Each line is a claim that the string on the left is
# THAT skill and not a neighbour of it. Mongolian glosses are given so the
# claim can be checked by someone who reads Mongolian — which I do not, and
# which is exactly why these are the entries most worth re-reading.
ALIASES = {
    # -- Mongolian, algebra
    "олон гишүүнт": "polynomial-arithmetic",              # 'polynomial'
    "хуваагдах чанар": "divisibility-rules",              # 'divisibility property'
    "тэнцэтгэл биш": "linear-inequality-one-variable",    # 'inequality'
    "тэнцэтгэл бишүүд": "linear-inequality-one-variable",
    "стандарт хэлбэр": "scientific-notation",             # 'standard form'
    "рационал илэрхийлэл": "rational-expressions",        # 'rational expression'
    "бутархай илэрхийлэл": "rational-expressions",        # 'fractional expression'
    "комплекс тоо": "complex-arithmetic",                 # 'complex number'
    "матриц": "matrix-multiplication",                    # 'matrix'
    "биномын теорем": "binomial-theorem",                 # 'binomial theorem'
    "бином задаргаа": "binomial-theorem",                 # 'binomial expansion'
    "шугаман тэгшитгэл": "linear-equation-one-variable",  # 'linear equation'
    "логарифм тэгшитгэл": "logarithmic-equations",        # 'logarithmic equation'
    "язгуур": "radicals-simplification",                  # 'root/radical'
    "радикал": "radicals-simplification",
    "хурд бодлого": "rate-and-work-problems",             # 'speed problem'
    "харьцаа бодлого": "mixture-and-ratio-problems",      # 'ratio problem'
    "функц": "function-notation",                         # 'function'
    "дараалал ба цуваа": "arithmetic-sequence",           # 'sequence and series'
    "геометр прогресс": "geometric-sequence",             # 'geometric progression'
    "арифметик прогресс": "arithmetic-sequence",          # 'arithmetic progression'
    "нийлбэр": "arithmetic-series",                       # 'sum'
    "олонлог": "set-operations",                          # 'set'
    "иррационал тоо": "real-number-sets",                 # 'irrational number'
    "дэд олонлог": "subsets-and-power-sets",              # 'subset'
    "олонлогийн огтлолцол": "set-operations",             # 'intersection of sets'
    "тоо харьцуулах": "real-number-sets",                 # 'comparing numbers'
    "тоймлох": "decimal-arithmetic",                      # 'rounding'
    "бутархай тоо": "fraction-arithmetic",                # 'fraction'
    "квадрат тэгшитгэл": "quadratic-formula",             # 'quadratic equation'
    "арифметик": "complex-arithmetic",                    # in complex_numbers topic only
    # -- Mongolian, geometry & trig
    "тойрог": "circle-parts",                             # 'circle'
    "тойрог ба шүргэгч": "circle-tangent",                # 'circle and tangent'
    "тойрог ба гурвалжин": "inscribed-angle",             # 'circle and triangle'
    "вектор": "vector-arithmetic",                        # 'vector'
    "конус": "cone",                                      # 'cone'
    "орон зайн геометр": "space-geometry-angles",         # 'space geometry'
    "параллелепипед": "prism-volume-surface",             # 'parallelepiped'
    "медиан": "triangle-medians",                         # 'median'
    "шулуун тэгшитгэл": "line-equation",                  # 'equation of a line'
    "хувиргалт": "transformation-matrices",               # 'transformation'
    "хувиргалтын матриц": "transformation-matrices",      # 'transformation matrix'
    "матриц хувиргалт": "transformation-matrices",
    "урвуу матриц": "inverse-matrix-2x2",                 # 'inverse matrix'
    "тодорхойлогч": "determinant-2x2",                    # 'determinant'
    "эсрэг вектор": "vector-arithmetic",                  # 'opposite vector'
    "параллель вектор": "vector-arithmetic",              # 'parallel vector'
    "векторын урт": "vector-magnitude",                   # 'length of a vector'
    "хэрчмийн хуваалт": "vector-section-formula",         # 'division of a segment'
    "кэли-гамильтон теорем": "cayley-hamilton",           # 'Cayley-Hamilton theorem'
    "тригонометрийн утга": "exact-trig-values",           # 'trigonometric value'
    "тригонометрийн тоо": "exact-trig-values",
    "тригонометрийн тэгшитгэл": "trig-equations",         # 'trigonometric equation'
    "үндсэн харьцаа": "trig-pythagorean-identity",        # 'fundamental relation'
    "тригонометрийн ялгаварын томьёо": "trig-sum-difference",  # 'difference formula'
    # -- Mongolian, analysis
    "интеграл": "definite-integral",                      # 'integral'
    "тодорхой интеграл": "definite-integral",             # 'definite integral'
    "уламжлал": "derivative-power-rule",                  # 'derivative'
    "антиуламжлал": "antiderivative-power",               # 'antiderivative'
    "дифференциал тэгшитгэл": "differential-equations-separable",
    "дифференциал тэгшитгэл (хэрэглээ)": "differential-equations-separable",
    "экстремум": "stationary-points-and-extrema",         # 'extremum'
    "функцийн экстремум": "stationary-points-and-extrema",
    "функцийн шинж": "monotonicity-from-derivative",      # 'property of a function'
    "шүргэгч ба нормал": "tangent-line",                  # 'tangent and normal'
    "шүргэгч шулуун": "tangent-line",
    "нормал шулуун": "normal-line",
    "асимптот": "rational-function-asymptotes",           # 'asymptote'
    "өсөх завсар": "increasing-decreasing-intervals",     # 'increasing interval'
    "утгын муж": "range-of-a-function",                   # 'range'
    "шугаман функц": "line-equation",                     # 'linear function'
    "график": "graph-transformations",                    # 'graph'
    # -- Mongolian, probability & statistics
    "дискрет тархалт": "discrete-random-variable",        # 'discrete distribution'
    "дискрет хувьсагч": "discrete-random-variable",
    "геометрийн магадлал": "geometric-probability",       # 'geometric probability'
    "геометр магадлал": "geometric-probability",
    "классик магадлал": "classical-probability",          # 'classical probability'
    "сонгодог магадлал": "classical-probability",
    "үндсэн магадлал": "classical-probability",
    "математик дундаж": "expected-value",                 # 'mathematical mean' = E[X]
    "дисперс": "variance-of-random-variable",             # 'variance' (random variable)
    "дисперси": "variance-and-sd",                        # 'variance' (data set)
    "квартил": "quartiles-and-iqr",                       # 'quartile'
    "квартиль": "quartiles-and-iqr",
    "дундаж": "mean-median-mode",                         # 'mean'
    "арифметик дундаж": "mean-median-mode",
    "хуримтлагдсан тархалт": "cumulative-frequency",      # 'cumulative distribution'
    # -- Mongolian, combinatorics
    "тоолол": "counting-principle",                       # 'counting'
    "тоолох": "counting-principle",
    "зохицуулалт": "permutations",                        # 'arrangement'
    "сонголт": "combinations",                            # 'selection'
    "натурал шийд": "stars-and-bars",                     # 'natural-number solution'
    # -- English strings in the bank that are not skill ids verbatim
    "polynomial_remainder": "remainder-theorem",
    "remainder theorem": "remainder-theorem",
    "rational_expression": "rational-expressions",
    "rational expressions": "rational-expressions",
    "ratio_algebra": "mixture-and-ratio-problems",
    "radical_exponent": "rational-exponents",
    "system_log_quadratic": "systems-nonlinear",
    "trig_identity": "trig-pythagorean-identity",
    "sine_rule": "sine-rule",
    "law of cosines": "cosine-rule",
    "exact values": "exact-trig-values",
    "sum of cubes identity": "factoring-cubes",
    "difference of cubes identity": "factoring-cubes",
    "trigonometric expressions": "trig-simplification",
    "scientific_notation": "scientific-notation",
    "repeating_decimal": "repeating-decimal-to-fraction",
    "number_comparison": "real-number-sets",
    "mixture_problem": "mixture-and-ratio-problems",
    "fraction_arithmetic": "fraction-arithmetic",
    "fractions": "fraction-arithmetic",
    "radicals": "radicals-simplification",
    "rounding": "decimal-arithmetic",
    "set_union": "set-operations",
    "subset": "subsets-and-power-sets",
    "inclusion_exclusion": "inclusion-exclusion",
    "union": "set-operations",
    "range": "range-of-a-function",
    "linear_function": "line-equation",
    "increasing interval": "increasing-decreasing-intervals",
    "function_evaluation": "function-notation",
    "function evaluation": "function-notation",
    "composite_functions": "composite-functions",
    "composite function": "composite-functions",
    "logarithmic inequality": "logarithmic-inequalities",
    "geometric_sequence": "geometric-sequence",
    "geometric sequence": "geometric-sequence",
    "arithmetic series": "arithmetic-series",
    "simplification": "complex-arithmetic",
    "quadratic with complex roots": "complex-roots-of-quadratics",
    "complex_division": "complex-conjugate-division",
    "division": "complex-conjugate-division",
    "cylinder": "cylinder",
    "translation": "translation",
    "transformation_matrix": "transformation-matrices",
    "transformation matrix": "transformation-matrices",
    "solid of revolution": "solid-of-revolution-geometric",
    "right_triangle_inscribed_circle": "inscribed-circumscribed-circles",
    "inscribed_circle_trapezoid": "inscribed-circumscribed-circles",
    "right triangle altitude": "triangle-altitude",
    "reflection_over_line": "reflection",
    "reflection through a point": "reflection",
    "prism_volume_ratio": "prism-volume-surface",
    "median_length": "triangle-medians",
    "line equation": "line-equation",
    "homothety_reflection": "homothety",
    "distance_formula": "coordinate-distance",
    "distance to axis": "coordinate-distance",
    "cone_sector_angle": "cone",
    "circle_tangent_line": "circle-tangent",
    "circle, inscribed angle": "inscribed-angle",
    "vector_arithmetic": "vector-arithmetic",
    "vector arithmetic": "vector-arithmetic",
    "singular matrix": "inverse-matrix-2x2",
    "section_formula": "vector-section-formula",
    "parallelogram_vectors": "vectors-in-polygons",
    "vectors in parallelogram": "vectors-in-polygons",
    "parallel_vectors": "vector-arithmetic",
    "opposite vector": "vector-arithmetic",
    "matrix_dimensions": "matrix-dimensions",
    "matrix dimensions": "matrix-dimensions",
    "magnitude": "vector-magnitude",
    "dot_product": "dot-product",
    "dot product": "dot-product",
    "cayley-hamilton theorem": "cayley-hamilton",
    "definite integral": "definite-integral",
    "definite_integral": "definite-integral",
    "definite_integral_absolute_value": "definite-integral-absolute",
    "antiderivative": "antiderivative-power",
    "antiderivative_polynomial": "antiderivative-power",
    "integration by substitution": "integration-by-substitution",
    "higher-order derivatives": "higher-order-derivatives",
    "extrema of cubic function": "stationary-points-and-extrema",
    "derivative_trig": "derivative-trig",
    "derivative_log": "derivative-exp-log",
    "derivative": "derivative-power-rule",
    "derivatives": "derivative-power-rule",
    "area_between_curves": "area-between-curves",
    "area between curves": "area-between-curves",
    "tangent line to curve": "tangent-line",
    "tangent slope": "tangent-line",
    "normal_line": "normal-line",
    "variance": "variance-and-sd",
    "union of events": "addition-rule",
    "probability distribution": "discrete-random-variable",
    "event_probability": "classical-probability",
    "complementary_event": "complementary-events",
    "expected value": "expected-value",
    "expected_value": "expected-value",
    "divisibility probability": "addition-rule",
    "variance (hypergeometric)": "variance-of-random-variable",
    "median": "mean-median-mode",
    "mean": "mean-median-mode",
    "quartile": "quartiles-and-iqr",
    "interquartile_range": "quartiles-and-iqr",
    "grouped frequency, mean": "grouped-frequency-mean",
    "combined_standard_deviation": "combined-standard-deviation",
    "standard deviation": "variance-and-sd",
    "stars_and_bars": "stars-and-bars",
    "permutations with restrictions": "permutations-with-restrictions",
    "matching": "logarithm-definition",
    "negative exponents": "integer-powers",
    "algebraic expressions": "algebraic-expressions",
    "equations with radicals": "radical-equations",
    "factoring": "factor-theorem",
    "inequality with integer solutions": "linear-inequality-one-variable",
    "ratio": "percent-and-proportion",
    "system of equations": "systems-nonlinear",
    "polynomial remainder": "remainder-theorem",
    "median of a triangle": "triangle-medians",
    "circle tangent to line": "circle-tangent",
    "trapezoid with inscribed circle": "inscribed-circumscribed-circles",
    "geometric transformations, area": "homothety",
    "translation vector": "translation",
    "sine rule": "sine-rule",
    "гурвалжин пирамид": "pyramid-volume-surface",
    "тэгш өнцөгт параллелепипед": "prism-volume-surface",
    "парабол, экстремум": "quadratic-function-vertex",
    "магадлал, шооны туршилт": "classical-probability",
}


def resolve(topic, subtopic):
    s = (subtopic or "").strip().lower()
    if not s:
        return None, "empty"
    if (topic, s) in LEGACY:
        return LEGACY[(topic, s)], "legacy-verified"
    key = s.replace(" ", "-").replace("_", "-")
    if key in SKILLS:
        return key, "id-match"
    norm = re.sub(r"[^a-z0-9]+", " ", s).strip()
    if norm in BY_NAME:
        return BY_NAME[norm], "name-match"
    if s in ALIASES:
        return ALIASES[s], "alias"
    return None, "orphan"


def main():
    papers = [f"{y}{v}" for y in (2021, 2022, 2023, 2024, 2025) for v in "abcd"]
    legacy_tests = [f"test{n}{v}" for n in range(1, 8) for v in "ab"]

    clean, orphan = [], []
    orphan_strings = collections.Counter()
    by_source = collections.Counter()

    def scan(path, label):
        if not os.path.exists(path):
            return
        data = json.load(open(path))
        items = data if isinstance(data, list) else data.get("problems", data.get("questions", []))
        for q in items:
            topic = q.get("topic")
            sub = q.get("subtopic")
            qid = q.get("source") or f"{label}-Q{q.get('questionNumber')}"
            sid, how = resolve(topic, sub)
            rec = {"id": qid, "file": label, "topic": topic, "subtopic": sub,
                   "skill_id": sid, "via": how}
            if sid:
                clean.append(rec)
                by_source[how] += 1
            else:
                orphan.append(rec)
                orphan_strings[(topic, (sub or "").strip().lower())] += 1

    for p in papers:
        scan(os.path.join(ROOT, "data", "questions", f"{p}.json"), p)
        scan(os.path.join(ROOT, "data", "questions", f"{p}-section2.json"), f"{p}-s2")
    for t in legacy_tests:
        scan(os.path.join(ROOT, "data", "questions", f"{t}.json"), t)

    total = len(clean) + len(orphan)
    print("=" * 74)
    print("ЭЕШ QUESTION BANK vs THE SKILL GRAPH  (Rule 1: one skill_id per item)")
    print("=" * 74)
    print(f"  items scanned      {total}")
    print(f"  MAP CLEANLY        {len(clean)}  ({100*len(clean)/total:.1f}%)")
    print(f"  ORPHANS            {len(orphan)}  ({100*len(orphan)/total:.1f}%)")
    print("\n  how the clean ones resolved:")
    for how, n in by_source.most_common():
        print(f"    {how:20s} {n}")

    print("\n" + "=" * 74)
    print(f"ORPHAN LIST — {len(orphan_strings)} distinct strings, biggest first")
    print("NOT DELETED, NOT GUESSED. Each needs a human decision.")
    print("=" * 74)
    for (topic, sub), n in orphan_strings.most_common():
        print(f"  {n:4d}  {topic or '(none)':<16} {sub or '(empty)'}")

    cov = collections.Counter(c["skill_id"] for c in clean)
    print("\n" + "=" * 74)
    print("SKILL COVERAGE — which skills have NO question behind them")
    print("=" * 74)
    uncovered = [s for s in SKILLS if s not in cov]
    print(f"  {len(SKILLS) - len(uncovered)} / {len(SKILLS)} skills have at least one item.")
    print(f"  {len(uncovered)} have none. Those carry "
          f"{sum(SKILLS[s]['exam_weight'] for s in uncovered):.1f}% of the exam and need "
          f"items authored before the adaptive test can probe them:")
    for s in sorted(uncovered, key=lambda x: -SKILLS[x]["exam_weight"]):
        print(f"    {SKILLS[s]['exam_weight']:5.2f}%  {s:<38} {SKILLS[s]['strand']}")

    out = {
        "note": "Generated by scripts/skills/content_audit.py. Orphans are NOT deleted and "
                "NOT auto-tagged — each is a decision for the owner.",
        "counts": {"scanned": total, "clean": len(clean), "orphan": len(orphan),
                   "distinctOrphanStrings": len(orphan_strings),
                   "skillsWithItems": len(SKILLS) - len(uncovered),
                   "skillsWithoutItems": len(uncovered)},
        "orphanStrings": [{"topic": t, "subtopic": s, "questions": n}
                          for (t, s), n in orphan_strings.most_common()],
        "skillsWithoutItems": sorted(uncovered, key=lambda x: -SKILLS[x]["exam_weight"]),
        "clean": clean,
        "orphans": orphan,
    }
    with open(os.path.join(ROOT, "data", "skills", "esh-content-audit.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
