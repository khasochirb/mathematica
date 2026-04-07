"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, Flame, Star, Trophy, BarChart3, Lock, BookOpen, Calculator, Sigma, Pi, Percent, Binary } from "lucide-react";
import { api, type TopicTree, type StreakData } from "@/lib/api";
import { useAuth } from "@/lib/auth-context";

const defaultTopics = [
  { id: "algebra", name: "Algebra", icon: Sigma, description: "Equations, expressions & functions" },
  { id: "geometry", name: "Geometry", icon: Pi, description: "Shapes, angles & proofs" },
  { id: "arithmetic", name: "Arithmetic", icon: Calculator, description: "Numbers & operations" },
  { id: "statistics", name: "Statistics & Probability", icon: Percent, description: "Data analysis & chance" },
  { id: "number-theory", name: "Number Theory", icon: Binary, description: "Primes, divisibility & patterns" },
  { id: "word-problems", name: "Word Problems", icon: BookOpen, description: "Real-world applications" },
];

export default function PracticePage() {
  const router = useRouter();
  const { user, loading: authLoading } = useAuth();
  const [topics, setTopics] = useState<TopicTree[]>([]);
  const [streak, setStreak] = useState<StreakData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      if (!user) { setLoading(false); return; }
      try {
        const [topicsData, streakData] = await Promise.all([
          api.topics.list(),
          api.streaks.get(),
        ]);
        setTopics(topicsData);
        setStreak(streakData);
      } catch {
        // stub endpoints return defaults
      } finally {
        setLoading(false);
      }
    }
    if (!authLoading) load();
  }, [user, authLoading]);

  if (authLoading || loading) {
    return (
      <div className="min-h-screen bg-surface-900 flex items-center justify-center pt-16">
        <div className="text-center">
          <div className="w-8 h-8 border-2 border-primary-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-gray-500 text-sm">Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen bg-surface-900 flex items-center justify-center pt-16 px-4 relative overflow-hidden">
        <div className="absolute inset-0 bg-grid opacity-50" />
        <div className="absolute inset-0 glow-center" />
        <div className="text-center max-w-sm relative">
          <div className="w-16 h-16 bg-primary-500/10 border border-primary-400/20 rounded-2xl flex items-center justify-center mx-auto mb-4">
            <Lock className="h-8 w-8 text-primary-400" />
          </div>
          <h2 className="font-display text-xl font-bold text-white mb-2">Sign in to practice</h2>
          <p className="text-gray-400 text-sm mb-6">
            Create a free account to access adaptive math practice, track your progress, and earn achievements.
          </p>
          <div className="flex flex-col gap-3">
            <Link href="/sign-up" className="btn-primary w-full text-center py-3">
              Create Free Account
            </Link>
            <Link href="/sign-in" className="btn-secondary w-full text-center py-3">
              Log In
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* User stats */}
        <div className="card-glass border-glow p-6 mb-8">
          <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
              <h1 className="font-display text-xl font-bold text-white">
                Welcome back, {user.displayName.split(" ")[0]}!
              </h1>
              <p className="text-gray-400 text-sm mt-0.5">Ready to practice today?</p>
            </div>
            <div className="flex items-center gap-3">
              {streak && (
                <div className="flex items-center gap-1.5 bg-orange-500/10 border border-orange-400/15 px-3 py-1.5 rounded-xl">
                  <Flame className="h-4 w-4 text-orange-400" />
                  <span className="font-bold text-orange-300 text-sm">{streak.currentStreak}</span>
                  <span className="text-orange-400/70 text-xs">day streak</span>
                </div>
              )}
              <div className="flex items-center gap-1.5 bg-accent-gold/10 border border-accent-gold/15 px-3 py-1.5 rounded-xl">
                <Star className="h-4 w-4 text-accent-gold" />
                <span className="font-bold text-yellow-300 text-sm">{user.globalXp.toLocaleString()} XP</span>
              </div>
            </div>
          </div>
          {/* Level progress */}
          <div className="mt-4">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-xs text-gray-500">Level {user.globalLevel}</span>
              <span className="text-xs text-gray-500">Level {user.globalLevel + 1}</span>
            </div>
            <div className="h-2 bg-white/[0.06] rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-primary-500 to-accent-cyan rounded-full transition-all"
                style={{ width: `${Math.round((user.xpCurrentLevel / user.xpNextLevel) * 100)}%` }}
              />
            </div>
          </div>
        </div>

        {/* ESH Practice Banner */}
        <Link href="/practice/esh" className="block mb-8 card-glass border-glow p-6 group hover:border-primary-400/30 transition-all">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="p-3 bg-gradient-to-br from-primary-500/20 to-accent-cyan/20 border border-primary-400/15 rounded-2xl">
                <Calculator className="h-7 w-7 text-primary-400" />
              </div>
              <div>
                <h2 className="font-display text-lg font-bold text-white group-hover:text-primary-300 transition-colors">
                  ЭЕШ Математик
                </h2>
                <p className="text-gray-400 text-sm mt-0.5">
                  216 бодлого · 6 тест · Сэдвээр ангилсан · Үзүүлэлт хянах
                </p>
              </div>
            </div>
            <ArrowRight className="h-5 w-5 text-gray-600 group-hover:text-primary-400 transition-colors" />
          </div>
        </Link>

        {/* Quick actions */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
          <Link href="/progress" className="card-glass-glow group">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-primary-500/10 border border-primary-400/10 rounded-xl group-hover:bg-primary-500/20 transition-colors">
                <BarChart3 className="h-5 w-5 text-primary-400" />
              </div>
              <div>
                <p className="font-semibold text-gray-200 text-sm group-hover:text-primary-300 transition-colors">View Progress</p>
                <p className="text-gray-500 text-xs">Track your growth</p>
              </div>
            </div>
          </Link>
          <Link href="/progress#achievements" className="card-glass-glow group">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-accent-gold/10 border border-accent-gold/10 rounded-xl group-hover:bg-accent-gold/20 transition-colors">
                <Trophy className="h-5 w-5 text-accent-gold" />
              </div>
              <div>
                <p className="font-semibold text-gray-200 text-sm group-hover:text-yellow-300 transition-colors">Achievements</p>
                <p className="text-gray-500 text-xs">Earn badges</p>
              </div>
            </div>
          </Link>
          <Link href="/tutoring" className="card-glass-glow group">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-accent-emerald/10 border border-accent-emerald/10 rounded-xl group-hover:bg-accent-emerald/20 transition-colors">
                <Flame className="h-5 w-5 text-accent-emerald" />
              </div>
              <div>
                <p className="font-semibold text-gray-200 text-sm group-hover:text-accent-emerald transition-colors">Book a Tutor</p>
                <p className="text-gray-500 text-xs">1-on-1 sessions</p>
              </div>
            </div>
          </Link>
        </div>

        {/* Topics */}
        <div>
          <h2 className="font-display text-lg font-bold text-white mb-4">Choose a topic</h2>
          {topics.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {topics.map((topic) => (
                <button
                  key={topic.id}
                  onClick={() => router.push(`/practice/session?topicId=${topic.id}`)}
                  className="card-glass-glow text-left group w-full"
                >
                  <div className="flex items-start justify-between">
                    <div>
                      <h3 className="font-semibold text-gray-200 group-hover:text-primary-300 transition-colors text-sm mb-1">
                        {topic.name}
                      </h3>
                      {topic.children && topic.children.length > 0 && (
                        <p className="text-gray-500 text-xs">{topic.children.length} subtopics</p>
                      )}
                    </div>
                    <ArrowRight className="h-4 w-4 text-gray-600 group-hover:text-primary-400 flex-shrink-0 mt-0.5 transition-colors" />
                  </div>
                </button>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {defaultTopics.map((topic) => {
                const Icon = topic.icon;
                return (
                  <div
                    key={topic.id}
                    className="card-glass group"
                  >
                    <div className="flex items-start gap-3">
                      <div className="p-2 bg-primary-500/10 border border-primary-400/10 rounded-xl flex-shrink-0">
                        <Icon className="h-5 w-5 text-primary-400" />
                      </div>
                      <div>
                        <h3 className="font-semibold text-gray-200 text-sm mb-0.5">
                          {topic.name}
                        </h3>
                        <p className="text-gray-500 text-xs">{topic.description}</p>
                        <span className="inline-block mt-2 text-xs text-primary-400/70 bg-primary-500/5 border border-primary-400/10 px-2 py-0.5 rounded-full">
                          Coming soon
                        </span>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
