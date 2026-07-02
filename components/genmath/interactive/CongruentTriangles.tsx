"use client";

import { useState } from "react";
import { Check, X } from "lucide-react";
import { Ticks, arcPath, GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { type CongruentTrianglesConfig } from "@/lib/genmath-interactive";

// Two congruent triangles side by side, with the GIVEN parts marked: tick marks
// for congruent sides, arc marks for congruent angles, and a small square for a
// right angle. The student picks which shortcut (SSS / SAS / ASA / AAS / HL)
// the marks justify — the wrong picks (AAA, SSA) are baked into the options so
// the classic traps get named.
const W = 320;
const H = 190;

// a fixed scalene template, drawn twice; vertices returned in screen coords
function template(offsetX: number) {
  return {
    A: { x: offsetX + 20, y: 150 }, // bottom-left
    B: { x: offsetX + 120, y: 150 }, // bottom-right
    C: { x: offsetX + 78, y: 45 }, // apex
  };
}

const SHORTCUTS = ["SSS", "SAS", "ASA", "AAS", "HL", "AAA", "SSA"] as const;

export default function CongruentTriangles({ config }: { config: CongruentTrianglesConfig }) {
  const { sides = [0, 0, 0], angles = [0, 0, 0], rightAngleAt = -1, answer, caption } = config;
  const [pick, setPick] = useState<string | null>(null);

  const left = template(0);
  const right = template(160);

  const renderTri = (v: ReturnType<typeof template>, keyPrefix: string) => {
    const verts = [v.A, v.B, v.C];
    const sidePairs: [number, number][] = [[0, 1], [1, 2], [2, 0]]; // AB, BC, CA
    return (
      <g key={keyPrefix}>
        <polygon points={verts.map((p) => `${p.x},${p.y}`).join(" ")} fill={`${GEO_ACCENT}10`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* side tick marks */}
        {sidePairs.map(([i, j], k) =>
          sides[k] > 0 ? <Ticks key={`s${k}`} x1={verts[i].x} y1={verts[i].y} x2={verts[j].x} y2={verts[j].y} count={sides[k]} color={GEO_ACCENT} /> : null
        )}
        {/* angle arcs */}
        {verts.map((vp, k) => {
          if (angles[k] <= 0) return null;
          const others = [0, 1, 2].filter((x) => x !== k);
          const a1 = (Math.atan2(verts[others[0]].y - vp.y, verts[others[0]].x - vp.x) * 180) / Math.PI;
          const a2 = (Math.atan2(verts[others[1]].y - vp.y, verts[others[1]].x - vp.x) * 180) / Math.PI;
          return (
            <g key={`a${k}`}>
              {Array.from({ length: angles[k] }).map((_, m) => (
                <path key={m} d={arcPath(vp.x, vp.y, 13 + m * 4, a1, a2)} fill="none" stroke="#5b8def" strokeWidth={1.8} />
              ))}
            </g>
          );
        })}
        {/* right-angle square */}
        {rightAngleAt >= 0 && (() => {
          const vp = verts[rightAngleAt];
          const others = [0, 1, 2].filter((x) => x !== rightAngleAt);
          const u1 = norm(verts[others[0]], vp);
          const u2 = norm(verts[others[1]], vp);
          const s = 12;
          return <path d={`M ${vp.x + u1.x * s} ${vp.y + u1.y * s} L ${vp.x + (u1.x + u2.x) * s} ${vp.y + (u1.y + u2.y) * s} L ${vp.x + u2.x * s} ${vp.y + u2.y * s}`} fill="none" stroke="var(--fg-2)" strokeWidth={1.5} />;
        })()}
      </g>
    );
  };

  function norm(to: { x: number; y: number }, from: { x: number; y: number }) {
    const dx = to.x - from.x, dy = to.y - from.y;
    const L = Math.hypot(dx, dy) || 1;
    return { x: dx / L, y: dy / L };
  }

  const correct = pick === answer;
  const wrong = pick !== null && pick !== answer;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {renderTri(left, "L")}
        {renderTri(right, "R")}
      </svg>

      {caption && (
        <div className="mt-1 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>{caption}</div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Which shortcut do the marks give?
      </div>
      <div className="mt-2 flex flex-wrap justify-center gap-1.5">
        {SHORTCUTS.map((s) => {
          const isPick = pick === s;
          const style = isPick
            ? s === answer
              ? { background: "rgba(80,160,90,0.15)", border: "1px solid rgba(80,160,90,0.6)", color: "var(--fg)" }
              : { background: "rgba(200,60,60,0.12)", border: "1px solid rgb(200,60,60)", color: "var(--fg)" }
            : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" };
          return (
            <button key={s} type="button" onClick={() => setPick(s)} className="gm-press rounded-full px-3.5 py-1.5 text-[13px]" style={style}>
              {s}
            </button>
          );
        })}
      </div>

      {pick && (
        <div className="mt-3 rounded-xl p-3 text-center text-[14px]" style={correct ? { background: "rgba(80,160,90,0.1)", border: "1px solid rgba(80,160,90,0.5)" } : { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }}>
          <span className="inline-flex items-center gap-1.5" style={{ color: "var(--fg)" }}>
            {correct ? <Check className="h-4 w-4" style={{ color: "rgb(70,150,80)" }} /> : <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />}
            {correct ? <b>{answer} — the triangles are congruent.</b> : <span>Not {pick}. Look again at which parts are marked.</span>}
          </span>
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Matching <b style={{ color: GEO_ACCENT }}>tick marks</b> = congruent sides; matching <b style={{ color: "#5b8def" }}>arcs</b> = congruent angles.
      </div>
    </div>
  );
}
