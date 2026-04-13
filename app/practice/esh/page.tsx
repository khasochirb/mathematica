"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  FileText,
  Target,
  BookOpen,
  BarChart3,
  Trophy,
  Flag,
  ChevronRight,
  Flame,
  Zap,
} from "lucide-react";
import useESHProgress from "@/lib/use-esh-progress";
import { getAllTests, getAllQuestions } from "@/lib/esh-questions";

export default function ESHHubPage() {
  const [mounted, setMounted] = useState(false);
  const progress = useESHProgress();

  useEffect(() => setMounted(true), []);

  const allTests = getAllTests();
  const totalQuestions = getAllQuestions().length;

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
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
              {allTests.length} тест, {totalQuestions} бодлого
            </p>
          </div>
          {mounted && progress.totalTestsTaken > 0 && (
            <div className="text-right">
              <span
                className={`text-2xl font-bold ${
                  progress.averageAccuracy >= 80
                    ? "text-emerald-400"
                    : progress.averageAccuracy >= 50
                      ? "text-yellow-400"
                      : "text-red-400"
                }`}
              >
                {progress.averageAccuracy}%
              </span>
              <p className="text-xs text-gray-500">дундаж оноо</p>
            </div>
          )}
        </div>

        {/* Quick stats (only if user has data) */}
        {mounted && progress.totalTestsTaken > 0 && (
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8">
            <div className="card-glass p-4 text-center">
              <FileText className="w-5 h-5 text-primary-400 mx-auto mb-1.5" />
              <p className="text-lg font-bold text-white">
                {progress.totalTestsTaken}
              </p>
              <p className="text-[11px] text-gray-500">Тест бодсон</p>
            </div>
            <div className="card-glass p-4 text-center">
              <Zap className="w-5 h-5 text-yellow-400 mx-auto mb-1.5" />
              <p className="text-lg font-bold text-white">
                {progress.totalQuestionsAnswered}
              </p>
              <p className="text-[11px] text-gray-500">Бодлого бодсон</p>
            </div>
            <div className="card-glass p-4 text-center">
              <Flame className="w-5 h-5 text-orange-400 mx-auto mb-1.5" />
              <p className="text-lg font-bold text-white">
                {progress.weeklyActivity.thisWeek}
              </p>
              <p className="text-[11px] text-gray-500">Энэ долоо хоногт</p>
            </div>
            <div className="card-glass p-4 text-center">
              <Flag className="w-5 h-5 text-orange-400 mx-auto mb-1.5" />
              <p className="text-lg font-bold text-white">
                {progress.flaggedCount}
              </p>
              <p className="text-[11px] text-gray-500">Тэмдэглэсэн</p>
            </div>
          </div>
        )}

        {/* Recommendation banner */}
        {mounted && progress.practiceRecommendation && (
          <div className="card-glass p-4 mb-8 border-primary-400/10">
            <p className="text-sm text-gray-300">
              <span className="text-primary-400 font-medium">Зөвлөгөө: </span>
              {progress.practiceRecommendation}
            </p>
          </div>
        )}

        {/* Section cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {/* Practice Tests */}
          <Link
            href="/practice/esh/test"
            className="card-glass p-6 hover:border-primary-400/30 hover:bg-white/[0.03] transition-all group"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="w-11 h-11 rounded-xl bg-primary-500/15 flex items-center justify-center">
                <FileText className="w-5 h-5 text-primary-400" />
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-primary-400 transition-colors" />
            </div>
            <h2 className="font-display text-lg font-bold text-white group-hover:text-primary-300 transition-colors mb-1">
              Дадлага шалгалт
            </h2>
            <p className="text-sm text-gray-500 mb-3">
              Шалгалтын горимд цагтай бодоорой
            </p>
            <div className="flex items-center gap-3 text-xs text-gray-600">
              <span>{allTests.length} тест</span>
              {mounted && progress.totalTestsTaken > 0 && (
                <>
                  <span>·</span>
                  <span className="flex items-center gap-1">
                    <Trophy className="w-3 h-3 text-yellow-500" />
                    {progress.totalTestsTaken} бодсон
                  </span>
                </>
              )}
            </div>
          </Link>

          {/* Practice Problems */}
          <Link
            href="/practice/esh/practice"
            className="card-glass p-6 hover:border-emerald-400/30 hover:bg-white/[0.03] transition-all group"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="w-11 h-11 rounded-xl bg-emerald-500/15 flex items-center justify-center">
                <Target className="w-5 h-5 text-emerald-400" />
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-emerald-400 transition-colors" />
            </div>
            <h2 className="font-display text-lg font-bold text-white group-hover:text-emerald-300 transition-colors mb-1">
              Дадлага бодлого
            </h2>
            <p className="text-sm text-gray-500 mb-3">
              Сэдвээр дадлага хийж, сул талаа сайжруул
            </p>
            <div className="flex items-center gap-3 text-xs text-gray-600">
              <span>{totalQuestions} бодлого</span>
              {mounted && progress.weakTopics.length > 0 && (
                <>
                  <span>·</span>
                  <span className="text-orange-400">
                    {progress.weakTopics.length} сул сэдэв
                  </span>
                </>
              )}
            </div>
          </Link>

          {/* Learn */}
          <Link
            href="/practice/esh/learn"
            className="card-glass p-6 hover:border-cyan-400/30 hover:bg-white/[0.03] transition-all group"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="w-11 h-11 rounded-xl bg-cyan-500/15 flex items-center justify-center">
                <BookOpen className="w-5 h-5 text-cyan-400" />
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-cyan-400 transition-colors" />
            </div>
            <h2 className="font-display text-lg font-bold text-white group-hover:text-cyan-300 transition-colors mb-1">
              Суралцах
            </h2>
            <p className="text-sm text-gray-500 mb-3">
              Сэдвээр унших материал, томьёо, видео хичээл
            </p>
            <div className="flex items-center gap-3 text-xs text-gray-600">
              <span>10 сэдэв</span>
            </div>
          </Link>

          {/* Progress */}
          <Link
            href="/practice/esh/progress"
            className="card-glass p-6 hover:border-yellow-400/30 hover:bg-white/[0.03] transition-all group"
          >
            <div className="flex items-start justify-between mb-3">
              <div className="w-11 h-11 rounded-xl bg-yellow-500/15 flex items-center justify-center">
                <BarChart3 className="w-5 h-5 text-yellow-400" />
              </div>
              <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-yellow-400 transition-colors" />
            </div>
            <h2 className="font-display text-lg font-bold text-white group-hover:text-yellow-300 transition-colors mb-1">
              Прогресс
            </h2>
            <p className="text-sm text-gray-500 mb-3">
              Оноогоо хяна, ахицаа хар
            </p>
            <div className="flex items-center gap-3 text-xs text-gray-600">
              {mounted && progress.totalTestsTaken > 0 ? (
                <span>{progress.averageAccuracy}% дундаж</span>
              ) : (
                <span>Мэдээлэл байхгүй</span>
              )}
            </div>
          </Link>
        </div>

        {/* Recent test results */}
        {mounted && progress.completedSessions.length > 0 && (
          <div className="mt-8">
            <h2 className="font-display text-base font-bold text-white mb-4">
              Сүүлийн шалгалтууд
            </h2>
            <div className="space-y-2">
              {progress.completedSessions.slice(0, 5).map((s) => (
                <Link
                  key={s.id}
                  href={`/practice/esh/test/${s.testKey.toLowerCase()}/results?session=${s.id}`}
                  className="flex items-center gap-3 px-4 py-3 rounded-xl bg-white/[0.03] border border-white/[0.06] hover:bg-white/[0.05] transition-all"
                >
                  <span className="w-8 h-8 rounded-lg bg-primary-500/15 flex items-center justify-center text-xs font-bold text-primary-300">
                    {s.testKey}
                  </span>
                  <div className="flex-1">
                    <span className="text-sm text-gray-300">
                      Тест {s.testKey}
                    </span>
                    <span className="text-xs text-gray-600 ml-2">
                      {s.completedAt &&
                        new Date(s.completedAt).toLocaleDateString("mn-MN")}
                    </span>
                  </div>
                  <span
                    className={`text-sm font-bold ${
                      (s.score?.accuracy || 0) >= 80
                        ? "text-emerald-400"
                        : (s.score?.accuracy || 0) >= 50
                          ? "text-yellow-400"
                          : "text-red-400"
                    }`}
                  >
                    {s.score?.accuracy || 0}%
                  </span>
                  <ChevronRight className="w-4 h-4 text-gray-600" />
                </Link>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
