"use client";

import { useState } from "react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { binCounts, type HistogramBinsConfig } from "@/lib/genmath-interactive";

// One dataset, several bin widths. The chips regroup the same values into a
// fresh histogram — too-wide bins bury the shape, too-narrow bins shatter
// it, and the middle choice lets the story (skew, peaks, gaps) show.

export default function HistogramBins({ config }: { config: HistogramBinsConfig }) {
  const { data, min, max, widths, start = 0, xLabel = "value" } = config;
  const [wIx, setWIx] = useState(Math.min(start, widths.length - 1));

  const w = widths[wIx];
  const counts = binCounts(data, min, w, max);
  const maxCount = Math.max(...counts, 1);

  const W = 360;
  const H = 210;
  const padL = 30;
  const padR = 14;
  const axisY = H - 40;
  const plotH = axisY - 20;
  const px = (x: number) => padL + ((x - min) / (max - min)) * (W - padL - padR);
  const barH = (c: number) => (c / maxCount) * plotH;

  const yTickStep = maxCount > 12 ? 4 : maxCount > 6 ? 2 : 1;
  const yTicks = [];
  for (let c = yTickStep; c <= maxCount; c += yTickStep) yTicks.push(c);

  // x labels on the bin edges, thinned when they crowd
  const edges = counts.map((_, i) => min + i * w).concat([min + counts.length * w]);
  const labelEvery = edges.length > 12 ? 2 : 1;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Histogram">
          {/* count gridlines */}
          {yTicks.map((c) => (
            <g key={c}>
              <line x1={padL} y1={axisY - barH(c)} x2={W - padR} y2={axisY - barH(c)} stroke="var(--line)" strokeWidth={1} />
              <text x={padL - 5} y={axisY - barH(c) + 3.5} fontSize="9" fill="var(--fg-3)" textAnchor="end" className="tabular">
                {c}
              </text>
            </g>
          ))}
          <line x1={padL} y1={axisY} x2={W - padR} y2={axisY} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={padL} y1={axisY} x2={padL} y2={axisY - plotH} stroke="var(--fg-2)" strokeWidth={1.6} />

          {/* bars — keyed by width so a regroup pops in fresh */}
          {counts.map((c, i) => (
            <g key={`${w}-${i}`} className="gm-pop" style={{ animationDelay: `${(i * 0.04).toFixed(2)}s` }}>
              <rect
                x={px(min + i * w) + 1}
                y={axisY - barH(c)}
                width={Math.max(1, px(min + (i + 1) * w) - px(min + i * w) - 2)}
                height={barH(c)}
                rx={3}
                fill={GEO_BLUE}
                fillOpacity={0.72}
                stroke="var(--bg-1)"
                strokeWidth={1}
              />
              {c > 0 && (
                <text x={(px(min + i * w) + px(min + (i + 1) * w)) / 2} y={axisY - barH(c) - 4} fontSize="8.5" fill="var(--fg-2)" textAnchor="middle" className="tabular">
                  {c}
                </text>
              )}
            </g>
          ))}

          {/* bin-edge labels */}
          {edges.map((e, i) =>
            i % labelEvery === 0 ? (
              <text key={i} x={px(e)} y={axisY + 14} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle" className="tabular">
                {Math.round(e * 100) / 100}
              </text>
            ) : null,
          )}
          <text x={W - padR} y={axisY + 28} fontSize="10" fill="var(--fg-2)" textAnchor="end">
            {xLabel}
          </text>
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
          {data.length} values → <b style={{ color: "var(--accent)" }}>{counts.length}</b> bins of width{" "}
          <b style={{ color: "var(--accent)" }}>{w}</b>
        </div>
        <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
          same data every time — only the grouping changes
        </div>
      </div>

      <div className="mt-3 flex flex-wrap justify-center gap-1.5">
        {widths.map((wd, i) => (
          <button
            key={wd}
            type="button"
            onClick={() => setWIx(i)}
            className="gm-press rounded-full px-3.5 py-1.5 text-[12px] tabular"
            style={
              wIx === i
                ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
            }
          >
            width {wd}
          </button>
        ))}
      </div>
    </div>
  );
}
