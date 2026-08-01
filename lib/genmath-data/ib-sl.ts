// IbSl course data — /math/ib-sl. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IB_SL_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import ibSlNumberAlgebra from "@/data/genmath/ib-sl/number-and-algebra.json";
import ibSlFunctions from "@/data/genmath/ib-sl/functions.json";
import ibSlGeoTrig from "@/data/genmath/ib-sl/geometry-and-trigonometry.json";
import ibSlStatsProb from "@/data/genmath/ib-sl/statistics-and-probability.json";
import ibSlCalculus from "@/data/genmath/ib-sl/calculus.json";

const ibSlUnits: CourseUnit[] = [
  ibSlNumberAlgebra as unknown as CourseUnit,
  ibSlFunctions as unknown as CourseUnit,
  ibSlGeoTrig as unknown as CourseUnit,
  ibSlStatsProb as unknown as CourseUnit,
  ibSlCalculus as unknown as CourseUnit,
];

export function getIbSlSpine(): GeometrySpineEntry[] {
  return IB_SL_SPINE;
}

export function getIbSlUnit(unitSlug: string): CourseUnit | null {
  return ibSlUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getIbSlLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIbSlUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
