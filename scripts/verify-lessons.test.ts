import { describe, it, expect } from "vitest";
import { getLesson, validateLesson, resolveWorkedExamples } from "@/lib/esh-lessons";
import { getFreeQuestions } from "@/lib/esh-questions";

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

describe("resolveWorkedExamples", () => {
  const lesson = getLesson("algebra")!;

  it("resolves every worked-example source to a real question", () => {
    const resolved = resolveWorkedExamples(lesson);
    expect(resolved.length).toBe(lesson.workedExamples.length);
    for (const r of resolved) {
      expect(r.question).toBeTruthy();
      expect(r.question.solution.length).toBeGreaterThan(0);
    }
  });

  it("only references free-pool questions (no premium leak)", () => {
    const freeSources = new Set(getFreeQuestions().map((q) => q.source));
    for (const ref of lesson.workedExamples) {
      expect(freeSources.has(ref.source)).toBe(true);
    }
  });

  it("carries the teaching note alongside the question", () => {
    const resolved = resolveWorkedExamples(lesson);
    expect(resolved[0].teachingNote).toBeTruthy();
  });
});

import { dedupeByFamily, selectTryItQuestions } from "@/lib/esh-lessons";
import { getQuestionsByTopicForUser } from "@/lib/esh-questions";

describe("dedupeByFamily", () => {
  it("collapses number-only variants to one per family", () => {
    const a = { source: "T-A", body: "$x=5$ үед утга ол" } as never;
    const b = { source: "T-B", body: "$x=9$ үед утга ол" } as never;
    const c = { source: "T-C", body: "өөр бодлого" } as never;
    expect(dedupeByFamily([a, b, c]).length).toBe(2);
  });
});

describe("selectTryItQuestions", () => {
  const lesson = getLesson("algebra")!;
  const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);

  it("returns distinct families, excludes worked-example sources, caps at inlineCount", () => {
    const worked = new Set(lesson.workedExamples.map((w) => w.source));
    const picked = selectTryItQuestions(lesson, pool);
    expect(picked.length).toBeGreaterThanOrEqual(3);
    expect(picked.length).toBeLessThanOrEqual(lesson.tryIt.inlineCount);
    for (const q of picked) {
      expect(q.skill_tag).toBe(lesson.tryIt.skillTag);
      expect(worked.has(q.source)).toBe(false);
    }
    const families = new Set(
      picked.map((q) => q.body.replace(/[0-9]/g, " ").replace(/\s+/g, " ").trim()),
    );
    expect(families.size).toBe(picked.length);
  });
});
