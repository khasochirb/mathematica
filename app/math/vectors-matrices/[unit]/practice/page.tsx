"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import GradedProblemList from "@/components/lesson/GradedProblemList";
import { getVecMatUnit } from "@/lib/genmath-lessons";
import ContentGate from "@/components/genmath/ContentGate";

const REVEAL_LABELS = {
  reveal: "Show solution",
  hide: "Hide",
  revealAria: "Show solution",
  hideAria: "Hide solution",
};

function VecMatPracticePageInner() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const unit = getVecMatUnit(unitSlug);

  if (!unit) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Unit <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href="/math/vectors-matrices" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
            <ArrowLeft className="h-3.5 w-3.5" /> Back to the course
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
            href={`/math/vectors-matrices/${unitSlug}`}
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Vectors & Matrices · Unit {unit.unit} · {unit.title}</div>
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
          Practice — {unit.title}
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-2)", fontSize: 14 }}>
          Work through each problem, then reveal the solution to check your answer.
        </p>

        <div className="space-y-4">
          <GradedProblemList problems={unit.practice} labels={REVEAL_LABELS} kind="practice" />
        </div>
      </div>
    </div>
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function VecMatPracticePage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/vectors-matrices/${unitSlug}`} backLabel="Back to unit">
      <VecMatPracticePageInner />
    </ContentGate>
  );
}
