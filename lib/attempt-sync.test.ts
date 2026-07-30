import { describe, it, expect } from "vitest";
import { reconcileFetchedAttempts } from "./data-erase";

const row = (questionSource: string, timestamp: number, extra: Record<string, unknown> = {}) => ({
  questionSource,
  topic: "algebra",
  subtopic: "",
  selectedAnswer: "A",
  correctAnswer: "A",
  isCorrect: true,
  timestamp,
  ...extra,
});

describe("reconcileFetchedAttempts — the server wins", () => {
  it("drops rows the server no longer has, so a deletion made on another device propagates", () => {
    // The bug this pins: a student erased their data on a laptop (server rows
    // deleted), opened their phone, and the phone's stale cache resurrected
    // everything because the fetch merged the cache back in. The cache is not
    // an input here — after a full erase, empty server means empty state.
    const staleCache = [row("Test-2024A-Q1", 1000), row("Test-2024A-Q2", 2000)];
    void staleCache; // deliberately NOT passed — that is the fix
    expect(reconcileFetchedAttempts([], [])).toEqual([]);
  });

  it("keeps unflushed queue rows and this session's writes — the server cannot know them yet", () => {
    const server = [row("Q1", 1000)];
    const pending = [row("Q2", 2000), row("Q3", 3000)];
    const out = reconcileFetchedAttempts(server, pending);
    expect(out.map((a) => a.questionSource).sort()).toEqual(["Q1", "Q2", "Q3"]);
  });

  it("dedupes when a protected row has already landed server-side", () => {
    // A direct insert that succeeded during the fetch appears in BOTH lists
    // on the next fetch; identity is (questionSource, timestamp).
    const landed = row("Q7", 7000);
    const out = reconcileFetchedAttempts([landed], [landed, row("Q8", 8000)]);
    expect(out).toHaveLength(2);
  });

  it("prefers the server's copy of a duplicated row", () => {
    // Same identity, different payload (e.g. topic reclassified server-side):
    // the server's version is the one kept.
    const serverCopy = row("Q9", 9000, { topic: "linear_algebra" });
    const localCopy = row("Q9", 9000, { topic: "other" });
    const out = reconcileFetchedAttempts([serverCopy], [localCopy]);
    expect(out).toHaveLength(1);
    expect(out[0].topic).toBe("linear_algebra");
  });
});
