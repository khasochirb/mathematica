// SAT Math course — the taught curriculum inside the SAT hub.
//
// STRUCTURE IS THE COLLEGE BOARD'S, EXACTLY. Four domain courses, and inside
// each one the Board's own published subtopics, in the Board's own order and
// under the Board's own names. A student holding the official topic outline
// can read it straight down this hub, line for line.
//
//   Algebra                              5 subtopics   13–15 of the 44 questions
//   Advanced Math                        4 subtopics   13–15
//   Problem-Solving & Data Analysis      7 subtopics    5–7
//   Geometry & Trigonometry              4 subtopics    5–7
//
// Until 2026-08 these four domains held units CURATED from the school catalog
// — "algebra-1/linear-equations", "geometry/circles" and so on. The
// mathematics was right and sympy-verified, but the unit boundaries were a
// school year's, not the exam's, so the hub could not be lined up against the
// Board's list. The units now come from data/genmath/sat/, written for this
// exam: one unit per subtopic, SAT register, traps named, Desmos routes given
// where they beat algebra.
//
// Subtopic slugs are globally unique, so `resolveSatSource` is a flat lookup
// and the domain grouping below is the only place order and weighting live.
//
// English content is exam-realism policy in this hub
// (memory/expansion-vision.md §4.7), not a stopgap.

import { resolveCatalogSource, type EshUnitEntry as SatUnitEntry } from "@/lib/esh-course";
import { getSatNativeUnit } from "@/lib/genmath-data/sat";
import type { CourseUnit, GenMathLesson } from "@/lib/genmath-lessons";
import type { CourseDef } from "@/components/course/CourseShell";

export type { SatUnitEntry };

export interface SatDomainCourse {
  /** Domain slug — equals the SAT bank's unit id (lib/problem-bank sat). */
  domain: string;
  /** The College Board's name for the domain. */
  title: string;
  /** How many of the 44 Math questions this domain carries. */
  weight: string;
  intro: string;
  units: SatUnitEntry[];
}

/**
 * "sat/<subtopic>" resolves against the SAT-native corpus; anything else falls
 * through to the shared school catalog, so a subtopic can still be backed by a
 * curated unit while its native version is being written.
 */
function resolveSatSource(source: string): CourseUnit | null {
  if (source.startsWith("sat/")) return getSatNativeUnit(source.slice(4));
  return resolveCatalogSource(source);
}

/** A subtopic whose unit is written and open. Title and blurb come from the
 *  unit's own data, so the hub can never describe something the student does
 *  not then open. */
function live(unit: number, slug: string, buildsOn?: string): SatUnitEntry {
  const source = `sat/${slug}`;
  const data = resolveSatSource(source);
  if (!data) throw new Error(`sat-course: source "${source}" did not resolve`);
  return { unit, slug, title: data.title, blurb: data.blurb, buildsOn, live: true, source };
}

/** A subtopic on the official list whose unit is not written yet. It is listed
 *  — the Board's structure is the point, and a student should see the whole
 *  map — but it does not link anywhere. */
function planned(unit: number, slug: string, title: string, blurb: string): SatUnitEntry {
  return { unit, slug, title, blurb, live: false, source: "authored" };
}

