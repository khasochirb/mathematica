import type { Metadata } from "next";
import Link from "next/link";
import {
  BookOpen,
  Trophy,
  Globe,
  Star,
  ArrowRight,
  CheckCircle,
  Brain,
  Flame,
  BarChart3,
} from "lucide-react";

export const metadata: Metadata = {
  title: "Mongol Potential | World Class Math Education",
  description:
    "High-quality math education for Mongolian students worldwide—aligned with AP, IB, and US curricula.",
};

const features = [
  {
    icon: BookOpen,
    title: "Curriculum-Aligned",
    description:
      "Personalized lessons mapped to AP, IB, and US state standards so students improve where it matters—classroom performance and exams.",
    color: "text-primary-600",
    bg: "bg-primary-50",
  },
  {
    icon: Globe,
    title: "Personal & Flexible",
    description:
      "One-on-one instruction, flexible scheduling across time zones, and goals tailored to each learner's needs.",
    color: "text-accent-green",
    bg: "bg-green-50",
  },
  {
    icon: Star,
    title: "Culture-Integrated",
    description:
      "We weave Mongolian history and everyday life into problems so learning is meaningful and identity-affirming.",
    color: "text-accent-amber",
    bg: "bg-amber-50",
  },
];

const examTypes = [
  "SAT Math",
  "ACT Math",
  "AP Calculus",
  "IB Math",
  "Math Olympiad",
  "GRE Quant",
  "GMAT Quant",
  "PSAT / NMSQT",
];

const grades = [
  { label: "Elementary", range: "Grades 2–5", href: "/courses#elementary" },
  { label: "Middle School", range: "Grades 6–8", href: "/courses#middle" },
  { label: "High School", range: "Grades 9–12", href: "/courses#high" },
  { label: "College", range: "Undergraduate", href: "/courses#college" },
  { label: "Adult Learning", range: "All ages", href: "/courses#adult" },
];

const testimonials = [
  {
    quote:
      "My daughter was struggling with math and wasn't confident going to class. Now she finishes her homework without problems.",
    author: "Misheel's Mom",
    color: "border-primary-200",
  },
  {
    quote:
      "She didn't like mathematics at all, but now the first homework she wants to finish is math. She's always excited to join tutoring sessions.",
    author: "Ari's Mom",
    color: "border-green-200",
  },
  {
    quote:
      "Our son loves going to school already knowing the material and coming back with interesting questions for the tutor.",
    author: "Subedei's Mom",
    color: "border-amber-200",
  },
];

const mathlyFeatures = [
  { icon: Brain, label: "Adaptive Problems", desc: "AI adjusts difficulty to your level" },
  { icon: Flame, label: "Daily Streaks", desc: "Build consistent practice habits" },
  { icon: BarChart3, label: "Progress Tracking", desc: "See your growth over time" },
  { icon: Trophy, label: "Achievements", desc: "Earn rewards as you improve" },
];

