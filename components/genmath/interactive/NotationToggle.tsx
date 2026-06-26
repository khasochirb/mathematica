"use client";

import { useState } from "react";
import { Check } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type NotationToggleConfig } from "@/lib/genmath-interactive";

export default function NotationToggle({ config }: { config: NotationToggleConfig }) {
  const { a, b, tokenA, tokenB } = config;
  const [active, setActive] = useState<number | null>(null);

  const forms = [`$${a}:${b}$`, `${a} to ${b}`, `$\\dfrac{${a}}{${b}}$`];

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* The quantities, once */}
      <div className="flex flex-wrap items-center justify-center gap-2 rounded-xl p-3" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {Array.from({ length: a }).map((_, i) => (
          <span key={`a${i}`} className="h-6 w-6 rounded-lg" style={{ background: tokenA.color, border: "1px solid rgba(0,0,0,0.10)" }} />
        ))}
        <span className="mx-1 text-[12px]" style={{ color: "var(--fg-3)" }}>{tokenA.label}</span>
        <span className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>·</span>
        {Array.from({ length: b }).map((_, i) => (
          <span key={`b${i}`} className="h-6 w-6 rounded-lg" style={{ background: tokenB.color, border: "1px solid rgba(0,0,0,0.10)" }} />
        ))}
        <span className="mx-1 text-[12px]" style={{ color: "var(--fg-3)" }}>{tokenB.label}</span>
      </div>

      {/* Three ways — tap each */}
      <div className="mt-4 grid grid-cols-3 gap-2">
        {forms.map((f, i) => {
          const on = active === i;
          return (
            <button
              key={i}
              type="button"
              onClick={() => setActive(i)}
              className="gm-press grid place-items-center rounded-xl px-2 py-4"
              style={{
                background: on ? "var(--accent-wash)" : "var(--bg-2)",
                border: `1.5px solid ${on ? "var(--accent)" : "var(--line)"}`,
              }}
            >
              <span className="q-math" style={{ fontSize: 17, color: "var(--fg)" }}>
                <MathText text={f} />
              </span>
            </button>
          );
        })}
      </div>

      <div className="mt-3 flex items-center justify-center gap-1.5 text-center text-[13px]" style={{ color: active === null ? "var(--fg-3)" : "#2f9e6e" }}>
        {active === null ? (
          "Tap each one — they all say the same thing"
        ) : (
          <>
            <Check className="h-4 w-4" /> Same ratio: {a} {tokenA.label} for every {b} {tokenB.label}
          </>
        )}
      </div>
    </div>
  );
}
