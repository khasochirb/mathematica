// The diagnostic placement's policy, held mechanically. Two properties matter
// more than any single case here and are asserted over the REAL banks at the
// bottom: a sitting always terminates, and it never places a student later
// than the earliest topic they failed. Both are silent failures if they break
// — the test still "works", it just places students wrong.
import { describe, it, expect } from "vitest";
import type { PlacementQuestion } from "@/lib/placement-bank";
import {
  getPlacementBank, // Grade 6, the default
  getGrade11PlacementBank,
  getGeometryPlacementBank,
} from "@/lib/placement-bank";
import {
  initDiagnostic,
  recordAnswer,
  addNote,
  topicVerdict,
  startPoint,
  focusTopic,
  targetDifficulty,
  candidateQuestions,
  deterministicNext,
  stopCheck,
  buildReport,
  toPlacementResult,
  canConsultAi,
  spendAiCall,
  MIN_QUESTIONS,
  MAX_QUESTIONS,
  AI_CALL_BUDGET,
  type DiagnosticState,
} from "@/lib/diagnostic-engine";

// A tiny synthetic bank: three topics in course order, three tiers each.
const q = (topic: string, d: 1 | 2 | 3): PlacementQuestion => ({
  id: `${topic}:d${d}`,
  topicSlug: topic,
  topicTitle: topic.toUpperCase(),
  difficulty: d,
  prompt: `${topic} ${d}`,
  options: ["right", "wrongA", "wrongB", "wrongC"],
  correctIndex: 0,
  explanation: "",
});
const BANK: PlacementQuestion[] = ["alpha", "beta", "gamma"].flatMap((t) =>
  ([1, 2, 3] as const).map((d) => q(t, d)),
);
const find = (id: string) => BANK.find((x) => x.id === id)!;
/** Answer a question by id: 0 is correct, 1 is a wrong option. */
const ans = (s: DiagnosticState, id: string, correct: boolean) =>
  recordAnswer(s, find(id), correct ? 0 : 1);

describe("evidence, not a score", () => {
  it("records WHICH option the student chose, not just correctness", () => {
    const s = ans(initDiagnostic(BANK), "alpha:d2", false);
    const a = s.answers[0];
    expect(a.correct).toBe(false);
    // The whole point of the rewrite: the distractor text survives into state,
    // because that is the only thing that identifies the misconception.
    expect(a.chosenText).toBe("wrongA");
    expect(a.correctText).toBe("right");
    expect(a.prompt).toBe("alpha 2");
  });
});

describe("topic verdicts", () => {
  it("settles a topic in ONE question at the extremes", () => {
    expect(topicVerdict(ans(initDiagnostic(BANK), "alpha:d3", true), "alpha")).toBe("solid");
    expect(topicVerdict(ans(initDiagnostic(BANK), "alpha:d1", false), "alpha")).toBe("weak");
  });

  it("refuses to settle on one middling answer", () => {
    expect(topicVerdict(ans(initDiagnostic(BANK), "alpha:d2", true), "alpha")).toBe("unknown");
    expect(topicVerdict(ans(initDiagnostic(BANK), "alpha:d2", false), "alpha")).toBe("unknown");
  });

  it("refuses to settle on contradictory extremes", () => {
    // Failed the easy one AND cleared the hard one: a student we have not
    // understood. Resolving either way here would be a coin flip.
    let s = ans(initDiagnostic(BANK), "alpha:d1", false);
    s = ans(s, "alpha:d3", true);
    expect(topicVerdict(s, "alpha")).toBe("unknown");
  });

  it("uses accuracy once there are two answers", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d2", false);
    s = ans(s, "beta:d2", true); // unrelated topic, must not leak
    expect(topicVerdict(s, "alpha")).toBe("unknown");
  });
});

