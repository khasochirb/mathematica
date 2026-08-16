// Every primary topic page must link to ITS OWN problem-bank course key.
//
// The regression this exists for: the 2026-08-13 renumber moved the routes
// (/math/3 -> /math/2, /math/4 -> /math/3, /math/5 -> /math/4) and retargeted
// the bank generators to match, but left the "Problem bank" button on each
// topic page pointing at the OLD key. Result, shipped to production:
//
//   /math/2/<topic>  ->  /math/problem-bank/3/<topic>   24 of 25 hard 404
//   /math/3/<topic>  ->  /math/problem-bank/4/<topic>
//   /math/4/<topic>  ->  /math/problem-bank/5/<topic>
//
// and one link that was WORSE than a 404: `addition-and-subtraction` names a
// unit in both grade 3 and grade 4, so /math/3/addition-and-subtraction
// returned 200 and quietly served the wrong year's problems. That slug
// collision is the same one recorded as unredirectable in the renumber commit.
//
// It went unnoticed because the only gate that walks links — verify:links —
// had itself been disabled by the primary-band withdrawal (its soft-404
// canary lived on /math/5). Two failures in the same band, each hiding the
// other. This test needs no server, so it cannot be disabled the same way.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

const PRIMARY_GRADES = ["2", "3", "4"];

describe("primary topic pages link to their own problem bank", () => {
  it.each(PRIMARY_GRADES)("grade %s links to problem-bank/%s", (grade) => {
    const file = path.join(process.cwd(), "app", "math", grade, "[topic]", "page.tsx");
    const src = fs.readFileSync(file, "utf-8");
    // exec loop rather than spreading matchAll: this repo's tsconfig target
    // does not allow iterating a RegExpStringIterator.
    const links: string[] = [];
    const re = /\/math\/problem-bank\/(\d+)\//g;
    for (let m = re.exec(src); m !== null; m = re.exec(src)) links.push(m[1]);
    expect(links.length, `${file} has no problem-bank link`).toBeGreaterThan(0);
    for (const key of links) {
      expect(key, `${file} links to problem-bank/${key}, not its own grade`).toBe(grade);
    }
  });

  it("every linked bank course actually has a unit for each of its topics", () => {
    // The 404s were only visible with a server running. This checks the same
    // thing against the shipped bank data, so it holds in CI.
    //
    // One bank JSON per course, keyed by the course slug; the units live
    // inside it. The route 404s when the unit slug is not among them, which
    // is exactly what 24 of the 25 links were doing.
    const missing: string[] = [];
    for (const grade of PRIMARY_GRADES) {
      const bankFile = path.join(process.cwd(), "data", "problembank", `${grade}.json`);
      if (!fs.existsSync(bankFile)) {
        missing.push(`bank course "${grade}" has no data/problembank/${grade}.json`);
        continue;
      }
      const bank = JSON.parse(fs.readFileSync(bankFile, "utf-8"));
      const units: string[] = (bank.units ?? bank.forms ?? []).map(
        (u: { slug?: string; unit?: string; id?: string }) => u.slug ?? u.unit ?? u.id ?? "",
      );
      const topics = fs
        .readdirSync(path.join(process.cwd(), "data", "genmath", grade))
        .filter((f) => f.endsWith(".json"))
        .map((f) => f.replace(/\.json$/, ""));
      for (const topic of topics) {
        if (!units.includes(topic)) {
          missing.push(`grade ${grade}: bank has no unit "${topic}"`);
        }
      }
    }
    expect(missing, "primary topics whose problem bank unit is missing").toEqual([]);
  });
});
