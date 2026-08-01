// Alg2 course data — /math/algebra-2. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { ALG2_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import a2Functions from "@/data/genmath/algebra-2/functions-and-transformations.json";
import a2Quadratics from "@/data/genmath/algebra-2/quadratics-and-complex-numbers.json";
import a2Systems from "@/data/genmath/algebra-2/systems-and-nonlinear-models.json";
import a2Polynomials from "@/data/genmath/algebra-2/polynomial-functions.json";
import a2Radicals from "@/data/genmath/algebra-2/radicals-and-rational-exponents.json";
import a2ExpLogs from "@/data/genmath/algebra-2/exponentials-and-logarithms.json";
import a2Rationals from "@/data/genmath/algebra-2/rational-functions.json";
import a2Sequences from "@/data/genmath/algebra-2/sequences-and-series.json";

const alg2Units: CourseUnit[] = [
  a2Functions as unknown as CourseUnit,
  a2Quadratics as unknown as CourseUnit,
  a2Systems as unknown as CourseUnit,
  a2Polynomials as unknown as CourseUnit,
  a2Radicals as unknown as CourseUnit,
  a2ExpLogs as unknown as CourseUnit,
  a2Rationals as unknown as CourseUnit,
  a2Sequences as unknown as CourseUnit,
];

export function getAlg2Spine(): GeometrySpineEntry[] {
  return ALG2_SPINE;
}

export function getAlg2Unit(unitSlug: string): CourseUnit | null {
  return alg2Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getAlg2Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getAlg2Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
