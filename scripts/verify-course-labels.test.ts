import { describe, it, expect } from "vitest";
import { EN_COURSE_LABELS, MN_COURSE_LABELS, courseLabels } from "../components/course/CourseShell";

// THE COURSE SHELL'S MONGOLIAN.
//
// Sixteen pages read these labels — the three Integrated courses and every
// named course that renders through CourseShell — so this is the
// highest-leverage translation in group 1 and the one whose failure would be
// widest.
//
// The shape that matters is the FALLBACK. courseLabels() merges Mongolian over
// English rather than switching between two objects, because MN_COURSE_LABELS
// is deliberately incomplete: four labels are prose that no source has, and
// Khas writes those. A merge renders them in English; a switch would render
// them as undefined, and `undefined` in JSX is invisible — a heading would
// simply vanish from sixteen pages with nothing to notice.

describe("course shell labels", () => {
  it("falls back to English for anything unwritten", () => {
    const mn = courseLabels("mn");
    for (const key of Object.keys(EN_COURSE_LABELS) as (keyof typeof EN_COURSE_LABELS)[]) {
      expect(mn[key], `label "${key}" is missing entirely — it must fall back to English`).toBeDefined();
      expect(mn[key], `label "${key}" resolved to an empty string`).not.toBe("");
    }
  });

  it("returns the English object untouched for English readers", () => {
    expect(courseLabels("en")).toBe(EN_COURSE_LABELS);
  });

  it("actually translates the labels it claims to", () => {
    const mn = courseLabels("mn");
    const CYRILLIC = /[А-Яа-яӨөҮү]/;
    for (const key of Object.keys(MN_COURSE_LABELS)) {
      const v = (mn as unknown as Record<string, unknown>)[key];
      if (typeof v === "string") {
        expect(CYRILLIC.test(v), `"${key}" is in MN_COURSE_LABELS but resolved to "${v}"`).toBe(true);
      }
    }
  });

  it("keeps the composed heading a function, not a baked string", () => {
    // spineHeading takes the unit count. Freezing it at one number would be
    // wrong on every course but one, and Mongolian puts the number in a
    // different place than English — so it has to stay a function.
    const mn = courseLabels("mn");
    expect(typeof mn.spineHeading).toBe("function");
    expect(mn.spineHeading(7)).toContain("7");
    expect(mn.spineHeading(7)).not.toBe(mn.spineHeading(8));
  });

  it("records which labels still need Khas", () => {
    // Not a failure — a ledger. These are prose rather than labels, no source
    // has them, and inventing them is precisely the translationese
    // docs/MONGOLIAN.md forbids. The test exists so the list cannot grow
    // silently.
    const missing = (Object.keys(EN_COURSE_LABELS) as string[]).filter(
      (k) => !(k in MN_COURSE_LABELS),
    );
    // `reveal` joined the list on 13 Sep 2026 for a different reason from the
    // rest: its Mongolian exists but is Claude's own, and its chrome entries
    // carry no `ok`. On production chrome() holds those back, so shipping them
    // from this object would have walked straight around that gate. Withdrawn
    // until Khas reads the four strings.
    expect(missing.sort()).toEqual(
      ["examsBody", "examsHeading", "examsTitle", "reveal", "selfGradedBody"].sort(),
    );
  });
});
