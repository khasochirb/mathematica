import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  HUBS,
  HUB_TAB_LABELS,
  HUB_TAB_ORDER,
  activeHubTab,
  hidesHubChrome,
  hubTabs,
  type HubKey,
} from "./hub-tabs";
import { UNPUBLISHED_PREFIXES, isUnpublished, publishedOnly } from "./unpublished";

// 01-ARCHITECTURE.md rules 3, 4 and 7, as tests. They are the three that
// erode quietly: a hub adds "just one" tab, a route sneaks back into
// navigation, an unpublished area keeps a link in from a live page.

describe("rule 3 — the five-tab contract", () => {
  it("is exactly Plan · Learn · Practice · Tests · Progress, in that order", () => {
    expect([...HUB_TAB_ORDER]).toEqual(["plan", "learn", "practice", "tests", "progress"]);
  });

  it("every hub declares all five and nothing else", () => {
    for (const [hub, spec] of Object.entries(HUBS)) {
      expect(Object.keys(spec.tabs).sort(), `${hub} tab set`).toEqual([...HUB_TAB_ORDER].sort());
    }
  });

  it("every hub renders its tabs in contract order", () => {
    for (const hub of Object.keys(HUBS) as HubKey[]) {
      const rendered = hubTabs(hub).map((t) => t.key);
      const expected = HUB_TAB_ORDER.filter((k) => rendered.includes(k));
      expect(rendered, `${hub} order`).toEqual([...expected]);
    }
  });

  it("every live tab points inside its own hub", () => {
    for (const [hub, spec] of Object.entries(HUBS)) {
      for (const t of hubTabs(hub as HubKey)) {
        expect(t.href.startsWith(spec.base), `${hub}/${t.key} → ${t.href}`).toBe(true);
      }
    }
  });

  it("every tab has both labels", () => {
    for (const k of HUB_TAB_ORDER) {
      expect(HUB_TAB_LABELS[k].en.length).toBeGreaterThan(0);
      expect(HUB_TAB_LABELS[k].mn.length).toBeGreaterThan(0);
    }
  });

  it("rule 7 — an unbuilt tab is declared but never rendered", () => {
    // Plan does not exist yet on either hub. It stays in the contract and out
    // of the nav bar until it has content.
    expect(HUBS.eysh.tabs.plan).toBeNull();
    expect(hubTabs("eysh").map((t) => t.key)).not.toContain("plan");
  });

  it("resolves the active tab by longest match, and nothing for non-tab routes", () => {
    expect(activeHubTab("eysh", "/practice/esh/test")).toBe("tests");
    expect(activeHubTab("eysh", "/practice/esh/test/2025a?session=x")).toBe("tests");
    expect(activeHubTab("eysh", "/practice/esh/progress")).toBe("progress");
    // `loop` and `topics` are real routes but not tabs — they highlight none.
    expect(activeHubTab("eysh", "/practice/esh/loop")).toBeNull();
    expect(activeHubTab("eysh", "/practice/esh/topics")).toBeNull();
    expect(activeHubTab("eysh", "/practice/esh")).toBeNull();
  });

  it("hides hub chrome inside a running test, and nowhere else", () => {
    expect(hidesHubChrome("/practice/esh/test/2025a")).toBe(true);
    expect(hidesHubChrome("/practice/esh/test/2025a?session=abc")).toBe(true);
    expect(hidesHubChrome("/practice/esh/test")).toBe(false); // the Tests landing
    expect(hidesHubChrome("/practice/esh")).toBe(false);
    expect(hidesHubChrome("/practice/esh/practice")).toBe(false);
  });
});

describe("unpublished routes", () => {
  it("matches on path boundaries, never on a prefix of a longer segment", () => {
    expect(isUnpublished("/math/6")).toBe(true);
    expect(isUnpublished("/math/6/fractions")).toBe(true);
    expect(isUnpublished("/math/6/")).toBe(true);
    expect(isUnpublished("/practice/ib/bank/sl")).toBe(true);
    // The renumbered primary band is NOT unpublished; /math/60 is not /math/6.
    expect(isUnpublished("/math/60")).toBe(false);
    expect(isUnpublished("/math/9")).toBe(false);
    expect(isUnpublished("/practice/esh")).toBe(false);
    expect(isUnpublished("/practice/sat/bank")).toBe(false);
    expect(isUnpublished("https://example.com/math/6")).toBe(false);
  });

  it("covers IB, AP, the standalone courses and grades 6–7", () => {
    for (const p of ["/practice/ib", "/practice/ap", "/math/6", "/math/7", "/math/algebra-1", "/math/geometry"]) {
      expect(UNPUBLISHED_PREFIXES).toContain(p);
    }
    // Grades that Phase 0 keeps.
    for (const p of ["/math/8", "/math/9", "/math/10", "/math/11", "/math/12"]) {
      expect(UNPUBLISHED_PREFIXES).not.toContain(p);
    }
  });

  it("filters nav lists", () => {
    expect(
      publishedOnly([{ href: "/practice/esh" }, { href: "/practice/ib" }, { href: "/math/7" }]),
    ).toEqual([{ href: "/practice/esh" }]);
  });

  it("noindex is served for every unpublished prefix", () => {
    // next.config.mjs builds the X-Robots-Tag rules off the same JSON, so the
    // header set can never drift from the list the app filters on.
    const cfg = fs.readFileSync(path.join(process.cwd(), "next.config.mjs"), "utf8");
    expect(cfg).toMatch(/unpublished-routes\.json/);
    expect(cfg).toMatch(/X-Robots-Tag/);
    expect(cfg).toMatch(/noindex/);
  });
});

describe("rule 7 — nothing unpublished stays in navigation", () => {
  it("no live page or component links into an unpublished area", () => {
    // The scan that stops the cut half-reverting: a live file linking to
    // /practice/ib or /math/geometry puts it back in navigation whatever the
    // nav component says.
    const roots = ["app", "components"].map((d) => path.join(process.cwd(), d));
    const offenders: string[] = [];

    const walk = (dir: string) => {
      for (const d of fs.readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, d.name);
        if (d.isDirectory()) {
          walk(p);
          continue;
        }
        if (!/\.tsx?$/.test(d.name)) continue;
        const rel = path.relative(process.cwd(), p);
        // Files INSIDE an unpublished area may link within it.
        const routePath = "/" + rel.replace(/^app/, "").replace(/^\/+/, "").replace(/\/page\.tsx?$/, "");
        if (isUnpublished(routePath)) continue;

        const src = fs.readFileSync(p, "utf8");
        // A file that imports the policy has APPLIED it — its catalog list
        // may still name unpublished hrefs because it filters them through
        // publishedOnly()/isUnpublished() before rendering. What this scan is
        // for is the file that links into an unpublished area having never
        // heard of the policy at all.
        if (src.includes('from "@/lib/unpublished"')) continue;
        // Both spellings: the JSX attribute and the object property that
        // nav/catalog lists use. Template literals with interpolation are out
        // of reach of a regex, but those only ever appear INSIDE the area
        // they link to, which the routePath check above already skips.
        const patterns = [/href=["'`](\/[^"'`\s${}]*)["'`]/g, /href:\s*["'`](\/[^"'`\s${}]*)["'`]/g];
        for (const re of patterns) {
          for (const m of Array.from(src.matchAll(re))) {
            if (isUnpublished(m[1])) offenders.push(`${rel} → ${m[1]}`);
          }
        }
      }
    };
    roots.forEach(walk);

    expect(
      offenders,
      `live files still linking into unpublished areas:\n${offenders.join("\n")}`,
    ).toEqual([]);
  });
});
