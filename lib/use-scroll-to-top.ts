"use client";

import { useEffect, useRef } from "react";

/**
 * Scrolls the window back to the top whenever `key` changes.
 *
 * Every paged surface on this site — test runners, practice drills, placement,
 * lesson steps — swaps content in place rather than navigating, so the browser
 * keeps the scroll offset from the PREVIOUS item. On a long problem the
 * student scrolls down to read it all, hits Next, and lands halfway down a
 * question whose heading is off-screen above them.
 *
 * Instant, not smooth: a long page animating back to the top is slower than
 * the tap that triggered it and reads as lag. Instant also sidesteps
 * prefers-reduced-motion, since there is no motion to reduce.
 *
 * The first render is skipped — on mount, the router has already positioned
 * the page (top on a fresh navigation, restored offset on a back), and
 * fighting that would break scroll restoration.
 */
export default function useScrollToTop(key: unknown, enabled = true): void {
  const first = useRef(true);

  useEffect(() => {
    if (first.current) {
      first.current = false;
      return;
    }
    if (!enabled) return;
    if (typeof window === "undefined") return;
    window.scrollTo({ top: 0, behavior: "auto" });
  }, [key, enabled]);
}
