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
});
