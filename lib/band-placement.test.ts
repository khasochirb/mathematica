import { describe, it, expect } from "vitest";
import {
  BANDS,
  TOPICS_PER_GRADE,
  bandTopicGrade,
  bandTopicHref,
  bandVerdict,
  getBandPlacementBank,
  SOLID_AT,
} from "./band-placement";
import { placementTopics } from "./placement-bank";
import type { PlacementResult } from "./placement-engine";

// A synthetic result: per-topic accuracy chosen by the topic's grade.
function resultWith(band: "mid" | "high", accByGrade: Record<number, number>): PlacementResult {
  const bank = getBandPlacementBank(band);
  const topicScores = placementTopics(bank).map((t) => {
    const grade = bandTopicGrade(band, t.slug);
    const acc = accByGrade[grade] ?? 0;
    const seen = 2;
    return { slug: t.slug, title: t.title, seen, correct: Math.round(acc * seen), accuracy: acc };
  });
  return {
    version: 1,
    overallAccuracy: 0,
    levelIndex: 0,
    level: "Foundational",
    topicScores,
    priorityTopics: [],
  };
}

describe("band placement bank", () => {
  it("samples every grade of the band, all three difficulties, unique ids", () => {
    for (const band of ["mid", "high"] as const) {
      const bank = getBandPlacementBank(band);
      const ids = new Set(bank.map((q) => q.id));
      expect(ids.size).toBe(bank.length);

      const grades = new Set(placementTopics(bank).map((t) => bandTopicGrade(band, t.slug)));
      expect(Array.from(grades).sort()).toEqual(BANDS[band].grades);

      for (const grade of BANDS[band].grades) {
        const topics = placementTopics(bank).filter((t) => bandTopicGrade(band, t.slug) === grade);
        expect(topics.length, `band ${band} grade ${grade}`).toBe(TOPICS_PER_GRADE);
        // every sampled topic ladders through all three tiers
        for (const t of topics) {
          const diffs = new Set(bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty));
          expect(diffs, `${band}/${t.slug}`).toEqual(new Set([1, 2, 3]));
        }
      }
      // topic titles carry the grade so the runner's breadcrumb is unambiguous
      for (const q of bank) expect(q.topicTitle).toMatch(/^Grade \d+ · /);
    }
  });

  it("routes each topic into its owning grade", () => {
    const bank = getBandPlacementBank("mid");
    for (const t of placementTopics(bank)) {
      const g = bandTopicGrade("mid", t.slug);
      expect(BANDS.mid.grades).toContain(g);
      expect(bandTopicHref("mid", t.slug)).toBe(`/math/${g}/${t.slug}`);
    }
  });
});

describe("band verdict", () => {
  it("recommends the first grade that is not yet solid", () => {
    // seen = 2 per topic in the synthetic result, so use accuracies that
    // 2 questions can actually produce (0, 0.5, 1)
    const v = bandVerdict("mid", resultWith("mid", { 6: 1, 7: 1, 8: 0.5, 9: 0 }));
    expect(v.grade).toBe(8);
    expect(v.clearedBand).toBe(false);
  });

  it("starts at the band's first grade when nothing is solid", () => {
    const v = bandVerdict("mid", resultWith("mid", { 6: 0.3, 7: 0.2, 8: 0, 9: 0 }));
    expect(v.grade).toBe(6);
    expect(v.clearedBand).toBe(false);
  });

  it("declares the band cleared only when every grade is solid", () => {
    const v = bandVerdict("high", resultWith("high", { 10: 1, 11: 1, 12: 1 }));
    expect(v.clearedBand).toBe(true);
    expect(v.grade).toBe(12);
    // ...and 0.5 sits below the bar
    expect(SOLID_AT).toBeGreaterThan(0.5);
  });

  it("a later solid grade cannot paper over an earlier gap", () => {
    // strong at 9 but weak at 7 → start at 7, where the gap is
    const v = bandVerdict("mid", resultWith("mid", { 6: 1, 7: 0.5, 8: 1, 9: 1 }));
    expect(v.grade).toBe(7);
  });

  it("per-grade scores aggregate the sampled topics", () => {
    const v = bandVerdict("mid", resultWith("mid", { 6: 1, 7: 1, 8: 1, 9: 1 }));
    for (const s of v.perGrade) {
      expect(s.seen).toBe(TOPICS_PER_GRADE * 2);
      expect(s.accuracy).toBe(1);
    }
  });
});
