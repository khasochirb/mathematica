// Interactive lesson model + pure interaction logic for the General Math hub.
// The manipulables are config-driven so later topics assemble interactives from
// these parts. All live math goes through the pure functions below so it can be
// unit-tested (scripts/verify-genmath-interactive.test.ts).

import type { GenMathLesson } from "@/lib/genmath-lessons";
import type { LessonProblem } from "@/lib/lesson-types";

// A small illustrated token (a colored chip standing in for cocoa, milk, an
// apple, …). Kept abstract/clean rather than emoji to stay on-brand.
export interface Token {
  label: string; // singular noun, e.g. "cocoa"
  plural: string; // e.g. "cocoa scoops"
  color: string; // CSS color for the chip fill
  glyph?: string; // optional 1-char/emoji hint, used small + decoratively
}

export interface ScalerConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  maxBatches: number; // slider runs 1..maxBatches
  goodLabel: string; // e.g. "tastes just right"
}

export interface OrderFlipConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  forwardLabel: string; // e.g. "Smooth hot chocolate"
  flippedLabel: string; // e.g. "A cup of mud"
}

export interface CompareGroup {
  count: number;
  token: Token;
}
export interface CompareToggleConfig {
  groupA: CompareGroup;
  groupB: CompareGroup;
}

// Equivalent ratios — a ratio table / double number line the student extends.
export interface RatioTableConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
  maxCols: number; // how many equivalent columns can be revealed
}

// Comparing ratios — two mixes side by side; reveal which is stronger.
export interface CompareRatio {
  a: number;
  b: number;
  label: string;
  token: Token;
}
export interface RatioCompareConfig {
  left: CompareRatio;
  right: CompareRatio;
  unitNote: string; // e.g. "more orangey" — what "bigger" means here
}

// Rates — a live two-quantity rate calculator (distance/time, items/min, …).
export interface RateMeterConfig {
  topLabel: string;
  topUnit: string;
  top: number;
  topMax: number;
  topStep: number;
  bottomLabel: string;
  bottomUnit: string;
  bottom: number;
  bottomMax: number;
  bottomStep: number;
  rateUnit: string; // e.g. "km per hour"
}

// Unit rate — two deals side by side; reveal the better buy per unit.
export interface Deal {
  label: string;
  price: number;
  qty: number;
}
export interface DealCompareConfig {
  unit: string; // e.g. "bottle"
  currency: string; // e.g. "$"
  dealA: Deal;
  dealB: Deal;
}

// Word problems — scale a known ratio to find the missing value.
export interface ProportionBuilderConfig {
  aLabel: string;
  bLabel: string;
  a: number;
  b: number;
  knownSide: "a" | "b";
  knownValue: number;
  tokenA: Token;
  tokenB: Token;
}

// A visual figure attached to teach steps and problems.
export interface FigureGroupSpec {
  count: number;
  color: string;
  label: string;
  glyph?: string;
}
export interface FigureSpec {
  mode: "groups" | "partToPart" | "partToWhole" | "cross" | "compareMix" | "fractionBar" | "decimalGrid" | "numberLine";
  groups?: FigureGroupSpec[];
  highlightIndex?: number; // the highlighted "part" in partToWhole (default 0)
  // "cross" — a cross-multiply diagram for a:b vs c:d (draws the two diagonals + products).
  cross?: { a: number; b: number; c: number; d: number };
  // "compareMix" — two read-only mixes side by side (juice + water), so a compare
  // question shows BOTH options, never just one.
  mixes?: { a: number; b: number; label?: string }[];
  // "fractionBar" — a bar split into `den` equal pieces with `num` shaded.
  fraction?: { num: number; den: number; label?: string };
  // "decimalGrid" — a 10×10 grid (one whole) with `value` shaded (e.g. 0.37).
  decimal?: { value: number; label?: string };
  // "numberLine" — a number line (default 0..1, ticks at tenths) with points plotted.
  numberLine?: { min?: number; max?: number; points: { value: number; label?: string; color?: string }[] };
}

