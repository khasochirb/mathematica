import { describe, it, expect } from "vitest";
import { courseTotalLessons } from "./genmath-lessons";

// Guards the dashboard progress-bar DENOMINATOR. Not pinned to exact counts
// (those grow as content is authored) — instead asserts the helper resolves
// every course context to a positive total and refuses non-course contexts,
// so a getter rename or a broken dispatch surfaces here instead of showing
// students a course with no progress bar.
describe("courseTotalLessons", () => {
  const COURSE_CONTEXTS = [
    "course:grade-6",
    "course:grade-7",
    "course:grade-8",
    "course:grade-9",
    "course:grade-10",
    "course:grade-11",
    "course:grade-12",
    "course:geometry",
    "course:prob-stats",
    "course:vectors-matrices",
    "course:algebra-1",
    "course:algebra-2",
    "course:precalculus",
    "course:calculus",
    "course:trigonometry",
    "course:solid-geometry",
    "course:ib-sl",
    "course:ib-hl",
  ];

  it("resolves every course context to a positive lesson total", () => {
    for (const ctx of COURSE_CONTEXTS) {
      const total = courseTotalLessons(ctx);
      expect(total, ctx).toBeGreaterThan(0);
    }
  });

  it("returns null for non-course contexts", () => {
    expect(courseTotalLessons("esh")).toBeNull();
    expect(courseTotalLessons("sat")).toBeNull();
    expect(courseTotalLessons("ib")).toBeNull();
    expect(courseTotalLessons("course:grade-99")).toBeNull();
    expect(courseTotalLessons("course:nonexistent")).toBeNull();
  });
});
