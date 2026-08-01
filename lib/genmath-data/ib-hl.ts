// IbHl course data — /math/ib-hl. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IB_HL_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import ibHlNumberAlgebra from "@/data/genmath/ib-hl/number-and-algebra.json";
import ibHlFunctions from "@/data/genmath/ib-hl/functions.json";
import ibHlGeoTrig from "@/data/genmath/ib-hl/geometry-and-trigonometry.json";
import ibHlStatsProb from "@/data/genmath/ib-hl/statistics-and-probability.json";
import ibHlCalculus from "@/data/genmath/ib-hl/calculus.json";

const ibHlUnits: CourseUnit[] = [
  ibHlNumberAlgebra as unknown as CourseUnit,
  ibHlFunctions as unknown as CourseUnit,
  ibHlGeoTrig as unknown as CourseUnit,
  ibHlStatsProb as unknown as CourseUnit,
  ibHlCalculus as unknown as CourseUnit,
];

export function getIbHlSpine(): GeometrySpineEntry[] {
  return IB_HL_SPINE;
}

export function getIbHlUnit(unitSlug: string): CourseUnit | null {
  return ibHlUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getIbHlLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIbHlUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
