// Trig course data — /math/trigonometry. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { TRIG_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import trigRight from "@/data/genmath/trigonometry/right-triangle-trigonometry.json";
import trigSpecial from "@/data/genmath/trigonometry/special-triangles-and-exact-values.json";
import trigCircle from "@/data/genmath/trigonometry/radians-and-the-unit-circle.json";
import trigGraphs from "@/data/genmath/trigonometry/graphs-of-trig-functions.json";
import trigIdent from "@/data/genmath/trigonometry/identities-and-equations.json";
import trigLaws from "@/data/genmath/trigonometry/laws-of-sines-and-cosines.json";

const trigUnits: CourseUnit[] = [
  trigRight as unknown as CourseUnit,
  trigSpecial as unknown as CourseUnit,
  trigCircle as unknown as CourseUnit,
  trigGraphs as unknown as CourseUnit,
  trigIdent as unknown as CourseUnit,
  trigLaws as unknown as CourseUnit,
];

export function getTrigSpine(): GeometrySpineEntry[] {
  return TRIG_SPINE;
}

export function getTrigUnit(unitSlug: string): CourseUnit | null {
  return trigUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getTrigLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getTrigUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
