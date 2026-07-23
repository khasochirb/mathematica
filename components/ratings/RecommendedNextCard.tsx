"use client";

// The pinned "start here" card — the owner's-voice recommendation for the
// focus attribute. When the attribute isn't confidently rated yet, the primary
// action is its adaptive placement test (the accurate way to pin down level);
// otherwise it's the course, with ranked "do X → +N points" next steps that
// point only at the units the student actually missed.

import Link from "next/link";
import { ArrowRight, Pin, Target } from "lucide-react";
import type { CourseRecommendation, ImprovementStep } from "@/lib/ratings";
import { useLang } from "@/lib/lang-context";

const i18n = {
  eyebrow: { en: "Recommended for you", mn: "Танд зөвлөх нь" },
  start: { en: "Start", mn: "Эхлэх" },
  placement: { en: "Take placement test", mn: "Түвшин тогтоох тест" },
  toRaise: { en: "To raise this rating", mn: "Энэ үнэлгээг өсгөхийн тулд" },
  pts: { en: "pts", mn: "оноо" },
};

function stepLabel(s: ImprovementStep, L: "en" | "mn") {
  return L === "mn" ? s.labelMn : s.labelEn;
}

export default function RecommendedNextCard({ rec }: { rec: CourseRecommendation }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";

  // When the focus isn't rated yet, lead with the placement test.
  const primaryHref = rec.needsPlacement ? rec.placementHref : rec.courseHref;
  const primaryLabel = rec.needsPlacement ? i18n.placement[L] : i18n.start[L];

  // "How to raise this" steps that carry a projected gain (skip the bare
  // "get rated" placement step here — it's already the primary CTA).
  const gainSteps = rec.improvements.filter((s) => (s.delta ?? 0) > 0).slice(0, 3);

  return (
    <section
      className="card-edit p-5"
      style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
    >
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div className="flex items-start gap-3 min-w-0 flex-1" style={{ minWidth: 240 }}>
          <Pin className="h-4 w-4 mt-1 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <div className="min-w-0">
            <div className="eyebrow" style={{ color: "var(--accent)" }}>
              {i18n.eyebrow[L]}
            </div>
            <p
              className="serif mt-1"
              style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.01em", color: "var(--fg)" }}
            >
              {L === "mn" ? rec.courseTitleMn : rec.courseTitleEn}
            </p>
            <p className="text-[13px] mt-1" style={{ color: "var(--fg-1)" }}>
              {L === "mn" ? rec.explanationMn : rec.explanationEn}
            </p>
          </div>
        </div>
        <Link href={primaryHref} className="btn btn-primary flex-shrink-0">
          {primaryLabel}
          <ArrowRight className="ml-1 h-3.5 w-3.5" />
        </Link>
      </div>

      {gainSteps.length > 0 && (
        <div className="mt-4 pt-3" style={{ borderTop: "1px solid var(--accent-line)" }}>
          <div className="mono text-[10px] uppercase mb-2" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
            {i18n.toRaise[L]}
          </div>
          <ul className="space-y-1.5">
            {gainSteps.map((s) => (
              <li key={`${s.kind}:${s.unitSlug ?? s.href}`}>
                <Link
                  href={s.href}
                  className="flex items-center gap-2 text-[13px]"
                  style={{ color: "var(--fg-1)", textDecoration: "none" }}
                >
                  <Target className="h-3.5 w-3.5 flex-shrink-0" style={{ color: "var(--accent)" }} />
                  <span className="flex-1 min-w-0">{stepLabel(s, L)}</span>
                  <span className="mono tabular text-[12px] flex-shrink-0" style={{ color: "var(--accent)" }}>
                    +{s.delta} {i18n.pts[L]}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      )}
    </section>
  );
}