// Fractions — a bar you split into more (equal) pieces to see equivalent fractions.
export interface FractionScalerConfig {
  num: number;
  den: number;
  maxSplit: number; // split each piece into 1..maxSplit
  color?: string;
}

// Fractions — a bar whose pieces you merge to reach simplest form.
export interface FractionSimplifyConfig {
  num: number;
  den: number;
  color?: string;
}

// Comparing — two bars; give them the same-size pieces (common denominator), then compare.
export interface FractionCompareConfig {
  left: { num: number; den: number; label?: string };
  right: { num: number; den: number; label?: string };
  color?: string;
}

// Add/subtract — match the pieces, then combine the shaded amounts.
export interface FractionCombineConfig {
  left: { num: number; den: number };
  right: { num: number; den: number };
  op: "add" | "sub";
  color?: string;
}

// Multiply — an area model: shade columns (first fraction) × rows (second fraction).
export interface AreaModelConfig {
  aNum: number;
  aDen: number;
  bNum: number;
  bDen: number;
}

// Divide — a measurement model: how many of the divisor fit into the dividend.
export interface FractionDivideConfig {
  dividend: { num: number; den: number };
  divisor: { num: number; den: number };
}

export interface NotationToggleConfig {
  a: number;
  b: number;
  tokenA: Token;
  tokenB: Token;
}

// Decimals — a 10×10 grid that is ONE whole. Filled tenths read as full
// columns, loose hundredths as single cells, so place value is literal. The
// student taps ±0.1 / ±0.01 to build a decimal and watch the grid + fraction
// update in lockstep.
export interface DecimalGridConfig {
  start: number; // initial value in [0, 1], a multiple of 0.01 (e.g. 0.37)
  color?: string;
}

// Comparing decimals — two grids side by side; the student taps <, =, or >
// and gets instant feedback. Targets the "more digits = bigger" misconception
// (0.5 shades more than 0.45).
export interface DecimalCompareConfig {
  left: number; // a value in [0, 1], multiple of 0.01
  right: number;
  color?: string;
}

// One worked example on a multi-example page (figure + reasoning steps).
export interface WorkedItem {
  prompt: string;
  figure?: FigureSpec;
  steps: string[];
  answer: string;
  check: string[];
}

// One try-it problem on a multi-problem page — the student ANSWERS (taps an
// option) and gets instant feedback, with a figure.
export interface TryItItem {
  prompt: string;
  figure?: FigureSpec;
  options: string[];
  correctIndex: number;
  explanation: string;
  check: string[];
}

export type InteractiveStep =
  | { kind: "concept"; eyebrow?: string; title: string; body: string }
  | { kind: "teach"; eyebrow?: string; title: string; body?: string; beats?: string[]; figure?: FigureSpec }
  | { kind: "notationToggle"; eyebrow?: string; title: string; teach: string; config: NotationToggleConfig }
  | { kind: "workedSet"; eyebrow?: string; title: string; intro?: string; examples: WorkedItem[] }
  | { kind: "tryItSet"; eyebrow?: string; title: string; intro?: string; problems: TryItItem[] }
  | { kind: "scaler"; eyebrow?: string; title: string; teach: string; config: ScalerConfig }
  | { kind: "orderFlip"; eyebrow?: string; title: string; teach: string; config: OrderFlipConfig }
  | { kind: "compareToggle"; eyebrow?: string; title: string; teach: string; config: CompareToggleConfig }
  | { kind: "ratioTable"; eyebrow?: string; title: string; teach: string; config: RatioTableConfig }
  | { kind: "ratioCompare"; eyebrow?: string; title: string; teach: string; config: RatioCompareConfig }
  | { kind: "rateMeter"; eyebrow?: string; title: string; teach: string; config: RateMeterConfig }
  | { kind: "dealCompare"; eyebrow?: string; title: string; teach: string; config: DealCompareConfig }
  | { kind: "proportionBuilder"; eyebrow?: string; title: string; teach: string; config: ProportionBuilderConfig }
  | { kind: "fractionScaler"; eyebrow?: string; title: string; teach: string; config: FractionScalerConfig }
  | { kind: "fractionSimplify"; eyebrow?: string; title: string; teach: string; config: FractionSimplifyConfig }
  | { kind: "fractionCompare"; eyebrow?: string; title: string; teach: string; config: FractionCompareConfig }
  | { kind: "fractionCombine"; eyebrow?: string; title: string; teach: string; config: FractionCombineConfig }
  | { kind: "areaModel"; eyebrow?: string; title: string; teach: string; config: AreaModelConfig }
  | { kind: "fractionDivide"; eyebrow?: string; title: string; teach: string; config: FractionDivideConfig }
  | { kind: "decimalGrid"; eyebrow?: string; title: string; teach: string; config: DecimalGridConfig }
  | { kind: "decimalCompare"; eyebrow?: string; title: string; teach: string; config: DecimalCompareConfig }
  | { kind: "worked"; eyebrow?: string; title: string; problemId: string }
  | { kind: "tryIt"; eyebrow?: string; title: string; problemId: string }
  | {
      kind: "tapQuestion";
      eyebrow?: string;
      title: string;
      prompt: string;
      options: string[];
      correctIndex: number;
      explanation: string;
      check: string[]; // sympy assertions proving the correct option is right
    }
  | { kind: "funFact"; eyebrow?: string; title: string; body: string }
  | { kind: "tip"; eyebrow?: string; title: string; body: string }
  | { kind: "recap"; eyebrow?: string; title: string; points: string[] };

