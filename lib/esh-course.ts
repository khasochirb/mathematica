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
// STRUCTURE ANSWERS TO THE MINISTRY. Mongolia's Ministry of Education
// publishes the grade 10-12 mathematics standard as order А/492 (2019-08-01,
// third appendix), and it numbers every learning objective — `10.5б`,
// `11.9ж`, `12.4и`. That numbering is the spine a Mongolian teacher, parent
// or student already knows, so every unit below records the objectives it
// teaches (MOE_COVERAGE) and lib/esh-course.test.ts fails if a CORE
// objective has no unit behind it. The syllabus itself is checked in at
// data/esh/moe-curriculum.json, parsed from the ministry PDF (archived
// beside it) by scripts/esh/parse_moe_curriculum.py — so the claim "we
// cover the national curriculum" is a test, not a slogan.
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
import { ESH_DOMAINS, type EshDomain } from "@/lib/esh-questions";

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

/**
 * Shared with the other hub-owned curated courses (lib/sat-course.ts): the
 * same "home/slug" provenance strings resolve against the same catalog.
 */
export function resolveCatalogSource(source: string): CourseUnit | null {
  return resolveSource(source);
}

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
  /**
   * The Mongolian name, taken from the ministry's own section headings in
   * data/esh/moe-curriculum.json wherever one exists — so the hub reads in
   * the words a Mongolian student has already met in class, not a fresh
   * translation of our English. `moeSections` names the headings it came
   * from, which is also the reader's route back into the standard.
   */
  titleMn: string;
  /** Ministry section codes this course answers to, e.g. ["10.5", "11.1"]. */
  moeSections: string[];
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



// -------------------------------------------------------------------------
// Ministry coverage — which objectives each unit teaches
// -------------------------------------------------------------------------

/**
 * Unit slug -> the МОЭ objective codes (data/esh/moe-curriculum.json) that
 * unit teaches. Codes are the ministry's own: <grade>.<section><letter>.
 * A unit may legitimately claim codes from several grades — the exam does
 * not respect year boundaries and neither do these courses — and one code
 * may be claimed by more than one unit where two courses genuinely share
 * it (the sine rule is taught in Trigonometry and used in Geometry).
 *
 * An EMPTY array is a deliberate statement: the unit is here for the exam,
 * not for the ministry's list. Percent applications, congruence proofs and
 * study design are all tested on ЭЕШ papers without appearing as a grade
 * 10-12 objective, because the ministry places them earlier.
 */
