import { describe, it, expect } from "vitest";
import { execFileSync } from "node:child_process";
import path from "node:path";

// THE REWRITE-ERA STRUCTURAL GATE.
//
// docs/MONGOLIAN.md sets the rule: we rewrite, we do not translate. Different
// sentence count, different examples, different order — expected. The old gate
// (scripts/i18n/mn_apply.py) asserts one Mongolian string per English string in
// the same walker slot, so the FIRST rewritten topic fails it, and fails it for
// being correct.
//
// scripts/i18n/mn_skeleton.py replaces that with a structural comparison:
// lesson count, slugs and order; problem ids; interactive step kind sequences;
// tapQuestion option counts and correctIndex; check[] presence. It never
// compares prose.
//
// A structural gate that silently passes is worse than no gate, because it
// certifies rewrites nobody checked. So its selftest mutates a REAL shipped
// mirror in each forbidden way and requires every one to be caught — and, just
// as importantly, exercises five rewrites the rule PERMITS (retitled lesson,
// added paragraph, removed paragraph, worked example with entirely new numbers
// and a new check[], fewer facts) and requires none of them to be flagged. A
// gate that fires on a legitimate rewrite would push authors back toward
// translating, which is the thing this whole programme exists to stop.
//
// Two tests, because they fail for different reasons and want different fixes:
// the selftest failing means the checker is broken; the sweep failing means a
// mirror is.

const ROOT = process.cwd();

function run(args: string[]): string {
  try {
    return execFileSync("python3", [path.join(ROOT, "scripts", "i18n", "mn_skeleton.py"), ...args], {
      encoding: "utf8",
      cwd: ROOT,
      maxBuffer: 16 * 1024 * 1024,
    });
  } catch (err) {
    const e = err as { stdout?: string; stderr?: string };
    throw new Error(`${e.stdout ?? ""}${e.stderr ?? ""}`);
  }
}

describe("mn_skeleton structural gate", () => {
  it("catches every forbidden mutation and permits every legitimate rewrite", () => {
    expect(run(["--selftest"])).toMatch(/selftest ok/);
  });

  it("finds every shipped Mongolian mirror structurally sound", () => {
    // Advisory single-asterisk warnings are expected and do not fail this —
    // they are inherited from the English source, which carries far more of
    // them (1,032 strings against 36). See split_severity() for why.
    expect(run(["--all"])).toMatch(/structurally sound/);
  });
});
