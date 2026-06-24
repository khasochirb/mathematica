"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getGenMathTopic } from "@/lib/genmath-lessons";

export default function GenMathTopicPage() {
  const params = useParams();
  const topicSlug = params.topic as string;
  const topic = getGenMathTopic(topicSlug);

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
            href="/math/6"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Grade 6</div>
        </div>

        {/* Topic heading */}
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(32px, 5vw, 56px)",
            letterSpacing: "-0.04em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          {topic.title}
        </h1>
        <p className="mt-3 mb-10" style={{ color: "var(--fg-1)", fontSize: 16 }}>
          {topic.blurb}
        </p>

        {/* Lesson list */}
        <div className="eyebrow mb-4">Lessons</div>
        <ol className="space-y-3 mb-10">
          {topic.lessons.map((lesson, i) => (
            <li key={lesson.slug}>
              <Link
                href={`/math/6/${topicSlug}/${lesson.slug}`}
                className="card-edit p-5 flex items-center gap-4 transition-colors"
                style={{ textDecoration: "none" }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
                  (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "";
                  (e.currentTarget as HTMLAnchorElement).style.background = "";
                }}
              >
                <span
                  className="mono text-[11px] flex-shrink-0 tabular"
                  style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}
                >
                  {String(i + 1).padStart(2, "0")}
                </span>
                <span
                  className="serif flex-1"
                  style={{ fontWeight: 400, fontSize: 17, letterSpacing: "-0.01em", color: "var(--fg)" }}
                >
                  {lesson.title}
                </span>
              </Link>
            </li>
          ))}
        </ol>

        {/* Practice + Test buttons */}
        <div className="flex gap-3 flex-wrap">
          <Link href={`/math/6/${topicSlug}/practice`} className="btn btn-primary">
            Practice
          </Link>
          <Link href={`/math/6/${topicSlug}/test`} className="btn btn-line">
            Test yourself
          </Link>
        </div>
      </div>
    </div>
  );
}