export const MOE_COVERAGE: Record<string, string[]> = {
  // --- arithmetic ------------------------------------------------
  "the-real-number-system": ["10.1г"],
  "exponents-and-scientific-notation": ["10.1а", "10.1б", "10.1в"],
  "roots": ["10.2а"],
  "percent-applications": [],
  // --- algebra ---------------------------------------------------
  "linear-equations": ["10.5а"],
  "inequalities": ["10.5а", "10.5г", "11.1б", "11.1в", "12.1а"],
  "systems-of-equations": ["10.5ж", "11.2б"],
  "polynomials-and-factoring": ["10.2б", "10.2д", "12.2а", "12.2б", "12.2в"],
  "quadratic-equations": ["10.5б", "10.5в", "10.5е", "11.1а", "11.1г"],
  "rational-expressions": ["10.2в", "10.2г", "12.2г", "12.2д", "12.2е"],
  "radicals-and-rational-exponents": ["10.2а"],
  "systems-and-nonlinear-models": ["11.2а", "11.2б"],
  // --- sets & logic ----------------------------------------------
  "sets-and-operations": ["10.6б"],
  "venn-diagrams-and-counting": ["10.6в", "10.6г"],
  "number-sets-and-intervals": ["10.6а"],
  // --- functions -------------------------------------------------
  "introduction-to-functions": ["10.3а", "11.3а", "11.3в", "11.3г", "11.3ж", "11.3з"],
  "linear-functions": ["10.8в", "10.8г"],
  "quadratic-functions": ["10.3б"],
  "piecewise-and-absolute-value-graphs": ["12.3е"],
  "functions-and-transformations": ["11.3д", "11.3е", "11.3и", "11.3к"],
  "polynomial-functions": ["10.3в", "11.3б"],
  "rational-functions": ["12.3г"],
  // --- exponentials & logarithms ---------------------------------
  "exponential-functions": ["10.3г", "10.3е", "10.5д"],
  "logarithms": ["12.3а", "12.3б"],
  "exponentials-and-logarithms": ["12.3в"],
  // --- sequences & series ----------------------------------------
  "sequences-and-series": [
    "11.4а", "11.4б", "11.4в", "11.4ж", "11.4з", "11.4и", "12.9а", "12.9б", "12.9в", "12.9г",
    "12.9д",
  ],
  // --- trigonometry ----------------------------------------------
  "right-triangle-trigonometry": ["10.10а"],
  "special-triangles-and-exact-values": ["11.7б"],
  "radians-and-the-unit-circle": ["11.6а", "11.6б", "11.7а", "12.3д"],
  "graphs-of-trig-functions": ["11.7г", "12.6а"],
  "identities-and-equations": ["11.7в", "11.7д", "11.7е", "12.6б", "12.6в", "12.6г"],
  "laws-of-sines-and-cosines": ["10.10б", "10.10в"],
  // --- geometry --------------------------------------------------
  "triangles-and-congruence": [],
  "relationships-in-triangles": ["10.7г"],
  "similarity": [],
  "right-triangles-and-trig": ["10.10г"],
  "quadrilaterals-and-polygons": ["10.7в"],
  "circles": ["10.7а", "10.7б", "10.8д"],
  "area-and-perimeter": ["10.12а"],
  "coordinate-geometry": ["10.8а", "10.8б", "11.5а", "11.5б"],
  "surface-area-and-volume": ["10.12б"],
  "lines-and-planes-in-space": ["10.12в", "11.5в", "11.5г"],
  "cylinders-and-cones": ["10.12б"],
  "spheres": ["10.12б"],
  // --- vectors & matrices ----------------------------------------
  "vector-arithmetic": ["10.9а", "10.9б"],
  "vectors-and-coordinates": ["10.9в", "10.9г", "11.5д"],
  "the-dot-product": ["10.9д", "10.9е"],
  "vectors-in-space": ["11.8а", "11.8б", "11.8в", "11.8г", "11.8д", "11.8е"],
  "matrices-and-operations": ["10.4а", "10.4б", "10.4в", "10.4г"],
  "determinants-and-inverses": ["10.4д", "10.4е", "11.2в"],
  "transformation-matrices": [
    "10.11а", "10.11б", "10.11в", "10.11г", "10.11д", "10.11е", "10.11ж",
  ],
  "systems-in-three-unknowns": ["11.2г", "11.2д", "11.2е"],
  // --- complex numbers -------------------------------------------
  "complex-numbers": ["12.4а", "12.4б", "12.4в", "12.4г", "12.4д"],
  "quadratics-and-complex-numbers": ["12.4г"],
  // --- combinatorics ---------------------------------------------
  "counting-principles": ["10.6в", "10.6г", "10.14а", "12.14а"],
  "permutations": ["10.14б", "11.12а", "11.12б"],
  "combinations": ["10.14б", "11.13а", "12.14б"],
  "binomial-theorem": ["11.4г", "11.4д", "11.4е", "12.9ж"],
  // --- probability -----------------------------------------------
  "probability-models": ["10.15а", "10.15б", "12.15а"],
  "conditional-probability": ["11.13б", "11.13в", "11.13г", "11.13д", "12.15а"],
  "random-variables": ["12.12а", "12.12б"],
  "binomial-distribution": ["12.12в", "12.12г"],
  // --- statistics ------------------------------------------------
  "describing-data": [
    "10.13а", "10.13б", "10.13г", "10.13д", "10.13е", "11.11а", "11.11б", "11.11в", "11.11г",
    "11.11д",
  ],
  "distributions-and-position": ["12.13а", "12.13б", "12.13в"],
  "two-variable-data": ["10.13в"],
  "inference-and-studies": [],
  // --- calculus --------------------------------------------------
  "limits-and-continuity": ["10.3д", "11.9а"],
  "the-derivative": ["11.9б", "11.9в", "11.9г", "11.9е"],
  "differentiation-techniques": ["11.9д", "12.7а", "12.7б", "12.7в", "12.7г"],
  "applications-of-derivatives": [
    "11.9ж", "11.9з", "11.9и", "11.9к", "11.9л", "11.9м", "11.9н",
  ],
  "integrals": [
    "11.10а", "11.10б", "11.10в", "11.10г", "11.10е", "12.8а", "12.8б", "12.8в", "12.8г",
    "12.8д", "12.8е",
  ],
  "applications-of-integrals": ["11.10д", "11.10ж", "11.10з", "11.10и", "11.10к", "12.8ж"],
};

