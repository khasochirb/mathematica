// IbAiSl course data — /math/ib-ai-sl. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).
//
// The Applications & Interpretation track, alongside Analysis & Approaches in
// lib/genmath-data/ib-sl.ts. All five syllabus topics are live.

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { IB_AI_SL_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import ibAiSlNumberAlgebra from "@/data/genmath/ib-ai-sl/number-and-algebra.json";
import ibAiSlFunctions from "@/data/genmath/ib-ai-sl/functions.json";
import ibAiSlGeoTrig from "@/data/genmath/ib-ai-sl/geometry-and-trigonometry.json";
import ibAiSlStatsProb from "@/data/genmath/ib-ai-sl/statistics-and-probability.json";
import ibAiSlCalculus from "@/data/genmath/ib-ai-sl/calculus.json";

const ibAiSlUnits: CourseUnit[] = [
  ibAiSlNumberAlgebra as unknown as CourseUnit,
  ibAiSlFunctions as unknown as CourseUnit,
  ibAiSlGeoTrig as unknown as CourseUnit,
  ibAiSlStatsProb as unknown as CourseUnit,
  ibAiSlCalculus as unknown as CourseUnit,
];

export function getIbAiSlSpine(): GeometrySpineEntry[] {
  return IB_AI_SL_SPINE;
}

export function getIbAiSlUnit(unitSlug: string): CourseUnit | null {
  return ibAiSlUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getIbAiSlLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIbAiSlUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
