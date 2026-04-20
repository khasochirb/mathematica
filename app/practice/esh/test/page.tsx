"use client";

import { useState, useEffect, useMemo } from "react";
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
import { getAllTestsCombined, type TestInfo } from "@/lib/esh-questions";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";
import PremiumBadge from "@/components/PremiumBadge";

export default function TestSelectionPage() {
  const router = useRouter();
  const { isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();
  const session = useTestSession();
  const [mounted, setMounted] = useState(false);
  const [showResumeModal, setShowResumeModal] = useState<string | null>(null);
  const [showStartModal, setShowStartModal] = useState<string | null>(null);

  useEffect(() => setMounted(true), []);

  // Free tests first, then locked premium. Within each group, source order preserved.
  const tests = useMemo<TestInfo[]>(() => {
    const all = getAllTestsCombined();
    return [...all.filter((t) => !t.isPremium), ...all.filter((t) => t.isPremium)];
  }, []);

  const lookupTest = (key: string) => tests.find((t) => t.key === key);

  const handleTestClick = (test: TestInfo) => {
    if (test.isPremium && !isSubscribed) {
      upgrade.open({
        source: "gated_legacy_tests",
        title: `${test.label} — Premium`,
        description:
          "Нэмэлт дадлага тестүүд нь Premium багцад багтсан. Premium эхлэхэд и-мэйлээр мэдэгдэнэ.",
      });
      return;
    }
    const active = session.getActiveSessionForTest(test.key);
    if (active) {
      setShowResumeModal(test.key);
    } else {
      setShowStartModal(test.key);
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

  const freeCount = tests.filter((t) => !t.isPremium).length;
  const premiumCount = tests.filter((t) => t.isPremium).length;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
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
            <div className="eyebrow mb-1.5">01 · Шалгалт</div>
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
              Дадлага шалгалт
            </h1>
            <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
              Тест сонгоод шалгалтын горимд бодоорой
            </p>
          </div>
          <div className="ml-auto text-right">
            <div className="eyebrow">НИЙТ</div>
            <div
              className="serif tabular mt-1"
              style={{ fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              {tests.length}
            </div>
            {!isSubscribed && premiumCount > 0 && (
              <div
                className="mono text-[10px] mt-1 tabular"
                style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                {freeCount} ҮНЭГҮЙ · {premiumCount} PREMIUM
              </div>
            )}
          </div>
        </div>

        {/* Test grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {tests.map((test) => {
            const locked = test.isPremium && !isSubscribed;
            const best = mounted && !locked ? session.getBestScore(test.key) : null;
            const latest =
              mounted && !locked ? session.getLatestSession(test.key) : undefined;
            const active =
              mounted && !locked
                ? session.getActiveSessionForTest(test.key)
                : undefined;
            const attemptCount =
              mounted && !locked ? session.getSessionsByTest(test.key).length : 0;

            return (
              <button
                key={test.key}
                onClick={() => handleTestClick(test)}
                className="card-edit p-5 text-left group relative"
                style={locked ? { opacity: 0.65 } : undefined}
              >
                <div className="flex items-start justify-between mb-4 gap-3">
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2 mb-1.5">
                      <div
                        className="eyebrow"
                        style={{ color: locked ? "var(--fg-3)" : "var(--accent)" }}
                      >
                        {test.key}
                      </div>
                      {locked && <PremiumBadge variant="inline" />}
                    </div>
                    <h3
                      className="serif"
                      style={{
                        fontWeight: 400,
                        fontSize: 22,
                        letterSpacing: "-0.02em",
                        color: "var(--fg)",
                        lineHeight: 1.1,
                      }}
                    >
                      {test.label}
                    </h3>
                    <div
                      className="flex items-center gap-2 mt-2 mono text-[11px]"
                      style={{ color: "var(--fg-3)" }}
                    >
                      <FileText className="w-3 h-3" />
                      <span className="tabular">{test.data.length} бодлого</span>
                      <span>·</span>
                      <Clock className="w-3 h-3" />
                      <span className="tabular">100 мин</span>
                    </div>
                  </div>
                  {locked ? (
                    <Lock className="w-5 h-5 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
                  ) : active ? (
                    <span className="badge-edit badge-warn flex-shrink-0">
                      Үргэлжлүүлэх
                    </span>
                  ) : (
                    <Play
                      className="w-5 h-5 flex-shrink-0 transition-colors"
                      style={{ color: "var(--fg-3)" }}
                    />
                  )}
                </div>

                {locked && (
                  <div
                    className="mt-4 pt-3 text-[12px]"
                    style={{ borderTop: "1px solid var(--line)", color: "var(--fg-2)" }}
                  >
                    Premium эхлэхэд нээгдэнэ
                  </div>
                )}

                {!locked && mounted && best !== null && (
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
                      {attemptCount} удаа бодсон
                    </span>
                    {latest?.completedAt && (
                      <span
                        className="mono tabular text-[11px] ml-auto"
                        style={{ color: "var(--fg-3)" }}
                      >
                        {new Date(latest.completedAt).toLocaleDateString("mn-MN")}
                      </span>
                    )}
                  </div>
                )}

                {!locked && mounted && best === null && (
                  <div
                    className="mt-4 pt-3 mono text-[11px]"
                    style={{ borderTop: "1px solid var(--line)", color: "var(--fg-3)" }}
                  >
                    Бодоогүй
                  </div>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Start confirmation modal */}
      {showStartModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "rgba(0,0,0,0.65)", backdropFilter: "blur(8px)" }}
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
                  {lookupTest(showStartModal)?.label}
                </h3>
              </div>
            </div>

            <div className="space-y-2 mb-6 text-[13px]" style={{ color: "var(--fg-1)" }}>
              <div className="flex items-center gap-2">
                <FileText className="w-3.5 h-3.5" style={{ color: "var(--fg-3)" }} />
                <span className="mono tabular">
                  {lookupTest(showStartModal)?.data.length} бодлого
                </span>
              </div>
              <div className="flex items-center gap-2">
                <Clock className="w-3.5 h-3.5" style={{ color: "var(--fg-3)" }} />
                <span className="mono tabular">100 минийн хугацаатай</span>
              </div>
              <div className="flex items-center gap-2">
                <AlertCircle className="w-3.5 h-3.5" style={{ color: "var(--fg-3)" }} />
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

      {/* Resume modal */}
      {showResumeModal && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "rgba(0,0,0,0.65)", backdropFilter: "blur(8px)" }}
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
                  {lookupTest(showResumeModal)?.label}
                </h3>
              </div>
            </div>

            <p className="text-[13px] mb-6" style={{ color: "var(--fg-1)" }}>
              Та өмнө нь энэ шалгалтыг эхлүүлсэн байна. Үргэлжлүүлэх үү эсвэл шинээр
              эхлэх үү?
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
