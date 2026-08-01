// Courses hub — data model + static registry.
// Authored inline (no question-bank dependency). Shares the hub-agnostic
// LessonProblem / LessonFact / LessonMistake types from lib/lesson-types.ts.

import type { LessonProblem, LessonFact, LessonMistake } from "@/lib/lesson-types";
import type { InteractiveLesson } from "@/lib/genmath-interactive";
// Spines and grade metadata live in lib/genmath-spines.ts (data-free, see
// its header); re-exported here so content code has one registry to import.
import {
  listGrades,
  GRADE7_SPINE,
  GRADE8_SPINE,
  GRADE9_SPINE,
  GRADE10_SPINE,
  GRADE11_SPINE,
  GRADE12_SPINE,
  GEOMETRY_SPINE,
  PROBSTAT_SPINE,
  VECMAT_SPINE,
  ALG1_SPINE,
  IM1_SPINE,
  IM2_SPINE,
  IM3_SPINE,
  ALG2_SPINE,
  PRECALC_SPINE,
  CALC_SPINE,
  TRIG_SPINE,
  SOLIDGEO_SPINE,
  IB_SL_SPINE,
  IB_HL_SPINE,
  GRADE6_SPINE,
} from "@/lib/genmath-spines";
export {
  listGrades,
  GRADE7_SPINE,
  GRADE8_SPINE,
  GRADE9_SPINE,
  GRADE10_SPINE,
  GRADE11_SPINE,
  GRADE12_SPINE,
  GEOMETRY_SPINE,
  PROBSTAT_SPINE,
  VECMAT_SPINE,
  ALG1_SPINE,
  IM1_SPINE,
  IM2_SPINE,
  IM3_SPINE,
  ALG2_SPINE,
  PRECALC_SPINE,
  CALC_SPINE,
  TRIG_SPINE,
  SOLIDGEO_SPINE,
  IB_SL_SPINE,
  IB_HL_SPINE,
  GRADE6_SPINE,
} from "@/lib/genmath-spines";
export type { GradeInfo, GradeSpineEntry, GeometrySpineEntry } from "@/lib/genmath-spines";
import type { GradeInfo, GradeSpineEntry, GeometrySpineEntry } from "@/lib/genmath-spines";


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
// Grade 7 topic JSON imports (added as each topic is authored + published).
import proportionalRelationships from "@/data/genmath/7/proportional-relationships.json";
import rationalNumberOperations from "@/data/genmath/7/rational-number-operations.json";
import equationsAndInequalities from "@/data/genmath/7/equations-and-inequalities.json";
import percentApplications from "@/data/genmath/7/percent-applications.json";
import geometryScaleCircles from "@/data/genmath/7/geometry-scale-and-circles.json";
import probability7 from "@/data/genmath/7/probability.json";
import samplingAndStatistics from "@/data/genmath/7/sampling-and-statistics.json";
// Grade 9 topic JSON imports (added as each topic is authored + published).
import equationsAndFormulas from "@/data/genmath/9/equations-and-formulas.json";
import inequalitiesAbsValue from "@/data/genmath/9/inequalities-and-absolute-value.json";
import introToFunctions from "@/data/genmath/9/introduction-to-functions.json";
import linearModelsVariation from "@/data/genmath/9/linear-models-and-variation.json";
import inequalitiesTwoVars from "@/data/genmath/9/inequalities-in-two-variables.json";
import piecewiseAbsGraphs from "@/data/genmath/9/piecewise-and-absolute-value-graphs.json";
import dataDistributions from "@/data/genmath/9/data-distributions.json";
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
import sequencesAndSeries from "@/data/genmath/11/sequences-and-series.json";
import trigonometryUnitCircle from "@/data/genmath/11/trigonometry-and-the-unit-circle.json";
import complexNumbers from "@/data/genmath/11/complex-numbers.json";
import statisticsAndData from "@/data/genmath/11/statistics-and-data.json";
// Grade 12 topic JSON imports (added as each topic is authored + published).
import trigonometricIdentities from "@/data/genmath/12/trigonometric-identities.json";
import limitsAndContinuity from "@/data/genmath/12/limits-and-continuity.json";
import derivatives from "@/data/genmath/12/derivatives.json";
import applicationsOfDerivatives from "@/data/genmath/12/applications-of-derivatives.json";
import integrals from "@/data/genmath/12/integrals.json";
import vectors from "@/data/genmath/12/vectors.json";
import conicSections from "@/data/genmath/12/conic-sections.json";
// Mongolian mirrors of the Grade 8 topics (identical structure/ids/checks;
// every prose string translated). Resolved by getGenMathTopicLocalized when
// the site language is "mn".
import realNumberSystemMn from "@/data/genmath/8-mn/the-real-number-system.json";
import exponentsScientificMn from "@/data/genmath/8-mn/exponents-and-scientific-notation.json";
import rootsMn from "@/data/genmath/8-mn/roots.json";
import linearEquationsMn from "@/data/genmath/8-mn/linear-equations.json";
import linearFunctionsMn from "@/data/genmath/8-mn/linear-functions.json";
import systemsMn from "@/data/genmath/8-mn/systems-of-linear-equations.json";
import scatterMn from "@/data/genmath/8-mn/scatter-plots-and-bivariate-data.json";
import ratiosMn from "@/data/genmath/6-mn/ratios-and-rates.json";
import fractionsMn from "@/data/genmath/6-mn/fractions.json";
import decimalsMn from "@/data/genmath/6-mn/decimals.json";
import percentagesMn from "@/data/genmath/6-mn/percentages.json";
import integersMn from "@/data/genmath/6-mn/integers.json";
import factorsMn from "@/data/genmath/6-mn/factors-and-multiples.json";
import exprMn from "@/data/genmath/6-mn/expressions-and-equations.json";
import coordMn from "@/data/genmath/6-mn/coordinate-plane.json";
import geoAvMn from "@/data/genmath/6-mn/geometry-area-volume.json";
import dataStatsMn from "@/data/genmath/6-mn/data-and-statistics.json";
import g7ProportionalMn from "@/data/genmath/7-mn/proportional-relationships.json";
import g7RationalOpsMn from "@/data/genmath/7-mn/rational-number-operations.json";
import g7EqIneqMn from "@/data/genmath/7-mn/equations-and-inequalities.json";
import g7PercentMn from "@/data/genmath/7-mn/percent-applications.json";
import g7GeoScaleMn from "@/data/genmath/7-mn/geometry-scale-and-circles.json";
import g7ProbabilityMn from "@/data/genmath/7-mn/probability.json";
import g7SamplingMn from "@/data/genmath/7-mn/sampling-and-statistics.json";
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
import psCountingPrinciples from "@/data/genmath/prob-stats/counting-principles.json";
import psPermutations from "@/data/genmath/prob-stats/permutations.json";
import psCombinations from "@/data/genmath/prob-stats/combinations.json";
import psBinomialTheorem from "@/data/genmath/prob-stats/binomial-theorem.json";
import psProbabilityModels from "@/data/genmath/prob-stats/probability-models.json";
import psConditional from "@/data/genmath/prob-stats/conditional-probability.json";
import psRandomVariables from "@/data/genmath/prob-stats/random-variables.json";
import psBinomialDist from "@/data/genmath/prob-stats/binomial-distribution.json";
import psDescribingData from "@/data/genmath/prob-stats/describing-data.json";
import psDistPosition from "@/data/genmath/prob-stats/distributions-and-position.json";
import psTwoVariable from "@/data/genmath/prob-stats/two-variable-data.json";
import psInference from "@/data/genmath/prob-stats/inference-and-studies.json";
import vmVectorsCoords from "@/data/genmath/vectors-matrices/vectors-and-coordinates.json";
import vmArithmetic from "@/data/genmath/vectors-matrices/vector-arithmetic.json";
import vmDotProduct from "@/data/genmath/vectors-matrices/the-dot-product.json";
import vmSpace from "@/data/genmath/vectors-matrices/vectors-in-space.json";
import vmMatrices from "@/data/genmath/vectors-matrices/matrices-and-operations.json";
import vmDeterminants from "@/data/genmath/vectors-matrices/determinants-and-inverses.json";
import a1Expressions from "@/data/genmath/algebra-1/expressions-and-operations.json";
import a1LinearEq from "@/data/genmath/algebra-1/linear-equations.json";
import a1Inequalities from "@/data/genmath/algebra-1/inequalities.json";
import a1Functions from "@/data/genmath/algebra-1/functions.json";
import a1LinearFn from "@/data/genmath/algebra-1/linear-functions.json";
import a1Systems from "@/data/genmath/algebra-1/systems-of-equations.json";
import a1Polynomials from "@/data/genmath/algebra-1/polynomials-and-factoring.json";
import a1Quadratics from "@/data/genmath/algebra-1/quadratic-equations.json";

