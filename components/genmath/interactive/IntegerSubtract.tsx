"use client";

import { useState } from "react";
import { Repeat, RotateCcw } from "lucide-react";
import { type IntegerAddConfig } from "@/lib/genmath-interactive";
import IntegerAddView from "@/components/genmath/interactive/IntegerAddView";

// Subtracting = adding the opposite. The student sees a − b, taps "add the
// opposite" to rewrite it as a + (−b), and the jump plays out on the line.
export default function IntegerSubtract({ config }: { config: IntegerAddConfig }) {
  const { a, b, min, max, color = "#e8913c" } = config;
  const [flipped, setFlipped] = useState(false);
  const opp = -b;
  const result = a - b;
  const bStr = b >= 0 ? `${b}` : `(${b})`;
  const oppStr = opp >= 0 ? `${opp}` : `(${opp})`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <IntegerAddView a={a} b={opp} min={min} max={max} color={color} showJump={flipped} />
      </div>

      <div className="mt-2 flex flex-wrap items-center justify-center gap-2">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{a} − {bStr}</span>
        {flipped && (
          <span className="gm-fade flex flex-wrap items-center gap-2">
            <span style={{ color: "var(--fg-3)" }}>=</span>
            <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>{a} + {oppStr}</span>
            <span style={{ color: "var(--fg-3)" }}>=</span>
            <span className="serif tabular rounded-lg px-3 py-1" style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{result}</span>
          </span>
        )}
      </div>

      <div className="mt-4 flex justify-center">
        {!flipped ? (
          <button
            type="button"
            onClick={() => setFlipped(true)}
            className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-[14px]"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <Repeat className="h-4 w-4" /> Add the opposite
          </button>
        ) : (
          <button
            type="button"
            onClick={() => setFlipped(false)}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RotateCcw className="h-3.5 w-3.5" /> Reset
          </button>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Subtracting is <b style={{ color: "var(--fg-1)" }}>adding the opposite</b> — then jump as usual.
      </div>
    </div>
  );
}