export const SAT_COURSES: SatDomainCourse[] = [
  {
    domain: "algebra",
    title: "Algebra",
    weight: "13–15 questions",
    intro:
      "The largest domain on the test, and the one everything else leans on. Linear equations in one and two variables, linear functions, systems, and inequalities — five official skills that between them carry about a third of the Math section.",
    units: [
      live(1, "linear-equations-one-variable"),
      live(2, "linear-equations-two-variables", "Solving in one variable — every method in Unit 2 ends with one of those."),
      live(3, "linear-functions", "Slope and intercepts from Unit 2, now in function notation."),
      live(4, "systems-of-linear-equations", "Units 1 and 2 — a system is two lines and one crossing."),
      live(5, "linear-inequalities", "Units 1 and 2 — an inequality is a line plus a side of it."),
    ],
  },
  {
    domain: "advanced-math",
    title: "Advanced Math",
    weight: "13–15 questions",
    intro:
      "Everything nonlinear, and the same share of the test as Algebra. Rewriting expressions into equivalent forms, solving nonlinear equations, systems where a line meets a curve, and the quadratic, exponential, polynomial and rational functions behind them.",
    units: [
      live(1, "equivalent-expressions"),
      live(2, "nonlinear-equations-one-variable", "Factoring from Unit 1 — every quadratic route starts there."),
      live(3, "systems-nonlinear-two-variables", "Quadratics from Unit 2, and linear systems from the Algebra course."),
      live(4, "nonlinear-functions", "Quadratics from Unit 2 and the equivalent forms of Unit 1."),
    ],
  },
  {
    domain: "problem-solving-data",
    title: "Problem-Solving and Data Analysis",
    weight: "5–7 questions",
    intro:
      "The quantitative-reasoning sixth of the paper, and the widest set of skills per question. Ratios and units, percentages, one- and two-variable data, probability, margins of error, and the study-design questions almost nobody revises.",
    units: [
      planned(
        1,
        "ratios-rates-proportions-units",
        "Ratios, Rates, Proportional Relationships and Units",
        "Scaling a ratio, reading a rate, converting units in one chain, and the proportional relationships that pass through the origin.",
      ),
      planned(
        2,
        "percentages",
        "Percentages",
        "Percent of, percent change, successive changes that do not add, and working backwards from a discounted price to the original.",
      ),
      planned(
        3,
        "one-variable-data",
        "One-Variable Data: Distributions and Measures of Center and Spread",
        "Mean and median and when they part company, range and standard deviation compared without computing either, and what an outlier does to each.",
      ),
      planned(
        4,
        "two-variable-data",
        "Two-Variable Data: Models and Scatterplots",
        "Reading a scatterplot, using a line or curve of best fit to predict, interpreting its slope in context, and knowing where the model stops being trustworthy.",
      ),
      planned(
        5,
        "probability-and-conditional-probability",
        "Probability and Conditional Probability",
        "Probability from two-way tables, and the conditional questions where the denominator is a row or a column rather than the whole table.",
      ),
      planned(
        6,
        "inference-and-margin-of-error",
        "Inference from Sample Statistics and Margin of Error",
        "What a sample can and cannot claim about a population, how a margin of error is read, and what makes an interval narrower.",
      ),
      planned(
        7,
        "evaluating-statistical-claims",
        "Evaluating Statistical Claims: Observational Studies and Experiments",
        "Random selection versus random assignment, and the single rule that decides whether a study may claim causation or only association.",
      ),
    ],
  },
  {
    domain: "geometry-trig",
    title: "Geometry and Trigonometry",
    weight: "5–7 questions",
    intro:
      "The smallest domain and the most formula-driven — and the reference sheet gives you most of the formulas. Area and volume, angle and triangle relationships, right-triangle trigonometry, and circles in both their geometric and coordinate forms.",
    units: [
      planned(
        1,
        "area-and-volume",
        "Area and Volume Formulas",
        "Areas of plane figures and volumes of the solids on the reference sheet, composite shapes, and what happens to area and volume when a dimension is scaled.",
      ),
      planned(
        2,
        "lines-angles-and-triangles",
        "Lines, Angles, and Triangles",
        "Angles on parallel lines, the triangle angle sum and exterior angle, congruence and similarity, and the two-step chains the SAT builds from them.",
      ),
      planned(
        3,
        "right-triangles-and-trigonometry",
        "Right Triangles and Trigonometry",
        "Pythagoras, the special right triangles, the three trigonometric ratios, the complementary-angle identity, and radians where the test uses them.",
      ),
      planned(
        4,
        "circles",
        "Circles",
        "The equation of a circle and completing the square to find it, plus arcs, sectors, central and inscribed angles, and radian measure.",
      ),
    ],
  },
];

