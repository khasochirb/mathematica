import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// WHO MAY CHANGE THE READER'S LANGUAGE.
//
// Language is global and PERSISTED (localStorage `mp_lang`), so a page that
// sets it does not just restyle itself — it changes the header, the
// dashboard and every lesson, for the rest of that reader's life on the site.
//
// This shipped: /tutoring is the Facebook-ad landing page, so it defaulted to
// Mongolian whenever `mp_lang` was unset. But English is the site DEFAULT, so
// a reader browsing happily in English has never written `mp_lang` either —
// which meant clicking "1-on-1 Tutoring" in the nav flipped the entire site
// to Mongolian for someone who never asked, signed in or not.
//
// The ad behaviour is deliberate and stays. The guard is that it may only
// fire for a reader who is actually ad traffic.

const ROOT = process.cwd();

// Files allowed to call setLang, and why.
const ALLOWED = new Map([
  ["lib/lang-context.tsx", "defines it"],
  ["components/layout/Header.tsx", "the EN/MN toggle — the reader's own choice"],
  ["app/tutoring/page.tsx", "ad landing page; must satisfy the guards below"],
]);

function sourceFiles(): string[] {
  const out: string[] = [];
  const walk = (dir: string) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name)) out.push(p);
    }
  };
  for (const d of ["app", "components", "lib"]) walk(path.join(ROOT, d));
  return out;
}

describe("global language auto-switching", () => {
  it("is confined to the files allowed to do it", () => {
    const offenders: string[] = [];
    for (const file of sourceFiles()) {
      const rel = path.relative(ROOT, file);
      if (ALLOWED.has(rel)) continue;
      const src = fs.readFileSync(file, "utf8");
      // A call, not a destructure or a type.
      if (/\bsetLang\s*\(/.test(src)) offenders.push(rel);
    }
    expect(
      offenders,
      `these change the reader's language without being allowed to:\n${offenders.join("\n")}\n` +
        `If a new landing page genuinely needs this, add it here WITH the same guards.`,
    ).toEqual([]);
  });

  it("keeps every guard on the tutoring page's Mongolian default", () => {
    const src = fs.readFileSync(path.join(ROOT, "app/tutoring/page.tsx"), "utf8");
    // Each guard rules out a reader who is not ad traffic. Dropping any one of
    // them reopens the bug for a different group of people.
    const guards: [string, RegExp, string][] = [
      ["saved language wins", /localStorage\.getItem\("mp_lang"\)/, "an explicit choice must never be overridden"],
      ["signed-in readers exempt", /if\s*\(\s*isAuthenticated\s*\)\s*return/, "an existing account is not a new ad click"],
      ["must be an off-site landing", /landedFromOffSite\(/, "in-site navigation must never switch the language"],
      ["waits for auth", /if\s*\(\s*loading\s*\)\s*return/, "deciding before auth resolves treats everyone as anonymous"],
    ];
    const missing = guards.filter(([, re]) => !re.test(src)).map(([name, , why]) => `${name} — ${why}`);
    expect(missing, `tutoring page lost a guard:\n${missing.join("\n")}`).toEqual([]);
  });

  it("does not decide the language from document.referrer alone", () => {
    // The App Router does not update document.referrer across a client-side
    // navigation, so after clicking a nav link it still describes the PREVIOUS
    // page and an in-site click reads as external. This is exactly the trap
    // the first attempt at this fix fell into.
    // Comments stripped: the page's own comment explains this trap, and
    // documenting a hazard must not read as committing it.
    const code = fs
      .readFileSync(path.join(ROOT, "app/tutoring/page.tsx"), "utf8")
      .replace(/\/\*[\s\S]*?\*\//g, "")
      .replace(/^\s*\/\/.*$/gm, "");
    expect(
      /document\.referrer/.test(code),
      "use landedFromOffSite() (which also checks the path the document loaded at), not document.referrer",
    ).toBe(false);
  });
});
