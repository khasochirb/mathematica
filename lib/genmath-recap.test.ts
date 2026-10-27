import { describe, expect, it } from "vitest";
import fs from "node:fs";
import path from "node:path";

// The lesson player renders a recap with `step.points.map(...)`. All 24 solid-
// geometry recaps once stored their lines under `bullets`, so the last step of
// every solid-geometry lesson (three of them live ЭШ units) threw, and no gate
// noticed (review pile 6bj). This walks every course file, English and
// Mongolian, and fails on any recap the player cannot render.
const DATA = path.join(process.cwd(), "data", "genmath");

describe("recap steps", () => {
  it("every recap carries a points array of strings", () => {
    const bad: string[] = [];
    for (const dir of fs.readdirSync(DATA)) {
      const full = path.join(DATA, dir);
      if (!fs.statSync(full).isDirectory()) continue;
      for (const f of fs.readdirSync(full).filter((x) => x.endsWith(".json"))) {
        const topic = JSON.parse(fs.readFileSync(path.join(full, f), "utf8"));
        (topic.lessons ?? []).forEach((lesson: any, li: number) => {
          (lesson.interactive?.steps ?? []).forEach((step: any, si: number) => {
            if (step?.kind !== "recap") return;
            const ok = Array.isArray(step.points) && step.points.every((p: unknown) => typeof p === "string");
            if (!ok) bad.push(`${dir}/${f} lessons/${li}/interactive/steps/${si}`);
          });
        });
      }
    }
    expect(bad, `recap steps the lesson player would crash on:\n${bad.join("\n")}`).toEqual([]);
  });
});
