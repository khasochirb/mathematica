// ЭЕШ prep courses — the taught curriculum inside the ЭЕШ hub.
//
// Coverage goal, set by the owner: a student who completes these fourteen
// courses should be able to score 800/800 on any ЭЕШ paper. That target
// shapes two decisions that differ from the rest of the platform:
//
//   1. ENGLISH FIRST (owner decision, 2026-07-28, amending the hub-language
//      rule in memory/expansion-vision.md §4.7 for course content only).
//      Course content ships in English so it can be curated from the
//      existing sympy-verified catalog immediately; a Mongolian translation
//      pass comes later, over frozen content, through scripts/i18n. The
//      hub's tests, papers and chrome remain Mongolian.
//   2. EXAM-LEVEL PITCH. These courses assume a student already scoring
//      ~650/800. They deliberately do NOT start from arithmetic basics —
//      a student projecting 400–600 is routed to the General Math courses
//      first (components/esh/course/EshLevelAdvisor.tsx does the routing,
//      via the exam-study-map).
//
// Units are the SAME verified English units taught in the named /math
// courses and grade ladders — one source of truth, resolved through the
// registry in lib/genmath-lessons.ts — curated and re-ordered for the exam
// rather than for a school year. `source` records where each unit lives
// ("algebra-1/quadratic-equations", "11/logarithms"), which is provenance
// today and the work order for the translation pass later.

import {
  getAlg1Unit,
  getAlg2Unit,
  getCalcUnit,
  getGenMathTopic,
  getGeometryUnit,
  getProbStatUnit,
  getSolidGeoUnit,
  getTrigUnit,
  getVecMatUnit,
  type CourseUnit,
  type GenMathLesson,
  type GeometrySpineEntry,
} from "@/lib/genmath-lessons";
import type { CourseDef } from "@/components/course/CourseShell";

// The three ЭЕШ-authored units — the one exam topic with no source in the
// /math catalog. Built by scripts/esh/build_sets_logic.py; never hand-edited.
import eshSets from "@/data/genmath/esh/sets-and-operations.json";
import eshVenn from "@/data/genmath/esh/venn-diagrams-and-counting.json";
import eshIntervals from "@/data/genmath/esh/number-sets-and-intervals.json";

const ESH_AUTHORED: Record<string, CourseUnit> = {
  "sets-and-operations": eshSets as unknown as CourseUnit,
  "venn-diagrams-and-counting": eshVenn as unknown as CourseUnit,
  "number-sets-and-intervals": eshIntervals as unknown as CourseUnit,
};

// ---------------------------------------------------------------------------
// Source resolution — "course/slug" or "<grade>/slug" → the unit's data.
// ---------------------------------------------------------------------------

const NAMED_UNIT_GETTERS: Record<string, (slug: string) => CourseUnit | null> = {
  "algebra-1": getAlg1Unit,
  "algebra-2": getAlg2Unit,
  calculus: getCalcUnit,
  geometry: getGeometryUnit,
  "prob-stats": getProbStatUnit,
  "solid-geometry": getSolidGeoUnit,
  trigonometry: getTrigUnit,
  "vectors-matrices": getVecMatUnit,
};

function resolveSource(source: string): CourseUnit | null {
  const cut = source.indexOf("/");
  if (cut < 0) return null; // "authored" — content not written yet
  const home = source.slice(0, cut);
  const slug = source.slice(cut + 1);
  if (home === "esh") return ESH_AUTHORED[slug] ?? null;
  if (/^\d+$/.test(home)) {
    // Grade-ladder topic. GenMathTopic has no `unit` number; the caller
    // stamps the ЭЕШ position on top.
    const topic = getGenMathTopic(slug);
    return topic ? (topic as unknown as CourseUnit) : null;
  }
  const getter = NAMED_UNIT_GETTERS[home];
  return getter ? getter(slug) : null;
}

// ---------------------------------------------------------------------------
// The spine
// ---------------------------------------------------------------------------

export interface EshUnitEntry extends GeometrySpineEntry {
  /**
   * Where this unit's content lives — "algebra-1/quadratic-equations",
   * "11/logarithms" — or "authored" for a unit that still needs writing.
   * Provenance, and later the translation-pass work order.
   */
  source: string;
}

