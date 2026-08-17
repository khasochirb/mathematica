// The contract with the model. Two halves matter: nothing malformed reaches
// the API (parseDiagnosticBody), and nothing the model invented reaches a
// student (parseDecision). The second is the load-bearing one — a model that
// hallucinates a question id must not be able to put an unverified problem in
// front of a child.
import { describe, it, expect } from "vitest";
import {
  parseDiagnosticBody,
  parseDecision,
  buildDiagnosticSystem,
  buildDiagnosticUser,
  DIAGNOSTIC_TOOL,
} from "./diagnostic-prompt";

const body = {
  lang: "en",
  course: "Grade 11",
  topics: ["Logarithms", "Sequences"],
  transcript: [
    {
      topic: "Logarithms",
      difficulty: 2,
      prompt: "Solve $\\log_2 x = 3$.",
      chose: "$6$",
      correctAnswer: "$8$",
      correct: false,
    },
  ],
  candidates: [
    { id: "logarithms:d1", topic: "Logarithms", difficulty: 1, prompt: "$\\log_2 8$?" },
    { id: "sequences:d2", topic: "Sequences", difficulty: 2, prompt: "Next term?" },
  ],
  finalReport: false,
};

describe("parseDiagnosticBody", () => {
  it("accepts a valid body", () => {
    const p = parseDiagnosticBody(body);
    expect(p).not.toBeNull();
    expect(p!.course).toBe("Grade 11");
    expect(p!.candidates).toHaveLength(2);
    expect(p!.finalReport).toBe(false);
  });

  it("rejects garbage shapes", () => {
    expect(parseDiagnosticBody(null)).toBeNull();
    expect(parseDiagnosticBody("x")).toBeNull();
    expect(parseDiagnosticBody({})).toBeNull();
    expect(parseDiagnosticBody({ ...body, lang: "fr" })).toBeNull();
    expect(parseDiagnosticBody({ ...body, course: "" })).toBeNull();
    expect(parseDiagnosticBody({ ...body, topics: [] })).toBeNull();
    expect(parseDiagnosticBody({ ...body, transcript: [] })).toBeNull();
  });

  it("rejects a transcript entry missing its evidence", () => {
    // `chose` is the whole diagnostic signal — a turn without it is useless.
    const t = { ...body.transcript[0], chose: "" };
    expect(parseDiagnosticBody({ ...body, transcript: [t] })).toBeNull();
  });

  it("rejects out-of-range difficulty", () => {
    expect(
      parseDiagnosticBody({ ...body, transcript: [{ ...body.transcript[0], difficulty: 9 }] }),
    ).toBeNull();
    expect(
      parseDiagnosticBody({ ...body, candidates: [{ ...body.candidates[0], difficulty: 0 }] }),
    ).toBeNull();
  });

  it("rejects duplicate candidate ids — the reply would be ambiguous", () => {
    expect(
      parseDiagnosticBody({ ...body, candidates: [body.candidates[0], body.candidates[0]] }),
    ).toBeNull();
  });

  it("rejects an empty menu on a non-final step, allows it on the report", () => {
    expect(parseDiagnosticBody({ ...body, candidates: [] })).toBeNull();
    expect(parseDiagnosticBody({ ...body, candidates: [], finalReport: true })).not.toBeNull();
  });

  it("caps oversized text instead of trusting it", () => {
    const p = parseDiagnosticBody({
      ...body,
      transcript: [{ ...body.transcript[0], prompt: "x".repeat(5_000) }],
    });
    expect(p!.transcript[0].prompt.length).toBe(600);
  });

  it("rejects an oversized transcript or menu outright", () => {
    const many = Array.from({ length: 25 }, () => body.transcript[0]);
    expect(parseDiagnosticBody({ ...body, transcript: many })).toBeNull();
    const menu = Array.from({ length: 9 }, (_, i) => ({ ...body.candidates[0], id: `q${i}` }));
    expect(parseDiagnosticBody({ ...body, candidates: menu })).toBeNull();
  });
});

