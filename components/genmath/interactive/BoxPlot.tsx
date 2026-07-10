"use client";

import { useMemo, useState } from "react";
import { GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { fencesOf, quartilesOf, type BoxPlotConfig } from "@/lib/genmath-interactive";

// A boxplot computed live from its data, with the raw values dotted above so
// the summary stays connected to what it summarizes. Chips light up each of
// the five numbers; the fences toggle draws the 1.5 × IQR lines and flags
// everything outside them in red.

const RED = "rgb(200,60,60)";

function fmt(n: number): string {
  const r = Math.round(n * 100) / 100;
  return Number.isInteger(r) ? r.toString() : r.toFixed(2);
}

type Part = "min" | "q1" | "median" | "q3" | "max" | "iqr" | null;

export default function BoxPlot({ config }: { config: BoxPlotConfig }) {
  const { data, xLabel = "value", showFences = false } = config;
  const [part, setPart] = useState<Part>(null);
  const [fences, setFences] = useState(showFences);

  const S = useMemo(() => {
    const sorted = [...data].sort((a, b) => a - b);
    const { q1, q2, q3 } = quartilesOf(sorted);
    const f = fencesOf(sorted);
    const outliers = sorted.filter((x) => x < f.lower || x > f.upper);
    const inside = sorted.filter((x) => x >= f.lower && x <= f.upper);
    // whiskers reach the farthest values still inside the fences
    const wLo = inside[0] ?? sorted[0];
    const wHi = inside[inside.length - 1] ?? sorted[sorted.length - 1];
    return { sorted, q1, q2, q3, iqr: q3 - q1, f, outliers, wLo, wHi };
  }, [data]);

  const lo = Math.min(S.sorted[0], fences ? S.f.lower : Infinity);
  const hi = Math.max(S.sorted[S.sorted.length - 1], fences ? S.f.upper : -Infinity);
  const pad = (hi - lo) * 0.07 + 0.5;

  const W = 360;
  const H = 200;
  const padL = 18;
  const padR = 18;
  const axisY = H - 34;
  const boxTop = 92;
  const boxBot = 148;
  const boxMid = (boxTop + boxBot) / 2;
  const px = (x: number) => padL + ((x - (lo - pad)) / (hi + pad - (lo - pad))) * (W - padL - padR);

  // stack the raw dots
  const stacks = useMemo(() => {
    const seen = new Map<number, number>();
    return S.sorted.map((v) => {
      const s = seen.get(v) ?? 0;
      seen.set(v, s + 1);
      return s;
    });
  }, [S.sorted]);

  const chips: { key: Part & string; label: string; value: number }[] = [
    { key: "min", label: "min", value: S.sorted[0] },
    { key: "q1", label: "Q1", value: S.q1 },
    { key: "median", label: "median", value: S.q2 },
    { key: "q3", label: "Q3", value: S.q3 },
    { key: "max", label: "max", value: S.sorted[S.sorted.length - 1] },
    { key: "iqr", label: "IQR", value: S.iqr },
  ];

  const hotX: Record<string, number | [number, number]> = {
    min: S.sorted[0],
    q1: S.q1,
    median: S.q2,
    q3: S.q3,
    max: S.sorted[S.sorted.length - 1],
    iqr: [S.q1, S.q3],
  };

  const ticks = useMemo(() => {
    const span = hi + pad - (lo - pad);
    const step = span > 40 ? 10 : span > 20 ? 5 : span > 10 ? 2 : 1;
    const first = Math.ceil((lo - pad) / step) * step;
    const t: number[] = [];
    for (let x = first; x <= hi + pad; x += step) t.push(x);
    return t;
  }, [lo, hi, pad]);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 400 }} role="img" aria-label="Boxplot">
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

          {/* raw data strip */}
          {S.sorted.map((v, i) => {
            const out = v < S.f.lower || v > S.f.upper;
            return (
              <circle
                key={i}
                cx={px(v)}
                cy={64 - stacks[i] * 11}
                r={4.5}
                fill={fences && out ? RED : GEO_BLUE}
                fillOpacity={0.75}
                stroke="var(--bg-1)"
                strokeWidth={1}
              />
            );
          })}
          {fences && S.outliers.length > 0 && (
            <circle className="gm-beacon" cx={px(S.outliers[S.outliers.length - 1])} cy={64 - (stacks[S.sorted.indexOf(S.outliers[S.outliers.length - 1])] ?? 0) * 11} r={10} fill="none" stroke={RED} strokeWidth={1.4} />
          )}

          {/* IQR highlight wash */}
          {part === "iqr" && <rect x={px(S.q1)} y={boxTop - 6} width={px(S.q3) - px(S.q1)} height={boxBot - boxTop + 12} fill="var(--accent-wash)" rx={6} />}

          {/* whiskers (to the farthest non-flagged values) */}
          <line x1={px(fences ? S.wLo : S.sorted[0])} y1={boxMid} x2={px(S.q1)} y2={boxMid} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={px(S.q3)} y1={boxMid} x2={px(fences ? S.wHi : S.sorted[S.sorted.length - 1])} y2={boxMid} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={px(fences ? S.wLo : S.sorted[0])} y1={boxMid - 10} x2={px(fences ? S.wLo : S.sorted[0])} y2={boxMid + 10} stroke="var(--fg-2)" strokeWidth={1.6} />
          <line x1={px(fences ? S.wHi : S.sorted[S.sorted.length - 1])} y1={boxMid - 10} x2={px(fences ? S.wHi : S.sorted[S.sorted.length - 1])} y2={boxMid + 10} stroke="var(--fg-2)" strokeWidth={1.6} />

          {/* the box */}
          <rect x={px(S.q1)} y={boxTop} width={px(S.q3) - px(S.q1)} height={boxBot - boxTop} rx={4} fill={GEO_BLUE} fillOpacity={0.18} stroke={GEO_BLUE} strokeWidth={1.8} />
          <line x1={px(S.q2)} y1={boxTop} x2={px(S.q2)} y2={boxBot} stroke={GEO_BLUE} strokeWidth={2.4} />

          {/* fences */}
          {fences &&
            [S.f.lower, S.f.upper].map((x, i) => (
              <g key={i}>
                <line x1={px(x)} y1={30} x2={px(x)} y2={axisY} stroke={RED} strokeWidth={1.4} strokeDasharray="5 4" />
                <text x={px(x)} y={24} fontSize="8.5" fill={RED} textAnchor="middle" className="tabular">
                  {fmt(x)}
                </text>
              </g>
            ))}

          {/* flagged outliers on the plot line */}
          {fences &&
            S.outliers.map((v, i) => <circle key={`o${i}`} cx={px(v)} cy={boxMid} r={4.5} fill={RED} stroke="var(--bg-1)" strokeWidth={1} />)}

          {/* highlight marker for the picked part */}
          {part && part !== "iqr" && (
            <g className="gm-pop">
              <line x1={px(hotX[part] as number)} y1={boxTop - 8} x2={px(hotX[part] as number)} y2={boxBot + 8} stroke="var(--accent)" strokeWidth={2} strokeDasharray="4 3" />
            </g>
          )}
        </svg>
      </div>

      {/* readout */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {part ? (
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            {chips.find((c) => c.key === part)?.label} ={" "}
            <b style={{ color: "var(--accent)" }}>{fmt(chips.find((c) => c.key === part)!.value)}</b>
            {part === "iqr" && (
              <span className="ml-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
                = Q3 − Q1 = {fmt(S.q3)} − {fmt(S.q1)} — the box's width
              </span>
            )}
          </div>
        ) : fences ? (
          <div className="serif tabular text-[14px]" style={{ color: "var(--fg)" }}>
            fences at Q1 − 1.5·IQR = {fmt(S.f.lower)} and Q3 + 1.5·IQR = {fmt(S.f.upper)}
            {S.outliers.length > 0 ? (
              <span style={{ color: RED }}> — {S.outliers.map(fmt).join(", ")} flagged</span>
            ) : (
              <span style={{ color: "var(--fg-2)" }}> — nothing flagged</span>
            )}
          </div>
        ) : (
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            five numbers summarize {data.length} values — pick one, or draw the fences
          </div>
        )}
      </div>

      <div className="mt-3 flex flex-wrap justify-center gap-1.5">
        {chips.map((c) => (
          <button
            key={c.key}
            type="button"
            onClick={() => setPart(part === c.key ? null : c.key)}
            className="gm-press rounded-full px-3 py-1.5 text-[12px]"
            style={
              part === c.key
                ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
            }
          >
            {c.label}
          </button>
        ))}
        <button
          type="button"
          onClick={() => setFences((v) => !v)}
          className="gm-press rounded-full px-3 py-1.5 text-[12px]"
          style={
            fences
              ? { background: "rgba(200,60,60,0.12)", border: `1px solid ${RED}`, color: RED }
              : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
          }
        >
          {fences ? "hide fences" : "show fences"}
        </button>
      </div>
    </div>
  );
}
