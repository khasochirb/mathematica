"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { BarChart3, ArrowRight, Target, Lock } from "lucide-react";
import { api, type TopicProgress, type StreakData, type AchievementWithStatus } from "@/lib/api";
import { useAuth } from "@/lib/auth-context";

const iconMap: Record<string, string> = {
  first_problem: "→",
  streak_3: "△",
  streak_7: "◇",
  streak_30: "◯",
  perfect_session: "✦",
  speed_demon: "⟶",
  century: "100",
  default: "✓",
};

export default function ProgressPage() {
  const { user, loading: authLoading } = useAuth();
  const [progress, setProgress] = useState<TopicProgress[]>([]);
  const [streak, setStreak] = useState<StreakData | null>(null);
  const [achievements, setAchievements] = useState<AchievementWithStatus[]>([]);
  const [subStatus, setSubStatus] = useState<{ isSubscribed: boolean } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      if (!user) { setLoading(false); return; }
      try {
        const [streakData, achData, subData] = await Promise.all([
          api.streaks.get(),
          api.achievements.all(),
          api.subscription.status(),
        ]);
        setStreak(streakData);
        setAchievements(achData);
        setSubStatus(subData);

        if (subData.isSubscribed) {
          try {
            const prog = await api.progress.all();
            setProgress(prog);
          } catch {
            // ignore if fails
          }
        }
      } catch {
        // fallback
      } finally {
        setLoading(false);
      }
    }
    if (!authLoading) load();
  }, [user, authLoading]);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20" style={{ background: "var(--bg)" }}>
        <div
          className="w-8 h-8 border-2 rounded-full animate-spin"
          style={{ borderColor: "var(--accent)", borderTopColor: "transparent" }}
        />
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20 px-4" style={{ background: "var(--bg)" }}>
        <div className="text-center max-w-sm">
          <div
            className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-5"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <BarChart3 className="h-6 w-6" />
          </div>
          <div className="eyebrow mb-2">Authentication required</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Sign in to see your <em className="serif-italic" style={{ color: "var(--accent)" }}>progress</em>.
          </h2>
          <p className="text-[14px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
            Track your topic mastery, streaks, and achievements.
          </p>
          <Link href="/sign-in" className="btn btn-primary">Log in</Link>
        </div>
      </div>
    );
  }

  const xpPercent = user.xpNextLevel > 0
    ? Math.round((user.xpCurrentLevel / user.xpNextLevel) * 100)
    : 0;

  const earnedCount = achievements.filter((a) => a.earned).length;

  const overviewStats = [
    { value: `Lv.${user.globalLevel}`, label: "Current level" },
    { value: user.globalXp.toLocaleString(), label: "Total XP" },
    ...(streak
      ? [
          { value: String(streak.currentStreak), label: "Day streak" },
          { value: String(streak.totalActiveDays), label: "Days active" },
        ]
      : []),
  ];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        <div className="eyebrow mb-3">Account · Progress</div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 6vw, 64px)", letterSpacing: "-0.04em", lineHeight: 0.98, color: "var(--fg)" }}>
          Your <em className="serif-italic" style={{ color: "var(--accent)" }}>progress</em>.
        </h1>

        {/* Overview */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-8">
          {overviewStats.map((s, i) => (
            <div key={s.label} className="card-edit p-5">
              <div className="mono text-[10px] mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {String(i + 1).padStart(2, "0")}
              </div>
              <p className="serif tabular" style={{ fontSize: 30, color: "var(--accent)", letterSpacing: "-0.02em" }}>
                {s.value}
              </p>
              <p className="mono text-[10px] mt-1 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {s.label}
              </p>
            </div>
          ))}
        </div>

        {/* XP bar */}
        <div className="card-edit p-5 mt-6">
          <div className="flex items-center justify-between mb-2">
            <span className="mono text-[11px] uppercase" style={{ color: "var(--fg-2)", letterSpacing: "0.06em" }}>
              Level {user.globalLevel}
            </span>
            <span className="mono tabular text-[11px]" style={{ color: "var(--fg-3)" }}>
              {xpPercent}% → Lv. {user.globalLevel + 1}
            </span>
          </div>
          <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
            <div className="h-full rounded-full transition-all" style={{ width: `${xpPercent}%`, background: "var(--accent)" }} />
          </div>
        </div>

        {/* Topic mastery */}
        {!subStatus?.isSubscribed ? (
          <div className="card-edit p-10 text-center mt-8">
            <div
              className="w-12 h-12 rounded-md flex items-center justify-center mx-auto mb-3"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
            >
              <Lock className="h-5 w-5" />
            </div>
            <div className="eyebrow mb-2">Subscriber · Locked</div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
              Сэдвийн дэлгэрэнгүй <em className="serif-italic" style={{ color: "var(--accent)" }}>шинжилгээ</em>
            </h3>
            <p className="text-[13px] mt-3 mb-5" style={{ color: "var(--fg-2)" }}>
              Topic-level breakdown unlocks with subscription.
            </p>
            <Link href="/upgrade" className="btn btn-primary">
              Элсэх — 19,900 ₮/сар
            </Link>
          </div>
        ) : progress.length > 0 ? (
          <div className="mt-8">
            <div className="flex items-center justify-between mb-4">
              <div className="eyebrow">Topic mastery</div>
              <Link href="/practice" className="mono text-[11px] uppercase flex items-center gap-1" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>
                Practice <ArrowRight className="h-3 w-3" />
              </Link>
            </div>
            <div className="card-edit p-0 overflow-hidden">
              {progress.map((p, i) => {
                const acc = Math.round(p.recentAccuracy * 100);
                const accColor = p.recentAccuracy >= 0.8 ? "var(--accent)" : p.recentAccuracy >= 0.5 ? "var(--warn)" : "var(--danger)";
                return (
                  <div
                    key={p.topicId}
                    className="flex items-center gap-4 px-5 py-4"
                    style={{ borderBottom: i < progress.length - 1 ? "1px solid var(--line)" : "none" }}
                  >
                    <div className="flex-1 min-w-0">
                      <p className="serif" style={{ fontWeight: 400, fontSize: 16, color: "var(--fg)" }}>{p.topic.name}</p>
                      <p className="mono text-[10px] mt-0.5 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                        {p.totalAttempts} attempts
                      </p>
                    </div>
                    <div className="w-28">
                      <div className="flex items-center justify-between mb-1">
                        <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>Accuracy</span>
                        <span className="mono tabular text-[11px]" style={{ color: "var(--fg-2)" }}>{acc}%</span>
                      </div>
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <div className="h-full rounded-full" style={{ width: `${acc}%`, background: accColor }} />
                      </div>
                    </div>
                    <div className="text-right w-16">
                      <p className="serif tabular" style={{ fontSize: 16, color: "var(--accent)" }}>Lv.{p.topicLevel}</p>
                      <p className="mono tabular text-[10px]" style={{ color: "var(--fg-3)" }}>{p.topicXp} XP</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        ) : null}

        {/* Achievements */}
        {achievements.length > 0 && (
          <div id="achievements" className="mt-10">
            <div className="flex items-center justify-between mb-4">
              <div className="eyebrow">Achievements</div>
              <span className="mono tabular text-[11px]" style={{ color: "var(--fg-3)" }}>
                {earnedCount} / {achievements.length}
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              {achievements.map((a) => (
                <div
                  key={a.id}
                  className="card-edit p-4 flex items-center gap-3"
                  style={a.earned ? { background: "var(--accent-wash)", borderColor: "var(--accent-line)" } : { opacity: 0.55 }}
                >
                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center flex-shrink-0 mono"
                    style={{
                      background: a.earned ? "var(--bg-1)" : "var(--bg-2)",
                      border: `1px solid ${a.earned ? "var(--accent-line)" : "var(--line)"}`,
                      color: a.earned ? "var(--accent)" : "var(--fg-3)",
                      fontSize: 13,
                    }}
                  >
                    {iconMap[a.iconKey] ?? iconMap.default}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="serif truncate" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>{a.name}</p>
                    <p className="text-[12px] truncate" style={{ color: "var(--fg-3)" }}>{a.description}</p>
                  </div>
                  <div className="text-right flex-shrink-0">
                    <p className="mono tabular text-[11px]" style={{ color: a.earned ? "var(--accent)" : "var(--fg-3)" }}>+{a.xpReward}</p>
                    {a.earned && a.earnedAt && (
                      <p className="mono text-[10px]" style={{ color: "var(--fg-3)" }}>
                        {new Date(a.earnedAt).toLocaleDateString()}
                      </p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Empty */}
        {progress.length === 0 && subStatus?.isSubscribed && (
          <div className="text-center py-16">
            <Target className="h-10 w-10 mx-auto mb-4" style={{ color: "var(--fg-3)" }} />
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
              No practice sessions <em className="serif-italic" style={{ color: "var(--accent)" }}>yet</em>.
            </h3>
            <p className="text-[14px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              Complete a practice session to see your topic progress here.
            </p>
            <Link href="/practice" className="btn btn-primary">
              Start practicing
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
