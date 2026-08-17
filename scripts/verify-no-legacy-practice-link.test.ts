// Nothing may link to /practice. The page is gone.
//
// /practice was the pre-hub practice landing — one page, ЭШ-only, behind a
// sign-in wall — superseded by the four hubs but never unwired. It stayed the
// destination of the home page's PRIMARY calls to action: "Take a diagnostic"
// (twice), "Start practicing", and "Next problem →" in the AI-tutor demo. The
// most valuable clicks on the site landed on the most stale page on it, and
// for a signed-out visitor that meant a sign-in wall instead of the product.
//
// The route now 302s to /practice/esh so external links survive, which is
// exactly why this test is needed: a stale href no longer 404s, so nothing
// would ever surface it again. A redirect hides the mistake instead of
// reporting it.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

const ROOTS = ["app", "components", "lib"];
const EXT = new Set([".ts", ".tsx"]);

function walk(dir: string, out: string[] = []): string[] {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "node_modules" || entry.name === ".next") continue;
      walk(full, out);
    } else if (EXT.has(path.extname(entry.name))) {
      out.push(full);
    }
  }
  return out;
}

describe("the legacy /practice landing stays gone", () => {
  it("has no page file", () => {
    expect(fs.existsSync(path.join(process.cwd(), "app", "practice", "page.tsx"))).toBe(false);
  });

  it("no source file links to /practice", () => {
    // Bare "/practice" only. The hubs (/practice/esh, /practice/sat, …) and the
    // per-unit course runners (/math/9/<topic>/practice) are untouched.
    const bare = /["'`]\/practice["'`]/;
    const offenders: string[] = [];
    for (const root of ROOTS) {
      for (const file of walk(path.join(process.cwd(), root))) {
        // Tests are not rendered links. lib/ratings.test.ts asserts
        // href.startsWith("/practice"), which is a prefix check covering every
        // hub and is correct as written.
        if (/\.test\.tsx?$/.test(file)) continue;
        const src = fs.readFileSync(file, "utf-8");
        src.split("\n").forEach((line, i) => {
          if (bare.test(line)) offenders.push(`${path.relative(process.cwd(), file)}:${i + 1}`);
        });
      }
    }
    expect(offenders, "these still point at the removed /practice landing").toEqual([]);
  });

  it("/practice still resolves, so old external links do not break", () => {
    // Removing the page without this would 404 every bookmark and every link
    // shared before today.
    const cfg = fs.readFileSync(path.join(process.cwd(), "next.config.mjs"), "utf-8");
    expect(cfg).toMatch(/source:\s*"\/practice"/);
    // 302, not 301: making it permanent would be very hard to take back if
    // /practice ever becomes a real hub chooser.
    expect(cfg).toMatch(/source:\s*"\/practice",\s*destination:\s*"\/practice\/esh",\s*permanent:\s*false/);
  });

  it("/ai no longer forwards into the removed page", () => {
    const cfg = fs.readFileSync(path.join(process.cwd(), "next.config.mjs"), "utf-8");
    expect(cfg).not.toMatch(/destination:\s*"\/practice"/);
  });
});
