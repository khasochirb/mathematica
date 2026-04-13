"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import {
  ArrowLeft,
  Clock,
  FileText,
  Trophy,
  Play,
  RotateCcw,
  AlertCircle,
} from "lucide-react";
import { getAllTests } from "@/lib/esh-questions";
import useTestSession from "@/lib/use-test-session";

export default function TestSelectionPage() {
  const router = useRouter();
  const tests = getAllTests();
  const session = useTestSession();
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
    // Abandon any existing active session for this test
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

  return (
    <div className="min-h-screen bg-surface-900 pt-20 relative">
      <div className="absolute inset-0 bg-grid opacity-30" />
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <Link
            href="/practice/esh"
            className="p-2 rounded-xl bg-white/[0.05] border border-white/[0.08] text-gray-400 hover:text-white hover:bg-white/[0.1] transition-colors"
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              Дадлага шалгалт
            </h1>
            <p className="text-sm text-gray-500">
              Тест сонгоод шалгалтын горимд бодоорой
            </p>
          </div>
        </div>

        {/* Test grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {tests.map((test) => {
            const best = mounted ? session.getBestScore(test.key) : null;
            const latest = mounted ? session.getLatestSession(test.key) : undefined;
            const active = mounted
              ? session.getActiveSessionForTest(test.key)
              : undefined;
            const attemptCount = mounted
              ? session.getSessionsByTest(test.key).length
              : 0;

            return (
              <button
                key={test.key}
                onClick={() => handleTestClick(test.key)}
                className="card-glass p-5 text-left hover:border-primary-400/30 hover:bg-white/[0.03] transition-all group"
              >
                <div className="flex items-start justify-between mb-3">
                  <div>
                    <h3 className="font-display font-bold text-white group-hover:text-primary-300 transition-colors">
                      {test.label}
                    </h3>
                    <div className="flex items-center gap-2 mt-1 text-xs text-gray-500">
                      <FileText className="w-3.5 h-3.5" />
                      <span>{test.data.length} бодлого</span>
                      <Clock className="w-3.5 h-3.5 ml-1" />
                      <span>100 мин</span>
                    </div>
                  </div>
                  {active ? (
                    <span className="text-xs font-medium px-2 py-1 rounded-full bg-yellow-500/15 text-yellow-400 border border-yellow-400/20">
                      Үргэлжлүүлэх
                    </span>
                  ) : (
                    <Play className="w-5 h-5 text-gray-600 group-hover:text-primary-400 transition-colors" />
                  )}
                </div>

                {mounted && best !== null && (
                  <div className="flex items-center gap-3 mt-3 pt-3 border-t border-white/[0.06]">
                    <div className="flex items-center gap-1.5">
                      <Trophy className="w-3.5 h-3.5 text-yellow-500" />
                      <span
                        className={`text-sm font-bold ${
                          best >= 80
                            ? "text-emerald-400"
                            : best >= 50
                              ? "text-yellow-400"
                              : "text-red-400"
                        }`}
                      >
                        {best}%
                      </span>
                    </div>
                    <span className="text-xs text-gray-600">
                      {attemptCount} удаа бодсон
                    </span>
                    {latest?.completedAt && (
                      <span className="text-xs text-gray-600 ml-auto">
                        {new Date(latest.completedAt).toLocaleDateString("mn-MN")}
                      </span>
                    )}
                  </div>
                )}

                {mounted && best === null && (
                  <div className="mt-3 pt-3 border-t border-white/[0.06]">
                    <span className="text-xs text-gray-600">Бодоогүй</span>
                  </div>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Start confirmation modal */}
      {showStartModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
          <div className="card-glass p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-primary-500/20 flex items-center justify-center">
                <Play className="w-5 h-5 text-primary-400" />
              </div>
              <div>
                <h3 className="font-display font-bold text-white">
                  {getAllTests().find((t) => t.key === showStartModal)?.label}
                </h3>
                <p className="text-xs text-gray-500">Шалгалт эхлүүлэх</p>
              </div>
            </div>

            <div className="space-y-2 mb-6 text-sm text-gray-400">
              <div className="flex items-center gap-2">
                <FileText className="w-4 h-4 text-gray-500" />
                <span>
                  {getAllTests().find((t) => t.key === showStartModal)?.data.length}{" "}
                  бодлого
                </span>
              </div>
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-gray-500" />
                <span>100 минийн хугацаатай</span>
              </div>
              <div className="flex items-center gap-2">
                <AlertCircle className="w-4 h-4 text-gray-500" />
                <span>Хариулт шалгалт дуусмагц харагдана</span>
              </div>
            </div>

            <div className="flex gap-3">
              <button
                onClick={() => setShowStartModal(null)}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Буцах
              </button>
              <button
                onClick={() => {
                  handleStart(showStartModal);
                  setShowStartModal(null);
                }}
                className="flex-1 btn-primary text-sm py-2.5"
              >
                Эхлэх
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Resume modal */}
      {showResumeModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
          <div className="card-glass p-6 max-w-sm w-full">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-yellow-500/20 flex items-center justify-center">
                <RotateCcw className="w-5 h-5 text-yellow-400" />
              </div>
              <div>
                <h3 className="font-display font-bold text-white">
                  Дуусаагүй шалгалт байна
                </h3>
                <p className="text-xs text-gray-500">
                  {getAllTests().find((t) => t.key === showResumeModal)?.label}
                </p>
              </div>
            </div>

            <p className="text-sm text-gray-400 mb-6">
              Та өмнө нь энэ шалгалтыг эхлүүлсэн байна. Үргэлжлүүлэх үү эсвэл
              шинээр эхлэх үү?
            </p>

            <div className="flex gap-3">
              <button
                onClick={() => {
                  handleStart(showResumeModal);
                  setShowResumeModal(null);
                }}
                className="flex-1 px-4 py-2.5 rounded-xl text-sm font-medium text-gray-400 bg-white/[0.05] border border-white/[0.08] hover:bg-white/[0.1] transition-colors"
              >
                Шинээр эхлэх
              </button>
              <button
                onClick={() => {
                  handleResume(showResumeModal);
                  setShowResumeModal(null);
                }}
                className="flex-1 btn-primary text-sm py-2.5"
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
