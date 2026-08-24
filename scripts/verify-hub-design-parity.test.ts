// Every hub is the same design, and the same thing wears the same icon.
//
// The hubs already shared components/hub/HubKit.tsx, so this looked done.
// It was not: each hub passed its own `icon` per card, and they drifted
// into contradicting each other —
//
//   BookOpen  = "course"      on ЭШ and IB, but "foundations" on SAT
//   Target    = "drill"       on ЭШ, while SAT and IB used Layers
//   Sparkles  = "SAT course", used nowhere else on the site
//
// A student moving from the ЭШ hub to the SAT hub was shown the same
// glyph for two different destinations, and two glyphs for the same one.
// Sharing a component is not the same as sharing a design.
//
// The fix is structural: a card declares a ROLE and the kit owns the
// icon, so there is nowhere left to put a one-off. These tests hold that
// shut, and hold the two pages that were off the kit entirely onto it.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

const read = (p: string) => fs.readFileSync(path.join(process.cwd(), p), "utf-8");

const KIT = read("components/hub/HubKit.tsx");
const HUBS = {
  "ЭШ": read("app/practice/esh/page.tsx"),
  SAT: read("app/practice/sat/page.tsx"),
  IB: read("app/practice/ib/page.tsx"),
};
const MATH = read("app/math/page.tsx");

describe("icons belong to the role, not to the hub", () => {
  it("the kit owns one icon per role", () => {
    expect(KIT).toContain("export const HUB_ROLE_ICON");
    for (const role of ["tests", "past-papers", "course", "drill", "foundations", "progress"]) {
      expect(KIT, `${role} has no icon`).toMatch(
        new RegExp(`["']?${role}["']?:\\s*\\w+,`),
      );
    }
  });

  it("a card declares what it IS, and cannot carry its own icon", () => {
    const def = KIT.slice(KIT.indexOf("export interface HubActionCardDef"));
    const body = def.slice(0, def.indexOf("}"));
    expect(body).toContain("role: HubCardRole");
    // Match a FIELD named icon, not the word in the doc comment above it.
    expect(body, "an `icon` escape hatch reopens the drift").not.toMatch(/^\s*icon\??:/m);
  });

  it("the grid resolves the icon from the role", () => {
    expect(KIT).toContain("HUB_ROLE_ICON[c.role]");
  });

  it("the progress banner cannot differ between hubs", () => {
    // All three used to pass the same BarChart3 by hand — a convention
    // held up by nothing but three people remembering.
    const banner = KIT.slice(KIT.indexOf("export function HubProgressBanner"));
    const sig = banner.slice(0, banner.indexOf("}) {"));
    expect(sig, "banner still takes an icon prop").not.toMatch(/\bicon\b/);
    expect(banner).toContain("HUB_ROLE_ICON.progress");
  });

  it("no hub passes an icon to the kit any more", () => {
    for (const [name, src] of Object.entries(HUBS)) {
      expect(src, `${name} still sets icon:`).not.toMatch(/^\s*icon:/m);
      expect(src, `${name} still sets icon={}`).not.toMatch(/icon=\{/);
    }
  });

  it("every hub card declares a role the kit knows", () => {
    const roles = new Set(["tests", "past-papers", "course", "drill", "foundations", "progress"]);
    let seen = 0;
    for (const [name, src] of Object.entries(HUBS)) {
      // exec loop rather than [...matchAll]: this repo's tsconfig targets
      // below es2015, where spreading an iterator needs downlevelIteration.
      const found: string[] = [];
      const re = /role:\s*"([^"]+)"/g;
      let m: RegExpExecArray | null;
      while ((m = re.exec(src)) !== null) found.push(m[1]);
      expect(found.length, `${name} declares no card roles`).toBeGreaterThan(0);
      for (const r of found) expect(roles, `${name} uses unknown role ${r}`).toContain(r);
      seen += found.length;
    }
    expect(seen, "expected 12 cards across the three hubs").toBe(12);
  });
});

