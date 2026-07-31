// SAT Math course — the taught curriculum inside the SAT hub (backlog #245,
// resource-blueprint build-order item 4).
//
// Four domain courses mirror the College Board's own blueprint — Algebra and
// Advanced Math carry ~35% of the test each, Problem-Solving & Data Analysis
// and Geometry & Trigonometry ~15% each — and the domain slugs equal the SAT
// bank's unit ids, so the hub's course, topic practice and analytics all
// speak the same taxonomy (the blueprint's consistency rule).
//
// Same architecture as the ЭЕШ prep courses (lib/esh-course.ts): units are
// CURATED from the sympy-verified English catalog through one registry, so
// every lesson, practice set and test-yourself a student opens here is the
// same verified content taught in /math — re-ordered for the exam, not for a
// school year. English content is exam-realism policy in this hub
// (memory/expansion-vision.md §4.7), not a stopgap.

import {
  resolveCatalogSource,
  type EshUnitEntry as SatUnitEntry,
} from "@/lib/esh-course";
import type { CourseUnit, GenMathLesson } from "@/lib/genmath-lessons";
import type { CourseDef } from "@/components/course/CourseShell";

export type { SatUnitEntry };

export interface SatDomainCourse {
  /** Domain slug — equals the SAT bank's unit id (lib/problem-bank sat). */
  domain: string;
  /** The College Board's name for the domain. */
  title: string;
  /** Approximate share of the Math section's questions. */
  weight: string;
  intro: string;
  units: SatUnitEntry[];
}

function live(unit: number, slug: string, source: string, buildsOn?: string): SatUnitEntry {
  const data = resolveCatalogSource(source);
  if (!data) throw new Error(`sat-course: source "${source}" did not resolve for "${slug}"`);
  return { unit, slug, title: data.title, blurb: data.blurb, buildsOn, live: true, source };
}

export const SAT_COURSES: SatDomainCourse[] = [
  {
    domain: "algebra",
    title: "Algebra",
    weight: "~35% of the test",
    intro:
      "The heart of the SAT Math section: linear equations and functions read every way the test asks — solve, interpret, build from context — plus systems and inequalities. Master the line and a third of the paper is yours.",
    units: [
      live(1, "linear-equations", "algebra-1/linear-equations"),
      live(2, "linear-functions", "algebra-1/linear-functions"),
      live(3, "systems-of-equations", "algebra-1/systems-of-equations"),
      live(4, "inequalities", "algebra-1/inequalities"),
      live(5, "linear-models-and-variation", "9/linear-models-and-variation",
        "Linear functions from Unit 2 — the SAT's favorite dress for them."),
      live(6, "inequalities-in-two-variables", "9/inequalities-in-two-variables",
        "Inequalities from Unit 4, now as constraint systems in the plane."),
    ],
  },
  {
    domain: "advanced-math",
    title: "Advanced Math",
    weight: "~35% of the test",
    intro:
      "Everything nonlinear: function notation, quadratics from every angle, exponents and radicals, exponential growth, rational expressions, transformations, and the nonlinear systems that close out the hard third of the section.",
    units: [
      live(1, "introduction-to-functions", "9/introduction-to-functions"),
      live(2, "polynomials-and-factoring", "algebra-1/polynomials-and-factoring"),
      live(3, "quadratic-equations", "algebra-1/quadratic-equations",
        "Factoring from Unit 2."),
      live(4, "quadratic-functions", "10/quadratic-functions",
        "Solving quadratics from Unit 3; here their graphs carry the questions."),
      live(5, "radicals-and-rational-exponents", "algebra-2/radicals-and-rational-exponents"),
      live(6, "exponential-functions", "10/exponential-functions"),
      live(7, "rational-expressions", "10/rational-expressions"),
      live(8, "functions-and-transformations", "algebra-2/functions-and-transformations",
        "Function notation from Unit 1."),
      live(9, "systems-and-nonlinear-models", "algebra-2/systems-and-nonlinear-models",
        "Quadratics from Units 3–4 meeting the lines of the Algebra course."),
    ],
  },
  {
    domain: "problem-solving-data",
    title: "Problem-Solving & Data Analysis",
    weight: "~15% of the test",
    intro:
      "The calculator-friendly sixth of the paper: ratios and rates, percentages, reading one- and two-variable data, probability from tables, and the study-design questions everyone forgets to prepare — every one of them answerable from a small set of moves.",
    units: [
      live(1, "proportional-relationships", "7/proportional-relationships"),
      live(2, "percent-applications", "7/percent-applications"),
      live(3, "describing-data", "prob-stats/describing-data"),
      live(4, "two-variable-data", "prob-stats/two-variable-data",
        "The one-variable summaries from Unit 3, now in scatterplots and fits."),
      live(5, "probability-models", "prob-stats/probability-models"),
      live(6, "inference-and-studies", "prob-stats/inference-and-studies",
        "Sampling ideas from Unit 5 — margins of error and what a study can claim."),
    ],
  },
  {
    domain: "geometry-trig",
    title: "Geometry & Trigonometry",
    weight: "~15% of the test",
    intro:
      "Lines, angles and triangles, similarity, right-triangle trig with SOH-CAH-TOA and the special triangles, circles, and volume — SAT geometry chains two facts per problem, and these six units build exactly those chains.",
    units: [
      live(1, "triangles-and-congruence", "geometry/triangles-and-congruence"),
      live(2, "similarity", "geometry/similarity",
        "Congruence from Unit 1 — similarity is congruence with a scale factor."),
      live(3, "right-triangles-and-trig", "geometry/right-triangles-and-trig",
        "Similarity from Unit 2 is why the trig ratios exist at all."),
      live(4, "area-and-perimeter", "geometry/area-and-perimeter"),
      live(5, "circles", "geometry/circles"),
      live(6, "surface-area-and-volume", "geometry/surface-area-and-volume",
        "The areas of Unit 4, extruded into the volume formulas the SAT provides."),
    ],
  },
];

// ---------------------------------------------------------------------------
// Lookups — same contract as lib/esh-course.ts
// ---------------------------------------------------------------------------

export const SAT_COURSE_CONTEXT = "course:sat";

export function getSatDomainCourse(domain: string): SatDomainCourse | null {
  return SAT_COURSES.find((c) => c.domain === domain) ?? null;
}

export function getSatUnit(domain: string, unitSlug: string): CourseUnit | null {
  const course = getSatDomainCourse(domain);
  if (!course) return null;
  const entry = course.units.find((u) => u.slug === unitSlug);
  if (!entry || !entry.live) return null;
  const data = resolveCatalogSource(entry.source);
  if (!data) return null;
  // Stamp the SAT position and REPLACE buildsOn: the data's buildsOn names
  // unit numbers of its home course, which would be wrong on this spine.
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
