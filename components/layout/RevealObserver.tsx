"use client";

import { useEffect } from "react";
import { usePathname } from "next/navigation";

// Scroll-reveal. Marks <html> with `js-reveal` so the CSS in globals.css is
// allowed to hide `[data-reveal]` elements, then lets each one in as it
// enters the viewport. Without the marker class nothing is ever hidden, so a
// slow or failed script leaves the page fully readable. Elements already in
// view on load are revealed on the first observer callback, with the stagger
// coming from each element's own --reveal-delay.
export default function RevealObserver() {
  const pathname = usePathname();

  useEffect(() => {
    const root = document.documentElement;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce || typeof IntersectionObserver === "undefined") {
      root.classList.remove("js-reveal");
      return;
    }
    root.classList.add("js-reveal");

    const io = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            e.target.classList.add("is-in");
            io.unobserve(e.target);
          }
        }
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );

    const attach = () => {
      document.querySelectorAll<HTMLElement>("[data-reveal]:not(.is-in)").forEach((el) => io.observe(el));
    };
    attach();

    // Client-side navigation and lazily rendered sections add nodes after
    // mount; pick them up without re-running the effect.
    const mo = new MutationObserver(() => attach());
    mo.observe(document.body, { childList: true, subtree: true });

    return () => {
      io.disconnect();
      mo.disconnect();
    };
    // Re-run per route so a fresh page's elements are observed from scratch.
  }, [pathname]);

  return null;
}
