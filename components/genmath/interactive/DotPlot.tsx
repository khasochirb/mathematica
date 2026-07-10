"use client";

import { useMemo, useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { meanOf, medianOf, stdevPop, type DotPlotConfig } from "@/lib/genmath-interactive";

// A dot plot on a number line, two ways:
//   meanMedian — steppers drag the biggest value away from the pack; the
//                mean's balance triangle chases it while the median post
//                doesn't budge. Robustness, played out.
//   deviations — sticks from the mean to each dot; their typical length is
//                the standard deviation.

const GREEN = "#3fa06a";
const RED = "rgb(200,60,60)";

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return Number.isInteger(r) ? r.toString() : r.toFixed(2);
}

export default function DotPlot({ config }: { config: DotPlotConfig }) {
  const { mode, data: data0, min, max, xLabel = "value" } = config;
  // meanMedian: the largest starting value is the one the steppers move
  const moveIx = useMemo(() => data0.indexOf(Math.max(...data0)), [data0]);
  const [moved, setMoved] = useState(data0[moveIx]);
  const [pick, setPick] = useState<number | null>(null);

  const data = mode === "meanMedian" ? data0.map((v, i) => (i === moveIx ? moved : v)) : data0;
  const mu = meanOf(data);
  const med = medianOf(data);
  const sd = stdevPop(data);
  const muA = useAnimatedValue(mu, { stiffness: 120, damping: 18 });
  const medA = useAnimatedValue(med, { stiffness: 120, damping: 18 });

  const W = 360;
  const H = mode === "deviations" ? 210 : 190;
  const padL = 20;
  const padR = 20;
  const axisY = H - 44;
  const px = (x: number) => padL + ((x - min) / (max - min)) * (W - padL - padR);

  // stack dots occupying the same value
  const stacks = useMemo(() => {
    const seen = new Map<number, number>();
    return data.map((v) => {
      const s = seen.get(v) ?? 0;
      seen.set(v, s + 1);
      return s;
    });
  }, [data]);

  const r = 6.5;
  const dotY = (stack: number) => axisY - 10 - stack * (r * 2 + 2);

  const ticks = useMemo(() => {
    const span = max - min;
    const step = span > 24 ? 5 : span > 12 ? 2 : 1;
    const t: number[] = [];
    for (let x = min; x <= max; x += step) t.push(x);
    return t;
  }, [min, max]);

  const pulled = mode === "meanMedian" && moved - data0[moveIx] >= 3;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Dot plot">
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

          {/* mean line for deviations mode */}
          {mode === "deviations" && (
            <line x1={px(mu)} y1={22} x2={px(mu)} y2={axisY} stroke="var(--accent)" strokeWidth={1.4} strokeDasharray="4 3" />
          )}

          {/* deviation sticks under their dots */}
          {mode === "deviations" &&
            data.map((v, i) => (
              <line
                key={`d${i}`}
                x1={px(mu)}
                y1={dotY(stacks[i])}
                x2={px(v)}
                y2={dotY(stacks[i])}
                stroke={v >= mu ? GREEN : RED}
                strokeWidth={2}
                strokeDasharray="3 2"
                opacity={pick === null || pick === i ? 0.75 : 0.2}
              />
            ))}

          {/* dots */}
          {data.map((v, i) => {
            const movable = mode === "meanMedian" && i === moveIx;
            const hot = pick === i;
            return (
              <circle
                key={i}
                cx={px(v)}
                cy={dotY(stacks[i])}
                r={r}
                fill={movable ? "var(--accent)" : hot ? "var(--accent)" : GEO_BLUE}
                fillOpacity={0.85}
                stroke="var(--bg-1)"
                strokeWidth={1}
                style={mode === "deviations" ? { cursor: "pointer" } : undefined}
                onClick={mode === "deviations" ? () => setPick(hot ? null : i) : undefined}
              />
            );
          })}

          {/* mean triangle + median post */}
          <g>
            <path d={`M${px(muA)},${axisY + 2} l -7,12 l 14,0 Z`} fill="var(--accent)" />
            <text x={px(muA)} y={axisY + 26} fontSize="9.5" fill="var(--accent)" textAnchor="middle" className="tabular" fontWeight={700}>
              mean {fmt(mu)}
            </text>
          </g>
          {mode === "meanMedian" && (
            <g>
              <line x1={px(medA)} y1={axisY - 2} x2={px(medA)} y2={26} stroke={GEO_BLUE} strokeWidth={2} />
              <text x={px(medA)} y={18} fontSize="9.5" fill={GEO_BLUE} textAnchor="middle" className="tabular" fontWeight={700}>
                median {fmt(med)}
              </text>
            </g>
          )}
        </svg>
      </div>

      {/* readout */}
      <div
        className="mt-2 rounded-xl p-3 text-center"
        style={{
          transition: "background 0.35s ease, border-color 0.35s ease",
          ...(pulled
            ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
            : { background: "var(--bg-2)", border: "1px solid var(--line)" }),
        }}
      >
        {mode === "meanMedian" ? (
          <>
            <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
              mean = <b style={{ color: "var(--accent)" }}>{fmt(mu)}</b> · median ={" "}
              <b style={{ color: GEO_BLUE }}>{fmt(med)}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              {pulled
                ? "one wild value dragged the mean — the median never moved"
                : "push the movable dot right and watch which summary follows"}
            </div>
          </>
        ) : pick !== null ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            deviation: {data[pick]} − {fmt(mu)} ={" "}
            <b style={{ color: data[pick] >= mu ? GREEN : RED }}>{fmt(data[pick] - mu)}</b>
          </div>
        ) : (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            σ = <b style={{ color: "var(--accent)" }}>{fmt(sd)}</b>
            <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              — the typical stick length; tap a dot for its deviation
            </span>
          </div>
        )}
      </div>

      {mode === "meanMedian" && (
        <div className="mt-3 flex items-center justify-center gap-2">
          <button
            type="button"
            onClick={() => setMoved((v) => Math.max(data0[moveIx], v - 1))}
            disabled={moved <= data0[moveIx]}
            aria-label="Pull the dot back"
            className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
          >
            <Minus className="h-4 w-4" />
          </button>
          <div className="text-[12px]" style={{ color: "var(--fg-2)", minWidth: 110, textAlign: "center" }}>
            movable dot at <b className="tabular" style={{ color: "var(--accent)" }}>{moved}</b>
          </div>
          <button
            type="button"
            onClick={() => setMoved((v) => Math.min(max, v + 1))}
            disabled={moved >= max}
            aria-label="Pull the dot right"
            className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35"
            style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
          >
            <Plus className="h-4 w-4" />
          </button>
        </div>
      )}
    </div>
  );
}
