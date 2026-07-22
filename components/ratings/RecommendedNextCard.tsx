"use client";

// The pinned "start here" card — the owner's-voice recommendation derived
// from the lowest attribute ("Your Geometry attribute is 65 — your lowest;
// it is recommended you start from this course").

import Link from "next/link";
import { ArrowRight, Pin } from "lucide-react";
import type { CourseRecommendation } from "@/lib/ratings";
import { useLang } from "@/lib/lang-context";

const i18n = {
  eyebrow: { en: "Recommended for you", mn: "Танд зөвлөх нь" },
  cta: { en: "Start", mn: "Эхлэх" },
};

export default function RecommendedNextCard({ rec }: { rec: CourseRecommendation }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";

  return (
    <section
      className="card-edit p-5 flex flex-wrap items-center justify-between gap-4"
      style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
    >
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
      <Link href={rec.courseHref} className="btn btn-primary flex-shrink-0">
        {i18n.cta[L]}
        <ArrowRight className="ml-1 h-3.5 w-3.5" />
      </Link>
    </section>
  );
}
