// Phase 3d §5 — recently-mastered suppression.

import { describe, it, expect } from "vitest";
import { recentlyMasteredTopics, partitionWeakTopics, type CompletedLoopLite } from "@/lib/refinement-loop-analytics";

const NOW = Date.parse("2026-06-16T00:00:00.000Z");
const daysAgo = (n: number) => new Date(NOW - n * 86_400_000).toISOString();

describe("recentlyMasteredTopics (§5, 14-day window)", () => {
  it("includes a topic mastered within the window", () => {
    const loops: CompletedLoopLite[] = [{ topic: "algebra", exitReason: "mastered", completedAt: daysAgo(3) }];
    expect(recentlyMasteredTopics(loops, NOW).has("algebra")).toBe(true);
  });
  it("excludes a mastery older than the window", () => {
    const loops: CompletedLoopLite[] = [{ topic: "algebra", exitReason: "mastered", completedAt: daysAgo(20) }];
    expect(recentlyMasteredTopics(loops, NOW).has("algebra")).toBe(false);
  });
  it("includes the 14-day boundary", () => {
    const loops: CompletedLoopLite[] = [{ topic: "geo", exitReason: "mastered", completedAt: daysAgo(14) }];
    expect(recentlyMasteredTopics(loops, NOW).has("geo")).toBe(true);
  });
  it("ignores non-mastered exits and null timestamps", () => {
    const loops: CompletedLoopLite[] = [
      { topic: "x", exitReason: "abandoned", completedAt: daysAgo(1) },
      { topic: "y", exitReason: "student_skipped", completedAt: daysAgo(1) },
      { topic: "z", exitReason: "mastered", completedAt: null },
    ];
    const set = recentlyMasteredTopics(loops, NOW);
    expect(set.size).toBe(0);
  });
  it("respects a custom window", () => {
    const loops: CompletedLoopLite[] = [{ topic: "t", exitReason: "mastered", completedAt: daysAgo(5) }];
    expect(recentlyMasteredTopics(loops, NOW, 3).has("t")).toBe(false);
    expect(recentlyMasteredTopics(loops, NOW, 7).has("t")).toBe(true);
  });
});

describe("partitionWeakTopics", () => {
  it("splits weak topics by the mastered set, preserving order", () => {
    const weak = [{ topic: "a", accuracy: 40 }, { topic: "b", accuracy: 50 }, { topic: "c", accuracy: 60 }];
    const { visible, recentlyMastered } = partitionWeakTopics(weak, new Set(["b"]));
    expect(visible.map((w) => w.topic)).toEqual(["a", "c"]);
    expect(recentlyMastered.map((w) => w.topic)).toEqual(["b"]);
  });
  it("returns all visible when nothing mastered", () => {
    const weak = [{ topic: "a" }, { topic: "b" }];
    expect(partitionWeakTopics(weak, new Set()).visible).toHaveLength(2);
  });
});
