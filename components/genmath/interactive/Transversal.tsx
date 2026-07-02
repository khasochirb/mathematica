"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { ArrowHead, arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { TRANSVERSAL_PAIRS } from "@/lib/geo";
import { type TransversalConfig } from "@/lib/genmath-interactive";

// Two lines cut by a transversal — the primitive the whole parallel-lines unit
// runs on. The eight angles are numbered in standard position; a pair selector
// highlights corresponding / alternate-interior / alternate-exterior /
// same-side-interior pairs and states whether they are congruent or
// supplementary. A "parallel" toggle shows the special relationships hold ONLY
// when the lines are parallel — the exact distinction beginners miss.

const W = 320;
const H = 260;
const PW = W / 2; // pivot x

// screen point along a ray of math-angle `deg` (y-up) from center
function ray(cx: number, cy: number, deg: number, r: number) {
  const t = (deg * Math.PI) / 180;
  return { x: cx + r * Math.cos(t), y: cy - r * Math.sin(t) };
}

// line-line intersection: point p1 + s·d1 == p2 + u·d2
function intersect(p1: { x: number; y: number }, d1: { x: number; y: number }, p2: { x: number; y: number }, d2: { x: number; y: number }) {
  const den = d1.x * d2.y - d1.y * d2.x;
  const s = ((p2.x - p1.x) * d2.y - (p2.y - p1.y) * d2.x) / den;
  return { x: p1.x + s * d1.x, y: p1.y + s * d1.y };
}

// The four regions around an intersection of a near-horizontal line (screen
// angle `lineDegScreen`, ~0) and the transversal (math-angle `transMath`).
// Returns the measure + centroid math-angle keyed by TL/TR/BL/BR.
function regionsAt(lineMath: number, transMath: number) {
  // four ray math-angles
  const rays = [lineMath, lineMath + 180, transMath, transMath + 180].map((d) => ((d % 360) + 360) % 360).sort((a, b) => a - b);
  const out: { measure: number; centroid: number }[] = [];
  for (let i = 0; i < 4; i++) {
    const a1 = rays[i];
    const a2 = rays[(i + 1) % 4] + (i === 3 ? 360 : 0);
    out.push({ measure: Math.round(a2 - a1), centroid: (a1 + a2) / 2 });
  }
  // classify each region to a screen quadrant by centroid (screen: y flipped)
  const byQuad: Record<string, { measure: number; centroid: number }> = {};
  for (const reg of out) {
    const c = ((reg.centroid % 360) + 360) % 360;
    const up = c > 0 && c < 180; // math y-up
    const right = c < 90 || c > 270;
    const key = (up ? "T" : "B") + (right ? "R" : "L");
    byQuad[key] = reg;
  }
  return byQuad;
}

