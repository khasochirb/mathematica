"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { PointDot, GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { rulerLength } from "@/lib/geo";
import { type SegmentRulerConfig } from "@/lib/genmath-interactive";

// A fixed segment above a ruler you slide underneath it. The endpoint readings
// change with every slide — but their difference (the length) never does.
// That's the Ruler Postulate made physical.
export default function SegmentRuler({ config }: { config: SegmentRulerConfig }) {
  const { length, max, start = 0, color = GEO_ACCENT } = config;
  const [r, setR] = useState(Math.min(Math.max(start, 0), max - length));

  const a = r;
  const b = r + length;
  const len = rulerLength(a, b);

  const W = 320;
  const x0 = 26;
  const x1 = W - 26;
  const unit = (x1 - x0) / max;
  // the segment stays visually fixed; the RULER numbers shift underneath it.
  // Segment occupies positions [r, r+length] on the ruler — draw the segment
  // fixed in the middle and slide the number labels instead.
  const segL = x0 + ((x1 - x0) * (max - length)) / (2 * max); // fixed left end (centered)
  const segR = segL + unit * length;
  // ruler tick i (value i) sits so that value a aligns with segL:
  const tickX = (i: number) => segL + (i - a) * unit;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} 150`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* the segment (fixed) */}
        <line x1={segL} y1={52} x2={segR} y2={52} stroke={color} strokeWidth={3.4} />
        <PointDot x={segL} y={52} label="A" />
        <PointDot x={segR} y={52} label="B" />
        {/* guides down to the ruler */}
        <line x1={segL} y1={52} x2={segL} y2={96} stroke={color} strokeWidth={1.2} strokeDasharray="3 3" />
        <line x1={segR} y1={52} x2={segR} y2={96} stroke={color} strokeWidth={1.2} strokeDasharray="3 3" />
        {/* the ruler (numbers slide) */}
        <rect x={8} y={96} width={W - 16} height={38} rx={6} fill="var(--bg-2)" stroke="var(--line)" />
        {Array.from({ length: max + 1 }).map((_, i) => {
          const x = tickX(i);
          if (x < 14 || x > W - 14) return null;
          const reading = i === a || i === b;
          return (
            <g key={i}>
              <line x1={x} y1={96} x2={x} y2={reading ? 112 : 106} stroke={reading ? color : "var(--fg-3)"} strokeWidth={reading ? 2 : 1} />
              <text x={x} y={127} fontSize="11" textAnchor="middle" fill={reading ? color : "var(--fg-2)"} fontWeight={reading ? 700 : 400}>
                {i}
              </text>
            </g>
          );
        })}
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">
          AB = |{b} − {a}| = <b style={{ color: "var(--accent)" }}>{len}</b>
        </span>
      </div>

      <div className="mt-3 flex items-center justify-center gap-3">
        <button
          type="button"
          onClick={() => setR((v) => Math.max(0, v - 1))}
          disabled={r <= 0}
          aria-label="Slide ruler left"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <Minus className="h-4 w-4" />
        </button>
        <div className="text-center" style={{ minWidth: 110 }}>
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>slide the ruler</div>
          <div className="serif tabular" style={{ fontSize: 15, color: "var(--fg)" }}>A reads {a}</div>
        </div>
        <button
          type="button"
          onClick={() => setR((v) => Math.min(max - length, v + 1))}
          disabled={r >= max - length}
          aria-label="Slide ruler right"
          className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        The readings change; the <b style={{ color: "var(--fg-1)" }}>difference</b> — the length — never does.
      </div>
    </div>
  );
}
