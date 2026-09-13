import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { ALL_CHROME } from "../lib/i18n/chrome";

// A THIRD COPY OF THE CHROME VOCABULARY.
//
// Header.tsx carries its own `mathHubs` table with inline `en`/`mn` pairs and
// never calls chrome(). That is reasonable — the table also holds hrefs and a
// `live` flag — but it means the site has a second opinion about what "hub" is
// in Mongolian, and for a while the two disagreed:
//
//   header      «ЭШ төв»     — shipped, live on production since before this work
//   dictionary  «ЭШ хэсэг»   — Claude's coinage, and wrong
//
// Worse, two «хэсэг» entries had been approved and were therefore rendering,
// so production said «SAT Math төв» in the nav and «SAT хэсэг рүү буцах» on a
// page. Found on 13 Sep 2026 by reading the deployed bundle, not the source.
//
// The header is the authority here: its wording predates the dictionary and is
// what students have been reading. This pins the dictionary to it.

const ROOT = process.cwd();
const MN_OF = (en: string) => ALL_CHROME.find((e) => e.en === en)?.mn ?? "";

function headerHubs(): { en: string; mn: string }[] {
  const src = fs.readFileSync(path.join(ROOT, "components/layout/Header.tsx"), "utf8");
  const block = src.slice(src.indexOf("const mathHubs"), src.indexOf("];", src.indexOf("const mathHubs")));
  const out: { en: string; mn: string }[] = [];
  for (const m of Array.from(block.matchAll(/\{\s*en:\s*"([^"]+)",\s*mn:\s*"([^"]+)"/g))) {
    out.push({ en: m[1], mn: m[2] });
  }
  return out;
}

describe("nav labels", () => {
  it("finds the header's hub table", () => {
    const hubs = headerHubs();
    expect(hubs.length, "Header.tsx mathHubs table not parsed — has it moved?").toBeGreaterThanOrEqual(4);
  });

  it("agrees with the chrome dictionary on every hub name", () => {
    const wrong: string[] = [];
    for (const { en, mn } of headerHubs()) {
      const dict = MN_OF(en);
      if (dict && dict !== mn) wrong.push(`${en}: header "${mn}" vs dictionary "${dict}"`);
    }
    expect(wrong, "the nav and the dictionary disagree — the header's wording is the shipped one").toEqual([]);
  });

  it("uses «төв» for a hub, not «хэсэг»", () => {
    // Pinned by value so that changing BOTH copies together still fails. «төв»
    // is what the site shipped; «хэсэг» was the coinage that slipped through.
    for (const { en, mn } of headerHubs()) {
      expect(mn, `${en} should use «төв»`).toContain("төв");
    }
    const strays = ALL_CHROME.filter((e) => /hub/i.test(e.en) && e.mn.includes("хэсэг"));
    expect(strays.map((e) => `${e.en} → ${e.mn}`), "«хэсэг» for a hub contradicts the nav").toEqual([]);
  });
});
