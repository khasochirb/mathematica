"use client";

import { useMemo, useState } from "react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { expectedValue, rvVariance, type DistributionBarsConfig } from "@/lib/genmath-interactive";

// A discrete random variable's distribution as bars on a number line —
// values may be negative, so winnings and losses work. Tap a bar for its
// x · P(x) contribution; the balance-point triangle sits at the mean, and
// whiskers stretch mu ± sigma when the lesson is about spread.

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return Number.isInteger(r) ? r.toString() : r.toFixed(2);
}

export default function DistributionBars({ config }: { config: DistributionBarsConfig }) {
  const { values, probs, pLabels, xLabel = "x", showMean = false, showSd = false } = config;
  const [pick, setPick] = useState<number | null>(null);

  const { mu, sd, lo, hi } = useMemo(() => {
    const mu = expectedValue(values, probs);
    const sd = Math.sqrt(rvVariance(values, probs));
    const lo = Math.min(...values, showMean ? mu : Infinity) - 1;
    const hi = Math.max(...values, showMean ? mu : -Infinity) + 1;
    return { mu, sd, lo: Math.floor(lo), hi: Math.ceil(hi) };
  }, [values, probs, showMean]);

  const W = 360;
  const H = 200;
  const padL = 16;
  const padR = 16;
  const axisY = H - 40;
  const plotH = axisY - 26;
  const px = (x: number) => padL + ((x - lo) / (hi - lo)) * (W - padL - padR);
  const maxP = Math.max(...probs);
  const barH = (p: number) => (p / maxP) * plotH;
  const barW = Math.min(34, ((W - padL - padR) / (hi - lo)) * 0.7);

  const ticks = useMemo(() => {
    const span = hi - lo;
    const step = span > 12 ? 2 : 1;
    const t: number[] = [];
    for (let x = lo; x <= hi; x += step) t.push(x);
    return t;
  }, [lo, hi]);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Probability distribution bars">
          {/* axis */}
          <line x1={padL} y1={axisY} x2={W - padR} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.6} />
          {ticks.map((x) => (
            <g key={x}>
              <line x1={px(x)} y1={axisY} x2={px(x)} y2={axisY + 4} stroke="var(--fg-2)" strokeWidth={1.2} />
              <text x={px(x)} y={axisY + 15} fontSize="9" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                {x}
              </text>
            </g>
          ))}
          <text x={W - padR} y={axisY + 28} fontSize="10" fill="var(--fg-2)" textAnchor="end">
            {xLabel}
          </text>

          {/* zero marker when losses are in play */}
          {lo < 0 && 0 < hi && <line x1={px(0)} y1={axisY} x2={px(0)} y2={26} stroke="var(--line)" strokeWidth={1.2} strokeDasharray="3 3" />}

          {/* bars */}
          {values.map((x, i) => {
            const hot = pick === i;
            return (
              <g key={i} className="gm-pop" style={{ cursor: "pointer", animationDelay: `${(i * 0.07).toFixed(2)}s` }} onClick={() => setPick(hot ? null : i)}>
                <rect
                  x={px(x) - barW / 2}
                  y={axisY - barH(probs[i])}
                  width={barW}
                  height={barH(probs[i])}
                  rx={4}
                  fill={hot ? "var(--accent)" : GEO_BLUE}
                  fillOpacity={hot ? 0.95 : 0.75}
                  stroke={hot ? "var(--accent)" : "none"}
                  style={{ transition: "fill 0.2s ease" }}
                />
                <text
                  x={px(x)}
                  y={axisY - barH(probs[i]) - 5}
                  fontSize="9.5"
                  textAnchor="middle"
                  className="tabular"
                  fill={hot ? "var(--accent)" : "var(--fg-2)"}
                  fontWeight={hot ? 700 : 500}
                >
                  {pLabels?.[i] ?? fmt(probs[i])}
                </text>
              </g>
            );
          })}

          {/* sigma whiskers under the axis, then the balance triangle */}
          {showSd && (
            <g>
              <line x1={px(mu - sd)} y1={axisY + 24} x2={px(mu + sd)} y2={axisY + 24} stroke="var(--accent)" strokeWidth={1.6} />
              {[mu - sd, mu + sd].map((x, i) => (
                <line key={i} x1={px(x)} y1={axisY + 20} x2={px(x)} y2={axisY + 28} stroke="var(--accent)" strokeWidth={1.6} />
              ))}
            </g>
          )}
          {showMean && (
            <g>
              <path
                d={`M${px(mu)},${axisY + 2} l -7,12 l 14,0 Z`}
                fill="var(--accent)"
                className="gm-pop"
                style={{ animationDelay: `${(values.length * 0.07 + 0.1).toFixed(2)}s` }}
              />
              <text x={px(mu)} y={axisY + 26} fontSize="9.5" fill="var(--accent)" textAnchor="middle" className="tabular" fontWeight={700}>
                μ = {fmt(mu)}
              </text>
            </g>
          )}
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {pick !== null ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            x = {values[pick]}: contributes {values[pick]} · {pLabels?.[pick] ?? fmt(probs[pick])} ={" "}
            <b style={{ color: "var(--accent)" }}>{fmt(values[pick] * probs[pick])}</b>
            <span className="ml-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
              toward the mean
            </span>
          </div>
        ) : showSd ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            μ = {fmt(mu)}, σ = <b style={{ color: "var(--accent)" }}>{fmt(sd)}</b>
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              — the whiskers reach one σ each way
            </span>
          </div>
        ) : showMean ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            E[X] = Σ x · P(x) = <b style={{ color: "var(--accent)" }}>{fmt(mu)}</b>
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              — the triangle marks the balance point
            </span>
          </div>
        ) : (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            each bar is P(X = x); heights add to 1 — tap a bar for its share
          </div>
        )}
      </div>
    </div>
  );
}
