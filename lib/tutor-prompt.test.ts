import { describe, it, expect } from "vitest";
import { parseTutorBody, buildTutorSystem } from "./tutor-prompt";

const validBody = {
  lang: "mn",
  messages: [{ role: "user", content: "Яагаад буруу вэ?" }],
  context: {
    kind: "question",
    question: "What is $2+2$?",
    options: { A: "3", B: "4" },
    correctAnswer: "B",
    selectedAnswer: "A",
  },
};

describe("parseTutorBody", () => {
  it("accepts a valid body and normalizes it", () => {
    const parsed = parseTutorBody(validBody);
    expect(parsed).not.toBeNull();
    expect(parsed!.lang).toBe("mn");
    expect(parsed!.context.kind).toBe("question");
    expect(parsed!.context.options).toEqual({ A: "3", B: "4" });
  });

  it("rejects garbage shapes", () => {
    expect(parseTutorBody(null)).toBeNull();
    expect(parseTutorBody("x")).toBeNull();
    expect(parseTutorBody({})).toBeNull();
    expect(parseTutorBody({ ...validBody, lang: "fr" })).toBeNull();
    expect(parseTutorBody({ ...validBody, messages: [] })).toBeNull();
    expect(parseTutorBody({ ...validBody, context: { kind: "chat" } })).toBeNull();
  });

  it("rejects conversations not ending on a user turn", () => {
    expect(
      parseTutorBody({
        ...validBody,
        messages: [
          { role: "user", content: "hi" },
          { role: "assistant", content: "hello" },
        ],
      }),
    ).toBeNull();
  });

  it("rejects oversized turns and caps context fields", () => {
    expect(
      parseTutorBody({ ...validBody, messages: [{ role: "user", content: "x".repeat(2001) }] }),
    ).toBeNull();
    const parsed = parseTutorBody({
      ...validBody,
      context: { kind: "lesson", content: "y".repeat(10_000) },
    });
    expect(parsed!.context.content!.length).toBe(6_000);
  });

  it("rejects too many turns", () => {
    const turns = Array.from({ length: 17 }, (_, i) => ({
      role: i % 2 === 0 ? "user" : "assistant",
      content: "m",
    }));
    expect(parseTutorBody({ ...validBody, messages: turns })).toBeNull();
  });
});

describe("buildTutorSystem", () => {
  it("grounds on question context including the student's wrong answer", () => {
    const sys = buildTutorSystem(parseTutorBody(validBody)!.context, "mn");
    expect(sys).toContain("What is $2+2$?");
    expect(sys).toContain("Student's answer: A");
    expect(sys).toContain("Correct answer: B");
    expect(sys).toContain("Монгол хэлээр");
  });

  it("grounds on lesson context and switches language", () => {
    const sys = buildTutorSystem(
      { kind: "lesson", course: "Algebra 2", title: "Vertex form", content: '{"kind":"tapQuestion"}' },
      "en",
    );
    expect(sys).toContain("Vertex form");
    expect(sys).toContain('{"kind":"tapQuestion"}');
    expect(sys).toContain("Reply in English");
    // Safety block always present — students are minors.
    expect(sys).toContain("personal information");
  });
});
