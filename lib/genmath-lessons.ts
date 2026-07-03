// General Math hub — data model + static registry.
// Authored inline (no question-bank dependency). Shares the hub-agnostic
// LessonProblem / LessonFact / LessonMistake types from lib/lesson-types.ts.

import type { LessonProblem, LessonFact, LessonMistake } from "@/lib/lesson-types";
import type { InteractiveLesson } from "@/lib/genmath-interactive";

export interface TryThis {
  title: string;
  body: string;
}

export interface GenMathLesson {
  slug: string;
  title: string;
  concreteComparison: string; // REQUIRED — real-world opener (MathText string)
  objective: string;
  concept: string[];           // paragraphs
  keyIdea?: string;
  tryThis?: TryThis;
  facts?: LessonFact[];
  workedExamples: LessonProblem[]; // authored inline
  commonMistakes: LessonMistake[];
  tryIt: LessonProblem[];          // short inline practice
  // When present, the route renders the paced interactive experience instead of
  // the static scroll page. Other topics omit this and stay static.
  interactive?: InteractiveLesson;
}

export interface GenMathTopic {
  slug: string;
  title: string;
  grade: number;
  blurb: string;
  // "published" topics are fully authored + sympy-verified (gated by
  // verify:genmath). Absent/"placeholder" topics are scaffold-only and exempt.
  status?: "published" | "placeholder";
  lessons: GenMathLesson[];
  practice: LessonProblem[];
  testYourself: LessonProblem[];
}

export interface GradeInfo {
  grade: number;
  active: boolean;
}

// ---------------------------------------------------------------------------
// Static registry — grade 6 topic JSON imports
// ---------------------------------------------------------------------------

import ratiosAndRates from "@/data/genmath/6/ratios-and-rates.json";
import fractions from "@/data/genmath/6/fractions.json";
import decimals from "@/data/genmath/6/decimals.json";
import percentages from "@/data/genmath/6/percentages.json";
import integers from "@/data/genmath/6/integers.json";
import factorsAndMultiples from "@/data/genmath/6/factors-and-multiples.json";
import expressionsAndEquations from "@/data/genmath/6/expressions-and-equations.json";
import coordinatePlane from "@/data/genmath/6/coordinate-plane.json";
import geometryAreaVolume from "@/data/genmath/6/geometry-area-volume.json";
import dataAndStatistics from "@/data/genmath/6/data-and-statistics.json";
import geometryFoundations from "@/data/genmath/geometry/foundations.json";
import geometryReasoning from "@/data/genmath/geometry/reasoning-and-proof.json";
import geometryParallel from "@/data/genmath/geometry/parallel-and-perpendicular.json";
import geometryTriangles from "@/data/genmath/geometry/triangles-and-congruence.json";
import geometryRelationships from "@/data/genmath/geometry/relationships-in-triangles.json";
import geometryQuadrilaterals from "@/data/genmath/geometry/quadrilaterals-and-polygons.json";
import geometrySimilarity from "@/data/genmath/geometry/similarity.json";
import geometryRightTriangles from "@/data/genmath/geometry/right-triangles-and-trig.json";
import geometryCircles from "@/data/genmath/geometry/circles.json";
import geometryAreaPerimeter from "@/data/genmath/geometry/area-and-perimeter.json";
import geometrySurfaceVolume from "@/data/genmath/geometry/surface-area-and-volume.json";

const grade6Topics: GenMathTopic[] = [
  ratiosAndRates as GenMathTopic,
  fractions as GenMathTopic,
  decimals as GenMathTopic,
  percentages as GenMathTopic,
  integers as GenMathTopic,
  factorsAndMultiples as GenMathTopic,
  expressionsAndEquations as GenMathTopic,
  coordinatePlane as GenMathTopic,
  geometryAreaVolume as GenMathTopic,
  dataAndStatistics as GenMathTopic,
];

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

const ALL_GRADES: GradeInfo[] = [
  { grade: 6, active: true },
  { grade: 7, active: false },
  { grade: 8, active: false },
  { grade: 9, active: false },
  { grade: 10, active: false },
  { grade: 11, active: false },
  { grade: 12, active: false },
];

export function listGrades(): GradeInfo[] {
  return ALL_GRADES;
}

export function getGrade6Topics(): GenMathTopic[] {
  return grade6Topics;
}

export function getGenMathTopic(topicSlug: string): GenMathTopic | null {
  return grade6Topics.find((t) => t.slug === topicSlug) ?? null;
}

