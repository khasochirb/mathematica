"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { type OrderOfOpsConfig } from "@/lib/genmath-interactive";

// Walks an expression down to its value one operation at a time. Each tap on
// "Next step" reveals the next stage — the running expression plus a note saying
// which operation was just carried out and why it came first (PEMDAS order).
export default function OrderOfOps({ config }: { config: OrderOfOpsConfig }) {
  const { stages, color = "#e8913c" } = config;
  const [shown, setShown] = useState(1);
  const done = shown >= stages.length;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex flex-col gap-2.5">
        {stages.slice(0, shown).map((s, i) => {
          const isCurrent = i === shown - 1;
          return (
            <div key={i}>
              <div
                className="serif tabular rounded-xl px-4 py-3 text-center"
                style={{
                  fontSize: 20,
                  background: isCurrent ? "var(--bg-2)" : "transparent",
                  border: isCurrent ? `1px solid ${color}` : "1px solid transparent",
                  color: i === stages.length - 1 && done ? "var(--accent)" : "var(--fg)",
                }}
              >
                {s.expr}
              </div>
              {s.did && i > 0 && (
                <div className="mt-1 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
                  {s.did}
                </div>
              )}
            </div>
          );
        })}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setShown(1)}
          disabled={shown === 1}
          aria-label="Reset"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
        <button
          type="button"
          onClick={() => setShown((v) => Math.min(stages.length, v + 1))}
          disabled={done}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          Next step
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {done ? "Done — operations followed PEMDAS order." : "Work one operation at a time, highest priority first."}
      </div>
    </div>
  );
}