// Integrated Mathematics 1 unit JSON imports
import im1Quantities from "@/data/genmath/integrated-1/quantities-and-expressions.json";
import im1LinearEq from "@/data/genmath/integrated-1/linear-equations-and-inequalities.json";
import im1Functions from "@/data/genmath/integrated-1/functions-and-sequences.json";
import im1LinearFn from "@/data/genmath/integrated-1/linear-functions.json";
import im1Systems from "@/data/genmath/integrated-1/systems-of-equations-and-inequalities.json";
import im1Exponential from "@/data/genmath/integrated-1/exponential-functions.json";
import im1Transformations from "@/data/genmath/integrated-1/transformations-and-congruence.json";
import im1CoordGeo from "@/data/genmath/integrated-1/coordinate-geometry.json";
import im1Data from "@/data/genmath/integrated-1/data-and-statistics.json";
import im2Radicals from "@/data/genmath/integrated-2/rational-exponents-and-radicals.json";
import im2Polynomials from "@/data/genmath/integrated-2/polynomials-and-factoring.json";
import im2Quadratics from "@/data/genmath/integrated-2/quadratic-functions.json";
import im2SolvingQuad from "@/data/genmath/integrated-2/solving-quadratic-equations.json";
import im2Similarity from "@/data/genmath/integrated-2/similarity-and-dilations.json";
import im2Trig from "@/data/genmath/integrated-2/right-triangle-trigonometry.json";
import im2Circles from "@/data/genmath/integrated-2/circles.json";
import im2Probability from "@/data/genmath/integrated-2/probability.json";
// Integrated Math 3 unit JSON imports (added as each unit is authored).
import im3Polynomials from "@/data/genmath/integrated-3/polynomial-functions.json";
import im3Rational from "@/data/genmath/integrated-3/rational-and-radical-functions.json";
import im3ExpLog from "@/data/genmath/integrated-3/exponential-and-logarithmic-functions.json";
import im3Trig from "@/data/genmath/integrated-3/trigonometric-functions.json";

