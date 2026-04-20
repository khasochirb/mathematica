"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  ArrowLeft,
  Clock,
  FileText,
  Play,
  RotateCcw,
  AlertCircle,
  Lock,
} from "lucide-react";
import { getPreviousYearTests } from "@/lib/esh-questions";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";

export default function PreviousYearsPage() {
  const router = useRouter();
  const tests = getPreviousYearTests();
  const session = useTestSession();
  const { user, loading } = useAuth();
  const [mounted, setMounted] = useState(false);
  const [showResumeModal, setShowResumeModal] = useState<string | null>(null);
  const [showStartModal, setShowStartModal] = useState<string | null>(null);

  useEffect(() => setMounted(true), []);

  const handleTestClick = (testKey: string) => {
    const active = session.getActiveSessionForTest(testKey);
    if (active) {
      setShowResumeModal(testKey);
    } else {
      setShowStartModal(testKey);
    }
  };

  const handleStart = (testKey: string) => {
    const existing = session.getActiveSessionForTest(testKey);
    if (existing) session.abandonSession(existing.id);

    const id = session.startSession(testKey);
    router.push(`/practice/esh/test/${testKey.toLowerCase()}?session=${id}`);
  };

  const handleResume = (testKey: string) => {
    const active = session.getActiveSessionForTest(testKey);
    if (active) {
      router.push(
        `/practice/esh/test/${testKey.toLowerCase()}?session=${active.id}`,
      );
    }
  };

  const scoreColor = (n: number) =>
    n >= 80 ? "var(--accent)" : n >= 50 ? "var(--warn)" : "var(--danger)";

  const grouped = tests.reduce<Record<string, typeof tests>>((acc, t) => {
    const year = t.key.slice(0, 4);
    (acc[year] ||= []).push(t);
    return acc;
  }, {});

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
            <div className="eyebrow mb-2">ҮНЭГҮЙ · НЭВТЭРСЭН ХЭРЭГЛЭГЧДЭД</div>
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
              Өмнөх жилийн{" "}
              <em className="serif-italic" style={{ color: "var(--accent)" }}>
                бодит шалгалтууд
              </em>
            </h1>
            <p
              className="text-[14px] mt-4 mb-6"
              style={{ color: "var(--fg-2)" }}
            >
              2021–2025 оны ЭЕШ-ийн бодит даалгавруудыг бүтэн 4 хувилбараар нь
              үзэхийн тулд нэвтэрнэ үү. Бүртгүүлэх нь үнэгүй.
            </p>
            <div className="flex gap-2 justify-center">
              <Link href="/sign-in" className="btn btn-line">
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
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div
          className="flex items-end gap-4 mb-10 pb-6"
          style={{ borderBottom: "1px solid var(--line)" }}
        >
          <Link
            href="/practice/esh"
            className="btn btn-ghost"
            style={{ padding: "8px 10px" }}
            aria-label="Back"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <div className="eyebrow mb-1.5">05 · ӨМНӨХ ЖИЛИЙН ШАЛГАЛТ</div>
            <h1
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: "clamp(32px, 4vw, 44px)",
                letterSpacing: "-0.03em",
                lineHeight: 1,
                color: "var(--fg)",
              }}
            >
              Өмнөх жилийн{" "}
              <em className="serif-italic">бодит шалгалтууд</em>
            </h1>
            <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
              2021–2025 оны ЭЕШ-ийн дөрвөн хувилбар тус бүр · бүх хэрэглэгчид
              үнэгүй
            </p>
          </div>
          <div className="ml-auto text-right">
            <div className="eyebrow">НИЙТ</div>
            <div
              className="serif tabular mt-1"
              style={{
                fontSize: 32,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
              }}
            >
              {tests.length}
            </div>
          </div>
        </div>

        {Object.entries(grouped)
          .sort(([a], [b]) => Number(b) - Number(a))
          .map(([year, list]) => (
            <div key={year} className="mb-10">
              <div className="flex items-baseline gap-3 mb-4">
                <span
                  className="serif tabular"
                  style={{
                    fontSize: 24,
                    letterSpacing: "-0.02em",
                    color: "var(--fg)",
                  }}
                >
                  {year}
                </span>
                <span
                  className="mono text-[11px]"
                  style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
                >
                  {list.length} ХУВИЛБАР · {list[0].data.length} БОДЛОГО ТУС БҮРТ
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                {list.map((test) => {
                  const best = mounted ? session.getBestScore(test.key) : null;
                  const latest = mounted
                    ? session.getLatestSession(test.key)
                    : undefined;
                  const active = mounted
                    ? session.getActiveSessionForTest(test.key)
                    : undefined;
                  const attemptCount = mounted
                    ? session.getSessionsByTest(test.key).length
                    : 0;
                  const variantLabel = test.label.split("·")[1]?.trim() || test.key;

                  return (
                    <button
                      key={test.key}
                      onClick={() => handleTestClick(test.key)}
                      className="card-edit p-5 text-left group"
                    >
                      <div className="flex items-start justify-between mb-4">
                        <div>
                          <div
                            className="eyebrow mb-1.5"
                            style={{ color: "var(--accent)" }}
                          >
                            {test.key}
                          </div>
                          <h3
                            className="serif"
                            style={{
                              fontWeight: 400,
                              fontSize: 20,
                              letterSpacing: "-0.02em",
                              color: "var(--fg)",
                              lineHeight: 1.1,
                            }}
                          >
                            {variantLabel}
                          </h3>
                          <div
                            className="flex items-center gap-2 mt-2 mono text-[11px]"
                            style={{ color: "var(--fg-3)" }}
                          >
                            <FileText className="w-3 h-3" />
                            <span className="tabular">
                              {test.data.length} бодлого
                            </span>
                            <span>·</span>
                            <Clock className="w-3 h-3" />
                            <span className="tabular">100 мин</span>
                          </div>
                        </div>
                        {active ? (
                          <span className="badge-edit badge-warn">
                            Үргэлжлүүлэх
                          </span>
                        ) : (
                          <Play
                            className="w-5 h-5 transition-colors"
                            style={{ color: "var(--fg-3)" }}
                          />
                        )}
                      </div>

                      {mounted && best !== null && (
                        <div
                          className="flex items-center gap-3 mt-4 pt-3"
                          style={{ borderTop: "1px solid var(--line)" }}
                        >
                          <span
                            className="serif tabular"
                            style={{
                              fontSize: 20,
                              letterSpacing: "-0.01em",
                              color: scoreColor(best),
                            }}
                          >
                            {best}%
                          </span>
                          <span
                            className="mono tabular text-[11px]"
                            style={{ color: "var(--fg-3)" }}
                          >
                            {attemptCount} удаа
                          </span>
                          {latest?.completedAt && (
                            <span
                              className="mono tabular text-[11px] ml-auto"
                              style={{ color: "var(--fg-3)" }}
                            >
                              {new Date(latest.completedAt).toLocaleDateString(
                                "mn-MN",
                              )}
                            </span>
                          )}
                        </div>
                      )}

                      {mounted && best === null && (
                        <div
                          className="mt-4 pt-3 mono text-[11px]"
                          style={{
                            borderTop: "1px solid var(--line)",
                            color: "var(--fg-3)",
                          }}
                        >
                          Бодоогүй
                        </div>
                      )}
                    </button>
                  );
                })}
              </div>
            </div>
          ))}
      </div>

      {showStartModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{
            background: "rgba(0,0,0,0.65)",
            backdropFilter: "blur(8px)",
          }}
        >
          <div className="card-edit p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-5">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{
                  background: "var(--accent-wash)",
                  border: "1px solid var(--accent-line)",
                  color: "var(--accent)",
                }}
              >
                <Play className="w-4 h-4" />
              </div>
              <div>
                <div className="eyebrow">Шалгалт эхлүүлэх</div>
                <h3
                  className="serif mt-0.5"
                  style={{
                    fontWeight: 400,
                    fontSize: 20,
                    letterSpacing: "-0.02em",
                    color: "var(--fg)",
                  }}
                >
                  {tests.find((t) => t.key === showStartModal)?.label}
                </h3>
              </div>
            </div>

            <div
              className="space-y-2 mb-6 text-[13px]"
              style={{ color: "var(--fg-1)" }}
            >
              <div className="flex items-center gap-2">
                <FileText
                  className="w-3.5 h-3.5"
                  style={{ color: "var(--fg-3)" }}
                />
                <span className="mono tabular">
                  {tests.find((t) => t.key === showStartModal)?.data.length}{" "}
                  бодлого
                </span>
              </div>
              <div className="flex items-center gap-2">
                <Clock
                  className="w-3.5 h-3.5"
                  style={{ color: "var(--fg-3)" }}
                />
                <span className="mono tabular">100 минийн хугацаатай</span>
              </div>
              <div className="flex items-center gap-2">
                <AlertCircle
                  className="w-3.5 h-3.5"
                  style={{ color: "var(--fg-3)" }}
                />
                <span>Хариулт шалгалт дуусмагц харагдана</span>
              </div>
            </div>

            <div className="flex gap-2">
              <button
                onClick={() => setShowStartModal(null)}
                className="btn btn-line flex-1"
              >
                Буцах
              </button>
              <button
                onClick={() => {
                  handleStart(showStartModal);
                  setShowStartModal(null);
                }}
                className="btn btn-primary flex-1"
              >
                Эхлэх
              </button>
            </div>
          </div>
        </div>
      )}

      {showResumeModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{
            background: "rgba(0,0,0,0.65)",
            backdropFilter: "blur(8px)",
          }}
        >
          <div className="card-edit p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-4">
              <div
                className="w-10 h-10 rounded-md flex items-center justify-center"
                style={{
                  background: "rgba(245, 158, 11, 0.10)",
                  border: "1px solid rgba(245, 158, 11, 0.32)",
                  color: "var(--warn)",
                }}
              >
                <RotateCcw className="w-4 h-4" />
              </div>
              <div>
                <div className="eyebrow">Дуусаагүй шалгалт</div>
                <h3
                  className="serif mt-0.5"
                  style={{
                    fontWeight: 400,
                    fontSize: 20,
                    letterSpacing: "-0.02em",
                    color: "var(--fg)",
                  }}
                >
                  {tests.find((t) => t.key === showResumeModal)?.label}
                </h3>
              </div>
            </div>

            <p
              className="text-[13px] mb-6"
              style={{ color: "var(--fg-1)" }}
            >
              Та өмнө нь энэ шалгалтыг эхлүүлсэн байна. Үргэлжлүүлэх үү эсвэл
              шинээр эхлэх үү?
            </p>

            <div className="flex gap-2">
              <button
                onClick={() => {
                  handleStart(showResumeModal);
                  setShowResumeModal(null);
                }}
                className="btn btn-line flex-1"
              >
                Шинээр эхлэх
              </button>
              <button
                onClick={() => {
                  handleResume(showResumeModal);
                  setShowResumeModal(null);
                }}
                className="btn btn-primary flex-1"
              >
                Үргэлжлүүлэх
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
