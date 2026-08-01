// SolidGeo course data — /math/solid-geometry. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { SOLIDGEO_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import sgPlanes from "@/data/genmath/solid-geometry/lines-and-planes-in-space.json";
import sgPrisms from "@/data/genmath/solid-geometry/prisms-and-the-cube.json";
import sgPyramids from "@/data/genmath/solid-geometry/pyramids.json";
import sgCylCones from "@/data/genmath/solid-geometry/cylinders-and-cones.json";
import sgSpheres from "@/data/genmath/solid-geometry/spheres.json";
import sgSections from "@/data/genmath/solid-geometry/cross-sections-and-similar-solids.json";

const solidGeoUnits: CourseUnit[] = [
  sgPlanes as unknown as CourseUnit,
  sgPrisms as unknown as CourseUnit,
  sgPyramids as unknown as CourseUnit,
  sgCylCones as unknown as CourseUnit,
  sgSpheres as unknown as CourseUnit,
  sgSections as unknown as CourseUnit,
];

export function getSolidGeoSpine(): GeometrySpineEntry[] {
  return SOLIDGEO_SPINE;
}

export function getSolidGeoUnit(unitSlug: string): CourseUnit | null {
  return solidGeoUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getSolidGeoLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getSolidGeoUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
