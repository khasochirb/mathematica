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

export const GRADE7_SPINE: GradeSpineEntry[] = [
  {
    slug: "proportional-relationships",
    title: "Proportional Relationships",
    blurb: "Unit rates with fractions, the constant of proportionality, y = kx, and reading proportionality from tables and graphs.",
    live: true,
  },
  {
    slug: "rational-number-operations",
    title: "Rational Number Operations",
    blurb: "Adding, subtracting, multiplying, and dividing with negatives — integers, fractions, and decimals, all four operations, one number line.",
    live: true,
  },
  {
    slug: "equations-and-inequalities",
    title: "Equations & Inequalities",
    blurb: "Simplifying expressions with negatives, two-step equations, and inequalities — including the flip when you multiply by a negative.",
    live: true,
  },
  {
    slug: "percent-applications",
    title: "Percent Applications",
    blurb: "Percent change, discounts, markups, tax, tips, simple interest, and percent error — the percents that show up on receipts.",
    live: true,
  },
  {
    slug: "geometry-scale-and-circles",
    title: "Geometry: Scale, Angles & Circles",
    blurb: "Scale drawings, angle relationships, the triangle inequality, and circles — where \u03c0 finally earns its name.",
    live: true,
  },
  {
    slug: "probability",
    title: "Probability",
    blurb: "Chance from 0 to 1: sample spaces, theoretical vs experimental probability, and simple compound events.",
    live: true,
  },
  {
    slug: "sampling-and-statistics",
    title: "Sampling & Statistics",
    blurb: "Random samples, inference about a population, and comparing two data sets with center and spread.",
    live: true,
  },
];

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

export const GRADE9_SPINE: GradeSpineEntry[] = [
  {
    slug: "equations-and-formulas",
    title: "Equations & Formulas",
    blurb: "Multi-step equations with variables on both sides, special cases, and literal equations — solving formulas for any letter.",
    live: true,
  },
  {
    slug: "inequalities-and-absolute-value",
    title: "Inequalities & Absolute Value",
    blurb: "Compound inequalities (and/or), absolute-value equations, and absolute-value inequalities — distances on the number line.",
    live: true,
  },
  {
    slug: "introduction-to-functions",
    title: "Introduction to Functions",
    blurb: "Function notation, domain and range, the vertical line test, and reading graphs qualitatively.",
    live: true,
  },
  {
    slug: "linear-models-and-variation",
    title: "Linear Models & Variation",
    blurb: "Writing linear models from context, direct variation revisited, and inverse variation \u2014 y = k/x, the other proportionality.",
    live: true,
  },
  {
    slug: "inequalities-in-two-variables",
    title: "Systems of Inequalities",
    blurb: "Graphing two-variable inequalities, shading half-planes, and systems of inequalities as feasible regions.",
    live: true,
  },
  {
    slug: "piecewise-and-absolute-value-graphs",
    title: "Piecewise & Absolute-Value Graphs",
    blurb: "The V of y = |x|, shifts of it, and functions defined in pieces \u2014 including step functions.",
    live: true,
  },
  {
    slug: "data-distributions",
    title: "Data Distributions",
    blurb: "Histograms, box plots, quartiles and IQR \u2014 the shape of data and how to compare distributions.",
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
    live: true,
  },
  {
    slug: "trigonometry-and-the-unit-circle",
    title: "Trigonometry & the Unit Circle",
    blurb: "Radians, the unit circle, sine and cosine as coordinates, and the waves they draw.",
    live: true,
  },
  {
    slug: "complex-numbers",
    title: "Complex Numbers",
    blurb: "The number i, arithmetic with a + bi, conjugates and division, and quadratics whose roots finally all exist.",
    live: true,
  },
  {
    slug: "statistics-and-data",
    title: "Statistics & Data",
    blurb: "Mean vs median, standard deviation, z-scores, and the normal curve that grades on it.",
    live: true,
  },
];

export const GRADE12_SPINE: GradeSpineEntry[] = [
  {
    slug: "trigonometric-identities",
    title: "Trigonometric Identities",
    blurb: "The Pythagorean identity, sum and double-angle formulas, proving identities, and solving trig equations.",
    live: true,
  },
  {
    slug: "limits-and-continuity",
    title: "Limits & Continuity",
    blurb: "What a function approaches: reading limits from graphs, computing them with algebra, and where functions break.",
    live: true,
  },
  {
    slug: "derivatives",
    title: "Derivatives",
    blurb: "The slope of a curve: the derivative as a limit, and the power, product, quotient, and chain rules.",
    live: true,
  },
  {
    slug: "applications-of-derivatives",
    title: "Applications of Derivatives",
    blurb: "Tangent lines, increasing and decreasing, maxima and minima, and optimization problems that pay.",
    live: true,
  },
  {
    slug: "integrals",
    title: "Integrals",
    blurb: "Undoing the derivative: antiderivatives, the area under a curve, and the Fundamental Theorem of Calculus.",
    live: true,
  },
  {
    slug: "vectors",
    title: "Vectors",
    blurb: "Magnitude and direction: components, addition, scalar multiples, the dot product, and the angle between.",
    live: true,
  },
  {
    slug: "conic-sections",
    title: "Conic Sections",
    blurb: "Circles, ellipses, parabolas, and hyperbolas — the four curves hiding in a sliced cone.",
    live: true,
  },
];

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

