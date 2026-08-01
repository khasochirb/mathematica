// Precalc course data — /math/precalculus. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { PRECALC_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import pcFunctions from "@/data/genmath/precalculus/functions-and-their-graphs.json";
import pcTransforms from "@/data/genmath/precalculus/transformations-of-graphs.json";
import pcPolyFns from "@/data/genmath/precalculus/polynomial-functions.json";
import pcRationals from "@/data/genmath/precalculus/rational-functions.json";
import pcExpLogs from "@/data/genmath/precalculus/exponentials-and-logarithms.json";
import pcUnitCircle from "@/data/genmath/precalculus/the-unit-circle.json";
import pcTrigGraphs from "@/data/genmath/precalculus/trigonometric-graphs-and-equations.json";
import pcConics from "@/data/genmath/precalculus/conic-sections.json";

const precalcUnits: CourseUnit[] = [
  pcFunctions as unknown as CourseUnit,
  pcTransforms as unknown as CourseUnit,
  pcPolyFns as unknown as CourseUnit,
  pcRationals as unknown as CourseUnit,
  pcExpLogs as unknown as CourseUnit,
  pcUnitCircle as unknown as CourseUnit,
  pcTrigGraphs as unknown as CourseUnit,
  pcConics as unknown as CourseUnit,
];

export function getPrecalcSpine(): GeometrySpineEntry[] {
  return PRECALC_SPINE;
}

export function getPrecalcUnit(unitSlug: string): CourseUnit | null {
  return precalcUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getPrecalcLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getPrecalcUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
