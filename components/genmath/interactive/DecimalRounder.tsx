"use client";

import { useState } from "react";
import { Check, X } from "lucide-react";
import { type DecimalRounderConfig } from "@/lib/genmath-interactive";

const STEP = { whole: 1, tenth: 0.1, hundredth: 0.01 } as const;
const PLACE_LABEL = { whole: "whole number", tenth: "tenth", hundredth: "hundredth" } as const;

export default function DecimalRounder({ config }: { config: DecimalRounderConfig }) {
  const { value, place, color = "#e8913c" } = config;
  const step = STEP[place];
  const lowerUnits = Math.floor(value / step + 1e-9);
  const lower = lowerUnits * step;
  const upper = lower + step;
  const mid = lower + step / 2;
  const roundsUp = value - lower >= step / 2 - 1e-9;
  const answer = roundsUp ? upper : lower;

  const dec = place === "whole" ? 0 : place === "tenth" ? 1 : 2;
  const fmtP = (x: number) => x.toFixed(dec);
  const fmtV = (x: number) => x.toFixed(3).replace(/0+$/, "").replace(/\.$/, "");

  const [picked, setPicked] = useState<number | null>(null);
  const done = picked !== null;
  const correct = picked === answer;

  // zoomed number line: lower → upper
  const W = 300;
  const pad = 26;
  const yb = 46;
  const px = (v: number) => pad + ((v - lower) / (upper - lower)) * (W - 2 * pad);

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Round <b className="serif tabular" style={{ color: "var(--fg)" }}>{fmtV(value)}</b> to the nearest {PLACE_LABEL[place]}
      </div>

      <div className="mt-1 flex justify-center">
        <svg width={W} height="74" viewBox={`0 0 ${W} 74`} role="img" aria-label={`Number line from ${fmtP(lower)} to ${fmtP(upper)} with ${fmtV(value)} marked`}>
          {/* axis */}
          <line x1={pad} y1={yb} x2={W - pad} y2={yb} stroke="var(--fg-3)" strokeWidth="1.5" />
          {/* endpoint ticks */}
          {[lower, upper].map((t, i) => (
            <g key={i}>
              <line x1={px(t)} y1={yb - 6} x2={px(t)} y2={yb + 6} stroke="var(--fg-2)" strokeWidth="1.5" />
              <text x={px(t)} y={yb + 22} textAnchor="middle" fontSize="13" fill="var(--fg-1)" fontFamily="Georgia, serif">{fmtP(t)}</text>
            </g>
          ))}
          {/* midpoint (halfway) */}
          <line x1={px(mid)} y1={yb - 7} x2={px(mid)} y2={yb + 7} stroke="var(--fg-3)" strokeWidth="1" strokeDasharray="3 3" />
          <text x={px(mid)} y={yb - 12} textAnchor="middle" fontSize="9" fill="var(--fg-3)">halfway</text>
          {/* the value */}
          <line x1={px(value)} y1={yb - 16} x2={px(value)} y2={yb} stroke={color} strokeWidth="2.5" />
          <circle cx={px(value)} cy={yb} r="5" fill={color} stroke="var(--bg)" strokeWidth="1.5" />
          <text x={px(value)} y={yb - 21} textAnchor="middle" fontSize="12" fill={color} fontFamily="Georgia, serif">{fmtV(value)}</text>
        </svg>
      </div>

      {/* tap the nearer mark */}
      <div className="mt-2 flex items-center justify-center gap-3">
        {[lower, upper].map((t) => {
          const isPick = picked === t;
          const reveal = done && t === answer;
          const wrongPick = done && isPick && t !== answer;
          return (
            <button
              key={t}
              type="button"
              onClick={() => !done && setPicked(t)}
              disabled={done}
              className="gm-press rounded-xl px-5 py-2.5 serif tabular"
              style={{
                fontSize: 18,
                background: reveal ? "var(--accent-wash)" : wrongPick ? "rgba(220,80,80,0.12)" : "var(--bg-2)",
                border: `1px solid ${reveal ? "var(--accent-line)" : wrongPick ? "rgba(220,80,80,0.5)" : "var(--line)"}`,
                color: reveal ? "var(--accent)" : wrongPick ? "rgb(200,60,60)" : "var(--fg)",
                opacity: done && !reveal && !wrongPick ? 0.45 : 1,
              }}
            >
              {fmtP(t)}
            </button>
          );
        })}
      </div>

      {done ? (
        <div className="gm-fade mt-3 flex items-center justify-center gap-2 text-center text-[13.5px]" style={{ color: "var(--fg-1)" }}>
          {correct ? <Check className="h-4 w-4" style={{ color: "var(--accent)" }} /> : <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />}
          <span>
            <b className="serif tabular">{fmtV(value)} → {fmtP(answer)}</b>
            {" — "}
            {roundsUp ? `at or past halfway, so round up.` : `before halfway, so round down.`}
          </span>
        </div>
      ) : (
        <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          Tap the mark it is closer to.
        </div>
      )}
    </div>
  );
}
