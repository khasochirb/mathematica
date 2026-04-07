"use client";

import { useState, useMemo } from "react";
import Link from "next/link";
import { ArrowLeft, Target, BarChart3, BookOpen, AlertTriangle } from "lucide-react";
import QuestionCard from "@/components/esh/QuestionCard";
import StatsPanel from "@/components/esh/StatsPanel";
import usePerformance from "@/lib/use-performance";

import test1aData from "@/data/questions/test1a.json";
import test1bData from "@/data/questions/test1b.json";
import test2aData from "@/data/questions/test2a.json";
import test2bData from "@/data/questions/test2b.json";
import test3aData from "@/data/questions/test3a.json";
import test3bData from "@/data/questions/test3b.json";

const ALL_TESTS = [
  { key: "1A", label: "Тест 1А", data: test1aData },
  { key: "1B", label: "Тест 1Б", data: test1bData },
  { key: "2A", label: "Тест 2А", data: test2aData },
  { key: "2B", label: "Тест 2Б", data: test2bData },
  { key: "3A", label: "Тест 3А", data: test3aData },
  { key: "3B", label: "Тест 3Б", data: test3bData },
];

const TOPICS = [
  { value: "", label: "Бүгд" },
  { value: "algebra", label: "Алгебр" },
  { value: "geometry", label: "Геометр" },
  { value: "trigonometry", label: "Тригнометр" },
  { value: "functions", label: "Функц" },
  { value: "logarithms", label: "Логарифм" },
  { value: "sequences", label: "Дараалал" },
  { value: "probability", label: "Магадлал" },
  { value: "combinatorics", label: "Комбинаторик" },
  { value: "calculus", label: "Анализ" },
  { value: "statistics", label: "Статистик" },
];

type Tab = "all" | "recommended" | "stats";

