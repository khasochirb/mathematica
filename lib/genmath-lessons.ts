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
// Grade 8 topic JSON imports (added as each topic is authored + published).
import realNumberSystem from "@/data/genmath/8/the-real-number-system.json";
import exponentsScientific from "@/data/genmath/8/exponents-and-scientific-notation.json";
import roots from "@/data/genmath/8/roots.json";
import linearEquations from "@/data/genmath/8/linear-equations.json";
import linearFunctions from "@/data/genmath/8/linear-functions.json";
import systemsOfEquations from "@/data/genmath/8/systems-of-linear-equations.json";
import scatterPlots from "@/data/genmath/8/scatter-plots-and-bivariate-data.json";
// Grade 10 topic JSON imports (added as each topic is authored + published).
import polynomialsAndFactoring from "@/data/genmath/10/polynomials-and-factoring.json";
import quadraticEquations from "@/data/genmath/10/quadratic-equations.json";
import quadraticFunctions from "@/data/genmath/10/quadratic-functions.json";
import rationalExpressions from "@/data/genmath/10/rational-expressions.json";
import radicalsRationalExponents from "@/data/genmath/10/radicals-and-rational-exponents.json";
import exponentialFunctions from "@/data/genmath/10/exponential-functions.json";
import probabilityAndCounting from "@/data/genmath/10/probability-and-counting.json";
// Grade 11 topic JSON imports (added as each topic is authored + published).
import functionsAndTransformations from "@/data/genmath/11/functions-and-transformations.json";
import polynomialFunctions from "@/data/genmath/11/polynomial-functions.json";
import logarithms from "@/data/genmath/11/logarithms.json";
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
import geometryTransformations from "@/data/genmath/geometry/transformations.json";
import geometryCoordinate from "@/data/genmath/geometry/coordinate-geometry.json";

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
// Grade 8 — built incrementally, one topic at a time (same schema + gate).
// GRADE8_SPINE shows the whole roadmap from day one; `live` topics have
// authored data and link in, the rest render as "coming soon".
// ---------------------------------------------------------------------------

export interface GradeSpineEntry {
  slug: string;
  title: string;
  blurb: string;
  live: boolean;
}

export const GRADE8_SPINE: GradeSpineEntry[] = [
  {
    slug: "the-real-number-system",
    title: "The Real Number System",
    blurb: "Rational vs. irrational numbers, terminating and repeating decimals, classifying the reals, and placing any number on the line.",
    live: true,
  },
  {
    slug: "exponents-and-scientific-notation",
    title: "Exponents & Scientific Notation",
    blurb: "The laws of exponents, zero and negative powers, and writing huge and tiny numbers in scientific notation.",
    live: true,
  },
  {
    slug: "roots",
    title: "Square & Cube Roots",
    blurb: "Square roots and cube roots, perfect squares and cubes, and solving equations like x² = 49 and x³ = 8.",
    live: true,
  },
  {
    slug: "linear-equations",
    title: "Linear Equations",
    blurb: "Multi-step equations, variables on both sides, and equations with no solution or infinitely many.",
    live: true,
  },
  {
    slug: "linear-functions",
    title: "Linear Functions",
    blurb: "Slope and rate of change, y = mx + b, and reading a line four ways: table, graph, equation, and words.",
    live: true,
  },
  {
    slug: "systems-of-linear-equations",
    title: "Systems of Linear Equations",
    blurb: "Two lines at once — solving by graphing, substitution, and elimination, and what the intersection means.",
    live: true,
  },
  {
    slug: "scatter-plots-and-bivariate-data",
    title: "Scatter Plots & Bivariate Data",
    blurb: "Plotting paired data, spotting correlation, fitting a trend line, and reading two-way tables.",
    live: true,
  },
];

export const GRADE10_SPINE: GradeSpineEntry[] = [
  {
    slug: "polynomials-and-factoring",
    title: "Polynomials & Factoring",
    blurb: "Terms, degree, and standard form; adding, subtracting, and multiplying polynomials; factoring from GCF to trinomials — and solving by the zero product.",
    live: true,
  },
  {
    slug: "quadratic-equations",
    title: "Quadratic Equations",
    blurb: "Solving by factoring, square roots, completing the square, and the quadratic formula — plus the discriminant.",
    live: true,
  },
  {
    slug: "quadratic-functions",
    title: "Quadratic Functions & Parabolas",
    blurb: "Graphs of y = ax² + bx + c: vertex, axis of symmetry, transformations, and max/min word problems.",
    live: true,
  },
  {
    slug: "rational-expressions",
    title: "Rational Expressions & Equations",
    blurb: "Simplifying, multiplying, and adding algebraic fractions; solving rational equations and spotting excluded values.",
    live: true,
  },
  {
    slug: "radicals-and-rational-exponents",
    title: "Radicals & Rational Exponents",
    blurb: "Operations with radicals, rationalizing, fractional exponents, and solving radical equations.",
    live: true,
  },
  {
    slug: "exponential-functions",
    title: "Exponential Functions & Growth",
    blurb: "y = a·bˣ: growth and decay, compound interest, and how exponentials outrun every line.",
    live: true,
  },
  {
    slug: "probability-and-counting",
    title: "Probability & Counting",
    blurb: "Counting principles, permutations and combinations, and probability of compound events.",
    live: true,
  },
];

