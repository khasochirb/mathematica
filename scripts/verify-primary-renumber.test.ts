// The primary band moved onto the ministry's grade labels on 2026-08-13
// (/math/3 -> /math/2, /math/4 -> /math/3, /math/5 -> /math/4). Renaming a
// live URL space is the kind of change that silently strands every saved
// link, so the redirect map is generated from the spines and asserted here:
// every moved topic must be redirected, the destination must be a topic that
// really exists at the new grade, and a redirect must never shadow a URL
// that is live TODAY.
import { describe, it, expect } from "vitest";
import { GRADE2_SPINE, GRADE3_SPINE, GRADE4_SPINE } from "@/lib/genmath-spines";
import map from "@/data/primary/renumber-redirects.json";

const NEW_SLUGS: Record<number, string[]> = {
  2: GRADE2_SPINE.map((t) => t.slug),
  3: GRADE3_SPINE.map((t) => t.slug),
  4: GRADE4_SPINE.map((t) => t.slug),
};
// old grade N taught what new grade N-1 teaches now
const SHIFT: Record<number, number> = { 3: 2, 4: 3, 5: 4 };

describe("primary-band renumber redirects", () => {
  const rules = map.redirects;

  it("redirects every moved topic, at every old grade", () => {
    for (const [oldStr, newGrade] of Object.entries(SHIFT)) {
      const oldGrade = Number(oldStr);
      const liveToday = new Set(NEW_SLUGS[oldGrade] ?? []);
      for (const slug of NEW_SLUGS[newGrade]) {
        const source = `/math/${oldGrade}/${slug}/:rest*`;
        const rule = rules.find((r) => r.source === source);
        if (liveToday.has(slug)) {
          // a live URL must NOT be redirected away from its own content
          expect(rule, `${source} shadows a live grade-${oldGrade} unit`).toBeUndefined();
          expect(map.collisions.some((c) => c.slug === slug && c.oldGrade === oldGrade)).toBe(true);
          continue;
        }
        expect(rule, `no redirect for moved topic ${source}`).toBeTruthy();
        expect(rule!.destination).toBe(`/math/${newGrade}/${slug}/:rest*`);
        expect(rule!.permanent).toBe(true);
      }
    }
  });

  it("sends every destination to a topic that actually exists", () => {
    for (const r of rules) {
      const m = /^\/math\/(\d+)(?:\/([a-z0-9-]+))?/.exec(r.destination);
      expect(m, `undecodable destination ${r.destination}`).toBeTruthy();
      const grade = Number(m![1]);
      expect(NEW_SLUGS[grade], `destination grade ${grade} is not a live primary grade`).toBeTruthy();
      if (m![2]) {
        expect(NEW_SLUGS[grade], `${r.destination} names no real topic`).toContain(m![2]);
      }
    }
  });

  it("never redirects a URL that is live today", () => {
    for (const r of rules) {
      const m = /^\/math\/(\d+)\/([a-z0-9-]+)/.exec(r.source);
      if (!m) continue;
      const grade = Number(m[1]);
      if (!NEW_SLUGS[grade]) continue; // that grade number no longer resolves
      expect(NEW_SLUGS[grade], `${r.source} would shadow a live URL`).not.toContain(m[2]);
    }
  });

  it("records the one collision it cannot redirect, and only that one", () => {
    // old grade 4 and old grade 5 both had an `addition-and-subtraction`
    // unit, so /math/4/addition-and-subtraction is a live new-grade-4 URL
    // AND an old-grade-4 bookmark. The live URL wins; the old bookmark
    // lands on harder content. Nothing else in the band collides.
    expect(map.collisions).toHaveLength(1);
    expect(map.collisions[0].slug).toBe("addition-and-subtraction");
    expect(map.collisions[0].oldGrade).toBe(4);
  });

  it("sends the orphaned grade index somewhere real, as a temporary rule", () => {
    // /math/5 no longer resolves (grade 5 is unauthored), so the old index
    // points at where its content went — a TEMPORARY 302, to be deleted the
    // day a real grade 5 ships.
    const bare = rules.find((r) => r.source === "/math/5");
    expect(bare).toBeTruthy();
    expect(bare!.destination).toBe("/math/4");
    expect(bare!.permanent).toBe(false);
    // grades that still resolve keep their own index
    expect(rules.some((r) => r.source === "/math/3" || r.source === "/math/4")).toBe(false);
  });
});
