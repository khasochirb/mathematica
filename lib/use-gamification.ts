"use client";

// Client gathering for the gamification layer: hand the attempt log to the
// pure module in lib/gamification.ts and memoize the result.
//
// The clock is pinned on MOUNT rather than read during render. Two reasons:
// a render-time Date.now() makes the component impure and re-derives on every
// render, and — worse — the server and client would read different clocks, so
// a render that straddles midnight would hydrate with a different streak than
// it painted. One value, set once, refreshed only when the day actually turns.

import { useEffect, useMemo, useState } from "react";
import usePerformance from "@/lib/use-performance";
import { summarize, dayKey, type GamificationSummary } from "@/lib/gamification";

export interface UseGamification {
  summary: GamificationSummary | null;
  /** False until the clock is pinned client-side; render nothing before then. */
  ready: boolean;
}

export default function useGamification(): UseGamification {
  const perf = usePerformance();
  const [now, setNow] = useState<number | null>(null);

  useEffect(() => {
    setNow(Date.now());

    // A dashboard left open overnight should roll its own day over rather
    // than show yesterday's streak until the tab is reloaded. Checking each
    // minute is far cheaper than it sounds and only ever sets state on the
    // one tick where the day key actually changes.
    const id = setInterval(() => {
      setNow((prev) => {
        const next = Date.now();
        return prev !== null && dayKey(prev) === dayKey(next) ? prev : next;
      });
    }, 60_000);
    return () => clearInterval(id);
  }, []);

  const summary = useMemo(
    () => (now === null ? null : summarize(perf.attempts, now)),
    [perf.attempts, now],
  );

  return { summary, ready: now !== null && perf.status !== "loading" };
}
