"use client";

import Link from "next/link";
import { ArrowRight, Layers, PencilLine } from "lucide-react";
import { useLang } from "@/lib/lang-context";
import type { BankWork } from "@/lib/use-bank-work";

// "Here is what you've put in." The problem bank's line on the dashboard.
//
// Counts only, and only things that went RIGHT: problems solved and problem
// types covered. No accuracy, no streak-at-risk, nothing that can drop. The
// bank is the one place on the platform where a wrong answer costs nothing,
// and this card is where that promise is visible — the number a student sees
// after a rough session is the same one they saw before it, plus whatever
// they got right.
//
// It sits under the ratings card because it answers the question that card
// provokes: "I practised — where did it go?"
const i18n = {
  eyebrow: { en: "Problem bank", mn: "Бодлогын сан" },
  solved: { en: "problems solved", mn: "бодлого бодсон" },
  types_one: { en: "problem type covered", mn: "төрлийн бодлого" },
  types_many: { en: "problem types covered", mn: "төрлийн бодлого" },
  most: { en: "Most work in", mn: "Хамгийн их ажилласан" },
  open: { en: "Open the bank", mn: "Бодлогын сан нээх" },
  note: {
    en: "Practice here only ever adds — a wrong answer never costs you anything.",
    mn: "Энд хийсэн дасгал зөвхөн нэмэгдэнэ — буруу хариулт юу ч хасахгүй.",
  },
};

export default function BankWorkCard({ work }: { work: BankWork }) {
  const { lang } = useLang();
  const t = (k: keyof typeof i18n) => i18n[k][lang === "mn" ? "mn" : "en"];

  return (
    <div className="card-edit p-5">
      <div className="flex items-start gap-4 flex-wrap">
        <div className="flex-1 min-w-[200px]">
          <div className="eyebrow mb-2">{t("eyebrow")}</div>
          <div className="flex items-baseline gap-2">
            <span
              className="serif tabular"
              style={{ fontSize: 34, lineHeight: 1, letterSpacing: "-0.03em", color: "var(--fg)" }}
            >
              {work.solvedProblems}
            </span>
            <span style={{ color: "var(--fg-1)", fontSize: 15 }}>{t("solved")}</span>
          </div>

          <div className="mt-2.5 flex items-center gap-2 flex-wrap text-[11px] mono" style={{ color: "var(--fg-3)" }}>
            <span
              className="inline-flex items-center gap-1 rounded-full px-2 py-0.5"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
            >
              <Layers className="h-3 w-3" />
              {work.solvedForms} {work.solvedForms === 1 ? t("types_one") : t("types_many")}
            </span>
            {work.topSubject && (
              <span
                className="rounded-full px-2 py-0.5"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
              >
                {t("most")}: {work.topSubject.title}
              </span>
            )}
          </div>

          <p className="mt-3 flex items-start gap-1.5 text-[12px]" style={{ color: "var(--fg-3)" }}>
            <PencilLine className="mt-[3px] h-3 w-3 flex-shrink-0" />
            <span>{t("note")}</span>
          </p>
        </div>

        <Link
          href="/math/problem-bank"
          className="btn btn-line inline-flex items-center gap-1.5 text-[13px] flex-shrink-0"
          style={{ textDecoration: "none" }}
        >
          {t("open")}
          <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  );
}