describe("the start point", () => {
  it("is unresolved while an earlier topic is still unknown", () => {
    const s = ans(initDiagnostic(BANK), "gamma:d1", false);
    // gamma is weak, but alpha and beta were never asked — the answer could
    // still move earlier, so it is NOT a placement yet.
    expect(startPoint(s)).toEqual({ slug: "alpha", resolved: false });
  });

  it("resolves at the earliest weak topic once everything before it is solid", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d3", true); // solid
    s = ans(s, "beta:d1", false); // weak
    expect(startPoint(s)).toEqual({ slug: "beta", resolved: true });
  });

  it("resolves to null when every topic is solid", () => {
    let s = initDiagnostic(BANK);
    for (const t of ["alpha", "beta", "gamma"]) s = ans(s, `${t}:d3`, true);
    expect(startPoint(s)).toEqual({ slug: null, resolved: true });
    expect(focusTopic(s)).toBeNull();
  });
});

describe("choosing the next problem", () => {
  it("opens a new topic HARD for a student who has been clearing everything", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d2", true);
    s = ans(s, "alpha:d3", true);
    expect(targetDifficulty(s, "beta")).toBe(3);
  });

  it("opens a new topic EASY for a student who has been missing", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d2", false);
    s = ans(s, "alpha:d1", false);
    expect(targetDifficulty(s, "beta")).toBe(1);
  });

  it("steps down inside a topic after a miss — the 'suitable problem'", () => {
    const s = ans(initDiagnostic(BANK), "alpha:d3", false);
    expect(targetDifficulty(s, "alpha")).toBe(2);
    expect(deterministicNext(s, BANK)!.id).toBe("alpha:d2");
  });

  it("offers a menu spanning easier, harder and move-on", () => {
    const s = ans(initDiagnostic(BANK), "alpha:d2", false);
    const menu = candidateQuestions(s, BANK, 6);
    expect(menu.length).toBeGreaterThanOrEqual(3);
    // Never re-offers a question already asked.
    expect(menu.some((c) => c.id === "alpha:d2")).toBe(false);
    // Both a same-topic rung and a different topic are reachable.
    expect(menu.some((c) => c.topicSlug === "alpha")).toBe(true);
    expect(menu.some((c) => c.topicSlug !== "alpha")).toBe(true);
  });

  it("is deterministic for a given seed and varies across seeds", () => {
    const a = candidateQuestions(initDiagnostic(BANK, 1), BANK, 6).map((c) => c.id);
    const b = candidateQuestions(initDiagnostic(BANK, 1), BANK, 6).map((c) => c.id);
    expect(a).toEqual(b);
  });
});

describe("stopping", () => {
  it("does not stop before the floor even when the answer is obvious", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d1", false);
    expect(startPoint(s).resolved).toBe(true); // located already...
    expect(stopCheck(s, BANK).stop).toBe(false); // ...but too early to be credible
    // Fill up to the floor with unrelated evidence.
    s = ans(s, "beta:d2", true);
    s = ans(s, "beta:d3", true);
    s = ans(s, "gamma:d2", true);
    s = ans(s, "gamma:d3", true);
    expect(s.answers.length).toBe(MIN_QUESTIONS);
    expect(stopCheck(s, BANK)).toEqual({ stop: true, reason: "located" });
  });

  it("stops when the bank runs out", () => {
    let s = initDiagnostic(BANK);
    for (const b of BANK) s = recordAnswer(s, b, 0);
    expect(stopCheck(s, BANK)).toEqual({ stop: true, reason: "exhausted" });
  });

  it("never runs past the cap on a real bank", () => {
    // Worst case: a student whose answers alternate, so no topic ever settles
    // by the extremes. The sitting must still end.
    const bank = getGrade11PlacementBank();
    let s = initDiagnostic(bank, 7);
    let asked = 0;
    for (;;) {
      const next = deterministicNext(s, bank);
      if (!next) break;
      s = recordAnswer(s, next, asked % 2 === 0 ? next.correctIndex : (next.correctIndex + 1) % 4);
      asked += 1;
      expect(asked).toBeLessThanOrEqual(MAX_QUESTIONS);
    }
    expect(stopCheck(s, bank).stop).toBe(true);
  });
});

