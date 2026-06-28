"use client";

// A number-line jump for adding integers: start at `a`, hop `b` units (an arc
// to the right for a positive, to the left for a negative), landing at a + b.
// Presentational; shared by the interactive IntegerAdd and the integerAdd figure.
export default function IntegerAddView({
  a,
  b,
  min,
  max,
  color = "#e8913c",
  showJump,
  width = 360,
}: {
  a: number;
  b: number;
  min: number;
  max: number;
  color?: string;
  showJump: boolean;
  width?: number;
}) {
  const pad = 22;
  const h = 88;
  const y = 60;
  const span = max - min || 1;
  const x = (v: number) => pad + ((v - min) / span) * (width - 2 * pad);
  const end = a + b;
  const dense = max - min > 13;
  const BLUE = "#3b82f6";
  const jumpColor = b < 0 ? BLUE : color;

  const ticks: number[] = [];
  for (let v = min; v <= max; v++) ticks.push(v);

  // arc from a to end, bowing upward
  const x1 = x(a);
  const x2 = x(end);
  const ctrlY = y - 34;
  const arc = `M ${x1} ${y - 6} Q ${(x1 + x2) / 2} ${ctrlY} ${x2} ${y - 6}`;

  return (
    <svg width={width} height={h} viewBox={`0 0 ${width} ${h}`} role="img" aria-label={`Add ${b} to ${a} on a number line`}>
      <defs>
        <marker id="ia-axis" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto">
          <path d="M0,0 L6,3 L0,6 Z" fill="var(--fg-3)" />
        </marker>
        <marker id="ia-jump" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
          <path d="M0,0 L6,3 L0,6 Z" fill={jumpColor} />
        </marker>
      </defs>
      {/* axis */}
      <line x1={pad - 8} y1={y} x2={width - pad + 8} y2={y} stroke="var(--fg-3)" strokeWidth="1.5" markerStart="url(#ia-axis)" markerEnd="url(#ia-axis)" />
      {ticks.map((t) => {
        const zero = t === 0;
        const showLabel = zero || !dense || t % 2 === 0;
        return (
          <g key={t}>
            <line x1={x(t)} y1={y - (zero ? 8 : 4)} x2={x(t)} y2={y + (zero ? 8 : 4)} stroke={zero ? "var(--fg-1)" : "var(--fg-3)"} strokeWidth={zero ? 1.8 : 1} />
            {showLabel && (
              <text x={x(t)} y={y + 20} textAnchor="middle" fontSize="10.5" fill={zero ? "var(--fg-1)" : "var(--fg-3)"} fontFamily="ui-monospace, monospace">{t}</text>
            )}
          </g>
        );
      })}
      {/* start marker */}
      <circle cx={x(a)} cy={y} r="4.5" fill={showJump ? "var(--fg-3)" : color} stroke="var(--bg)" strokeWidth="1.5" />
      <text x={x(a)} y={y + 34} textAnchor="middle" fontSize="11.5" fill="var(--fg-2)" fontFamily="Georgia, serif">start {a}</text>
      {/* the jump */}
      {showJump && (
        <g className="gm-fade">
          {b !== 0 && <path d={arc} fill="none" stroke={jumpColor} strokeWidth="2" markerEnd="url(#ia-jump)" />}
          <text x={(x1 + x2) / 2} y={ctrlY - 5} textAnchor="middle" fontSize="12" fill={jumpColor} fontFamily="Georgia, serif">
            {b >= 0 ? `+${b}` : b}
          </text>
          <circle cx={x(end)} cy={y} r="5" fill={color} stroke="var(--bg)" strokeWidth="1.5" />
          <text x={x(end)} y={y - 12} textAnchor="middle" fontSize="13" fill={color} fontFamily="Georgia, serif">{end}</text>
        </g>
      )}
    </svg>
  );
}
