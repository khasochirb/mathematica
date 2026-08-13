// The bank's ANSWER CHECKER — the piece that turns a problem from "reveal the
// solution" into "commit an answer, then find out".
//
// Why this exists (student feedback, 2026-08-13): a one-click "Show solution"
// button is tempting even for disciplined students, and a student who peeks
// before solving learns nothing. So the bank now makes you answer FIRST. Two
// ways to answer, chosen per problem by the shape of its correct answer:
//
//   "numeric" — the answer is a plain number ($-6$, $0.1$, $\frac{2}{3}$).
//               The student TYPES it. No options are shown, so there is
//               nothing to back-solve from — the closest thing to paper.
//   "choice"  — the answer is an expression, an equation or a sentence
//               ($x^2 - 9x + 20$, "Each additional hour adds 25 dollars").
//               String-matching those would mark correct answers wrong, so
//               the student picks from the four authored options instead.
//
// Roughly two thirds of the corpus is numeric, so most problems get the
// stronger mode. The grader is deliberately FORGIVING IN ONE DIRECTION: it
// accepts the ways students really write a right answer ("x = 5", "5 cm",
// "2/3", "0,5") and never accepts a wrong value. When it cannot parse what
// was typed it says so rather than guessing.
//
// Pure module — no React, no storage — so lib/bank-answer.test.ts can pin
// every rule.

export type AnswerMode = "numeric" | "choice";

// ---------------------------------------------------------------------------
// Parsing
// ---------------------------------------------------------------------------

// Spacing and layout macros that carry no value. \quad/\qquad must precede
// the bare "\ " alternative or they would be eaten a character at a time.
const MATH_NOISE = /\\left|\\right|\\qquad|\\quad|\\[!,;:]|\\ /g;

// \text{ cm}, \mathrm{kg} — a unit rides along with the number and does not
// change it. Stripping them means "$12\text{ cm}$" checks against "12".
const TEXT_MACRO = /\\(?:text|textrm|mathrm|mbox|operatorname)\{[^}]*\}/g;

function stripMathWrapping(raw: string): string {
  return raw
    .replace(/\$/g, "")
    .replace(TEXT_MACRO, "")
    .replace(MATH_NOISE, "")
    .replace(/\{,\}/g, "") // KaTeX thousands separator: 1{,}000
    .replace(/\s+/g, "");
}

// A decimal or integer, tolerating both separator conventions students use:
// "1,234.5" (thousands) and "0,5" (Mongolian/European decimal comma).
function plainNumber(body: string): number | null {
  let t = body;
  if (/^\d{1,3}(?:,\d{3})+(?:\.\d+)?$/.test(t)) t = t.replace(/,/g, "");
  else if (/^\d+,\d+$/.test(t)) t = t.replace(",", ".");
  if (!/^(?:\d+\.?\d*|\.\d+)$/.test(t)) return null;
  const n = Number(t);
  return Number.isFinite(n) ? n : null;
}

const FRAC_MACRO = /^\\[dt]?frac\{([+-]?[\d.,]+)\}\{([+-]?[\d.,]+)\}$/;
const FRAC_SLASH = /^([+-]?[\d.,]+)\/([+-]?[\d.,]+)$/;

function signedPlain(body: string): number | null {
  const { sign, rest } = peelSign(body);
  const n = plainNumber(rest);
  return n === null ? null : sign * n;
}

// U+2212 MINUS SIGN shows up in pasted math; treat it as "-".
function peelSign(s: string): { sign: number; rest: string } {
  let sign = 1;
  let rest = s;
  while (rest.startsWith("-") || rest.startsWith("+") || rest.startsWith("−")) {
    if (rest[0] !== "+") sign = -sign;
    rest = rest.slice(1);
  }
  return { sign, rest };
}

function toNumber(normalized: string): number | null {
  if (!normalized) return null;

  const { sign, rest } = peelSign(normalized);

  // A trailing percent scales by 1/100, so "25\%" and "0.25" are the same
  // value — a student who types either has the answer.
  let body = rest;
  let scale = 1;
  if (/\\?%$/.test(body)) {
    body = body.replace(/\\?%$/, "");
    scale = 1 / 100;
  }

  const macro = FRAC_MACRO.exec(body);
  if (macro) {
    const num = signedPlain(macro[1]);
    const den = signedPlain(macro[2]);
    if (num === null || den === null || den === 0) return null;
    return (sign * num * scale) / den;
  }

  const slash = FRAC_SLASH.exec(body);
  if (slash) {
    const num = signedPlain(slash[1]);
    const den = signedPlain(slash[2]);
    if (num === null || den === null || den === 0) return null;
    return (sign * num * scale) / den;
  }

  const plain = plainNumber(body);
  return plain === null ? null : sign * plain * scale;
}

/**
 * The numeric value of an AUTHORED answer string, or null when the answer is
 * not a bare number (an expression, an equation, a sentence). Null is what
 * puts a problem into "choice" mode, so this function decides how a problem
 * is asked — keep it strict.
 */
export function parseNumericAnswer(raw: string): number | null {
  return toNumber(stripMathWrapping(raw));
}

// Units a student may append with NO space ("5cm"). Listed longest-first so
// "minutes" is not cut down to "min" and "mm" not to "m". A bare letter is
// deliberately NOT in this list: "5cm" is five centimetres, but "2x" is an
// expression, not the number 2, and must never be accepted for it.
const KNOWN_UNIT =
  "(?:seconds?|minutes?|degrees?|dollars?|inches|hours?|cents?|units?|days?|secs?|mins?|hrs?|inch|deg|lbs?|cm|mm|km|kg|mg|ml|ft|yd|mi|oz|in|hr|[mgsl])";