export default function ESHPracticePage() {
  const [selectedTopic, setSelectedTopic] = useState("");
  const [selectedTest, setSelectedTest] = useState("1A");
  const [activeTab, setActiveTab] = useState<Tab>("all");
  const perf = usePerformance();

  const handleAnswer = (
    questionSource: string,
    topic: string,
    subtopic: string,
    difficulty: number,
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) => {
    perf.recordAttempt({
      questionSource,
      topic,
      subtopic,
      difficulty,
      selectedAnswer: selected,
      correctAnswer: correct,
      isCorrect,
    });
  };

  const weakTopics = perf.getWeakTopics();
  const topicStats = perf.getTopicStats();
  const overall = perf.getOverallStats();

  const allQuestions = useMemo(() => ALL_TESTS.flatMap((t) => t.data), []);
  const currentTestData = ALL_TESTS.find((t) => t.key === selectedTest)?.data || [];

  const questions = useMemo(() => {
    let qs: any[] = activeTab === "recommended" ? allQuestions : currentTestData;

    if (activeTab === "recommended") {
      qs = qs.filter((q: any) => {
        if (!weakTopics.includes(q.topic)) return false;
        const last = perf.getLastAttempt(q.source);
        return !last || !last.isCorrect;
      });
      if (qs.length === 0) {
        qs = allQuestions.filter((q: any) => weakTopics.includes(q.topic));
      }
    }

    if (selectedTopic) {
      qs = qs.filter((q: any) => q.topic === selectedTopic);
    }

    return qs;
  }, [activeTab, selectedTopic, weakTopics, perf, currentTestData, allQuestions]);

  const tabs = [
    { key: "all" as Tab, label: "Бүх бодлого", icon: BookOpen, count: currentTestData.length },
    {
      key: "recommended" as Tab,
      label: "Санал болгох",
      icon: Target,
      count: allQuestions.filter((q: any) => weakTopics.includes(q.topic)).length,
      badge: overall.total > 0,
    },
    { key: "stats" as Tab, label: "Статистик", icon: BarChart3 },
  ];

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Back + header */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="flex-1">
            <h1 className="font-display text-xl font-bold text-white">
              ЭЕШ Математик
            </h1>
            <p className="text-sm text-gray-500">
              {ALL_TESTS.length} тест, {allQuestions.length} бодлого
            </p>
          </div>
          {overall.total > 0 && (
            <div className="text-right">
              <span
                className={`text-2xl font-bold ${
                  overall.accuracy >= 80
                    ? "text-emerald-400"
                    : overall.accuracy >= 50
                    ? "text-yellow-400"
                    : "text-red-400"
                }`}
              >
                {overall.accuracy}%
              </span>
              <p className="text-xs text-gray-500">
                {overall.correct}/{overall.total} зөв
              </p>
            </div>
          )}
        </div>

        {/* Tabs */}
        <div className="flex gap-1 mb-6 bg-white/[0.03] border border-white/[0.06] rounded-xl p-1">
          {tabs.map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.key}
                onClick={() => setActiveTab(tab.key)}
                className={`flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium transition-all relative ${
                  activeTab === tab.key
                    ? "bg-primary-500/15 text-primary-300 border border-primary-400/20"
                    : "text-gray-500 hover:text-gray-300 border border-transparent"
                }`}
              >
                <Icon className="w-4 h-4" />
                <span className="hidden sm:inline">{tab.label}</span>
                {"count" in tab && tab.count !== undefined && (
                  <span className="text-xs text-gray-600">({tab.count})</span>
                )}
                {"badge" in tab && tab.badge && (
                  <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-orange-500 rounded-full" />
                )}
              </button>
            );
          })}
        </div>

        {/* Test selector */}
        {activeTab === "all" && (
          <div className="flex gap-2 mb-6 overflow-x-auto pb-1">
            {ALL_TESTS.map((t) => (
              <button
                key={t.key}
                onClick={() => setSelectedTest(t.key)}
                className={`px-4 py-2 rounded-xl text-sm font-medium whitespace-nowrap transition-all ${
                  selectedTest === t.key
                    ? "bg-primary-500/20 text-primary-300 border border-primary-400/25"
                    : "bg-white/[0.04] text-gray-500 border border-white/[0.08] hover:bg-white/[0.08] hover:text-gray-300"
                }`}
              >
                {t.label}
                <span className="ml-1 text-xs opacity-60">({t.data.length})</span>
              </button>
            ))}
          </div>
        )}

        {/* Recommended message */}
        {activeTab === "recommended" && overall.total > 0 && weakTopics.length > 0 && (
          <div className="card-glass p-4 mb-6 border-orange-400/15">
            <div className="flex items-start gap-3">
              <AlertTriangle className="w-5 h-5 text-orange-400 shrink-0 mt-0.5" />
              <div>
                <p className="text-sm text-orange-300">
                  <span className="font-semibold">Сайжруулах сэдвүүд: </span>
                  {weakTopics
                    .map((t) => {
                      const stat = topicStats.find((s) => s.topic === t);
                      const label = TOPICS.find((tp) => tp.value === t)?.label || t;
                      return stat ? `${label} (${stat.accuracy}%)` : label;
                    })
                    .join(", ")}
                </p>
                <p className="text-xs text-gray-500 mt-1">
                  Бүх тестүүдээс эдгээр сэдвийн бодлогуудыг цуглуулсан.
                </p>
              </div>
            </div>
          </div>
        )}

        {activeTab === "recommended" && overall.total === 0 && (
          <div className="card-glass p-8 text-center mb-6">
            <Target className="w-10 h-10 text-gray-600 mx-auto mb-3" />
            <p className="text-gray-300 font-medium">Эхлээд бодлого бодоорой!</p>
            <p className="text-sm text-gray-500 mt-1 mb-4">
              Бодлого бодсоны дараа сул сэдвүүдийн бодлогуудыг санал болгоно.
            </p>
            <button
              onClick={() => setActiveTab("all")}
              className="btn-primary text-sm px-6 py-2"
            >
              Бодлого бодох
            </button>
          </div>
        )}

        {/* Topic filter */}
        {activeTab !== "stats" && (
          <div className="mb-6 flex flex-wrap gap-2">
            {TOPICS.map((t) => (
              <button
                key={t.value}
                onClick={() =>
                  setSelectedTopic(selectedTopic === t.value ? "" : t.value)
                }
                className={`px-3 py-1.5 rounded-full text-xs font-medium transition-all border ${
                  selectedTopic === t.value
                    ? "bg-primary-500/20 text-primary-300 border-primary-400/30"
                    : weakTopics.includes(t.value) && activeTab === "recommended"
                    ? "bg-orange-500/10 text-orange-400 border-orange-400/20 hover:bg-orange-500/15"
                    : "bg-white/[0.04] text-gray-500 border-white/[0.08] hover:bg-white/[0.08] hover:text-gray-300"
                }`}
              >
                {t.label}
                {weakTopics.includes(t.value) && overall.total > 0 && (
                  <span className="ml-1 w-1.5 h-1.5 bg-orange-500 rounded-full inline-block" />
                )}
              </button>
            ))}
          </div>
        )}

        {/* Stats tab */}
        {activeTab === "stats" && (
          <StatsPanel
            overall={overall}
            topicStats={topicStats}
            onClear={perf.clearAll}
          />
        )}

        {/* Questions */}
        {activeTab !== "stats" && (
          <div>
            {questions.map((q: any, i: number) => (
              <QuestionCard
                key={q.source}
                question={q}
                onAnswer={handleAnswer}
                highlight={
                  activeTab === "recommended" && weakTopics.includes(q.topic)
                }
              />
            ))}

            {questions.length === 0 && (
              <div className="text-center py-12 text-gray-500">
                Энэ сэдвээр бодлого олдсонгүй.
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
