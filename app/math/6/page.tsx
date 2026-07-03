"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Sparkles } from "lucide-react";
import { getGrade6Topics } from "@/lib/genmath-lessons";
import { useAuth } from "@/lib/auth-context";
import { loadPlacement, type StoredPlacement } from "@/lib/placement-result";

export default function Grade6TopicsPage() {
  const topics = getGrade6Topics();
  const { user } = useAuth();
  const [placement, setPlacement] = useState<StoredPlacement | null>(null);

  // Placement result lives in the browser (keyed to the account when signed in),
  // so load it after mount and re-read when the signed-in user changes.
  useEffect(() => {
    setPlacement(loadPlacement(user?.id));
  }, [user?.id]);

  const prioritySet = new Set(placement?.priorityTopics ?? []);
  const priorityTitles = (placement?.priorityTopics ?? [])
    .map((slug) => topics.find((t) => t.slug === slug)?.title)
    .filter(Boolean) as string[];

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Grade 6</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          Grade 6 Topics
        </h1>
        <p className="mt-3 mb-6" style={{ color: "var(--fg-1)", fontSize: 16 }}>
          Select a topic to explore lessons, practice problems, and self-tests.
        </p>

        {/* Placement CTA / summary */}
        {placement ? (
          <Link href="/math/6/placement" className="card-edit p-4 mb-8 flex items-center gap-4" style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}>
            <span className="grid h-9 w-9 flex-shrink-0 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
              <Sparkles className="h-4.5 w-4.5" />
            </span>
            <div className="flex-1 min-w-0">
              <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>
                You're at the <b style={{ color: "var(--accent)" }}>{placement.level}</b> level
              </p>
              <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                {priorityTitles.length > 0
                  ? <>Focus first on <b>{priorityTitles.slice(0, 3).join(", ")}</b> — marked below.</>
                  : <>You're strong across the board. Retake anytime.</>}
              </p>
            </div>
            <span className="mono text-[11px] flex-shrink-0" style={{ color: "var(--accent)" }}>Retake →</span>
          </Link>
        ) : (
          <Link href="/math/6/placement" className="card-edit p-4 mb-8 flex items-center gap-4" style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}>
            <span className="grid h-9 w-9 flex-shrink-0 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
              <Sparkles className="h-4.5 w-4.5" />
            </span>
            <div className="flex-1 min-w-0">
              <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>Take the placement test</p>
              <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                A quick adaptive test builds a personalized plan and marks the topics most important for you.
              </p>
            </div>
            <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          </Link>
        )}

        <div className="space-y-3">
          {topics.map((topic, i) => {
            const important = prioritySet.has(topic.slug);
            return (
              <Link
                key={topic.slug}
                href={`/math/6/${topic.slug}`}
                className="card-edit p-5 flex items-center gap-5 transition-colors"
                style={{ textDecoration: "none", ...(important ? { borderColor: "var(--accent-line)" } : {}) }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
                  (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = important ? "var(--accent-line)" : "";
                  (e.currentTarget as HTMLAnchorElement).style.background = "";
                }}
              >
                <span className="mono text-[11px] flex-shrink-0 tabular" style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap">
                    <p className="serif" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {topic.title}
                    </p>
                    {important && (
                      <span className="rounded-full px-2 py-0.5 text-[10px] font-medium" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
                        Important for you
                      </span>
                    )}
                  </div>
                  <p className="text-[13px] mt-0.5 truncate" style={{ color: "var(--fg-2)" }}>
                    {topic.blurb}
                  </p>
                </div>
                <span className="mono text-[11px] flex-shrink-0" style={{ color: "var(--fg-3)" }}>
                  {topic.lessons.length} lesson{topic.lessons.length !== 1 ? "s" : ""}
                </span>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
