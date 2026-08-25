"use client";

import { useLang } from "@/lib/lang-context";
import { useTheme } from "@/lib/theme-context";

// Theme and language as labelled settings rows.
//
// Both already work — the header carries the same two toggles and this
// calls the same contexts. What the header cannot do is SAY what they are:
// a sun icon and the letters "MN" are discoverable only if you already
// know. A settings page is where a control gets a name.
//
// "This device" is not a hedge. Both values live in localStorage
// (lib/theme-context.tsx:24, lib/lang-context.tsx:53) and nothing syncs
// them to the account, so a student who sets Mongolian on the family
// desktop still gets English on their phone. Saying so is better than
// letting them find out.
//
// NOTE for whoever moves this file: lib/lang-autoswitch.test.ts holds an
// allowlist of files permitted to call setLang, and this path is on it.
// The rule exists because /tutoring quietly switches ad traffic to
// Mongolian only when no preference has been saved yet — so nothing here
// may write mp_lang except in direct response to a click.
export default function PreferencesPanel() {
  const { lang, setLang } = useLang();
  const { theme, toggle } = useTheme();
  const mn = lang === "mn";

  const row = {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    gap: 16,
    padding: "14px 0",
    borderTop: "1px solid var(--line)",
  } as const;

  const choice = (on: boolean) =>
    ({
      padding: "6px 14px",
      fontSize: 13,
      fontWeight: on ? 600 : 500,
      borderRadius: 8,
      border: `1px solid ${on ? "var(--accent)" : "var(--line)"}`,
      background: on ? "var(--accent-wash)" : "transparent",
      color: on ? "var(--accent)" : "var(--fg-2)",
      cursor: "pointer",
    }) as const;

  return (
    <div className="card-edit p-6 mt-8" style={{ scrollMarginTop: 80 }} id="preferences">
      <div className="eyebrow">{mn ? "Тохиргоо" : "Preferences"}</div>
      <h2
        className="serif mt-1"
        style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", lineHeight: 1.1 }}
      >
        {mn ? "Харагдах байдал" : "Appearance"}
      </h2>
      <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
        {mn
          ? "Эдгээр тохиргоо зөвхөн энэ төхөөрөмж дээр хадгалагдана."
          : "These are saved on this device only — not to your account."}
      </p>

      <div style={row}>
        <div>
          <div className="text-[14px]" style={{ color: "var(--fg)" }}>
            {mn ? "Загвар" : "Theme"}
          </div>
          <div className="text-[12px]" style={{ color: "var(--fg-3)" }}>
            {mn ? "Гэрэл эсвэл харанхуй" : "Light or dark"}
          </div>
        </div>
        <div className="flex gap-2">
          <button type="button" onClick={() => theme !== "light" && toggle()} style={choice(theme === "light")} aria-pressed={theme === "light"}>
            {mn ? "Гэрэл" : "Light"}
          </button>
          <button type="button" onClick={() => theme !== "dark" && toggle()} style={choice(theme === "dark")} aria-pressed={theme === "dark"}>
            {mn ? "Харанхуй" : "Dark"}
          </button>
        </div>
      </div>

      <div style={row}>
        <div>
          <div className="text-[14px]" style={{ color: "var(--fg)" }}>
            {mn ? "Хэл" : "Language"}
          </div>
          <div className="text-[12px]" style={{ color: "var(--fg-3)" }}>
            {mn
              ? "Цэс, товчлуурын хэл. Бодлогын хэл өөрчлөгдөхгүй."
              : "Menus and buttons. Question content is set by each hub and does not change."}
          </div>
        </div>
        <div className="flex gap-2">
          <button type="button" onClick={() => setLang("en")} style={choice(lang === "en")} aria-pressed={lang === "en"}>
            English
          </button>
          <button type="button" onClick={() => setLang("mn")} style={choice(lang === "mn")} aria-pressed={lang === "mn"}>
            Монгол
          </button>
        </div>
      </div>
    </div>
  );
}
