"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import GradedProblemList from "@/components/lesson/GradedProblemList";
import { getGenMathTopicLocalized } from "@/lib/genmath-lessons";
import ContentGate from "@/components/genmath/ContentGate";
import { useLang } from "@/lib/lang-context";

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

function GenMathTestPageInner() {
  const params = useParams();
  const { lang } = useLang();
  const mn = lang === "mn";
  const REVEAL_LABELS = mn ? REVEAL_LABELS_MN : REVEAL_LABELS_EN;
  const topicSlug = params.topic as string;
  const topic = getGenMathTopicLocalized(topicSlug, lang);

  if (!topic) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Topic <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href="/math/6" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> Back to Grade 6
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
            href={`/math/6/${topicSlug}`}
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{mn ? "Ерөнхий математик · 6-р анги" : "General Math · Grade 6"} · {topic.title}</div>
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
          {mn ? "Өөрийгөө шалга — " : "Test Yourself — "}{topic.title}
        </h1>

        {/* Note about grading mode */}
        <div
          className="card-edit p-4 mt-4 mb-8"
          style={{ background: "var(--bg-1)" }}
        >
          <p className="mono text-[11px] uppercase mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
            {mn ? "Тун удахгүй" : "Coming soon"}
          </p>
          <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            {mn
              ? "Дүгнэдэг горим дараагийн шатанд нэмэгдэнэ. Одоохондоо бодлого бүрийг өөрөө бодоод, бодолтыг нээж шалгаарай."
              : "Graded mode coming in a later step. For now, attempt each problem and reveal the solution to self-check."}
          </p>
        </div>

        <div className="space-y-4">
          <GradedProblemList problems={topic.testYourself} labels={REVEAL_LABELS} kind="test" />
        </div>
      </div>
    </div>
  );
}

// Content requires an account; the hub and topic pages above stay public.
export default function GenMathTestPage() {
  const params = useParams();
  const topicSlug = params.topic as string;
  return (
    <ContentGate backHref={`/math/6/${topicSlug}`} backLabel="Back to topic">
      <GenMathTestPageInner />
    </ContentGate>
  );
}
