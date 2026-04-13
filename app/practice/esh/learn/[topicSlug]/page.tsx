"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, BookOpen, Lightbulb, Target } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { TOPIC_LABELS, getQuestionsByTopic } from "@/lib/esh-questions";
import topicsData from "@/data/learn/topics.json";

export default function TopicLearnPage() {
  const params = useParams();
  const topicSlug = params.topicSlug as string;
  const data = (topicsData as any)[topicSlug];

  if (!data) {
    return (
      <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-400 mb-4">Сэдэв олдсонгүй</p>
          <Link
            href="/practice/esh/learn"
            className="text-primary-400 hover:text-primary-300 text-sm"
          >
            Буцах
          </Link>
        </div>
      </div>
    );
  }

  const questionCount = getQuestionsByTopic(topicSlug).length;

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh/learn"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              {data.title}
            </h1>
            <p className="text-sm text-gray-500">{questionCount} бодлого байна</p>
          </div>
        </div>

        {/* Overview */}
        <div className="card-glass p-6 mb-6">
          <div className="flex items-center gap-2 mb-3">
            <BookOpen className="w-5 h-5 text-primary-400" />
            <h2 className="font-display text-base font-bold text-white">
              Тойм
            </h2>
          </div>
          <p className="text-sm text-gray-300 leading-relaxed">
            {data.overview}
          </p>
        </div>

        {/* Key formulas */}
        <div className="card-glass p-6 mb-6">
          <h2 className="font-display text-base font-bold text-white mb-4">
            Гол томьёонууд
          </h2>
          <div className="space-y-4">
            {data.formulas.map(
              (formula: { title: string; latex: string }, i: number) => (
                <div
                  key={i}
                  className="p-4 bg-white/[0.03] border border-white/[0.06] rounded-xl"
                >
                  <p className="text-xs font-medium text-primary-300 mb-2">
                    {formula.title}
                  </p>
                  <div className="text-gray-200 text-sm">
                    <MathText text={formula.latex} />
                  </div>
                </div>
              ),
            )}
          </div>
        </div>

        {/* Tips */}
        <div className="card-glass p-6 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <Lightbulb className="w-5 h-5 text-yellow-400" />
            <h2 className="font-display text-base font-bold text-white">
              Зөвлөгөө
            </h2>
          </div>
          <ul className="space-y-2">
            {data.tips.map((tip: string, i: number) => (
              <li key={i} className="flex items-start gap-2 text-sm text-gray-300">
                <span className="w-1.5 h-1.5 rounded-full bg-yellow-500 mt-1.5 shrink-0" />
                {tip}
              </li>
            ))}
          </ul>
        </div>

        {/* Practice link */}
        <Link
          href={`/practice/esh/practice`}
          className="card-glass p-5 flex items-center gap-4 hover:border-primary-400/30 transition-all group"
        >
          <div className="w-10 h-10 rounded-xl bg-primary-500/15 flex items-center justify-center">
            <Target className="w-5 h-5 text-primary-400" />
          </div>
          <div className="flex-1">
            <p className="text-sm font-medium text-white group-hover:text-primary-300 transition-colors">
              Энэ сэдвээр дадлага хийх
            </p>
            <p className="text-xs text-gray-500">
              {questionCount} бодлого бэлэн байна
            </p>
          </div>
        </Link>
      </div>
    </div>
  );
}
