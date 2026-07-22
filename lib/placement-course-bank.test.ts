import { describe, it, expect } from "vitest";
import { getCoursePlacementBank } from "./placement-bank";
import { getBankTopics } from "./problem-bank";

// The harvested course placement banks: every problem-bank subject must
// yield a usable adaptive bank — every unit represented, three difficulty
// tiers overall, valid MCQs (4 distinct options, in-range answer), and the
// topicSlug vocabulary must be the course's unit slugs (that is what lets a
// placement result seed unit-mapped attribute ratings).
describe("getCoursePlacementBank", () => {
  const subjects = getBankTopics();

  it("covers every problem-bank subject", () => {
    expect(subjects.length).toBeGreaterThanOrEqual(9);
    for (const s of subjects) {
      expect(getCoursePlacementBank(s.slug).length, s.slug).toBeGreaterThan(0);
    }
  });

  for (const s of subjects) {
    it(`${s.slug}: sound bank`, () => {
      const bank = getCoursePlacementBank(s.slug);
      const unitIds = new Set(s.units.map((u) => u.id));
      const seenUnits = new Set<string>();
      const seenIds = new Set<string>();
      const levels = new Set<number>();
      for (const q of bank) {
        expect(seenIds.has(q.id), `dup id ${q.id}`).toBe(false);
        seenIds.add(q.id);
        expect(unitIds.has(q.topicSlug), `unknown unit ${q.topicSlug}`).toBe(true);
        seenUnits.add(q.topicSlug);
        levels.add(q.difficulty);
        expect(q.options.length).toBe(4);
        expect(new Set(q.options).size).toBe(4);
        expect(q.correctIndex).toBeGreaterThanOrEqual(0);
        expect(q.correctIndex).toBeLessThan(4);
        expect(q.prompt.length).toBeGreaterThan(0);
        expect(q.explanation.length).toBeGreaterThan(0);
        expect(q.topicTitle.length).toBeGreaterThan(0);
      }
      // Every unit contributes at least one question, and the bank as a
      // whole spans all three tiers.
      expect(seenUnits.size, `${s.slug} units covered`).toBe(unitIds.size);
      expect(levels).toEqual(new Set([1, 2, 3]));
    });
  }

  it("unknown course yields an empty bank", () => {
    expect(getCoursePlacementBank("no-such-course")).toEqual([]);
  });
});
