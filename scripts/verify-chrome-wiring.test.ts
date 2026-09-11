import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { ALL_CHROME, chrome, untranslated } from "../lib/i18n/chrome";

// GROUP 1 — THE CHROME DICTIONARY AND ITS WIRING.
//
// 173 of 218 pages ignored the language toggle entirely. lib/i18n/chrome.ts is
// the dictionary they read from, and this pins the three things that would
// silently undo it.
//
// NOTHING HERE HAS SHIPPED. Wiring lives on the branch so the wording is
// reviewable in place on the preview URL — a table of 91 strings cannot show
// how a label reads inside its own page. docs/MONGOLIAN.md's "never deploy
// unreviewed Mongolian" still binds, and the last test below is what keeps
// that honest.

const ROOT = process.cwd();

const MN_OF = (en: string) => ALL_CHROME.find((e) => e.en === en)?.mn ?? "";

function sourceFiles(dirs: string[]): string[] {
  const out: string[] = [];
  const walk = (dir: string) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name)) out.push(p);
    }
  };
  for (const d of dirs) walk(path.join(ROOT, d));
  return out;
}

describe("chrome dictionary", () => {
  it("falls back to English rather than rendering a blank", () => {
    // A page that silently loses its labels is harder to notice than one that
    // is half-translated, and this dictionary is deliberately incomplete while
    // the voice strings are outstanding.
    expect(chrome("Lessons", "en")).toBe("Lessons");
    expect(chrome("a string nobody has translated", "mn")).toBe("a string nobody has translated");
    expect(chrome("Lessons", "mn")).not.toBe("Lessons");
  });

  it("never returns an empty string for an entry Khas has not written yet", () => {
    const empties = untranslated().map((e) => e.en);
    for (const en of empties) {
      expect(chrome(en, "mn"), `"${en}" is unwritten and must fall through to English`).toBe(en);
    }
    // Every empty entry must be a VOICE one. An empty NEW entry is a mistake:
    // it means a proposal was deleted rather than corrected.
    const wrongKind = untranslated().filter((e) => e.src !== "VOICE");
    expect(
      wrongKind.map((e) => `${e.en} (${e.src})`),
      "only VOICE entries may be empty — Khas writes those and Claude never drafts them",
    ).toEqual([]);
  });

  it("has no duplicate English keys", () => {
    const seen = new Map<string, number>();
    for (const e of ALL_CHROME) seen.set(e.en, (seen.get(e.en) ?? 0) + 1);
    const dupes = Array.from(seen).filter(([, n]) => n > 1).map(([en]) => en);
    expect(dupes, "a duplicate key makes which Mongolian wins depend on array order").toEqual([]);
  });

  it("is never called with a composed string", () => {
    // Mongolian suffixes agree with what they attach to, so an interpolated
    // string cannot be looked up — `chrome(\`Unit ${n}\`, lang)` would miss the
    // map and silently render English forever. The two sites that genuinely
    // need a function instead are in memory/mn-group1-audits.md §2.
    const offenders: string[] = [];
    for (const file of sourceFiles(["app", "components", "lib"])) {
      const src = fs.readFileSync(file, "utf8");
      for (const m of Array.from(src.matchAll(/chrome\(\s*([`"'])/g))) {
        if (m[1] === "`") offenders.push(path.relative(ROOT, file));
      }
    }
    expect(
      Array.from(new Set(offenders)),
      "chrome() takes a literal English key, never a template literal",
    ).toEqual([]);
  });

  it("has no two keys differing only by case", () => {
    // chrome() is an exact-match lookup, so "Practice by Topic" and "Practice
    // by topic" are two different entries that can drift apart in wording. Two
    // Mongolian labels for one English label is the thing this dictionary
    // exists to prevent.
    const byLower = new Map<string, string[]>();
    for (const e of ALL_CHROME) {
      const k = e.en.toLowerCase();
      byLower.set(k, [...(byLower.get(k) ?? []), e.en]);
    }
    const drifted = Array.from(byLower.values())
      .filter((v) => v.length > 1)
      .filter((v) => new Set(v.map((en) => MN_OF(en))).size > 1);
    expect(
      drifted,
      "these keys differ only by case AND have different Mongolian — pick one wording",
    ).toEqual([]);
  });

  it("resolves a key whose casing differs from the dictionary's", () => {
    // Pages write the same label with different capitalisation, so chrome()
    // falls back to a case-insensitive lookup. Without it each mismatch
    // renders English and is indistinguishable from an un-wired page.
    expect(chrome("practice by topic", "mn")).toBe(chrome("Practice by Topic", "mn"));
    expect(chrome("SAT MATH COURSE", "mn")).toBe(chrome("SAT Math course", "mn"));
    expect(chrome("practice by topic", "mn")).not.toBe("practice by topic");
  });

  it("only wires keys the dictionary actually has", () => {
    // A typo'd key renders English forever and looks like an un-wired page,
    // which is the one failure this whole batch is meant to remove.
    const keys = new Set(ALL_CHROME.map((e) => e.en));
    const missing: string[] = [];
    for (const file of sourceFiles(["app", "components", "lib"])) {
      const src = fs.readFileSync(file, "utf8");
      for (const m of Array.from(src.matchAll(/chrome\(\s*"((?:[^"\\]|\\.)*)"/g))) {
        if (!keys.has(m[1])) missing.push(`${path.relative(ROOT, file)}: "${m[1]}"`);
      }
    }
    expect(missing, "these call chrome() with a key that is not in the dictionary").toEqual([]);
  });
});