export interface InteractiveLesson {
  steps: InteractiveStep[];
}

// ---------------------------------------------------------------------------
// Pure interaction logic — unit-tested
// ---------------------------------------------------------------------------

export function gcd(a: number, b: number): number {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b) {
    [a, b] = [b, a % b];
  }
  return a || 1;
}

// Simplest form of a ratio, e.g. simplifyRatio(2,6) -> [1,3].
export function simplifyRatio(a: number, b: number): [number, number] {
  const g = gcd(a, b);
  return [a / g, b / g];
}

// Scale a ratio by n batches, e.g. scaleRatio(2,6,3) -> [6,18].
export function scaleRatio(a: number, b: number, n: number): [number, number] {
  return [a * n, b * n];
}

// True when a:b and c:d are the same ratio (cross-multiply).
export function ratioEquivalent(a: number, b: number, c: number, d: number): boolean {
  return a * d === b * c;
}

// Format a ratio as "a:b".
export function formatRatio(a: number, b: number): string {
  return `${a}:${b}`;
}

// Part-to-whole pair for a compare toggle, e.g. partToWhole(3,5) -> [3,8].
export function partToWhole(part: number, other: number): [number, number] {
  return [part, part + other];
}

// Unit price of a deal (price per single unit).
export function unitPrice(price: number, qty: number): number {
  return price / qty;
}

// Index (0 = first, 1 = second) of the cheaper deal by unit price; -1 if equal.
export function cheaperDeal(
  a: { price: number; qty: number },
  b: { price: number; qty: number },
): number {
  const ua = a.price / a.qty;
  const ub = b.price / b.qty;
  if (ua < ub) return 0;
  if (ub < ua) return 1;
  return -1;
}

// A rate value, top per bottom (e.g. distance per time).
export function rateValue(top: number, bottom: number): number {
  return bottom === 0 ? 0 : top / bottom;
}

// Scale a:b so the known side equals knownValue; return the matching other side.
// e.g. proportionMissing(3,5,"b",15) -> 9  (red:blue 3:5, 15 blue -> 9 red)
export function proportionMissing(
  a: number,
  b: number,
  knownSide: "a" | "b",
  knownValue: number,
): number {
  return knownSide === "a" ? (b * knownValue) / a : (a * knownValue) / b;
}

// ---------------------------------------------------------------------------
// Helpers for the renderer
// ---------------------------------------------------------------------------

// Find a worked-example or try-it problem referenced by an interactive step.
export function getLessonProblem(lesson: GenMathLesson, id: string): LessonProblem | null {
  return (
    lesson.workedExamples.find((p) => p.id === id) ??
    lesson.tryIt.find((p) => p.id === id) ??
    null
  );
}
