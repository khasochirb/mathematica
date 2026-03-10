"use client";

import { useLang } from "@/lib/lang-context";

interface TProps {
  en: string;
  mn: string;
}

/** Renders the correct language string based on the active lang context. */
export function T({ en, mn }: TProps) {
  const { lang } = useLang();
  return <>{lang === "mn" ? mn : en}</>;
}
