"use client";

import Link from "next/link";
import { ArrowLeft, BookOpen, ChevronRight } from "lucide-react";
import { TOPICS, TOPIC_LABELS } from "@/lib/esh-questions";
import topicsData from "@/data/learn/topics.json";

const topicColors: Record<string, string> = {
  algebra: "bg-primary-500/15 text-primary-400",
  geometry: "bg-emerald-500/15 text-emerald-400",
  trigonometry: "bg-cyan-500/15 text-cyan-400",
  functions: "bg-yellow-500/15 text-yellow-400",
  logarithms: "bg-purple-500/15 text-purple-400",
  sequences: "bg-orange-500/15 text-orange-400",
  probability: "bg-pink-500/15 text-pink-400",
  combinatorics: "bg-red-500/15 text-red-400",
  calculus: "bg-blue-500/15 text-blue-400",
  statistics: "bg-teal-500/15 text-teal-400",
};

export default function LearnPage() {
  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              Суралцах
            </h1>
            <p className="text-sm text-gray-500">
              Сэдвээр томьёо, зөвлөгөө, видео хичээл
            </p>
          </div>
        </div>

        {/* Topic grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {TOPICS.map((topic) => {
            const data = (topicsData as any)[topic.value];
            if (!data) return null;
            const colorCls = topicColors[topic.value] || "bg-primary-500/15 text-primary-400";

            return (
              <Link
                key={topic.value}
                href={`/practice/esh/learn/${topic.value}`}
                className="card-glass p-5 hover:border-white/[0.15] hover:bg-white/[0.03] transition-all group"
              >
                <div className="flex items-start justify-between mb-3">
                  <div
                    className={`w-10 h-10 rounded-xl flex items-center justify-center ${colorCls}`}
                  >
                    <BookOpen className="w-5 h-5" />
                  </div>
                  <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-gray-400 transition-colors" />
                </div>
                <h3 className="font-display font-bold text-white mb-1">
                  {data.title}
                </h3>
                <p className="text-sm text-gray-500 line-clamp-2 mb-3">
                  {data.overview}
                </p>
                <div className="flex items-center gap-3 text-xs text-gray-600">
                  <span>{data.formulas.length} томьёо</span>
                  <span>{data.tips.length} зөвлөгөө</span>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
