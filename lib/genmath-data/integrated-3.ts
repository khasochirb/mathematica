// Im3 course data — /math/integrated-3. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IM3_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import im3Polynomials from "@/data/genmath/integrated-3/polynomial-functions.json";
import im3Rational from "@/data/genmath/integrated-3/rational-and-radical-functions.json";
import im3ExpLog from "@/data/genmath/integrated-3/exponential-and-logarithmic-functions.json";
import im3Trig from "@/data/genmath/integrated-3/trigonometric-functions.json";
import im3Families from "@/data/genmath/integrated-3/function-families-and-inverses.json";
import im3Series from "@/data/genmath/integrated-3/sequences-series-and-the-binomial-theorem.json";

const im3Units: CourseUnit[] = [
  im3Polynomials,
  im3Rational,
  im3ExpLog,
  im3Trig,
  im3Families,
  im3Series,
] as unknown as CourseUnit[];

export function getIm3Spine(): GeometrySpineEntry[] {
  return IM3_SPINE;
}

export function getIm3Unit(unitSlug: string): CourseUnit | null {
  return im3Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getIm3Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIm3Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
