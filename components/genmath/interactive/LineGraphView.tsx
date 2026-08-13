"use client";

// A line graph for the primary band. The grade-4 line-graph lesson used to
// hand a child "heights 4, 7, 11, 12, 12" and ask questions about "the
// graph" — so the one skill the lesson exists to teach, reading a plotted
// line, was never exercised. This draws it: gridlines to count, a marked
// dot per reading, and the value printed beside each dot so a young reader
// can check the axis against the number.
import type { FigureSpec } from "@/lib/genmath-interactive";

export default function LineGraphView({ spec }: { spec: NonNullable<FigureSpec["lineGraph"]> }) {
  const { points, unit } = spec;
  const color = spec.color ?? "#3b82f6";
  const step = spec.step && spec.step > 0 ? spec.step : 1;
  const dataMax = Math.max(...points.map((p) => p.value), 1);
  const max = spec.max && spec.max >= dataMax ? spec.max : Math.ceil(dataMax / step) * step;

  const W = Math.max(280, 62 * points.length + 46);
  const H = 190;
  const left = 34;
  const bottom = H - 28;
  const top = 14;
  const plotH = bottom - top;
  const slot = (W - left - 12) / Math.max(points.length - 1, 1);

  const x = (i: number) => left + slot * i;
  const y = (v: number) => bottom - (v / max) * plotH;
  const ticks: number[] = [];
  for (let v = 0; v <= max; v += step) ticks.push(v);
  const path = points.map((p, i) => `${i === 0 ? "M" : "L"} ${x(i)} ${y(p.value)}`).join(" ");

  return (
    <div className="gm-fade flex justify-center rounded-xl p-3" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <svg
        width={W}
        height={H}
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label={`Line graph: ${points.map((p) => `${p.label} ${p.value}`).join(", ")}${unit ? ` (${unit})` : ""}`}
      >
        {ticks.map((v) => (
          <g key={v}>
            <line x1={left} y1={y(v)} x2={W - 8} y2={y(v)} stroke="var(--line)" strokeWidth={v === 0 ? 1.5 : 1} strokeDasharray={v === 0 ? undefined : "3 3"} />
            <text x={left - 6} y={y(v)} textAnchor="end" dominantBaseline="central" fontSize="10" fill="var(--fg-3)">
              {v}
            </text>
          </g>
        ))}
        {unit && (
          <text x={left - 24} y={top - 4} fontSize="9" fill="var(--fg-3)">
            {unit}
          </text>
        )}
        <path d={path} fill="none" stroke={color} strokeWidth={2.5} strokeLinejoin="round" strokeLinecap="round" />
        {points.map((p, i) => (
          <g key={p.label}>
            <circle cx={x(i)} cy={y(p.value)} r={4} fill={color} stroke="var(--bg-2)" strokeWidth={1.5} />
            <text x={x(i)} y={y(p.value) - 9} textAnchor="middle" fontSize="10" fontFamily="Georgia, serif" fill="var(--fg)">
              {p.value}
            </text>
            <text x={x(i)} y={bottom + 13} textAnchor="middle" fontSize="10" fill="var(--fg-2)">
              {p.label}
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}
