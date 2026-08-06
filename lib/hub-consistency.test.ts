import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// STANDING OWNER REQUIREMENT, direction corrected 2026-08-01: the ЭЕШ hub's
// ORIGINAL design is the reference, and SAT and IB are built to match IT —
// wide shell, bordered stats header, accent progress banner, 2×2 icon action
// cards (components/hub/HubKit.tsx). An earlier pass flattened ЭЕШ into a
// simpler row-link style instead; the owner rejected that. This test keeps
// all three hubs on the kit and keeps the reference direction honest.

const ROOT = path.resolve(__dirname, "..");

const HUBS = [
  { name: "ЭЕШ", file: "app/practice/esh/page.tsx" },
  { name: "SAT", file: "app/practice/sat/page.tsx" },
  { name: "IB", file: "app/practice/ib/page.tsx" },
];

describe("hub landing pages share the ЭЕШ design idiom", () => {
  for (const hub of HUBS) {
    const src = fs.readFileSync(path.join(ROOT, hub.file), "utf8");

    it(`${hub.name} hub builds on HubKit`, () => {
      expect(src).toMatch(/from\s+["']@\/components\/hub\/HubKit["']/);
      for (const piece of ["<HubShell>", "<HubHeader", "<HubProgressBanner", "<HubActionGrid"]) {
        expect(src, `${hub.name}: missing ${piece}`).toContain(piece);
      }
    });

    it(`${hub.name} hub does not hand-roll the shell`, () => {
      // Drift signature: a page-local width container instead of HubShell.
      expect(src, `${hub.name}: page-local max-w container`).not.toMatch(
        /className="[^"]*max-w-(3xl|5xl)[^"]*mx-auto/,
      );
    });
  }

  it("the kit itself keeps the ЭЕШ dimensions (wide shell, card grid)", () => {
    const kit = fs.readFileSync(path.join(ROOT, "components/hub/HubKit.tsx"), "utf8");
    expect(kit, "HubShell must stay max-w-5xl (the ЭЕШ width)").toContain("max-w-5xl");
    expect(kit, "action grid must stay the 2-col card grid").toContain("sm:grid-cols-2");
  });

  it("every hub still surfaces its three schema branches (tests · course · topic practice)", () => {
    // The resource blueprint's consistency rule, checked as destinations.
    const need: Record<string, string[]> = {
      "app/practice/esh/page.tsx": ["/practice/esh/test", "/practice/esh/topics", "/practice/esh/practice"],
      "app/practice/sat/page.tsx": ["/practice/sat/test/", "/practice/sat/learn", "/practice/sat/bank"],
      "app/practice/ib/page.tsx": ["/math/ib-sl", "/math/ib-hl", "/math/ib-ai-sl", "/practice/ib/bank"],
    };
    for (const [file, hrefs] of Object.entries(need)) {
      const src = fs.readFileSync(path.join(ROOT, file), "utf8");
      for (const href of hrefs) {
        expect(src, `${file} lost its ${href} destination`).toContain(href);
      }
    }
  });

  it("no course lesson surface mounts the AI tutor", () => {
    // Owner decision 2026-08-01: the AI explains missed EXAM problems (the
    // ЭЕШ RefinementLoop) and routes to practice — it does not chat inside
    // course lessons. LessonPlayer must stay tutor-free.
    const player = fs.readFileSync(
      path.join(ROOT, "components/genmath/interactive/LessonPlayer.tsx"),
      "utf8",
    );
    expect(player).not.toMatch(/from\s+["']@\/components\/tutor\/TutorPanel["']/);
    // ...and the post-exam surface KEEPS it.
    const loop = fs.readFileSync(path.join(ROOT, "components/esh/RefinementLoop.tsx"), "utf8");
    expect(loop).toMatch(/from\s+["']@\/components\/tutor\/TutorPanel["']/);
  });
});
