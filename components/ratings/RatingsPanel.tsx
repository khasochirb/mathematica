"use client";

// The 2K-style attribute card: one overall score, eight attribute rows.
// Each rated row expands into a "why this number" breakdown — the evidence
// streams, the active caps, and the ranked next steps — so the strict score
// is never a black box. Strictly presentational — all math lives in
// lib/ratings.ts.

import { useState } from "react";
import Link from "next/link";
import { ChevronDown, Target } from "lucide-react";
import {
  ATTRIBUTES,
  BAND_LABELS,
  UNRATED_LABEL,
  type AttributeRating,
  type Band,
  type EvidenceStream,
  type RatingsProfile,
} from "@/lib/ratings";
import { useLang } from "@/lib/lang-context";

const BAND_COLOR: Record<Band, string> = {
  beginner: "var(--danger)",
  developing: "var(--warn)",
  strong: "var(--accent)",
  mastery: "var(--accent)",
};

const i18n = {
  eyebrow: { en: "Your ratings", mn: "Таны үнэлгээ" },
  overall: { en: "Overall", mn: "Ерөнхий оноо" },
  provisional: { en: "provisional", mn: "урьдчилсан" },
  units: { en: "units", mn: "нэгж" },
  hint: {
    en: "Rated skills run 40–100 and count only when accurate: it takes about five full tests, or one placement test, to rate a skill (\"—\" until then). Harder exams count for more — a 100% on ЭШ or IB outranks a 100% on the easier SAT. Tap a rated skill to see exactly why it's the number it is.",
    mn: "Үнэлгээ 40–100 хооронд, зөвхөн үнэн зөв үед л тооцогдоно: чадварыг үнэлэхэд ойролцоогоор таван бүтэн тест эсвэл нэг түвшин тогтоох тест шаардлагатай (түүнээс өмнө \"—\"). Хүнд шалгалт илүү үнэ цэнэтэй — ЭШ эсвэл IB-д 100% авах нь илүү хялбар SAT-д 100% авахаас дээгүүр. Үнэлгээтэй чадвар дээр дарж яагаад ийм оноотойгоо хараарай.",
  },
  whyTitle: { en: "Why this number", mn: "Яагаад ийм оноотой вэ" },
  toRaise: { en: "To raise it", mn: "Өсгөхийн тулд" },
  pts: { en: "pts", mn: "оноо" },
  evExam: { en: "Mock exams", mn: "Бүтэн шалгалтууд" },
  evPlacement: { en: "Placement test", mn: "Түвшин тогтоох тест" },
  evCourse: { en: "Course work", mn: "Хичээлийн ажил" },
  evPractice: { en: "Bank practice", mn: "Бодлогын сангийн дасгал" },
  evCredit: { en: "credit", mn: "оноо" },
  evPracticeNote: {
    en: "Bank practice can raise this number but never settles it — a test or a placement does that.",
    mn: "Бодлогын сангийн дасгал энэ оноог өсгөж чадна ч тогтоохгүй — үүнийг тест эсвэл түвшин тогтоох шалгалт хийнэ.",
  },
  questions: { en: "questions", mn: "асуулт" },
  accuracy: { en: "accuracy", mn: "оновчтой" },
  arguesFor: { en: "argues", mn: "заана" },
  satCeiling: {
    en: "Your exam evidence is mostly SAT — a perfect SAT alone tops out at 80. ЭШ and IB mocks can take this to 100.",
    mn: "Таны шалгалтын нотолгоо голдуу SAT — SAT дангаараа дээд тал нь 80. ЭШ болон IB-ийн шалгалтууд 100 хүртэл өсгөнө.",
  },
  placementCeiling: {
    en: "A placement rates up to 90 — real mocks and unit tests go beyond.",
    mn: "Түвшин тогтоох тест дээд тал нь 90 — жинхэнэ шалгалт болон нэгжийн тестүүд түүнээс дээш гаргана.",
  },
  courseCap: {
    en: "Course work alone caps at 84 — prove it on a real mock to go higher.",
    mn: "Дан хичээлийн ажил дээд тал нь 84 — илүү өндөрт гарахын тулд жинхэнэ шалгалтаар баталгаажуулаарай.",
  },
  confidence: {
    en: (conf: number, argued: number) =>
      `Evidence confidence ${conf}% — the score sits ${conf}% of the way from 40 toward what your evidence argues (≈${argued}). More evidence closes the gap.`,
    mn: (conf: number, argued: number) =>
      `Нотолгооны итгэл ${conf}% — оноо 40-өөс таны нотолгооны заасан түвшин (≈${argued}) хүртэлх замын ${conf}%-д байна. Нотолгоо нэмэгдэх тусам ойртоно.`,
  },
};

