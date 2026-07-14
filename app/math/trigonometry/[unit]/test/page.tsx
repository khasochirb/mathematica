"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import GradedProblemList from "@/components/lesson/GradedProblemList";
import { getTrigUnit } from "@/lib/genmath-lessons";
import ContentGate from "@/components/genmath/ContentGate";

const REVEAL_LABELS = {
  reveal: "Show solution",
  hide: "Hide",
  revealAria: "Show solution",
  hideAria: "Hide solution",
};

function TrigTestPageInner() {
  const params = useParams();
  const unitSlug = params.unit as string;
  const unit = getTrigUnit(unitSlug);

  if (!unit) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Unit <em className="serif-italic" style={{ color: "var(--accent)" }}>not found</em>.
          </p>
          <Link href="/math/trigonometry" className="btn btn-line mt-5 inline-flex items-center gap-1.5">
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
            href={`/math/trigonometry/${unitSlug}`}
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Trigonometry · Unit {unit.unit} · {unit.title}</div>
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
          Test Yourself — {unit.title}
        </h1>

        {/* Note about grading mode */}
        <div
          className="card-edit p-4 mt-4 mb-8"
          style={{ background: "var(--bg-1)" }}
        >
          <p className="mono text-[11px] uppercase mb-1" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
            Self-graded
          </p>
          <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            Attempt each problem on paper, reveal the solution, and grade yourself honestly — your self-checks feed your progress stats.
          </p>
        </div>

        <div className="space-y-4">
          <GradedProblemList problems={unit.testYourself} labels={REVEAL_LABELS} kind="test" />
        </div>
      </div>
    </div>
  );
}

// Content requires an account; the hub and unit pages above stay public.
export default function TrigTestPage() {
  const params = useParams();
  const unitSlug = params.unit as string;
  return (
    <ContentGate backHref={`/math/trigonometry/${unitSlug}`} backLabel="Back to unit">
      <TrigTestPageInner />
    </ContentGate>
  );
}
