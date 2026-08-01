// Im1 course data — /math/integrated-1. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IM1_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import im1Quantities from "@/data/genmath/integrated-1/quantities-and-expressions.json";
import im1LinearEq from "@/data/genmath/integrated-1/linear-equations-and-inequalities.json";
import im1Functions from "@/data/genmath/integrated-1/functions-and-sequences.json";
import im1LinearFn from "@/data/genmath/integrated-1/linear-functions.json";
import im1Systems from "@/data/genmath/integrated-1/systems-of-equations-and-inequalities.json";
import im1Exponential from "@/data/genmath/integrated-1/exponential-functions.json";
import im1Transformations from "@/data/genmath/integrated-1/transformations-and-congruence.json";
import im1CoordGeo from "@/data/genmath/integrated-1/coordinate-geometry.json";
import im1Data from "@/data/genmath/integrated-1/data-and-statistics.json";

const im1Units: CourseUnit[] = [
  im1Quantities as unknown as CourseUnit,
  im1LinearEq as unknown as CourseUnit,
  im1Functions as unknown as CourseUnit,
  im1LinearFn as unknown as CourseUnit,
  im1Systems as unknown as CourseUnit,
  im1Exponential as unknown as CourseUnit,
  im1Transformations as unknown as CourseUnit,
  im1CoordGeo as unknown as CourseUnit,
  im1Data as unknown as CourseUnit,
];

export function getIm1Spine(): GeometrySpineEntry[] {
  return IM1_SPINE;
}

export function getIm1Unit(unitSlug: string): CourseUnit | null {
  return im1Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getIm1Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIm1Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
