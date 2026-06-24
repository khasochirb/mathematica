"use client";

import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getGrade6Topics } from "@/lib/genmath-lessons";

export default function Grade6TopicsPage() {
  const topics = getGrade6Topics();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/math"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Grade 6</div>
        </div>

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
          Grade 6 Topics
        </h1>
        <p className="mt-3 mb-10" style={{ color: "var(--fg-1)", fontSize: 16 }}>
          Select a topic to explore lessons, practice problems, and self-tests.
        </p>

        <div className="space-y-3">
          {topics.map((topic, i) => (
            <Link
              key={topic.slug}
              href={`/math/6/${topic.slug}`}
              className="card-edit p-5 flex items-center gap-5 transition-colors"
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
              <div className="flex-1 min-w-0">
                <p
                  className="serif"
                  style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}
                >
                  {topic.title}
                </p>
                <p className="text-[13px] mt-0.5 truncate" style={{ color: "var(--fg-2)" }}>
                  {topic.blurb}
                </p>
              </div>
              <span className="mono text-[11px] flex-shrink-0" style={{ color: "var(--fg-3)" }}>
                {topic.lessons.length} lesson{topic.lessons.length !== 1 ? "s" : ""}
              </span>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
