import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// STANDING OWNER REQUIREMENT (asked repeatedly before 2026-08-01, then
// enforced): the ЭЕШ, SAT and IB hub landing pages must be consistent in
// design and structure. Consistency is enforced by construction — all three
// build on components/hub/HubKit.tsx — and by THIS test, which fails the
// moment a hub page abandons the kit or reorders the canonical sections:
//
//   hero → tests → course → practice by topic → progress
//
// Hub-specific extras (stats, recommendations, roadmap) are allowed AFTER
// the canonical sections, never between them.

const ROOT = path.resolve(__dirname, "..");

const HUBS: {
  name: string;
  file: string;
  // The four canonical section labels, in required order (each hub's
  // content language — ЭЕШ Mongolian, SAT/IB English).
  sections: [string, string, string, string];
}[] = [
  {
    name: "ЭЕШ",
    file: "app/practice/esh/page.tsx",
    sections: ["Бодит шалгалт", "Сэдвээр суралцах", "Сэдвээр дадлагажих", "Ахиц"],
  },
  {
    name: "SAT",
    file: "app/practice/sat/page.tsx",
    sections: ["Practice tests", "The course", "Practice by topic", "Your progress"],
  },
  {
    name: "IB",
    file: "app/practice/ib/page.tsx",
    sections: ["Practice sets", "The courses", "Practice by topic", "Your progress"],
  },
];

describe("hub landing pages stay structurally consistent", () => {
  for (const hub of HUBS) {
    const src = fs.readFileSync(path.join(ROOT, hub.file), "utf8");

    it(`${hub.name} hub builds on HubKit`, () => {
      expect(src).toMatch(/from\s+["']@\/components\/hub\/HubKit["']/);
      expect(src, `${hub.name}: missing <HubShell>`).toContain("<HubShell>");
      expect(src, `${hub.name}: missing <HubHero`).toContain("<HubHero");
    });

    it(`${hub.name} hub keeps the canonical section order`, () => {
      // Section labels appear as HubSection label props; their source order
      // is their render order.
      const positions = hub.sections.map((label) => {
        const idx = src.indexOf(`label="${label}"`);
        expect(idx, `${hub.name}: section "${label}" is missing`).toBeGreaterThan(-1);
        return idx;
      });
      const sorted = [...positions].sort((a, b) => a - b);
      expect(positions, `${hub.name}: sections out of canonical order`).toEqual(sorted);
    });

    it(`${hub.name} hub does not hand-roll the shell`, () => {
      // The old drift signature: a page-local min-h-screen wrapper with its
      // own max-width instead of HubShell.
      expect(src, `${hub.name}: page-local max-w container`).not.toMatch(
        /className="[^"]*max-w-(3xl|5xl)[^"]*mx-auto/,
      );
    });
  }
});
