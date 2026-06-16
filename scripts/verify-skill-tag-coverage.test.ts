// Phase 3b.5 — asserts the skill-tag pass (3b.4) fully covered Section 1 and
// that every applied tag is in the locked taxonomy with a correctly-derived
// difficulty_tier. Guards against a future question landing without a tag, or
// a typo'd / off-taxonomy tag slipping into the data.

import { describe, it, expect } from "vitest";
import { getAllQuestions } from "@/lib/esh-questions";

// The locked taxonomy (49 tags) — memory/skill-tag-taxonomy.md. Mirror of the
// list in scripts/preclassify-skill-tags.mjs; kept here so the test has no
// dependency on the classification harness.
const SKILL_TAGS = new Set([
  // algebra (10)
  "linear_equation", "quadratic_equation", "polynomial_factoring",
  "polynomial_remainder", "system_of_equations", "linear_inequality",
  "quadratic_inequality", "radical_expression", "rational_expression",
  "exponent_rules",
  // geometry (7)
  "triangle_geometry", "circle_geometry", "polygon_geometry",
  "coordinate_geometry", "solid_geometry", "geometric_transformation",
  "circle_theorem",
  // calculus (5)
  "derivative_rules", "derivative_application", "indefinite_integral",
  "definite_integral", "differential_equation",
  // linear_algebra (3)
  "matrix_operation", "matrix_inverse", "vector_geometry",
  // probability (4)
  "discrete_distribution", "compound_event", "geometric_probability",
  "expected_value",
  // statistics (3)
  "central_tendency", "dispersion", "data_display",
  // trigonometry (4)
  "trig_identity", "trig_equation", "trig_value", "trig_triangle",
  // arithmetic (3)
  "number_representation", "fraction_arithmetic", "word_problem_arithmetic",
  // functions (3)
  "function_domain_range", "function_inverse_composite", "function_graph",
  // combinatorics (3)
  "permutation_arrangement", "combination_selection", "counting_principle",
  // singles (4)
  "set_theory", "complex_numbers", "progression", "logarithm",
]);

function expectedTier(d: number): "easy" | "medium" | "hard" {
  return d <= 2 ? "easy" : d === 3 ? "medium" : "hard";
}

const questions = getAllQuestions();

describe("skill-tag coverage (Phase 3b.4)", () => {
  it("loads the full Section 1 pool (1,224 questions)", () => {
    expect(questions.length).toBe(1224);
  });

  it("taxonomy is exactly 49 tags", () => {
    expect(SKILL_TAGS.size).toBe(49);
  });

  it("every question has a skill_tag", () => {
    const missing = questions.filter((q) => !q.skill_tag).map((q) => q.source);
    expect(missing).toEqual([]);
  });

  it("every skill_tag is in the locked taxonomy", () => {
    const offTaxonomy = questions
      .filter((q) => q.skill_tag && !SKILL_TAGS.has(q.skill_tag))
      .map((q) => `${q.source}:${q.skill_tag}`);
    expect(offTaxonomy).toEqual([]);
  });

  it("every question has a difficulty_tier consistent with its difficulty", () => {
    const wrong = questions
      .filter((q) => q.difficulty_tier !== expectedTier(q.difficulty))
      .map((q) => `${q.source}:${q.difficulty}->${q.difficulty_tier}`);
    expect(wrong).toEqual([]);
  });
});
