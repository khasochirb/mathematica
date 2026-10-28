import { describe, expect, it } from "vitest";
import { getCourseExam } from "@/lib/course-exam";
import { EXAMS_MN } from "@/lib/course-exam-mn";

// The Mongolian exams are generated from the Mongolian bank by variant id
// (scripts/i18n/mn_exams.py). Scoring reads correctIndex and the unit tags, so
// a mirror that drifted from its English paper would grade students wrongly
// while looking fine. These hold the mirror to the English key.
describe("Mongolian course exams", () => {
  const ids = Object.keys(EXAMS_MN);

  it("has at least the band exit exams", () => {
    expect(ids.length).toBeGreaterThan(0);
  });

  for (const id of ids) {
    it(`${id} matches its English paper question for question`, () => {
      const en = getCourseExam(id);
      const mn = EXAMS_MN[id];
      expect(en).not.toBeNull();
      expect(mn.meta.examId).toBe(id);
      expect(mn.meta.course).toBe(en!.meta.course);
      expect(mn.meta.minutes).toBe(en!.meta.minutes);
      expect(mn.questions.map((q) => q.id)).toEqual(en!.questions.map((q) => q.id));
      mn.questions.forEach((q, i) => {
        const e = en!.questions[i];
        expect(q.correctIndex).toBe(e.correctIndex);
        expect(q.unit).toBe(e.unit);
        expect(q.options.length).toBe(e.options.length);
        // Rewritten, not copied: the statement must not still be the English.
        expect(q.statement === e.statement && /[a-z]{4,}/.test(e.statement.replace(/\$[^$]*\$/g, ""))).toBe(false);
      });
    });
  }
});