// ---------------------------------------------------------------------------
// Skill tags — one per official subtopic
// ---------------------------------------------------------------------------

/**
 * The SAT skill-tag taxonomy, one tag per official College Board subtopic.
 * Tags are what make gap detection and re-drill routing accurate
 * (`skill-taxonomy`), so they are pinned to the Board's own skill boundaries
 * rather than to any convenient grouping of our own.
 */
export const SAT_SKILL_TAGS: Record<string, string> = {
  "linear-equations-one-variable": "sat-linear-eq-one-var",
  "linear-equations-two-variables": "sat-linear-eq-two-var",
  "linear-functions": "sat-linear-functions",
  "systems-of-linear-equations": "sat-systems-linear",
  "linear-inequalities": "sat-linear-inequalities",
  "equivalent-expressions": "sat-equivalent-expressions",
  "nonlinear-equations-one-variable": "sat-nonlinear-eq-one-var",
  "systems-nonlinear-two-variables": "sat-nonlinear-systems",
  "nonlinear-functions": "sat-nonlinear-functions",
  "ratios-rates-proportions-units": "sat-ratios-rates",
  percentages: "sat-percentages",
  "one-variable-data": "sat-data-one-var",
  "two-variable-data": "sat-data-two-var",
  "probability-and-conditional-probability": "sat-probability",
  "inference-and-margin-of-error": "sat-inference-margin-error",
  "evaluating-statistical-claims": "sat-claims-study-design",
  "area-and-volume": "sat-area-volume",
  "lines-angles-and-triangles": "sat-lines-angles-triangles",
  "right-triangles-and-trigonometry": "sat-right-triangle-trig",
  circles: "sat-circles",
};

// ---------------------------------------------------------------------------
// Lookups — same contract as lib/esh-course.ts
// ---------------------------------------------------------------------------

export const SAT_COURSE_CONTEXT = "course:sat";

export function getSatDomainCourse(domain: string): SatDomainCourse | null {
  return SAT_COURSES.find((c) => c.domain === domain) ?? null;
}

/** Every subtopic across all four domains, in the Board's order. */
export function allSatSubtopics(): { domain: string; entry: SatUnitEntry }[] {
  return SAT_COURSES.flatMap((c) => c.units.map((entry) => ({ domain: c.domain, entry })));
}

export function getSatUnit(domain: string, unitSlug: string): CourseUnit | null {
  const course = getSatDomainCourse(domain);
  if (!course) return null;
  const entry = course.units.find((u) => u.slug === unitSlug);
  if (!entry || !entry.live) return null;
  const data = resolveSatSource(entry.source);
  if (!data) return null;
  // Stamp the SAT position and REPLACE buildsOn: a curated unit's own buildsOn
  // names unit numbers of its home course, which would be wrong on this spine.
  return { ...data, unit: entry.unit, buildsOn: entry.buildsOn };
}

export function getSatLesson(
  domain: string,
  unitSlug: string,
  lessonSlug: string,
): GenMathLesson | null {
  const unit = getSatUnit(domain, unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

/** The domain's course rendered through the shared CourseShell. */
export function satCourseDef(domain: string): CourseDef | null {
  const course = getSatDomainCourse(domain);
  if (!course) return null;
  return {
    slug: domain,
    title: course.title,
    context: SAT_COURSE_CONTEXT,
    intro: course.intro,
    basePath: `/practice/sat/learn/${domain}`,
    rootHref: "/practice/sat/learn",
    // Same reason as the ЭЕШ courses: all SAT course attempts share one
    // context, so the per-unit ratings plan would mislead here.
    personalize: false,
    spine: () => course.units,
    unit: (unitSlug) => getSatUnit(domain, unitSlug),
    lesson: (unitSlug, lessonSlug) => getSatLesson(domain, unitSlug, lessonSlug),
  };
}
