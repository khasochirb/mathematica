import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  GRADE6_SPINE,
  GRADE7_SPINE,
  GRADE8_SPINE,
  GRADE9_SPINE,
  GRADE10_SPINE,
  GRADE11_SPINE,
  GRADE12_SPINE,
} from "./genmath-spines";
import {
  getGrade6Topics,
  getGrade7Topics,
  getGrade8Topics,
  getGrade9Topics,
  getGrade10Topics,
  getGrade11Topics,
  getGrade12Topics,
} from "./genmath-lessons";

// The genmath data/spine split (2026-08-01): lib/genmath-spines.ts carries
// the light structural metadata (pure literals), lib/genmath-lessons.ts the
// ~14 MB corpus. The ratings taxonomy, placement title maps, the /math
// catalog and the dashboard now read spines/props only — these tests keep
// the corpus from creeping back into their client graphs, and keep the
// spines truthful about the data they stand in for.

const ROOT = path.resolve(__dirname, "..");

describe("grade spines mirror the registry", () => {
  const pairs: [string, { slug: string; title: string; live: boolean }[], () => { slug: string; title: string; status?: string }[]][] = [
    ["6", GRADE6_SPINE, getGrade6Topics],
    ["7", GRADE7_SPINE, getGrade7Topics],
    ["8", GRADE8_SPINE, getGrade8Topics],
    ["9", GRADE9_SPINE, getGrade9Topics],
    ["10", GRADE10_SPINE, getGrade10Topics],
    ["11", GRADE11_SPINE, getGrade11Topics],
    ["12", GRADE12_SPINE, getGrade12Topics],
  ];

  it("live spine entries equal the non-placeholder topics, in order", () => {
    // lib/ratings.ts builds the rated-unit spine from the SPINES; before the
    // split it used the topic lists. This is the equivalence that makes the
    // swap behavior-identical — a topic wired without flipping its spine
    // entry live (or vice versa) breaks ratings coverage and fails here.
    for (const [grade, spine, topics] of pairs) {
      const live = spine.filter((t) => t.live);
      const published = topics().filter((t) => t.status !== "placeholder");
      expect(live.map((t) => t.slug), `grade ${grade}`).toEqual(published.map((t) => t.slug));
      expect(live.map((t) => t.title), `grade ${grade}`).toEqual(published.map((t) => t.title));
    }
  });
});

