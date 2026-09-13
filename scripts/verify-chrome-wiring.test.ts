import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { ALL_CHROME, chrome, untranslated, isApproved, gatedLookup } from "../lib/i18n/chrome";

// GROUP 1 — THE CHROME DICTIONARY AND ITS WIRING.
//
// 173 of 218 pages ignored the language toggle entirely. lib/i18n/chrome.ts is
// the dictionary they read from, and this pins the three things that would
// silently undo it.
//
// docs/MONGOLIAN.md: "Never deploy unreviewed Mongolian. Once I've approved a
// batch, deploy it freely." As of 13 Sep 2026 that is enforced rather than
// observed — `chrome()` consults an approved-only map on production builds,
// and the tests below pin both halves: that the approval predicate admits
// only somebody else's judgement, and that nothing outside it reaches a
// reader. The approved batch ships; my wording waits.

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

  it("keeps the placement card's inline label equal to the dictionary's", () => {
    // The focus label is the one approved string rendered inline rather than
    // through chrome(), because live unit names sit bold inside the same
    // line. That is seven copies of a string Khas wrote — exactly the drift
    // the dictionary exists to prevent — so they are checked instead.
    const label = MN_OF("Focus first on");
    expect(label, "the dictionary entry itself").toBe("Түрүүнд анхаарах зүйлс:");

    const wrong: string[] = [];
    let found = 0;
    for (const file of sourceFiles(["app"])) {
      const src = fs.readFileSync(file, "utf8");
      if (!src.includes("Focus first on")) continue;
      // A page is wired if it carries the label; an un-wired course hub has
      // no Mongolian on it at all and is not a failure here.
      if (!/useLang|const mn =/.test(src)) continue;
      found++;
      if (!src.includes(label)) wrong.push(path.relative(ROOT, file));
    }
    expect(wrong, "these render the focus line but not the approved label").toEqual([]);
    expect(found, "the seven grade hubs render this line").toBe(7);
  });

  it("counts as approved only what somebody other than Claude decided", () => {
    // This predicate is what production ships. Widening it is how unreviewed
    // Mongolian would reach students, so the four qualifying routes are
    // pinned: Khas approved the exact string, it came verbatim from the live
    // site, the ministry/glossary fixes it, or Khas wrote it.
    for (const e of ALL_CHROME) {
      if (!isApproved(e)) continue;
      const why = e.ok || e.src === "SITE" || e.src === "GLOSS" || e.src === "VOICE";
      expect(why, `"${e.en}" is treated as approved but nobody approved it`).toBeTruthy();
    }
    // A NEW/DERIV entry without `ok` is Claude's own wording and must not ship.
    const mine = ALL_CHROME.filter(
      (e) => (e.src === "NEW" || e.src === "DERIV") && !e.ok && isApproved(e),
    );
    expect(mine.map((e) => e.en), "these are Claude's wording and unreviewed").toEqual([]);
  });

  it("leaves the gate open in dev and tests, so wording stays reviewable", () => {
    // vitest runs with NODE_ENV !== "production", the same state as local
    // `next dev`. The gate must be off here or working on the wording would
    // mean working blind.
    expect(process.env.NODE_ENV).not.toBe("production");
    const unapproved = ALL_CHROME.find((e) => !isApproved(e) && e.mn);
    expect(unapproved, "fixture: expected at least one unapproved entry").toBeTruthy();
    expect(chrome(unapproved!.en, "mn")).toBe(unapproved!.mn);
  });

  it("renders no unapproved wording once the gate is closed", () => {
    // The claim every Mongolian deploy rests on, checked against the gated
    // lookup itself rather than trusting the predicate.
    //
    // Note what this does NOT claim: the unapproved strings are still present
    // in the JS bundle, because ALL_CHROME is one array and bundlers do not
    // tree-shake data. They are never rendered, which is what the rule is
    // about — and the repository is public anyway, so stripping them from the
    // payload would buy nothing.
    //
    // A key differing only by case resolves through its twin, and the twin
    // carries identical Mongolian (pinned by the case-drift test above), so
    // an approved string surfacing that way is correct, not a leak.
    const approvedStrings = new Set(ALL_CHROME.filter(isApproved).map((e) => e.mn));
    const leaked: string[] = [];
    for (const e of ALL_CHROME) {
      if (isApproved(e) || !e.mn) continue;
      const out = gatedLookup(e.en);
      if (out !== e.en && !approvedStrings.has(out)) leaked.push(`${e.en} -> ${out}`);
    }
    expect(leaked, "unreviewed Mongolian would reach a student").toEqual([]);
  });

  it("closes the gate on an unknown environment rather than opening it", () => {
    // The failure this guards against is silent: if the gate keyed off a
    // variable that went missing, it would read false, open, and ship
    // unreviewed Mongolian to students. So the condition must be "production
    // build AND nobody asked for drafts" — never "environment equals
    // preview". This asserts the source spells it that way, because the
    // behaviour itself cannot be observed from inside a test run (NODE_ENV is
    // fixed at "test" here).
    const src = fs.readFileSync(path.join(ROOT, "lib/i18n/chrome.ts"), "utf8");
    const line = src.split("\n").find((l) => l.includes("GATE_TO_APPROVED ="));
    expect(line, "GATE_TO_APPROVED must exist").toBeTruthy();
    const decl = src.slice(src.indexOf("const GATE_TO_APPROVED"), src.indexOf("const MN_APPROVED"));
    expect(decl).toContain('process.env.NODE_ENV === "production"');
    expect(decl).toContain("NEXT_PUBLIC_MN_SHOW_DRAFTS");
    // An equality test against a named non-production environment would mean
    // an absent variable opens the gate.
    expect(decl).not.toMatch(/VERCEL_ENV\s*===\s*"production"/);
  });

  it("never stamps an approval on an empty string", () => {
    // `ok` is the record that Khas read a specific Mongolian string and
    // approved it, and it is what makes an entry deployable. Stamping one
    // with no `mn` would claim a review of nothing — and since `chrome()`
    // falls back to English, the page would ship English under an approval.
    const empty = ALL_CHROME.filter((e) => e.ok && !e.mn).map((e) => e.en);
    expect(empty, "these are marked approved but have no Mongolian").toEqual([]);
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
