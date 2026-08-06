"use client";

// The dashboard's gamification strip: streak, level, and today's goal ring.
//
// Deliberately NOT a scoreboard. There is no comparison to other students
// anywhere in here — the audience is minors and the only useful comparison is
// with yesterday's self. The streak line invites ("keep it going today") and
// never threatens; a broken streak is reported as a fact next to the personal
// best, not as a loss.

import { Flame, Star, Target } from "lucide-react";
import { useLang } from "@/lib/lang-context";
import type { GamificationSummary } from "@/lib/gamification";

const i18n = {
  eyebrow: { en: "Your momentum", mn: "Таны эрч" },
  streak: { en: "Day streak", mn: "Өдрийн цуваа" },
  streak_one: { en: "day", mn: "өдөр" },
  streak_many: { en: "days", mn: "өдөр" },
  best: { en: "Best", mn: "Дээд" },
  level: { en: "Level", mn: "Түвшин" },
  xp_to_next: { en: "XP to next level", mn: "Дараагийн түвшин хүртэл XP" },
  today: { en: "Today", mn: "Өнөөдөр" },
  of_goal: { en: "of", mn: "/" },
  goal_met: { en: "Daily goal met", mn: "Өдрийн зорилт биеллээ" },
  keep_going: { en: "Practice today to keep your streak going", mn: "Цувааг үргэлжлүүлэхийн тулд өнөөдөр хичээллээрэй" },
  start_streak: { en: "Answer one problem to start a streak", mn: "Нэг бодлого бодоод цуваагаа эхлүүлээрэй" },
  active_day: { en: "active day", mn: "идэвхтэй өдөр" },
  active_days: { en: "active days", mn: "идэвхтэй өдөр" },
  new_streak: { en: "Practice today to start a new streak", mn: "Шинэ цуваа эхлүүлэхийн тулд өнөөдөр хичээллээрэй" },
  next_up: { en: "Next up", mn: "Дараагийн зорилт" },
  capped: {
    en: "Totals count your 2000 most recent problems",
    mn: "Нийт тоо нь сүүлийн 2000 бодлогыг тооцно",
  },
};

/** A ring that fills clockwise from the top. */
function Ring({
  progress,
  size = 56,
  stroke = 5,
  color,
  children,
}: {
  progress: number;
  size?: number;
  stroke?: number;
  color: string;
  children?: React.ReactNode;
}) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const p = Math.max(0, Math.min(1, progress));
  return (
    <span className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} aria-hidden="true" style={{ transform: "rotate(-90deg)" }}>
        <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="var(--line)" strokeWidth={stroke} />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={color}
          strokeWidth={stroke}
          strokeLinecap="round"
          strokeDasharray={c}
          strokeDashoffset={c * (1 - p)}
          style={{ transition: "stroke-dashoffset 600ms ease" }}
        />
      </svg>
      <span className="absolute inset-0 flex items-center justify-center">{children}</span>
    </span>
  );
}

