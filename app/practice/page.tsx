"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { ArrowRight, Flame, Star, Trophy, BarChart3, Lock } from "lucide-react";
import { api, type TopicTree, type StreakData } from "@/lib/api";

function TopicCard({
  topic,
  onStart,
}: {
  topic: TopicTree;
  onStart: (id: string, name: string) => void;
}) {
  return (
    <button
      onClick={() => onStart(topic.id, topic.name)}
      className="card text-left hover:border-primary-300 hover:shadow-md transition-all group w-full"
    >
      <div className="flex items-start justify-between">
        <div>
          <h3 className="font-semibold text-gray-900 group-hover:text-primary-600 transition-colors text-sm mb-1">
            {topic.name}
          </h3>
          {topic.children && topic.children.length > 0 && (
            <p className="text-gray-400 text-xs">{topic.children.length} subtopics</p>
          )}
        </div>
        <ArrowRight className="h-4 w-4 text-gray-300 group-hover:text-primary-500 flex-shrink-0 mt-0.5 transition-colors" />
      </div>
    </button>
  );
}

export default function PracticePage() {
  const router = useRouter();
  const [topics, setTopics] = useState<TopicTree[]>([]);
  const [streak, setStreak] = useState<StreakData | null>(null);
  const [user, setUser] = useState<{ displayName: string; globalLevel: number; globalXp: number; xpCurrentLevel: number; xpNextLevel: number } | null>(null);
  const [loading, setLoading] = useState(true);
  const [authed, setAuthed] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const [topicsData, userData, streakData] = await Promise.all([
          api.topics.list(),
          api.auth.me(),
          api.streaks.get(),
        ]);
        setTopics(topicsData);
        setUser(userData);
        setStreak(streakData);
      } catch {
        setAuthed(false);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  async function startSession(topicId: string) {
    try {
      const { sessionId, firstProblem } = await api.sessions.create({
        mode: "practice",
        topicIds: [topicId],
        problemCount: 10,
      });
      router.push(`/practice/session?sessionId=${sessionId}&topicId=${topicId}`);
    } catch {
      router.push("/sign-in");
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16">
        <div className="text-center">
          <div className="w-8 h-8 border-2 border-primary-600 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-gray-500 text-sm">Loading your dashboard...</p>
        </div>
      </div>
    );
  }

  if (!authed) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16 px-4">
        <div className="text-center max-w-sm">
          <div className="w-16 h-16 bg-primary-50 rounded-full flex items-center justify-center mx-auto mb-4">
            <Lock className="h-8 w-8 text-primary-400" />
          </div>
          <h2 className="text-xl font-bold text-gray-900 mb-2">Sign in to practice</h2>
          <p className="text-gray-500 text-sm mb-6">
            Create a free account to access adaptive math practice, track your progress, and earn
            achievements.
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

  const xpPercent = user
    ? Math.round(((user.globalXp - user.xpCurrentLevel) / (user.xpNextLevel - user.xpCurrentLevel)) * 100)
    : 0;

  return (
    <div className="min-h-screen bg-gray-50 pt-20">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* User stats */}
        {user && (
          <div className="bg-white rounded-2xl border border-gray-100 p-6 mb-8 shadow-sm">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div>
                <h1 className="text-xl font-bold text-gray-900">
                  Welcome back, {user.displayName.split(" ")[0]}! 👋
                </h1>
                <p className="text-gray-500 text-sm mt-0.5">Ready to practice today?</p>
              </div>
              <div className="flex items-center gap-4">
                {streak && (
                  <div className="flex items-center gap-1.5 bg-orange-50 px-3 py-1.5 rounded-lg">
                    <Flame className="h-4 w-4 text-orange-500" />
                    <span className="font-bold text-orange-600 text-sm">{streak.currentStreak}</span>
                    <span className="text-orange-400 text-xs">day streak</span>
                  </div>
                )}
                <div className="flex items-center gap-1.5 bg-yellow-50 px-3 py-1.5 rounded-lg">
                  <Star className="h-4 w-4 text-yellow-500" />
                  <span className="font-bold text-yellow-600 text-sm">{user.globalXp.toLocaleString()} XP</span>
                </div>
              </div>
            </div>
            {/* Level progress */}
            <div className="mt-4">
              <div className="flex items-center justify-between mb-1.5">
                <span className="text-xs text-gray-500">Level {user.globalLevel}</span>
                <span className="text-xs text-gray-400">{xpPercent}% to Level {user.globalLevel + 1}</span>
              </div>
              <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-primary-500 to-primary-600 rounded-full transition-all"
                  style={{ width: `${xpPercent}%` }}
                />
              </div>
            </div>
          </div>
        )}

        {/* Quick actions */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
          <Link href="/progress" className="card hover:border-primary-200 hover:shadow-md transition-all group">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-primary-50 rounded-xl">
                <BarChart3 className="h-5 w-5 text-primary-600" />
              </div>
              <div>
                <p className="font-semibold text-gray-900 text-sm group-hover:text-primary-600 transition-colors">View Progress</p>
                <p className="text-gray-400 text-xs">Track your growth</p>
              </div>
            </div>
          </Link>
          <Link href="/progress#achievements" className="card hover:border-yellow-200 hover:shadow-md transition-all group">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-yellow-50 rounded-xl">
                <Trophy className="h-5 w-5 text-yellow-500" />
              </div>
              <div>
                <p className="font-semibold text-gray-900 text-sm group-hover:text-yellow-600 transition-colors">Achievements</p>
                <p className="text-gray-400 text-xs">Earn badges</p>
              </div>
            </div>
          </Link>
          <button
            onClick={() => topics[0] && startSession(topics[0].id)}
            className="card hover:border-green-200 hover:shadow-md transition-all group text-left"
          >
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-green-50 rounded-xl">
                <Flame className="h-5 w-5 text-accent-green" />
              </div>
              <div>
                <p className="font-semibold text-gray-900 text-sm group-hover:text-accent-green transition-colors">Quick Practice</p>
                <p className="text-gray-400 text-xs">10 adaptive problems</p>
              </div>
            </div>
          </button>
        </div>

        {/* Topics */}
        <div>
          <h2 className="text-lg font-bold text-gray-900 mb-4">Choose a topic</h2>
          {topics.length === 0 ? (
            <div className="text-center py-12 text-gray-400">
              <p>No topics available yet. Check back soon!</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {topics.map((topic) => (
                <TopicCard key={topic.id} topic={topic} onStart={startSession} />
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
