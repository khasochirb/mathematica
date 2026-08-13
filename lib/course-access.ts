// COURSE ACCESS POLICY — the single source of truth for what a non-Premium
// learner may open in /math.
//
// The rule (owner decision, 2026-08-04):
//   - Every course opens its FIRST topic free: its lessons, its practice set
//     and its test-yourself. A visitor to any course gets a real taste of
//     that course, not of some other grade's.
//   - One full course EXAM is free per course (the first one).
//   - Every other topic, and exams 2+, require Premium.
//   - Locked material stays VISIBLE (title, blurb, lesson count) behind a
//     lock + Premium badge — students see what they would get, and the
//     catalog stays indexable.
//
// Freeness is DERIVED from each course's spine (the first entry), never
// hand-listed, so adding or reordering topics can never silently open or
// close the gate. lib/course-access.test.ts pins that invariant.
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
// taught order. Grades and named courses share one shape here on purpose:
// the policy should not care which band a course belongs to.
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

/**
 * The one free topic of a course — the first entry of its spine, or null for
 * a course this module has never heard of.
 *
 * Grades that go live topic-by-topic use their first LIVE topic, so the free
 * sample is never a "coming soon" card.
 */
export function freeTopicSlug(courseKey: CourseKey): string | null {
  const order = COURSE_TOPIC_ORDER[courseKey];
  if (!order || order.length === 0) return null;
  const live = liveSlugsFor(courseKey);
  const firstLive = order.find((slug) => live === null || live.has(slug));
  return firstLive ?? null;
}

// Grade spines carry a `live` flag; named-course spines carry it too. A
// course whose entries have no flag is treated as all-live.
function liveSlugsFor(courseKey: CourseKey): Set<string> | null {
  const spine = SPINE_WITH_LIVE[courseKey];
  if (!spine) return null;
  const live = spine.filter((e) => e.live).map((e) => e.slug);
  return live.length ? new Set(live) : null;
}

const SPINE_WITH_LIVE: Record<CourseKey, { slug: string; live: boolean }[]> = {
  "2": GRADE2_SPINE,
  "3": GRADE3_SPINE,
  "4": GRADE4_SPINE,
  "6": GRADE6_SPINE,
  "7": GRADE7_SPINE,
  "8": GRADE8_SPINE,
  "9": GRADE9_SPINE,
  "10": GRADE10_SPINE,
  "11": GRADE11_SPINE,
  "12": GRADE12_SPINE,
  "algebra-1": ALG1_SPINE,
  "algebra-2": ALG2_SPINE,
  geometry: GEOMETRY_SPINE,
  trigonometry: TRIG_SPINE,
  "solid-geometry": SOLIDGEO_SPINE,
  "prob-stats": PROBSTAT_SPINE,
  precalculus: PRECALC_SPINE,
  calculus: CALC_SPINE,
  "vectors-matrices": VECMAT_SPINE,
  "integrated-1": IM1_SPINE,
  "integrated-2": IM2_SPINE,
  "integrated-3": IM3_SPINE,
  "ib-sl": IB_SL_SPINE,
  "ib-hl": IB_HL_SPINE,
  "ib-ai-sl": IB_AI_SL_SPINE,
};

/**
 * Is this topic readable without Premium? True only for the course's single
 * free topic. An unknown course fails CLOSED (locked) — a new course added
 * without registering here is never accidentally given away.
 */
export function isTopicFree(courseKey: CourseKey, topicSlug: string): boolean {
  const free = freeTopicSlug(courseKey);
  return free !== null && free === topicSlug;
}

/**
 * Is this course exam readable without Premium? The first exam of each
 * course is the free sample; the rest are Premium. Exam ids are of the form
 * "<course-prefix><n>" (im3e1, g12e2, …), so the policy reads the trailing
 * number rather than hard-coding ids.
 */
export function isExamFree(examId: string): boolean {
  const m = /(\d+)$/.exec(examId);
  return m ? Number(m[1]) === 1 : false;
}

/**
 * Is this problem-bank unit readable without Premium? The bank mirrors the
 * course units, so it follows the same rule — otherwise a locked topic's
 * practice would be free through the bank's back door.
 */
export function isBankUnitFree(bankSlug: string, unitId: string): boolean {
  // Bank slugs mirror course keys ("5", "integrated-3", "algebra-1"); hub
  // banks (sat, ib-sl, ib-hl) key straight through too.
  return isTopicFree(bankSlug, unitId);
}

/**
 * The access verdict for a piece of course content.
 *   "open"    — readable now
 *   "sign-in" — free material, but the reader is anonymous
 *   "premium" — Premium material, reader is signed in without a subscription
 */
export type AccessVerdict = "open" | "sign-in" | "premium";

export function accessFor(opts: {
  isAuthenticated: boolean;
  isSubscribed: boolean;
  free: boolean;
}): AccessVerdict {
  if (opts.isSubscribed) return "open";
  if (!opts.free) return opts.isAuthenticated ? "premium" : "premium";
  return opts.isAuthenticated ? "open" : "sign-in";
}
