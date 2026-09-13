import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// THE SLUG-COLLISION HAZARD IN THE MONGOLIAN MIRROR MAP.
//
// lib/genmath-lessons.ts builds GENMATH_TOPICS_MN by spreading each grade's
// MN map into one object keyed by SLUG ALONE — no grade, no course. That is
// fine while only grades 6/7/8 contribute, because their slugs happen not to
// overlap. It stops being fine the moment a course whose slug already exists
// elsewhere joins the map.
//
// The live example: "quadratic-equations" is BOTH
//   data/genmath/10/quadratic-equations.json           (Grade 10)
//   data/genmath/algebra-1/quadratic-equations.json    (Algebra 1)
// so an Algebra 1 mirror in the global map would serve Algebra 1's Mongolian
// to a Grade 10 student reading Grade 10's English page. Silent, and wrong in
// the direction nobody checks — the page still renders, just with another
// course's lesson in it.
//
// The fix in place is that alg1UnitsMn lives in lib/genmath-data/algebra-1.ts
// and is NOT spread into the aggregator. This test keeps it that way, and
// fails on the next mirror that would reintroduce the collision.
//
// The mn-translation skill states the rule ("the map is slug-keyed and
// grade-agnostic — check before registering"). This is that check.

const ROOT = process.cwd();
const DATA = path.join(ROOT, "data", "genmath");

/** Every EN corpus directory (a grade number or a course name). */
function corpora(): string[] {
  return fs
    .readdirSync(DATA, { withFileTypes: true })
    .filter((e) => e.isDirectory() && !e.name.endsWith("-mn"))
    .map((e) => e.name);
}

/** Slugs that exist in more than one corpus — the collision set. */
function collidingSlugs(): Map<string, string[]> {
  const owners = new Map<string, string[]>();
  for (const c of corpora()) {
    for (const f of fs.readdirSync(path.join(DATA, c))) {
      if (!f.endsWith(".json")) continue;
      const slug = f.replace(/\.json$/, "");
      owners.set(slug, [...(owners.get(slug) ?? []), c]);
    }
  }
  return new Map(Array.from(owners).filter(([, cs]) => cs.length > 1));
}

/** The map names spread into GENMATH_TOPICS_MN in the aggregator. */
function aggregatedMnMaps(): string[] {
  const src = fs.readFileSync(path.join(ROOT, "lib", "genmath-lessons.ts"), "utf8");
  const block = src.match(/GENMATH_TOPICS_MN[^=]*=\s*\{([\s\S]*?)\n\};/);
  if (!block) throw new Error("could not find GENMATH_TOPICS_MN in lib/genmath-lessons.ts");
  return Array.from(block[1].matchAll(/\.\.\.(\w+)/g)).map((m) => m[1]);
}

/** Mirrors registered into the aggregator whose slug exists in >1 corpus. */
function aggregatedCollisions(): string[] {
  const colliding = collidingSlugs();
  const out: string[] = [];
  for (const mapName of aggregatedMnMaps()) {
    const file = fs
      .readdirSync(path.join(ROOT, "lib", "genmath-data"))
      .map((f) => path.join(ROOT, "lib", "genmath-data", f))
      .find((p) => p.endsWith(".ts") && fs.readFileSync(p, "utf8").includes(`export const ${mapName}`));
    if (!file) continue;
    const src = fs.readFileSync(file, "utf8");
    for (const m of Array.from(src.matchAll(/@\/data\/genmath\/[\w-]+-mn\/([\w-]+)\.json/g))) {
      const owners = colliding.get(m[1]);
      if (owners) out.push(`${mapName}: "${m[1]}" also in ${owners.filter((c) => !mapName.includes(c)).join(", ")}`);
    }
  }
  return out.sort();
}

