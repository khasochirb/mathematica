"use client";

// A number line (default 0..1, major ticks at every tenth) with decimal points
// plotted above it. Makes "0.45 sits left of 0.5" literal, and is the natural
// tool for ordering and (later) rounding. Presentational only.
export default function DecimalNumberLineView({
  min = 0,
  max = 1,
  points,
  width = 320,
}: {
  min?: number;
  max?: number;
  points: { value: number; label?: string; color?: string }[];
  width?: number;
}) {
  const pad = 18;
  const h = 86;
  const y = 56; // baseline
  const span = max - min || 1;
  const x = (v: number) => pad + ((v - min) / span) * (width - 2 * pad);

  // Major ticks at each tenth across the range.
  const tickStep = 0.1;
  const ticks: number[] = [];
  for (let v = min; v <= max + 1e-9; v += tickStep) ticks.push(Math.round(v * 100) / 100);

  return (
    <svg
      width={width}
      height={h}
      viewBox={`0 0 ${width} ${h}`}
      role="img"
      aria-label={`Number line from ${min} to ${max} with ${points.map((p) => p.value).join(", ")} marked`}
    >
      {/* axis */}
      <line x1={pad} y1={y} x2={width - pad} y2={y} stroke="var(--fg-3)" strokeWidth="1.5" />
      {/* ticks + labels */}
      {ticks.map((t, i) => (
        <g key={i}>
          <line x1={x(t)} y1={y - 5} x2={x(t)} y2={y + 5} stroke="var(--fg-3)" strokeWidth="1" />
          <text x={x(t)} y={y + 20} textAnchor="middle" fontSize="10" fill="var(--fg-3)" fontFamily="ui-monospace, monospace">
            {t % 1 === 0 ? t.toFixed(0) : t.toFixed(1)}
          </text>
        </g>
      ))}
      {/* plotted points */}
      {points.map((p, i) => {
        const c = p.color ?? "var(--accent)";
        return (
          <g key={`p${i}`}>
            <line x1={x(p.value)} y1={y - 14} x2={x(p.value)} y2={y} stroke={c} strokeWidth="2" />
            <circle cx={x(p.value)} cy={y} r="4.5" fill={c} stroke="var(--bg)" strokeWidth="1.5" />
            <text x={x(p.value)} y={y - 19} textAnchor="middle" fontSize="11.5" fill={c} fontFamily="Georgia, serif">
              {p.label ?? p.value}
            </text>
          </g>
        );
      })}
    </svg>
  );
}
