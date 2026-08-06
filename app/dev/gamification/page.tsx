"use client";

// Dev-only preview for the gamification surfaces. Renders ProgressStrip and
// BadgeShelf against synthetic attempt logs — a brand-new student, a steady
// fortnight, a broken streak, a one-night binge — so the copy and the tuning
// can be eyeballed side by side without seeding a real account.
//
// The profiles are built as ATTEMPT LOGS and run through the real
// `summarize()`, not hand-written summaries. A preview that fakes its numbers
// would happily show a layout the production path can never produce.
//
// Gated to non-production via NODE_ENV, matching app/dev/section2-preview.

import { notFound } from "next/navigation";
import { summarize } from "@/lib/gamification";
import type { AttemptRecord } from "@/lib/use-performance";
import ProgressStrip from "@/components/gamification/ProgressStrip";
import BadgeShelf from "@/components/gamification/BadgeShelf";

const isDev = process.env.NODE_ENV !== "production";
const DAY = 86_400_000;

function mk(ts: number, ok: boolean, i: number, ctx = "esh", topic = "algebra"): AttemptRecord {
  return {
    questionSource: `preview-${i}`,
    topic,
    subtopic: "",
    selectedAnswer: "A",
    correctAnswer: ok ? "A" : "B",
    isCorrect: ok,
    timestamp: ts,
    context: ctx,
    source: "drill",
  };
}

function steady(now: number, days: number, perDay: number, offsetDays = 0): AttemptRecord[] {
  const rows: AttemptRecord[] = [];
  let i = 0;
  for (let d = 0; d < days; d++) {
    for (let n = 0; n < perDay; n++) {
      rows.push(mk(now - (d + offsetDays) * DAY - n * 60_000, n % 4 !== 0, i++));
    }
  }
  return rows;
}

const PROFILES: { name: string; note: string; rows: (now: number) => AttemptRecord[] }[] = [
  {
    name: "Brand new",
    note: "3 problems, first day — the very first thing a student sees",
    rows: (now) => [mk(now - 60_000, true, 1), mk(now - 120_000, false, 2), mk(now - 180_000, true, 3)],
  },
  {
    name: "One good session",
    note: "15 problems today, nothing before",
    rows: (now) => Array.from({ length: 15 }, (_, i) => mk(now - i * 60_000, i % 5 !== 0, i)),
  },
  {
    name: "Two steady weeks",
    note: "12 a day for 14 days — the shape the design rewards",
    rows: (now) => steady(now, 14, 12),
  },
  {
    name: "One-night binge",
    note: "300 problems in a single night — must NOT out-score the fortnight above",
    rows: (now) => Array.from({ length: 300 }, (_, i) => mk(now - i * 30_000, i % 4 !== 0, i)),
  },
  {
    name: "Streak broken",
    note: "10 solid days, then three days off — best is kept, tone stays kind",
    rows: (now) => steady(now, 10, 12, 3),
  },
  {
    name: "Breadth",
    note: "Across ЭЕШ, a course and IB — the explorer badge",
    rows: (now) => [
      ...Array.from({ length: 8 }, (_, i) => mk(now - i * 60_000, true, i, "esh", "algebra")),
      ...Array.from({ length: 8 }, (_, i) => mk(now - DAY - i * 60_000, true, 100 + i, "course:geometry", "circles")),
      ...Array.from({ length: 8 }, (_, i) => mk(now - 2 * DAY - i * 60_000, true, 200 + i, "course:ib-ai-sl", "calculus")),
    ],
  },
];

export default function GamificationPreviewPage() {
  if (!isDev) notFound();

  // Fixed clock so the preview is stable to look at and to screenshot.
  const now = new Date(2026, 5, 10, 20, 0, 0).getTime();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="eyebrow mb-2">Dev preview</div>
        <h1 className="serif mb-2" style={{ fontWeight: 400, fontSize: 34, color: "var(--fg)" }}>
          Gamification surfaces
        </h1>
        <p className="mb-10 text-[14px]" style={{ color: "var(--fg-2)", maxWidth: "60ch" }}>
          Six synthetic attempt logs run through the real{" "}
          <code className="mono text-[12px]">summarize()</code>. Clock pinned to 10 June 2026, 20:00.
        </p>

        <div className="space-y-12">
          {PROFILES.map((p) => {
            const summary = summarize(p.rows(now), now);
            return (
              <section key={p.name}>
                <div className="mb-3">
                  <h2 className="serif" style={{ fontWeight: 400, fontSize: 20, color: "var(--fg)" }}>
                    {p.name}
                  </h2>
                  <p className="text-[13px]" style={{ color: "var(--fg-3)" }}>
                    {p.note} · <span className="mono tabular">L{summary.level.level} · {summary.level.xp} xp</span>
                  </p>
                </div>
                <div className="space-y-4">
                  <ProgressStrip summary={summary} />
                  <BadgeShelf badges={summary.badges} />
                </div>
              </section>
            );
          })}
        </div>
      </div>
    </div>
  );
}
