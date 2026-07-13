"use client";

import { Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { ArrowRight, BarChart3, Sparkles } from "lucide-react";
import BackButton from "@/components/BackButton";
import usePerformance from "@/lib/use-performance";
import { contextHref, contextLabel } from "@/lib/perf-context";
import { courseTotalLessons } from "@/lib/genmath-lessons";
import { useLang } from "@/lib/lang-context";

const i18n = {
  eyebrow: { en: "Progress", mn: "Прогресс" },
  stat_lessons: { en: "Lessons", mn: "Хичээл" },
  stat_checks: { en: "Lesson checks", mn: "Хичээлийн даалгавар" },
  stat_accuracy: { en: "Accuracy", mn: "Зөв хариулсан хувь" },
  units_eyebrow: { en: "By unit", mn: "Нэгжээр" },
  open_course: { en: "Open the course", mn: "Курс руу очих" },
  empty_h: { en: "No practice data yet.", mn: "Одоогоор мэдээлэл алга." },
  empty_p: {
    en: "Work through a lesson and its checks — your progress shows up here.",
    mn: "Хичээл үзэж даалгавраа бодмогц таны ахиц энд харагдана.",
  },
  not_found_h: { en: "Course not found.", mn: "Курс олдсонгүй." },
  not_found_p: {
    en: "Pick a course from the catalog to see its progress.",
    mn: "Прогрессоо харахын тулд каталогоос курс сонгоно уу.",
  },
  all_courses: { en: "All courses", mn: "Бүх курс" },
};

// Unit slugs read as titles: "probability-models" → "Probability models".
function humanizeSlug(slug: string): string {
  const s = slug.replace(/-/g, " ");
  return s.charAt(0).toUpperCase() + s.slice(1);
}

// The full report for a COURSE context (course:algebra-1, course:grade-6, …) —
// the destination behind the dashboard's "Details" link. Exam hubs have their
// own richer pages (/analytics, HubProgress); courses share this one, keyed by
// ?course=. Reachable from many places, so the back button is history-back.
function CourseProgress() {
  const params = useSearchParams();
  const slug = params.get("course") ?? "";
  const context = `course:${slug}`;
  const perf = usePerformance();
  const { lang } = useLang();
  const t = (key: keyof typeof i18n) => i18n[key][lang === "mn" ? "mn" : "en"];

  const courseHome = contextHref(context);
  if (!slug || !courseHome) {
    return (
      <Frame back="/math">
        <section className="card-edit p-8 mt-8 text-center">
          <p className="serif" style={{ fontSize: 22, color: "var(--fg)" }}>
            {t("not_found_h")}
          </p>
          <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
            {t("not_found_p")}
          </p>
          <Link href="/math" className="btn btn-primary mt-6 inline-flex">
            {t("all_courses")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
        </section>
      </Frame>
    );
  }

  const overall = perf.getOverallStats(context);
  const unitStats = perf.getTopicStats(context);
  const lessonsTotal = courseTotalLessons(context);
  const lessonsWorked = perf.getLessonsWorked(context);
  const hasData = overall.total > 0 || lessonsWorked > 0;

  const tiles: { lbl: string; val: string; suffix: string; accent?: boolean }[] = [
    ...(lessonsTotal && lessonsTotal > 0
      ? [{ lbl: t("stat_lessons"), val: `${lessonsWorked}`, suffix: ` / ${lessonsTotal}` }]
      : []),
    { lbl: t("stat_checks"), val: `${overall.total}`, suffix: "" },
    { lbl: t("stat_accuracy"), val: `${overall.accuracy}`, suffix: "%", accent: true },
  ];

  return (
    <Frame back={courseHome} eyebrow={`${contextLabel(context)} · ${t("eyebrow")}`}>
      <h1
        className="serif"
        style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
      >
        {contextLabel(context)}
      </h1>

      {!hasData ? (
        <section className="card-edit p-8 mt-8 text-center">
          <BarChart3 className="mx-auto h-8 w-8" style={{ color: "var(--fg-3)" }} />
          <p className="serif mt-4" style={{ fontSize: 20, color: "var(--fg)" }}>
            {t("empty_h")}
          </p>
          <p className="text-[13px] mt-2 mx-auto" style={{ color: "var(--fg-2)", maxWidth: "44ch" }}>
            {t("empty_p")}
          </p>
          <Link href={courseHome} className="btn btn-primary mt-6 inline-flex">
            {t("open_course")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
        </section>
      ) : (
        <>
          <section
            className="grid gap-4 mt-8"
            style={{ gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))" }}
          >
            {tiles.map((tile) => (
              <div key={tile.lbl} className="card-edit p-5">
                <div className="eyebrow">{tile.lbl}</div>
                <div
                  className="serif tabular mt-2"
                  style={{
                    fontSize: 36,
                    letterSpacing: "-0.03em",
                    color: tile.accent ? "var(--accent)" : "var(--fg)",
                  }}
                >
                  {tile.val}
                  {tile.suffix && (
                    <span className="mono ml-1" style={{ fontSize: 15, color: "var(--fg-3)" }}>
                      {tile.suffix}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </section>

          {unitStats.length > 0 && (
            <section className="card-edit p-6 mt-5">
              <div className="flex items-center gap-2 mb-4">
                <Sparkles className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                <div className="eyebrow">{t("units_eyebrow")}</div>
              </div>
              <div className="space-y-3">
                {unitStats.map((u) => (
                  <div key={u.topic}>
                    <div className="flex items-baseline justify-between gap-2 mb-1.5 text-sm">
                      <Link
                        href={`${courseHome}/${u.topic}`}
                        className="underline underline-offset-2 decoration-[color:var(--line)]"
                        style={{ color: "var(--fg-1)" }}
                      >
                        {humanizeSlug(u.topic)}
                      </Link>
                      <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                        {u.correct}/{u.total} · {u.accuracy}%
                      </span>
                    </div>
                    <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                      <div
                        className="h-full rounded-full"
                        style={{
                          width: `${u.accuracy}%`,
                          background:
                            u.accuracy >= 80 ? "var(--accent)" : u.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                        }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}

          <div className="mt-6">
            <Link href={courseHome} className="btn btn-line inline-flex">
              {t("open_course")}
              <ArrowRight className="ml-1 h-3.5 w-3.5" />
            </Link>
          </div>
        </>
      )}
    </Frame>
  );
}

function Frame({
  back,
  eyebrow,
  children,
}: {
  back: string;
  eyebrow?: string;
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <BackButton fallback={back} className="gm-press p-2 rounded-md" />
          {eyebrow && <div className="eyebrow flex-1">{eyebrow}</div>}
        </div>
        {children}
      </div>
    </div>
  );
}

export default function CourseProgressPage() {
  // useSearchParams needs a Suspense boundary for static prerender.
  return (
    <Suspense fallback={<div className="min-h-screen pt-20" style={{ background: "var(--bg)" }} />}>
      <CourseProgress />
    </Suspense>
  );
}
