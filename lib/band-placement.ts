// Band placement — the ENTRY test of a school band (resource blueprint:
// every band carries a placement diagnostic at the top and full-course exams
// at the bottom). It answers the one question a family actually has when
// they arrive: "which grade should this student start in?"
//
// Composition, not authoring: every grade already has a curated placement
// bank (lib/placement-bank.ts) with three genuine difficulty tiers per
// topic. A band test SAMPLES a spread of topics from each of its grades, so
// the sitting stays ~20 questions while still touching every grade. The
// per-grade accuracy then names the starting grade: the first grade the
// student is not yet solid on.

import {
  getPlacementBank,
  getGrade7PlacementBank,
  getGrade8PlacementBank,
  getGrade9PlacementBank,
  getGrade10PlacementBank,
  getGrade11PlacementBank,
  getGrade12PlacementBank,
  placementTopics,
  type PlacementQuestion,
} from "@/lib/placement-bank";
import type { PlacementResult } from "@/lib/placement-engine";

export type BandId = "mid" | "high";

export const BANDS: Record<
  BandId,
  { title: string; grades: number[]; namespace: string }
> = {
  mid: { title: "Mid school", grades: [6, 7, 8, 9], namespace: "band-mid" },
  high: { title: "High school", grades: [10, 11, 12], namespace: "band-high" },
};

const GRADE_BANK: Record<number, () => PlacementQuestion[]> = {
  6: getPlacementBank,
  7: getGrade7PlacementBank,
  8: getGrade8PlacementBank,
  9: getGrade9PlacementBank,
  10: getGrade10PlacementBank,
  11: getGrade11PlacementBank,
  12: getGrade12PlacementBank,
};

/** How many topics each grade contributes to its band's test. */
export const TOPICS_PER_GRADE = 3;

// A topic slug can, in principle, appear in two grades' spines. The band
// bank prefixes ids with the grade so ids stay unique, and this map is how
// results route back into the owning grade.
const gradeOfCache = new Map<BandId, Map<string, number>>();
const bankCache = new Map<BandId, PlacementQuestion[]>();

/**
 * A deterministic spread of TOPICS_PER_GRADE topics per grade: first,
 * middle, last of the grade's topic list, so the sample spans the year
 * rather than clustering at its start.
 */
function sampleTopics(bank: PlacementQuestion[]): string[] {
  const topics = placementTopics(bank).map((t) => t.slug);
  if (topics.length <= TOPICS_PER_GRADE) return topics;
  const picks = new Set<number>();
  for (let i = 0; i < TOPICS_PER_GRADE; i++) {
    picks.add(Math.round((i * (topics.length - 1)) / (TOPICS_PER_GRADE - 1)));
  }
  return Array.from(picks).map((i) => topics[i]);
}

export function getBandPlacementBank(band: BandId): PlacementQuestion[] {
  const cached = bankCache.get(band);
  if (cached) return cached;

  const gradeOf = new Map<string, number>();
  const out: PlacementQuestion[] = [];
  for (const grade of BANDS[band].grades) {
    const bank = GRADE_BANK[grade]();
    const keep = new Set(sampleTopics(bank));
    for (const q of bank) {
      if (!keep.has(q.topicSlug)) continue;
      // First grade to claim a slug wins — a duplicate slug in a later grade
      // would make routing ambiguous, so it is skipped rather than shadowed.
      if (gradeOf.has(q.topicSlug) && gradeOf.get(q.topicSlug) !== grade) continue;
      gradeOf.set(q.topicSlug, grade);
      out.push({ ...q, id: `g${grade}:${q.id}`, topicTitle: `Grade ${grade} · ${q.topicTitle}` });
    }
  }
  gradeOfCache.set(band, gradeOf);
  bankCache.set(band, out);
  return out;
}

/** The grade a band-bank topic belongs to (for routing links). */
export function bandTopicGrade(band: BandId, topicSlug: string): number {
  getBandPlacementBank(band); // ensure the map is built
  return gradeOfCache.get(band)!.get(topicSlug) ?? BANDS[band].grades[0];
}

export function bandTopicHref(band: BandId, topicSlug: string): string {
  return `/math/${bandTopicGrade(band, topicSlug)}/${topicSlug}`;
}

// ---------------------------------------------------------------------------
// The verdict: which grade to start in
// ---------------------------------------------------------------------------

/** A grade is "solid" at or above this accuracy on its sampled topics. */
export const SOLID_AT = 0.7;

export type GradeScore = { grade: number; seen: number; correct: number; accuracy: number };

export type BandVerdict = {
  /** The recommended starting grade. */
  grade: number;
  /** True when every grade of the band was solid — the student is ready to
   *  finish the band (sit the exit exams / move up), not to re-study it. */
  clearedBand: boolean;
  perGrade: GradeScore[];
};

export function bandVerdict(band: BandId, result: PlacementResult): BandVerdict {
  getBandPlacementBank(band);
  const gradeOf = gradeOfCache.get(band)!;
  const byGrade = new Map<number, GradeScore>(
    BANDS[band].grades.map((g) => [g, { grade: g, seen: 0, correct: 0, accuracy: 0 }]),
  );
  for (const t of result.topicScores) {
    const g = gradeOf.get(t.slug);
    if (g === undefined) continue;
    const s = byGrade.get(g)!;
    s.seen += t.seen;
    s.correct += t.correct;
  }
  const perGrade = Array.from(byGrade.values()).map((s) => ({
    ...s,
    accuracy: s.seen ? s.correct / s.seen : 0,
  }));

  // The starting grade is the FIRST grade (in band order) the student is not
  // yet solid on: everything before it is secure, and starting any later
  // would build on gaps. An unseen grade (seen = 0 should not happen, but
  // storage/version drift could produce it) counts as not-solid, never as
  // cleared.
  for (const s of perGrade) {
    if (s.seen === 0 || s.accuracy < SOLID_AT) {
      return { grade: s.grade, clearedBand: false, perGrade };
    }
  }
  const last = BANDS[band].grades[BANDS[band].grades.length - 1];
  return { grade: last, clearedBand: true, perGrade };
}
