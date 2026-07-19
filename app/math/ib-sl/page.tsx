"use client";

import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getIbSlSpine } from "@/lib/genmath-lessons";

// The IB Mathematics SL course hub — Analysis & Approaches, taught by the
// official syllabus: five topics, each lesson one subtopic code (SL 1.1,
// SL 1.2, …), formulas flagged booklet/memorize, solutions to markscheme
// standard. Lives under /math for the course machinery; the IB hub at
// /practice/ib is the front door.
export default function IbSlCoursePage() {
  const spine = getIbSlSpine();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link href="/practice/ib" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">IB Mathematics · Analysis &amp; Approaches</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 54px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
          IB Math SL
        </h1>
        <p className="mt-4 mb-4" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          The complete Analysis &amp; Approaches SL syllabus, taught topic by
          topic and code by code — every lesson is one official subtopic
          (SL 1.1, SL 1.2, …), every formula flagged as in-the-booklet or
          memorize, and every worked example solved the way an IB examiner
          marks it: method, accuracy, and reasoning.
        </p>
        <p className="mb-8 text-[13px]" style={{ color: "var(--fg-3)", maxWidth: "56ch" }}>
          English-only, like the real exam. HL — which contains everything
          here plus its extension codes — opens after the SL topics land.
        </p>

        {/* The spine */}
        <div className="eyebrow mb-4">The course — 5 topics, in syllabus order</div>
        <ol className="space-y-3">
          {spine.map((u) => {
            return u.live ? (
              <li key={u.slug}>
                <Link
                  href={`/math/ib-sl/${u.slug}`}
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
                    {String(u.unit).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="serif block" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {u.title}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {u.blurb}
                    </span>
                  </span>
                  <span className="mono text-[10px] uppercase mt-1 flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
                    Start
                  </span>
                </Link>
              </li>
            ) : (
              <li key={u.slug}>
                <div className="card-edit p-5 flex items-start gap-4" style={{ opacity: 0.45, cursor: "default" }}>
                  <span className="mono text-[11px] flex-shrink-0 tabular mt-1" style={{ color: "var(--fg-3)", letterSpacing: "0.04em", minWidth: 24 }}>
                    {String(u.unit).padStart(2, "0")}
                  </span>
                  <span className="flex-1 min-w-0">
                    <span className="serif block" style={{ fontWeight: 400, fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                      {u.title}
                    </span>
                    <span className="block mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>
                      {u.blurb}
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