export default function RatingsPanel({ profile }: { profile: RatingsProfile }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";
  const t = (k: Exclude<keyof typeof i18n, "confidence">) => i18n[k][L];
  const [open, setOpen] = useState<string | null>(null);

  return (
    <section className="card-edit p-5 md:p-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <div className="eyebrow">{t("eyebrow")}</div>
          <p className="text-[12px] mt-1 max-w-[46ch]" style={{ color: "var(--fg-3)" }}>
            {t("hint")}
          </p>
        </div>
        {/* Overall badge */}
        <div
          className="flex flex-col items-center justify-center rounded-md px-5 py-3"
          style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}
        >
          <span
            className="serif tabular"
            style={{ fontWeight: 400, fontSize: 40, lineHeight: 1, color: "var(--accent)" }}
          >
            {profile.overall}
          </span>
          <span
            className="mono text-[10px] uppercase mt-1"
            style={{ color: "var(--fg-2)", letterSpacing: "0.08em" }}
          >
            {t("overall")}
          </span>
        </div>
      </div>

      <div className="mt-5 grid gap-x-8 gap-y-3 sm:grid-cols-2">
        {ATTRIBUTES.map((info) => {
          const a = profile.attributes.find((x) => x.key === info.key)!;
          const color = a.rated ? BAND_COLOR[a.band] : "var(--fg-3)";
          const isOpen = open === info.key;
          return (
            <div key={info.key} className={isOpen ? "sm:col-span-2" : undefined}>
              <button
                type="button"
                className="w-full text-left"
                onClick={() => setOpen(isOpen ? null : info.key)}
                disabled={!a.rated}
                aria-expanded={isOpen}
                style={{ cursor: a.rated ? "pointer" : "default" }}
              >
                <div className="flex items-baseline justify-between gap-2">
                  <span className="text-[13px] inline-flex items-center gap-1" style={{ color: "var(--fg)" }}>
                    {info[L]}
                    {a.rated && (
                      <ChevronDown
                        className="h-3 w-3 transition-transform"
                        style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
                      />
                    )}
                  </span>
                  <span className="mono tabular text-[13px]" style={{ color }}>
                    {a.rated ? a.score : "—"}
                    {a.rated && a.provisional && (
                      <span className="ml-1 text-[10px]" style={{ color: "var(--fg-3)" }}>
                        ({t("provisional")})
                      </span>
                    )}
                  </span>
                </div>
                <div
                  className="h-[5px] rounded-full overflow-hidden mt-1"
                  style={{ background: "var(--bg-2)" }}
                >
                  {a.rated && (
                    <div
                      className="h-full rounded-full"
                      style={{ width: `${a.score}%`, background: color }}
                    />
                  )}
                </div>
                <div className="flex items-center justify-between mt-0.5">
                  <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                    {a.rated ? BAND_LABELS[a.band][L] : UNRATED_LABEL[L]}
                  </span>
                  <span className="mono tabular text-[10px]" style={{ color: "var(--fg-3)" }}>
                    {a.unitsTouched}/{a.unitsTotal} {t("units")}
                  </span>
                </div>
              </button>
              {isOpen && a.rated && <AttributeExplainer a={a} L={L} />}
            </div>
          );
        })}
      </div>
    </section>
  );
}

