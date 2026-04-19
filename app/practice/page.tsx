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
      <div className="min-h-screen flex items-center justify-center pt-20" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <div
            className="w-8 h-8 border-2 rounded-full animate-spin mx-auto mb-4"
            style={{ borderColor: "var(--accent)", borderTopColor: "transparent" }}
          />
          <p className="mono text-[12px]" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>LOADING...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-20 px-4 relative overflow-hidden" style={{ background: "var(--bg)" }}>
        <div
          className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[720px] h-[460px] pointer-events-none"
          style={{
            background: "radial-gradient(closest-side, color-mix(in oklch, var(--accent) 12%, transparent), transparent 70%)",
            filter: "blur(40px)",
          }}
        />
        <div className="text-center max-w-sm relative">
          <div
            className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-5"
            style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
          >
            <Lock className="h-6 w-6" />
          </div>
          <div className="eyebrow mb-2">Authentication required</div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Sign in to <em className="serif-italic" style={{ color: "var(--accent)" }}>practice</em>.
          </h2>
          <p className="text-[14px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
            Create a free account to access adaptive math practice, track your progress, and earn achievements.
          </p>
          <div className="flex flex-col gap-2">
            <Link href="/sign-up" className="btn btn-primary w-full">
              Create free account
            </Link>
            <Link href="/sign-in" className="btn btn-line w-full">
              Log in
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const xpPct = Math.round((user.xpCurrentLevel / user.xpNextLevel) * 100);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        {/* Header */}
        <div className="eyebrow mb-3">Practice · Home</div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 6vw, 64px)", letterSpacing: "-0.04em", lineHeight: 0.98, color: "var(--fg)" }}>
          Welcome back,{" "}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {user.displayName.split(" ")[0]}
          </em>
          .
        </h1>
        <p className="serif mt-4 max-w-2xl" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
          Ready to practice today?
        </p>

        {/* Stats strip */}
        <div className="card-edit p-5 mt-8">
          <div className="flex flex-wrap items-center justify-between gap-4 mb-4">
            <div className="flex items-center gap-6">
              {streak && (
                <div className="flex items-baseline gap-2">
                  <Flame className="h-4 w-4" style={{ color: "var(--warn)" }} />
                  <span className="serif tabular" style={{ fontSize: 26, color: "var(--fg)", letterSpacing: "-0.02em" }}>
                    {streak.currentStreak}
                  </span>
                  <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    day streak
                  </span>
                </div>
              )}
              <div className="flex items-baseline gap-2">
                <Star className="h-4 w-4" style={{ color: "var(--accent)" }} />
                <span className="serif tabular" style={{ fontSize: 26, color: "var(--fg)", letterSpacing: "-0.02em" }}>
                  {user.globalXp.toLocaleString()}
                </span>
                <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  XP
                </span>
              </div>
              <div className="flex items-baseline gap-2">
                <Trophy className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                <span className="serif tabular" style={{ fontSize: 26, color: "var(--fg)", letterSpacing: "-0.02em" }}>
                  {user.globalLevel}
                </span>
                <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  level
                </span>
              </div>
            </div>
          </div>
          <div className="flex items-center justify-between mb-1.5">
            <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
              Level {user.globalLevel}
            </span>
            <span className="mono tabular text-[10px]" style={{ color: "var(--fg-3)" }}>
              {xpPct}%
            </span>
            <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
              Level {user.globalLevel + 1}
            </span>
          </div>
          <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
            <div className="h-full rounded-full transition-all" style={{ width: `${xpPct}%`, background: "var(--accent)" }} />
          </div>
        </div>

        {/* ESH banner */}
        <Link
          href="/practice/esh"
          className="block mt-6 card-edit p-6 group"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-4">
              <div
                className="w-12 h-12 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-1)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
              >
                <Calculator className="h-5 w-5" />
              </div>
              <div>
                <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Featured · ЭЕШ</div>
                <h2 className="serif" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  ЭЕШ Математик
                </h2>
                <p className="mono text-[11px] mt-1" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                  216 БОДЛОГО · 6 ТЕСТ · СЭДВЭЭР АНГИЛСАН
                </p>
              </div>
            </div>
            <ArrowRight className="h-5 w-5 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
          </div>
        </Link>

        {/* Quick actions */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mt-6">
          {[
            { href: "/progress", icon: BarChart3, title: "View progress", desc: "Track your growth" },
            { href: "/progress#achievements", icon: Trophy, title: "Achievements", desc: "Earn badges" },
            { href: "/practice/esh/previous-years", icon: Flame, title: "Previous year tests", desc: "2024–2025 ЭЕШ, free" },
          ].map(({ href, icon: Icon, title, desc }) => (
            <Link key={href} href={href} className="card-edit p-4 flex items-center gap-3 group">
              <div
                className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
              >
                <Icon className="h-4 w-4" />
              </div>
              <div>
                <p className="serif" style={{ fontWeight: 400, fontSize: 15, color: "var(--fg)" }}>{title}</p>
                <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>{desc}</p>
              </div>
            </Link>
          ))}
        </div>

        {/* Topics */}
        <div className="mt-10">
          <div className="eyebrow mb-3">Topics · Choose</div>
          <h2 className="serif mb-5" style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Pick a <em className="serif-italic" style={{ color: "var(--accent)" }}>topic</em>.
          </h2>
          {topics.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {topics.map((topic, i) => (
                <button
                  key={topic.id}
                  onClick={() => router.push(`/practice/session?topicId=${topic.id}`)}
                  className="card-edit p-5 text-left group w-full"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <div className="mono text-[10px] mb-1.5" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                        {String(i + 1).padStart(2, "0")}
                      </div>
                      <h3 className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                        {topic.name}
                      </h3>
                      {topic.children && topic.children.length > 0 && (
                        <p className="text-[12px] mt-1" style={{ color: "var(--fg-3)" }}>{topic.children.length} subtopics</p>
                      )}
                    </div>
                    <ArrowRight className="h-4 w-4 flex-shrink-0 mt-1" style={{ color: "var(--fg-3)" }} />
                  </div>
                </button>
              ))}
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {defaultTopics.map((topic, i) => {
                const Icon = topic.icon;
                return (
                  <div key={topic.id} className="card-edit p-5">
                    <div className="flex items-start gap-3">
                      <div
                        className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
                      >
                        <Icon className="h-4 w-4" />
                      </div>
                      <div className="min-w-0">
                        <div className="mono text-[10px] mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                          {String(i + 1).padStart(2, "0")}
                        </div>
                        <h3 className="serif" style={{ fontWeight: 400, fontSize: 17, color: "var(--fg)" }}>
                          {topic.name}
                        </h3>
                        <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>{topic.description}</p>
                        <span className="badge-edit mt-2 inline-block" style={{ background: "var(--bg-2)" }}>
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