export default function ProgressStrip({ summary }: { summary: GamificationSummary }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";
  const { streak, level, daily, nextBadge } = summary;

  // The one-line status under the streak. Order matters: celebrate first,
  // invite second, and only explain the zero case last.
  const streakLine = streak.activeToday
    ? `${streak.totalActiveDays} ${streak.totalActiveDays === 1 ? i18n.active_day[L] : i18n.active_days[L]}`
    : streak.current > 0
      ? i18n.keep_going[L]
      : streak.longest > 0
        ? i18n.new_streak[L]
        : i18n.start_streak[L];

  return (
    <section className="card-edit p-5">
      <div className="eyebrow mb-4">{i18n.eyebrow[L]}</div>

      <div className="grid gap-5 sm:grid-cols-3">
        {/* Streak */}
        <div className="flex items-center gap-3">
          <span
            className="grid place-items-center rounded-full flex-shrink-0"
            style={{
              width: 56,
              height: 56,
              background: streak.current > 0 ? "var(--accent-wash)" : "var(--bg-2)",
              border: `1px solid ${streak.current > 0 ? "var(--accent-line)" : "var(--line)"}`,
              color: streak.current > 0 ? "var(--accent)" : "var(--fg-3)",
            }}
          >
            <Flame className="h-6 w-6" />
          </span>
          <div className="min-w-0">
            <div className="serif tabular" style={{ fontSize: 26, lineHeight: 1.1, color: "var(--fg)" }}>
              {streak.current}
              <span className="ml-1.5" style={{ fontSize: 13, color: "var(--fg-2)" }}>
                {streak.current === 1 ? i18n.streak_one[L] : i18n.streak_many[L]}
              </span>
            </div>
            <div className="text-[12px] mt-0.5" style={{ color: "var(--fg-2)" }}>
              {streakLine}
            </div>
            {streak.longest > streak.current && (
              <div className="mono text-[10px] uppercase mt-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {i18n.best[L]} {streak.longest}
              </div>
            )}
          </div>
        </div>

        {/* Level */}
        <div className="flex items-center gap-3">
          <Ring progress={level.progress} color="var(--accent)">
            <Star className="h-5 w-5" style={{ color: "var(--accent)" }} />
          </Ring>
          <div className="min-w-0">
            <div className="serif tabular" style={{ fontSize: 26, lineHeight: 1.1, color: "var(--fg)" }}>
              {level.level}
              <span className="ml-1.5" style={{ fontSize: 13, color: "var(--fg-2)" }}>
                {i18n.level[L]}
              </span>
            </div>
            <div className="text-[12px] mt-0.5 tabular" style={{ color: "var(--fg-2)" }}>
              {level.xpToNext} {i18n.xp_to_next[L]}
            </div>
          </div>
        </div>

        {/* Daily goal */}
        <div className="flex items-center gap-3">
          <Ring progress={daily.progress} color={daily.met ? "var(--ok, var(--accent))" : "var(--accent)"}>
            <span className="serif tabular text-[13px]" style={{ color: "var(--fg)" }}>
              {daily.done}
            </span>
          </Ring>
          <div className="min-w-0">
            <div className="serif" style={{ fontSize: 15, lineHeight: 1.2, color: "var(--fg)" }}>
              {i18n.today[L]}
            </div>
            <div className="text-[12px] mt-0.5 tabular" style={{ color: "var(--fg-2)" }}>
              {daily.met ? (
                i18n.goal_met[L]
              ) : (
                <>
                  {daily.done} {i18n.of_goal[L]} {daily.goal}
                </>
              )}
            </div>
            {daily.done > 0 && (
              <div className="flex items-center gap-1.5 mt-1">
                <Target className="h-3 w-3 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
                <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  {daily.correct}/{daily.done}
                </span>
              </div>
            )}
          </div>
        </div>
      </div>

      {nextBadge && (
        <div className="mt-5 pt-4" style={{ borderTop: "1px solid var(--line)" }}>
          <div className="flex items-center justify-between gap-4 flex-wrap">
            <div className="min-w-0">
              <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {i18n.next_up[L]}
              </span>
              <span className="ml-2 text-[13px]" style={{ color: "var(--fg-1)" }}>
                {L === "mn" ? nextBadge.mn : nextBadge.en}
                <span style={{ color: "var(--fg-3)" }}> — {L === "mn" ? nextBadge.descMn : nextBadge.descEn}</span>
              </span>
            </div>
            <span className="mono tabular text-[11px] flex-shrink-0" style={{ color: "var(--fg-2)" }}>
              {nextBadge.current}/{nextBadge.threshold}
            </span>
          </div>
          <div className="mt-2 h-1 rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
            <div
              className="h-full rounded-full"
              style={{
                width: `${Math.round(nextBadge.progress * 100)}%`,
                background: "var(--accent)",
                transition: "width 600ms ease",
              }}
            />
          </div>
        </div>
      )}

      {summary.attemptsAreCapped && (
        <p className="mt-3 text-[11px]" style={{ color: "var(--fg-3)" }}>
          {i18n.capped[L]}
        </p>
      )}
    </section>
  );
}
