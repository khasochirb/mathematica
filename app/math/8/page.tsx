"use client";

import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getGrade8Spine, getGenMathTopic } from "@/lib/genmath-lessons";

// Grade 8 hub — built one topic at a time. The full roadmap is visible from
// day one: live topics link in, the rest show the road ahead.
export default function Grade8TopicsPage() {
  const spine = getGrade8Spine();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Grade 8</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          Grade 8 Topics
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "56ch" }}>
          The year algebra begins in earnest — real numbers, exponents, roots,
          linear equations and functions, and the data that lives on a graph.
          Each topic is taught from the ground up with interactive, self-checking lessons.
        </p>

        {/* The spine */}
        <div className="eyebrow mb-4">The course — 7 topics, in order</div>
        <ol className="space-y-3">
          {spine.map((t, i) => {
            const topic = t.live ? getGenMathTopic(t.slug) : null;
            const lessonCount = topic?.lessons.length ?? 0;
            return t.live ? (
              <li key={t.slug}>
                <Link
                  href={`/math/8/${t.slug}`}
                  className="card-edit p-5 flex items-start gap-4 transition-colors"
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
                  <span className="mono text-[11px] flex-shrink-0 tabular mt-1" style={{ color: "var(--accent)", letterSpacing: "0.04em", minWidth: 24 }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="serif block" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {t.title}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {t.blurb}
                    </span>
                  </span>
                  <span className="mono text-[11px] flex-shrink-0 mt-1" style={{ color: "var(--fg-3)" }}>
                    {lessonCount} lesson{lessonCount !== 1 ? "s" : ""}
                  </span>
                </Link>
              </li>
            ) : (
              <li key={t.slug}>
                <div className="card-edit p-5 flex items-start gap-4" style={{ opacity: 0.45, cursor: "default" }}>
                  <span className="mono text-[11px] flex-shrink-0 tabular mt-1" style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}>
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="serif block" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {t.title}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {t.blurb}
                    </span>
                  </span>
                  <span className="mono text-[10px] uppercase mt-1 flex-shrink-0" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    Soon
                  </span>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
}
