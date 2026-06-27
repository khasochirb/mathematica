"use client";

import { useState } from "react";
import { Minus, Plus, Check } from "lucide-react";
import {
  type ScalerConfig,
  scaleRatio,
  simplifyRatio,
  formatRatio,
} from "@/lib/genmath-interactive";

function TokenCluster({
  count,
  color,
  glyph,
}: {
  count: number;
  color: string;
  glyph?: string;
}) {
  return (
    <div className="flex flex-wrap content-start gap-1.5" style={{ minHeight: 64 }}>
      {Array.from({ length: count }).map((_, i) => (
        <span
          key={i}
          className="gm-pop grid place-items-center rounded-lg"
          style={{
            width: 26,
            height: 26,
            background: color,
            border: "1px solid rgba(0,0,0,0.10)",
            fontSize: 13,
            lineHeight: 1,
            animationDelay: `${(i % 12) * 28}ms`,
            boxShadow: "0 1px 2px rgba(0,0,0,0.08)",
          }}
        >
          {glyph ?? ""}
        </span>
      ))}
    </div>
  );
}

export default function QuantityScaler({ config }: { config: ScalerConfig }) {
  const [n, setN] = useState(1);
  const [a, b] = scaleRatio(config.a, config.b, n);
  const [sa, sb] = simplifyRatio(config.a, config.b);

  const dec = () => setN((v) => Math.max(1, v - 1));
  const inc = () => setN((v) => Math.min(config.maxBatches, v + 1));

  return (
    <div
      className="rounded-2xl p-4 sm:p-5"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      {/* Stage: the two quantities */}
      <div className="grid grid-cols-2 gap-3">
        {[
          { token: config.tokenA, count: a },
          { token: config.tokenB, count: b },
        ].map((g, gi) => (
          <div
            key={gi}
            className="rounded-xl p-3"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
          >
            <div className="flex items-baseline gap-2">
              <span
                className="serif tabular"
                style={{ fontSize: 30, lineHeight: 1, color: "var(--fg)", transition: "color .2s" }}
              >
                {g.count}
              </span>
              <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>
                {g.token.plural}
              </span>
            </div>
            <div className="mt-2.5">
              <TokenCluster count={g.count} color={g.token.color} glyph={g.token.glyph} />
            </div>
          </div>
        ))}
      </div>

      {/* Stepper */}
      <div className="mt-4 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={dec}
          disabled={n <= 1}
          aria-label="Fewer batches"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-5 w-5" />
        </button>
        <div className="text-center" style={{ minWidth: 96 }}>
          <div className="serif tabular" style={{ fontSize: 26, lineHeight: 1, color: "var(--fg)" }}>
            {n}
          </div>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            {n === 1 ? "batch" : "batches"}
          </div>
        </div>
        <button
          type="button"
          onClick={inc}
          disabled={n >= config.maxBatches}
          aria-label="More batches"
          className="gm-press grid h-12 w-12 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-5 w-5" />
        </button>
      </div>

      {/* Live ratio readout */}
      <div className="mt-4 flex flex-wrap items-center justify-center gap-2 text-center">
        <span className="serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>
          {formatRatio(a, b)}
        </span>
        <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          always the same mix
        </span>
        <span
          className="rounded-full px-2.5 py-0.5 text-[12px]"
          style={{ background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}
        >
          = {formatRatio(sa, sb)}
        </span>
      </div>

      {/* Taste meter — stays full because the mix never changes */}
      <div className="mt-4 rounded-xl p-3" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="flex items-center justify-between">
          <span className="text-[12px]" style={{ color: "var(--fg-2)" }}>
            Taste
          </span>
          <span className="inline-flex items-center gap-1 text-[12px]" style={{ color: "#2f9e6e" }}>
            <Check className="h-3.5 w-3.5" /> {config.goodLabel}
          </span>
        </div>
        <div className="mt-1.5 h-2.5 w-full overflow-hidden rounded-full" style={{ background: "var(--bg-1)" }}>
          <div className="gm-fade h-full rounded-full" style={{ width: "100%", background: "#3fb27f" }} />
        </div>
      </div>
    </div>
  );
}
