"use client";

// In-course personalization, from the ratings profile: where should THIS
// student work in THIS course? Renders nothing until the student has any
// rating evidence for the course, so fresh visitors see the plain spine.
//
// Three pieces, all derived in lib/ratings.ts (recommendedUnits):
//   - a skip-ahead banner when the leading units are already solid
//   - a pinned "start here" unit with the score that justifies it
//   - a per-unit rating strip + "take the unit test" prompts for units that
//     look good but are unproven.

import Link from "next/link";
import { ArrowRight, Pin } from "lucide-react";
import useRatings from "@/lib/use-ratings";
import { recommendedUnits, type Band, type UnitRating } from "@/lib/ratings";
import { contextHref } from "@/lib/perf-context";
import { useLang } from "@/lib/lang-context";

const BAND_COLOR: Record<Band, string> = {
  beginner: "var(--danger)",
  developing: "var(--warn)",
  strong: "var(--accent)",
  mastery: "var(--accent)",
};

const i18n = {
  eyebrow: { en: "Your plan for this course", mn: "Таны энэ курсын төлөвлөгөө" },
  skip: {
    en: (n: number) => `Your first ${n === 2 ? "unit is" : `${n - 1} units are`} already solid — you can start at Unit ${n}.`,
    mn: (n: number) => `Эхний ${n - 1} нэгжээ сайн эзэмшсэн байна — та ${n}-р нэгжээс эхлэж болно.`,
  },
  startHere: { en: "Start here", mn: "Эндээс эхлээрэй" },
  startWhy: {
    en: (score: number) => `Your rating on this unit is ${score} — the first not-yet-solid unit in the course order.`,
    mn: (score: number) => `Энэ нэгж дээрх таны үнэлгээ ${score} — дарааллын дагуу бүрэн эзэмшээгүй эхний нэгж.`,
  },
  weakPins: { en: "Focus units", mn: "Анхаарах нэгжүүд" },
  needsTest: {
    en: "Looks solid — take the unit test to prove it:",
    mn: "Сайн харагдаж байна — нэгжийн тестээ өгч баталгаажуулаарай:",
  },
  unitRatings: { en: "Your unit ratings", mn: "Нэгж тус бүрийн үнэлгээ" },
  open: { en: "Open", mn: "Нээх" },
};

export default function CoursePersonalization({ context }: { context: string }) {
  const { profile } = useRatings();
  const { lang } = useLang();
  const L = lang === "mn" ? "mn" : "en";

  const mine = profile.units.filter((u) => u.context === context);
  const touched = mine.some((u) => u.touched);
  if (!touched) return null;

  const rec = recommendedUnits(profile, context);
  const baseHref = contextHref(context) ?? `/math/${context.slice("course:".length)}`;
  const unitHref = (u: UnitRating) => `${baseHref}/${u.slug}`;

  return (
    <section className="mb-8 space-y-3">
      <div className="eyebrow">{i18n.eyebrow[L]}</div>

      {rec.canStartAtUnit !== null && (
        <div
          className="card-edit p-4 text-[13px]"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)", color: "var(--fg-1)" }}
        >
          {i18n.skip[L](rec.canStartAtUnit)}
        </div>
      )}

      {rec.startHere && (
        <Link
          href={unitHref(rec.startHere)}
          className="card-edit p-4 flex items-center gap-3 transition-colors"
          style={{ textDecoration: "none", borderColor: "var(--accent-line)" }}
        >
          <Pin className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <span className="flex-1 min-w-0">
            <span className="mono text-[10px] uppercase block" style={{ color: "var(--accent)", letterSpacing: "0.08em" }}>
              {i18n.startHere[L]} · {String(rec.startHere.index).padStart(2, "0")}
            </span>
            <span className="serif block mt-0.5" style={{ fontWeight: 400, fontSize: 17, color: "var(--fg)" }}>
              {rec.startHere.title}
            </span>
            {rec.startHere.touched && (
              <span className="block mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
                {i18n.startWhy[L](rec.startHere.score)}
              </span>
            )}
          </span>
          <span className="mono text-[10px] uppercase flex-shrink-0 inline-flex items-center gap-1" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>
            {i18n.open[L]}
            <ArrowRight className="h-3 w-3" />
          </span>
        </Link>
      )}

      {/* Per-unit rating strip — number, score, band color. */}
      <div className="card-edit p-4">
        <div className="mono text-[10px] uppercase mb-2" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          {i18n.unitRatings[L]}
        </div>
        <div className="flex flex-wrap gap-1.5">
          {mine
            .sort((a, b) => a.index - b.index)
            .map((u) => (
              <Link
                key={u.slug}
                href={unitHref(u)}
                title={u.title}
                className="mono tabular text-[11px] rounded px-2 py-1"
                style={{
                  textDecoration: "none",
                  background: "var(--bg-2)",
                  border: "1px solid var(--line)",
                  color: "var(--fg-2)",
                }}
              >
                {String(u.index).padStart(2, "0")}{" "}
                <span style={{ color: u.touched ? BAND_COLOR[u.band] : "var(--fg-3)" }}>
                  {u.touched ? u.score : "—"}
                </span>
              </Link>
            ))}
        </div>
        {rec.needsUnitTest.length > 0 && (
          <p className="text-[12px] mt-3" style={{ color: "var(--fg-2)" }}>
            {i18n.needsTest[L]}{" "}
            {rec.needsUnitTest.map((u, i) => (
              <span key={u.slug}>
                {i > 0 && ", "}
                <Link
                  href={`${unitHref(u)}/test`}
                  className="underline underline-offset-2"
                  style={{ color: "var(--accent)" }}
                >
                  {u.title}
                </Link>
              </span>
            ))}
          </p>
        )}
      </div>
    </section>
  );
}