export function getGenMathLesson(
  topicSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const topic = getGenMathTopic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Geometry — a standalone subject course (single source of truth for geometry).
// One continuous, near-linear spine; grade hubs will later LINK into units
// rather than re-authoring them. Same lesson schema as grade-6 topics, so the
// verify:genmath gate covers it automatically.
// ---------------------------------------------------------------------------

export interface GeometryUnit extends Omit<GenMathTopic, "grade"> {
  unit: number;
  buildsOn?: string; // what earlier units this one rests on
}

// The full course spine. `live` units have authored data; the rest render as
// "coming soon" so the whole track is visible from day one.
export interface GeometrySpineEntry {
  unit: number;
  slug: string;
  title: string;
  blurb: string;
  buildsOn?: string;
  live: boolean;
}

export const GEOMETRY_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "foundations",
    title: "Foundations: Points, Lines & Angles",
    blurb: "Points, lines, rays, segments and planes; measuring segments and angles; angle types, angle pairs, and bisectors.",
    buildsOn: "Nothing — geometry starts here, from zero.",
    live: true,
  },
  {
    unit: 2,
    slug: "reasoning-and-proof",
    title: "Reasoning & Proof",
    blurb: "From noticing patterns to proving facts: conjectures, if-then statements, and your first two-column proofs.",
    buildsOn: "Unit 1's definitions and the segment/angle facts you measured there.",
    live: true,
  },
  {
    unit: 3,
    slug: "parallel-and-perpendicular",
    title: "Parallel & Perpendicular Lines",
    blurb: "Transversals and the angle pairs they create — which are congruent, which are supplementary — and proving lines parallel.",
    buildsOn: "Angle pairs from Unit 1; the proof habits from Unit 2.",
    live: true,
  },
  {
    unit: 4,
    slug: "triangles-and-congruence",
    title: "Triangles & Congruence",
    blurb: "Triangle types, the angle sum, the triangle inequality, and the congruence shortcuts SSS · SAS · ASA · AAS · HL.",
    buildsOn: "Units 1–3: angles, proof, and parallel-line facts.",
    live: true,
  },
  {
    unit: 5,
    slug: "relationships-in-triangles",
    title: "Relationships in Triangles",
    blurb: "Bisectors, medians, altitudes, the midsegment theorem, and inequalities inside a triangle.",
    buildsOn: "Triangle congruence from Unit 4.",
    live: true,
  },
  {
    unit: 6,
    slug: "quadrilaterals-and-polygons",
    title: "Quadrilaterals & Polygons",
    blurb: "Angle sums for any polygon; parallelograms, rectangles, rhombi, squares, trapezoids, and kites — with proofs.",
    buildsOn: "Triangles (Unit 4) and parallel lines (Unit 3).",
    live: true,
  },
  {
    unit: 7,
    slug: "similarity",
    title: "Similarity",
    blurb: "Ratio and proportion, similar polygons, the AA · SSS · SAS similarity shortcuts, and the side-splitter theorem.",
    buildsOn: "Triangle facts from Units 4–5; ratios from Grade 6.",
    live: true,
  },
  {
    unit: 8,
    slug: "right-triangles-and-trig",
    title: "Right Triangles & Trigonometry",
    blurb: "The Pythagorean theorem, special right triangles, and sine · cosine · tangent with elevation and depression.",
    buildsOn: "Similarity (Unit 7) — trig ratios ARE similarity.",
    live: true,
  },
  {
    unit: 9,
    slug: "circles",
    title: "Circles",
    blurb: "Radius, chord, tangent, secant; central and inscribed angles; arcs; and the circle relationships.",
    buildsOn: "Angles (Unit 1), triangles (Unit 4), and right triangles (Unit 8).",
    live: true,
  },
  {
    unit: 10,
    slug: "area-and-perimeter",
    title: "Area & Perimeter",
    blurb: "Areas of triangles, quadrilaterals and regular polygons; circumference, circle area, sectors, and composite figures.",
    buildsOn: "The shape properties from Units 4, 6, and 9.",
    live: true,
  },
  {
    unit: 11,
    slug: "surface-area-and-volume",
    title: "Surface Area & Volume",
    blurb: "Prisms, cylinders, pyramids, cones, and spheres — wrapping and filling 3-D solids.",
    buildsOn: "Area formulas from Unit 10.",
    live: true,
  },
  {
    unit: 12,
    slug: "transformations",
    title: "Transformations",
    blurb: "Translations, reflections, rotations, and dilations; symmetry; congruence and similarity re-seen through motion.",
    buildsOn: "Congruence (Unit 4) and similarity (Unit 7).",
    live: false,
  },
  {
    unit: 13,
    slug: "coordinate-geometry",
    title: "Coordinate Geometry",
    blurb: "Distance, midpoint, and slope; equations of lines and circles; proofs with coordinates — the course capstone.",
    buildsOn: "Everything — algebra meets every earlier unit.",
    live: false,
  },
];

const geometryUnits: GeometryUnit[] = [
  geometryFoundations as unknown as GeometryUnit,
  geometryReasoning as unknown as GeometryUnit,
  geometryParallel as unknown as GeometryUnit,
  geometryTriangles as unknown as GeometryUnit,
  geometryRelationships as unknown as GeometryUnit,
  geometryQuadrilaterals as unknown as GeometryUnit,
  geometrySimilarity as unknown as GeometryUnit,
  geometryRightTriangles as unknown as GeometryUnit,
  geometryCircles as unknown as GeometryUnit,
  geometryAreaPerimeter as unknown as GeometryUnit,
  geometrySurfaceVolume as unknown as GeometryUnit,
];

export function getGeometrySpine(): GeometrySpineEntry[] {
  return GEOMETRY_SPINE;
}

export function getGeometryUnit(unitSlug: string): GeometryUnit | null {
  return geometryUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getGeometryLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getGeometryUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Validation
// ---------------------------------------------------------------------------

export function validateGenMathLesson(lesson: GenMathLesson): string[] {
  const errors: string[] = [];
  if (!lesson.concreteComparison || lesson.concreteComparison.trim() === "") {
    errors.push("concreteComparison is required and must not be empty");
  }
  if (!lesson.title || lesson.title.trim() === "") {
    errors.push("title is required and must not be empty");
  }
  if (!lesson.objective || lesson.objective.trim() === "") {
    errors.push("objective is required and must not be empty");
  }
  if (!lesson.concept || lesson.concept.length === 0) {
    errors.push("concept must have at least one paragraph");
  }
  if (!lesson.workedExamples || lesson.workedExamples.length === 0) {
    errors.push("workedExamples must have at least one example");
  }
  return errors;
}
