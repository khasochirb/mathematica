import { describe, it, expect } from "vitest";
import { getCoursePlacementBank, getCoursePlacementBankMn, getCourseTitleMn } from "./placement-course-bank";
import { getBankTopics } from "./bank-data";
import { BANK_MN } from "./bank-data-mn";

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

// The Mongolian twin must be the English sitting in another language, never a
// different sitting: same ids in the same order, same answer key, same unit
// slugs (results, storage and the engine all key on these).
describe("getCoursePlacementBankMn", () => {
  const mirrored = Object.keys(BANK_MN).filter((slug) => getCoursePlacementBank(slug).length > 0);

  it("every mirrored course yields a Mongolian bank", () => {
    expect(mirrored.length).toBeGreaterThan(0);
    for (const slug of mirrored) {
      expect(getCoursePlacementBankMn(slug), slug).not.toBeNull();
      expect(getCourseTitleMn(slug), slug).toBeTruthy();
    }
  });

  for (const slug of mirrored) {
    it(`${slug}: same ids, correctIndex and topicSlug as the English harvest`, () => {
      const en = getCoursePlacementBank(slug);
      const mn = getCoursePlacementBankMn(slug)!;
      expect(mn.map((q) => q.id)).toEqual(en.map((q) => q.id));
      expect(mn.map((q) => q.correctIndex)).toEqual(en.map((q) => q.correctIndex));
      expect(mn.map((q) => q.topicSlug)).toEqual(en.map((q) => q.topicSlug));
      expect(mn.map((q) => q.difficulty)).toEqual(en.map((q) => q.difficulty));
      mn.forEach((q, i) => {
        expect(q.options.length, q.id).toBe(en[i].options.length);
        expect(q.prompt.length, q.id).toBeGreaterThan(0);
        expect(q.topicTitle.length, q.id).toBeGreaterThan(0);
      });
    });
  }

  it("a course without a mirror yields null", () => {
    expect(getCoursePlacementBankMn("no-such-course")).toBeNull();
  });
});
