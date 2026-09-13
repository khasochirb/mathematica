import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// THE PRINTED DICTIONARY, AND THE ONE THING THAT COULD SILENTLY ROT IT.
//
// docs/en-mn-math-glossary.md is a transcription of the printed English–
// Mongolian mathematics dictionary; docs/en-mn-math-glossary.tsv is the flat
// form the markdown's own "How to use" section tells you to grep. The two are
// generated from each other, so the failure mode is a quiet drift: someone
// edits the markdown, the tsv keeps the old row, and a grep returns wording
// the book does not actually print.
//
// This does not re-audit the transcription — that was done against the
// photographs. It pins the parts a future session could break by accident.

const ROOT = process.cwd();
const MD = path.join(ROOT, "docs/en-mn-math-glossary.md");
const TSV = path.join(ROOT, "docs/en-mn-math-glossary.tsv");

function rows(): { en: string; mn: string }[] {
  const lines = fs.readFileSync(TSV, "utf8").trim().split("\n").slice(1);
  return lines.map((l) => {
    const p = l.split("\t");
    return { en: p[0], mn: p[1] ?? "" };
  });
}

describe("en-mn math glossary", () => {
  it("ships both the readable and the greppable form", () => {
    expect(fs.existsSync(MD), "docs/en-mn-math-glossary.md").toBe(true);
    expect(fs.existsSync(TSV), "docs/en-mn-math-glossary.tsv").toBe(true);
  });

  it("has a row for every headword the markdown prints", () => {
    const md = fs.readFileSync(MD, "utf8");
    // `\|` inside a markdown table cell is table escaping, not part of the
    // term — one headword really is `Read || as is parallel.` — so unescape
    // before comparing, or the tsv looks wrong when it is the reader that is.
    const headwords = new Set(
      Array.from(md.matchAll(/^\|\s*`([^`]+)`\s*\|/gm)).map((m) =>
        m[1].trim().replace(/\\\|/g, "|"),
      ),
    );
    const have = new Set(rows().map((r) => r.en));
    const missing = Array.from(headwords).filter((h) => !have.has(h));
    expect(missing, "headwords in the markdown with no tsv row — regenerate the tsv").toEqual([]);
  });

  it("carries no empty Mongolian", () => {
    // An empty rendering would read as "the book has no word for this", which
    // is a different and much stronger claim than "we have not transcribed it".
    const blank = rows().filter((r) => r.en && !r.mn).map((r) => r.en);
    expect(blank, "these rows claim the dictionary prints nothing").toEqual([]);
  });

  it("states its own coverage, because the gap is the dangerous part", () => {
    // The transcription reaches `base` and no further. A reader who assumes it
    // is complete would take a missing headword as licence to invent — which
    // is exactly what docs/MONGOLIAN.md's term-not-found rule forbids.
    const md = fs.readFileSync(MD, "utf8");
    expect(md).toMatch(/a.*→.*base/);
    expect(md.toLowerCase()).toContain("not permission to invent");
  });

  it("keeps the entries this session actually relied on", () => {
    // Spot-checks, not a re-audit: the terms drafted against the dictionary on
    // 13 Sep. If a regeneration drops or alters one of these, a draft that
    // cites the book stops matching it.
    const by = new Map(rows().map((r) => [r.en.toLowerCase(), r.mn]));
    expect(by.get("absolute value")).toBe("абсолют хэмжигдэхүүн");
    expect(by.get("angle of depression")).toBe("доошоо харах өнцөг");
    expect(by.get("angle of elevation")).toBe("дээшээ харах өнцөг");
    expect(by.get("abscissa")).toBe("абсцисс");
    expect(by.get("additive inverse")).toContain("эсрэг тоо");
  });
});
