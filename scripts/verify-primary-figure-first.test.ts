// FIGURE-FIRST is the primary band's house rule, set by the owner on
// 2026-08-13: young children are taught with pictures, then try it with
// pictures. It is a rule precisely because it is easy to violate silently —
// the audit that day found the band's top year shipping FORTY lessons with
// not one figure, which no existing gate noticed because every lesson was
// otherwise well-formed.
//
// So the rule is mechanical now: every lesson of every primary grade must
// TEACH with at least one figure. Prose-only teaching in this band fails the
// build.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// The primary band on ministry labels. Grades 1 and 5 join as they are
// authored; a missing directory is a grade that does not exist yet, not a
// failure — but a grade that EXISTS must obey the rule.
const PRIMARY = ["1", "2", "3", "4", "5"];

type Step = { kind: string; figure?: { mode?: string }; teach?: string };
type Lesson = { slug: string; interactive: { steps: Step[] } };
type Unit = { slug: string; lessons: Lesson[] };

function unitsOf(grade: string): { file: string; unit: Unit }[] {
  const dir = path.join(process.cwd(), "data", "genmath", grade);
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .map((f) => ({ file: `${grade}/${f}`, unit: JSON.parse(fs.readFileSync(path.join(dir, f), "utf-8")) }));
}

const ALL = PRIMARY.flatMap((g) => unitsOf(g).map((u) => ({ grade: g, ...u })));

describe("primary band is figure-first", () => {
  it("has the authored primary grades on ministry labels", () => {
    const grades = Array.from(new Set(ALL.map((u) => u.grade))).sort();
    expect(grades).toEqual(["2", "3", "4"]);
    expect(ALL.length).toBe(24); // 8 units per authored year
  });

  it("teaches every lesson with at least one figure", () => {
    const bare: string[] = [];
    for (const { file, unit } of ALL) {
      for (const lesson of unit.lessons) {
        const figures = lesson.interactive.steps.filter(
          // a `figure` on any step, or a widget step that carries teaching
          (s) => s.figure || (s.teach && s.kind !== "teach"),
        );
        if (figures.length === 0) bare.push(`${file} / ${lesson.slug}`);
      }
    }
    expect(bare, "primary lessons that teach with no figure at all").toEqual([]);
  });

  it("draws every figure with a mode the renderer knows", () => {
    // RatioFigure dispatches on `mode`; an unknown one renders nothing at
    // all, which looks exactly like the prose-only lesson this gate exists
    // to prevent.
    const KNOWN = new Set([
      "groups", "partToPart", "partToWhole", "cross", "compareMix", "fractionBar",
      "decimalGrid", "numberLine", "decimalColumn", "decimalArea", "divideChain",
      "percentBar", "percentChange", "percentChangeFinder", "integerLine",
      "integerAdd", "geo", "barChart", "pictograph", "lineGraph", "clockFace",
    ]);
    const bad: string[] = [];
    for (const { file, unit } of ALL) {
      for (const lesson of unit.lessons) {
        for (const s of lesson.interactive.steps) {
          if (s.figure && !KNOWN.has(s.figure.mode ?? "")) {
            bad.push(`${file} / ${lesson.slug}: ${s.figure.mode}`);
          }
        }
      }
    }
    expect(bad, "figures whose mode no renderer handles").toEqual([]);
  });

  it("keeps the year that had none — grade 4 — well above zero", () => {
    // The specific regression this gate was written for.
    const g4 = ALL.filter((u) => u.grade === "4");
    const figures = g4.reduce(
      (n, { unit }) =>
        n + unit.lessons.reduce((m, l) => m + l.interactive.steps.filter((s) => s.figure).length, 0),
      0,
    );
    expect(figures).toBeGreaterThanOrEqual(80);
  });
});