export interface EshTopicCourse {
  /** Canonical ЭЕШ topic key from lib/esh-questions (TOPICS). */
  topic: string;
  /** Course title shown in the hub and crumbs. English-first (see header). */
  title: string;
  /** One-paragraph intro on the topic page. */
  intro: string;
  units: EshUnitEntry[];
}

/**
 * Spine entry backed by a live unit. Title and blurb come from the unit's
 * own data so they can never drift from what the student opens. `buildsOn`
 * comes ONLY from this spine — the unit data's buildsOn references unit
 * numbers of its HOME course ("Factoring (Unit 7)"), which are wrong here.
 */
function live(unit: number, slug: string, source: string, buildsOn?: string): EshUnitEntry {
  const data = resolveSource(source);
  if (!data) throw new Error(`esh-course: source "${source}" did not resolve for "${slug}"`);
  return { unit, slug, title: data.title, blurb: data.blurb, buildsOn, live: true, source };
}


export const ESH_COURSES: EshTopicCourse[] = [
  {
    topic: "arithmetic",
    title: "Numbers & Arithmetic",
    intro:
      "The number system as the exam uses it: rational vs irrational, exponent laws, scientific notation, roots, and the percent problems (interest, markup, error) that appear on nearly every paper. Short by design — at this level you are sharpening, not learning to count.",
    units: [
      live(1, "the-real-number-system", "8/the-real-number-system"),
      live(2, "exponents-and-scientific-notation", "8/exponents-and-scientific-notation"),
      live(3, "roots", "8/roots"),
      live(4, "percent-applications", "7/percent-applications"),
    ],
  },
  {
    topic: "algebra",
    title: "Algebra",
    intro:
      "The heaviest-weighted topic on the exam. Equations and inequalities, systems, polynomial identities and factoring, quadratics by every method, rational expressions with their forbidden values, and radical manipulation — each unit feeds the next, so the order matters.",
    units: [
      live(1, "linear-equations", "algebra-1/linear-equations"),
      live(2, "inequalities", "algebra-1/inequalities"),
      live(3, "systems-of-equations", "algebra-1/systems-of-equations"),
      live(4, "polynomials-and-factoring", "algebra-1/polynomials-and-factoring"),
      live(5, "quadratic-equations", "algebra-1/quadratic-equations", "Factoring from Unit 4."),
      live(6, "rational-expressions", "10/rational-expressions"),
      live(7, "radicals-and-rational-exponents", "algebra-2/radicals-and-rational-exponents"),
      live(8, "systems-and-nonlinear-models", "algebra-2/systems-and-nonlinear-models"),
    ],
  },
  {
    topic: "set_theory",
    title: "Sets & Logic",
    intro:
      "Set operations, Venn counting, and interval notation — tested directly and used as the language of probability problems. Authored specifically for this course: nothing on the platform covered it before.",
    units: [
      live(1, "sets-and-operations", "esh/sets-and-operations"),
      live(2, "venn-diagrams-and-counting", "esh/venn-diagrams-and-counting",
        "Set operations and complements from Unit 1."),
      live(3, "number-sets-and-intervals", "esh/number-sets-and-intervals",
        "Set operations from Unit 1; the counting habits of Unit 2."),
    ],
  },
  {
    topic: "functions",
    title: "Functions",
    intro:
      "The backbone of the paper: domain and range, graphs, transformations, composition and inverses — then the full family tour from linear through quadratic, piecewise, polynomial and rational.",
    units: [
      live(1, "introduction-to-functions", "9/introduction-to-functions"),
      live(2, "linear-functions", "algebra-1/linear-functions"),
      live(3, "quadratic-functions", "10/quadratic-functions"),
      live(4, "piecewise-and-absolute-value-graphs", "9/piecewise-and-absolute-value-graphs"),
      live(5, "functions-and-transformations", "algebra-2/functions-and-transformations"),
      live(6, "polynomial-functions", "algebra-2/polynomial-functions"),
      live(7, "rational-functions", "algebra-2/rational-functions"),
    ],
  },
  {
    topic: "logarithms",
    title: "Exponentials & Logarithms",
    intro:
      "Two sides of one coin, and three recurring exam shapes: growth-and-decay models, equation solving, and expression manipulation with the log laws.",
    units: [
      live(1, "exponential-functions", "10/exponential-functions"),
      live(2, "logarithms", "11/logarithms"),
      live(3, "exponentials-and-logarithms", "algebra-2/exponentials-and-logarithms", "The log laws from Unit 2."),
    ],
  },
  {
    topic: "sequences",
    title: "Sequences & Series",
    intro:
      "Arithmetic and geometric progressions, their sums, and recursive definitions. The exam rarely hands you the formula — it hands you conditions and expects you to rebuild it.",
    units: [live(1, "sequences-and-series", "11/sequences-and-series")],
  },
  {
    topic: "trigonometry",
    title: "Trigonometry",
    intro:
      "From right-triangle ratios to the unit circle, exact values, graphs, identities, trig equations, and the sine and cosine rules — nearly every ЭЕШ trig question lives inside these six units.",
    units: [
      live(1, "right-triangle-trigonometry", "trigonometry/right-triangle-trigonometry"),
      live(2, "special-triangles-and-exact-values", "trigonometry/special-triangles-and-exact-values"),
      live(3, "radians-and-the-unit-circle", "trigonometry/radians-and-the-unit-circle"),
      live(4, "graphs-of-trig-functions", "trigonometry/graphs-of-trig-functions"),
      live(5, "identities-and-equations", "trigonometry/identities-and-equations"),
      live(6, "laws-of-sines-and-cosines", "trigonometry/laws-of-sines-and-cosines"),
    ],
  },
  {
    topic: "geometry",
    title: "Geometry",
    intro:
      "Plane geometry through solids: triangles and their centers, similarity, right-triangle trig, quadrilaterals, circles, areas, coordinate methods, and 3D measurement. Exam geometry chains two or three facts per problem — the order here builds those chains.",
    units: [
      live(1, "triangles-and-congruence", "geometry/triangles-and-congruence"),
      live(2, "relationships-in-triangles", "geometry/relationships-in-triangles"),
      live(3, "similarity", "geometry/similarity"),
      live(4, "right-triangles-and-trig", "geometry/right-triangles-and-trig"),
      live(5, "quadrilaterals-and-polygons", "geometry/quadrilaterals-and-polygons"),
      live(6, "circles", "geometry/circles"),
      live(7, "area-and-perimeter", "geometry/area-and-perimeter"),
      live(8, "coordinate-geometry", "geometry/coordinate-geometry"),
      live(9, "surface-area-and-volume", "geometry/surface-area-and-volume"),
      live(10, "lines-and-planes-in-space", "solid-geometry/lines-and-planes-in-space"),
      live(11, "cylinders-and-cones", "solid-geometry/cylinders-and-cones"),
      live(12, "spheres", "solid-geometry/spheres"),
    ],
  },
  {
    topic: "linear_algebra",
    title: "Vectors & Matrices",
    intro:
      "Vector arithmetic and coordinates, the dot product, 3D vectors, then matrix operations, determinants and inverses — the exam connects vectors to geometry and matrices to systems.",
    units: [
      live(1, "vector-arithmetic", "vectors-matrices/vector-arithmetic"),
      live(2, "vectors-and-coordinates", "vectors-matrices/vectors-and-coordinates"),
      live(3, "the-dot-product", "vectors-matrices/the-dot-product"),
      live(4, "vectors-in-space", "vectors-matrices/vectors-in-space"),
      live(5, "matrices-and-operations", "vectors-matrices/matrices-and-operations"),
      live(6, "determinants-and-inverses", "vectors-matrices/determinants-and-inverses"),
    ],
  },
  {
    topic: "complex_numbers",
    title: "Complex Numbers",
    intro:
      "Where a negative discriminant leads: arithmetic with i, conjugates and modulus, the complex plane, and the complete picture of quadratic roots.",
    units: [
      live(1, "complex-numbers", "11/complex-numbers"),
      live(2, "quadratics-and-complex-numbers", "algebra-2/quadratics-and-complex-numbers"),
    ],
  },
  {
    topic: "combinatorics",
    title: "Combinatorics",
    intro:
      "The art of counting: multiplication and addition principles, permutations, combinations, and the binomial theorem. Half of the probability section is secretly this topic.",
    units: [
      live(1, "counting-principles", "prob-stats/counting-principles"),
      live(2, "permutations", "prob-stats/permutations"),
      live(3, "combinations", "prob-stats/combinations"),
      live(4, "binomial-theorem", "prob-stats/binomial-theorem", "Combinations from Unit 3."),
    ],
  },
  {
    topic: "probability",
    title: "Probability",
    intro:
      "Probability models, conditional probability, random variables with expectation and variance, and the binomial distribution — in the order the exam escalates them.",
    units: [
      live(1, "probability-models", "prob-stats/probability-models"),
      live(2, "conditional-probability", "prob-stats/conditional-probability"),
      live(3, "random-variables", "prob-stats/random-variables"),
      live(4, "binomial-distribution", "prob-stats/binomial-distribution"),
    ],
  },
  {
    topic: "statistics",
    title: "Statistics",
    intro:
      "Describing data, position and distribution (z-scores, the normal curve), two-variable data with regression, and inference — ЭЕШ statistics rewards interpretation over computation.",
    units: [
      live(1, "describing-data", "prob-stats/describing-data"),
      live(2, "distributions-and-position", "prob-stats/distributions-and-position"),
      live(3, "two-variable-data", "prob-stats/two-variable-data"),
      live(4, "inference-and-studies", "prob-stats/inference-and-studies"),
    ],
  },
  {
    topic: "calculus",
    title: "Calculus",
    intro:
      "Limits, the derivative and its techniques, applications (monotonicity, extrema, optimization), then integrals and their applications — ЭЕШ analysis questions concentrate on derivative applications, so that unit deserves the most repetitions.",
    units: [
      live(1, "limits-and-continuity", "calculus/limits-and-continuity"),
      live(2, "the-derivative", "calculus/the-derivative"),
      live(3, "differentiation-techniques", "calculus/differentiation-techniques"),
      live(4, "applications-of-derivatives", "calculus/applications-of-derivatives"),
      live(5, "integrals", "calculus/integrals"),
      live(6, "applications-of-integrals", "calculus/applications-of-integrals"),
    ],
  },
];

