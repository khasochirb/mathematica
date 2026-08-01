import { describe, it, expect } from "vitest";
import {
  contextFromPathname,
  lessonSlugsFromPathname,
  contextLabel,
  contextHref,
} from "@/lib/perf-context";

describe("performance contexts", () => {
  it("derives course contexts from lesson pathnames", () => {
    expect(contextFromPathname("/math/prob-stats/probability-models/geometric-probability")).toBe("course:prob-stats");
    expect(contextFromPathname("/math/geometry/circles/inscribed-angles")).toBe("course:geometry");
    expect(contextFromPathname("/math/vectors-matrices/the-dot-product/perpendicularity")).toBe("course:vectors-matrices");
    expect(contextFromPathname("/math/algebra-1/quadratic-equations/completing-the-square-and-the-quadratic-formula")).toBe("course:algebra-1");
    expect(contextFromPathname("/math/precalculus/the-unit-circle/radians")).toBe("course:precalculus");
    // "calculus" must never swallow "precalculus" paths (or vice versa)
    expect(contextFromPathname("/math/calculus/the-derivative/the-power-rule")).toBe("course:calculus");
    expect(contextFromPathname("/math/trigonometry/the-unit-circle/radians")).toBe("course:trigonometry");
    // "solid-geometry" must never be swallowed by the "geometry" alternative
    expect(contextFromPathname("/math/solid-geometry/pyramids/pyramid-anatomy")).toBe("course:solid-geometry");
    expect(contextFromPathname("/math/algebra-2/polynomial-functions/polynomial-basics-and-end-behavior")).toBe("course:algebra-2");
    expect(contextFromPathname("/math/6/fractions/adding-fractions")).toBe("course:grade-6");
    expect(contextFromPathname("/math/12/derivatives/the-power-rule")).toBe("course:grade-12");
  });

  it("returns null off the course tree — record nothing rather than guess", () => {
    expect(contextFromPathname("/practice/esh/test/2024a")).toBeNull();
    expect(contextFromPathname("/math")).toBeNull();
    expect(contextFromPathname("/dashboard")).toBeNull();
  });

  it("parses unit and lesson slugs from lesson pathnames only", () => {
    expect(lessonSlugsFromPathname("/math/prob-stats/combinations/stars-and-bars")).toEqual({
      unit: "combinations",
      lesson: "stars-and-bars",
    });
    expect(lessonSlugsFromPathname("/math/6/fractions/what-is-a-fraction")).toEqual({
      unit: "fractions",
      lesson: "what-is-a-fraction",
    });
    // hub / practice / test / placement pages are not lessons
    expect(lessonSlugsFromPathname("/math/geometry/circles")).toBeNull();
    expect(lessonSlugsFromPathname("/math/geometry/circles/practice")).toBeNull();
    expect(lessonSlugsFromPathname("/math/geometry/circles/test")).toBeNull();
    expect(lessonSlugsFromPathname("/math/6/placement")).toBeNull();
  });

  it("labels and hrefs cover every context shape", () => {
    expect(contextLabel("esh")).toBe("ЭЕШ бэлтгэл");
    expect(contextLabel("course:prob-stats")).toBe("Магадлал ба Статистик");
    expect(contextLabel("course:grade-8")).toBe("8-р анги");
    expect(contextLabel("mystery")).toBe("mystery");
    expect(contextHref("course:geometry")).toBe("/math/geometry");
    expect(contextHref("course:grade-7")).toBe("/math/7");
    expect(contextHref("esh")).toBe("/practice/esh");
    expect(contextHref("mystery")).toBeNull();
  });

  // Regression guard: integrated-3 shipped with pages and attempt-recording
  // (contextFromPathname matched it) but WITHOUT a label or href, so every
  // IM3 student's /math/progress read "Course not found" and the dashboard
  // could not link the course. Any course reachable by contextFromPathname
  // must be fully wired here — this test walks the real course routes so a
  // half-wired course fails in CI instead of in a student's progress page.
  it("every course a pathname maps to has a label AND an href", () => {
    const COURSE_ROUTES = [
      "geometry", "prob-stats", "vectors-matrices", "algebra-1", "algebra-2",
      "integrated-1", "integrated-2", "integrated-3", "precalculus",
      "calculus", "trigonometry", "solid-geometry", "ib-sl", "ib-hl",
      "6", "7", "8", "9", "10", "11", "12",
    ];
    for (const route of COURSE_ROUTES) {
      const context = contextFromPathname(`/math/${route}/some-unit/some-lesson`);
      expect(context, `/math/${route} produced no context`).not.toBeNull();
      // contextLabel echoes its input when it has no entry — that echo IS
      // the bug, so assert a real translation was found.
      expect(contextLabel(context!), `${context} has no label`).not.toBe(context);
      expect(contextHref(context!), `${context} has no href`).toBe(`/math/${route}`);
    }
  });
});
