"use client";

import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getIbHlSpine } from "@/lib/genmath-lessons";
import CoursePersonalization from "@/components/course/CoursePersonalization";

// The IB Mathematics HL course hub — the Additional Higher Level (AHL)
// extension codes of Analysis & Approaches, taught one code per lesson
// (AHL 1.10, AHL 1.11, …) at HL depth: proofs carry R marks, complex
// numbers go to De Moivre, and every problem chains ideas the way HL
// Paper 1 does. The shared SL foundation lives at /math/ib-sl; the IB hub
// at /practice/ib is the front door.
export default function IbHlCoursePage() {
  const spine = getIbHlSpine();

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
          IB Math HL
        </h1>
        <p className="mt-4 mb-4" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          The Additional Higher Level syllabus of Analysis &amp; Approaches,
          taught code by code — every lesson is one official AHL subtopic
          (AHL 1.10, AHL 1.11, …), pitched at genuine HL depth: proof by
          induction and contradiction, complex numbers to De Moivre and
          roots, and worked examples marked the way HL examiners mark —
          method, accuracy, and reasoning.
        </p>
        <p className="mb-8 text-[13px]" style={{ color: "var(--fg-3)", maxWidth: "56ch" }}>
          HL = SL + these extension codes. The shared foundation is the{" "}
          <Link href="/math/ib-sl" style={{ color: "var(--accent)", textDecoration: "underline" }}>
            complete SL course
          </Link>{" "}
          — an HL student works both. English-only, like the real exam.
          Topics open in syllabus order.
        </p>

        <CoursePersonalization context="course:ib-hl" />

        {/* The spine */}
        <div className="eyebrow mb-4">The course — 5 topics, in syllabus order</div>
        <ol className="space-y-3">
          {spine.map((u) => {
            return u.live ? (
              <li key={u.slug}>
                <Link
                  href={`/math/ib-hl/${u.slug}`}
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
