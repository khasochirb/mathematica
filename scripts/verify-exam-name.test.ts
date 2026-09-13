import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// THE EXAM'S NAME CHANGED.
//
// It was ЭЕШ — Элсэлтийн Ерөнхий Шалгалт, the "General Entrance Examination".
// It is now ЭШ — Элсэлтийн Шалгалт. The «Ерөнхий» is gone. (Khas, 13 Sep 2026.)
//
// This matters more than a rename usually would, because the whole product is
// built around that exam and its name is in the eyebrow, the headline and the
// hub label. The `/exam-prep` H1 carried the old name all the way to
// production before this check existed.
//
// What is deliberately NOT caught:
//   - PDF filenames («ЭЕШ-2025-Математик-A-хувилбар.pdf»). Those are real
//     files on disk, published under the old name. Renaming them would break
//     the extraction scripts and falsify the source.
//   - memory/ and the closed chats' status files, which are history. CLAUDE.md
//     forbids writing to the closed ones at all.

const ROOT = process.cwd();
const OLD_SHORT = "ЭЕШ";
const OLD_LONG = "Элсэлтийн Ерөнхий Шалгалт";

function sourceFiles(dirs: string[]): string[] {
  const out: string[] = [];
  const walk = (dir: string) => {
    if (!fs.existsSync(dir)) return;
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else if (/\.(tsx?|json|md)$/.test(e.name)) out.push(p);
    }
  };
  for (const d of dirs) walk(path.join(ROOT, d));
  return out;
}

describe("exam name", () => {
  it("uses ЭШ, not the retired ЭЕШ, on every user-facing surface", () => {
    const offenders: string[] = [];
    for (const file of sourceFiles(["app", "components", "lib", "data", "docs"])) {
      const src = fs.readFileSync(file, "utf8");
      // A PDF filename is the one legitimate place the old name survives.
      const lines = src.split("\n");
      lines.forEach((line, i) => {
        if (!line.includes(OLD_SHORT) && !line.includes(OLD_LONG)) return;
        if (/\.pdf/i.test(line)) return;
        offenders.push(`${path.relative(ROOT, file)}:${i + 1}`);
      });
    }
    expect(
      offenders,
      "the exam is Элсэлтийн Шалгалт (ЭШ) — «Ерөнхий» was dropped; these still say ЭЕШ",
    ).toEqual([]);
  });

  it("still reads the exam's Ш as «шалгалт»", () => {
    // The chrome dictionary splits «шалгалт» (the real state papers) from
    // «тест» (a practice test), and the reason given is that the exam's own
    // name ends in Шалгалт. Dropping «Ерөнхий» does not disturb that — but if
    // the name ever loses its Ш, the note in the dictionary stops being true.
    expect("Элсэлтийн Шалгалт").toMatch(/Шалгалт$/);
  });
});