const ALL_GRADES: GradeInfo[] = [
  { grade: 6, active: true },
  { grade: 7, active: true },
  { grade: 8, active: true },
  { grade: 9, active: true },
  { grade: 10, active: true },
  { grade: 11, active: true },
  { grade: 12, active: true },
];

export function listGrades(): GradeInfo[] {
  return ALL_GRADES;
}

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
// Combinatorics, Probability & Statistics — the second standalone course.
// Same architecture as Geometry: one near-linear spine in three acts
// (count → chance → data), same lesson schema, same verify:genmath gate.
// Units reuse the GeometryUnit shape (unit number + buildsOn, no grade).
// ---------------------------------------------------------------------------

export type CourseUnit = GeometryUnit;

export const PROBSTAT_SPINE: GeometrySpineEntry[] = [
  {
    unit: 1,
    slug: "counting-principles",
    title: "Counting Principles",
    blurb: "The multiplication and addition principles, complementary counting, and organized lists — how to count without counting.",
    buildsOn: "Nothing — the course starts here, from zero.",
    live: true,
  },
  {
    unit: 2,
    slug: "permutations",
    title: "Permutations & Arrangements",
    blurb: "Factorials, arrangements of all or some objects, repeated letters, and seating with restrictions.",
    buildsOn: "The multiplication principle from Unit 1.",
    live: true,
  },
  {
    unit: 3,
    slug: "combinations",
    title: "Combinations",
    blurb: "Choosing without order: nCr, committees, at-least and at-most counts, and when order matters vs when it doesn't.",
    buildsOn: "Permutations (Unit 2) — combinations are permutations with the order divided out.",
    live: true,
  },
  {
    unit: 4,
    slug: "binomial-theorem",
    title: "Pascal's Triangle & the Binomial Theorem",
    blurb: "The triangle that counts everything: binomial coefficients, expanding powers, and finding specific terms.",
    buildsOn: "Combinations (Unit 3) — Pascal's triangle IS nCr in disguise.",
    live: true,
  },
  {
    unit: 5,
    slug: "probability-models",
    title: "Probability Models",
    blurb: "Sample spaces, events, equally-likely outcomes, complements, and the addition rule with Venn diagrams.",
    buildsOn: "Counting (Units 1–3) — probability is counting favorable over counting all.",
    live: true,
  },
  {
    unit: 6,
    slug: "conditional-probability",
    title: "Conditional Probability & Independence",
    blurb: "How information changes chance: P(A|B), the multiplication rule, independence, weighted trees, and Bayes by table.",
    buildsOn: "Probability models from Unit 5.",
    live: true,
  },
  {
    unit: 7,
    slug: "random-variables",
    title: "Random Variables & Expected Value",
    blurb: "Turning outcomes into numbers: probability distributions, expected value, variance, and what makes a game fair.",
    buildsOn: "Units 5–6 — distributions are probability models wearing numbers.",
    live: true,
  },
  {
    unit: 8,
    slug: "binomial-distribution",
    title: "The Binomial Distribution",
    blurb: "Repeated independent trials: binomial probabilities, expected count np, shape, and simulation.",
    buildsOn: "Combinations (Unit 3) and random variables (Unit 7) — the course's two halves meet here.",
    live: true,
  },
  {
    unit: 9,
    slug: "describing-data",
    title: "Describing Data",
    blurb: "Center and spread done right: mean, median, IQR, standard deviation, boxplots, and the 1.5×IQR outlier fence.",
    buildsOn: "Expected value (Unit 7) — the mean of data is expectation seen from below.",
    live: true,
  },
  {
    unit: 10,
    slug: "distributions-and-position",
    title: "Distribution Shape & Position",
    blurb: "Histograms and shape, percentiles, z-scores, and the normal curve with the 68–95–99.7 rule.",
    buildsOn: "Center and spread from Unit 9.",
    live: false,
  },
  {
    unit: 11,
    slug: "two-variable-data",
    title: "Two-Variable Data",
    blurb: "Scatterplots, the correlation coefficient, the least-squares line, and why correlation is not causation.",
    buildsOn: "One-variable tools from Units 9–10.",
    live: false,
  },
  {
    unit: 12,
    slug: "inference-and-studies",
    title: "Sampling, Studies & Inference",
    blurb: "Random sampling, bias, experiments vs observation, simulation-based inference, and margin of error — the capstone.",
    buildsOn: "Everything — probability (Units 5–8) judges what data (Units 9–11) shows.",
    live: false,
  },
];

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
