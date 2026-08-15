"use client";

// An analogue clock face — and, when `until` is given, two faces side by
// side for an elapsed-time problem. The grade-4 measurement unit asked
// children to work out the time from 7:50 to 9:15 with no clock anywhere on
// the page; a clock question without a clock is a reading-comprehension
// question wearing a maths hat.
//
// The hour hand moves WITH the minutes (at 7:50 it sits nearly on 8, not on
// 7) because a clock that lies about that teaches the wrong reading habit.
import type { FigureSpec } from "@/lib/genmath-interactive";

const R = 46;
const CX = 54;
const CY = 54;

function pol(angleDeg: number, radius: number) {
  // 0° at 12 o'clock, clockwise
  const a = ((angleDeg - 90) * Math.PI) / 180;
  return { x: CX + radius * Math.cos(a), y: CY + radius * Math.sin(a) };
}

function Face({ hour, minute, label }: { hour: number; minute: number; label?: string }) {
  const minuteAngle = minute * 6;
  const hourAngle = ((hour % 12) + minute / 60) * 30;
  const mh = pol(minuteAngle, R * 0.78);
  const hh = pol(hourAngle, R * 0.52);
  const stamp = `${hour}:${String(minute).padStart(2, "0")}`;

  return (
    <div className="flex flex-col items-center gap-1">
      <svg width={108} height={108} viewBox="0 0 108 108" role="img" aria-label={`Clock showing ${stamp}`}>
        <circle cx={CX} cy={CY} r={R} fill="var(--bg-1)" stroke="var(--fg-3)" strokeWidth={2} />
        {Array.from({ length: 12 }).map((_, i) => {
          const outer = pol(i * 30, R - 4);
          const inner = pol(i * 30, R - 10);
          const num = pol(i * 30, R - 17);
          const n = i === 0 ? 12 : i;
          return (
            <g key={i}>
              <line x1={outer.x} y1={outer.y} x2={inner.x} y2={inner.y} stroke="var(--fg-3)" strokeWidth={1.5} />
              <text x={num.x} y={num.y} textAnchor="middle" dominantBaseline="central" fontSize="9" fill="var(--fg-2)">
                {n}
              </text>
            </g>
          );
        })}
        <line x1={CX} y1={CY} x2={hh.x} y2={hh.y} stroke="var(--fg)" strokeWidth={3.5} strokeLinecap="round" />
        <line x1={CX} y1={CY} x2={mh.x} y2={mh.y} stroke="#3b82f6" strokeWidth={2.5} strokeLinecap="round" />
        <circle cx={CX} cy={CY} r={3} fill="var(--fg)" />
      </svg>
      <span className="mono text-[11px]" style={{ color: "var(--fg-2)" }}>
        {label ?? stamp}
      </span>
    </div>
  );
}

export default function ClockFaceView({ spec }: { spec: NonNullable<FigureSpec["clockFace"]> }) {
  return (
    <div className="gm-fade flex items-center justify-center gap-5 rounded-xl p-3" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <Face hour={spec.hour} minute={spec.minute} label={spec.label} />
      {spec.until && (
        <>
          <span aria-hidden className="serif" style={{ fontSize: 22, color: "var(--fg-3)" }}>
            →
          </span>
          <Face hour={spec.until.hour} minute={spec.until.minute} label={spec.untilLabel} />
        </>
      )}
    </div>
  );
}