// ---------------------------------------------------------------------------
// Lookups
// ---------------------------------------------------------------------------

export const ESH_COURSE_CONTEXT = "course:esh";

/** Below this projected score, the advisor routes to General Math first. */
export const ESH_COURSE_READY_SCORE = 650;

export function getEshTopicCourse(topic: string): EshTopicCourse | null {
  return ESH_COURSES.find((c) => c.topic === topic) ?? null;
}

export function getEshUnit(topic: string, unitSlug: string): CourseUnit | null {
  const course = getEshTopicCourse(topic);
  if (!course) return null;
  const entry = course.units.find((u) => u.slug === unitSlug);
  if (!entry || !entry.live) return null;
  const data = resolveSource(entry.source);
  if (!data) return null;
  // Stamp the ЭЕШ position and REPLACE buildsOn: the data's buildsOn names
  // unit numbers of its home course, which would be wrong on this spine.
  return { ...data, unit: entry.unit, buildsOn: entry.buildsOn };
}

export function getEshLesson(
  topic: string,
  unitSlug: string,
  lessonSlug: string,
): GenMathLesson | null {
  const unit = getEshUnit(topic, unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

/** How many units of this topic a student can actually open today. */
export function liveUnitCount(topic: string): number {
  return getEshTopicCourse(topic)?.units.filter((u) => u.live).length ?? 0;
}

export function totalUnitCount(topic: string): number {
  return getEshTopicCourse(topic)?.units.length ?? 0;
}

/**
 * The topic's course rendered through the shared CourseShell. English chrome
 * (the shell's default) to match the English content — see the header note.
 */
export function eshCourseDef(topic: string): CourseDef | null {
  const course = getEshTopicCourse(topic);
  if (!course) return null;
  return {
    slug: topic,
    title: course.title,
    context: ESH_COURSE_CONTEXT,
    intro: course.intro,
    basePath: `/practice/esh/learn/${topic}`,
    rootHref: "/practice/esh/learn",
    // The ratings-driven plan reads /math course contexts; ЭЕШ course
    // attempts land under a single context, so the per-unit plan would be
    // misleading here until ratings are namespaced per topic.
    personalize: false,
    spine: () => course.units,
    unit: (unitSlug) => getEshUnit(topic, unitSlug),
    lesson: (unitSlug, lessonSlug) => getEshLesson(topic, unitSlug, lessonSlug),
  };
}
