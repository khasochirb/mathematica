"use client";

// The 2K-style attribute card: one overall score, eight attribute rows.
// Strictly presentational — all math lives in lib/ratings.ts.

import { ATTRIBUTES, BAND_LABELS, UNRATED_LABEL, type Band, type RatingsProfile } from "@/lib/ratings";
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
    en: "Rated skills run 40–100 — everyone starts at 40, and 100 means mastery, earned through lessons, unit tests, the problem bank, and exams. \"—\" means not rated yet: take a test or a placement to rate it.",
    mn: "Үнэлгээ 40–100 хооронд — хүн бүр 40-өөс эхэлнэ, 100 гэдэг нь хичээл, нэгжийн тест, бодлогын сан, шалгалтаар бүрэн эзэмшснийг илтгэнэ. \"—\" гэдэг нь хараахан үнэлэгдээгүй — тест эсвэл түвшин тогтоох тест өгч үнэлүүлээрэй.",
  },
};

export default function RatingsPanel({ profile }: { profile: RatingsProfile }) {
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";
  const t = (k: keyof typeof i18n) => i18n[k][L];

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
          return (
            <div key={info.key}>
              <div className="flex items-baseline justify-between gap-2">
                <span className="text-[13px]" style={{ color: "var(--fg)" }}>
                  {info[L]}
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
            </div>
          );
        })}
      </div>
    </section>
  );
}