// Match import SPECIFIERS, not prose — the headers of these modules
// legitimately talk about the registry they must not import.
const IMPORTS_REGISTRY = /from\s+["'][^"']*genmath-lessons["']/;
const IMPORTS_GENMATH_DATA = /from\s+["']@\/data\/genmath/;

describe("the corpus stays out of the light modules", () => {

  it("genmath-spines imports no data at all", () => {
    const src = fs.readFileSync(path.join(ROOT, "lib/genmath-spines.ts"), "utf8");
    expect(/from\s+["']@\/data\//.test(src)).toBe(false);
    expect(IMPORTS_REGISTRY.test(src)).toBe(false);
  });

  it("client-reachable modules do not import the course registry", () => {
    // Each of these sits in the client graph of high-traffic non-content
    // pages (dashboard, /math catalog, placements, anything with a ratings
    // card). Importing lib/genmath-lessons from any of them ships the
    // corpus to every such page.
    const fenced = [
      "lib/ratings.ts",
      "lib/use-ratings.ts",
      "lib/placement-bank.ts",
      "lib/placement-engine.ts",
      "lib/band-placement.ts",
      "app/math/page.tsx",
      "components/dashboard/DashboardHome.tsx",
      "components/placement/PlacementRunner.tsx",
      "components/placement/CoursePlacement.tsx",
    ];
    for (const rel of fenced) {
      const src = fs.readFileSync(path.join(ROOT, rel), "utf8");
      expect(IMPORTS_REGISTRY.test(src), `${rel} imports the registry`).toBe(false);
      expect(IMPORTS_GENMATH_DATA.test(src), `${rel} imports genmath data`).toBe(false);
    }
  });
});

describe("per-course data modules keep the corpus split", () => {
  // The per-course split (2026-08-01): lib/genmath-data/<course>.ts holds one
  // course's corpus; pages import their own course's module so webpack chunks
  // the corpus per course instead of shipping one ~10 MB registry chunk. The
  // aggregator (lib/genmath-lessons.ts) still imports everything — it exists
  // for the genuinely cross-course consumers (ЭЕШ/SAT curation, cross-grade
  // slug lookup, dashboard lesson totals) and the server shells that pass
  // plain props.
  const DATA_DIR = path.join(ROOT, "lib/genmath-data");

  // Which raw-data directories each module may import from.
  const ALLOWED_DATA: Record<string, string[]> = {
    "grade-6": ["6/", "6-mn/"],
    "grade-7": ["7/", "7-mn/"],
    "grade-8": ["8/", "8-mn/"],
    "grade-9": ["9/", "9-mn/"],
    "grade-10": ["10/", "10-mn/"],
    "grade-11": ["11/", "11-mn/"],
    "grade-12": ["12/", "12-mn/"],
    geometry: ["geometry/"],
    "prob-stats": ["prob-stats/"],
    "vectors-matrices": ["vectors-matrices/"],
    "algebra-1": ["algebra-1/"],
    "algebra-2": ["algebra-2/"],
    "integrated-1": ["integrated-1/"],
    "integrated-2": ["integrated-2/"],
    "integrated-3": ["integrated-3/"],
    precalculus: ["precalculus/"],
    calculus: ["calculus/"],
    trigonometry: ["trigonometry/"],
    "solid-geometry": ["solid-geometry/"],
    "ib-sl": ["ib-sl/"],
    "ib-hl": ["ib-hl/"],
  };

  it("every data module exists and imports ONLY its own course's data", () => {
    for (const [name, allowed] of Object.entries(ALLOWED_DATA)) {
      const rel = `lib/genmath-data/${name}.ts`;
      const src = fs.readFileSync(path.join(DATA_DIR, `${name}.ts`), "utf8");
      // One course per module — a stray import from another course's data
      // dir re-couples the chunks (exactly the integrated-3 generator bug).
      const dataImports = Array.from(
        src.matchAll(/from\s+["']@\/data\/genmath\/([^"']+)["']/g)
      ).map((m) => m[1]);
      expect(dataImports.length, `${rel} has no data imports`).toBeGreaterThan(0);
      for (const spec of dataImports) {
        expect(
          allowed.some((prefix) => spec.startsWith(prefix)),
          `${rel} imports foreign data @/data/genmath/${spec}`
        ).toBe(true);
      }
      // And never the aggregator — that would pull every other course back in.
      expect(IMPORTS_REGISTRY.test(src), `${rel} imports the registry`).toBe(false);
    }
  });

  it("no app or component file imports the registry except the server shells", () => {
    // The registry aggregates ALL courses, so any page-graph import ships the
    // full corpus. The only sanctioned entry points are server shells that
    // read it server-side and pass plain props to their client bodies.
    const ALLOWED = new Set(["app/dashboard/page.tsx", "app/math/progress/page.tsx"]);
    const offenders: string[] = [];
    const walk = (dir: string) => {
      for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const abs = path.join(dir, entry.name);
        if (entry.isDirectory()) walk(abs);
        else if (/\.(ts|tsx)$/.test(entry.name)) {
          const rel = path.relative(ROOT, abs);
          if (ALLOWED.has(rel)) continue;
          if (IMPORTS_REGISTRY.test(fs.readFileSync(abs, "utf8"))) offenders.push(rel);
        }
      }
    };
    walk(path.join(ROOT, "app"));
    walk(path.join(ROOT, "components"));
    expect(offenders, "registry imports outside the server shells").toEqual([]);
  });
});
