import { describe, it, expect } from "vitest";
import { execFileSync } from "node:child_process";
import path from "node:path";

// THE GLOSSARY GROUNDING CHECKER MUST KEEP DISCRIMINATING.
//
// scripts/i18n/mn_ground.py answers one question for every proposed Mongolian
// term: does it actually occur in the source its provenance label claims —
// ministry order А/492, the established glossary, or the shipped mirrors? The
// owner reads those labels to decide where to spend correction time, so a
// label that overclaims routes them AWAY from the entry that needs them most.
//
// The tool's failure mode is grounding TOO MUCH, and that failure is silent.
// Its first version matched stems as raw substrings against the source text
// and reported all 100 glossary terms as present in the grade 10-12 standard —
// including "tip" and "tree diagram", which are primary-school concepts. It
// passed a smoke test at the time, because the one fabricated control it was
// checked against still came back absent.
//
// So the selftest asserts in BOTH directions: out-of-scope vocabulary must
// come back absent, core upper-secondary vocabulary must come back present,
// and a fabricated string must match nothing. This test runs it, so the check
// is covered by `npx vitest run` — the gate every session already runs —
// rather than living in a script nobody remembers to invoke.

const ROOT = process.cwd();

describe("mn_ground grounding checker", () => {
  it("still tells grounded terms from ungrounded ones", () => {
    let out = "";
    try {
      out = execFileSync(
        "python3",
        [path.join(ROOT, "scripts", "i18n", "mn_ground.py"), "--selftest"],
        { encoding: "utf8", cwd: ROOT },
      );
    } catch (err) {
      const e = err as { stdout?: string; stderr?: string };
      throw new Error(
        `mn_ground selftest failed — the checker no longer discriminates:\n${e.stdout ?? ""}${e.stderr ?? ""}`,
      );
    }
    expect(out).toMatch(/selftest ok/);
  });
});
