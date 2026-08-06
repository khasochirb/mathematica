"use client";

// The badge shelf. Every badge is always visible, earned or not, with the
// unearned ones showing real progress rather than a question mark — a student
// should be able to see what the platform values and how close they are, not
// be teased with a locked mystery.

import {
  CalendarCheck,
  CalendarDays,
  CalendarHeart,
  Compass,
  Crosshair,
  Crown,
  Flame,
  Footprints,
  Layers,
  Medal,
  Target,
  Trophy,
  type LucideIcon,
} from "lucide-react";
import { useLang } from "@/lib/lang-context";
import type { Badge } from "@/lib/gamification";

// Explicit map, not a dynamic lookup: a bundler can only tree-shake icons it
// can see, and a typo becomes a build error here instead of a blank square.
const ICONS: Record<string, LucideIcon> = {
  Footprints,
  Flame,
  Trophy,
  Medal,
  CalendarCheck,
  CalendarHeart,
  Crown,
  Target,
  Crosshair,
  Compass,
  Layers,
  CalendarDays,
};

const i18n = {
  eyebrow: { en: "Badges", mn: "Тэмдэг" },
  earned: { en: "earned", mn: "авсан" },
};

export default function BadgeShelf({ badges }: { badges: Badge[] }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";
  const earned = badges.filter((b) => b.earned).length;

  // Earned first, then whatever is closest — the shelf reads as a record of
  // what you did, followed by what is within reach.
  const ordered = [...badges].sort((a, b) => {
    if (a.earned !== b.earned) return a.earned ? -1 : 1;
    return b.progress - a.progress;
  });

  return (
    <section className="card-edit p-5">
      <div className="flex items-baseline justify-between gap-3 mb-4">
        <div className="eyebrow">{i18n.eyebrow[L]}</div>
        <span className="mono tabular text-[11px]" style={{ color: "var(--fg-3)" }}>
          {earned}/{badges.length} {i18n.earned[L]}
        </span>
      </div>

      <ul className="grid gap-3 grid-cols-2 sm:grid-cols-3 lg:grid-cols-4">
        {ordered.map((b) => {
          const Icon = ICONS[b.icon] ?? Trophy;
          return (
            <li
              key={b.slug}
              className="rounded-lg p-3 flex items-start gap-2.5"
              style={{
                background: b.earned ? "var(--accent-wash)" : "var(--bg-1)",
                border: `1px solid ${b.earned ? "var(--accent-line)" : "var(--line)"}`,
              }}
            >
              <span
                className="grid place-items-center rounded-md flex-shrink-0 mt-0.5"
                style={{
                  width: 30,
                  height: 30,
                  background: b.earned ? "var(--accent)" : "var(--bg-2)",
                  color: b.earned ? "var(--accent-ink, #fff)" : "var(--fg-3)",
                }}
              >
                <Icon className="h-4 w-4" />
              </span>
              <span className="min-w-0 flex-1">
                <span
                  className="serif block text-[13px] leading-tight"
                  style={{ color: b.earned ? "var(--fg)" : "var(--fg-1)" }}
                >
                  {L === "mn" ? b.mn : b.en}
                </span>
                <span className="block text-[11px] mt-0.5 leading-snug" style={{ color: "var(--fg-3)" }}>
                  {L === "mn" ? b.descMn : b.descEn}
                </span>
                {!b.earned && (
                  <>
                    <span
                      className="mt-1.5 block h-1 rounded-full overflow-hidden"
                      style={{ background: "var(--bg-2)" }}
                    >
                      <span
                        className="block h-full rounded-full"
                        style={{ width: `${Math.round(b.progress * 100)}%`, background: "var(--accent)" }}
                      />
                    </span>
                    <span className="mono tabular text-[10px] mt-1 block" style={{ color: "var(--fg-3)" }}>
                      {b.current}/{b.threshold}
                    </span>
                  </>
                )}
              </span>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
