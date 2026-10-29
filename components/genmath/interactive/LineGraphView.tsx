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
  // Extra lines over the same x labels (two plans whose costs meet). With
  // more than one line, the per-dot values are dropped so the plot stays
  // readable, and a legend names each line instead.
  const extra = (spec.series ?? []).map((s, k) => ({
    ...s,
    color: s.color ?? ["#f97316", "#10b981", "#a855f7"][k % 3],
  }));
  const multi = extra.length > 0;
  const dataMax = Math.max(...points.map((p) => p.value), ...extra.flatMap((s) => s.values), 1);
  const max = spec.max && spec.max >= dataMax ? spec.max : Math.ceil(dataMax / step) * step;

  const W = Math.max(280, 62 * points.length + 46);
  const H = multi ? 230 : 190;
  const left = 34;
  const bottom = H - (multi ? 44 : 28);
  const top = 14;
  const plotH = bottom - top;
  const slot = (W - left - 12) / Math.max(points.length - 1, 1);

  const x = (i: number) => left + slot * i;
  const y = (v: number) => bottom - (v / max) * plotH;
  const ticks: number[] = [];
  for (let v = 0; v <= max; v += step) ticks.push(v);
  const path = points.map((p, i) => `${i === 0 ? "M" : "L"} ${x(i)} ${y(p.value)}`).join(" ");
  const pathOf = (vals: number[]) => vals.map((v, i) => `${i === 0 ? "M" : "L"} ${x(i)} ${y(v)}`).join(" ");
  const legend = multi ? [{ label: spec.seriesLabel ?? "", color }, ...extra.map((s) => ({ label: s.label, color: s.color }))] : [];

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
        {spec.xLabel && (
          <text x={W - 8} y={bottom + 26} textAnchor="end" fontSize="10" fill="var(--fg-3)">
            {spec.xLabel}
          </text>
        )}
        {spec.markAt !== undefined && spec.markAt >= 0 && spec.markAt < points.length && (
          <line x1={x(spec.markAt)} y1={top} x2={x(spec.markAt)} y2={bottom} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="4 3" />
        )}
        <path d={path} fill="none" stroke={color} strokeWidth={2.5} strokeLinejoin="round" strokeLinecap="round" />
        {extra.map((s) => (
          <g key={s.label}>
            <path d={pathOf(s.values)} fill="none" stroke={s.color} strokeWidth={2.5} strokeLinejoin="round" strokeLinecap="round" />
            {s.values.map((v, i) => (
              <circle key={i} cx={x(i)} cy={y(v)} r={3.5} fill={s.color} stroke="var(--bg-2)" strokeWidth={1.5} />
            ))}
          </g>
        ))}
        {legend.map((l, k) => (
          <g key={k} transform={`translate(${left + k * 120}, ${H - 2})`}>
            <rect x={0} y={-8} width={14} height={4} rx={2} fill={l.color} />
            <text x={20} y={-4} fontSize="10" fill="var(--fg-2)" dominantBaseline="central">
              {l.label}
            </text>
          </g>
        ))}
        {points.map((p, i) => (
          <g key={p.label}>
            <circle cx={x(i)} cy={y(p.value)} r={4} fill={color} stroke="var(--bg-2)" strokeWidth={1.5} />
            {!multi && (
              <text x={x(i)} y={y(p.value) - 9} textAnchor="middle" fontSize="10" fontFamily="Georgia, serif" fill="var(--fg)">
                {p.value}
              </text>
            )}
            <text x={x(i)} y={bottom + 13} textAnchor="middle" fontSize="10" fill="var(--fg-2)">
              {p.label}
            </text>
          </g>
        ))}
      </svg>
    </div>
  );
}