/**
 * Ministry objectives NO unit teaches yet, with the reason. This list is
 * asserted EXACTLY by lib/esh-course.test.ts: a code may only sit here
 * deliberately, and the moment a unit claims it the test demands it be
 * removed. Silence about a gap is the thing the list exists to prevent.
 *
 * EVERY remaining entry is elective (сонгон судлах, starred in the
 * ministry's own text), which the ЭЕШ paper reaches for far less often.
 * The core list is empty, and lib/esh-course.test.ts asserts that: the last
 * six core gaps — section 10.11 (transformations as matrices) and 11.2г
 * (Gauss's method) — were closed on 2026-08-12 by Vectors & Matrices units
 * 7 and 8. A core objective may not silently reappear here.
 */
export const MOE_NOT_YET_COVERED: { code: string; why: string }[] = [
  // --- elective (сонгон судлах) --------------------------------------
  { code: "12.3ж", why: "Parametric equations and their graphs." },
  { code: "12.3з", why: "Curves and their equations, sketched from the equation." },
  { code: "12.4е", why: "Polar and exponential form r(cos θ + i sin θ) = re^{iθ}." },
  { code: "12.4ж", why: "Square roots of a complex number, and why there are two." },
  { code: "12.4з", why: "The geometric meaning of complex arithmetic and conjugation." },
  { code: "12.4и", why: "Loci in the complex plane: |z - a| < k, |z - a| = |z - b|, arg(z - a) = α." },
  { code: "12.5а", why: "Огторгуйн шулуун — the vector equation of a line in space. Geometry Unit 10 does lines and planes synthetically; the vector/Cartesian treatment the ministry asks for is missing." },
  { code: "12.5б", why: "Two lines in space: parallel, intersecting or skew (солбисон)." },
  { code: "12.5в", why: "The angle between two lines in space, and their point of intersection." },
  { code: "12.5г", why: "The equation of a plane, ax + by + cz = d and in vector form." },
  { code: "12.5д", why: "Distances and angles between points, lines and planes in space." },
  { code: "12.9е", why: "Ялгаврын арга — summing a series by the method of differences." },
  { code: "12.10а", why: "Математик индукц — proof by mathematical induction. Nothing on the platform teaches it." },
  { code: "12.11а", why: "Дифференциал тэгшитгэл — setting up a differential equation from a situation." },
  { code: "12.11б", why: "Separable first-order differential equations, general solution." },
  { code: "12.11в", why: "Using an initial condition to find the particular solution." },
  { code: "12.11г", why: "Interpreting the solution of a differential equation in context." },
  { code: "12.15б", why: "Геометр магадлал — geometric probability." },
];