// Algebra 2 unit JSON imports
import a2Functions from "@/data/genmath/algebra-2/functions-and-transformations.json";
import a2Quadratics from "@/data/genmath/algebra-2/quadratics-and-complex-numbers.json";
import a2Systems from "@/data/genmath/algebra-2/systems-and-nonlinear-models.json";
import a2Polynomials from "@/data/genmath/algebra-2/polynomial-functions.json";
import a2Radicals from "@/data/genmath/algebra-2/radicals-and-rational-exponents.json";
import a2ExpLogs from "@/data/genmath/algebra-2/exponentials-and-logarithms.json";
import a2Rationals from "@/data/genmath/algebra-2/rational-functions.json";
import a2Sequences from "@/data/genmath/algebra-2/sequences-and-series.json";
import pcFunctions from "@/data/genmath/precalculus/functions-and-their-graphs.json";
import pcTransforms from "@/data/genmath/precalculus/transformations-of-graphs.json";
import pcPolyFns from "@/data/genmath/precalculus/polynomial-functions.json";
import pcRationals from "@/data/genmath/precalculus/rational-functions.json";
import pcExpLogs from "@/data/genmath/precalculus/exponentials-and-logarithms.json";
import pcUnitCircle from "@/data/genmath/precalculus/the-unit-circle.json";
import pcTrigGraphs from "@/data/genmath/precalculus/trigonometric-graphs-and-equations.json";
import pcConics from "@/data/genmath/precalculus/conic-sections.json";
import calLimits from "@/data/genmath/calculus/limits-and-continuity.json";
import calDeriv from "@/data/genmath/calculus/the-derivative.json";
import calTech from "@/data/genmath/calculus/differentiation-techniques.json";
import calDerivApps from "@/data/genmath/calculus/applications-of-derivatives.json";
import calIntegrals from "@/data/genmath/calculus/integrals.json";
import calIntApps from "@/data/genmath/calculus/applications-of-integrals.json";
import trigRight from "@/data/genmath/trigonometry/right-triangle-trigonometry.json";
import trigSpecial from "@/data/genmath/trigonometry/special-triangles-and-exact-values.json";
import trigCircle from "@/data/genmath/trigonometry/radians-and-the-unit-circle.json";
import trigGraphs from "@/data/genmath/trigonometry/graphs-of-trig-functions.json";
import trigIdent from "@/data/genmath/trigonometry/identities-and-equations.json";
import trigLaws from "@/data/genmath/trigonometry/laws-of-sines-and-cosines.json";
import ibSlNumberAlgebra from "@/data/genmath/ib-sl/number-and-algebra.json";
import ibSlFunctions from "@/data/genmath/ib-sl/functions.json";
import ibSlGeoTrig from "@/data/genmath/ib-sl/geometry-and-trigonometry.json";
import ibSlStatsProb from "@/data/genmath/ib-sl/statistics-and-probability.json";
import ibSlCalculus from "@/data/genmath/ib-sl/calculus.json";
import ibHlNumberAlgebra from "@/data/genmath/ib-hl/number-and-algebra.json";
import ibHlFunctions from "@/data/genmath/ib-hl/functions.json";
import ibHlGeoTrig from "@/data/genmath/ib-hl/geometry-and-trigonometry.json";
import ibHlStatsProb from "@/data/genmath/ib-hl/statistics-and-probability.json";
import ibHlCalculus from "@/data/genmath/ib-hl/calculus.json";
import sgPlanes from "@/data/genmath/solid-geometry/lines-and-planes-in-space.json";
import sgPrisms from "@/data/genmath/solid-geometry/prisms-and-the-cube.json";
import sgPyramids from "@/data/genmath/solid-geometry/pyramids.json";
import sgCylCones from "@/data/genmath/solid-geometry/cylinders-and-cones.json";
import sgSpheres from "@/data/genmath/solid-geometry/spheres.json";
import sgSections from "@/data/genmath/solid-geometry/cross-sections-and-similar-solids.json";

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