export default function Transversal({ config }: { config: TransversalConfig }) {
  const {
    acute: a0 = 62,
    highlight: hl0 = "corresponding",
    interactive = true,
    showParallelToggle = false,
    startParallel = true,
    showMeasures = false,
  } = config;

  const [a, setA] = useState(a0);
  const [hl, setHl] = useState<TransversalConfig["highlight"]>(hl0);
  const [parallel, setParallel] = useState(startParallel);

  // geometry: line m horizontal through P=(PW, 95). transversal through P at
  // math-angle `a` (up-right). line n horizontal (parallel) or tilted.
  const P = { x: PW, y: 95 };
  const transMath = a; // up-right
  const transDir = { x: Math.cos((a * Math.PI) / 180), y: -Math.sin((a * Math.PI) / 180) };

  const tilt = parallel ? 0 : -14; // line n tilt in degrees (screen)
  const nAnchor = { x: PW - 20, y: 180 };
  const nDir = { x: Math.cos((tilt * Math.PI) / 180), y: -Math.sin((tilt * Math.PI) / 180) };
  const Q = intersect(P, transDir, nAnchor, nDir);

  // region measures at each intersection
  const topR = regionsAt(0, transMath);
  const botR = regionsAt(-tilt, transMath); // line n math-angle = -tilt (screen tilt flips)

  // numbering: top 1=TL 2=TR 3=BL 4=BR ; bottom 5=TL 6=TR 7=BL 8=BR
  const num: Record<number, { at: { x: number; y: number }; reg: { measure: number; centroid: number } }> = {
    1: { at: P, reg: topR.TL }, 2: { at: P, reg: topR.TR }, 3: { at: P, reg: topR.BL }, 4: { at: P, reg: topR.BR },
    5: { at: Q, reg: botR.TL }, 6: { at: Q, reg: botR.TR }, 7: { at: Q, reg: botR.BL }, 8: { at: Q, reg: botR.BR },
  };

  const meta = hl && hl !== "none" ? TRANSVERSAL_PAIRS[hl] : null;
  const activePair = meta ? meta.pairs[0] : null;
  const relHolds = meta ? (!meta.onlyIfParallel || parallel) : false;
  const highlighted = new Set(activePair ?? []);

  // extend a line across the viewBox
  const seg = (pt: { x: number; y: number }, dir: { x: number; y: number }, len = 240) => ({
    x1: pt.x - dir.x * len, y1: pt.y - dir.y * len, x2: pt.x + dir.x * len, y2: pt.y + dir.y * len,
  });
  const mLine = seg(P, { x: 1, y: 0 });
  const nLine = seg(Q, nDir);
  const tLine = seg(P, transDir);

  const PAIR_LABEL: Record<string, string> = {
    corresponding: "Corresponding", altInterior: "Alternate interior", altExterior: "Alternate exterior",
    sameSideInterior: "Same-side interior", vertical: "Vertical", linearPair: "Linear pair",
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* the two lines */}
        <line x1={mLine.x1} y1={mLine.y1} x2={mLine.x2} y2={mLine.y2} stroke="var(--fg-1)" strokeWidth={2} />
        <ArrowHead x={W - 6} y={P.y} deg={0} color="var(--fg-1)" />
        <ArrowHead x={6} y={P.y} deg={180} color="var(--fg-1)" />
        <line x1={nLine.x1} y1={nLine.y1} x2={nLine.x2} y2={nLine.y2} stroke="var(--fg-1)" strokeWidth={2} />
        {/* transversal */}
        <line x1={tLine.x1} y1={tLine.y1} x2={tLine.x2} y2={tLine.y2} stroke="var(--fg-2)" strokeWidth={2} />

        {/* parallel tick marks (arrowheads mid-line) when parallel */}
        {parallel && (
          <>
            <path d={`M ${PW - 46} ${P.y - 5} l 7 5 l -7 5`} fill="none" stroke="var(--fg-3)" strokeWidth={1.4} />
            <path d={`M ${PW - 46} ${Q.y - 5} l 7 5 l -7 5`} fill="none" stroke="var(--fg-3)" strokeWidth={1.4} />
          </>
        )}

        {/* angle arcs + numbers */}
        {Object.entries(num).map(([n, { at, reg }]) => {
          const on = highlighted.has(Number(n));
          const color = on ? (relHolds ? GEO_ACCENT : "rgb(200,60,60)") : "var(--fg-3)";
          const lp = ray(at.x, at.y, reg.centroid, 26);
          return (
            <g key={n}>
              {on && (
                <path
                  d={arcPath(at.x, at.y, 16, reg.centroid - reg.measure / 2, reg.centroid + reg.measure / 2)}
                  fill="none"
                  stroke={color}
                  strokeWidth={2.4}
                />
              )}
              <text x={lp.x} y={lp.y + 4} fontSize="12" textAnchor="middle" fill={color} fontWeight={on ? 700 : 400}>
                {showMeasures ? `${reg.measure}°` : n}
              </text>
            </g>
          );
        })}
        <circle cx={P.x} cy={P.y} r={3.2} fill="var(--fg)" />
        <circle cx={Q.x} cy={Q.y} r={3.2} fill="var(--fg)" />
      </svg>

      {/* verdict */}
      {meta && activePair && (
        <div
          className="mt-2 rounded-xl p-3 text-center"
          style={
            relHolds
              ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
              : { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }
          }
        >
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            {PAIR_LABEL[hl!]} angles — <b style={{ color: "var(--fg)" }}>∠{activePair[0]} and ∠{activePair[1]}</b>
          </div>
          <div className="mt-0.5 serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            {relHolds ? (
              meta.rel === "congruent" ? (
                <>∠{activePair[0]} ≅ ∠{activePair[1]} <span style={{ color: "var(--accent)" }}>({num[activePair[0]].reg.measure}° = {num[activePair[1]].reg.measure}°)</span></>
              ) : (
                <>∠{activePair[0]} + ∠{activePair[1]} = <span style={{ color: "var(--accent)" }}>{num[activePair[0]].reg.measure}° + {num[activePair[1]].reg.measure}° = 180°</span></>
              )
            ) : (
              <span style={{ color: "rgb(200,60,60)" }}>
                {num[activePair[0]].reg.measure}° ≠ {num[activePair[1]].reg.measure}° — not related, because the lines aren&apos;t parallel
              </span>
            )}
          </div>
        </div>
      )}

      {/* pair selector */}
      {interactive && (
        <div className="mt-3 flex flex-wrap justify-center gap-1.5">
          {(["corresponding", "altInterior", "altExterior", "sameSideInterior"] as const).map((k) => (
            <button
              key={k}
              type="button"
              onClick={() => setHl(k)}
              className="gm-press rounded-full px-3 py-1.5 text-[12px]"
              style={
                hl === k
                  ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                  : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }
              }
            >
              {PAIR_LABEL[k]}
            </button>
          ))}
        </div>
      )}

      {/* controls */}
      {interactive && (
        <div className="mt-3 flex items-center justify-center gap-3">
          <button type="button" onClick={() => setA((v) => Math.max(35, v - 3))} disabled={a <= 35} aria-label="Tilt transversal" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
          <div className="text-center text-[12px]" style={{ color: "var(--fg-3)", minWidth: 90 }}>tilt the transversal</div>
          <button type="button" onClick={() => setA((v) => Math.min(90, v + 3))} disabled={a >= 90} aria-label="Tilt transversal" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
        </div>
      )}

      {showParallelToggle && (
        <div className="mt-3 flex justify-center">
          <button
            type="button"
            onClick={() => setParallel((v) => !v)}
            className="gm-press rounded-full px-4 py-2 text-[13px]"
            style={{ background: parallel ? "var(--accent)" : "var(--bg-2)", border: parallel ? "1px solid var(--accent)" : "1px solid var(--line)", color: parallel ? "var(--accent-ink, #fff)" : "var(--fg)" }}
          >
            {parallel ? "Lines are parallel ✓" : "Lines are NOT parallel"}
          </button>
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {hl === "sameSideInterior"
          ? <>Same-side interior angles are <b style={{ color: "var(--fg-1)" }}>supplementary</b> (sum 180°) — not congruent.</>
          : <>These pairs are <b style={{ color: "var(--fg-1)" }}>congruent</b> — but only when the lines are parallel.</>}
      </div>
    </div>
  );
}