export const ESH_COURSES: EshTopicCourse[] = [
  {
    topic: "arithmetic",
    title: "Numbers & Arithmetic",
    titleMn: "Тоо ба үсэгт илэрхийлэл",
    moeSections: ["10.1", "10.2"],
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
    titleMn: "Тэгшитгэл, тэнцэтгэл биш",
    moeSections: ["10.2", "10.5", "11.1", "11.2", "12.1", "12.2"],
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
    titleMn: "Олонлог",
    moeSections: ["10.6"],
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
    titleMn: "Функц ба график",
    moeSections: ["10.3", "11.3", "12.3"],
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
    titleMn: "Илтгэгч ба логарифм функц",
    moeSections: ["10.3", "12.3"],
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
    titleMn: "Дараалал, цуваа",
    moeSections: ["11.4", "12.9"],
    intro:
      "Arithmetic and geometric progressions, their sums, and recursive definitions. The exam rarely hands you the formula — it hands you conditions and expects you to rebuild it.",
    units: [live(1, "sequences-and-series", "11/sequences-and-series")],
  },
  {
    topic: "trigonometry",
    title: "Trigonometry",
    titleMn: "Тригонометр",
    moeSections: ["10.10", "11.6", "11.7", "12.6"],
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
    titleMn: "Геометр ба хэмжигдэхүүн",
    moeSections: ["10.7", "10.8", "10.12", "11.5"],
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
    titleMn: "Вектор ба матриц",
    moeSections: ["10.4", "10.9", "10.11", "11.2", "11.8"],
    intro:
      "Vector arithmetic and coordinates, the dot product, 3D vectors, then matrix operations, determinants and inverses, geometric transformations as matrices, and systems in three unknowns — the exam connects vectors to geometry and matrices to systems.",
    units: [
      live(1, "vector-arithmetic", "vectors-matrices/vector-arithmetic"),
      live(2, "vectors-and-coordinates", "vectors-matrices/vectors-and-coordinates"),
      live(3, "the-dot-product", "vectors-matrices/the-dot-product"),
      live(4, "vectors-in-space", "vectors-matrices/vectors-in-space"),
      live(5, "matrices-and-operations", "vectors-matrices/matrices-and-operations"),
      live(6, "determinants-and-inverses", "vectors-matrices/determinants-and-inverses"),
      live(7, "transformation-matrices", "vectors-matrices/transformation-matrices"),
      live(8, "systems-in-three-unknowns", "vectors-matrices/systems-in-three-unknowns"),
    ],
  },
  {
    topic: "complex_numbers",
    title: "Complex Numbers",
    titleMn: "Комплекс тоо",
    moeSections: ["12.4"],
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
    titleMn: "Комбинаторик",
    moeSections: ["10.14", "11.12", "12.14"],
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
    titleMn: "Магадлал",
    moeSections: ["10.15", "11.13", "12.12", "12.15"],
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
    titleMn: "Өгөгдлийн шинжилгээ",
    moeSections: ["10.13", "11.11", "12.13"],
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
    titleMn: "Анализын эхлэл",
    moeSections: ["11.9", "11.10", "12.7", "12.8"],
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

/**
 * The learn hub's shape: five MAIN topics (the ministry's strands, defined
 * in lib/esh-questions ESH_DOMAINS), each carrying its subtopic courses in
 * the domain's own display order. Derived rather than stored, so the course
 * list and the question taxonomy can never disagree about where a topic
 * lives — lib/esh-course.test.ts asserts the derivation is total (every
 * course reachable, every domain non-empty).
 */
export function eshCoursesByDomain(): { domain: EshDomain; courses: EshTopicCourse[] }[] {
  return ESH_DOMAINS.map((domain) => ({
    domain,
    courses: domain.topics
      .map((t) => getEshTopicCourse(t))
      .filter((c): c is EshTopicCourse => c !== null),
  }));
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