export default function HomePage() {
  return (
    <>
      {/* Hero */}
      <section className="relative bg-gradient-to-br from-primary-900 via-primary-800 to-primary-700 text-white pt-32 pb-24 overflow-hidden">
        {/* Background decoration */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-40 -right-40 w-96 h-96 rounded-full bg-white/5 blur-3xl" />
          <div className="absolute -bottom-20 -left-20 w-80 h-80 rounded-full bg-primary-500/20 blur-3xl" />
          <div className="mongolian-vertical">ᠮᠣᠩᠭᠣᠯ ᠫᠣᠲ᠋ᠧᠨᠼᠢᠶᠠᠯ ᠠᠻᠠᠳ᠋ᠧᠮᠢ</div>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-1.5 text-sm mb-6">
              <span className="text-yellow-300">✦</span>
              <span>World Class Education for Mongolians</span>
            </div>

            <h1 className="text-5xl sm:text-6xl font-bold leading-tight mb-6">
              Helping Mongol minds{" "}
              <span className="text-yellow-300">reach their potential</span>
            </h1>

            <p className="text-xl text-blue-100 leading-relaxed mb-10 max-w-2xl">
              High-quality math and science education for Mongolian students around the world—aligned
              with AP, IB, and US state curricula, while strengthening cultural connection through
              Mongolian-context problems and stories.
            </p>

            <div className="flex flex-wrap gap-4">
              <Link href="/tutoring" className="btn-white text-base px-8 py-3.5">
                Find Your Tutor
                <ArrowRight className="ml-2 h-4 w-4" />
              </Link>
              <Link
                href="/practice"
                className="inline-flex items-center gap-2 px-8 py-3.5 border-2 border-white/30 text-white font-semibold rounded-lg hover:bg-white/10 transition-colors text-base"
              >
                Try Practice Free
              </Link>
            </div>

            <div className="mt-10 flex flex-wrap gap-6 text-sm text-blue-200">
              {["No commitment required", "Flexible scheduling", "Bilingual tutors"].map((item) => (
                <span key={item} className="flex items-center gap-1.5">
                  <CheckCircle className="h-4 w-4 text-green-400" />
                  {item}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Mission section */}
      <section className="section bg-navy-DEFAULT">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
              To the Future of Mongolians Living Abroad
            </h2>
            <p className="text-gray-300 max-w-2xl mx-auto text-lg leading-relaxed">
              Many Mongolian children grow up in the United States and across the world. They remain
              proudly Mongolian—and deserve to be well-educated, confident, and connected to their
              heritage.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {features.map((f) => {
              const Icon = f.icon;
              return (
                <div key={f.title} className="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition-colors">
                  <div className={`inline-flex p-3 rounded-xl ${f.bg} mb-4`}>
                    <Icon className={`h-6 w-6 ${f.color}`} />
                  </div>
                  <h3 className="text-lg font-semibold text-white mb-2">{f.title}</h3>
                  <p className="text-gray-400 text-sm leading-relaxed">{f.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Mathly Practice Platform */}
      <section className="section bg-gradient-to-br from-primary-50 to-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div>
              <div className="badge bg-primary-100 text-primary-700 mb-4">
                New: AI-Powered Practice
              </div>
              <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-5">
                Practice math with adaptive AI
              </h2>
              <p className="text-gray-600 text-lg leading-relaxed mb-8">
                Our Mathly practice platform adapts to your level, giving you problems that challenge
                you just the right amount. Get AI-powered hints, track your streaks, and earn
                achievements as you improve.
              </p>

              <div className="grid grid-cols-2 gap-4 mb-8">
                {mathlyFeatures.map((f) => {
                  const Icon = f.icon;
                  return (
                    <div key={f.label} className="flex items-start gap-3">
                      <div className="p-2 bg-primary-100 rounded-lg flex-shrink-0">
                        <Icon className="h-4 w-4 text-primary-600" />
                      </div>
                      <div>
                        <p className="font-semibold text-gray-900 text-sm">{f.label}</p>
                        <p className="text-gray-500 text-xs">{f.desc}</p>
                      </div>
                    </div>
                  );
                })}
              </div>

              <Link href="/practice" className="btn-primary text-base px-8 py-3.5">
                Start Practicing Free
                <ArrowRight className="ml-2 h-4 w-4" />
              </Link>
            </div>

            {/* Practice card preview */}
            <div className="relative">
              <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-6">
                <div className="flex items-center justify-between mb-4">
                  <div>
                    <p className="text-xs text-gray-500 font-medium">ALGEBRA • LEVEL 3</p>
                    <p className="font-semibold text-gray-900 text-sm mt-0.5">Problem 4 of 10</p>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="text-orange-500 font-bold text-sm">🔥 7</span>
                    <span className="text-primary-600 font-bold text-sm">⭐ 420 XP</span>
                  </div>
                </div>
                <div className="h-1.5 bg-gray-100 rounded-full mb-6">
                  <div className="h-full w-2/5 bg-primary-600 rounded-full" />
                </div>
                <div className="bg-gray-50 rounded-xl p-4 mb-4">
                  <p className="text-gray-900 font-medium text-sm leading-relaxed">
                    If 3x + 7 = 22, what is the value of 6x − 4?
                  </p>
                </div>
                <div className="grid grid-cols-2 gap-2 mb-4">
                  {["A. 20", "B. 26", "C. 30", "D. 34"].map((opt, i) => (
                    <button
                      key={opt}
                      className={`px-3 py-2.5 rounded-lg text-sm font-medium border transition-colors text-left ${
                        i === 1
                          ? "bg-primary-600 text-white border-primary-600"
                          : "border-gray-200 text-gray-700 hover:border-primary-300"
                      }`}
                    >
                      {opt}
                    </button>
                  ))}
                </div>
                <button className="w-full btn-primary py-2.5 text-sm">Submit Answer</button>
              </div>
              {/* XP badge */}
              <div className="absolute -top-4 -right-4 bg-yellow-400 text-yellow-900 rounded-full px-3 py-1 text-xs font-bold shadow-lg">
                +15 XP
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Exam Prep */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
              Exam preparation you can trust
            </h2>
            <p className="text-gray-500 max-w-xl mx-auto">
              Expert preparation for the exams that matter most to Mongolian students studying abroad.
            </p>
          </div>
          <div className="flex flex-wrap justify-center gap-3 mb-10">
            {examTypes.map((exam) => (
              <Link
                key={exam}
                href="/exam-prep"
                className="px-4 py-2 bg-primary-50 text-primary-700 rounded-full text-sm font-medium hover:bg-primary-100 transition-colors"
              >
                {exam}
              </Link>
            ))}
          </div>
          <div className="text-center">
            <Link href="/exam-prep" className="btn-primary text-base">
              View All Exam Programs
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
      </section>

      {/* Grade Levels */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
              Math tutoring for every age group
            </h2>
            <p className="text-gray-500 max-w-lg mx-auto">
              We believe everyone can learn. We offer world-class online tutoring from 2nd grade
              through adulthood.
            </p>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
            {grades.map((g) => (
              <Link
                key={g.label}
                href={g.href}
                className="card hover:border-primary-200 hover:shadow-md text-center group"
              >
                <p className="font-semibold text-gray-900 group-hover:text-primary-600 transition-colors">
                  {g.label}
                </p>
                <p className="text-gray-400 text-xs mt-1">{g.range}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="section bg-white">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
              Success stories from our students
            </h2>
            <p className="text-gray-500">Real words from Mongolian families learning with us online</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {testimonials.map((t) => (
              <div
                key={t.author}
                className={`card border-l-4 ${t.color} hover:shadow-md`}
              >
                <p className="text-gray-600 leading-relaxed mb-4 text-sm">"{t.quote}"</p>
                <p className="font-semibold text-gray-900 text-sm">— {t.author}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="section bg-primary-600">
        <div className="container-lg text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Ready to reach your potential?
          </h2>
          <p className="text-blue-100 text-lg mb-8 max-w-xl mx-auto">
            Join hundreds of Mongolian students worldwide who are building confidence and excelling in
            math.
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <Link href="/tutoring" className="btn-white text-base px-8 py-3.5">
              Find Your Tutor
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
            <Link
              href="/practice"
              className="inline-flex items-center gap-2 px-8 py-3.5 border-2 border-white/40 text-white font-semibold rounded-lg hover:bg-white/10 transition-colors text-base"
            >
              Try Practice Free
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