describe("the report", () => {
  it("carries the start point, the findings and the stop reason", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d3", true);
    s = ans(s, "beta:d1", false);
    s = addNote(s, "beta", "adds denominators");
    s = spendAiCall(s);
    const r = buildReport(s, BANK, { narrative: "Start with beta." });
    expect(r.startSlug).toBe("beta");
    expect(r.startTitle).toBe("BETA");
    expect(r.priorityTopics).toEqual(["beta"]);
    expect(r.findings).toEqual([{ topicSlug: "beta", hypothesis: "adds denominators" }]);
    expect(r.narrative).toBe("Start with beta.");
    expect(r.aiAssisted).toBe(true);
  });

  it("keeps the newest hypothesis per topic", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d1", false);
    s = addNote(s, "alpha", "first read");
    s = addNote(s, "alpha", "better read");
    expect(buildReport(s, BANK).findings).toEqual([{ topicSlug: "alpha", hypothesis: "better read" }]);
  });

  it("says aiAssisted:false when no model ran", () => {
    const r = buildReport(ans(initDiagnostic(BANK), "alpha:d1", false), BANK);
    expect(r.aiAssisted).toBe(false);
    expect(r.narrative).toBeNull();
  });

  it("converts to the stored shape every existing reader already understands", () => {
    let s = ans(initDiagnostic(BANK), "alpha:d3", true);
    s = ans(s, "beta:d1", false);
    const res = toPlacementResult(buildReport(s, BANK));
    expect(res.version).toBe(1);
    expect(res.level).toBeTypeOf("string");
    expect(res.topicScores.map((t) => t.slug)).toEqual(["alpha", "beta", "gamma"]);
    // Unseen topics report seen:0 rather than a fabricated zero score.
    expect(res.topicScores.find((t) => t.slug === "gamma")!.seen).toBe(0);
    expect(res.priorityTopics).toEqual(["beta"]);
    expect(res.diagnosis!.startSlug).toBe("beta");
  });
});

describe("the AI call budget", () => {
  it("runs out after AI_CALL_BUDGET consults", () => {
    let s = initDiagnostic(BANK);
    for (let i = 0; i < AI_CALL_BUDGET; i++) {
      expect(canConsultAi(s)).toBe(true);
      s = spendAiCall(s);
    }
    expect(canConsultAi(s)).toBe(false);
  });
});

describe("over the real placement banks", () => {
  const banks: [string, PlacementQuestion[]][] = [
    ["grade6", getPlacementBank()],
    ["grade11", getGrade11PlacementBank()],
    ["geometry", getGeometryPlacementBank()],
  ];

  it.each(banks)("%s: a perfect student is placed at no topic, inside the cap", (_name, bank) => {
    let s = initDiagnostic(bank, 3);
    for (;;) {
      const next = deterministicNext(s, bank);
      if (!next) break;
      s = recordAnswer(s, next, next.correctIndex);
    }
    expect(s.answers.length).toBeLessThanOrEqual(MAX_QUESTIONS);
    expect(startPoint(s).slug).toBeNull();
    expect(buildReport(s, bank).priorityTopics).toEqual([]);
  });

  it.each(banks)("%s: a student who fails everything is placed at the FIRST topic", (_name, bank) => {
    let s = initDiagnostic(bank, 3);
    for (;;) {
      const next = deterministicNext(s, bank);
      if (!next) break;
      s = recordAnswer(s, next, (next.correctIndex + 1) % next.options.length);
    }
    const first = s.topics[0].slug;
    expect(startPoint(s)).toEqual({ slug: first, resolved: true });
    // ...and it took few questions to say so. Locating a floor should not
    // require marching a struggling child through the whole course.
    expect(s.answers.length).toBeLessThanOrEqual(MIN_QUESTIONS + 3);
  });

  it.each(banks)("%s: a student solid until topic 3 is placed AT topic 3", (_name, bank) => {
    const topics = initDiagnostic(bank).topics.map((t) => t.slug);
    const target = topics[2];
    let s = initDiagnostic(bank, 5);
    for (;;) {
      const next = deterministicNext(s, bank);
      if (!next) break;
      const idx = topics.indexOf(next.topicSlug);
      const correct = idx < 2; // solid on the first two topics, then not
      s = recordAnswer(s, next, correct ? next.correctIndex : (next.correctIndex + 1) % next.options.length);
    }
    expect(startPoint(s)).toEqual({ slug: target, resolved: true });
  });
});
