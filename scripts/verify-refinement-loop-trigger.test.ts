// Phase 3d — §3a auto-trigger picker (pickAutoTriggerSkill).

import { describe, it, expect } from "vitest";
import { pickAutoTriggerSkill, type GradedResult } from "@/lib/refinement-loop";

function g(source: string, skillTag: string | null, correct: boolean): GradedResult {
  return { source, skillTag, correct };
}

describe("pickAutoTriggerSkill (§3a: missRate ≥ 0.5 AND misses ≥ 2)", () => {
  it("returns null when no skill clears the bar (strong test)", () => {
    expect(pickAutoTriggerSkill([g("q1", "algebra_a", false), g("q2", "algebra_a", true), g("q3", "geo", true)])).toBeNull();
  });

  it("requires at least 2 misses even at 100% miss rate", () => {
    // one tag, 1/1 missed → missRate 1.0 but only 1 miss → not eligible
    expect(pickAutoTriggerSkill([g("q1", "solo", false)])).toBeNull();
  });

  it("fires on an eligible skill and enters on its first missed question", () => {
    const t = pickAutoTriggerSkill([
      g("q1", "quad", true),
      g("q2", "quad", false),
      g("q3", "quad", false), // quad: 2/3 missed = 0.67 ≥ 0.5, misses 2 ✓
      g("q4", "geo", true),
    ]);
    expect(t).not.toBeNull();
    expect(t!.skillTag).toBe("quad");
    expect(t!.triggerQuestion).toBe("q2"); // first missed of quad
    expect(t!.misses).toBe(2);
    expect(t!.total).toBe(3);
  });

  it("picks the highest miss-rate among eligible skills", () => {
    const t = pickAutoTriggerSkill([
      // A: 2/4 = 0.50 (eligible, boundary)
      g("a1", "A", false), g("a2", "A", false), g("a3", "A", true), g("a4", "A", true),
      // B: 3/4 = 0.75 (eligible, higher)
      g("b1", "B", false), g("b2", "B", false), g("b3", "B", false), g("b4", "B", true),
    ]);
    expect(t!.skillTag).toBe("B");
  });

  it("breaks ties on absolute miss count", () => {
    const t = pickAutoTriggerSkill([
      // A: 2/2 = 1.0, misses 2
      g("a1", "A", false), g("a2", "A", false),
      // B: 3/3 = 1.0, misses 3 → wins the tie
      g("b1", "B", false), g("b2", "B", false), g("b3", "B", false),
    ]);
    expect(t!.skillTag).toBe("B");
    expect(t!.misses).toBe(3);
  });

  it("includes the 50% boundary as eligible", () => {
    const t = pickAutoTriggerSkill([g("q1", "x", false), g("q2", "x", false), g("q3", "x", true), g("q4", "x", true)]);
    expect(t).not.toBeNull();
    expect(t!.missRate).toBe(0.5);
  });

  it("ignores untagged questions", () => {
    expect(pickAutoTriggerSkill([g("q1", null, false), g("q2", null, false), g("q3", null, false)])).toBeNull();
  });
});
