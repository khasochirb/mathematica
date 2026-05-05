"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Play, Lock } from "lucide-react";
import { TOPICS } from "@/lib/esh-questions";
import topicsData from "@/data/learn/topics.json";
import ComingSoonBadge from "@/components/ComingSoonBadge";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";

export default function LearnPage() {
  const upgrade = useUpgradeModal();
  const { user, loading } = useAuth();
  const [mounted, setMounted] = useState(false);

  useEffect(() => setMounted(true), []);

  // Auth wall for anonymous users — full-page card with sign-in/sign-up CTAs.
  if (mounted && !loading && !user) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <Link
            href="/practice/esh"
            className="btn btn-ghost mb-8 inline-flex"
            style={{ padding: "8px 10px" }}
            aria-label="Back"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div
            className="card-edit p-8 text-center"
            style={{ background: "var(--bg-1)" }}
          >
            <div
              className="w-12 h-12 rounded-md flex items-center justify-center mx-auto mb-5"
              style={{
                background: "var(--accent-wash)",
                border: "1px solid var(--accent-line)",
                color: "var(--accent)",
              }}
            >
              <Lock className="w-5 h-5" />
            </div>
            <div className="eyebrow mb-2">БҮРТГҮҮЛСЭН ХЭРЭГЛЭГЧДЭД</div>
            <h1
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: 28,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
                lineHeight: 1.1,
              }}
            >
              Сэдвээр{" "}
              <em className="serif-italic" style={{ color: "var(--accent)" }}>
                суралцах
              </em>
            </h1>
            <p
              className="text-[14px] mt-4 mb-6"
              style={{ color: "var(--fg-2)" }}
            >
              Сэдэв бүрийн томьёо, зөвлөгөө, материалыг үзэхийн тулд бүртгүүлнэ
              үү. Бүртгүүлэх нь үнэгүй.
            </p>
            <div className="flex gap-2 justify-center">
              <Link
                href={`/sign-in?next=${encodeURIComponent("/practice/esh/learn")}`}
                className="btn btn-line"
              >
                Нэвтрэх
              </Link>
              <Link href="/sign-up" className="btn btn-primary">
                Бүртгүүлэх
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        {/* Header */}
        <div className="flex items-center gap-3 mb-6">
          <Link
            href="/practice/esh"
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">ЭЕШ · Суралцах</div>
        </div>

        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(40px, 6vw, 64px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.98,
            color: "var(--fg)",
          }}
        >
          Сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>суралцах</em>.
        </h1>
        <p className="serif mt-4 max-w-2xl" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
          Томьёо, зөвлөгөө — сэдэв тус бүрээр.
        </p>

        {/* Coming-soon disclosure — video lessons are the next layer on top of the current text content. */}
        <button
          type="button"
          onClick={() =>
            upgrade.open({
              source: "coming_soon_suraltsah",
              title: "Видео хичээл удахгүй",
              description:
                "Сэдэв тус бүрт зориулсан видео хичээл бэлдэж байна. Имэйлээ үлдээвэл эхэлмэгц мэдэгдэнэ.",
            })
          }
          className="mt-6 w-full sm:w-auto inline-flex items-center gap-3 rounded-md p-3 pr-4 transition-colors text-left"
          style={{
            background: "var(--bg-2)",
            border: "1px solid var(--line)",
          }}
        >
          <span
            className="w-8 h-8 rounded-md flex items-center justify-center shrink-0"
            style={{
              background: "var(--bg)",
              border: "1px solid var(--line)",
              color: "var(--fg-2)",
            }}
          >
            <Play className="w-3.5 h-3.5" />
          </span>
          <span className="flex-1 min-w-0">
            <span className="flex items-center gap-2">
              <ComingSoonBadge variant="inline" />
              <span
                className="mono text-[10px] uppercase"
                style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                Видео хичээл
              </span>
            </span>
            <span className="block text-[13px] mt-1" style={{ color: "var(--fg-1)" }}>
              Сэдэв тус бүрийн видео хичээл удахгүй. Имэйлээ үлдээх үү?
            </span>
          </span>
          <span
            className="mono text-[10px] uppercase shrink-0"
            style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
          >
            Мэдэгдэх →
          </span>
        </button>

        {/* Topic grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-10">
          {TOPICS.map((topic, i) => {
            const data = (topicsData as Record<string, { title: string; overview: string; formulas: unknown[]; tips: unknown[] }>)[topic.value];
            if (!data) return null;

            return (
              <Link
                key={topic.value}
                href={`/practice/esh/learn/${topic.value}`}
                className="card-edit p-5 group"
              >
                <div className="flex items-start justify-between mb-3">
                  <div className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                    {String(i + 1).padStart(2, "0")} · СЭДЭВ
                  </div>
                  <ArrowRight className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
                </div>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {data.title}
                </h3>
                <p className="text-[13px] mt-2 line-clamp-2" style={{ color: "var(--fg-2)" }}>
                  {data.overview}
                </p>
                <div className="flex items-center gap-4 mt-4">
                  <div className="flex items-baseline gap-1">
                    <span className="serif tabular" style={{ fontSize: 18, color: "var(--accent)", letterSpacing: "-0.02em" }}>
                      {data.formulas.length}
                    </span>
                    <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                      томьёо
                    </span>
                  </div>
                  <div className="flex items-baseline gap-1">
                    <span className="serif tabular" style={{ fontSize: 18, color: "var(--accent)", letterSpacing: "-0.02em" }}>
                      {data.tips.length}
                    </span>
                    <span className="mono text-[10px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>
                      зөвлөгөө
                    </span>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