// The collisions that ALREADY existed when this test was written. They are
// latent, not live: nothing calls getGenMathTopicLocalized (the second test
// enforces that), and the grade routes use their own correctly-scoped
// getGradeNTopicLocalized instead. Pinned rather than asserted-empty so the
// hazard cannot grow quietly while the real fix — keying the aggregator by
// corpus+slug — is still outstanding.
const KNOWN_COLLISIONS = [
  'grade6TopicsMn: "data-and-statistics" also in integrated-1',
  'grade6TopicsMn: "percentages" also in sat',
  'grade7TopicsMn: "probability" also in integrated-2',
  'grade8TopicsMn: "linear-equations" also in algebra-1',
  'grade8TopicsMn: "linear-functions" also in algebra-1, integrated-1, sat',
  'grade8TopicsMn: "systems-of-linear-equations" also in sat',
].sort();

describe("Mongolian mirror registration", () => {
  it("does not add new colliding slugs to the aggregator's slug-keyed map", () => {
    const now = aggregatedCollisions();
    const added = now.filter((c) => !KNOWN_COLLISIONS.includes(c));

    expect(
      added,
      "New mirror(s) registered into the grade-agnostic GENMATH_TOPICS_MN map under a slug " +
        `that another corpus also owns:\n${added.join("\n")}\n` +
        "Keep the map course-local (see alg1UnitsMn in lib/genmath-data/algebra-1.ts), " +
        "or key the aggregator by corpus+slug and clear KNOWN_COLLISIONS.",
    ).toEqual([]);

    // If someone fixes the keying, the pinned list should shrink — tell them
    // to update it rather than leaving a stale record of a solved problem.
    const stale = KNOWN_COLLISIONS.filter((c) => !now.includes(c));
    expect(stale, `KNOWN_COLLISIONS is stale — these no longer occur:\n${stale.join("\n")}`).toEqual([]);
  });

  it("keeps the unsafe aggregator getter uncalled while its keying is wrong", () => {
    // getGenMathTopicLocalized resolves through GENMATH_TOPICS_MN, which is
    // keyed by slug with no corpus in the key. With the collisions above
    // present, the FIRST caller starts serving one course's Mongolian on
    // another course's page. Fix the keying before adding a caller.
    const offenders: string[] = [];
    const walk = (dir: string) => {
      for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, e.name);
        if (e.isDirectory()) walk(p);
        else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name)) {
          const rel = path.relative(ROOT, p);
          if (rel === path.join("lib", "genmath-lessons.ts")) continue; // defines it
          if (/getGenMathTopicLocalized\s*\(/.test(fs.readFileSync(p, "utf8"))) offenders.push(rel);
        }
      }
    };
    for (const d of ["app", "components", "lib"]) walk(path.join(ROOT, d));

    expect(
      offenders,
      `these call getGenMathTopicLocalized, which can serve the wrong course's Mongolian:\n${offenders.join("\n")}\n` +
        "Key GENMATH_TOPICS_MN by corpus+slug first, or use the corpus' own localized getter.",
    ).toEqual([]);
  });

  it("has a route that can actually reach every MN mirror on disk", () => {
    // A mirror no code imports is invisible: the pipeline wrote it, the gates
    // pass, and no student ever sees it. algebra-1-mn/quadratic-equations.json
    // sat unreferenced from the day it was generated. Product rule 1 says
    // orphan content is LISTED, never deleted — so this lists it, loudly,
    // instead of letting it rot silently.
    const onDisk: string[] = [];
    for (const d of fs.readdirSync(DATA)) {
      if (!d.endsWith("-mn")) continue;
      for (const f of fs.readdirSync(path.join(DATA, d))) {
        if (f.endsWith(".json")) onDisk.push(`${d}/${f}`);
      }
    }

    const libSrc = fs
      .readdirSync(path.join(ROOT, "lib", "genmath-data"))
      .filter((f) => f.endsWith(".ts"))
      .map((f) => fs.readFileSync(path.join(ROOT, "lib", "genmath-data", f), "utf8"))
      .join("\n");

    const unreferenced = onDisk.filter((rel) => !libSrc.includes(`@/data/genmath/${rel}`));

    expect(
      unreferenced,
      `these Mongolian mirrors exist but nothing imports them — a student cannot reach them:\n${unreferenced.join("\n")}`,
    ).toEqual([]);
  });
});
