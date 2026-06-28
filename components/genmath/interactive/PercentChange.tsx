"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type PercentChangeConfig } from "@/lib/genmath-interactive";
import PercentChangeView from "@/components/genmath/interactive/PercentChangeView";

export default function PercentChange({ config }: { config: PercentChangeConfig }) {
  const { original, start = 0, mode, currency = "$", color = "#e8913c" } = config;
  const [p, setP] = useState(Math.max(0, Math.min(100, Math.round(start))));
  const step = (d: number) => setP((v) => Math.max(0, Math.min(100, v + d)));

  return (
    <div className="rounded-2xl p-4 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <PercentChangeView original={original} percent={p} mode={mode} currency={currency} color={color} />
      </div>

      <div className="mt-5 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => step(-5)}
          disabled={p <= 0}
          aria-label="Lower the percent"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center" style={{ minWidth: 96 }}>
          <div className="serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>{p}%</div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            {mode === "discount" ? "discount" : "tax / tip"}
          </div>
        </div>
        <button
          type="button"
          onClick={() => step(5)}
          disabled={p >= 100}
          aria-label="Raise the percent"
          className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
    </div>
  );
}
