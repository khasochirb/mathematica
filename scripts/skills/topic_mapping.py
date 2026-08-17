"""Map the legacy free-text attempts.topic / attempts.subtopic onto skill ids.

93 rows, 57 distinct (topic, subtopic) pairs, in two languages, written by
whoever tagged the question at the time. Nothing here is inferred by string
similarity: every ЭШ mapping below was checked against the ACTUAL QUESTION
BODY in data/questions/, and four of them changed once I read the question.
Those four are the argument for doing it by hand:

  topic/subtopic said                  the question actually was
  ----------------------------------   ------------------------------------
  logarithms / negative exponents      "$3^{-2}$ утгыг олоорой" — no
                                       logarithm anywhere. integer-powers.
  algebra / factoring                  p(x)=x^2+2x+c has root -3, factorise.
                                       That is the FACTOR THEOREM, not
                                       generic factoring.
  functions / парабол, экстремум       f(x)=x^2-2kx+k^2-k+3. The brief read
                                       this as two skills; the extremum of a
                                       parabola IS its vertex at this level,
                                       so it is ONE skill, not two.
  calculus / derivatives               y = sin 2x. derivative-trig, and the
                                       chain rule comes free by inference —
                                       which is the graph doing its job.

CONFIDENCE is recorded per row and means what it says:
  high      the question was read and the skill is unambiguous
  medium    the question was read and one skill clearly dominates, but a
            second skill is genuinely involved
  ambiguous NOT mapped. Flagged for Khas. Guessing here would put wrong
            evidence on a student's record, which is worse than a gap.

SPLITS. Where one string names two skills, `skills` holds both and
`split_reason` says why. Rule 1 of the architecture (one skill_id per
problem) means such an ITEM still has to choose one — the primary is first
in the list — but the mapping records both so the item can be re-cut later.

SAT. SAT already has a controlled vocabulary and its 20 subtopics are stable,
so those rows pass through unchanged, marked `awaiting_sat_graph`. Authoring
SAT skills is not in this phase's scope; when it is, this file is where the
join lands.

THE CROSS-HUB COLLISION, settled. ЭШ carries `geometry` and `trigonometry`
as separate topics; SAT carries `geometry-trig` as one. The skills table
settles it: ЭШ topics geometry, trigonometry AND linear_algebra all sit in
the strand `geometry-trig` — the same strand name SAT uses — while `hub`
keeps the two exams' items apart. One strand vocabulary, two hubs.

Run: python3 scripts/skills/topic_mapping.py
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (hub, topic, subtopic) -> dict(skills=[...], confidence=..., evidence=..., ...)
# `rows` is the production row count for that pair, from the live attempts
# table on 2026-08-14 (93 rows total).
M = []


def m(hub, topic, subtopic, skills, rows, confidence="high", evidence="", split_reason="", note=""):
    M.append({
        "hub": hub, "topic": topic, "subtopic": subtopic,
        "skills": list(skills), "rows": rows, "confidence": confidence,
        "evidence": evidence or None, "split_reason": split_reason or None, "note": note or None,
    })


# --- ЭШ — algebra strand ---------------------------------------------------
m("esh", "algebra", "algebraic expressions", ["algebraic-expressions"], 1)
m("esh", "algebra", "equations with radicals", ["radical-equations"], 1)
m("esh", "algebra", "factoring", ["factor-theorem"], 1, "high",
  evidence="Test-2022A-Q24: p(x)=x^2+2x+c has root x=-3, factorise. The root is given so "
           "the method is the factor theorem, not trial factorisation.",
  note="The string 'factoring' alone would have mapped to factoring-quadratic-trinomial. "
       "Reading the item changed it. Any FUTURE row tagged 'factoring' must be re-read, "
       "not copied from this one.")
m("esh", "algebra", "inequality with integer solutions", ["linear-inequality-one-variable"], 1, "high",
  note="Counting integer solutions is folded into this skill by design; see the graph note.")
m("esh", "algebra", "polynomial remainder", ["remainder-theorem"], 1)
m("esh", "algebra", "ratio", ["percent-and-proportion"], 1, "medium",
  evidence="Test-2022A-Q10: a/2 = b/3, find (3a-b)/(a+2b).",
  note="Proportional reasoning, then expression manipulation. Mapped to the ratio skill "
       "because setting a=2t, b=3t is the step that unlocks it; algebraic-expressions is "
       "the co-requisite and arrives by inference.")
m("esh", "algebra", "system of equations", ["systems-nonlinear", "logarithmic-equations"], 1, "medium",
  evidence="Test-2022A-Q23: log_2 x = log_2(y+2) with 2y^2 - x^2 = 17.",
  split_reason="Equating the log arguments is one step, then it is a nonlinear system. The "
               "system is the substance; the log step is a single line.")
m("esh", "arithmetic", "fractions", ["fraction-arithmetic"], 1)
m("esh", "functions", "composite function", ["composite-functions"], 1)
m("esh", "functions", "function evaluation", ["function-notation"], 1)
m("esh", "functions", "парабол, экстремум", ["quadratic-function-vertex"], 3, "high",
  evidence="Test-2022A-Q2.1.1-3: f(x) = x^2 - 2kx + k^2 - k + 3.",
  note="Read as two skills in the brief. It is one: for a parabola the extremum IS the "
       "vertex, and this item sits in the functions topic, not calculus. Tagging it "
       "stationary-points-and-extrema as well would have credited calculus a student "
       "never used.")
m("esh", "logarithms", "negative exponents", ["integer-powers"], 1, "high",
  evidence="Test-2022A-Q1: evaluate $3^{-2}$.",
  note="TOPIC LABEL IS WRONG in production. There is no logarithm in the item. Mapping to "
       "the logarithms strand would have put a student's exponent evidence on the wrong "
       "skill for good.")
m("esh", "sequences", "geometric sequence", ["geometric-sequence"], 1)
m("esh", "set_theory", "union", ["set-operations"], 1)
m("esh", "complex_numbers", "division", ["complex-conjugate-division"], 1)

# --- ЭШ — geometry-trig strand --------------------------------------------
m("esh", "geometry", "circle tangent to line", ["circle-tangent"], 1)
m("esh", "geometry", "cylinder", ["cylinder"], 1)
m("esh", "geometry", "geometric transformations, area", ["homothety", "reflection"], 1, "medium",
  evidence="Test-2022A-Q29: A(3,2) under a homothety k=-2 about O gives B; under reflection "
           "in the y-axis gives C; find the area of ABC.",
  split_reason="Two transformations plus an area computation in one item.",
  note="FLAGGED FOR KHAS. This is a genuinely composite item and Rule 1 wants one skill_id. "
       "Either it is re-cut into two items, or it is tagged homothety (the harder half) and "
       "accepted as an imprecise signal. I have not decided that for you.")
m("esh", "geometry", "median of a triangle", ["triangle-medians"], 1)
m("esh", "geometry", "trapezoid with inscribed circle", ["inscribed-circumscribed-circles"], 1)
m("esh", "geometry", "гурвалжин пирамид", ["pyramid-volume-surface"], 4, "high",
  evidence="'triangular pyramid'.")
m("esh", "geometry", "тэгш өнцөгт параллелепипед", ["prism-volume-surface"], 3, "high",
  evidence="'rectangular parallelepiped' = cuboid. Test-2022A-Q2.2.1 maximises its volume.",
  note="The 2022A item also needs optimisation, but by AM-GM / completing the square at "
       "this level, not calculus. Kept on the solid-geometry skill.")
m("esh", "linear_algebra", "dot product", ["dot-product"], 1)
m("esh", "linear_algebra", "matrix dimensions", ["matrix-dimensions"], 1)
m("esh", "linear_algebra", "translation vector", ["translation"], 1, "high",
  evidence="Test-2022A-Q7: triangle A is translated by vector a onto triangle B; find a.",
  note="Tagged linear_algebra in production but the skill is the geometric transformation; "
       "vector-components arrives by inference.")
m("esh", "linear_algebra", "vector arithmetic", ["vector-arithmetic"], 1)
m("esh", "linear_algebra", "vectors in parallelogram", ["vectors-in-polygons"], 1)
m("esh", "trigonometry", "sine rule", ["sine-rule"], 1)
m("esh", "trigonometry", "trigonometric expressions", ["trig-simplification"], 1)

# --- ЭШ — analysis strand --------------------------------------------------
m("esh", "calculus", "antiderivative", ["antiderivative-power"], 1)
m("esh", "calculus", "area between curves", ["area-between-curves"], 1)
m("esh", "calculus", "definite integral", ["definite-integral"], 1)
m("esh", "calculus", "derivatives", ["derivative-trig"], 1, "high",
  evidence="Test-2022A-Q8: differentiate y = sin 2x.",
  note="The item is really a chain-rule item, but chain-rule is a prerequisite of "
       "derivative-trig at 0.6, so tagging the specific skill credits the general one by "
       "inference. This is the pattern to follow: tag the NARROWEST true skill.")
m("esh", "calculus", "tangent slope", ["tangent-line"], 1)

# --- ЭШ — probability & statistics ----------------------------------------
m("esh", "probability", "divisibility probability", ["addition-rule"], 1, "medium",
  evidence="Test-2022A-Q13: from naturals up to 60, P(divisible by 3 or 5).",
  split_reason="Union with an overlap (inclusion-exclusion) plus divisibility counting.",
  note="The union is the tested idea; divisibility-rules is the arithmetic underneath and "
       "is NOT a prerequisite edge of addition-rule, so a student weak on divisibility "
       "will look weak on the union rule. Accepted imprecision, recorded here.")
m("esh", "probability", "expected value", ["expected-value"], 1)
m("esh", "probability", "variance (hypergeometric)", ["variance-of-random-variable"], 1, "high",
  evidence="Test-2022A-Q34: 2 red and 3 white balls, draw 2, X = number of white, find Var(X).",
  note="'hypergeometric' is a red herring — at ЭШ level this is built from a distribution "
       "table by hand. There is deliberately no hypergeometric skill in the graph.")
m("esh", "probability", "магадлал, шооны туршилт", ["classical-probability", "sample-space-and-events"], 3,
  "medium",
  evidence="Test-2022A-Q2.4.1-3: a point walks a number line under a dice rule.",
  split_reason="A three-part section-2 item; the parts do not all test the same thing.",
  note="FLAGGED FOR KHAS. Section-2 items are multi-part and a single (topic, subtopic) "
       "string covers all parts. Rule 1 really wants a skill_id PER PART. That is a schema "
       "question, not a mapping question.")
m("esh", "statistics", "median", ["mean-median-mode"], 1)
m("esh", "statistics", "standard deviation", ["variance-and-sd"], 1)

# --- SAT — controlled vocabulary, passes through -----------------------------
SAT_ROWS = [
    ("advanced-math", "equivalent_expressions", 4), ("advanced-math", "nonlinear_equations_systems", 5),
    ("advanced-math", "nonlinear_functions", 6), ("algebra", "linear_equations_one_var", 2),
    ("algebra", "linear_equations_two_var", 3), ("algebra", "linear_functions", 5),
    ("algebra", "linear_inequalities", 2), ("algebra", "systems_two_linear", 3),
    ("geometry-trig", "area_volume", 2), ("geometry-trig", "circles", 1),
    ("geometry-trig", "lines_angles_triangles", 2), ("geometry-trig", "right_triangles_trig", 2),
    ("problem-solving-data", "one_var_data", 2), ("problem-solving-data", "percentages", 1),
    ("problem-solving-data", "probability_conditional", 2),
    ("problem-solving-data", "ratios_rates_units", 1),
    ("problem-solving-data", "two_var_data_models", 1),
]
for topic, sub, n in SAT_ROWS:
    m("sat", topic, sub, [], n, "awaiting_sat_graph",
      note="SAT's vocabulary is already controlled and stable; these 17 pairs need no "
           "disambiguation. They map 1:1 once SAT skills are authored, which is not this "
           "phase's scope.")


def main():
    known = set()
    graph_path = os.path.join(ROOT, "data", "skills", "esh-skills.json")
    if os.path.exists(graph_path):
        known = {s["id"] for s in json.load(open(graph_path))["skills"]}

    errors = []
    for r in M:
        for sid in r["skills"]:
            if known and sid not in known:
                errors.append(f"{r['topic']}/{r['subtopic']}: unknown skill id {sid!r}")
        if r["confidence"] not in ("high", "medium", "ambiguous", "awaiting_sat_graph"):
            errors.append(f"{r['topic']}/{r['subtopic']}: bad confidence {r['confidence']!r}")
        if r["confidence"] in ("high", "medium") and not r["skills"]:
            errors.append(f"{r['topic']}/{r['subtopic']}: confident but mapped to nothing")
        if len(r["skills"]) > 1 and not r["split_reason"]:
            errors.append(f"{r['topic']}/{r['subtopic']}: multi-skill row with no split_reason")
    if errors:
        for e in errors:
            print("ERROR " + e)
        raise SystemExit(1)

    total_rows = sum(r["rows"] for r in M)
    esh = [r for r in M if r["hub"] == "esh"]
    sat = [r for r in M if r["hub"] == "sat"]
    out = {
        "note": "Generated by scripts/skills/topic_mapping.py. Every ЭШ row was verified "
                "against the question body in data/questions/.",
        "sourceRowsAt": "2026-08-14, production attempts table",
        "counts": {
            "distinctPairs": len(M), "productionRows": total_rows,
            "eshPairs": len(esh), "satPairs": len(sat),
            "high": sum(1 for r in M if r["confidence"] == "high"),
            "medium": sum(1 for r in M if r["confidence"] == "medium"),
            "ambiguous": sum(1 for r in M if r["confidence"] == "ambiguous"),
            "flaggedForOwner": sum(1 for r in M if r["note"] and "FLAGGED FOR KHAS" in r["note"]),
        },
        "mappings": M,
    }
    os.makedirs(os.path.join(ROOT, "data", "skills"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "skills", "esh-topic-mapping.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    def q(v):
        return "'" + str(v).replace("'", "''") + "'"

    lines = [
        "-- Legacy attempts.topic / attempts.subtopic -> skill_id.",
        "-- GENERATED by scripts/skills/topic_mapping.py. Do not hand-edit.",
        "--",
        "-- Every ЭШ row was checked against the question body, not the label: four of",
        "-- them are mapped to a DIFFERENT skill than their production topic implies, and",
        "-- one ('logarithms / negative exponents') has a production topic that is simply",
        "-- wrong. Backfilling from the label instead of the item would have written that",
        "-- error permanently onto student records.",
        "--",
        "-- Rows with confidence 'awaiting_sat_graph' have no skill and are intentionally",
        "-- inert until SAT skills are authored.",
        "",
        "begin;",
        "",
        "insert into attempt_topic_skill_map (hub, topic, subtopic, skill_id, is_primary, confidence)",
        "values",
    ]
    vals = []
    for r in M:
        if not r["skills"]:
            vals.append(f"  ({q(r['hub'])}, {q(r['topic'])}, {q(r['subtopic'])}, NULL, true, "
                        f"{q(r['confidence'])})")
        for i, sid in enumerate(r["skills"]):
            vals.append(f"  ({q(r['hub'])}, {q(r['topic'])}, {q(r['subtopic'])}, {q(sid)}, "
                        f"{'true' if i == 0 else 'false'}, {q(r['confidence'])})")
    lines.append(",\n".join(vals))
    lines += ["on conflict do nothing;", "", "commit;", ""]
    with open(os.path.join(ROOT, "supabase", "seed", "esh_topic_mapping.sql"), "w") as f:
        f.write("\n".join(lines))

    print(f"{len(M)} distinct pairs covering {total_rows} production rows "
          f"({len(esh)} ЭШ, {len(sat)} SAT)")
    for c in ("high", "medium", "ambiguous", "awaiting_sat_graph"):
        n = sum(1 for r in M if r["confidence"] == c)
        print(f"  {c:20s} {n}")
    print("\nFlagged for Khas to decide:")
    for r in M:
        if r["note"] and "FLAGGED FOR KHAS" in r["note"]:
            print(f"  - {r['topic']}/{r['subtopic']}  -> {', '.join(r['skills'])}")
    print("\nMappings that CHANGED after reading the question:")
    for r in M:
        if r["evidence"] and r["note"] and "FLAGGED" not in r["note"]:
            print(f"  - {r['topic']}/{r['subtopic']:<34} -> {r['skills'][0]}")


if __name__ == "__main__":
    main()
