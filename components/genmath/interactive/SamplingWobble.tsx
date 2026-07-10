"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type SamplingWobbleConfig } from "@/lib/genmath-interactive";

// The sampling-wobble machine: draw samples of size n from a population with
// true proportion p, and stack every sample's p-hat as a dot. Small n → a
// wide, scattered pile; big n → a tight one hugging the dashed truth line.
// The optional band shades p ± 1/√n, the margin-of-error rule of thumb.

const MAX_SAMPLES = 200;

function fmt(n: number, dp = 2): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toFixed(dp);
}

export default function SamplingWobble({ config }: { config: SamplingWobbleConfig }) {
  const { p, pLabel, statLabel = "sample proportion p̂", nChoices = [25, 100, 400], showMoe = false } = config;
  const [n, setN] = useState(nChoices[0]);
  const [samples, setSamples] = useState<number[]>([]);

  const draw = (count: number) => {
    const add = Math.min(count, MAX_SAMPLES - samples.length);
    if (add <= 0) return;
    const next = [...samples];
    for (let s = 0; s < add; s++) {
      let hits = 0;
      for (let i = 0; i < n; i++) if (Math.random() < p) hits++;
      next.push(hits / n);
    }
    setSamples(next);
  };

  const switchN = (nn: number) => {
    setN(nn);
    setSamples([]);
  };

  const W = 380;
  const H = 210;
  const padL = 16;
  const padR = 16;
  const axisY = H - 36;
  // window wide enough for the wobble of the smallest n on offer
  const halfSpan = Math.min(0.5, Math.max(0.16, 2.8 * Math.sqrt((p * (1 - p)) / Math.min(...nChoices))));
  const lo = Math.max(0, p - halfSpan);
  const hi = Math.min(1, p + halfSpan);
  const px = (v: number) => padL + ((v - lo) / (hi - lo)) * (W - padL - padR);

  // stack dots into 0.01-wide slots
  const slotOf = (v: number) => Math.round(v * 100);
  const seen = new Map<number, number>();
  const stacked = samples.map((v) => {
    const k = slotOf(v);
    const s = seen.get(k) ?? 0;
    seen.set(k, s + 1);
    return { v, stack: s };
  });

  const moe = 1 / Math.sqrt(n);
  const last = samples[samples.length - 1];

  const btn = (label: string, onClick: () => void, primary: boolean, disabled = false) => (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className="gm-press rounded-full px-4 py-2 text-[13px] disabled:opacity-35"
      style={
        primary
          ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
          : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
      }
    >
      {label}
    </button>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* sample-size chips */}
      <div className="mb-3 flex justify-center gap-1.5">
        {nChoices.map((nn) => (
          <button
            key={nn}
            type="button"
            onClick={() => switchN(nn)}
            className="gm-press rounded-full px-3.5 py-1.5 text-[12px] tabular"
            style={
              n === nn
                ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
            }
          >
            n = {nn}
          </button>
        ))}
      </div>

      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 420 }} role="img" aria-label="Sampling distribution dots">
          {/* margin-of-error band */}
          {showMoe && (
            <rect
              x={px(Math.max(lo, p - moe))}
              y={20}
              width={px(Math.min(hi, p + moe)) - px(Math.max(lo, p - moe))}
              height={axisY - 20}
              fill="var(--accent)"
              fillOpacity={0.1}
            />
          )}

          {/* axis */}
          <line x1={padL} y1={axisY} x2={W - padR} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.6} />
          {Array.from({ length: 11 }, (_, i) => lo + (i / 10) * (hi - lo)).map((v, i) => (
            <g key={i}>
              <line x1={px(v)} y1={axisY} x2={px(v)} y2={axisY + 4} stroke="var(--fg-2)" strokeWidth={1} />
              {i % 2 === 0 && (
                <text x={px(v)} y={axisY + 15} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                  {fmt(v)}
                </text>
              )}
            </g>
          ))}
          <text x={W - padR} y={H - 6} fontSize="10" fill="var(--fg-2)" textAnchor="end">
            {statLabel}
          </text>

          {/* the truth line */}
          <line x1={px(p)} y1={16} x2={px(p)} y2={axisY} stroke="var(--accent)" strokeWidth={1.6} strokeDasharray="5 4" />
          <text x={px(p)} y={12} fontSize="9.5" fill="var(--accent)" textAnchor="middle" className="tabular">
            true p = {pLabel ?? fmt(p)}
          </text>

          {/* the pile of sample results */}
          {stacked.map(({ v, stack }, i) => (
            <circle
              key={i}
              className={i === samples.length - 1 ? "gm-pop" : undefined}
              cx={px(Math.max(lo, Math.min(hi, v)))}
              cy={axisY - 7 - stack * 9}
              r={4}
              fill={i === samples.length - 1 ? "var(--accent)" : GEO_BLUE}
              fillOpacity={0.8}
              stroke="var(--bg-1)"
              strokeWidth={0.8}
            />
          ))}
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {samples.length === 0 ? (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            every dot will be one whole survey of {n} people — draw a few
          </div>
        ) : (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              {samples.length} samples of n = {n} · latest p̂ = <b style={{ color: "var(--accent)" }}>{fmt(last)}</b>
              {showMoe && (
                <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                  band: p ± 1/√{n} = ±{fmt(moe)}
                </span>
              )}
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {n >= Math.max(...nChoices)
                ? "big samples wobble least — the pile hugs the truth"
                : "the pile centres on p, but small samples spread wide — try a bigger n"}
            </div>
          </>
        )}
      </div>

      <div className="mt-3 flex flex-wrap justify-center gap-2">
        {btn("draw 1 sample", () => draw(1), false, samples.length >= MAX_SAMPLES)}
        {btn("draw 20", () => draw(20), true, samples.length >= MAX_SAMPLES)}
        <button
          type="button"
          onClick={() => setSamples([])}
          disabled={samples.length === 0}
          aria-label="Reset"
          className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-3.5 w-3.5" /> reset
        </button>
      </div>
    </div>
  );
}
