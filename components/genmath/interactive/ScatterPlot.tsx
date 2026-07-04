"use client";

import { useMemo, useState } from "react";
import { Minus, Plus, Sparkles } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type ScatterPlotConfig } from "@/lib/genmath-interactive";

// The bivariate-data workbench, in four animated modes:
//   plot         — the points RAIN IN one by one, like data being collected.
//   correlation  — buttons swap the dataset and every point GLIDES to its new
//                  home: positive ↗, negative ↘, or no pattern at all.
//   outlier      — one point sits far off the trend, marked with a beacon.
//   fit          — the line-fitting game: steer m and b to shrink the residual
//                  sticks and the "average miss" score; one button springs the
//                  line to the true least-squares fit.

const GREEN = "#3fa06a";
const RED = "rgb(200,60,60)";

// Honest fixed datasets on a 0–10 grid (12 points each).
const DATA: Record<string, [number, number][]> = {
  positive: [[1, 3], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [5, 7], [6, 7], [7, 8], [8, 8], [8, 9], [9, 10]],
  negative: [[1, 9], [2, 9], [2, 8], [3, 8], [4, 7], [5, 7], [5, 6], [6, 5], [7, 5], [8, 4], [8, 3], [9, 3]],
  none: [[1, 5], [2, 8], [2, 3], [3, 6], [4, 2], [4, 9], [5, 5], [6, 8], [7, 3], [7, 7], [8, 2], [9, 6]],
  outlier: [[1, 3], [2, 4], [2, 5], [3, 5], [4, 6], [5, 6], [5, 7], [6, 7], [7, 8], [8, 9], [9, 10], [8, 2]],
};

const CORR_LABEL: Record<string, { name: string; blurb: string; color: string }> = {
  positive: { name: "positive correlation", blurb: "as x grows, y tends to grow — the cloud climbs ↗", color: GREEN },
  negative: { name: "negative correlation", blurb: "as x grows, y tends to fall — the cloud sinks ↘", color: RED },
  none: { name: "no correlation", blurb: "no pattern — knowing x tells you nothing about y", color: "var(--fg-2)" },
};

function fmt(n: number): string {
  return Number.isInteger(n) ? n.toString() : (Math.round(n * 100) / 100).toString();
}

// least-squares slope/intercept for a dataset
function leastSquares(pts: [number, number][]) {
  const n = pts.length;
  const sx = pts.reduce((s, p) => s + p[0], 0);
  const sy = pts.reduce((s, p) => s + p[1], 0);
  const sxx = pts.reduce((s, p) => s + p[0] * p[0], 0);
  const sxy = pts.reduce((s, p) => s + p[0] * p[1], 0);
  const m = (n * sxy - sx * sy) / (n * sxx - sx * sx);
  const b = (sy - m * sx) / n;
  return { m, b };
}

// One dot that springs to its target — dataset swaps make the whole cloud glide.
function SpringPoint({ tx, ty, px, py, delay, color, r = 4 }: {
  tx: number; ty: number;
  px: (x: number) => number; py: (y: number) => number;
  delay: number; color: string; r?: number;
}) {
  const x = useAnimatedValue(tx, { stiffness: 90, damping: 16 });
  const y = useAnimatedValue(ty, { stiffness: 90, damping: 16 });
  return (
    <g className="gm-pop" style={{ animationDelay: `${delay.toFixed(2)}s` }}>
      <circle cx={px(x)} cy={py(y)} r={r} fill={color} fillOpacity={0.85} stroke="var(--bg-1)" strokeWidth={1} />
    </g>
  );
}