// The transparent breakdown: each evidence stream in plain words, the caps
// that are biting, the confidence pull, then the ranked "+N" next steps.
function AttributeExplainer({ a, L }: { a: AttributeRating; L: "en" | "mn" }) {
  const t = (k: Exclude<keyof typeof i18n, "confidence">) => i18n[k][L];
  const ev = a.evidence;
  const pct = (x: number) => Math.round(100 * x);
  const confPct = pct(ev.combinedConf);
  const argued = Math.round(ev.perfBlend);
  const satHeavy = ev.streams.some((s) => s.kind === "exam") && ev.examDifficulty < 0.95;
  const hasPlacement = ev.streams.some((s) => s.kind === "placement");
  const gainSteps = a.improvements.filter((s) => (s.delta ?? 0) > 0).slice(0, 3);

  const hasPractice = ev.streams.some((s) => s.kind === "practice");

  const streamLabel = (kind: EvidenceStream["kind"]) =>
    kind === "exam"
      ? t("evExam")
      : kind === "placement"
        ? t("evPlacement")
        : kind === "practice"
          ? t("evPractice")
          : t("evCourse");

  return (
    <div
      className="mt-2 rounded-md p-3"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      <div className="mono text-[10px] uppercase mb-2" style={{ color: "var(--fg-2)", letterSpacing: "0.08em" }}>
        {t("whyTitle")}
      </div>
      <ul className="space-y-1.5">
        {ev.streams.map((s) => (
          <li key={s.kind} className="flex items-baseline justify-between gap-3 text-[12px]">
            <span style={{ color: "var(--fg-1)" }}>
              {streamLabel(s.kind)}
              {" — "}
              {s.kind === "course"
                ? `${a.unitsTouched}/${a.unitsTotal} ${i18n.units[L]}`
                : s.kind === "practice"
                  ? `${Math.round(s.n)} ${t("questions")} · ${pct(s.acc)}% ${t("evCredit")}`
                  : `${pct(s.acc)}% ${t("accuracy")} · ~${Math.round(s.n)} ${t("questions")}`}
            </span>
            <span className="mono tabular text-[11px] shrink-0" style={{ color: "var(--fg-3)" }}>
              {t("arguesFor")} {Math.round(s.perf)}/100
            </span>
          </li>
        ))}
      </ul>
      {(satHeavy || hasPlacement || ev.capNoExam) && (
        <ul className="mt-2 space-y-1">
          {satHeavy && (
            <li className="text-[11px]" style={{ color: "var(--fg-2)" }}>
              {t("satCeiling")}
            </li>
          )}
          {hasPlacement && (
            <li className="text-[11px]" style={{ color: "var(--fg-2)" }}>
              {t("placementCeiling")}
            </li>
          )}
          {ev.capNoExam && (
            <li className="text-[11px]" style={{ color: "var(--fg-2)" }}>
              {t("courseCap")}
            </li>
          )}
        </ul>
      )}
      {confPct < 100 && (
        <p className="text-[11px] mt-2" style={{ color: "var(--fg-3)" }}>
          {i18n.confidence[L](confPct, argued)}
        </p>
      )}

      {gainSteps.length > 0 && (
        <div className="mt-3 pt-2" style={{ borderTop: "1px solid var(--line)" }}>
          <div className="mono text-[10px] uppercase mb-1.5" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
            {t("toRaise")}
          </div>
          <ul className="space-y-1">
            {gainSteps.map((s) => (
              <li key={`${s.kind}:${s.unitSlug ?? s.href}`}>
                <Link
                  href={s.href}
                  className="flex items-center gap-2 text-[12px]"
                  style={{ color: "var(--fg-1)", textDecoration: "none" }}
                >
                  <Target className="h-3 w-3 flex-shrink-0" style={{ color: "var(--accent)" }} />
                  <span className="flex-1 min-w-0">{L === "mn" ? s.labelMn : s.labelEn}</span>
                  <span className="mono tabular text-[11px] flex-shrink-0" style={{ color: "var(--accent)" }}>
                    +{s.delta} {t("pts")}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
