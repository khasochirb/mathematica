"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import { getGenMathTopicLocalized } from "@/lib/genmath-lessons";
import { useLang } from "@/lib/lang-context";
import ContentGate from "@/components/genmath/ContentGate";

const REVEAL_LABELS_EN = {
  reveal: "Show solution",
  hide: "Hide",
  revealAria: "Show solution",
  hideAria: "Hide solution",
};
const REVEAL_LABELS_MN = {
  reveal: "Бодолтыг харах",
  hide: "Нуух",
  revealAria: "Бодолтыг харах",
  hideAria: "Бодолтыг нуух",
};

function GenMathPracticePageInner() {
  const params = useParams();
  const topicSlug = params.topic as string;
  const { lang } = useLang();
  const mn = lang === "mn";
  const REVEAL_LABELS = mn ? REVEAL_LABELS_MN : REVEAL_LABELS_EN;
  const topic = getGenMathTopicLocalized(topicSlug, lang);

  if (!topic) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Topic <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href="/math/8" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> Back to Grade 8
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href={`/math/8/${topicSlug}`}
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{mn ? "Ерөнхий математик · 8-р анги" : "General Math · Grade 8"} · {topic.title}</div>
        </div>

        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(28px, 4vw, 48px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          {mn ? "Дасгал" : "Practice"} — {topic.title}
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-2)", fontSize: 14 }}>
          {mn ? "Бодлого бүрийг бодоод, бодолтыг нээж хариугаа шалгаарай." : "Work through each problem, then reveal the solution to check your answer."}
        </p>

        <div className="space-y-4">
          {topic.practice.map((problem, i) => (
            <RevealProblemCard
              key={problem.id}
              problem={problem}
              index={i}
              labels={REVEAL_LABELS}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

// Content requires an account; the hub and topic pages above stay public.
export default function GenMathPracticePage() {
  const params = useParams();
  const topicSlug = params.topic as string;
  return (
    <ContentGate backHref={`/math/8/${topicSlug}`} backLabel="Back to topic">
      <GenMathPracticePageInner />
    </ContentGate>
  );
}
