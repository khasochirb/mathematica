"use client";

import { Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Trophy, Star, ArrowRight, RotateCcw } from "lucide-react";

function ResultContent() {
  const params = useSearchParams();
  const correct = Number(params.get("correct") ?? 0);
  const total = Number(params.get("total") ?? 0);
  const xp = Number(params.get("xp") ?? 0);
  const leveledUp = params.get("leveledUp") === "true";
  const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0;

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center pt-16 px-4">
      <div className="max-w-md w-full text-center">
        {leveledUp && (
          <div className="mb-6 inline-flex items-center gap-2 bg-yellow-100 border border-yellow-200 text-yellow-800 px-4 py-2 rounded-full text-sm font-semibold">
            ⬆️ Level Up!
          </div>
        )}

        <div className="w-20 h-20 bg-primary-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <Trophy className="h-10 w-10 text-white" />
        </div>

        <h1 className="text-3xl font-bold text-gray-900 mb-2">Session Complete!</h1>
        <p className="text-gray-500 mb-8">Great work—keep building that streak!</p>

        <div className="grid grid-cols-3 gap-4 mb-8">
          <div className="bg-white rounded-2xl border border-gray-100 p-4">
            <p className="text-2xl font-bold text-primary-600">{correct}/{total}</p>
            <p className="text-gray-400 text-xs mt-1">Correct</p>
          </div>
          <div className="bg-white rounded-2xl border border-gray-100 p-4">
            <p className="text-2xl font-bold text-accent-green">{accuracy}%</p>
            <p className="text-gray-400 text-xs mt-1">Accuracy</p>
          </div>
          <div className="bg-white rounded-2xl border border-gray-100 p-4">
            <p className="text-2xl font-bold text-yellow-500">+{xp}</p>
            <p className="text-gray-400 text-xs mt-1">XP Earned</p>
          </div>
        </div>

        <div className="flex flex-col gap-3">
          <Link href="/practice" className="btn-primary w-full py-3 text-center">
            Practice Again
            <RotateCcw className="ml-2 h-4 w-4" />
          </Link>
          <Link href="/progress" className="btn-secondary w-full py-3 text-center">
            View Progress
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function ResultPage() {
  return (
    <Suspense>
      <ResultContent />
    </Suspense>
  );
}
