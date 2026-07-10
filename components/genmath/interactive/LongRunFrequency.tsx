"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type LongRunFrequencyConfig } from "@/lib/genmath-interactive";

// The Law of Large Numbers as a toy: run the event in batches and watch the
// running relative frequency wobble hard, then settle onto the dashed
// true-probability line. Short runs lie; long runs don't.

const MAX_TRIALS = 400;

export default function LongRunFrequency({ config }: { config: LongRunFrequencyConfig }) {
  const { p, pLabel, eventLabel, actionLabel = "run" } = config;
  // freqs[i] = running relative frequency after trial i+1
  const [freqs, setFreqs] = useState<number[]>([]);
  const [hits, setHits] = useState(0);

  const total = freqs.length;

  const run = (n: number) => {
    const add = Math.min(n, MAX_TRIALS - total);
    if (add <= 0) return;
    let h = hits;
    const next = [...freqs];
    for (let i = 0; i < add; i++) {
      if (Math.random() < p) h++;
      next.push(h / (next.length + 1));
    }
    setHits(h);
    setFreqs(next);
  };

  const reset = () => {
    setFreqs([]);
    setHits(0);
  };

  const W = 360;
  const H = 190;
  const padL = 34;
  const padR = 12;
  const padT = 14;
  const padB = 26;
  const plotW = W - padL - padR;
  const plotH = H - padT - padB;
  const px = (i: number) => padL + (i / MAX_TRIALS) * plotW;
  const py = (f: number) => padT + (1 - f) * plotH;

  const path = freqs.map((f, i) => `${i === 0 ? "M" : "L"}${px(i + 1).toFixed(1)},${py(f).toFixed(1)}`).join(" ");
  const current = total > 0 ? freqs[total - 1] : null;
  const settled = total >= 100 && current !== null && Math.abs(current - p) < 0.05;

  const batchBtn = (n: number, primary: boolean) => (
    <button
      key={n}
      type="button"
      onClick={() => run(n)}
      disabled={total >= MAX_TRIALS}
      className="gm-press rounded-full px-4 py-2 text-[13px] disabled:opacity-35"
      style={
        primary
          ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
          : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
      }
    >
      {actionLabel} ×{n}
    </button>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Running relative frequency chart">
          {/* frame + gridlines at 0, ½, 1 */}
          {[0, 0.5, 1].map((f) => (
            <g key={f}>
              <line x1={padL} y1={py(f)} x2={W - padR} y2={py(f)} stroke="var(--line)" strokeWidth={1} />
              <text x={padL - 5} y={py(f) + 3.5} fontSize="9" fill="var(--fg-3)" textAnchor="end" className="tabular">
                {f === 0.5 ? "0.5" : f}
              </text>
            </g>
          ))}
          <line x1={padL} y1={padT} x2={padL} y2={H - padB} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={padL} y1={py(0)} x2={W - padR} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.6} />
          {[100, 200, 300, 400].map((t) => (
            <text key={t} x={px(t)} y={H - 10} fontSize="9" fill="var(--fg-3)" textAnchor="middle" className="tabular">
              {t}
            </text>
          ))}
          <text x={W - padR} y={H - 10} fontSize="9" fill="var(--fg-3)" textAnchor="end" />

          {/* the true-p line the frequency settles toward */}
          <line x1={padL} y1={py(p)} x2={W - padR} y2={py(p)} stroke="var(--accent)" strokeWidth={1.6} strokeDasharray="5 4" />
          <text x={W - padR - 2} y={py(p) - 5} fontSize="9.5" fill="var(--accent)" textAnchor="end" className="tabular">
            true p = {pLabel}
          </text>

          {/* the running frequency */}
          {total > 0 && <path d={path} fill="none" stroke={GEO_BLUE} strokeWidth={1.8} />}
          {current !== null && <circle cx={px(total)} cy={py(current)} r={4} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1} />}
        </svg>
      </div>

      {/* readout */}
      <div
        className="mt-2 rounded-xl p-3 text-center"
        style={{
          transition: "background 0.35s ease, border-color 0.35s ease",
          ...(settled
            ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
            : { background: "var(--bg-2)", border: "1px solid var(--line)" }),
        }}
      >
        {current === null ? (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            event: <b>{eventLabel}</b>, true probability {pLabel} — run it and watch the frequency
          </div>
        ) : (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              {hits} / {total} = <b style={{ color: settled ? "var(--accent)" : GEO_BLUE }}>{(current).toFixed(3)}</b>
              <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                vs true p = {pLabel} ≈ {(Math.round(p * 1000) / 1000).toString()}
              </span>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {total < 30
                ? "short runs swing wildly — probability says nothing about a handful of tries"
                : settled
                  ? "🎯 settled — the long run keeps its promise"
                  : "getting steadier — the wobble shrinks as the run grows"}
            </div>
          </>
        )}
      </div>

      <div className="mt-3 flex flex-wrap justify-center gap-2">
        {batchBtn(1, false)}
        {batchBtn(10, false)}
        {batchBtn(100, true)}
        <button
          type="button"
          onClick={reset}
          disabled={total === 0}
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
