import { describe, it, expect } from "vitest";
import { MN_COURSE_LABELS } from "../components/course/CourseShell";
import { ALL_CHROME, isApproved } from "../lib/i18n/chrome";

// A SECOND COPY OF THE CHROME VOCABULARY.
//
// `MN_COURSE_LABELS` is read by sixteen pages and holds its own Mongolian for
// words the chrome dictionary also defines — unit, lesson, "back to unit",
// "builds on". Two copies of one vocabulary is exactly the drift the
// dictionary exists to prevent, and it already happened: Khas ruled «Бүлэг»
// for unit and rewrote "Builds on" on 13 Sep 2026, both were applied to
// chrome.ts, and this object kept «Нэгж» and «Уг нь тулгуурлах» — wrong on
// sixteen pages, silently, because nothing compared the two.
//
// Merging them is the real fix; the shapes differ (some labels are functions
// of a count) so it is not a one-line change. Until then this test makes the
// divergence impossible to reintroduce.

const MN_OF = (en: string) => ALL_CHROME.find((e) => e.en === en)?.mn ?? "";

// label key in MN_COURSE_LABELS -> the chrome entry that governs the same word
const GOVERNED_BY: Record<string, string> = {
  unitWord: "Unit",
  unitLead: "Unit",
  lessonLead: "Lesson",
  lessons: "Lessons",
  buildsOn: "Builds on",
  backToCourse: "Back to the course",
  backToUnit: "Back to unit",
};

describe("MN course labels", () => {
  it("never contradicts the chrome dictionary", () => {
    const wrong: string[] = [];
    for (const [key, en] of Object.entries(GOVERNED_BY)) {
      const label = (MN_COURSE_LABELS as Record<string, unknown>)[key];
      if (typeof label !== "string" || !label) continue;
      const canonical = MN_OF(en);
      if (canonical && label !== canonical) {
        wrong.push(`${key}: "${label}" but chrome["${en}"] is "${canonical}"`);
      }
    }
    expect(wrong, "two Mongolian words for one English word — one of them is stale").toEqual([]);
  });

  it("carries Khas's 13 Sep rulings, which this object originally missed", () => {
    // Pinned by value, not by comparison, so that reverting BOTH copies
    // together still fails. These are the exact words he ruled.
    expect(MN_COURSE_LABELS.unitWord).toBe("Бүлэг");
    expect(MN_COURSE_LABELS.unitLead).toBe("Бүлэг");
    expect(MN_COURSE_LABELS.backToUnit).toBe("Бүлэг рүү буцах");
    expect(MN_COURSE_LABELS.buildsOn).toBe("Тулгуур сэдэв нь:");
    // The spine heading interpolates a count and says the word inline.
    const heading = MN_COURSE_LABELS.spineHeading?.(7) ?? "";
    expect(heading).toContain("бүлэг");
    expect(heading).not.toContain("нэгж");
  });

  it("only carries wording somebody other than Claude decided", () => {
    // Every string here should be traceable: verbatim from the live site,
    // written by Khas, or an approved chrome entry. This checks the ones the
    // dictionary governs; the rest carry a provenance comment in the source.
    for (const en of Object.values(GOVERNED_BY)) {
      const entry = ALL_CHROME.find((e) => e.en === en);
      expect(entry, `chrome has no entry for "${en}"`).toBeTruthy();
      expect(
        isApproved(entry!),
        `"${en}" governs a course label but is not approved — it must not reach production`,
      ).toBe(true);
    }
  });
});
