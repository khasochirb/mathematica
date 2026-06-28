"use client";

// A number line that crosses zero: integer ticks, zero emphasized, negatives to
// the left and positives to the right, with arrowheads to suggest it runs
// forever both ways. Marked points are plotted above. Presentational; shared by
// the interactive IntegerLine and the static integerLine figure.
export default function IntegerLineView({
  min,
  max,
  points,
  width = 340,
  highlightFromZero,
}: {
  min: number;
  max: number;
  points: { value: number; label?: string; color?: string }[];
  width?: number;
  highlightFromZero?: number; // draw a distance band from 0 to this value
}) {
  const pad = 20;
  const h = 70;
  const y = 44;
  const span = max - min || 1;
  const x = (v: number) => pad + ((v - min) / span) * (width - 2 * pad);
  const dense = max - min > 13; // label every other tick when crowded

  const ticks: number[] = [];
  for (let v = min; v <= max; v++) ticks.push(v);

  return (
    <svg width={width} height={h} viewBox={`0 0 ${width} ${h}`} role="img" aria-label={`Number line from ${min} to ${max}`}>
      <defs>
        <marker id="il-arrow" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto">
          <path d="M0,0 L6,3 L0,6 Z" fill="var(--fg-3)" />
        </marker>
      </defs>
      {/* axis with arrowheads both ends */}
      <line x1={pad - 8} y1={y} x2={width - pad + 8} y2={y} stroke="var(--fg-3)" strokeWidth="1.5" markerStart="url(#il-arrow)" markerEnd="url(#il-arrow)" />
      {/* distance band from zero (absolute value) */}
      {highlightFromZero !== undefined && highlightFromZero !== 0 && (
        <>
          <line x1={x(0)} y1={y} x2={x(highlightFromZero)} y2={y} stroke="var(--accent)" strokeWidth="5" strokeLinecap="round" opacity="0.55" />
          <text x={(x(0) + x(highlightFromZero)) / 2} y={y - 28} textAnchor="middle" fontSize="11" fill="var(--accent)">
            distance {Math.abs(highlightFromZero)}
          </text>
        </>
      )}
      {/* ticks + labels */}
      {ticks.map((t) => {
        const zero = t === 0;
        const showLabel = zero || !dense || t % 2 === 0;
        return (
          <g key={t}>
            <line x1={x(t)} y1={y - (zero ? 9 : 5)} x2={x(t)} y2={y + (zero ? 9 : 5)} stroke={zero ? "var(--fg-1)" : "var(--fg-3)"} strokeWidth={zero ? 1.8 : 1} />
            {showLabel && (
              <text x={x(t)} y={y + 22} textAnchor="middle" fontSize="10.5" fill={zero ? "var(--fg-1)" : "var(--fg-3)"} fontFamily="ui-monospace, monospace">
                {t}
              </text>
            )}
          </g>
        );
      })}
      {/* plotted points */}
      {points.map((p, i) => {
        const c = p.color ?? "var(--accent)";
        return (
          <g key={`p${i}`}>
            <line x1={x(p.value)} y1={y - 15} x2={x(p.value)} y2={y} stroke={c} strokeWidth="2" />
            <circle cx={x(p.value)} cy={y} r="4.5" fill={c} stroke="var(--bg)" strokeWidth="1.5" />
            <text x={x(p.value)} y={y - 20} textAnchor="middle" fontSize="12" fill={c} fontFamily="Georgia, serif">
              {p.label ?? p.value}
            </text>
          </g>
        );
      })}
    </svg>
  );
}