const UNIT_SUFFIX = new RegExp(`\\s*${KNOWN_UNIT}\\s*[²³]?\\.?$`, "i");

/**
 * The numeric value of what a STUDENT typed. Same grammar as above, plus the
 * habits people actually have: restating the variable ("x = 5"), writing the
 * unit ("5 cm", "12cm²", "40 degrees"), or wrapping it in math delimiters.
 *
 * Forgiving in ONE direction only. Everything here changes how an answer is
 * written, never what it is worth, so a wrong value can never be relaxed
 * into a right one.
 */
export function parseStudentAnswer(raw: string): number | null {
  const direct = parseNumericAnswer(raw);
  if (direct !== null) return direct;

  const trimmed = raw.trim();
  const relaxed = trimmed
    .replace(/^[a-zA-Z]\s*=\s*/, "") // x = 5
    .replace(UNIT_SUFFIX, "") // 5cm, 12 degrees
    .replace(/\s+[a-zA-Z°²³]+\.?$/, "") // any other spaced-off word
    .trim();
  if (relaxed === trimmed) return null; // nothing was relaxed; don't re-parse
  return parseNumericAnswer(relaxed);
}

// ---------------------------------------------------------------------------
// Checking
// ---------------------------------------------------------------------------

// Relative tolerance, so "0.6666666666666667" checks out against 2/3 while
// "0.67" does not — a fraction answered as a rounded decimal is not the same
// answer, and saying so is the pedagogically correct call.
function numbersEqual(a: number, b: number): boolean {
  const scale = Math.max(1, Math.abs(a), Math.abs(b));
  return Math.abs(a - b) <= 1e-9 * scale;
}

export type NumericVerdict = "correct" | "incorrect" | "unparsed";

/**
 * Grade a typed answer. "unparsed" is deliberately distinct from
 * "incorrect": the student gets "that doesn't look like a number" and
 * another try, instead of being told they were wrong when they were only
 * unclear.
 */
export function checkNumericAnswer(input: string, correct: string): NumericVerdict {
  const expected = parseNumericAnswer(correct);
  if (expected === null) return "unparsed";
  const got = parseStudentAnswer(input);
  if (got === null) return "unparsed";
  return numbersEqual(got, expected) ? "correct" : "incorrect";
}

/**
 * Could THIS variant be typed? Two conditions, and the second is the subtle
 * one: the correct answer must be a bare number, AND so must every
 * distractor — because a distractor that isn't a number is evidence that the
 * answer space isn't numbers.
 *
 * "How many solutions does this system have?" with options 0 / 1 / 2 /
 * "infinitely many" is the case that taught us this. Its answer is often
 * "$1$", which parses fine, but hiding the options would hide a legitimate
 * answer the student cannot type. Same for "Simplify $i^{6}$" — answer
 * $-1$, but the answer space is {1, −1, i, −i}.
 */
export function variantAnswerMode(v: { options: string[]; correctIndex: number }): AnswerMode {
  const correct = v.options[v.correctIndex];
  if (typeof correct !== "string") return "choice";
  return v.options.every((o) => parseNumericAnswer(o) !== null) ? "numeric" : "choice";
}

/**
 * How a problem TYPE is asked — the mode the UI actually uses.
 *
 * Decided per form rather than per variant so a student never sees the same
 * kind of problem typed at #3 and multiple-choice at #8 just because one set
 * of numbers happened to come out irrational. A form is typed only when
 * EVERY variant of it could be; one exception drags the whole form to
 * choices, which is the safe direction.
 */
// Deciding a form means regex-parsing every option of every variant (a form
// can carry 30+). The browse page calls this once per rendered row, so the
// answer is cached against the form object, which is a stable literal from
// the corpus.
const FORM_MODES = new WeakMap<object, AnswerMode>();

export function formAnswerMode(form: {
  variants: { options: string[]; correctIndex: number }[];
}): AnswerMode {
  const cached = FORM_MODES.get(form);
  if (cached) return cached;
  const mode: AnswerMode =
    form.variants.length > 0 && form.variants.every((v) => variantAnswerMode(v) === "numeric")
      ? "numeric"
      : "choice";
  FORM_MODES.set(form, mode);
  return mode;
}

// ---------------------------------------------------------------------------
// SSR-safe option order
// ---------------------------------------------------------------------------

// mulberry32, same tiny PRNG as lib/refinement-loop-select.ts.
function mulberry32(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function hashString(s: string): number {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/**
 * Shuffle a variant's options DETERMINISTICALLY from its id.
 *
 * The browse page renders its problems during SSR, so a Math.random shuffle
 * there would hand the client a different order than the server sent and
 * trip a hydration mismatch (the same reason ExerciseSet's variant pick is
 * strided rather than random). Seeding from the variant id keeps the order
 * stable across server and client while still varying between problems.
 */
export function seededOptionOrder(
  v: { id: string; options: string[]; correctIndex: number },
  salt = "",
): { options: string[]; correctIndex: number } {
  const rng = mulberry32(hashString(`${v.id}:${salt}`));
  const idx = v.options.map((_, i) => i);
  for (let i = idx.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1)) % (i + 1);
    [idx[i], idx[j]] = [idx[j], idx[i]];
  }
  return {
    options: idx.map((i) => v.options[i]),
    correctIndex: idx.indexOf(v.correctIndex),
  };
}
