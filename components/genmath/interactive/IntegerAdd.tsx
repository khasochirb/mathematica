"use client";

import { useState } from "react";
import { CornerUpRight, RotateCcw } from "lucide-react";
import { type IntegerAddConfig } from "@/lib/genmath-interactive";
import IntegerAddView from "@/components/genmath/interactive/IntegerAddView";

export default function IntegerAdd({ config }: { config: IntegerAddConfig }) {
  const { a, b, min, max, color = "#e8913c" } = config;
  const [jumped, setJumped] = useState(false);
  const sum = a + b;
  const dir = b < 0 ? "left" : "right";
  const bStr = b >= 0 ? `+ ${b}` : `+ (${b})`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <IntegerAddView a={a} b={b} min={min} max={max} color={color} showJump={jumped} />
      </div>

      <div className="mt-2 flex flex-wrap items-center justify-center gap-2">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{a} {bStr}</span>
        {jumped && (
          <span className="gm-fade">
            <span style={{ color: "var(--fg-3)" }}> = </span>
            <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{sum}</span>
          </span>
        )}
      </div>

      <div className="mt-4 flex justify-center">
        {!jumped ? (
          <button
            type="button"
            onClick={() => setJumped(true)}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <CornerUpRight className="h-4 w-4" /> Jump {Math.abs(b)} {dir}
          </button>
        ) : (
          <button
            type="button"
            onClick={() => setJumped(false)}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RotateCcw className="h-3.5 w-3.5" /> Reset
          </button>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Add a <b style={{ color: "var(--fg-1)" }}>positive</b> → jump right; add a <b style={{ color: "var(--fg-1)" }}>negative</b> → jump left.
      </div>
    </div>
  );
}
