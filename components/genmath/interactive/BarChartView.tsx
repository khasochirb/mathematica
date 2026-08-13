"use client";

// A real bar chart for the primary band's data lessons — the figure the
// bar-graph unit teaches ABOUT, finally drawn instead of narrated. Pure
// presentational SVG: theme-safe (CSS variables only), value labels on the
// bars so young readers can check their count against the axis, and an
// optional highlighted bar for "look at THIS one" questions.
import type { FigureSpec } from "@/lib/genmath-interactive";

const FALLBACK = ["#3b82f6", "#d97706", "#16a34a", "#dc2626", "#7c3aed", "#0891b2"];

export default function BarChartView({ spec }: { spec: NonNullable<FigureSpec["barChart"]> }) {
  const { categories, unit, highlight } = spec;
  const step = spec.step && spec.step > 0 ? spec.step : 1;
  const dataMax = Math.max(...categories.map((c) => c.value), 1);
  const max = spec.max && spec.max >= dataMax ? spec.max : Math.ceil(dataMax / step) * step;

  const W = Math.max(260, 64 * categories.length + 48);
  const H = 190;
  const left = 34;
  const bottom = H - 28;
  const top = 14;
  const plotH = bottom - top;
  const slot = (W - left - 8) / categories.length;
  const barW = Math.min(40, slot * 0.6);

  const y = (v: number) => bottom - (v / max) * plotH;
  const lines: number[] = [];
  for (let v = 0; v <= max; v += step) lines.push(v);

  return (
    <div className="gm-fade flex justify-center rounded-xl p-3" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <svg
        width={W}
        height={H}
        viewBox={`0 0 ${W} ${H}`}
        role="img"
        aria-label={`Bar chart: ${categories.map((c) => `${c.label} ${c.value}`).join(", ")}${unit ? ` (${unit})` : ""}`}
      >
        {/* gridlines + axis numbers — the "lines" a young reader counts to */}
        {lines.map((v) => (
          <g key={v}>
            <line x1={left} y1={y(v)} x2={W - 6} y2={y(v)} stroke="var(--line)" strokeWidth={v === 0 ? 1.5 : 1} strokeDasharray={v === 0 ? undefined : "3 3"} />
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
        {categories.map((c, i) => {
          const cx = left + slot * i + slot / 2;
          const color = c.color ?? FALLBACK[i % FALLBACK.length];
          const dim = highlight !== undefined && highlight !== i;
          return (
            <g key={c.label} opacity={dim ? 0.35 : 1}>
              <rect
                x={cx - barW / 2}
                y={y(c.value)}
                width={barW}
                height={bottom - y(c.value)}
                rx={4}
                fill={color}
                stroke="rgba(0,0,0,0.15)"
              />
              <text x={cx} y={y(c.value) - 5} textAnchor="middle" fontSize="11" fontFamily="Georgia, serif" fill="var(--fg)">
                {c.value}
              </text>
              <text x={cx} y={bottom + 13} textAnchor="middle" fontSize="10" fill="var(--fg-2)">
                {c.label}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
}
