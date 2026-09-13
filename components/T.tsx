"use client";

import { useLang } from "@/lib/lang-context";
import { chrome } from "@/lib/i18n/chrome";

interface TProps {
  en: string;
  mn: string;
}

/** Renders the correct language string based on the active lang context. */
export function T({ en, mn }: TProps) {
  const { lang } = useLang();
  return <>{lang === "mn" ? mn : en}</>;
}

/**
 * A chrome-dictionary text node — the client leaf a SERVER component needs.
 *
 * Half the app's pages are server components, so they cannot call `useLang()`
 * and cannot call `chrome()`. Until now that left them with no way to localise
 * at all short of converting the whole page to a client component, which is
 * why 47 server pages sat un-wired.
 *
 * `<Tc>` is the smallest possible client boundary: the server page keeps
 * passing plain English props, and only this one text node re-renders on the
 * language toggle.
 *
 *   <div className="eyebrow"><Tc en={eyebrow} /></div>
 *
 * Prefer `chrome(en, lang)` directly inside a component that already has
 * `lang`; reach for this only when the surrounding component is server-side.
 * The English string stays the dictionary key, so a missing entry renders the
 * English exactly as `chrome()` does.
 */
export function Tc({ en }: { en: string }) {
  const { lang } = useLang();
  return <>{chrome(en, lang)}</>;
}
