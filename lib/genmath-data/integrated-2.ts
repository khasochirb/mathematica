// Im2 course data — /math/integrated-2. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IM2_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import im2Radicals from "@/data/genmath/integrated-2/rational-exponents-and-radicals.json";
import im2Polynomials from "@/data/genmath/integrated-2/polynomials-and-factoring.json";
import im2Quadratics from "@/data/genmath/integrated-2/quadratic-functions.json";
import im2SolvingQuad from "@/data/genmath/integrated-2/solving-quadratic-equations.json";
import im2Similarity from "@/data/genmath/integrated-2/similarity-and-dilations.json";
import im2Trig from "@/data/genmath/integrated-2/right-triangle-trigonometry.json";
import im2Circles from "@/data/genmath/integrated-2/circles.json";
import im2Measurement from "@/data/genmath/integrated-2/geometric-measurement-and-modelling.json";
import im2Probability from "@/data/genmath/integrated-2/probability.json";

const im2Units: CourseUnit[] = [
  im2Radicals as unknown as CourseUnit,
  im2Polynomials as unknown as CourseUnit,
  im2Quadratics as unknown as CourseUnit,
  im2SolvingQuad as unknown as CourseUnit,
  im2Similarity as unknown as CourseUnit,
  im2Trig as unknown as CourseUnit,
  im2Circles as unknown as CourseUnit,
  im2Measurement as unknown as CourseUnit,
  im2Probability as unknown as CourseUnit,
];

export function getIm2Spine(): GeometrySpineEntry[] {
  return IM2_SPINE;
}

export function getIm2Unit(unitSlug: string): CourseUnit | null {
  return im2Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getIm2Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIm2Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
