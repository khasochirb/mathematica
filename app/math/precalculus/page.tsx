"use client";

import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getPrecalcSpine } from "@/lib/genmath-lessons";
import CoursePersonalization from "@/components/course/CoursePersonalization";
import CoursePlacementCta from "@/components/course/CoursePlacementCta";

// The Precalculus course hub — the bridge to calculus, taught graph-first:
// function anatomy, transformations, polynomial and rational graphs,
// exponentials and logs, the unit circle, trig waves, and conic sections.
export default function PrecalcCoursePage() {
  const spine = getPrecalcSpine();

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Courses</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 54px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
          Precalculus
        </h1>
        <p className="mt-4 mb-8" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          The bridge to calculus, taught graph-first: functions and their
          transformations, polynomial and rational graphs, exponentials and
          logarithms, the unit circle and trig waves — ending at the conic
          sections. Every big idea arrives as a picture you can play with.
        </p>

        <CoursePlacementCta
          namespace="precalculus"
          href="/math/precalculus/placement"
          unitTitle={(s) => spine.find((u) => u.slug === s)?.title}
        />

        <CoursePersonalization context="course:precalculus" />

        {/* The spine */}
        <div className="eyebrow mb-4">The course — 8 units, in order</div>
        <ol className="space-y-3">
          {spine.map((u) => {
            return u.live ? (
              <li key={u.slug}>
                <Link
                  href={`/math/precalculus/${u.slug}`}
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
