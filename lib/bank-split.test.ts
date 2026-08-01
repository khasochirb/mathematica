import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { getBankTopics, getSatBankTopic, getIbBankTopic } from "./bank-data";
import { bankManifest, courseLadderManifest } from "./bank-manifest";

// The bank data/logic split (2026-08-01): lib/bank-data.ts holds the ~9 MB
// corpus and is SERVER-ONLY; client code renders topic lists from the ~55 KB
// manifest. Before the split, lib/problem-bank.ts mixed both, so every
// client page touching bank logic — including the ratings card, i.e. the
// dashboard and the whole /math catalog — shipped a 10 MB chunk. These
// tests are the fence that keeps the corpus from creeping back.

const ROOT = path.resolve(__dirname, "..");
const CORPUS_MODULES = [/@\/lib\/bank-data/, /@\/lib\/placement-course-bank/, /@\/data\/problembank\//];

function walk(dir: string, out: string[] = []): string[] {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "node_modules" || entry.name.startsWith(".")) continue;
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(p, out);
    else if (/\.(ts|tsx)$/.test(entry.name) && !entry.name.endsWith(".test.ts")) out.push(p);
  }
  return out;
}

describe("the corpus stays out of the client bundle", () => {
  it("no client component or page imports a corpus module", () => {
    const offenders: string[] = [];
    for (const dir of ["app", "components"]) {
      for (const file of walk(path.join(ROOT, dir))) {
        const src = fs.readFileSync(file, "utf8");
        // "use client" appears in the directive prologue; server files never
        // carry it. A client file importing the corpus bundles all 16 topics.
        if (!/^\s*["']use client["']/m.test(src.slice(0, 200))) continue;
        if (CORPUS_MODULES.some((re) => re.test(src))) {
          offenders.push(path.relative(ROOT, file));
        }
      }
    }
    expect(offenders, `client files importing the corpus: ${offenders.join(", ")}`).toEqual([]);
  });

  it("client-reachable lib modules do not import the corpus", () => {
    // These modules are (directly or via hooks) in client import graphs.
    // Any of them importing bank-data would drag the corpus into the shared
    // chunk exactly the way lib/problem-bank.ts used to.
    const clientReachable = [
      "lib/problem-bank.ts",
      "lib/bank-manifest.ts",
      "lib/use-ratings.ts",
      "lib/placement-bank.ts",
      "lib/band-placement.ts",
      "lib/use-performance.ts",
    ];
    for (const rel of clientReachable) {
      const src = fs.readFileSync(path.join(ROOT, rel), "utf8");
      for (const re of CORPUS_MODULES) {
        expect(re.test(src), `${rel} matches ${re}`).toBe(false);
      }
    }
  });
});

describe("the manifest mirrors the corpus", () => {
  it("course-ladder entries match getBankTopics() exactly", () => {
    const ladder = courseLadderManifest();
    const topics = getBankTopics();
    expect(ladder.map((t) => t.slug)).toEqual(topics.map((t) => t.slug));
    for (let i = 0; i < topics.length; i++) {
      const m = ladder[i];
      const t = topics[i];
      expect(m.title).toBe(t.title);
      expect(m.unitCount).toBe(t.units.length);
      expect(m.problemCount).toBe(t.forms.reduce((n, f) => n + f.variants.length, 0));
      expect(m.forms.map((f) => f.id)).toEqual(t.forms.map((f) => f.id));
      expect(m.forms.map((f) => f.unit)).toEqual(t.forms.map((f) => f.unit));
      expect(m.forms.map((f) => f.level)).toEqual(t.forms.map((f) => f.level));
    }
  });

  it("hub-owned entries are present and flagged off the ladder", () => {
    const bySlug = new Map(bankManifest().map((t) => [t.slug, t]));
    for (const t of [getSatBankTopic(), getIbBankTopic("sl"), getIbBankTopic("hl")]) {
      const m = bySlug.get(t.slug);
      expect(m, t.slug).toBeTruthy();
      expect(m!.courseLadder).toBe(false);
      expect(m!.forms.map((f) => f.id)).toEqual(t.forms.map((f) => f.id));
    }
  });
});

describe("check[] never leaves the gate", () => {
  it("loaded topics carry no sympy source", () => {
    // The verify gate reads the JSON files directly; at runtime the checks
    // are dead weight in every RSC payload, so the loader strips them.
    const all = [...getBankTopics(), getSatBankTopic(), getIbBankTopic("sl"), getIbBankTopic("hl")];
    for (const t of all) {
      for (const f of t.forms) {
        for (const v of f.variants) {
          expect("check" in v, `${t.slug}/${f.id}/${v.id} still has check[]`).toBe(false);
        }
      }
    }
  });
});
