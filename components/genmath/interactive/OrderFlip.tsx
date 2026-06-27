"use client";

import { useState } from "react";
import { ArrowLeftRight, Smile, Frown } from "lucide-react";
import { type OrderFlipConfig, formatRatio } from "@/lib/genmath-interactive";

// The two labels stay PUT (cocoa first, milk second); flipping swaps only the
// NUMBERS. Forward: a cocoa : b milk (good). Flipped: b cocoa : a milk (mud).
// That's what makes "order matters" true — the actual mix changes.
export default function OrderFlip({ config }: { config: OrderFlipConfig }) {
  const [flipped, setFlipped] = useState(false);

  const countA = flipped ? config.b : config.a; // number on tokenA (e.g. cocoa)
  const countB = flipped ? config.a : config.b; // number on tokenB (e.g. milk)
  const outcome = flipped ? config.flippedLabel : config.forwardLabel;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* Order readout — tokens fixed, numbers swap */}
      <div className="flex items-center justify-center gap-3">
        {[
          { token: config.tokenA, n: countA },
          { token: config.tokenB, n: countB },
        ].map((g, gi) => (
          <div key={gi} className="flex items-center gap-2">
            {gi === 1 && <span className="serif" style={{ fontSize: 24, color: "var(--fg-3)" }}>:</span>}
            <div
              key={g.n}
              className="gm-fade flex items-center gap-2 rounded-xl px-3 py-2"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
            >
              <span className="grid h-7 w-7 place-items-center rounded-lg" style={{ background: g.token.color, border: "1px solid rgba(0,0,0,0.10)" }}>
                {g.token.glyph ?? ""}
              </span>
              <span className="serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>{g.n}</span>
              <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>{g.token.label}</span>
            </div>
          </div>
        ))}
      </div>

      {/* Outcome */}
      <div
        key={flipped ? "bad" : "good"}
        className="gm-step mx-auto mt-4 flex max-w-xs items-center gap-3 rounded-xl p-3"
        style={{
          background: flipped ? "rgba(90,70,50,0.12)" : "var(--accent-wash)",
          border: `1px solid ${flipped ? "rgba(90,70,50,0.35)" : "var(--accent-line)"}`,
        }}
      >
        <span
          className="grid h-12 w-12 flex-shrink-0 place-items-center rounded-full"
          style={{ background: flipped ? "#5a4632" : "#c98a4b", color: "#fff" }}
        >
          {flipped ? <Frown className="h-6 w-6" /> : <Smile className="h-6 w-6" />}
        </span>
        <div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            {config.tokenA.label} : {config.tokenB.label} = {formatRatio(countA, countB)} makes
          </div>
          <div className="serif" style={{ fontSize: 18, color: "var(--fg)" }}>{outcome}</div>
        </div>
      </div>

      {/* Flip control */}
      <div className="mt-4 flex justify-center">
        <button
          type="button"
          onClick={() => setFlipped((v) => !v)}
          className="gm-press inline-flex items-center gap-2 rounded-full px-5 py-3 text-[14px]"
          style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)", border: "1px solid var(--accent)" }}
        >
          <ArrowLeftRight className="h-4 w-4" />
          Flip the order
        </button>
      </div>
    </div>
  );
}
