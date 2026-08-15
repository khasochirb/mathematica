"""The ЭЕШ prerequisite skill graph — source of truth.

WHY THIS FILE EXISTS AND WHY IT IS NOT SQL
------------------------------------------
The placement test will directly probe ~30 skills but must report on all of
them. It does that by INFERENCE down the prerequisite edges: solve a
logarithmic equation and we credit exponent rules, the logarithm definition
and integer powers, because they are genuinely required to have solved it.
The accuracy of that inference is entirely a function of how honest the edges
are. A wrong edge silently credits a student with something they cannot do,
and nobody ever sees the error — not the student, not the teacher, not the
score report. So every edge here is a claim to defend to a parent.

Keeping the graph as data (not as hand-written SQL) buys three things:

1. INVARIANTS ARE MECHANICAL. `verify()` refuses to emit anything if the graph
   has a cycle, a dangling edge, a duplicate id, a strength outside (0,1], a
   cross-strand edge that was not declared deliberate, or exam weights that do
   not sum to the measured strand shares. A prerequisite graph that silently
   grows a cycle would make inference diverge; it now fails the build instead.
2. THE WEIGHTS ARE DERIVED, NOT TYPED. `exam_weight` is computed from the
   MEASURED share of each topic in 20 real past papers
   (data/esh/exam-weights.json, 980 questions) split across that topic's
   skills by a small integer `share`. The judgement is visible as an integer
   I can defend; the arithmetic is exact by construction.
3. THE SCHEMA IS AN EMITTER, NOT THE ASSET. The expensive asset is the 160
   skills and their edges. Emitting SQL is ~40 lines at the bottom of this
   file, so if the table shape differs from what lands in the architecture
   doc, that is a re-run and not a re-author.

GRANULARITY RULE (applied to every entry below)
    A skill is teachable in ~10 minutes and testable in 3 questions.
    "Logarithms" is a topic. "Log product rule" is a skill.

EDGE STRENGTH SCALE — this field does real work, inference weights by it:
    1.0  Hard blocker. You cannot do S at all without this. Failing the
         prerequisite guarantees failing S.
    0.8  Strong. Every standard route through S uses it; failing it breaks
         S in almost every case.
    0.6  Moderate. The standard method needs it, but a competent student has
         another route (e.g. factoring vs the quadratic formula).
    0.4  Helpful. Needed for the harder cases of S, or it removes the
         arithmetic friction rather than the idea.
    Below 0.4 is not asserted at all. A 0.2 edge adds noise to inference
    without adding information, and every edge costs accuracy when wrong.

WHAT IS DELIBERATELY *NOT* HERE
    - name_mn. Mongolian is authored in Phase 3 by a Mongolian-speaking maths
      teacher expressing the idea, never translated from these strings. The
      column is emitted NULL.
    - Sub-skills. Two levels only: strand -> skill.
    - IB and AP skills.
    - Curriculum order masquerading as dependency. Textbooks teach the unit
      circle before vectors; neither needs the other. Only real dependencies
      are edges.

Run:  python3 scripts/skills/esh_graph.py
Emits data/skills/esh-skills.json and supabase/seed/esh_skills.sql
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Strand of each topic. Reuses the taxonomy already shipped in
# lib/esh-questions.ts (ESH_DOMAINS) rather than inventing a second one — the
# hub, the question bank and this graph must agree or analytics splits.
STRAND_OF_TOPIC = {
    "arithmetic": "algebra",
    "algebra": "algebra",
    "set_theory": "algebra",
    "functions": "algebra",
    "logarithms": "algebra",
    "sequences": "algebra",
    "complex_numbers": "algebra",
    "geometry": "geometry-trig",
    "trigonometry": "geometry-trig",
    "linear_algebra": "geometry-trig",
    "calculus": "analysis",
    "probability": "probability-statistics",
    "statistics": "probability-statistics",
    "combinatorics": "combinatorics",
}

# Strand shares MEASURED from 20 real past papers, not invented.
# Source: data/esh/exam-weights.json (scripts/esh/build_exam_weights.py).
# Premium tests are excluded there so our own authoring cannot bias them.
STRAND_SHARE_PCT = {
    "algebra": 36.1,
    "geometry-trig": 30.1,
    "analysis": 16.2,
    "probability-statistics": 15.5,
    "combinatorics": 2.0,
}

# Per-topic measured share of the whole exam, same source. exam_weight for a
# skill is TOPIC_SHARE_PCT[topic] * share / (sum of shares in that topic).
TOPIC_SHARE_PCT = {
    "arithmetic": 2.9, "algebra": 19.4, "set_theory": 2.0, "functions": 8.9,
    "logarithms": 0.7, "sequences": 0.8, "complex_numbers": 1.4,
    "geometry": 20.6, "trigonometry": 3.6, "linear_algebra": 5.9,
    "calculus": 16.2,
    "probability": 10.3, "statistics": 5.2,
    "combinatorics": 2.0,
}


@dataclass
class Skill:
    id: str
    topic: str
    name_en: str
    difficulty: int          # typical_difficulty, 1-5
    share: int               # relative weight WITHIN its topic (see above)
    prereqs: list = field(default_factory=list)   # [(prereq_id, strength), ...]
    note: str = ""           # why an unobvious edge or grouping exists


def S(id, topic, name_en, difficulty, share, prereqs=(), note=""):
    return Skill(id, topic, name_en, difficulty, share, list(prereqs), note)


# ===========================================================================
# STRAND 1 — ALGEBRA (36.1% of the exam)
# The largest strand and, more importantly, the one that carries the
# foundational chain: most inference in every other strand terminates here.
# ===========================================================================

ARITHMETIC = [
    S("integer-operations", "arithmetic", "Signed integer arithmetic and order of operations", 1, 3,
      note="Root of the graph. Nothing precedes it; almost everything descends from it."),
    S("fraction-arithmetic", "arithmetic", "Add, subtract, multiply and divide fractions", 1, 3,
      [("integer-operations", 1.0)]),
    S("decimal-arithmetic", "arithmetic", "Decimal place value, rounding and estimation", 1, 4,
      [("integer-operations", 1.0)]),
    S("repeating-decimal-to-fraction", "arithmetic", "Convert a repeating decimal to a fraction", 3, 2,
      [("fraction-arithmetic", 0.8), ("decimal-arithmetic", 0.6), ("linear-equation-one-variable", 0.8)],
      note="The standard 10x-x method IS solving a linear equation; without that the topic is a memorised trick."),
    S("integer-powers", "arithmetic", "Powers with integer exponents, including negatives", 2, 3,
      [("integer-operations", 1.0), ("fraction-arithmetic", 0.6)]),
    S("radicals-simplification", "arithmetic", "Simplify surds and nth roots", 2, 3,
      [("integer-powers", 0.8), ("prime-factorisation", 0.8)]),
    S("prime-factorisation", "arithmetic", "Prime factorisation, HCF and LCM", 2, 2,
      [("integer-operations", 0.8)]),
    S("divisibility-rules", "arithmetic", "Divisibility tests and remainder reasoning", 2, 2,
      [("integer-operations", 0.8)]),
    S("scientific-notation", "arithmetic", "Write and compute in standard form", 2, 2,
      [("integer-powers", 1.0), ("decimal-arithmetic", 0.8)]),
    S("real-number-sets", "arithmetic", "Rational vs irrational; ordering and comparing reals", 2, 2,
      [("fraction-arithmetic", 0.6), ("radicals-simplification", 0.6)]),
    S("percent-and-proportion", "arithmetic", "Percent of, percent change, ratio and proportion", 2, 3,
      [("fraction-arithmetic", 1.0), ("decimal-arithmetic", 0.8)]),
]

SET_THEORY = [
    S("set-notation", "set_theory", "Set notation, membership and set-builder form", 1, 3,
      [("real-number-sets", 0.6)]),
    S("subsets-and-power-sets", "set_theory", "Subsets, proper subsets and counting subsets", 2, 3,
      [("set-notation", 1.0)]),
    S("set-operations", "set_theory", "Union, intersection, complement and Venn diagrams", 2, 6,
      [("set-notation", 1.0)],
      note="Venn diagrams are not a separate skill: on this exam they are how set operations "
           "are presented, and a student who can do one can do the other."),
    S("inclusion-exclusion", "set_theory", "Inclusion–exclusion for two and three sets", 3, 4,
      [("set-operations", 1.0)]),
    S("interval-notation", "set_theory", "Intervals on the real line and their unions", 2, 3,
      [("set-notation", 0.8), ("real-number-sets", 0.8)]),
]

ALGEBRA_CORE = [
    S("algebraic-expressions", "algebra", "Evaluate and simplify algebraic expressions", 1, 4,
      [("integer-operations", 1.0)]),
    S("like-terms-and-distribution", "algebra", "Collect like terms and expand brackets", 1, 4,
      [("algebraic-expressions", 1.0)]),
    S("linear-equation-one-variable", "algebra", "Solve a linear equation in one variable", 1, 5,
      [("like-terms-and-distribution", 1.0)]),
    S("rearranging-formulas", "algebra", "Change the subject of a formula", 2, 3,
      [("linear-equation-one-variable", 1.0)]),
    S("linear-inequality-one-variable", "algebra", "Solve a linear inequality and list its integer solutions", 2, 6,
      [("linear-equation-one-variable", 1.0), ("interval-notation", 0.8)],
      note="Counting the integer solutions is folded in rather than split off: it is the same "
           "lesson, and the error is the endpoint, which is the inequality skill itself."),
    S("absolute-value-equations", "algebra", "Solve equations containing absolute value", 3, 3,
      [("linear-equation-one-variable", 1.0), ("integer-operations", 0.8)]),
    S("absolute-value-inequalities", "algebra", "Solve inequalities containing absolute value", 3, 3,
      [("absolute-value-equations", 0.8), ("linear-inequality-one-variable", 1.0), ("interval-notation", 0.8)]),
    S("polynomial-arithmetic", "algebra", "Add, subtract and multiply polynomials", 2, 4,
      [("like-terms-and-distribution", 1.0), ("integer-powers", 0.8)]),
    S("special-products", "algebra", "Square of a binomial and difference of two squares", 2, 4,
      [("polynomial-arithmetic", 1.0)]),
    S("factoring-common-factor", "algebra", "Factor out the highest common factor", 2, 4,
      [("polynomial-arithmetic", 1.0), ("prime-factorisation", 0.6)]),
    S("factoring-quadratic-trinomial", "algebra", "Factor a quadratic trinomial", 2, 5,
      [("factoring-common-factor", 0.8), ("special-products", 0.8)]),
    S("factoring-by-grouping", "algebra", "Factor a four-term expression by grouping", 3, 3,
      [("factoring-common-factor", 1.0)]),
    S("factoring-cubes", "algebra", "Sum and difference of two cubes", 3, 3,
      [("special-products", 0.8), ("polynomial-arithmetic", 0.8)]),
    S("rational-expressions", "algebra", "Simplify and combine rational expressions", 3, 7,
      [("factoring-quadratic-trinomial", 1.0), ("factoring-common-factor", 1.0),
       ("fraction-arithmetic", 1.0)]),
    S("rational-equations", "algebra", "Solve equations with the unknown in a denominator", 3, 3,
      [("rational-expressions", 1.0), ("linear-equation-one-variable", 1.0)],
      note="Extraneous roots are the whole point; the check step belongs to this skill."),
    S("quadratic-by-factoring", "algebra", "Solve a quadratic equation by factoring", 2, 4,
      [("factoring-quadratic-trinomial", 1.0), ("linear-equation-one-variable", 0.8)]),
    S("completing-the-square", "algebra", "Complete the square", 3, 3,
      [("special-products", 1.0), ("fraction-arithmetic", 0.8)]),
    S("quadratic-formula", "algebra", "Solve a quadratic with the quadratic formula", 2, 4,
      [("radicals-simplification", 0.8), ("quadratic-by-factoring", 0.6)],
      note="0.6 to factoring, not 1.0: the formula is a genuine alternative route, not a follow-on."),
    S("discriminant", "algebra", "Use the discriminant to determine the nature of the roots", 3, 4,
      [("quadratic-formula", 1.0), ("radicals-simplification", 0.6)]),
    S("vieta-formulas", "algebra", "Relate the sum and product of roots to the coefficients", 3, 4,
      [("quadratic-formula", 0.8), ("polynomial-arithmetic", 0.8)],
      note="Heavily used in ЭЕШ — it answers 'find the sum of the roots' without solving."),
    S("quadratic-inequalities", "algebra", "Solve a quadratic inequality", 3, 4,
      [("quadratic-by-factoring", 1.0), ("linear-inequality-one-variable", 0.8), ("interval-notation", 0.8)]),
    S("systems-two-linear", "algebra", "Solve a system of two linear equations", 2, 4,
      [("linear-equation-one-variable", 1.0), ("rearranging-formulas", 0.8)]),
    S("systems-three-linear", "algebra", "Solve a system of three linear equations", 3, 2,
      [("systems-two-linear", 1.0)]),
    S("systems-nonlinear", "algebra", "Solve a system with one non-linear equation", 4, 3,
      [("systems-two-linear", 1.0), ("quadratic-by-factoring", 1.0)]),
    S("radical-equations", "algebra", "Solve equations containing a square root", 3, 3,
      [("radicals-simplification", 1.0), ("quadratic-by-factoring", 0.8)],
      note="Squaring both sides creates extraneous roots; checking is part of the skill."),
    S("polynomial-division", "algebra", "Divide polynomials by long or synthetic division", 3, 3,
      [("polynomial-arithmetic", 1.0)]),
    S("remainder-theorem", "algebra", "Find a remainder by evaluating the polynomial", 3, 5,
      [("polynomial-division", 0.6), ("function-notation", 0.8)],
      note="0.6 only to long division: the theorem REPLACES the division. Its real prerequisite is "
           "being able to substitute into a polynomial, which is function evaluation."),
    S("factor-theorem", "algebra", "Use the factor theorem to factor a cubic", 3, 3,
      [("remainder-theorem", 1.0), ("polynomial-division", 0.8), ("factoring-quadratic-trinomial", 0.8)]),
    S("binomial-theorem", "algebra", "Expand a binomial power and find a specific term", 4, 4,
      [("polynomial-arithmetic", 0.8), ("integer-powers", 0.8), ("combinations", 1.0)],
      note="DELIBERATE CROSS-STRAND EDGE. The general term is C(n,k)a^(n-k)b^k — a student who "
           "cannot evaluate a binomial coefficient cannot do this, whatever the syllabus says."),
    S("rate-and-work-problems", "algebra", "Set up and solve speed, distance and work problems", 3, 3,
      [("linear-equation-one-variable", 1.0), ("percent-and-proportion", 0.8), ("rational-equations", 0.6)]),
    S("mixture-and-ratio-problems", "algebra", "Set up and solve mixture and ratio word problems", 3, 3,
      [("percent-and-proportion", 1.0), ("systems-two-linear", 0.8)]),
]

FUNCTIONS = [
    S("function-notation", "functions", "Function notation and evaluating f(x)", 1, 5,
      [("algebraic-expressions", 1.0)]),
    S("domain-of-a-function", "functions", "Find the domain of a function", 3, 4,
      [("function-notation", 1.0), ("interval-notation", 0.8), ("rational-expressions", 0.6),
       ("radicals-simplification", 0.6)]),
    S("range-of-a-function", "functions", "Find the range of a function", 3, 4,
      [("domain-of-a-function", 0.8), ("quadratic-function-vertex", 0.6)]),
    S("composite-functions", "functions", "Form and evaluate a composite function", 3, 4,
      [("function-notation", 1.0)]),
    S("inverse-functions", "functions", "Find and verify an inverse function", 3, 3,
      [("function-notation", 1.0), ("rearranging-formulas", 1.0)]),
    S("quadratic-function-vertex", "functions", "Vertex, axis of symmetry and direction of a parabola", 2, 8,
      [("function-notation", 0.8), ("completing-the-square", 0.8), ("quadratic-by-factoring", 0.6),
       ("discriminant", 0.6)],
      note="Reading a parabola off its graph is the same skill run backwards, so it is not split off."),
    S("increasing-decreasing-intervals", "functions", "Identify intervals where a function increases or decreases", 3, 4,
      [("function-notation", 0.8), ("interval-notation", 0.8), ("quadratic-function-vertex", 0.6)]),
    S("graph-transformations", "functions", "Translate, stretch and reflect a graph, including |f(x)|", 3, 5,
      [("function-notation", 1.0), ("absolute-value-equations", 0.6)]),
    S("piecewise-functions", "functions", "Evaluate and sketch a piecewise function", 3, 2,
      [("function-notation", 1.0), ("interval-notation", 1.0)]),
    S("rational-function-asymptotes", "functions", "Find vertical and horizontal asymptotes", 4, 3,
      [("rational-expressions", 1.0), ("domain-of-a-function", 1.0)]),
    S("exponential-and-log-graphs", "functions", "Recognise and sketch exponential and logarithmic graphs", 3, 3,
      [("exponent-rules", 1.0), ("logarithm-definition", 1.0), ("graph-transformations", 0.6),
       ("inverse-functions", 0.6)]),
]

LOGS = [
    # The chain the brief names as the worked example. It is short, low-weight
    # on the exam (0.7%) and disproportionately valuable to inference, because
    # every link is a hard blocker.
    S("exponent-rules", "logarithms", "Product, quotient and power rules for exponents", 2, 4,
      [("integer-powers", 1.0)]),
    S("rational-exponents", "logarithms", "Fractional exponents and their radical form", 3, 3,
      [("exponent-rules", 1.0), ("radicals-simplification", 1.0)]),
    S("exponential-equations", "logarithms", "Solve equations by matching bases", 3, 3,
      [("exponent-rules", 1.0)]),
    S("logarithm-definition", "logarithms", "The definition of a logarithm and conversion to exponential form", 3, 4,
      [("exponent-rules", 1.0)]),
    S("log-product-rule", "logarithms", "log(ab) = log a + log b", 3, 3,
      [("logarithm-definition", 1.0)]),
    S("log-quotient-rule", "logarithms", "log(a/b) = log a − log b", 3, 2,
      [("logarithm-definition", 1.0)]),
    S("log-power-rule", "logarithms", "log(a^n) = n log a", 3, 3,
      [("logarithm-definition", 1.0), ("exponent-rules", 0.8)]),
    S("change-of-base", "logarithms", "Change the base of a logarithm", 4, 2,
      [("logarithm-definition", 1.0), ("log-power-rule", 0.6)]),
    S("logarithmic-equations", "logarithms", "Solve logarithmic equations", 4, 4,
      [("log-product-rule", 1.0), ("log-power-rule", 1.0), ("logarithm-definition", 1.0),
       ("quadratic-by-factoring", 0.6), ("domain-of-a-function", 0.6)],
      note="The domain edge is the whole trap: log arguments must stay positive, so a solution "
           "that satisfies the algebra can still be rejected."),
    S("logarithmic-inequalities", "logarithms", "Solve logarithmic inequalities", 5, 3,
      [("logarithmic-equations", 1.0), ("linear-inequality-one-variable", 1.0)],
      note="Base < 1 reverses the inequality — the single most common error in this skill."),
]

SEQUENCES = [
    S("arithmetic-sequence", "sequences", "nth term of an arithmetic sequence", 2, 4,
      [("algebraic-expressions", 1.0), ("function-notation", 0.6), ("linear-equation-one-variable", 0.8)]),
    S("arithmetic-series", "sequences", "Sum of an arithmetic series", 3, 3,
      [("arithmetic-sequence", 1.0)]),
    S("geometric-sequence", "sequences", "nth term of a geometric sequence", 3, 4,
      [("algebraic-expressions", 1.0), ("exponent-rules", 0.8)]),
    S("geometric-series", "sequences", "Sum of a geometric series, finite and infinite", 3, 4,
      [("geometric-sequence", 1.0)]),
]

COMPLEX = [
    S("imaginary-unit", "complex_numbers", "The imaginary unit and powers of i", 2, 3,
      [("integer-powers", 1.0), ("radicals-simplification", 0.8)]),
    S("complex-arithmetic", "complex_numbers", "Add, subtract and multiply complex numbers", 3, 4,
      [("imaginary-unit", 1.0), ("polynomial-arithmetic", 0.8)]),
    S("complex-conjugate-division", "complex_numbers", "Divide complex numbers using the conjugate", 3, 4,
      [("complex-arithmetic", 1.0), ("special-products", 0.8), ("rational-expressions", 0.6)]),
    S("complex-roots-of-quadratics", "complex_numbers", "Quadratics with complex roots", 3, 4,
      [("quadratic-formula", 1.0), ("discriminant", 1.0), ("imaginary-unit", 1.0)]),
]

# ===========================================================================
# STRAND 2 — GEOMETRY & TRIGONOMETRY (30.1%)
# Geometry alone is 20.6%, the single largest topic on the paper.
# ===========================================================================

GEOMETRY = [
    S("angles-and-parallel-lines", "geometry", "Angles on lines and with parallels", 1, 3,
      [("linear-equation-one-variable", 0.6)]),
    S("triangle-angle-sum", "geometry", "Angle sum, exterior angle and isosceles triangles", 1, 5,
      [("angles-and-parallel-lines", 1.0)]),
    S("pythagoras", "geometry", "Pythagoras' theorem and its converse", 2, 4,
      [("radicals-simplification", 0.8), ("quadratic-by-factoring", 0.4)]),
    S("special-right-triangles", "geometry", "30–60–90 and 45–45–90 triangles", 2, 3,
      [("pythagoras", 1.0), ("radicals-simplification", 0.8)]),
    S("triangle-similarity", "geometry", "Similar triangles and the ratio of sides", 2, 4,
      [("triangle-angle-sum", 1.0), ("percent-and-proportion", 1.0)]),
    S("triangle-area", "geometry", "Area of a triangle by base–height and by ½ab sin C", 2, 4,
      [("triangle-angle-sum", 0.8), ("right-triangle-ratios", 0.6)]),
    S("triangle-altitude", "geometry", "Altitudes, including the altitude to the hypotenuse", 3, 3,
      [("triangle-similarity", 1.0), ("pythagoras", 0.8)]),
    S("triangle-medians", "geometry", "Medians, the centroid and the median-length formula", 3, 4,
      [("triangle-similarity", 0.8), ("pythagoras", 0.8), ("coordinate-midpoint", 0.6)]),
    S("quadrilateral-properties", "geometry", "Parallelograms, rectangles, rhombuses and squares", 2, 3,
      [("angles-and-parallel-lines", 1.0), ("triangle-angle-sum", 0.6)]),
    S("trapezoid-properties", "geometry", "Trapezoid properties and area", 2, 3,
      [("quadrilateral-properties", 1.0), ("triangle-area", 0.8)]),
    S("polygon-angles", "geometry", "Interior and exterior angles of a polygon", 2, 2,
      [("triangle-angle-sum", 1.0)]),
    S("circle-parts", "geometry", "Radius, chord, arc, sector and segment", 1, 3,
      [("angles-and-parallel-lines", 0.6)]),
    S("inscribed-angle", "geometry", "Inscribed angle and angle at the centre", 3, 4,
      [("circle-parts", 1.0), ("triangle-angle-sum", 1.0)]),
    S("circle-tangent", "geometry", "Tangent–radius perpendicularity and tangent length", 3, 4,
      [("circle-parts", 1.0), ("pythagoras", 1.0)]),
    S("chords-and-power-of-a-point", "geometry", "Intersecting chords and secant–tangent relations", 4, 3,
      [("circle-tangent", 0.8), ("triangle-similarity", 1.0), ("inscribed-angle", 0.8)]),
    S("circle-area-and-arc", "geometry", "Circumference, area, arc length and sector area", 2, 4,
      [("circle-parts", 1.0), ("percent-and-proportion", 0.8)]),
    S("inscribed-circumscribed-circles", "geometry", "Incircles and circumcircles of triangles and quadrilaterals", 4, 4,
      [("circle-tangent", 1.0), ("triangle-area", 0.8), ("trapezoid-properties", 0.6)],
      note="The inscribed-circle-in-a-trapezoid item recurs; it needs the tangent-length equality "
           "plus the area relation, which is why both edges are strong."),
    S("coordinate-distance", "geometry", "Distance between two points", 1, 3,
      [("pythagoras", 1.0), ("integer-operations", 0.8)]),
    S("coordinate-midpoint", "geometry", "Midpoint and the section formula in coordinates", 2, 3,
      [("coordinate-distance", 0.6), ("fraction-arithmetic", 0.8)]),
    S("line-equation", "geometry", "Equation of a straight line in its various forms", 2, 4,
      [("function-notation", 0.8), ("rearranging-formulas", 0.8)]),
    S("parallel-perpendicular-lines", "geometry", "Gradient conditions for parallel and perpendicular lines", 2, 3,
      [("line-equation", 1.0)]),
    S("circle-equation", "geometry", "Equation of a circle, centre and radius", 3, 4,
      [("coordinate-distance", 1.0), ("completing-the-square", 0.8)]),
    S("line-circle-intersection", "geometry", "Intersection of a line and a circle; tangency condition", 4, 3,
      [("circle-equation", 1.0), ("systems-nonlinear", 1.0), ("discriminant", 0.8)]),
    S("translation", "geometry", "Translate a figure by a vector", 2, 3,
      [("coordinate-distance", 0.6), ("vector-components", 0.8)]),
    S("reflection", "geometry", "Reflect a point or figure in a line or through a point", 2, 3,
      [("coordinate-distance", 0.6), ("parallel-perpendicular-lines", 0.6)]),
    S("rotation", "geometry", "Rotate a figure about a point", 3, 3,
      [("coordinate-distance", 0.6), ("exact-trig-values", 0.4)]),
    S("homothety", "geometry", "Enlargement about a centre with a scale factor", 3, 3,
      [("triangle-similarity", 1.0), ("coordinate-midpoint", 0.6)]),
    S("transformation-matrices", "geometry", "Represent and compose transformations as 2×2 matrices", 4, 6,
      [("matrix-multiplication", 1.0), ("reflection", 0.8), ("rotation", 0.8), ("homothety", 0.6)]),
    S("prism-volume-surface", "geometry", "Volume and surface area of prisms and cuboids", 2, 4,
      [("triangle-area", 0.8), ("quadrilateral-properties", 0.8)]),
    S("pyramid-volume-surface", "geometry", "Volume and surface area of a pyramid", 3, 4,
      [("prism-volume-surface", 0.8), ("pythagoras", 1.0), ("triangle-area", 0.8)],
      note="The slant height is a Pythagoras step inside the solid; that is where students fail, "
           "not on the ⅓Bh formula."),
    S("cylinder", "geometry", "Volume and surface area of a cylinder", 2, 3,
      [("circle-area-and-arc", 1.0), ("prism-volume-surface", 0.6)]),
    S("cone", "geometry", "Volume, surface area and the sector-to-cone relation", 3, 4,
      [("circle-area-and-arc", 1.0), ("pythagoras", 1.0), ("cylinder", 0.6)]),
    S("sphere", "geometry", "Volume and surface area of a sphere", 2, 2,
      [("circle-area-and-arc", 0.8)]),
    S("solid-of-revolution-geometric", "geometry", "Identify the solid generated by rotating a plane figure", 3, 2,
      [("cylinder", 0.8), ("cone", 0.8), ("sphere", 0.6)]),
    S("space-geometry-angles", "geometry", "Angles and distances between lines and planes in space", 4, 3,
      [("pythagoras", 1.0), ("right-triangle-ratios", 0.8), ("prism-volume-surface", 0.6)]),
]

TRIGONOMETRY = [
    S("right-triangle-ratios", "trigonometry", "Sine, cosine and tangent in a right triangle", 2, 4,
      [("triangle-similarity", 1.0), ("pythagoras", 0.8)]),
    S("exact-trig-values", "trigonometry", "Exact values at 0°, 30°, 45°, 60° and 90°", 2, 4,
      [("right-triangle-ratios", 1.0), ("special-right-triangles", 1.0)]),
    S("unit-circle-and-radians", "trigonometry", "The unit circle, radians and signs by quadrant", 3, 4,
      [("exact-trig-values", 1.0), ("circle-parts", 0.8)]),
    S("trig-pythagorean-identity", "trigonometry", "sin²θ + cos²θ = 1 and its rearrangements", 3, 4,
      [("unit-circle-and-radians", 1.0), ("special-products", 0.6)]),
    S("trig-sum-difference", "trigonometry", "Sine and cosine of a sum or difference", 4, 3,
      [("unit-circle-and-radians", 1.0), ("exact-trig-values", 0.8)]),
    S("double-angle-formulas", "trigonometry", "Double-angle formulas", 4, 3,
      [("trig-sum-difference", 1.0), ("trig-pythagorean-identity", 0.8)]),
    S("trig-simplification", "trigonometry", "Simplify a trigonometric expression using identities", 4, 4,
      [("trig-pythagorean-identity", 1.0), ("double-angle-formulas", 0.6),
       ("rational-expressions", 0.6)]),
    S("trig-equations", "trigonometry", "Solve a trigonometric equation over a given interval", 4, 4,
      [("unit-circle-and-radians", 1.0), ("trig-pythagorean-identity", 0.8), ("quadratic-by-factoring", 0.6)]),
    S("sine-rule", "trigonometry", "The sine rule, including the ambiguous case", 3, 4,
      [("right-triangle-ratios", 1.0), ("triangle-angle-sum", 1.0)]),
    S("cosine-rule", "trigonometry", "The cosine rule", 3, 4,
      [("right-triangle-ratios", 1.0), ("pythagoras", 0.8), ("quadratic-formula", 0.4)]),
    S("trig-graphs", "trigonometry", "Amplitude, period and shifts of trigonometric graphs", 4, 2,
      [("unit-circle-and-radians", 1.0), ("graph-transformations", 0.8)]),
]

LINEAR_ALGEBRA = [
    S("vector-components", "linear_algebra", "Vectors in component form and position vectors", 2, 4,
      [("coordinate-distance", 0.6), ("integer-operations", 0.8)]),
    S("vector-arithmetic", "linear_algebra", "Add, subtract and scale vectors; equal and opposite vectors", 2, 6,
      [("vector-components", 1.0)]),
    S("vector-magnitude", "linear_algebra", "Magnitude of a vector and unit vectors", 2, 3,
      [("vector-components", 1.0), ("pythagoras", 1.0)]),
    S("dot-product", "linear_algebra", "Scalar product and the angle between vectors", 3, 4,
      [("vector-components", 1.0), ("vector-magnitude", 0.8), ("exact-trig-values", 0.6)]),
    S("vectors-in-polygons", "linear_algebra", "Express a vector in a polygon in terms of given vectors", 3, 4,
      [("vector-arithmetic", 1.0), ("quadrilateral-properties", 0.8)]),
    S("vector-section-formula", "linear_algebra", "Divide a segment in a given ratio using vectors", 4, 3,
      [("vector-arithmetic", 1.0), ("coordinate-midpoint", 0.8), ("percent-and-proportion", 0.8)]),
    S("matrix-dimensions", "linear_algebra", "Matrix notation, dimensions and when a product exists", 1, 3,
      [("integer-operations", 0.6)]),
    S("matrix-addition-scalar", "linear_algebra", "Add matrices and multiply by a scalar", 2, 3,
      [("matrix-dimensions", 1.0)]),
    S("matrix-multiplication", "linear_algebra", "Multiply matrices", 3, 4,
      [("matrix-dimensions", 1.0), ("matrix-addition-scalar", 0.6)]),
    S("determinant-2x2", "linear_algebra", "Determinant of a 2×2 matrix", 2, 3,
      [("matrix-dimensions", 1.0), ("integer-operations", 0.8)]),
    S("inverse-matrix-2x2", "linear_algebra", "Inverse of a 2×2 matrix and singularity", 3, 4,
      [("determinant-2x2", 1.0), ("matrix-multiplication", 0.8)]),
    S("cayley-hamilton", "linear_algebra", "Apply the Cayley–Hamilton theorem to a 2×2 matrix", 5, 3,
      [("determinant-2x2", 1.0), ("matrix-multiplication", 1.0), ("polynomial-arithmetic", 0.8)]),
    S("determinant-3x3", "linear_algebra", "Determinant of a 3×3 matrix and Cramer's rule", 3, 3,
      [("determinant-2x2", 1.0), ("systems-three-linear", 0.8)]),
    S("gaussian-elimination", "linear_algebra", "Solve a linear system by row reduction", 4, 2,
      [("systems-three-linear", 1.0), ("matrix-dimensions", 0.8)]),
]

# ===========================================================================
# STRAND 3 — ANALYSIS (16.2%)
# ===========================================================================

CALCULUS = [
    S("limit-concept", "calculus", "Evaluate a limit, including indeterminate quotients", 3, 3,
      [("rational-expressions", 1.0), ("factoring-quadratic-trinomial", 0.8)]),
    S("derivative-definition", "calculus", "The derivative as a limit of the difference quotient", 3, 2,
      [("limit-concept", 1.0), ("function-notation", 1.0)]),
    S("derivative-power-rule", "calculus", "Differentiate powers and polynomials", 2, 5,
      [("derivative-definition", 0.6), ("integer-powers", 1.0), ("rational-exponents", 0.6)],
      note="0.6 to the definition on purpose: nearly every student who can differentiate a "
           "polynomial cannot reproduce the limit definition, and pretending otherwise would "
           "make the placement mark them down for a skill they do not need here."),
    S("derivative-product-quotient", "calculus", "Product and quotient rules", 3, 4,
      [("derivative-power-rule", 1.0), ("rational-expressions", 0.6)]),
    S("chain-rule", "calculus", "Differentiate a composite function", 3, 4,
      [("derivative-power-rule", 1.0), ("composite-functions", 1.0)]),
    S("derivative-trig", "calculus", "Differentiate trigonometric functions", 3, 3,
      [("derivative-power-rule", 1.0), ("unit-circle-and-radians", 0.8), ("chain-rule", 0.6)]),
    S("derivative-exp-log", "calculus", "Differentiate exponential and logarithmic functions", 3, 3,
      [("derivative-power-rule", 1.0), ("logarithm-definition", 0.8), ("chain-rule", 0.6)]),
    S("higher-order-derivatives", "calculus", "Second and higher derivatives", 3, 3,
      [("derivative-power-rule", 1.0)]),
    S("tangent-line", "calculus", "Equation of the tangent to a curve at a point", 3, 4,
      [("derivative-power-rule", 1.0), ("line-equation", 1.0)]),
    S("normal-line", "calculus", "Equation of the normal to a curve", 3, 3,
      [("tangent-line", 1.0), ("parallel-perpendicular-lines", 1.0)]),
    S("monotonicity-from-derivative", "calculus", "Use the sign of f′ to find increasing and decreasing intervals", 3, 4,
      [("derivative-power-rule", 1.0), ("quadratic-inequalities", 0.8), ("increasing-decreasing-intervals", 0.6)]),
    S("stationary-points-and-extrema", "calculus", "Find and classify stationary points", 3, 5,
      [("monotonicity-from-derivative", 1.0), ("quadratic-by-factoring", 0.8)]),
    S("concavity-and-inflection", "calculus", "Concavity and points of inflection", 4, 2,
      [("higher-order-derivatives", 1.0), ("stationary-points-and-extrema", 0.8)]),
    S("optimisation", "calculus", "Optimisation word problems", 4, 3,
      [("stationary-points-and-extrema", 1.0), ("rearranging-formulas", 0.8)]),
    S("antiderivative-power", "calculus", "Antiderivatives of powers and polynomials", 2, 5,
      [("derivative-power-rule", 1.0)]),
    S("antiderivative-trig-exp", "calculus", "Antiderivatives of trigonometric and exponential functions", 3, 3,
      [("antiderivative-power", 1.0), ("derivative-trig", 0.8), ("derivative-exp-log", 0.8)]),
    S("integration-by-substitution", "calculus", "Integrate by substitution", 4, 3,
      [("antiderivative-power", 1.0), ("chain-rule", 1.0)]),
    S("definite-integral", "calculus", "Evaluate a definite integral", 3, 5,
      [("antiderivative-power", 1.0), ("function-notation", 0.8)]),
    S("definite-integral-absolute", "calculus", "Definite integral of a function containing absolute value", 4, 3,
      [("definite-integral", 1.0), ("absolute-value-equations", 1.0), ("piecewise-functions", 0.8)]),
    S("area-under-curve", "calculus", "Area between a curve and the x-axis", 3, 4,
      [("definite-integral", 1.0)]),
    S("area-between-curves", "calculus", "Area between two curves", 4, 4,
      [("area-under-curve", 1.0), ("systems-nonlinear", 0.8)],
      note="Finding the limits IS solving the curves simultaneously; that is where the marks go."),
    S("volume-of-revolution", "calculus", "Volume generated by rotating a region", 4, 2,
      [("definite-integral", 1.0), ("area-under-curve", 0.8), ("cylinder", 0.4)]),
    S("differential-equations-separable", "calculus", "Solve a separable differential equation", 4, 4,
      [("antiderivative-power", 1.0), ("integration-by-substitution", 0.6), ("derivative-exp-log", 0.6)]),
]

# ===========================================================================
# STRAND 4 — PROBABILITY & STATISTICS (15.5%)
# ===========================================================================

PROBABILITY = [
    S("sample-space-and-events", "probability", "Sample spaces, events and listing outcomes", 1, 4,
      [("set-notation", 0.8), ("counting-principle", 0.6)]),
    S("classical-probability", "probability", "Probability as favourable over total outcomes", 2, 5,
      [("sample-space-and-events", 1.0), ("fraction-arithmetic", 1.0)]),
    S("complementary-events", "probability", "The complement rule", 2, 3,
      [("classical-probability", 1.0)]),
    S("addition-rule", "probability", "P(A ∪ B) and mutually exclusive events", 3, 4,
      [("classical-probability", 1.0), ("set-operations", 0.8), ("inclusion-exclusion", 0.8)]),
    S("independent-events", "probability", "Multiplication rule for independent events", 3, 4,
      [("classical-probability", 1.0)]),
    S("conditional-probability", "probability", "Conditional probability and dependent events", 4, 3,
      [("independent-events", 1.0), ("classical-probability", 1.0)]),
    S("geometric-probability", "probability", "Probability from length, area or volume", 3, 4,
      [("classical-probability", 1.0), ("circle-area-and-arc", 0.6), ("triangle-area", 0.6)]),
    S("counting-based-probability", "probability", "Probability problems that need permutations or combinations", 4, 4,
      [("classical-probability", 1.0), ("combinations", 1.0), ("permutations", 0.8)]),
    S("discrete-random-variable", "probability", "Discrete random variables and probability distributions", 3, 5,
      [("classical-probability", 1.0), ("sample-space-and-events", 0.8)]),
    S("expected-value", "probability", "Expected value of a discrete random variable", 3, 5,
      [("discrete-random-variable", 1.0), ("fraction-arithmetic", 0.8)]),
    S("variance-of-random-variable", "probability", "Variance and standard deviation of a random variable", 4, 4,
      [("expected-value", 1.0), ("integer-powers", 0.8)]),
    S("binomial-distribution", "probability", "Binomial probabilities", 4, 3,
      [("independent-events", 1.0), ("combinations", 1.0), ("discrete-random-variable", 0.8)]),
]

STATISTICS = [
    S("data-representation", "statistics", "Read bar charts, histograms and frequency tables", 1, 3,
      [("percent-and-proportion", 0.6)]),
    S("mean-median-mode", "statistics", "Mean, median and mode of a data set", 1, 5,
      [("fraction-arithmetic", 0.8), ("data-representation", 0.6)]),
    S("grouped-frequency-mean", "statistics", "Estimate the mean from a grouped frequency table", 3, 4,
      [("mean-median-mode", 1.0), ("data-representation", 1.0)]),
    S("quartiles-and-iqr", "statistics", "Range, quartiles and the interquartile range", 3, 6,
      [("mean-median-mode", 1.0)]),
    S("box-plots", "statistics", "Construct and interpret a box plot", 2, 2,
      [("quartiles-and-iqr", 1.0)]),
    S("cumulative-frequency", "statistics", "Cumulative frequency curves and reading a median from one", 3, 3,
      [("data-representation", 1.0), ("quartiles-and-iqr", 0.8)]),
    S("variance-and-sd", "statistics", "Variance and standard deviation of a data set", 3, 5,
      [("mean-median-mode", 1.0), ("integer-powers", 0.8)]),
    S("combined-standard-deviation", "statistics", "Combine the means and standard deviations of two groups", 5, 3,
      [("variance-and-sd", 1.0), ("mean-median-mode", 1.0)],
      note="Genuinely hard and it recurs. It needs the sum-of-squares identity, not just the formula."),
]

# ===========================================================================
# STRAND 5 — COMBINATORICS (2.0%)
# Smallest strand, but it feeds probability and the binomial theorem, so its
# edges point OUT of the strand more than in.
# ===========================================================================

COMBINATORICS = [
    S("counting-principle", "combinatorics", "The multiplication principle for counting", 2, 5,
      [("integer-operations", 0.8)]),
    S("permutations", "combinatorics", "Permutations and factorial notation", 3, 5,
      [("counting-principle", 1.0)]),
    S("permutations-with-restrictions", "combinatorics", "Permutations with restrictions or repeated items", 4, 4,
      [("permutations", 1.0)]),
    S("combinations", "combinatorics", "Combinations and when order does not matter", 3, 5,
      [("permutations", 1.0)]),
    S("stars-and-bars", "combinatorics", "Count non-negative integer solutions of an equation", 5, 3,
      [("combinations", 1.0)]),
]

ALL_SKILLS = (
    ARITHMETIC + SET_THEORY + ALGEBRA_CORE + FUNCTIONS + LOGS + SEQUENCES + COMPLEX
    + GEOMETRY + TRIGONOMETRY + LINEAR_ALGEBRA
    + CALCULUS
    + PROBABILITY + STATISTICS
    + COMBINATORICS
)

# Edges that deliberately cross a strand boundary. Every one is listed here so
# that a cross-strand edge is a decision someone made, never an accident.
DELIBERATE_CROSS_STRAND = {
    ("combinations", "binomial-theorem"),
    ("counting-principle", "sample-space-and-events"),
    ("combinations", "counting-based-probability"),
    ("permutations", "counting-based-probability"),
    ("combinations", "binomial-distribution"),
    ("matrix-multiplication", "transformation-matrices"),
    ("vector-components", "translation"),
    ("exact-trig-values", "rotation"),
    ("right-triangle-ratios", "triangle-area"),
    ("systems-three-linear", "gaussian-elimination"),
    ("systems-three-linear", "determinant-3x3"),
    ("function-notation", "line-equation"),
        ("quadratic-formula", "cosine-rule"),
    ("coordinate-midpoint", "vector-section-formula"),
    ("percent-and-proportion", "vector-section-formula"),
    ("coordinate-distance", "vector-components"),
    ("pythagoras", "vector-magnitude"),
    ("quadrilateral-properties", "vectors-in-polygons"),
    ("exact-trig-values", "dot-product"),
    ("circle-parts", "unit-circle-and-radians"),
    ("special-right-triangles", "exact-trig-values"),
    ("triangle-similarity", "right-triangle-ratios"),
    ("pythagoras", "right-triangle-ratios"),
    ("special-products", "trig-pythagorean-identity"),
    ("rational-expressions", "trig-simplification"),
    ("quadratic-by-factoring", "trig-equations"),
    ("graph-transformations", "trig-graphs"),
    ("triangle-angle-sum", "sine-rule"),
    ("pythagoras", "cosine-rule"),
    ("linear-equation-one-variable", "angles-and-parallel-lines"),
    ("radicals-simplification", "pythagoras"),
    ("quadratic-by-factoring", "pythagoras"),
    ("percent-and-proportion", "triangle-similarity"),
    ("completing-the-square", "circle-equation"),
    ("systems-nonlinear", "line-circle-intersection"),
    ("discriminant", "line-circle-intersection"),
    ("linear-function-graph", "line-equation"),
    ("rearranging-formulas", "line-equation"),
    ("integer-operations", "coordinate-distance"),
    ("fraction-arithmetic", "coordinate-midpoint"),
    ("integer-operations", "matrix-dimensions"),
    ("integer-operations", "determinant-2x2"),
    ("polynomial-arithmetic", "cayley-hamilton"),
    ("integer-operations", "vector-components"),
    ("integer-operations", "counting-principle"),
    ("set-notation", "sample-space-and-events"),
    ("fraction-arithmetic", "classical-probability"),
    ("set-operations", "addition-rule"),
    ("inclusion-exclusion", "addition-rule"),
    ("circle-area-and-arc", "geometric-probability"),
    ("triangle-area", "geometric-probability"),
    ("fraction-arithmetic", "expected-value"),
    ("integer-powers", "variance-of-random-variable"),
    ("percent-and-proportion", "data-representation"),
    ("fraction-arithmetic", "mean-median-mode"),
    ("integer-powers", "variance-and-sd"),
    ("cylinder", "volume-of-revolution"),
        ("line-equation", "tangent-line"),
    ("parallel-perpendicular-lines", "normal-line"),
    ("unit-circle-and-radians", "derivative-trig"),
    ("logarithm-definition", "derivative-exp-log"),
    ("systems-nonlinear", "area-between-curves"),
    ("prism-volume-surface", "space-geometry-angles"),
    ("right-triangle-ratios", "space-geometry-angles"),
    ("radicals-simplification", "special-right-triangles"),
    ("percent-and-proportion", "circle-area-and-arc"),
    # ANALYSIS rests almost entirely on ALGEBRA. Every edge below is a real
    # blocker observed in marking: students do not fail calculus on the
    # calculus, they fail it on the algebra inside the calculus.
    ("rational-expressions", "limit-concept"),
    ("factoring-quadratic-trinomial", "limit-concept"),
        ("function-notation", "derivative-definition"),
    ("integer-powers", "derivative-power-rule"),
    ("rational-exponents", "derivative-power-rule"),
    ("rational-expressions", "derivative-product-quotient"),
    ("composite-functions", "chain-rule"),
    ("quadratic-inequalities", "monotonicity-from-derivative"),
    ("increasing-decreasing-intervals", "monotonicity-from-derivative"),
    ("quadratic-by-factoring", "stationary-points-and-extrema"),
    ("rearranging-formulas", "optimisation"),
    ("function-notation", "definite-integral"),
    ("absolute-value-equations", "definite-integral-absolute"),
    ("piecewise-functions", "definite-integral-absolute"),
}


# ---------------------------------------------------------------------------
# Verification. Nothing is emitted unless every one of these holds.
# ---------------------------------------------------------------------------

def verify(skills):
    by_id = {}
    errors = []

    for s in skills:
        if s.id in by_id:
            errors.append(f"duplicate skill id: {s.id}")
        by_id[s.id] = s
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s.id):
            errors.append(f"{s.id}: id is not kebab-case")
        if s.topic not in STRAND_OF_TOPIC:
            errors.append(f"{s.id}: unknown topic {s.topic!r}")
        if not 1 <= s.difficulty <= 5:
            errors.append(f"{s.id}: typical_difficulty {s.difficulty} outside 1-5")
        if s.share < 1:
            errors.append(f"{s.id}: share must be >= 1")
        # Names are sentence-case, except where the maths starts the sentence:
        # "log(ab) = log a + log b" must not be bent into "Log(ab)".
        MATH_START = ("log", "sin", "cos", "tan", "nth", "e^", "f(", "P(")
        if not s.name_en:
            errors.append(f"{s.id}: name_en missing")
        elif s.name_en[0].islower() and not s.name_en.startswith(MATH_START):
            errors.append(f"{s.id}: name_en is not capitalised ({s.name_en!r})")

    # Edges: endpoints exist, strengths in range, no self-loops, no duplicates,
    # and every cross-strand edge is on the deliberate list.
    for s in skills:
        seen = set()
        for pid, strength in s.prereqs:
            if pid == s.id:
                errors.append(f"{s.id}: is its own prerequisite")
            if pid not in by_id:
                errors.append(f"{s.id}: prerequisite {pid!r} does not exist")
                continue
            if pid in seen:
                errors.append(f"{s.id}: duplicate prerequisite {pid!r}")
            seen.add(pid)
            if not (0 < strength <= 1):
                errors.append(f"{s.id} <- {pid}: strength {strength} outside (0,1]")
            if strength < 0.4:
                errors.append(f"{s.id} <- {pid}: strength {strength} below the 0.4 floor")
            a, b = STRAND_OF_TOPIC[by_id[pid].topic], STRAND_OF_TOPIC[s.topic]
            if a != b and (pid, s.id) not in DELIBERATE_CROSS_STRAND:
                errors.append(f"{s.id} <- {pid}: crosses {a} -> {b} but is not declared deliberate")

    # Acyclicity. A cycle makes inference circular: A credits B credits A.
    colour = {}

    def visit(node, stack):
        if colour.get(node) == "done":
            return
        if colour.get(node) == "open":
            i = stack.index(node)
            errors.append("prerequisite CYCLE: " + " -> ".join(stack[i:] + [node]))
            return
        colour[node] = "open"
        for pid, _ in by_id[node].prereqs:
            if pid in by_id:
                visit(pid, stack + [node])
        colour[node] = "done"

    for s in skills:
        visit(s.id, [])

    # A skill nothing depends on and that depends on nothing is disconnected —
    # almost always a sign it was invented rather than observed.
    depended_on = {pid for s in skills for pid, _ in s.prereqs}
    for s in skills:
        if not s.prereqs and s.id not in depended_on:
            errors.append(f"{s.id}: disconnected — no prerequisites and nothing needs it")

    # Weights: each topic's skills must carry exactly that topic's measured
    # share, and the strands must sum to the measured strand shares.
    topics = {}
    for s in skills:
        topics.setdefault(s.topic, []).append(s)
    for t in TOPIC_SHARE_PCT:
        if t not in topics:
            errors.append(f"topic {t} has measured weight but no skills")
    strand_totals = {}
    for t, group in topics.items():
        total_share = sum(x.share for x in group)
        for s in group:
            s.exam_weight = round(TOPIC_SHARE_PCT[s.topic] * s.share / total_share, 4)
        strand_totals.setdefault(STRAND_OF_TOPIC[t], 0.0)
        strand_totals[STRAND_OF_TOPIC[t]] += sum(s.exam_weight for s in group)
    for strand, expected in STRAND_SHARE_PCT.items():
        got = round(strand_totals.get(strand, 0.0), 2)
        if abs(got - expected) > 0.05:
            errors.append(f"strand {strand}: weights sum to {got}, measured share is {expected}")

    return errors, by_id


def display_orders(skills, by_id):
    """Order within a strand so that prerequisites always come first.

    This makes display_order double as a defensible teaching order: you can
    read a strand top to bottom and never meet a skill before its
    prerequisites. Ties break on (topic order, difficulty, id) so the output
    is deterministic.
    """
    topic_rank = {t: i for i, t in enumerate(TOPIC_SHARE_PCT)}
    out = {}
    for strand in STRAND_SHARE_PCT:
        members = [s for s in skills if STRAND_OF_TOPIC[s.topic] == strand]
        ids = {s.id for s in members}
        remaining = {s.id: {p for p, _ in s.prereqs if p in ids} for s in members}
        ordered, n = [], 0
        while remaining:
            ready = [i for i, deps in remaining.items() if not deps]
            if not ready:  # verify() already rejects cycles; belt and braces
                raise SystemExit(f"cycle inside strand {strand}")
            ready.sort(key=lambda i: (topic_rank[by_id[i].topic], by_id[i].difficulty, i))
            pick = ready[0]
            del remaining[pick]
            for deps in remaining.values():
                deps.discard(pick)
            n += 1
            out[pick] = n
            ordered.append(pick)
    return out


def emit(skills, by_id):
    order = display_orders(skills, by_id)
    rows = []
    for s in sorted(skills, key=lambda x: (STRAND_OF_TOPIC[x.topic], order[x.id])):
        rows.append({
            "id": s.id,
            # 'eysh', not 'esh': migration 010 puts a CHECK constraint on this
            # column (hub IN ('eysh','sat')) and every row would be rejected.
            "hub": "eysh",
            "strand": STRAND_OF_TOPIC[s.topic],
            "topic": s.topic,
            "name_en": s.name_en,
            "name_mn": None,
            "exam_weight": s.exam_weight,
            "typical_difficulty": s.difficulty,
            "display_order": order[s.id],
            "note": s.note or None,
        })
    edges = []
    for s in sorted(skills, key=lambda x: x.id):
        for pid, strength in sorted(s.prereqs):
            edges.append({"skill_id": s.id, "prereq_skill_id": pid, "strength": strength})

    os.makedirs(os.path.join(ROOT, "data", "skills"), exist_ok=True)
    payload = {
        "note": "Generated by scripts/skills/esh_graph.py. Do not hand-edit — edit the builder.",
        "hub": "eysh",
        "strandWeights": STRAND_SHARE_PCT,
        "weightsMeasuredFrom": "data/esh/exam-weights.json (20 past papers, 980 questions)",
        "counts": {"skills": len(rows), "edges": len(edges)},
        "skills": rows,
        "edges": edges,
    }
    with open(os.path.join(ROOT, "data", "skills", "esh-skills.json"), "w") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")

    def q(v):
        if v is None:
            return "NULL"
        return "'" + str(v).replace("'", "''") + "'"

    lines = [
        "-- 011: seed the ЭЕШ skill graph.",
        "--",
        "-- GENERATED by scripts/skills/esh_graph.py. Do not hand-edit — edit the builder",
        "-- and re-run, or the graph and the database drift apart silently and nobody",
        "-- finds out until a student is placed wrong.",
        "--",
        f"-- {len(rows)} skills, {len(edges)} prerequisite edges, hub = 'esh'.",
        "--",
        "-- DATA ONLY, NO DDL. `skills` and `skill_prerequisites` already exist in",
        "-- production (confirmed by the owner, both empty). This migration fills them.",
        "--",
        "-- WHY SKILLS ARE UPSERTED AND NEVER DELETED. Migration 010 defines",
        "--   skill_state.skill_id REFERENCES skills(id) ON DELETE CASCADE",
        "-- so deleting a skill deletes every student's mastery state for it. An",
        "-- earlier draft of this file did delete-then-insert; against this schema",
        "-- that would silently destroy learner records on any re-run. Skills are",
        "-- therefore upserted on the primary key and never removed here.",
        "--   attempts.skill_id also references skills(id), without CASCADE, so a",
        "--   delete would additionally ERROR once attempts carry skill ids.",
        "-- EDGES are different: nothing references skill_prerequisites, so the hub's",
        "-- edges are cleared and rewritten. That keeps a revision that DROPS an edge",
        "-- from leaving it behind, which an upsert alone cannot do.",
        "-- A skill that a later revision drops is REPORTED at the end, not deleted —",
        "-- removing it is a decision with student data attached.",
        "--",
        "-- name_mn is NULL on every row by design: Mongolian is authored in Phase 3 by a",
        "-- Mongolian-speaking maths teacher expressing the idea, never translated from",
        "-- the English here.",
        "--",
        "-- exam_weight is a percentage of the WHOLE exam, derived from the measured",
        "-- share of each topic across 20 real past papers (data/esh/exam-weights.json,",
        "-- 980 questions). The strand totals are 36.1 / 30.1 / 16.2 / 15.5 / 2.0 and the",
        "-- builder refuses to emit if they drift.",
        "",
        "begin;",
        "",
        "-- Fail with a readable message rather than a raw column error if the live",
        "-- schema does not match what this file was generated against.",
        "do $$",
        "declare",
        "  missing text;",
        "begin",
        "  select string_agg(c, ', ') into missing from (",
        "    select c from unnest(array['id','hub','strand','name_en','name_mn',",
        "                              'exam_weight','typical_difficulty','display_order']) as c",
        "    where not exists (",
        "      select 1 from information_schema.columns",
        "      where table_schema = 'public' and table_name = 'skills' and column_name = c)",
        "  ) t;",
        "  if missing is not null then",
        "    raise exception 'skills is missing expected column(s): %. This migration was "
        "generated against id, hub, strand, name_en, name_mn, exam_weight, "
        "typical_difficulty, display_order. Re-run scripts/skills/esh_graph.py after "
        "adjusting the emitter to the real schema.', missing;",
        "  end if;",
        "",
        "  select string_agg(c, ', ') into missing from (",
        "    select c from unnest(array['skill_id','requires_id','strength']) as c",
        "    where not exists (",
        "      select 1 from information_schema.columns",
        "      where table_schema = 'public' and table_name = 'skill_prerequisites'",
        "        and column_name = c)",
        "  ) t;",
        "  if missing is not null then",
        "    raise exception 'skill_prerequisites is missing expected column(s): %.', missing;",
        "  end if;",
        "end $$;",
        "",
        "delete from skill_prerequisites",
        " where skill_id in (select id from skills where hub = 'eysh')",
        "    or requires_id in (select id from skills where hub = 'eysh');",
        "",
        "insert into skills (id, hub, strand, name_en, name_mn, exam_weight, typical_difficulty, display_order)",
        "values",
    ]
    body = []
    for r in rows:
        body.append(
            f"  ({q(r['id'])}, {q(r['hub'])}, {q(r['strand'])}, {q(r['name_en'])}, NULL, "
            f"{r['exam_weight']}, {r['typical_difficulty']}, {r['display_order']})"
        )
    lines.append(",\n".join(body))
    lines += [
        "on conflict (id) do update set",
        "  hub = excluded.hub,",
        "  strand = excluded.strand,",
        "  name_en = excluded.name_en,",
        "  exam_weight = excluded.exam_weight,",
        "  typical_difficulty = excluded.typical_difficulty,",
        "  display_order = excluded.display_order;",
        "-- name_mn is deliberately NOT in the update list: once a Mongolian",
        "-- teacher writes it in Phase 3, re-running this seed must not blank it.",
    ]
    lines += [
        "",
        "insert into skill_prerequisites (skill_id, requires_id, strength)",
        "values",
    ]
    lines.append(",\n".join(
        f"  ({q(e['skill_id'])}, {q(e['prereq_skill_id'])}, {e['strength']})" for e in edges
    ) + "\non conflict (skill_id, requires_id) do update set strength = excluded.strength;")
    lines += [
        "",
        "-- Post-conditions. If any of these fail the whole migration rolls back, so a",
        "-- partially-seeded graph can never reach a student.",
        "do $$",
        "declare",
        "  n_skills int;",
        "  n_edges int;",
        "  n_dangling int;",
        "begin",
        "  select count(*) into n_skills from skills where hub = 'eysh';",
        f"  if n_skills < {len(rows)} then",
        f"    raise exception 'expected at least {len(rows)} ЭЕШ skills, found %', n_skills;",
        "  end if;",
        "",
        "  select count(*) into n_edges from skill_prerequisites p",
        "    join skills s on s.id = p.skill_id where s.hub = 'eysh';",
        f"  if n_edges <> {len(edges)} then",
        f"    raise exception 'expected {len(edges)} prerequisite edges, found %', n_edges;",
        "  end if;",
        "",
        "  -- Every edge endpoint must resolve. A dangling prerequisite would make the",
        "  -- inference walk silently skip a whole branch.",
        "  select count(*) into n_dangling from skill_prerequisites p",
        "   where not exists (select 1 from skills s where s.id = p.skill_id)",
        "      or not exists (select 1 from skills s where s.id = p.requires_id);",
        "  if n_dangling > 0 then",
        "    raise exception '% prerequisite edge(s) point at a skill that does not exist',",
        "      n_dangling;",
        "  end if;",
        "end $$;",
        "",
        "commit;",
        "",
    ]
    os.makedirs(os.path.join(ROOT, "supabase", "migrations"), exist_ok=True)
    path = os.path.join(ROOT, "supabase", "migrations", "011_seed_esh_graph.sql")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    # The old hand-rolled seed lived at supabase/seed/esh_skills.sql. Two files
    # emitting the same rows is two files that can disagree, so it goes.
    stale = os.path.join(ROOT, "supabase", "seed", "esh_skills.sql")
    if os.path.exists(stale):
        os.remove(stale)
    return rows, edges


def main():
    errors, by_id = verify(ALL_SKILLS)
    if errors:
        print(f"GRAPH REJECTED — {len(errors)} problem(s):", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        raise SystemExit(1)
    rows, edges = emit(ALL_SKILLS, by_id)

    per_strand = {}
    for r in rows:
        per_strand.setdefault(r["strand"], []).append(r)
    print(f"{len(rows)} skills, {len(edges)} edges")
    for strand, share in STRAND_SHARE_PCT.items():
        g = per_strand.get(strand, [])
        w = sum(x["exam_weight"] for x in g)
        print(f"  {strand:24s} {len(g):3d} skills   weight {w:5.1f}%  (measured {share}%)")
    roots = [r["id"] for r in rows if not by_id[r["id"]].prereqs]
    print(f"  roots (no prerequisites): {', '.join(roots)}")
    depth = {}

    def d(i):
        if i in depth:
            return depth[i]
        depth[i] = 0 if not by_id[i].prereqs else 1 + max(d(p) for p, _ in by_id[i].prereqs)
        return depth[i]

    deepest = max(rows, key=lambda r: d(r["id"]))
    print(f"  deepest chain: {deepest['id']} at depth {d(deepest['id'])}")


if __name__ == "__main__":
    main()
