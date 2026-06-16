// Refinement loop — mastery analytics (Phase 3d, §5).
//
// Pure helpers for the "recently mastered" rule: once a student completes a
// loop with EXIT_MASTERED on a topic, that topic should stop surfacing as a
// weak spot on the dashboard for a window (default 14 days, per §5) — stats
// lag the actual learning, so we give the student credit for the work. Kept
// pure + data-shape-light so it is unit-testable and reusable by the dashboard
// and any future analytics surface.

import type { ExitReason } from "./refinement-loop";

const DAY_MS = 86_400_000;

// Minimal shape needed from a completed refinement_loop_sessions row.
export interface CompletedLoopLite {
  topic: string;
  exitReason: ExitReason | null;
  completedAt: string | null;
}

// Topics with an EXIT_MASTERED loop completed within the suppression window.
export function recentlyMasteredTopics(
  loops: readonly CompletedLoopLite[],
  now: number = Date.now(),
  windowDays = 14,
): Set<string> {
  const cutoff = now - windowDays * DAY_MS;
  const out = new Set<string>();
  for (const l of loops) {
    if (l.exitReason !== "mastered" || !l.completedAt) continue;
    const t = Date.parse(l.completedAt);
    if (!Number.isNaN(t) && t >= cutoff) out.add(l.topic);
  }
  return out;
}

// Split weak topics into those still shown vs. those hidden because they were
// recently mastered (kept for an optional "Бүрэн эзэмшсэн" badge).
export function partitionWeakTopics<T extends { topic: string }>(
  weak: readonly T[],
  mastered: Set<string>,
): { visible: T[]; recentlyMastered: T[] } {
  const visible: T[] = [];
  const recentlyMastered: T[] = [];
  for (const w of weak) (mastered.has(w.topic) ? recentlyMastered : visible).push(w);
  return { visible, recentlyMastered };
}