export const GRADE11_SPINE: GradeSpineEntry[] = [
  {
    slug: "functions-and-transformations",
    title: "Functions & Transformations",
    blurb: "Function notation, domain and range, shifts, stretches, reflections — and inverse functions that undo it all.",
    live: true,
  },
  {
    slug: "polynomial-functions",
    title: "Polynomial Functions",
    blurb: "Cubics and beyond: end behavior, zeros and multiplicity, the remainder and factor theorems, and sketching from factors.",
    live: true,
  },
  {
    slug: "logarithms",
    title: "Logarithms",
    blurb: "The inverse of the exponential: log laws, solving exponential and log equations, and the scales that measure earthquakes and sound.",
    live: true,
  },
  {
    slug: "sequences-and-series",
    title: "Sequences & Series",
    blurb: "Arithmetic and geometric sequences, recursive and explicit rules, and the sums that add a whole list at once.",
    live: false,
  },
  {
    slug: "trigonometry-and-the-unit-circle",
    title: "Trigonometry & the Unit Circle",
    blurb: "Radians, the unit circle, sine and cosine as coordinates, and the waves they draw.",
    live: false,
  },
  {
    slug: "complex-numbers",
    title: "Complex Numbers",
    blurb: "The number i, arithmetic with a + bi, conjugates and division, and quadratics whose roots finally all exist.",
    live: false,
  },
  {
    slug: "statistics-and-data",
    title: "Statistics & Data",
    blurb: "Mean vs median, standard deviation, z-scores, and the normal curve that grades on it.",
    live: false,
  },
];

const grade11Topics: GenMathTopic[] = [
  functionsAndTransformations as GenMathTopic,
  polynomialFunctions as GenMathTopic,
  logarithms as GenMathTopic,
];

const grade10Topics: GenMathTopic[] = [
  polynomialsAndFactoring as GenMathTopic,
  quadraticEquations as GenMathTopic,
  quadraticFunctions as GenMathTopic,
  rationalExpressions as GenMathTopic,
  radicalsRationalExponents as GenMathTopic,
  exponentialFunctions as GenMathTopic,
  probabilityAndCounting as GenMathTopic,
];

const grade8Topics: GenMathTopic[] = [
  realNumberSystem as GenMathTopic,
  exponentsScientific as GenMathTopic,
  roots as GenMathTopic,
  linearEquations as GenMathTopic,
  linearFunctions as GenMathTopic,
  systemsOfEquations as GenMathTopic,
  scatterPlots as GenMathTopic,
];

// Every authored General-Math topic across grades. Topic slugs are unique
// across grades, so slug lookups stay unambiguous.
const allGenMathTopics: GenMathTopic[] = [...grade6Topics, ...grade8Topics, ...grade10Topics, ...grade11Topics];

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

const ALL_GRADES: GradeInfo[] = [
  { grade: 6, active: true },
  { grade: 7, active: false },
  { grade: 8, active: true },
  { grade: 9, active: false },
  { grade: 10, active: true },
  { grade: 11, active: true },
  { grade: 12, active: false },
];

export function listGrades(): GradeInfo[] {
  return ALL_GRADES;
}

export function getGrade6Topics(): GenMathTopic[] {
  return grade6Topics;
}

export function getGrade8Topics(): GenMathTopic[] {
  return grade8Topics;
}

export function getGrade8Spine(): GradeSpineEntry[] {
  return GRADE8_SPINE;
}

export function getGrade10Topics(): GenMathTopic[] {
  return grade10Topics;
}

export function getGrade10Spine(): GradeSpineEntry[] {
  return GRADE10_SPINE;
}

export function getGrade11Topics(): GenMathTopic[] {
  return grade11Topics;
}

export function getGrade11Spine(): GradeSpineEntry[] {
  return GRADE11_SPINE;
}

export function getGenMathTopic(topicSlug: string): GenMathTopic | null {
  return allGenMathTopics.find((t) => t.slug === topicSlug) ?? null;
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
    live: true,
  },
  {
    unit: 13,
    slug: "coordinate-geometry",
    title: "Coordinate Geometry",
    blurb: "Distance, midpoint, and slope; equations of lines and circles; proofs with coordinates — the course capstone.",
    buildsOn: "Everything — algebra meets every earlier unit.",
    live: true,
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
  geometryTransformations as unknown as GeometryUnit,
  geometryCoordinate as unknown as GeometryUnit,
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
