// PER-QUESTION TIMING — the accounting, with no React in it.
//
// `attempts.time_spent_seconds` has existed since migration 004 and was NULL
// on all 93 rows: designed, never hooked up. It gates the learning engine,
// and unlike almost everything else it CANNOT be backfilled — a question
// answered without a timer is timing evidence lost permanently.
//
// The clocks live here rather than inside the hooks so they can be tested
// against an injected `now` (same shape as the injected rng in
// lib/problem-bank), which is the only way to assert "two minutes elapsed"
// without waiting two minutes. lib/use-question-timer.ts is the thin React
// wrapper.
//
// Honesty rules, shared by both clocks:
//   • Time only accrues while the tab is VISIBLE. A student who opens a test
//     and goes to dinner must not read as a four-hour thinker.
//   • A question never presented reports `undefined`, not 0. "We don't know"
//     and "instant" are different claims and only one of them is true.
//   • Values clamp to MAX_SECONDS. A visible-but-idle tab still accrues, so
//     the tail is capped rather than left to poison every downstream mean.

/** One hour. Past this the number stopped measuring thinking. */
export const MAX_SECONDS = 3600;

export type NowFn = () => number;

export function toSeconds(ms: number): number {
  const s = Math.round(ms / 1000);
  if (!Number.isFinite(s) || s < 0) return 0;
  return Math.min(s, MAX_SECONDS);
}

// ---------------------------------------------------------------------------
// Accumulating clock — for navigable test runners
// ---------------------------------------------------------------------------

/**
 * Tracks time per question key, summing repeat visits.
 *
 * Test runners let a student jump back and forth and only record attempts at
 * submit, so a question's time is the SUM of its visits, not the last one.
 */
export function createQuestionClock(now: NowFn = Date.now) {
  const totals = new Map<string, number>();
  let activeKey: string | null = null;
  let runningSince: number | null = null;
  let paused = false;

  /** Bank the running segment into its key and stop the clock. */
  function bank(): void {
    if (activeKey === null || runningSince === null) return;
    const delta = now() - runningSince;
    runningSince = null;
    if (delta <= 0) return;
    totals.set(activeKey, (totals.get(activeKey) ?? 0) + delta);
  }

  return {
    /** Put the clock on the question now on screen; null = nothing showing. */
    focus(key: string | null): void {
      if (key === activeKey && runningSince !== null) return;
      bank();
      activeKey = key;
      if (key === null) return;
      // A focused key with no time yet still gets an entry, so "seen and
      // answered instantly" reports 0 rather than "never seen".
      if (!totals.has(key)) totals.set(key, 0);
      runningSince = paused ? null : now();
    },

    /** Tab hidden — stop accruing. */
    pause(): void {
      if (paused) return;
      bank();
      paused = true;
    },

    /** Tab visible again — resume the active question. */
    resume(): void {
      if (!paused) return;
      paused = false;
      if (activeKey !== null && runningSince === null) runningSince = now();
    },

    /** Accumulated visible seconds, or undefined if never focused. */
    secondsFor(key: string): number | undefined {
      const banked = totals.get(key);
      if (banked === undefined) return undefined;
      const live = activeKey === key && runningSince !== null ? now() - runningSince : 0;
      return toSeconds(banked + live);
    },

    reset(): void {
      totals.clear();
      activeKey = null;
      runningSince = null;
      paused = false;
    },
  };
}

export type QuestionClock = ReturnType<typeof createQuestionClock>;

// ---------------------------------------------------------------------------
// Lap clock — for worksheet screens
// ---------------------------------------------------------------------------

/**
 * Times a list of questions shown together (the refinement loop's similar and
 * drill sets, the similar-questions panel, a lesson step's tap questions).
 *
 * There is no "current question" on such a screen, and timing every card from
 * when the screen appeared would charge the same seconds to every question
 * below the first. Each answer instead takes a LAP — the time since the
 * screen appeared or since the previous answer, whichever is later. That
 * matches how a list is actually worked, top to bottom, and the laps SUM to
 * the real time on screen instead of a multiple of it.
 */
export function createLapClock(now: NowFn = Date.now) {
  let mark: number | null = null;
  let hiddenAt: number | null = null;

  return {
    /** Begin a fresh set. Null parks the clock (nothing on screen). */
    start(active: boolean): void {
      mark = active ? now() : null;
      hiddenAt = null;
    },

    pause(): void {
      if (mark === null || hiddenAt !== null) return;
      hiddenAt = now();
    },

    /** Push the mark forward by the away time, so hidden time is not charged. */
    resume(): void {
      if (hiddenAt === null) return;
      const away = now() - hiddenAt;
      hiddenAt = null;
      if (mark !== null) mark += away;
    },

    /** Seconds since the last lap (or the set's start), and restart. */
    lap(): number | undefined {
      if (mark === null) return undefined;
      const at = hiddenAt ?? now(); // answering while hidden is not a real case
      const elapsed = at - mark;
      mark = now();
      hiddenAt = null;
      return toSeconds(elapsed);
    },
  };
}

export type LapClock = ReturnType<typeof createLapClock>;
