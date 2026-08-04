"use client";

import { createContext, useContext, useState, useEffect, type ReactNode } from "react";

type Lang = "en" | "mn";

/**
 * The path the browser actually LOADED, and the referrer it loaded with.
 *
 * Captured at module scope. This module is imported by the root layout, so it
 * is evaluated once per document load and never again — client-side
 * navigation does not re-run it. That makes these the entry conditions for
 * the whole session, which `document.referrer` alone cannot tell you: the App
 * Router leaves the referrer frozen at whatever the document loaded with, so
 * after a client-side navigation it still describes the PREVIOUS page.
 *
 * A landing page may use this to decide whether it was genuinely arrived at
 * from off-site, rather than reached by a link inside the site.
 */
export const ENTRY = {
  path: typeof window === "undefined" ? null : window.location.pathname.replace(/\/+$/, "") || "/",
  referrer: typeof window === "undefined" ? null : document.referrer,
};

/** True when the document was loaded directly at `path` from off-site. */
export function landedFromOffSite(path: string): boolean {
  if (typeof window === "undefined") return false;
  if (ENTRY.path !== path.replace(/\/+$/, "")) return false; // reached by in-site navigation
  const ref = ENTRY.referrer;
  if (!ref) return true; // direct hit: typed, bookmarked, or an app with no referrer
  try {
    return new URL(ref).origin !== window.location.origin;
  } catch {
    return true;
  }
}

const LangContext = createContext<{ lang: Lang; setLang: (l: Lang) => void }>({
  lang: "en",
  setLang: () => {},
});

export function LangProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>("en");

  useEffect(() => {
    const saved = localStorage.getItem("mp_lang") as Lang | null;
    if (saved === "en" || saved === "mn") setLangState(saved);
  }, []);

  function setLang(l: Lang) {
    setLangState(l);
    localStorage.setItem("mp_lang", l);
  }

  return <LangContext.Provider value={{ lang, setLang }}>{children}</LangContext.Provider>;
}

export function useLang() {
  return useContext(LangContext);
}