export default function ScatterPlot({ config }: { config: ScatterPlotConfig }) {
  const {
    mode,
    dataset: ds0 = "positive",
    xLabel = "x",
    yLabel = "y",
    m0 = 0.3,
    b0 = 6,
  } = config;

  const [dataset, setDataset] = useState(ds0);
  const [m, setM] = useState(m0);
  const [b, setB] = useState(b0);
  const [showResiduals, setShowResiduals] = useState(true);

  const pts = mode === "outlier" ? DATA.outlier : DATA[dataset] ?? DATA.positive;
  const best = useMemo(() => leastSquares(mode === "fit" ? DATA.positive : pts), [mode, pts]);

  // the fitted line glides as m/b step (and leaps when "best fit" is pressed)
  const md = useAnimatedValue(m, { stiffness: 120, damping: 18 });
  const bd = useAnimatedValue(b, { stiffness: 120, damping: 18 });

  const min = 0, max = 10;
  const N = max - min;
  const cell = 27;
  const pad = 26;
  const W = N * cell + pad * 2;
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;
  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);

  // fit-game scoring uses EXACT m/b (never the in-flight spring values)
  const fitPts = DATA.positive;
  const avgMiss = fitPts.reduce((s, [x, y]) => s + Math.abs(y - (m * x + b)), 0) / fitPts.length;
  const bestMiss = fitPts.reduce((s, [x, y]) => s + Math.abs(y - (best.m * x + best.b)), 0) / fitPts.length;
  const nearBest = avgMiss <= bestMiss + 0.15;

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, lo: number, hi: number, delta: number) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(lo, Math.round((v - delta) * 100) / 100))} disabled={val <= lo} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 40, fontSize: 16, color: GEO_BLUE }}>{fmt(val)}</div>
        <button type="button" onClick={() => set((v) => Math.min(hi, Math.round((v + delta) * 100) / 100))} disabled={val >= hi} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  const corr = CORR_LABEL[mode === "outlier" ? "positive" : dataset] ?? CORR_LABEL.positive;
  const outlierIx = pts.length - 1; // in the outlier dataset the stray point is last

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 350 }} role="img" aria-label="Scatter plot">
          {ints.map((g) => (
            <g key={`g${g}`}>
              <line x1={px(g)} y1={py(max)} x2={px(g)} y2={py(min)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(min)} y1={py(g)} x2={px(max)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          {/* axes */}
          <line x1={px(min)} y1={py(min)} x2={px(max)} y2={py(min)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(min)} y1={py(min)} x2={px(min)} y2={py(max)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {ints.filter((g) => g % 2 === 0 && g > 0).map((g) => (
            <g key={`lbl${g}`}>
              <text x={px(g)} y={py(0) + 13} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{g}</text>
              <text x={px(0) - 5} y={py(g) + 3} fontSize="8.5" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}
          <text x={px(max / 2)} y={W - 3} fontSize="10" fill="var(--fg-2)" textAnchor="middle">{xLabel}</text>
          <text x={10} y={py(max / 2)} fontSize="10" fill="var(--fg-2)" textAnchor="middle" transform={`rotate(-90 10 ${py(max / 2)})`}>{yLabel}</text>

          {/* fit mode: residual sticks under the points, line on top */}
          {mode === "fit" && showResiduals && fitPts.map(([x, y], i) => {
            const yHat = m * x + b;
            const miss = y - yHat;
            return (
              <line
                key={`r${i}`}
                x1={px(x)} y1={py(y)} x2={px(x)} y2={py(Math.max(min, Math.min(max, yHat)))}
                stroke={miss >= 0 ? GREEN : RED}
                strokeWidth={2}
                strokeDasharray="3 2"
                opacity={0.7}
              />
            );
          })}
          {mode === "fit" && (
            <line x1={px(min)} y1={py(md * min + bd)} x2={px(max)} y2={py(md * max + bd)} stroke={GEO_ACCENT} strokeWidth={2.6} />
          )}

          {/* the point cloud — rain-in entrance, spring morph on dataset swaps */}
          {pts.map(([x, y], i) => (
            <SpringPoint
              key={i}
              tx={x} ty={y}
              px={px} py={py}
              delay={mode === "plot" ? 0.15 + i * 0.14 : 0.05 + i * 0.05}
              color={mode === "outlier" && i === outlierIx ? RED : GEO_BLUE}
            />
          ))}
          {/* beacon on the outlier */}
          {mode === "outlier" && (
            <circle className="gm-beacon" cx={px(pts[outlierIx][0])} cy={py(pts[outlierIx][1])} r={11} fill="none" stroke={RED} strokeWidth={1.6} />
          )}
        </svg>
      </div>

      {/* readout per mode */}
      {mode === "plot" && (
        <div className="mt-2 rounded-xl p-3 text-center text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          Each dot is <b>one observation</b> — one person, one day, one game — placed at its
          ({xLabel}, {yLabel}) pair. Twelve observations, twelve dots.
        </div>
      )}

      {mode === "correlation" && (
        <>
          <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", transition: "border-color 0.35s ease" }}>
            <div className="serif text-[15px]" style={{ color: corr.color, fontWeight: 700 }}>{corr.name}</div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>{corr.blurb}</div>
          </div>
          <div className="mt-3 flex flex-wrap justify-center gap-1.5">
            {(["positive", "negative", "none"] as const).map((k) => (
              <button
                key={k}
                type="button"
                onClick={() => setDataset(k)}
                className="gm-press rounded-full px-3.5 py-1.5 text-[12px]"
                style={dataset === k
                  ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                  : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
              >
                {k === "none" ? "no pattern" : k}
              </button>
            ))}
          </div>
          <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
            swap the dataset — watch every point glide to its new story
          </div>
        </>
      )}

      {mode === "outlier" && (
        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }}>
          <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>The red point is an <b style={{ color: RED }}>outlier</b></div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            Eleven points tell one story ↗ — one point sits far from the pack. Real data has stragglers;
            spot them before you trust a trend.
          </div>
        </div>
      )}

      {mode === "fit" && (
        <>
          <div
            className="mt-2 rounded-xl p-3 text-center"
            style={{
              transition: "background 0.35s ease, border-color 0.35s ease",
              ...(nearBest
                ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)" }),
            }}
          >
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              y = {fmt(m)}x {b >= 0 ? "+" : "−"} {fmt(Math.abs(b))} · average miss: <b style={{ color: nearBest ? "var(--accent)" : "var(--fg)" }}>{avgMiss.toFixed(2)}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {nearBest
                ? <>🎯 that's the best-fit zone — no line misses these points by less.</>
                : <>the dashed sticks are the misses — steer the line to shrink them.</>}
            </div>
          </div>
          <div className="mt-3 flex items-center justify-center gap-5">
            {stepper("slope m", m, setM, -1, 2, 0.25)}
            {stepper("intercept b", b, setB, 0, 9, 0.5)}
          </div>
          <div className="mt-3 flex justify-center gap-2">
            <button
              type="button"
              onClick={() => { setM(Math.round(best.m * 100) / 100); setB(Math.round(best.b * 100) / 100); }}
              className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]"
              style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              <Sparkles className="h-3.5 w-3.5" /> Snap to best fit
            </button>
            <button
              type="button"
              onClick={() => setShowResiduals((v) => !v)}
              className="gm-press rounded-full px-4 py-2 text-[13px]"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
            >
              {showResiduals ? "Hide misses" : "Show misses"}
            </button>
          </div>
        </>
      )}
    </div>
  );
}
