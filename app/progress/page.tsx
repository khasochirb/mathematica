"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Flame, Star, Trophy, BarChart3, ArrowRight, Target } from "lucide-react";
import { api, type TopicProgress, type StreakData, type AchievementWithStatus } from "@/lib/api";
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
  const [progress, setProgress] = useState<TopicProgress[]>([]);
  const [streak, setStreak] = useState<StreakData | null>(null);
  const [achievements, setAchievements] = useState<AchievementWithStatus[]>([]);
  const [user, setUser] = useState<{ displayName: string; globalLevel: number; globalXp: number; xpCurrentLevel: number; xpNextLevel: number } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const [prog, streakData, achData, userData] = await Promise.all([
          api.progress.all(),
          api.streaks.get(),
          api.achievements.all(),
          api.auth.me(),
        ]);
        setProgress(prog);
        setStreak(streakData);
        setAchievements(achData);
        setUser(userData);
      } catch {
        // not logged in
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16">
        <div className="w-8 h-8 border-2 border-primary-600 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16 px-4">
        <div className="text-center max-w-sm">
          <BarChart3 className="h-12 w-12 text-gray-300 mx-auto mb-4" />
          <h2 className="text-xl font-bold text-gray-900 mb-2">Sign in to see your progress</h2>
          <p className="text-gray-500 text-sm mb-6">
            Track your topic mastery, streaks, and achievements.
          </p>
          <Link href="/sign-in" className="btn-primary">Log In</Link>
        </div>
      </div>
    );
  }

  const xpPercent = Math.round(
    ((user.globalXp - user.xpCurrentLevel) / (user.xpNextLevel - user.xpCurrentLevel)) * 100
  );

  const earnedCount = achievements.filter((a) => a.earned).length;

  return (
    <div className="min-h-screen bg-gray-50 pt-20">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-8">Your Progress</h1>

        {/* Overview cards */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
          <div className="bg-white rounded-2xl border border-gray-100 p-4 text-center shadow-sm">
            <p className="text-2xl font-bold text-primary-600">Lv. {user.globalLevel}</p>
            <p className="text-gray-400 text-xs mt-1">Current Level</p>
          </div>
          <div className="bg-white rounded-2xl border border-gray-100 p-4 text-center shadow-sm">
            <p className="text-2xl font-bold text-yellow-500">{user.globalXp.toLocaleString()}</p>
            <p className="text-gray-400 text-xs mt-1">Total XP</p>
          </div>
          {streak && (
            <>
              <div className="bg-white rounded-2xl border border-gray-100 p-4 text-center shadow-sm">
                <p className="text-2xl font-bold text-orange-500">{streak.currentStreak}</p>
                <p className="text-gray-400 text-xs mt-1">Day Streak</p>
              </div>
              <div className="bg-white rounded-2xl border border-gray-100 p-4 text-center shadow-sm">
                <p className="text-2xl font-bold text-gray-700">{streak.totalActiveDays}</p>
                <p className="text-gray-400 text-xs mt-1">Days Active</p>
              </div>
            </>
          )}
        </div>

        {/* XP progress bar */}
        <div className="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm mb-8">
          <div className="flex items-center justify-between mb-2">
            <span className="font-semibold text-gray-900 text-sm">Level {user.globalLevel}</span>
            <span className="text-gray-400 text-xs">{xpPercent}% to Level {user.globalLevel + 1}</span>
          </div>
          <div className="h-3 bg-gray-100 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-primary-500 to-blue-400 rounded-full transition-all"
              style={{ width: `${xpPercent}%` }}
            />
          </div>
        </div>

        {/* Topic progress */}
        {progress.length > 0 && (
          <div className="bg-white rounded-2xl border border-gray-100 shadow-sm mb-8">
            <div className="flex items-center justify-between p-5 border-b border-gray-50">
              <h2 className="font-bold text-gray-900">Topic Mastery</h2>
              <Link href="/practice" className="text-sm text-primary-600 hover:underline flex items-center gap-1">
                Practice <ArrowRight className="h-3.5 w-3.5" />
              </Link>
            </div>
            <div className="divide-y divide-gray-50">
              {progress.map((p) => (
                <div key={p.topicId} className="flex items-center gap-4 px-5 py-3.5">
                  <div className="flex-1">
                    <p className="font-medium text-gray-900 text-sm">{p.topic.name}</p>
                    <p className="text-gray-400 text-xs mt-0.5">{p.totalAttempts} attempts</p>
                  </div>
                  <div className="w-24">
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs text-gray-400">Accuracy</span>
                      <span className="text-xs font-semibold text-gray-700">
                        {Math.round(p.recentAccuracy * 100)}%
                      </span>
                    </div>
                    <div className="h-1.5 bg-gray-100 rounded-full overflow-hidden">
                      <div
                        className={cn(
                          "h-full rounded-full",
                          p.recentAccuracy >= 0.8
                            ? "bg-accent-green"
                            : p.recentAccuracy >= 0.5
                            ? "bg-yellow-400"
                            : "bg-red-400"
                        )}
                        style={{ width: `${Math.round(p.recentAccuracy * 100)}%` }}
                      />
                    </div>
                  </div>
                  <div className="text-right w-16">
                    <p className="text-xs font-semibold text-yellow-600">Lv.{p.topicLevel}</p>
                    <p className="text-xs text-gray-400">{p.topicXp} XP</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Achievements */}
        {achievements.length > 0 && (
          <div id="achievements" className="bg-white rounded-2xl border border-gray-100 shadow-sm">
            <div className="flex items-center justify-between p-5 border-b border-gray-50">
              <h2 className="font-bold text-gray-900">Achievements</h2>
              <span className="text-sm text-gray-400">{earnedCount} / {achievements.length}</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 p-5">
              {achievements.map((a) => (
                <div
                  key={a.id}
                  className={cn(
                    "flex items-center gap-3 p-3 rounded-xl border transition-colors",
                    a.earned
                      ? "border-yellow-200 bg-yellow-50"
                      : "border-gray-100 bg-gray-50 opacity-50"
                  )}
                >
                  <div className="text-2xl w-10 text-center flex-shrink-0">
                    {iconMap[a.iconKey] ?? iconMap.default}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-semibold text-gray-900 text-sm truncate">{a.name}</p>
                    <p className="text-gray-500 text-xs truncate">{a.description}</p>
                  </div>
                  <div className="text-right flex-shrink-0">
                    <p className="text-xs font-bold text-yellow-600">+{a.xpReward} XP</p>
                    {a.earned && a.earnedAt && (
                      <p className="text-xs text-gray-400">
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
            <Target className="h-12 w-12 text-gray-200 mx-auto mb-4" />
            <h3 className="font-semibold text-gray-700 mb-2">No practice sessions yet</h3>
            <p className="text-gray-400 text-sm mb-6">
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
