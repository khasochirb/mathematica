import { describe, it, expect } from "vitest";
import { getLesson, validateLesson } from "@/lib/esh-lessons";

describe("getLesson", () => {
  it("loads the algebra lesson with all six content sections", () => {
    const lesson = getLesson("algebra");
    expect(lesson).toBeTruthy();
    expect(lesson!.skillTag).toBe("rational_expression");
    expect(lesson!.objective.length).toBeGreaterThan(0);
    expect(lesson!.concept.length).toBeGreaterThanOrEqual(2);
    expect(lesson!.formulas.length).toBeGreaterThanOrEqual(3);
    expect(lesson!.workedExamples.length).toBe(3);
    expect(lesson!.commonMistakes.length).toBeGreaterThanOrEqual(3);
    expect(lesson!.tryIt.skillTag).toBe("rational_expression");
  });

  it("returns null for a topic without a lesson file", () => {
    expect(getLesson("geometry")).toBeNull();
  });

  it("validateLesson accepts the shipped lesson", () => {
    expect(validateLesson(getLesson("algebra"))).toEqual([]);
  });

  it("validateLesson reports missing required fields", () => {
    const errors = validateLesson({ slug: "x" } as never);
    expect(errors.length).toBeGreaterThan(0);
  });
});
