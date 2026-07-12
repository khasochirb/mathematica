"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { getPrecalcUnit, getPrecalcSpine } from "@/lib/genmath-lessons";

// A Precalculus unit page: what it builds on, then the lessons in order.
export default function PrecalcUnitPage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const unit = getPrecalcUnit(unitSlug);
  const spineEntry = getPrecalcSpine().find((u) => u.slug === unitSlug);

  if (!unit) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Unit <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href="/math/precalculus" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> Back to the course
          </Link>
        </div>
      </div>
    );
  }

  const buildsOn = unit.buildsOn ?? spineEntry?.buildsOn;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        {/* Back + eyebrow */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/math/precalculus"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Precalculus · Unit {unit.unit}</div>
        </div>

        {/* Unit heading */}
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(30px, 5vw, 52px)",
            letterSpacing: "-0.04em",
            lineHeight: 1.02,
            color: "var(--fg)",
          }}
        >
          {unit.title}
        </h1>
        <p className="mt-3 mb-6" style={{ color: "var(--fg-1)", fontSize: 16 }}>
          {unit.blurb}
        </p>

        {/* Builds on */}
        {buildsOn && (
          <div
            className="card-edit p-4 mb-10"
            style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
          >
            <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
              Builds on
            </div>
            <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
              {buildsOn}
            </p>
          </div>
        )}

        {/* Lesson list */}
        <div className="eyebrow mb-4">Lessons</div>
        <ol className="space-y-3">
          {unit.lessons.map((lesson, i) => (
            <li key={lesson.slug}>
              <Link
                href={`/math/precalculus/${unitSlug}/${lesson.slug}`}
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

        {/* Practice + Test yourself */}
        {(unit.practice.length > 0 || unit.testYourself.length > 0) && (
          <>
            <div className="eyebrow mt-10 mb-3">Ready to check yourself?</div>
            <div className="flex flex-wrap gap-3">
              {unit.practice.length > 0 && (
                <Link href={`/math/precalculus/${unitSlug}/practice`} className="btn btn-primary">
                  Practice
                </Link>
              )}
              {unit.testYourself.length > 0 && (
                <Link href={`/math/precalculus/${unitSlug}/test`} className="btn btn-line">
                  Test yourself
                </Link>
              )}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
