import Link from "next/link";
import { Tc } from "@/components/T";
import { Archive, BarChart3, BookOpen, ChevronRight, FileText, Layers, Target } from "lucide-react";
import type { LucideIcon } from "lucide-react";

// THE hub design system — and the direction matters: the ЭШ hub's original
// design is the REFERENCE (owner, 2026-08-01: "make SAT and IB hubs like the
// old ЭШ design"). These primitives are extracted from that page so SAT and
// IB render in its idiom — wide shell, bordered stats header, accent
// progress banner, 2×2 icon action cards. Never the reverse: do not flatten
// the ЭШ hub to fit a simpler kit.
//
// Content language stays a HUB property (ЭШ Mongolian, SAT/IB English) —
// the kit carries no copy. Server-safe: no hooks; client hubs (ЭШ) can
// pass live values as props/children.

// ── Icons belong to the ROLE, not to the hub ────────────────────────────
//
// Cards used to carry their own `icon`, and the three hubs drifted into
// contradicting each other: BookOpen meant "course" on ЭШ and IB but
// "foundations" on SAT; the drill card was Target on ЭШ and Layers on
// SAT and IB; the SAT course card was Sparkles, used nowhere else. A
// student moving between hubs was being shown the same glyph for
// different things and different glyphs for the same thing.
//
// So a card declares WHAT IT IS and the kit decides how it looks. Adding
// a hub cannot introduce a new icon for an existing role, because there
// is no longer anywhere to put one.
export type HubCardRole =
  /** Full-length timed papers under exam conditions. */
  | "tests"
  /** Real past papers, as sat in previous years. */
  | "past-papers"
  /** The taught course — lessons in syllabus order. */
  | "course"
  /** Drill a chosen topic; the engine picks what to serve. */
  | "drill"
  /** The general-maths courses under /math, below this hub's level. */
  | "foundations"
  /** Analytics, score projection, weak-spot report. */
  | "progress";

export const HUB_ROLE_ICON: Record<HubCardRole, LucideIcon> = {
  tests: FileText,
  "past-papers": Archive,
  course: BookOpen,
  drill: Target,
  foundations: Layers,
  progress: BarChart3,
};

export function HubShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">{children}</div>
    </div>
  );
}

// Bordered header: eyebrow · big serif title · mono stats line, with an
// optional right-side block (the ЭШ hub puts the live average there).
export function HubHeader({
  eyebrow,
  title,
  statsLine,
  aside,
}: {
  eyebrow: string;
  title: string;
  statsLine?: React.ReactNode;
  aside?: React.ReactNode;
}) {
  return (
    <div
      className="flex items-end justify-between gap-3 mb-10 pb-6"
      style={{ borderBottom: "1px solid var(--line)" }}
    >
      <div>
        <div className="eyebrow mb-1.5"><Tc en={eyebrow} /></div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(32px, 4vw, 44px)",
            letterSpacing: "-0.03em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          <Tc en={title} />
        </h1>
        {statsLine && (
          <p className="mono mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {statsLine}
          </p>
        )}
      </div>
      {aside}
    </div>
  );
}

// The full-width accent banner above the action grid — the hub's progress /
// analytics destination.
// The banner is always the progress destination, so it always wears the
// progress icon. It used to take `icon` and all three hubs passed the
// same BarChart3 — a convention held up by nothing but three people
// remembering. Now it cannot differ.
export function HubProgressBanner({
  href,
  eyebrow,
  title,
  subtitle,
  cta,
}: {
  href: string;
  eyebrow: string;
  title: string;
  subtitle: string;
  cta: string;
}) {
  const Icon = HUB_ROLE_ICON.progress;
  return (
    <Link
      href={href}
      className="block mb-4 p-5 group transition-colors"
      style={{
        background: "var(--bg-1)",
        border: "1px solid var(--accent-line)",
        borderRadius: 12,
      }}
    >
      <div className="flex items-center gap-4">
        <div
          className="w-11 h-11 rounded-md flex items-center justify-center shrink-0"
          style={{
            background: "var(--accent-wash)",
            border: "1px solid var(--accent-line)",
            color: "var(--accent)",
          }}
        >
          <Icon className="w-5 h-5" />
        </div>
        <div className="flex-1 min-w-0">
          <div className="eyebrow" style={{ color: "var(--accent)" }}>
            <Tc en={eyebrow} />
          </div>
          <h2
            className="serif mt-1"
            style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.1 }}
          >
            <Tc en={title} />
          </h2>
          <p className="text-[13px] mt-1" style={{ color: "var(--fg-2)" }}>
            <Tc en={subtitle} />
          </p>
        </div>
        <span
          className="mono text-[11px] uppercase shrink-0 hidden sm:inline-flex items-center gap-1"
          style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
        >
          <Tc en={cta} />
          <ChevronRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
        </span>
        <ChevronRight
          className="w-5 h-5 sm:hidden transition-transform group-hover:translate-x-0.5"
          style={{ color: "var(--accent)" }}
        />
      </div>
    </Link>
  );
}

export interface HubActionCardDef {
  href: string;
  title: string;
  subtitle: string;
  /** What this card IS. The kit picks the icon — see HUB_ROLE_ICON. */
  role: HubCardRole;
  badge?: { label: string; tone: "accent" | "muted" };
}

// The 2×2 equal-weight action grid — each card: icon box top-left, chevron
// top-right, serif title with optional badge, subtitle.
export function HubActionGrid({ cards }: { cards: HubActionCardDef[] }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
      {cards.map((c) => {
        const Icon = HUB_ROLE_ICON[c.role];
        return (
          <Link key={c.href} href={c.href} className="card-edit p-6 group block">
            <div className="flex items-start justify-between mb-4">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--accent)" }}
              >
                <Icon className="w-4 h-4" />
              </div>
              <ChevronRight
                className="w-4 h-4 transition-transform group-hover:translate-x-0.5"
                style={{ color: "var(--fg-3)" }}
              />
            </div>
            <div className="flex items-center gap-2 mb-1.5 flex-wrap">
              <h2
                className="serif"
                style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)", lineHeight: 1.1 }}
              >
                <Tc en={c.title} />
              </h2>
              {c.badge && (
                <span
                  className="mono text-[10px] uppercase px-2 py-0.5 rounded-full"
                  style={
                    c.badge.tone === "accent"
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
                  <Tc en={c.badge.label} />
                </span>
              )}
            </div>
            <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              <Tc en={c.subtitle} />
            </p>
          </Link>
        );
      })}
    </div>
  );
}
