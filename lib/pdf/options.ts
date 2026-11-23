// What a printable worksheet is: which source, and how it is laid out.
//
// One canonical shape, parsed strictly from untrusted input (a JSON body or a
// query string) and serialized back to a fixed query string. The signed print
// token covers that exact string, so the print page renders only what the API
// route authorised, and nothing a reader edits into the URL.
//
// Answers, not solutions: a PDF carries at most an answer key, and the key
// points at the site for the step-by-step solution (Khas, 23 Nov 2026; the
// reasoning is in docs/pdf-export.md).

export type PdfSource =
  | { kind: "bank"; bank: string; unit: string; level: 0 | 1 | 2 | 3; count: number | "all" }
  | { kind: "exam"; examId: string }
  | { kind: "esh"; testKey: string };

export type PdfOptions = {
  source: PdfSource;
  lang: "mn" | "en";
  /** "none": problems only. "key": an answer key on its own page at the end. */
  answers: "none" | "key";
  /** Blank space under every problem for working. */
  space: boolean;
  /** A "Name ____ Date ____" line at the top of page 1. */
  nameLine: boolean;
};

export const COUNT_CHOICES = [10, 20, 40] as const;

const SLUG = /^[a-z0-9][a-z0-9-]{0,63}$/;
const TEST_KEY = /^[0-9A-Z]{2,6}$/;

type Raw = Record<string, unknown>;

function str(v: unknown): string | null {
  return typeof v === "string" ? v : null;
}

/** Parse untrusted input. Returns null on anything malformed: fail closed. */
export function parsePdfOptions(raw: Raw): PdfOptions | null {
  const kind = str(raw.kind);
  let source: PdfSource;
  if (kind === "bank") {
    const bank = str(raw.bank);
    const unit = str(raw.unit);
    if (!bank || !unit || !SLUG.test(bank) || !SLUG.test(unit)) return null;
    const levelN = Number(raw.level ?? 0);
    if (![0, 1, 2, 3].includes(levelN)) return null;
    const c = raw.count ?? "all";
    let count: number | "all";
    if (c === "all") count = "all";
    else {
      const n = Number(c);
      if (!(COUNT_CHOICES as readonly number[]).includes(n)) return null;
      count = n;
    }
    source = { kind, bank, unit, level: levelN as 0 | 1 | 2 | 3, count };
  } else if (kind === "exam") {
    const examId = str(raw.examId);
    if (!examId || !SLUG.test(examId)) return null;
    source = { kind, examId };
  } else if (kind === "esh") {
    const testKey = str(raw.testKey);
    if (!testKey || !TEST_KEY.test(testKey)) return null;
    source = { kind, testKey };
  } else return null;

  const lang = str(raw.lang) ?? "mn";
  if (lang !== "mn" && lang !== "en") return null;
  const answers = str(raw.answers) ?? "key";
  if (answers !== "none" && answers !== "key") return null;
  const flag = (v: unknown, dflt: boolean) =>
    v === undefined ? dflt : v === true || v === "1" ? true : v === false || v === "0" ? false : null;
  const space = flag(raw.space, false);
  const nameLine = flag(raw.nameLine, true);
  if (space === null || nameLine === null) return null;
  // ЭШ papers exist only in Mongolian.
  return { source, lang: source.kind === "esh" ? "mn" : lang, answers, space, nameLine };
}

/** Fixed-order query string. The print token signs exactly this. */
export function canonicalQuery(o: PdfOptions): string {
  const p = new URLSearchParams();
  const s = o.source;
  p.set("kind", s.kind);
  if (s.kind === "bank") {
    p.set("bank", s.bank);
    p.set("unit", s.unit);
    p.set("level", String(s.level));
    p.set("count", String(s.count));
  } else if (s.kind === "exam") p.set("examId", s.examId);
  else p.set("testKey", s.testKey);
  p.set("lang", o.lang);
  p.set("answers", o.answers);
  p.set("space", o.space ? "1" : "0");
  p.set("nameLine", o.nameLine ? "1" : "0");
  return p.toString();
}

/** `MongolPotential_<slug>_<YYYY-MM-DD>.pdf`, ASCII only (safe in headers). */
export function pdfFileName(o: PdfOptions, date = new Date()): string {
  const s = o.source;
  const slug =
    s.kind === "bank" ? `${s.bank}-${s.unit}` : s.kind === "exam" ? s.examId : `ESH-${s.testKey}`;
  const day = date.toISOString().slice(0, 10);
  return `MongolPotential_${slug.replace(/[^A-Za-z0-9-]/g, "")}_${day}.pdf`;
}
