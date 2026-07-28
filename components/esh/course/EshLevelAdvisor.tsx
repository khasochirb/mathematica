"use client";

// Readiness advisory for the ЭЕШ prep courses.
//
// The prep courses are pitched at a student already scoring ~650/800
// (lib/esh-course.ts, ESH_COURSE_READY_SCORE). A student projecting below
// that is better served building foundations in the General Math courses
// first — this component reads the student's real test history and says so,
// with concrete destinations from the exam-study-map, instead of letting
// them bounce off exam-level material.
//
// Three states, all advisory (never a lock):
//   - no tests yet   → suggest sitting one past paper to calibrate
//   - projected <650 → route to General Math, weakest topics first
//   - projected ≥650 → a one-line confirmation, then stay out of the way
//
// Chrome is Mongolian (hub chrome policy); course content itself is
// English-first for now.

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowRight, Compass } from "lucide-react";
import useESHProgress from "@/lib/use-esh-progress";
import { ESH_COURSE_READY_SCORE } from "@/lib/esh-course";
import { getStudyTarget } from "@/lib/exam-study-map";
import { TOPIC_LABELS } from "@/lib/esh-questions";

export default function EshLevelAdvisor() {
  const [mounted, setMounted] = useState(false);
  const progress = useESHProgress();
  useEffect(() => setMounted(true), []);
  if (!mounted) return null;

  // Same projection the analytics report uses: accuracy → the 400–800 scale.
  const projected =
    progress.totalTestsTaken > 0
      ? Math.min(800, Math.max(400, Math.round(progress.averageAccuracy * 8)))
      : null;

  if (projected === null) {
    return (
      <div className="card-edit p-4 mt-6 flex items-start gap-3" style={{ background: "var(--bg-1)" }}>
        <Compass className="w-4 h-4 shrink-0 mt-0.5" style={{ color: "var(--accent)" }} />
        <p className="text-[13px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
          Эдгээр курс ~{ESH_COURSE_READY_SCORE}+/800 оноотой сурагчид зориулагдсан. Түвшнээ мэдэхийн тулд
          эхлээд нэг жинхэнэ ЭЕШ тест бодоорой —{" "}
          <Link href="/practice/esh/test?type=previous" className="underline underline-offset-2" style={{ color: "var(--accent)" }}>
            тест сонгох
          </Link>
          .
        </p>
      </div>
    );
  }

  if (projected >= ESH_COURSE_READY_SCORE) {
    return (
      <p className="mono text-[11px] mt-6" style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}>
        Таны сүүлийн тестүүд ≈{projected}/800 — эдгээр курс яг таны түвшинд.
      </p>
    );
  }

  // Below the bar: name it honestly and route to foundations, weakest first.
  const targets = progress.weakTopics
    .slice(0, 3)
    .map((t) => ({ topic: t, target: getStudyTarget(t) }))
    .filter((x) => x.target !== null);

  return (
    <div
      className="card-edit p-5 mt-6"
      style={{
        background: "color-mix(in oklch, var(--warn) 6%, transparent)",
        borderColor: "color-mix(in oklch, var(--warn) 25%, transparent)",
      }}
    >
      <div className="flex items-start gap-3">
        <Compass className="w-5 h-5 shrink-0 mt-0.5" style={{ color: "var(--warn)" }} />
        <div className="flex-1">
          <div className="eyebrow mb-1" style={{ color: "var(--warn)" }}>
            Эхлэхээсээ өмнө
          </div>
          <p className="text-[13px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
            Таны сүүлийн тестүүд ≈{projected}/800 оноо руу чиглэж байна. Эдгээр бэлтгэл курс
            ~{ESH_COURSE_READY_SCORE}+ түвшинд зориулагдсан тул эхлээд Ерөнхий математикийн курсээр
            суурь тавихыг зөвлөж байна — тэндээс эргэж ирэхэд энд байгаа бүх зүйл хамаагүй хялбар
            санагдана.
          </p>
          {targets.length > 0 && (
            <div className="mt-3 space-y-1.5">
              {targets.map(({ topic, target }) => (
                <div key={topic} className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                  <span style={{ color: "var(--fg-1)" }}>{TOPIC_LABELS[topic] || topic}</span>
                  {": "}
                  <Link
                    href={target!.primary.href}
                    className="underline underline-offset-2"
                    style={{ color: "var(--accent)" }}
                  >
                    {target!.primary.label}
                  </Link>
                </div>
              ))}
            </div>
          )}
          <Link
            href="/math"
            className="mono text-[11px] uppercase mt-3 inline-flex items-center gap-1"
            style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
          >
            Ерөнхий математикийн курсууд
            <ArrowRight className="w-3 h-3" />
          </Link>
        </div>
      </div>
    </div>
  );
}
