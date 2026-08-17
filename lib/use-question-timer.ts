"use client";

// React wrappers around the timing clocks. All the accounting — and every
// honesty rule — lives in lib/question-clock.ts, which is pure and tested
// against an injected `now`. These hooks only bind a clock to a component
// and to the tab's visibility.
//
// Which one to use:
//   useQuestionTimers()   navigable test runners (ЭШ, SAT): a question's
//                         time is the sum of its visits, read at submit.
//   useLapTimer(key)      worksheet screens showing several questions at
//                         once (refinement loop sets, similar-questions
//                         panel, a lesson step's tap questions).
//   useQuestionTimer(key) one question on screen, answering ends it (drills).

import { useCallback, useEffect, useMemo, useRef } from "react";
import { createLapClock, createQuestionClock, MAX_SECONDS } from "./question-clock";

export { MAX_SECONDS };

// Binds a clock's pause/resume to tab visibility, and banks on unmount so a
// student who navigates away mid-question does not silently lose the segment.
function useVisibility(clock: { pause: () => void; resume: () => void }) {
  useEffect(() => {
    if (typeof document === "undefined") return;
    // Resume on MOUNT, not just on a visibility event. The cleanup below
    // pauses, and React remounts effects (StrictMode in dev does it on every
    // mount) — without this the very first remount latched the clock paused
    // and every attempt recorded 0 seconds. Caught end-to-end, not in review.
    if (!document.hidden) clock.resume();
    const onVisibility = () => (document.hidden ? clock.pause() : clock.resume());
    document.addEventListener("visibilitychange", onVisibility);
    return () => {
      document.removeEventListener("visibilitychange", onVisibility);
      // Bank the running segment so navigating away mid-question keeps it.
      clock.pause();
    };
  }, [clock]);
}

export interface QuestionTimers {
  /** Put the clock on the question now on screen; null when none is. */
  focus: (key: string | null) => void;
  /** Accumulated visible seconds for `key`, or undefined if never focused. */
  secondsFor: (key: string) => number | undefined;
  reset: () => void;
}

export function useQuestionTimers(): QuestionTimers {
  const clock = useMemo(() => createQuestionClock(), []);
  useVisibility(clock);

  const focus = useCallback((key: string | null) => clock.focus(key), [clock]);
  const secondsFor = useCallback((key: string) => clock.secondsFor(key), [clock]);
  const reset = useCallback(() => clock.reset(), [clock]);

  return useMemo(() => ({ focus, secondsFor, reset }), [focus, secondsFor, reset]);
}

/**
 * Lap timer for a set of questions shown together. `resetKey` starts a fresh
 * set (a new loop state, a reopened panel, the next lesson step); null parks
 * the clock.
 */
export function useLapTimer(resetKey: string | null): { lap: () => number | undefined } {
  const clock = useMemo(() => createLapClock(), []);
  const lastKey = useRef<string | null | undefined>(undefined);
  useVisibility(clock);

  // Start during render rather than in an effect, so a question answered
  // before effects flush is still timed from when its set appeared.
  if (resetKey !== lastKey.current) {
    lastKey.current = resetKey;
    clock.start(resetKey !== null);
  }

  const lap = useCallback(() => clock.lap(), [clock]);
  return useMemo(() => ({ lap }), [lap]);
}

/**
 * Single-question stopwatch for flows where one question is on screen and
 * answering ends it (topic drills).
 */
export function useQuestionTimer(key: string | null): { seconds: () => number | undefined } {
  const clock = useMemo(() => createQuestionClock(), []);
  const lastKey = useRef<string | null | undefined>(undefined);
  useVisibility(clock);

  if (key !== lastKey.current) {
    lastKey.current = key;
    clock.focus(key);
  }

  const seconds = useCallback(
    () => (key === null ? undefined : clock.secondsFor(key)),
    [key, clock],
  );
  return useMemo(() => ({ seconds }), [seconds]);
}