describe("every hub is built from the kit", () => {
  it("the three exam hubs use the same four primitives in the same order", () => {
    for (const [name, src] of Object.entries(HUBS)) {
      const order = ["HubShell", "HubHeader", "HubProgressBanner", "HubActionGrid"];
      let at = -1;
      for (const prim of order) {
        const i = src.indexOf(`<${prim}`);
        expect(i, `${name} does not render ${prim}`).toBeGreaterThan(-1);
        expect(i, `${name} renders ${prim} out of order`).toBeGreaterThan(at);
        at = i;
      }
    }
  });

  it("/math is on the shell too, not a hand-copy of it", () => {
    // It used to reproduce HubShell's markup with pt-12 pb-16 instead of
    // the kit's py-8, and its own <h1> at a different size.
    expect(MATH).toContain("<HubShell>");
    expect(MATH).toContain("<HubHeader");
    expect(MATH, "still hand-rolling the shell").not.toContain('className="min-h-screen pt-20"');
    expect(MATH, "still hand-rolling the inner container").not.toContain(
      "max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16",
    );
  });

  it("every hub route renders the shell rather than reproducing it", () => {
    // Scoped to the hub routes on purpose. `min-h-screen pt-20` is the
    // site-wide "sit below the fixed header" idiom used by ~20 pages —
    // asserting the kit is its only user would be asserting something
    // false. What matters is that a HUB gets its frame from the kit.
    const hubRoutes = [
      "app/practice/esh/page.tsx",
      "app/practice/sat/page.tsx",
      "app/practice/ib/page.tsx",
      "app/math/page.tsx",
    ];
    for (const r of hubRoutes) {
      expect(read(r), `${r} does not use HubShell`).toContain("<HubShell>");
    }
  });

  it("the one hub route still off the kit is AP, and it is a coming-soon page", () => {
    // /practice/ap renders ComingSoonHub — a centred marketing page with
    // a waitlist form, not a hub surface. Recorded here rather than left
    // as an unexplained inconsistency: when AP gets real content it
    // should join the kit, and this test should then be tightened.
    const ap = read("app/practice/ap/page.tsx");
    expect(ap).toContain("ComingSoonHub");
    expect(ap).not.toContain("HubShell");
  });
});

describe("every exam hub wears the five-tab bar", () => {
  // THE MISS. The first pass at "make the hubs identical" compared icons
  // and card grids and declared victory. The owner opened them on a phone
  // and saw it immediately: ЭШ had the tab bar and SAT and IB had none.
  //
  // lib/hub-tabs.ts had declared SAT's tabs since the contract was written
  // — but no layout mounted them, and IB was not in HubKey at all. A spec
  // nothing renders looks exactly like a spec that does, from the source.
  // These tests check the mounting, not the declaration.
  const HUB_KEYS: Record<string, string> = {
    "app/practice/esh/layout.tsx": "eysh",
    "app/practice/sat/layout.tsx": "sat",
    "app/practice/ib/layout.tsx": "ib",
  };

  it("each exam hub has a layout that mounts HubTabs for its own key", () => {
    for (const [file, key] of Object.entries(HUB_KEYS)) {
      const src = read(file);
      expect(src, `${file} does not mount HubTabs`).toContain("<HubTabs");
      expect(src, `${file} mounts the wrong hub key`).toContain(`hub="${key}"`);
      // A running test is a timed exam and gets no navigation out of it.
      expect(src, `${file} does not hide chrome inside a test`).toContain("hidesHubChrome");
    }
  });

  it("all three render the SAME tabs, not merely some tabs", () => {
    // Mounting the bar on a hub whose landings do not exist would give
    // 4 tabs on ЭШ, 3 on SAT and 2 on IB — visibly still not identical,
    // which is the state this replaces.
    const spec = read("lib/hub-tabs.ts");
    for (const key of ["eysh", "sat", "ib"]) {
      expect(spec, `${key} is not in the hub table`).toMatch(
        new RegExp(`^\\s*${key}:\\s*\\{`, "m"),
      );
    }
    const live = ["learn", "practice", "tests", "progress"];
    const blocks = spec.split(/^  (?=\w+: \{$)/m).filter((b) => /^(eysh|sat|ib):/.test(b));
    expect(blocks.length, "expected three hub blocks").toBe(3);
    for (const b of blocks) {
      const name = b.slice(0, b.indexOf(":"));
      for (const tab of live) {
        expect(b, `${name} has no live ${tab} tab`).toMatch(
          new RegExp(`${tab}: "/practice/`),
        );
      }
      // Plan is the one piece nobody has built. Null everywhere, so the
      // hubs are equal in what they lack too.
      expect(b, `${name} should not fake a Plan tab`).toMatch(/plan: null/);
    }
  });

  it("every tab destination is a real page", () => {
    const spec = read("lib/hub-tabs.ts");
    const re = /"(\/practice\/[a-z]+\/[a-z]+)"/g;
    let m: RegExpExecArray | null;
    const missing: string[] = [];
    while ((m = re.exec(spec)) !== null) {
      const route = m[1];
      const file = path.join(process.cwd(), "app", route, "page.tsx");
      if (!fs.existsSync(file)) missing.push(route);
    }
    // A tab pointing at a route with no page.tsx is the dead-link class
    // lib/link-integrity.test.ts caught once before.
    expect(missing, "tab destinations without a page").toEqual([]);
  });
});

describe("the hubs agree on the small things too", () => {
  it("no hub reintroduces the italic-plus-colour double highlight", () => {
    for (const [name, src] of Object.entries(HUBS)) {
      expect(src, `${name} uses serif-italic`).not.toContain("serif-italic");
    }
    expect(MATH).not.toContain("serif-italic");
  });

  it("the kit still declares the ЭШ hub as the reference design", () => {
    // Direction matters: SAT and IB were built to match ЭШ, never the
    // reverse. Losing this comment is how a future edit flattens the
    // richest hub to fit the simplest one.
    expect(KIT).toMatch(/REFERENCE/);
  });
});
