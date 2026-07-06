"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type VectorGraphConfig } from "@/lib/genmath-interactive";

// The vectors workbench — three modes:
//  components: one arrow ⟨x, y⟩ with steppers on both components. Dashed
//              right-triangle legs show the walk-east/walk-north reading and
//              the magnitude readout runs the Pythagorean theorem live.
//  add:        u = ⟨3, 1⟩ fixed; v adjustable and drawn TIP-TO-TAIL from u's
//              head. The resultant u + v springs from the origin — addition
//              as a two-leg journey collapsed to one.
//  dot:        u = ⟨2, 3⟩ fixed; v adjustable. The dot product u·v is
//              computed term by term, and its SIGN calls the angle: positive
//              acute, zero perpendicular (beacon), negative obtuse.

const RED = "rgb(200,60,60)";

function fmt(n: number, dp = 2): string {
  return (Math.round(n * 10 ** dp) / 10 ** dp).toString();
}

export default function VectorGraph({ config }: { config: VectorGraphConfig }) {
  const { mode } = config;

  const [vx, setVx] = useState(mode === "components" ? 3 : mode === "add" ? 1 : 3);
  const [vy, setVy] = useState(mode === "components" ? 4 : mode === "add" ? 3 : 1);

  const vxd = useAnimatedValue(vx, { stiffness: 120, damping: 18 });
  const vyd = useAnimatedValue(vy, { stiffness: 120, damping: 18 });

  const U = mode === "add" ? { x: 3, y: 1 } : { x: 2, y: 3 }; // fixed partner vector

  // grid geometry — centered origin
  const W = 320;
  const H = 300;
  const padL = 26, padR = 12, padT = 12, padB = 22;
  const R = 5.2;
  const px = (x: number) => padL + ((x + R) / (2 * R)) * (W - padL - padR);
  const py = (y: number) => (H - padB) - ((y + R) / (2 * R)) * (H - padB - padT);

  // arrow with a manual head
  const arrow = (x0: number, y0: number, x1: number, y1: number, color: string, w = 2.6, dash?: string, cls?: string) => {
    const dx = px(x1) - px(x0);
    const dy = py(y1) - py(y0);
    const len = Math.hypot(dx, dy) || 1;
    const ux = dx / len, uy = dy / len;
    const hx = px(x1) - ux * 9, hy = py(y1) - uy * 9;
    return (
      <g className={cls}>
        <line x1={px(x0)} y1={py(y0)} x2={hx} y2={hy} stroke={color} strokeWidth={w} strokeDasharray={dash} strokeLinecap="round" />
        <polygon
          points={`${px(x1)},${py(y1)} ${hx - uy * 4.5},${hy + ux * 4.5} ${hx + uy * 4.5},${hy - ux * 4.5}`}
          fill={color}
        />
      </g>
    );
  };

  const mag = Math.hypot(vx, vy);
  const dot = U.x * vx + U.y * vy;
  const sum = { x: U.x + vx, y: U.y + vy };

  const stepper = (label: string, val: number, set: (f: (v: number) => number) => void, color: string) => (
    <div className="text-center">
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>{label}</div>
      <div className="mt-1 flex items-center gap-2">
        <button type="button" onClick={() => set((v) => Math.max(-4, v - 1))} disabled={val <= -4} aria-label={`Decrease ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 34, fontSize: 16, color }}>{val}</div>
        <button type="button" onClick={() => set((v) => Math.min(4, v + 1))} disabled={val >= 4} aria-label={`Increase ${label}`} className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );

  const eqnText =
    mode === "components" ? `v = ⟨${vx}, ${vy}⟩` :
    mode === "add" ? `u = ⟨3, 1⟩,  v = ⟨${vx}, ${vy}⟩` :
    `u = ⟨2, 3⟩ · v = ⟨${vx}, ${vy}⟩`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Vectors as arrows on a grid">
          {Array.from({ length: 11 }, (_, i) => i - 5).map((g) => (
            <g key={g}>
              <line x1={px(g)} y1={py(-R)} x2={px(g)} y2={py(R)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(-R)} y1={py(g)} x2={px(R)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          <line x1={px(-R)} y1={py(0)} x2={px(R)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(-R)} x2={px(0)} y2={py(R)} stroke="var(--fg-2)" strokeWidth={1.8} />
          {[-4, -2, 2, 4].map((g) => (
            <text key={`x${g}`} x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
          ))}
          {[-4, -2, 2, 4].map((g) => (
            <text key={`y${g}`} x={px(0) - 5} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
          ))}

          {/* components mode: dashed legs + the arrow */}
          {mode === "components" && (
            <>
              <line x1={px(0)} y1={py(0)} x2={px(vxd)} y2={py(0)} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="4 3" />
              <line x1={px(vxd)} y1={py(0)} x2={px(vxd)} y2={py(vyd)} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="4 3" />
              {arrow(0, 0, vxd, vyd, GEO_ACCENT)}
            </>
          )}

          {/* add mode: u from origin, v tip-to-tail, resultant */}
          {mode === "add" && (
            <>
              {arrow(0, 0, U.x, U.y, GEO_BLUE)}
              {arrow(U.x, U.y, U.x + vxd, U.y + vyd, GEO_ACCENT)}
              {arrow(0, 0, U.x + vxd, U.y + vyd, RED, 2.6, undefined, "gm-fade")}
              <text x={px(U.x / 2) + 6} y={py(U.y / 2) - 6} fontSize="11" fill={GEO_BLUE} fontWeight={600}>u</text>
              <text x={px(U.x + vxd / 2) + 6} y={py(U.y + vyd / 2) - 6} fontSize="11" fill={GEO_ACCENT} fontWeight={600}>v</text>
            </>
          )}

          {/* dot mode: both from origin + right-angle beacon when perpendicular */}
          {mode === "dot" && (
            <>
              {arrow(0, 0, U.x, U.y, GEO_BLUE)}
              {arrow(0, 0, vxd, vyd, GEO_ACCENT)}
              <text x={px(U.x) + 8} y={py(U.y) - 4} fontSize="11" fill={GEO_BLUE} fontWeight={600}>u</text>
              <text x={px(vxd) + 8} y={py(vyd) - 4} fontSize="11" fill={GEO_ACCENT} fontWeight={600}>v</text>
              {dot === 0 && (vx !== 0 || vy !== 0) && (
                <circle cx={px(0)} cy={py(0)} r={12} fill="none" stroke={RED} strokeWidth={1.4} opacity={0.6} className="gm-beacon" />
              )}
            </>
          )}
        </svg>
      </div>

      <div className="mt-2 flex justify-center text-[14px]">
        <span className="serif tabular" style={{ color: GEO_ACCENT }}>{eqnText}</span>
      </div>

      {/* readouts */}
      <div className="mt-2 grid grid-cols-2 gap-2">
        {mode === "components" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_BLUE }}>the walk</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>{vx} east, {vy} north</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>magnitude |v|</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>√({vx}² + {vy}²) = {fmt(mag)}</div>
            </div>
          </>
        )}
        {mode === "add" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: RED }}>resultant u + v</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>⟨{sum.x}, {sum.y}⟩</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>component recipe</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>⟨3+{vx}, 1+{vy}⟩</div>
            </div>
          </>
        )}
        {mode === "dot" && (
          <>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>term by term</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: "var(--fg)" }}>2·{vx} + 3·{vy}</div>
            </div>
            <div className="rounded-xl p-2.5 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
              <div className="text-[10px] uppercase tracking-wide" style={{ color: GEO_ACCENT }}>u · v</div>
              <div className="serif tabular mt-0.5 text-[14px]" style={{ color: dot === 0 ? RED : "var(--fg)" }}>{dot}</div>
            </div>
          </>
        )}
      </div>

      {/* verdict */}
      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {mode === "components" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              One arrow, two numbers: <b style={{ color: GEO_ACCENT }}>⟨{vx}, {vy}⟩</b>, length <b style={{ color: GEO_BLUE }}>{fmt(mag)}</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              the dashed legs are the components — Pythagoras runs the magnitude
            </div>
          </>
        )}
        {mode === "add" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              Walk <b style={{ color: GEO_BLUE }}>u</b>, then <b style={{ color: GEO_ACCENT }}>v</b> — the shortcut home is <b style={{ color: RED }}>u + v = ⟨{sum.x}, {sum.y}⟩</b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              tip-to-tail in the picture; add the components in the algebra
            </div>
          </>
        )}
        {mode === "dot" && (
          <>
            <div className="serif text-[15px]" style={{ color: "var(--fg)" }}>
              u · v = <b style={{ color: dot === 0 ? RED : dot > 0 ? GEO_BLUE : RED }}>{dot}</b> — the angle is{" "}
              <b style={{ color: dot === 0 ? RED : dot > 0 ? GEO_BLUE : RED }}>
                {dot > 0 ? "acute" : dot === 0 ? "a right angle" : "obtuse"}
              </b>
            </div>
            <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
              positive agrees, zero is perpendicular, negative opposes — the sign is a protractor
            </div>
          </>
        )}
      </div>

      {/* controls */}
      <div className="mt-4 flex items-center justify-center gap-6">
        {stepper(mode === "components" ? "x-component" : "vₓ", vx, setVx, GEO_ACCENT)}
        {stepper(mode === "components" ? "y-component" : "vᵧ", vy, setVy, GEO_BLUE)}
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        {mode === "components" && "step the components — the arrow and its length follow"}
        {mode === "add" && "reshape v — it stays glued tip-to-tail; the red shortcut updates"}
        {mode === "dot" && "aim v — find the spots where u · v hits exactly zero"}
      </div>
    </div>
  );
}
