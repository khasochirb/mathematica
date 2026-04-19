"use client";

import { Suspense } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Trophy, ArrowRight, RotateCcw } from "lucide-react";

function ResultContent() {
  const params = useSearchParams();
  const correct = Number(params.get("correct") ?? 0);
  const total = Number(params.get("total") ?? 0);
  const xp = Number(params.get("xp") ?? 0);
  const leveledUp = params.get("leveledUp") === "true";
  const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0;

  return (
    <div className="min-h-screen flex items-center justify-center pt-20 px-4" style={{ background: "var(--bg)" }}>
      <div className="max-w-md w-full text-center">
        {leveledUp && (
          <div
            className="mb-6 inline-flex items-center gap-2 px-3 py-1.5 rounded-full mono text-[11px]"
            style={{
              background: "var(--accent-wash)",
              border: "1px solid var(--accent-line)",
              color: "var(--accent)",
              letterSpacing: "0.06em",
            }}
          >
            ↑ LEVEL UP
          </div>
        )}

        <div
          className="w-16 h-16 rounded-md flex items-center justify-center mx-auto mb-6"
          style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
        >
          <Trophy className="h-7 w-7" />
        </div>

        <div className="eyebrow mb-2">Session · Complete</div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: 40, letterSpacing: "-0.03em", color: "var(--fg)" }}>
          Nicely <em className="serif-italic" style={{ color: "var(--accent)" }}>done</em>.
        </h1>
        <p className="text-[14px] mt-3 mb-8" style={{ color: "var(--fg-2)" }}>
          Great work — keep building that streak.
        </p>

        <div className="grid grid-cols-3 gap-3 mb-8">
          {[
            { value: `${correct}/${total}`, label: "Correct" },
            { value: `${accuracy}%`, label: "Accuracy" },
            { value: `+${xp}`, label: "XP earned" },
          ].map((s) => (
            <div key={s.label} className="card-edit p-4">
              <p className="serif tabular" style={{ fontSize: 26, letterSpacing: "-0.02em", color: "var(--accent)" }}>
                {s.value}
              </p>
              <p className="mono text-[10px] mt-1 uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                {s.label}
              </p>
            </div>
          ))}
        </div>

        <div className="flex flex-col gap-2">
          <Link href="/practice" className="btn btn-primary w-full">
            Practice again
            <RotateCcw className="ml-1 h-3.5 w-3.5" />
          </Link>
          <Link href="/progress" className="btn btn-line w-full">
            View progress
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
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