const grade12Topics: GenMathTopic[] = [
  trigonometricIdentities as GenMathTopic,
  limitsAndContinuity as GenMathTopic,
  derivatives as GenMathTopic,
  applicationsOfDerivatives as GenMathTopic,
  integrals as GenMathTopic,
  vectors as GenMathTopic,
  conicSections as GenMathTopic,
];

const grade11Topics: GenMathTopic[] = [
  functionsAndTransformations as GenMathTopic,
  polynomialFunctions as GenMathTopic,
  logarithms as GenMathTopic,
  sequencesAndSeries as GenMathTopic,
  trigonometryUnitCircle as GenMathTopic,
  complexNumbers as GenMathTopic,
  statisticsAndData as GenMathTopic,
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

const grade7Topics: GenMathTopic[] = [
  proportionalRelationships as GenMathTopic,
  rationalNumberOperations as GenMathTopic,
  equationsAndInequalities as GenMathTopic,
  percentApplications as GenMathTopic,
  geometryScaleCircles as GenMathTopic,
  probability7 as GenMathTopic,
  samplingAndStatistics as GenMathTopic,
];

const grade9Topics: GenMathTopic[] = [
  equationsAndFormulas as GenMathTopic,
  inequalitiesAbsValue as GenMathTopic,
  introToFunctions as GenMathTopic,
  linearModelsVariation as GenMathTopic,
  inequalitiesTwoVars as GenMathTopic,
  piecewiseAbsGraphs as GenMathTopic,
  dataDistributions as GenMathTopic,
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
const allGenMathTopics: GenMathTopic[] = [...grade6Topics, ...grade7Topics, ...grade8Topics, ...grade9Topics, ...grade10Topics, ...grade11Topics, ...grade12Topics];

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------



export function getGrade6Topics(): GenMathTopic[] {
  return grade6Topics;
}

export function getGrade7Topics(): GenMathTopic[] {
  return grade7Topics;
}

export function getGrade7Spine(): GradeSpineEntry[] {
  return GRADE7_SPINE;
}

export function getGrade8Topics(): GenMathTopic[] {
  return grade8Topics;
}

export function getGrade8Spine(): GradeSpineEntry[] {
  return GRADE8_SPINE;
}

export function getGrade9Topics(): GenMathTopic[] {
  return grade9Topics;
}

export function getGrade9Spine(): GradeSpineEntry[] {
  return GRADE9_SPINE;
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

export function getGrade12Topics(): GenMathTopic[] {
  return grade12Topics;
}

export function getGrade12Spine(): GradeSpineEntry[] {
  return GRADE12_SPINE;
}

export function getGenMathTopic(topicSlug: string): GenMathTopic | null {
  return allGenMathTopics.find((t) => t.slug === topicSlug) ?? null;
}

// Mongolian topic mirrors, keyed by slug. Grown as courses are localized.
const GENMATH_TOPICS_MN: Record<string, GenMathTopic> = {
  "the-real-number-system": realNumberSystemMn as GenMathTopic,
  "exponents-and-scientific-notation": exponentsScientificMn as GenMathTopic,
  "roots": rootsMn as GenMathTopic,
  "linear-equations": linearEquationsMn as GenMathTopic,
  "linear-functions": linearFunctionsMn as GenMathTopic,
  "systems-of-linear-equations": systemsMn as GenMathTopic,
  "scatter-plots-and-bivariate-data": scatterMn as GenMathTopic,
  "ratios-and-rates": ratiosMn as GenMathTopic,
  "fractions": fractionsMn as GenMathTopic,
  "decimals": decimalsMn as GenMathTopic,
  "percentages": percentagesMn as GenMathTopic,
  "integers": integersMn as GenMathTopic,
  "factors-and-multiples": factorsMn as GenMathTopic,
  "expressions-and-equations": exprMn as GenMathTopic,
  "coordinate-plane": coordMn as GenMathTopic,
  "geometry-area-volume": geoAvMn as GenMathTopic,
  "data-and-statistics": dataStatsMn as GenMathTopic,
  // Grade 7 mirrors (grown one topic at a time; slug-keyed, grade-agnostic).
  "proportional-relationships": g7ProportionalMn as GenMathTopic,
  "rational-number-operations": g7RationalOpsMn as GenMathTopic,
  "equations-and-inequalities": g7EqIneqMn as GenMathTopic,
  "percent-applications": g7PercentMn as GenMathTopic,
  "geometry-scale-and-circles": g7GeoScaleMn as GenMathTopic,
  "probability": g7ProbabilityMn as GenMathTopic,
  "sampling-and-statistics": g7SamplingMn as GenMathTopic,
};

// Locale-aware topic lookup: Mongolian mirror when the site language is "mn"
// and a translation exists; the English original otherwise.
export function getGenMathTopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && GENMATH_TOPICS_MN[topicSlug]) return GENMATH_TOPICS_MN[topicSlug];
  return getGenMathTopic(topicSlug);
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
// Combinatorics, Probability & Statistics — the second standalone course.
// Same architecture as Geometry: one near-linear spine in three acts
// (count → chance → data), same lesson schema, same verify:genmath gate.
// Units reuse the GeometryUnit shape (unit number + buildsOn, no grade).
// ---------------------------------------------------------------------------

export type CourseUnit = GeometryUnit;


const probStatUnits: CourseUnit[] = [
  psCountingPrinciples as unknown as CourseUnit,
  psPermutations as unknown as CourseUnit,
  psCombinations as unknown as CourseUnit,
  psBinomialTheorem as unknown as CourseUnit,
  psProbabilityModels as unknown as CourseUnit,
  psConditional as unknown as CourseUnit,
  psRandomVariables as unknown as CourseUnit,
  psBinomialDist as unknown as CourseUnit,
  psDescribingData as unknown as CourseUnit,
  psDistPosition as unknown as CourseUnit,
  psTwoVariable as unknown as CourseUnit,
  psInference as unknown as CourseUnit,
];

export function getProbStatSpine(): GeometrySpineEntry[] {
  return PROBSTAT_SPINE;
}

export function getProbStatUnit(unitSlug: string): CourseUnit | null {
  return probStatUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getProbStatLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getProbStatUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Vectors & Matrices course — /math/vectors-matrices
// Built to close the ЭЕШ linear_algebra gap: ~90 exam questions (vector
// arithmetic, dot products, space geometry, matrix operations, determinants,
// inverses) previously had no course to remediate into.
// ---------------------------------------------------------------------------


const vecMatUnits: CourseUnit[] = [
  vmVectorsCoords as unknown as CourseUnit,
  vmArithmetic as unknown as CourseUnit,
  vmDotProduct as unknown as CourseUnit,
  vmSpace as unknown as CourseUnit,
  vmMatrices as unknown as CourseUnit,
  vmDeterminants as unknown as CourseUnit,
];

export function getVecMatSpine(): GeometrySpineEntry[] {
  return VECMAT_SPINE;
}

export function getVecMatUnit(unitSlug: string): CourseUnit | null {
  return vecMatUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getVecMatLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getVecMatUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Algebra 1 course — /math/algebra-1
// The full first-algebra sequence taught as a topic course: expressions,
// linear equations, inequalities, functions, lines, systems, polynomials &
// factoring, quadratics. Reuses the interactive primitive library
// (balanceScale, algebraTiles, evaluator, coordinateGrid, orderOfOps,
// exponentBuilder, integerLine, absoluteValue).
// ---------------------------------------------------------------------------


const alg1Units: CourseUnit[] = [
  a1Expressions as unknown as CourseUnit,
  a1LinearEq as unknown as CourseUnit,
  a1Inequalities as unknown as CourseUnit,
  a1Functions as unknown as CourseUnit,
  a1LinearFn as unknown as CourseUnit,
  a1Systems as unknown as CourseUnit,
  a1Polynomials as unknown as CourseUnit,
  a1Quadratics as unknown as CourseUnit,
];

export function getAlg1Spine(): GeometrySpineEntry[] {
  return ALG1_SPINE;
}

export function getAlg1Unit(unitSlug: string): CourseUnit | null {
  return alg1Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getAlg1Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getAlg1Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Integrated Mathematics 1 — /math/integrated-1
// The first year of the integrated pathway (CCSS Integrated Mathematics I).
// Where Algebra 1 → Geometry → Algebra 2 teaches one subject at a time, the
// integrated pathway mixes algebra, geometry and statistics inside every year:
// IM1 runs from quantities and linear models through congruence and coordinate
// proof to one-variable data. Same lesson schema, same widget library, same
// verify:genmath gate as every other course here.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// Integrated Mathematics 2 — /math/integrated-2
// The middle year of the integrated pathway (CCSS Integrated Mathematics II).
// Quadratics end to end, the number system extended to rational exponents and
// complex numbers, similarity and right-triangle trigonometry, circles, and
// probability. Where IM1 was linear and exponential, IM2 is quadratic — and
// where IM1 defined congruence by rigid motion, IM2 defines similarity by
// dilation and proves with it.
// ---------------------------------------------------------------------------


const im2Units: CourseUnit[] = [
  im2Radicals as unknown as CourseUnit,
  im2Polynomials as unknown as CourseUnit,
  im2Quadratics as unknown as CourseUnit,
  im2SolvingQuad as unknown as CourseUnit,
  im2Similarity as unknown as CourseUnit,
  im2Trig as unknown as CourseUnit,
  im2Circles as unknown as CourseUnit,
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

// ---------------------------------------------------------------------------
// Integrated Mathematics 3 — /math/integrated-3
// The final year of the integrated pathway (CCSS Integrated Mathematics III).
// IM1 was linear and exponential, IM2 quadratic; IM3 widens the function
// catalogue to polynomial, rational, radical, logarithmic and trigonometric,
// and closes with the inference half of statistics — the year that opens
// Precalculus.
// ---------------------------------------------------------------------------


const im3Units: CourseUnit[] = [
  im3Polynomials,
  im3Rational,
  im3ExpLog,
  im3Trig,
] as unknown as CourseUnit[];

export function getIm3Spine(): GeometrySpineEntry[] {
  return IM3_SPINE;
}

export function getIm3Unit(unitSlug: string): CourseUnit | null {
  return im3Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getIm3Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getIm3Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Algebra 2 course — /math/algebra-2
// The bridge between Algebra 1 and Precalculus: transformations and
// piecewise functions, quadratics with complex numbers, advanced systems,
// polynomial/radical/exponential-log/rational function families, and
// sequences & series. Interactive-graph heavy by design: parabolaGraph,
// polyGraph, expGraph, systemGraph, limitGraph, conicGraph, patternGrow,
// absoluteValue, evaluator, exponentBuilder, and coordinateGrid figures.
// ---------------------------------------------------------------------------


const alg2Units: CourseUnit[] = [
  a2Functions as unknown as CourseUnit,
  a2Quadratics as unknown as CourseUnit,
  a2Systems as unknown as CourseUnit,
  a2Polynomials as unknown as CourseUnit,
  a2Radicals as unknown as CourseUnit,
  a2ExpLogs as unknown as CourseUnit,
  a2Rationals as unknown as CourseUnit,
  a2Sequences as unknown as CourseUnit,
];

export function getAlg2Spine(): GeometrySpineEntry[] {
  return ALG2_SPINE;
}

export function getAlg2Unit(unitSlug: string): CourseUnit | null {
  return alg2Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getAlg2Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getAlg2Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Precalculus course — /math/precalculus
// The bridge to calculus, taught graph-first: function anatomy and
// transformations, polynomial and rational graphs, exponentials and
// logarithms, the unit circle, trig graphs and equations, and conic
// sections. Leans on the graph-widget family (parabolaGraph, polyGraph,
// limitGraph, expGraph, unitCircle, circleUnroll, conicGraph) plus
// coordinateGrid figures in nearly every lesson.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// Calculus course — /math/calculus
// The capstone of the topic ladder and the full ЭЕШ calculus scope: limits
// and continuity, the derivative and its rules (power, product, quotient,
// chain), curve analysis and optimization, then antiderivatives, the definite
// integral, the Fundamental Theorem, substitution, and integral applications
// (areas between curves, motion, average value). Leans on the limitGraph /
// tangentGraph / areaGraph widget family throughout.
// ---------------------------------------------------------------------------


const calcUnits: CourseUnit[] = [
  calLimits as unknown as CourseUnit,
  calDeriv as unknown as CourseUnit,
  calTech as unknown as CourseUnit,
  calDerivApps as unknown as CourseUnit,
  calIntegrals as unknown as CourseUnit,
  calIntApps as unknown as CourseUnit,
];

export function getCalcSpine(): GeometrySpineEntry[] {
  return CALC_SPINE;
}

export function getCalcUnit(unitSlug: string): CourseUnit | null {
  return calcUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getCalcLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getCalcUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Trigonometry course — /math/trigonometry
// The figure-first course: right-triangle ratios, the two special triangles,
// radians and the unit circle, the wave graphs, identities and equations,
// and the laws of sines and cosines. Full ЭЕШ trigonometry scope; leans on
// geo-diagram figures (GeoDiagram specs on teach/worked/tryIt/tapQuestion
// steps and practice problems) plus the trigRatios / specialTriangle /
// unitCircle / circleUnroll widget family.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// Solid Geometry course — /math/solid-geometry
// Geometry 2: stereometry for ЭЕШ. Lines & planes in space, the prism/pyramid/
// cylinder/cone/sphere families, cross-sections, similar-solid scaling, and
// the extract-the-flat-triangle exam strategy. Figure-dense by design: oblique
// wireframes with dashed hidden edges on the 3D views, true-shape extracted
// right triangles for every computation, plus the solid3d / solidNet /
// arcSector interactive widgets.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// IB Mathematics: Analysis & Approaches SL — /math/ib-sl
// The IB course lives in the IB hub (/practice/ib) but rides the same course
// machinery as the topic ladder. Units are the five official syllabus topics;
// lessons are the official subtopic codes (SL 1.1–1.9 etc.), taught to
// markscheme standard with formula-booklet flags. English-only by policy
// (exam realism), like the SAT hub.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// IB Mathematics: Analysis & Approaches HL — /math/ib-hl
// HL = the SL course PLUS the Additional Higher Level (AHL) extension codes.
// This course teaches ONLY the AHL codes — the shared SL foundation lives at
// /math/ib-sl and every HL unit's buildsOn points the student there first.
// Same English-only policy and markscheme discipline as SL.
// ---------------------------------------------------------------------------


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

// ---------------------------------------------------------------------------
// Course size — total lessons per performance context. The DENOMINATOR of the
// dashboard's per-course progress bar. Every authored lesson carries a
// tapQuestion (the LessonPlayer's first-attempt recorder), so this count is
// exactly the reachable maximum: a student who works every lesson hits 100%.
// Grades count published topics' lessons; named courses count live units'
// lessons. Returns null for non-course contexts (esh / sat / ib).
// ---------------------------------------------------------------------------

const GRADE_TOPIC_GETTERS: Record<number, () => GenMathTopic[]> = {
  6: getGrade6Topics,
  7: getGrade7Topics,
  8: getGrade8Topics,
  9: getGrade9Topics,
  10: getGrade10Topics,
  11: getGrade11Topics,
  12: getGrade12Topics,
};

const NAMED_COURSE_LESSON_SOURCES: Record<
  string,
  { spine: () => GeometrySpineEntry[]; unit: (slug: string) => CourseUnit | null }
> = {
  "course:geometry": { spine: getGeometrySpine, unit: getGeometryUnit },
  "course:prob-stats": { spine: getProbStatSpine, unit: getProbStatUnit },
  "course:vectors-matrices": { spine: getVecMatSpine, unit: getVecMatUnit },
  "course:algebra-1": { spine: getAlg1Spine, unit: getAlg1Unit },
  "course:integrated-1": { spine: getIm1Spine, unit: getIm1Unit },
  "course:integrated-2": { spine: getIm2Spine, unit: getIm2Unit },
  "course:integrated-3": { spine: getIm3Spine, unit: getIm3Unit },
  "course:algebra-2": { spine: getAlg2Spine, unit: getAlg2Unit },
  "course:precalculus": { spine: getPrecalcSpine, unit: getPrecalcUnit },
  "course:calculus": { spine: getCalcSpine, unit: getCalcUnit },
  "course:trigonometry": { spine: getTrigSpine, unit: getTrigUnit },
  "course:solid-geometry": { spine: getSolidGeoSpine, unit: getSolidGeoUnit },
  "course:ib-sl": { spine: getIbSlSpine, unit: getIbSlUnit },
  "course:ib-hl": { spine: getIbHlSpine, unit: getIbHlUnit },
};

/**
 * Lesson totals for EVERY course context, in one small map — computed
 * server-side (the dashboard's server page) so the client only receives
 * ~20 numbers instead of importing this registry and its corpus.
 */
export function allCourseLessonTotals(): Record<string, number> {
  const totals: Record<string, number> = {};
  for (const context of Object.keys(NAMED_COURSE_LESSON_SOURCES)) {
    const n = courseTotalLessons(context);
    if (n !== null) totals[context] = n;
  }
  for (const g of listGrades()) {
    const context = `course:grade-${g.grade}`;
    const n = courseTotalLessons(context);
    if (n !== null) totals[context] = n;
  }
  return totals;
}

export function courseTotalLessons(context: string): number | null {
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) {
    const getter = GRADE_TOPIC_GETTERS[Number(grade[1])];
    if (!getter) return null;
    return getter()
      .filter((t) => t.status !== "placeholder")
      .reduce((n, t) => n + t.lessons.length, 0);
  }
  const named = NAMED_COURSE_LESSON_SOURCES[context];
  if (named) {
    return named
      .spine()
      .filter((e) => e.live)
      .reduce((n, e) => n + (named.unit(e.slug)?.lessons.length ?? 0), 0);
  }
  return null;
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
