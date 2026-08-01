import Link from "next/link";
import { ArrowRight } from "lucide-react";
import type { LucideIcon } from "lucide-react";

// THE hub skeleton — ЭЕШ, SAT and IB hub landing pages are all built from
// these four pieces, in the same canonical order:
//
//   <HubShell>
//     <HubHero .../>            1. eyebrow · italic-accent title · lede
//     <HubSection> tests        2. the hub's full-length sittings
//     <HubSection> the course   3. the taught curriculum
//     <HubSection> by topic     4. the drill bank
//     <HubSection> progress     5. analytics / weakness practice
//     ...hub-specific extras    (recommendations, recents, roadmap)
//   </HubShell>
//
// Content language stays a HUB property (ЭЕШ Mongolian, SAT/IB English) —
// this kit carries no copy, only structure. Server-safe: no hooks, so the
// SAT/IB pages stay server components; the ЭЕШ page uses it from a client
// component. If a hub page stops using this kit, it has drifted — that is
// the review flag.

export function HubShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {children}
      </div>
    </div>
  );
}

export function HubHero({
  eyebrow,
  title,
  accent,
  titleAfter,
  lede,
  statsLine,
}: {
  eyebrow: string;
  /** Text before the accent word. */
  title: string;
  /** The italic accent word (rendered serif-italic in the accent color). */
  accent: string;
  /** Text after the accent word (punctuation usually lives here). */
  titleAfter?: string;
  lede: string;
  /** Optional mono stats line under the lede, e.g. "34 тест · 1,224 бодлого". */
  statsLine?: React.ReactNode;
}) {
  return (
    <>
      <div className="eyebrow mb-4">{eyebrow}</div>
      <h1
        className="serif"
        style={{
          fontWeight: 400,
          fontSize: "clamp(36px, 6vw, 56px)",
          letterSpacing: "-0.04em",
          lineHeight: 1.0,
          color: "var(--fg)",
        }}
      >
        {title}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>
          {accent}
        </em>
        {titleAfter}
      </h1>
      <p className="text-[15px] mt-4" style={{ color: "var(--fg-2)", maxWidth: "52ch" }}>
        {lede}
      </p>
      {statsLine && (
        <p className="mono mt-3 text-[12px]" style={{ color: "var(--fg-2)" }}>
          {statsLine}
        </p>
      )}
    </>
  );
}

export function HubSection({
  label,
  children,
}: {
  label: string;
  children: React.ReactNode;
}) {
  return (
    <>
      <div className="eyebrow mt-10 mb-3">{label}</div>
      {children}
    </>
  );
}

// The standard destination card: icon · title · one-line description · arrow.
// Optional trailing badge ("Үнэгүй", "Live", "Түгжээтэй") after the title.
export function HubRowLink({
  href,
  icon: Icon,
  title,
  desc,
  badge,
  badgeTone = "accent",
  onClick,
}: {
  href: string;
  icon: LucideIcon;
  title: string;
  desc: string;
  badge?: string;
  badgeTone?: "accent" | "muted";
  onClick?: () => void;
}) {
  return (
    <Link
      href={href}
      onClick={onClick}
      className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
      style={{ display: "flex", textDecoration: "none" }}
    >
      <span className="inline-flex items-start gap-2.5" style={{ color: "var(--fg-1)" }}>
        <Icon className="h-4 w-4 mt-[3px] shrink-0" style={{ color: "var(--fg-2)" }} />
        <span>
          <span className="inline-flex items-center gap-2 flex-wrap">
            <span style={{ color: "var(--fg)" }}>{title}</span>
            {badge && (
              <span
                className="mono text-[10px] uppercase px-1.5 py-0.5 rounded-full"
                style={
                  badgeTone === "accent"
                    ? {
                        background: "color-mix(in oklch, var(--accent) 14%, transparent)",
                        color: "var(--accent)",
                        letterSpacing: "0.08em",
                      }
                    : {
                        background: "var(--bg-2)",
                        border: "1px solid var(--line)",
                        color: "var(--fg-3)",
                        letterSpacing: "0.08em",
                      }
                }
              >
                {badge}
              </span>
            )}
          </span>
          <span className="block text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>
            {desc}
          </span>
        </span>
      </span>
      <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
    </Link>
  );
}
