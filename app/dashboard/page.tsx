"use client";

import { useState } from "react";
import Link from "next/link";
import usePerformance from "@/lib/use-performance";
import { useAuth } from "@/lib/auth-context";

const STREAK_DAYS = [0, 0, 1, 2, 2, 3, 1, 0, 0, 2, 3, 3, 4, 2, 0, 2, 3, 4, 3, 4, 4, 3, 3, 4, 4, 3, 4, 4];

const PLAN = [
  { t: "Warm-up drill · mixed algebra", minutes: 8, done: true },
  { t: "AI problems · definite integration · 5 qs", minutes: 14, done: false },
  { t: "Mini-lesson · sequences & limits", minutes: 8, done: false },
  { t: "Timed mixed-calc drill · 15 qs", minutes: 15, done: false },
];

export default function DashboardPage() {
  const perf = usePerformance();
  const { user } = useAuth();
  const overall = perf.getOverallStats();
  const weakTopics = perf.getWeakTopics();
  const topicStats = perf.getTopicStats();
  const [plan, setPlan] = useState(PLAN);

  const completed = plan.filter((p) => p.done).length;
  const minutesLeft = plan.filter((p) => !p.done).reduce((s, p) => s + p.minutes, 0);
  const predicted = overall.total > 0 ? Math.min(800, Math.round(560 + (overall.accuracy / 100) * 240)) : 742;
  const daysToExam = 57;
  const streakDays = 12;
  const firstName = user?.displayName?.split(" ")[0] || "Эрдэнэ";

  return (
    <div className="min-h-screen pt-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-7xl mx-auto px-6 md:px-10 py-10 md:py-12">
        {/* Welcome row */}
        <section
          className="grid gap-10 items-end pb-7"
          style={{ gridTemplateColumns: "minmax(0, 1.2fr) minmax(0, 1fr)", borderBottom: "1px solid var(--line)" }}
        >
          <div>
            <div className="eyebrow">Welcome back · {firstName}</div>
            <h1
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: "clamp(48px, 6vw, 72px)",
                letterSpacing: "-0.04em",
                lineHeight: 0.96,
                margin: "8px 0 0",
                color: "var(--fg)",
              }}
            >
              Сайн уу, <em className="serif-italic" style={{ color: "var(--accent)" }}>{firstName}</em>.
            </h1>
            <p className="mt-3 text-[15px]" style={{ color: "var(--fg-2)" }}>
              ЭЕШ хүртэл {daysToExam} өдөр. Та{" "}
              <strong style={{ color: "var(--accent)" }}>{streakDays} өдрийн турш</strong> тасралтгүй бэлдэж байна.
            </p>
          </div>

          {/* Countdown grid */}
          <div
            className="card-edit overflow-hidden"
            style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", borderRadius: 14 }}
          >
            {[
              { big: daysToExam, lbl: "days to exam", color: "var(--fg)" },
              { big: predicted, lbl: "projected", color: "var(--accent)" },
              { big: streakDays, lbl: "day streak", color: "var(--fg)" },
              { big: weakTopics.length || 6, lbl: "weak topics", color: "var(--fg)" },
            ].map((it, i) => (
              <div
                key={it.lbl}
                className="px-5 py-5 text-center"
                style={{ borderRight: i < 3 ? "1px solid var(--line)" : "none" }}
              >
                <div className="serif tabular" style={{ fontSize: 36, lineHeight: 1, letterSpacing: "-0.03em", color: it.color }}>
                  {it.big}
                </div>
                <div className="eyebrow mt-1.5" style={{ fontSize: 10 }}>
                  {it.lbl}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Two-column body */}
        <section
          className="grid gap-5 mt-7"
          style={{ gridTemplateColumns: "minmax(0, 1.6fr) minmax(0, 1fr)" }}
        >
          {/* LEFT */}
          <div className="grid gap-5">
            {/* Today's plan */}
            <div className="card-edit p-6 md:p-7 flex flex-col">
              <div className="eyebrow">
                Today · {new Date().toLocaleDateString("en-US", { month: "short", day: "numeric" })}
              </div>
              <h3 className="serif mt-2 mb-2" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                Your 45-minute plan
              </h3>
              <p className="text-sm" style={{ color: "var(--fg-1)" }}>
                Focused on the two topics moving your score most. Swap or skip anything.
              </p>
              <ul className="list-none p-0 mt-5">
                {plan.map((p, i) => (
                  <li
                    key={p.t}
                    className="grid items-center gap-3.5 py-3.5"
                    style={{
                      gridTemplateColumns: "32px 1fr auto",
                      borderTop: i === 0 ? "none" : "1px solid var(--line)",
                      fontSize: 14,
                    }}
                  >
                    <button
                      onClick={() => setPlan((arr) => arr.map((x, j) => (j === i ? { ...x, done: !x.done } : x)))}
                      className="flex items-center justify-center"
                      style={{
                        width: 20,
                        height: 20,
                        borderRadius: 4,
                        border: `1px solid ${p.done ? "var(--accent)" : "var(--line-strong)"}`,
                        background: p.done ? "var(--accent)" : "transparent",
                        color: p.done ? "var(--accent-ink)" : "transparent",
                        fontSize: 14,
                        cursor: "pointer",
                      }}
                    >
                      ✓
                    </button>
                    <div style={{ color: p.done ? "var(--fg-3)" : "var(--fg)", textDecoration: p.done ? "line-through" : "none" }}>
                      {p.t}
                    </div>
                    <div className="mono" style={{ fontSize: 11, color: p.done ? "var(--accent)" : "var(--fg-3)", letterSpacing: "0.06em" }}>
                      {p.minutes} MIN
                    </div>
                  </li>
                ))}
              </ul>
              <div className="mt-5 flex justify-between items-center">
                <span className="eyebrow">
                  {completed} OF {plan.length} COMPLETE · {minutesLeft} MIN LEFT
                </span>
                <Link href="/ai" className="btn btn-primary">Continue plan →</Link>
              </div>
            </div>

            {/* Streak */}
            <div className="card-edit p-6 md:p-7">
              <div className="eyebrow">Practice streak · last 28 days</div>
              <h3 className="serif mt-2" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                {streakDays} days in a row.
              </h3>
              <div
                className="mt-4 grid gap-1"
                style={{ gridTemplateColumns: "repeat(28, 1fr)" }}
              >
                {STREAK_DAYS.map((v, i) => (
                  <span
                    key={i}
                    style={{
                      aspectRatio: "1",
                      borderRadius: 2,
                      background: v === 0 ? "var(--bg-3)" : "var(--accent)",
                      opacity: v === 0 ? 1 : 0.2 + v * 0.2,
                    }}
                  />
                ))}
              </div>
              <div className="mt-3 mono flex justify-between items-center" style={{ fontSize: 11, color: "var(--fg-3)" }}>
                <span>LESS</span>
                <div className="flex gap-0.5">
                  <span style={{ width: 12, height: 12, background: "var(--bg-3)" }} />
                  <span style={{ width: 12, height: 12, background: "var(--accent)", opacity: 0.35 }} />
                  <span style={{ width: 12, height: 12, background: "var(--accent)", opacity: 0.6 }} />
                  <span style={{ width: 12, height: 12, background: "var(--accent)", opacity: 0.85 }} />
                  <span style={{ width: 12, height: 12, background: "var(--accent)" }} />
                </div>
                <span>MORE</span>
              </div>
            </div>

            {/* Quick links */}
            <div className="grid gap-3" style={{ gridTemplateColumns: "repeat(3, 1fr)" }}>
              {[
                { to: "/practice", eye: "Practice", t: "Take a test →" },
                { to: "/analytics", eye: "Analytics", t: "Full report →" },
                { to: "/ai", eye: "AI tutor", t: "Generate problems →" },
              ].map((l) => (
                <Link
                  key={l.to}
                  href={l.to}
                  className="card-edit p-5 block"
                  style={{ textDecoration: "none" }}
                >
                  <div className="eyebrow">{l.eye}</div>
                  <div className="serif mt-1" style={{ fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    {l.t}
                  </div>
                </Link>
              ))}
            </div>
          </div>

          {/* RIGHT */}
          <div className="grid gap-5">
            {/* Focus card */}
            <div
              className="card-edit p-6 md:p-7 flex flex-col"
              style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
            >
              <div className="eyebrow" style={{ color: "var(--accent)" }}>This week · focus</div>
              <h3
                className="serif mt-2 mb-2"
                style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--accent)" }}
              >
                Close the integration gap.
              </h3>
              <p className="text-sm" style={{ color: "var(--fg-1)" }}>
                You&apos;re losing ~24 points to definite integration and limits. Moving these to 65% lifts your projection to{" "}
                <strong>{Math.min(800, predicted + 26)}</strong>.
              </p>
              <div className="mt-5 grid gap-2">
                {(topicStats.length > 0
                  ? topicStats.slice(0, 2)
                  : [
                      { topic: "integration", label: "Definite integration", accuracy: 38 },
                      { topic: "sequences", label: "Sequences · limits", accuracy: 41 },
                    ]
                ).map((s) => (
                  <div
                    key={s.topic}
                    className="flex justify-between items-center px-3 py-3 rounded-lg text-sm"
                    style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
                  >
                    <span style={{ color: "var(--fg-1)" }}>{s.label}</span>
                    <span className="mono" style={{ color: "var(--warn)" }}>{s.accuracy}%</span>
                  </div>
                ))}
              </div>
              <Link href="/ai" className="btn btn-primary mt-4 self-start">Drill now →</Link>
            </div>

            {/* Tutor */}
            <div className="card-edit p-6 md:p-7">
              <div className="eyebrow">Upcoming · tutor</div>
              <div className="mt-3 flex gap-3 items-center">
                <div
                  className="serif"
                  style={{
                    width: 48,
                    height: 48,
                    borderRadius: 99,
                    background: "var(--bg-3)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: 18,
                    color: "var(--fg)",
                  }}
                >
                  ДЭ
                </div>
                <div>
                  <div className="serif" style={{ fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>Д. Энхжаргал</div>
                  <div className="eyebrow mt-0.5">FRI · MAR 28 · 19:00 UB</div>
                </div>
              </div>
              <p className="serif mt-4" style={{ fontSize: 14, color: "var(--fg-1)", lineHeight: 1.55 }}>
                &ldquo;Let&apos;s do u-substitution patterns — I&apos;ll bring 6 problems calibrated to your gap.&rdquo;
              </p>
              <div className="flex gap-2 mt-3">
                <button className="btn btn-line" style={{ fontSize: 12, padding: "7px 12px" }}>Reschedule</button>
                <button className="btn btn-ghost" style={{ fontSize: 12, padding: "7px 12px" }}>Message</button>
              </div>
            </div>

            {/* Latest report preview */}
            <Link href="/analytics" className="card-edit p-6 md:p-7 block" style={{ textDecoration: "none" }}>
              <div className="eyebrow">Latest report · Week 8</div>
              <div className="flex justify-between items-baseline mt-2">
                <div className="serif" style={{ fontSize: 56, letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
                  {predicted}
                  <span className="mono ml-1" style={{ fontSize: 16, color: "var(--fg-3)" }}>/800</span>
                </div>
                <div className="mono" style={{ fontSize: 11, color: "var(--accent)" }}>▲ +62 PTS</div>
              </div>
              <svg viewBox="0 0 300 60" preserveAspectRatio="none" width="100%" height="60" style={{ marginTop: 12 }}>
                <defs>
                  <linearGradient id="hg" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0" stopColor="var(--accent)" stopOpacity={0.3} />
                    <stop offset="1" stopColor="var(--accent)" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <path
                  d="M0,48 C40,44 80,38 120,32 C160,26 200,20 240,14 C260,11 290,6 300,4 L300,60 L0,60 Z"
                  fill="url(#hg)"
                />
                <path
                  d="M0,48 C40,44 80,38 120,32 C160,26 200,20 240,14 C260,11 290,6 300,4"
                  fill="none"
                  stroke="var(--accent)"
                  strokeWidth={1.5}
                />
              </svg>
              <div className="eyebrow mt-2.5">VIEW FULL REPORT →</div>
            </Link>
          </div>
        </section>
      </div>
    </div>
  );
}
