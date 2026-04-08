"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Flame, Star, Trophy, BarChart3, ArrowRight, Target, Lock } from "lucide-react";
import { api, type TopicProgress, type StreakData, type AchievementWithStatus } from "@/lib/api";
import { useAuth } from "@/lib/auth-context";
import { cn } from "@/lib/utils";

const iconMap: Record<string, string> = {
  first_problem: "🎯",
  streak_3: "🔥",
  streak_7: "🌟",
  streak_30: "💫",
  perfect_session: "✨",
  speed_demon: "⚡",
  century: "💯",
  default: "🏆",
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

        // Topic progress is subscriber-only — fetch if subscribed
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
      <div className="min-h-screen bg-surface-900 flex items-center justify-center pt-16">
        <div className="w-8 h-8 border-2 border-primary-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen bg-surface-900 flex items-center justify-center pt-16 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-grid opacity-50" />
        <div className="text-center max-w-sm relative">
          <BarChart3 className="h-12 w-12 text-gray-600 mx-auto mb-4" />
          <h2 className="font-display text-xl font-bold text-white mb-2">Sign in to see your progress</h2>
          <p className="text-gray-400 text-sm mb-6">
            Track your topic mastery, streaks, and achievements.
          </p>
          <Link href="/sign-in" className="btn-primary">Log In</Link>
        </div>
      </div>
    );
  }

  const xpPercent = user.xpNextLevel > 0
    ? Math.round((user.xpCurrentLevel / user.xpNextLevel) * 100)
    : 0;

  const earnedCount = achievements.filter((a) => a.earned).length;

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        <h1 className="font-display text-2xl font-bold text-white mb-8">Your Progress</h1>

        {/* Overview cards */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
          <div className="card-glass text-center">
            <p className="font-display text-2xl font-bold gradient-text">Lv. {user.globalLevel}</p>
            <p className="text-gray-500 text-xs mt-1">Current Level</p>
          </div>
          <div className="card-glass text-center">
            <p className="font-display text-2xl font-bold text-accent-gold">{user.globalXp.toLocaleString()}</p>
            <p className="text-gray-500 text-xs mt-1">Total XP</p>
          </div>
          {streak && (
            <>
              <div className="card-glass text-center">
                <p className="font-display text-2xl font-bold text-orange-400">{streak.currentStreak}</p>
                <p className="text-gray-500 text-xs mt-1">Day Streak</p>
              </div>
              <div className="card-glass text-center">
                <p className="font-display text-2xl font-bold text-gray-300">{streak.totalActiveDays}</p>
                <p className="text-gray-500 text-xs mt-1">Days Active</p>
              </div>
            </>
          )}
        </div>

        {/* XP progress bar */}
        <div className="card-glass mb-8">
          <div className="flex items-center justify-between mb-2">
            <span className="font-semibold text-gray-200 text-sm">Level {user.globalLevel}</span>
            <span className="text-gray-500 text-xs">{xpPercent}% to Level {user.globalLevel + 1}</span>
          </div>
          <div className="h-3 bg-white/[0.06] rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-primary-500 to-accent-cyan rounded-full transition-all"
              style={{ width: `${xpPercent}%` }}
            />
          </div>
        </div>

        {/* Topic progress — subscriber only */}
        {!subStatus?.isSubscribed ? (
          <div className="card-glass text-center py-10 mb-8">
            <Lock className="h-8 w-8 text-gray-600 mx-auto mb-3" />
            <p className="text-gray-400 text-sm mb-4">
              Сэдвийн дэлгэрэнгүй шинжилгээ харахын тулд элс
            </p>
            <Link href="/upgrade" className="btn-primary">
              Элсэх — 19,900 ₮/сар
            </Link>
          </div>
        ) : progress.length > 0 ? (
          <div className="card-glass p-0 mb-8 overflow-hidden">
            <div className="flex items-center justify-between p-5 border-b border-white/[0.06]">
              <h2 className="font-display font-bold text-white">Topic Mastery</h2>
              <Link href="/practice" className="text-sm text-primary-400 hover:text-primary-300 flex items-center gap-1 transition-colors">
                Practice <ArrowRight className="h-3.5 w-3.5" />
              </Link>
            </div>
            <div className="divide-y divide-white/[0.04]">
              {progress.map((p) => (
                <div key={p.topicId} className="flex items-center gap-4 px-5 py-3.5">
                  <div className="flex-1">
                    <p className="font-medium text-gray-200 text-sm">{p.topic.name}</p>
                    <p className="text-gray-500 text-xs mt-0.5">{p.totalAttempts} attempts</p>
                  </div>
                  <div className="w-24">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs text-gray-500">Accuracy</span>
                      <span className="text-xs font-semibold text-gray-300">
                        {Math.round(p.recentAccuracy * 100)}%
                      </span>
                    </div>
                    <div className="h-1.5 bg-white/[0.06] rounded-full overflow-hidden">
                      <div
                        className={cn(
                          "h-full rounded-full",
                          p.recentAccuracy >= 0.8
                            ? "bg-accent-emerald"
                            : p.recentAccuracy >= 0.5
                            ? "bg-accent-gold"
                            : "bg-red-400"
                        )}
                        style={{ width: `${Math.round(p.recentAccuracy * 100)}%` }}
                      />
                    </div>
                  </div>
                  <div className="text-right w-16">
                    <p className="text-xs font-semibold text-accent-gold">Lv.{p.topicLevel}</p>
                    <p className="text-xs text-gray-500">{p.topicXp} XP</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ) : null}

        {/* Achievements */}
        {achievements.length > 0 && (
          <div id="achievements" className="card-glass p-0 overflow-hidden">
            <div className="flex items-center justify-between p-5 border-b border-white/[0.06]">
              <h2 className="font-display font-bold text-white">Achievements</h2>
              <span className="text-sm text-gray-500">{earnedCount} / {achievements.length}</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 p-5">
              {achievements.map((a) => (
                <div
                  key={a.id}
                  className={cn(
                    "flex items-center gap-3 p-3 rounded-xl border transition-colors",
                    a.earned
                      ? "border-accent-gold/20 bg-accent-gold/5"
                      : "border-white/[0.06] bg-white/[0.02] opacity-50"
                  )}
                >
                  <div className="text-2xl w-10 text-center flex-shrink-0">
                    {iconMap[a.iconKey] ?? iconMap.default}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-semibold text-gray-200 text-sm truncate">{a.name}</p>
                    <p className="text-gray-500 text-xs truncate">{a.description}</p>
                  </div>
                  <div className="text-right flex-shrink-0">
                    <p className="text-xs font-bold text-accent-gold">+{a.xpReward} XP</p>
                    {a.earned && a.earnedAt && (
                      <p className="text-xs text-gray-500">
                        {new Date(a.earnedAt).toLocaleDateString()}
                      </p>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Empty state */}
        {progress.length === 0 && (
          <div className="text-center py-16">
            <Target className="h-12 w-12 text-gray-700 mx-auto mb-4" />
            <h3 className="font-display font-semibold text-gray-300 mb-2">No practice sessions yet</h3>
            <p className="text-gray-500 text-sm mb-6">
              Complete a practice session to see your topic progress here.
            </p>
            <Link href="/practice" className="btn-primary">
              Start Practicing
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
