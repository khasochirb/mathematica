// COURSE ACCESS POLICY — the single source of truth for what a learner may
// open in /math, the problem bank and the course exams.
//
// The rule (owner decision, 2026-11-23 — replaces the 2026-08-04 paywall):
//   - The whole site is FREE. There is no Premium tier: every topic, every
//     course exam and every problem-bank unit opens for any signed-in user.
//   - An ACCOUNT is still required. Anonymous visitors meet the sign-in wall
//     on content routes, exactly as before, so progress and placement have
//     somewhere to live.
//
// The `is*Free` helpers are kept (and now always answer true) so every
// call site keeps asking one place; if a paid tier ever returns, it returns
// here and lib/course-access.test.ts says so.
//
// This module imports ONLY lib/genmath-spines (pure literals, no corpus), so
// it is safe to use from client components and adds no bundle weight.

import {
  ALG1_SPINE,
  ALG2_SPINE,
  CALC_SPINE,
  GEOMETRY_SPINE,
  GRADE2_SPINE,
  GRADE3_SPINE,
  GRADE4_SPINE,
  GRADE6_SPINE,
  GRADE7_SPINE,
  GRADE8_SPINE,
  GRADE9_SPINE,
  GRADE10_SPINE,
  GRADE11_SPINE,
  GRADE12_SPINE,
  IB_HL_SPINE,
  IB_SL_SPINE,
  IB_AI_SL_SPINE,
  IM1_SPINE,
  IM2_SPINE,
  IM3_SPINE,
  PRECALC_SPINE,
  PROBSTAT_SPINE,
  SOLIDGEO_SPINE,
  TRIG_SPINE,
  VECMAT_SPINE,
} from "@/lib/genmath-spines";

/** A course's URL segment under /math — "5", "algebra-1", "integrated-3". */
export type CourseKey = string;

// Every course keyed by its /math segment, mapped to its spine's slugs in
// taught order. Nothing is gated on it any more; it stays so the tests can
// prove every routed course, and every topic in it, opens for a signed-in
// user.
const COURSE_TOPIC_ORDER: Record<CourseKey, string[]> = {
  "2": GRADE2_SPINE.map((t) => t.slug),
  "3": GRADE3_SPINE.map((t) => t.slug),
  "4": GRADE4_SPINE.map((t) => t.slug),
  "6": GRADE6_SPINE.map((t) => t.slug),
  "7": GRADE7_SPINE.map((t) => t.slug),
  "8": GRADE8_SPINE.map((t) => t.slug),
  "9": GRADE9_SPINE.map((t) => t.slug),
  "10": GRADE10_SPINE.map((t) => t.slug),
  "11": GRADE11_SPINE.map((t) => t.slug),
  "12": GRADE12_SPINE.map((t) => t.slug),
  "algebra-1": ALG1_SPINE.map((u) => u.slug),
  "algebra-2": ALG2_SPINE.map((u) => u.slug),
  geometry: GEOMETRY_SPINE.map((u) => u.slug),
  trigonometry: TRIG_SPINE.map((u) => u.slug),
  "solid-geometry": SOLIDGEO_SPINE.map((u) => u.slug),
  "prob-stats": PROBSTAT_SPINE.map((u) => u.slug),
  precalculus: PRECALC_SPINE.map((u) => u.slug),
  calculus: CALC_SPINE.map((u) => u.slug),
  "vectors-matrices": VECMAT_SPINE.map((u) => u.slug),
  "integrated-1": IM1_SPINE.map((u) => u.slug),
  "integrated-2": IM2_SPINE.map((u) => u.slug),
  "integrated-3": IM3_SPINE.map((u) => u.slug),
  "ib-sl": IB_SL_SPINE.map((u) => u.slug),
  "ib-hl": IB_HL_SPINE.map((u) => u.slug),
  "ib-ai-sl": IB_AI_SL_SPINE.map((u) => u.slug),
};

/** Every course the policy knows about. */
export function listCourseKeys(): CourseKey[] {
  return Object.keys(COURSE_TOPIC_ORDER);
}

/** A course's topic slugs in taught order, or null for an unknown course. */
export function courseTopicSlugs(courseKey: CourseKey): string[] | null {
  return COURSE_TOPIC_ORDER[courseKey] ?? null;
}

/** Is this topic readable by a signed-in user? Always — the site is free. */
export function isTopicFree(_courseKey: CourseKey, _topicSlug: string): boolean {
  return true;
}

/** Is this course exam readable by a signed-in user? Always — the site is free. */
export function isExamFree(_examId: string): boolean {
  return true;
}

/**
 * Is this problem-bank unit readable by a signed-in user? Always — the site
 * is free. (Signature kept so the bank gates keep calling one place.)
 */
export function isBankUnitFree(
  _bankSlug: string,
  _unitId: string,
  _unitOrder?: readonly string[],
): boolean {
  return true;
}

/**
 * The access verdict for a piece of course content.
 *   "open"    — readable now (any signed-in user)
 *   "sign-in" — the reader is anonymous
 */
export type AccessVerdict = "open" | "sign-in";

export function accessFor(opts: { isAuthenticated: boolean }): AccessVerdict {
  return opts.isAuthenticated ? "open" : "sign-in";
}
