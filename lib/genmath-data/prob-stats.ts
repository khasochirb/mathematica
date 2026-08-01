// ProbStat course data — /math/prob-stats. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { PROBSTAT_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import psCountingPrinciples from "@/data/genmath/prob-stats/counting-principles.json";
import psPermutations from "@/data/genmath/prob-stats/permutations.json";
import psCombinations from "@/data/genmath/prob-stats/combinations.json";
import psBinomialTheorem from "@/data/genmath/prob-stats/binomial-theorem.json";
import psProbabilityModels from "@/data/genmath/prob-stats/probability-models.json";
import psConditional from "@/data/genmath/prob-stats/conditional-probability.json";
import psRandomVariables from "@/data/genmath/prob-stats/random-variables.json";
import psBinomialDist from "@/data/genmath/prob-stats/binomial-distribution.json";
import psDescribingData from "@/data/genmath/prob-stats/describing-data.json";
import psDistPosition from "@/data/genmath/prob-stats/distributions-and-position.json";
import psTwoVariable from "@/data/genmath/prob-stats/two-variable-data.json";
import psInference from "@/data/genmath/prob-stats/inference-and-studies.json";

const probStatUnits: CourseUnit[] = [
  psCountingPrinciples as unknown as CourseUnit,
  psPermutations as unknown as CourseUnit,
  psCombinations as unknown as CourseUnit,
  psBinomialTheorem as unknown as CourseUnit,
  psProbabilityModels as unknown as CourseUnit,
  psConditional as unknown as CourseUnit,
  psRandomVariables as unknown as CourseUnit,
  psBinomialDist as unknown as CourseUnit,
  psDescribingData as unknown as CourseUnit,
  psDistPosition as unknown as CourseUnit,
  psTwoVariable as unknown as CourseUnit,
  psInference as unknown as CourseUnit,
];

export function getProbStatSpine(): GeometrySpineEntry[] {
  return PROBSTAT_SPINE;
}

export function getProbStatUnit(unitSlug: string): CourseUnit | null {
  return probStatUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getProbStatLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getProbStatUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
