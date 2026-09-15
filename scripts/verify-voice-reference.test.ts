import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// THE VOICE REFERENCE, AND THE TWO WAYS IT COULD QUIETLY STOP MATTERING.
//
// docs/mn-voice-reference.md is derived from 1,047 English sentences printed
// beside their published Mongolian rendering. Terminology has been mechanical
// since mn_terms.py shipped; voice was not, which is how a draft could pass
// every gate and still read as translated.
//
// Two failure modes this pins:
//
//   1. The reference is edited or replaced and the checks in mn_draft_check.py
//      no longer correspond to anything in it.
//   2. Someone deletes a check from mn_draft_check.py and the rule silently
//      reverts to being advice nobody applies.
//
// It does NOT re-derive the corpus counts — those come from the book.

const ROOT = process.cwd();
const REF = path.join(ROOT, "docs/mn-voice-reference.md");
const CHECKER = path.join(ROOT, "scripts/i18n/mn_draft_check.py");

describe("mn voice reference", () => {
  it("ships alongside the glossary it complements", () => {
    expect(fs.existsSync(REF), "docs/mn-voice-reference.md").toBe(true);
  });

  it("still states the rules the draft checker encodes", () => {
    const ref = fs.readFileSync(REF, "utf8");
    // §7 decimal comma / thousands space, §8 hyphenated suffixes, §9 no em
    // dashes, and the оюутан smell test. If a future batch rewrites the file
    // and drops one of these, the matching check in mn_draft_check.py is
    // enforcing a rule its own source no longer makes.
    expect(ref, "§7 — decimal comma").toMatch(/36,27/);
    expect(ref, "§8 — hyphenated case suffix").toMatch(/x-ийн/);
    expect(ref, "§9 — the em dash").toMatch(/em dash/i);
    expect(ref, "smell test — оюутан is a university student").toMatch(/оюутан/);
    expect(ref, "§5 — bare imperative task wording").toMatch(/сурагч/);
  });

  it("keeps those rules mechanical in mn_draft_check.py", () => {
    // The point of the checks is that they run, not that they are written
    // down. A rule removed from here goes back to depending on whoever is
    // drafting remembering it — which is the state this file exists to end.
    const py = fs.readFileSync(CHECKER, "utf8");
    expect(py, "decimal-point check").toContain("DECIMAL_POINT");
    expect(py, "unhyphenated-suffix check").toContain("NO_HYPHEN_SUFFIX");
    expect(py, "em-dash advisory").toContain("EMDASH_SCAFFOLD");
    expect(py, "оюутан check").toContain("STUDENT_WORD");
    expect(py, "checks cite their source").toContain("mn-voice-reference.md");
  });

  it("records that the register question is open, not settled", () => {
    // §5 says task wording is a bare imperative; the standing ruling on this
    // repo is «та» with a polite imperative, and both came from Khas. Ten
    // drafts ride on it. If this note disappears, the next session will pick
    // one silently — which is exactly the drift CLAUDE.md was written to stop.
    const prog = fs.readFileSync(path.join(ROOT, "docs/MONGOLIAN.md"), "utf8");
    expect(prog).toMatch(/register contradiction/i);
    expect(prog.toLowerCase()).toContain("not acted on");
  });
});