describe("parseDecision", () => {
  const parsed = parseDiagnosticBody(body)!;

  it("keeps a decision that stays inside the menu", () => {
    const d = parseDecision(
      {
        hypothesis: "reads $\\log_2 x = 3$ as $2 \\times 3$",
        hypothesis_topic: "Logarithms",
        next_question_id: "logarithms:d1",
        narrative: null,
      },
      parsed,
    );
    expect(d.nextQuestionId).toBe("logarithms:d1");
    expect(d.hypothesisTopic).toBe("Logarithms");
    expect(d.hypothesis).toContain("log_2");
  });

  it("DROPS an id the model invented", () => {
    const d = parseDecision(
      { hypothesis: null, hypothesis_topic: null, next_question_id: "made:up", narrative: null },
      parsed,
    );
    // Null is the caller's signal to use the deterministic pick — the student
    // gets a real bank question either way.
    expect(d.nextQuestionId).toBeNull();
  });

  it("drops a topic outside the course, and the orphaned hypothesis with it", () => {
    const d = parseDecision(
      { hypothesis: "something", hypothesis_topic: "Astrology", next_question_id: null, narrative: null },
      parsed,
    );
    expect(d.hypothesisTopic).toBeNull();
    expect(d.hypothesis).toBe("something");
  });

  it("ignores a narrative on a non-final step", () => {
    const d = parseDecision(
      { hypothesis: null, hypothesis_topic: null, next_question_id: null, narrative: "Well done!" },
      parsed,
    );
    expect(d.narrative).toBeNull();
  });

  it("takes the narrative and refuses a question on the final step", () => {
    const final = parseDiagnosticBody({ ...body, candidates: [], finalReport: true })!;
    const d = parseDecision(
      {
        hypothesis: "drops the base",
        hypothesis_topic: "Logarithms",
        next_question_id: "logarithms:d1",
        narrative: "Start with logarithms.",
      },
      final,
    );
    expect(d.narrative).toBe("Start with logarithms.");
    expect(d.nextQuestionId).toBeNull();
  });

  it("survives junk from the model", () => {
    expect(parseDecision(null, parsed).nextQuestionId).toBeNull();
    expect(parseDecision("nope", parsed).hypothesis).toBeNull();
    expect(parseDecision({ next_question_id: 42 }, parsed).nextQuestionId).toBeNull();
  });
});

describe("the prompt", () => {
  const parsed = parseDiagnosticBody(body)!;

  it("tells the model to read the chosen distractor, not the score", () => {
    const sys = buildDiagnosticSystem(parsed);
    expect(sys).toContain("WHICH option they picked");
    expect(sys).toContain("record_diagnosis");
    // Students are minors — the framing has to survive prompt edits.
    expect(sys).toContain("children and teenagers");
  });

  it("carries no student identity — only math", () => {
    const text = buildDiagnosticSystem(parsed) + buildDiagnosticUser(parsed);
    for (const leak of ["email", "user id", "userId", "@"]) {
      expect(text.toLowerCase()).not.toContain(leak.toLowerCase());
    }
  });

  it("shows the wrong choice AND the right answer for every miss", () => {
    const user = buildDiagnosticUser(parsed);
    expect(user).toContain("they chose: $6$");
    expect(user).toContain("correct answer: $8$");
    expect(user).toContain("id: logarithms:d1");
  });

  it("hides the menu and asks for the report on the final step", () => {
    const final = parseDiagnosticBody({ ...body, candidates: [], finalReport: true })!;
    const user = buildDiagnosticUser(final);
    expect(user).toContain("This sitting is over");
    expect(user).not.toContain("QUESTIONS YOU MAY ASK NEXT");
  });

  it("switches the student-facing half to Mongolian without moving the notation", () => {
    const mn = buildDiagnosticSystem({ ...parsed, lang: "mn" });
    expect(mn).toContain("Mongolian");
    expect(mn).toContain("mathematical notation universal");
  });

  it("forces every field of the tool so a partial reply cannot slip through", () => {
    expect(DIAGNOSTIC_TOOL.input_schema.required).toEqual([
      "hypothesis",
      "hypothesis_topic",
      "next_question_id",
      "narrative",
    ]);
    expect(DIAGNOSTIC_TOOL.input_schema.additionalProperties).toBe(false);
  });
});
