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

export type InteractiveStep =
  | { kind: "concept"; eyebrow?: string; title: string; body: string }
  | { kind: "scaler"; eyebrow?: string; title: string; teach: string; config: ScalerConfig }
  | { kind: "orderFlip"; eyebrow?: string; title: string; teach: string; config: OrderFlipConfig }
  | { kind: "compareToggle"; eyebrow?: string; title: string; teach: string; config: CompareToggleConfig }
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
