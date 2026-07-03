"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { ArrowHead, arcPath, sectorPath, GEO_ACCENT } from "@/components/genmath/interactive/GeoDiagram";
import { TRANSVERSAL_PAIRS } from "@/lib/geo";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type TransversalConfig } from "@/lib/genmath-interactive";

// Two lines cut by a transversal — the primitive the whole parallel-lines unit
// runs on. The eight angles are numbered in standard position; a pair selector
// highlights corresponding / alternate-interior / alternate-exterior /
// same-side-interior pairs and states whether they are congruent or
// supplementary. A "parallel" toggle shows the special relationships hold ONLY
// when the lines are parallel — the exact distinction beginners miss.
//
// Angle convention: all geometry is done in MATH angles (y up); converting to
// screen space happens in exactly two places — ray() for positions and
// toScreen() for arc/sector angles. Mixing the two is what mirrored the arcs
// into the wrong wedge before, so keep the conversion at the edge.

const W = 320;
const H = 260;
const PW = W / 2; // pivot x

// math angle (y-up) -> screen angle (y-down) for arcPath/sectorPath
const toScreen = (mathDeg: number) => -mathDeg;

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

// The four regions around the intersection of a line at math-angle `lineMath`
// and the transversal at math-angle `transMath`. Returns measure + start/end
// math-angles + centroid, keyed by screen quadrant TL/TR/BL/BR.
function regionsAt(lineMath: number, transMath: number) {
  const rays = [lineMath, lineMath + 180, transMath, transMath + 180].map((d) => ((d % 360) + 360) % 360).sort((a, b) => a - b);
  const byQuad: Record<string, { measure: number; a1: number; a2: number; centroid: number }> = {};
  for (let i = 0; i < 4; i++) {
    const a1 = rays[i];
    const a2 = rays[(i + 1) % 4] + (i === 3 ? 360 : 0);
    const centroid = (a1 + a2) / 2;
    const c = ((centroid % 360) + 360) % 360;
    const up = c > 0 && c < 180; // math y-up
    const right = c < 90 || c > 270;
    byQuad[(up ? "T" : "B") + (right ? "R" : "L")] = { measure: Math.round(a2 - a1), a1, a2, centroid };
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

  const [aTarget, setATarget] = useState(a0);
  const [hl, setHl] = useState<TransversalConfig["highlight"]>(hl0);
  const [pairIx, setPairIx] = useState(0);
  const [parallel, setParallel] = useState(startParallel);

  // Spring-animate the transversal tilt and line n's tilt so every change —
  // button taps and the parallel toggle alike — glides instead of jumping.
  const a = useAnimatedValue(aTarget, { stiffness: 150, damping: 20, from: a0 - 16 }); // swings into place on entry
  const tilt = useAnimatedValue(parallel ? 0 : -14, { stiffness: 150, damping: 20 }); // line n math-angle

  // geometry: line m horizontal through P=(PW, 95); transversal through P at
  // math-angle `a`; line n through a fixed anchor at math-angle `tilt`.
  const P = { x: PW, y: 95 };
  const transDir = { x: Math.cos((a * Math.PI) / 180), y: -Math.sin((a * Math.PI) / 180) };
  const nAnchor = { x: PW - 20, y: 180 };
  const nDir = { x: Math.cos((tilt * Math.PI) / 180), y: -Math.sin((tilt * Math.PI) / 180) };
  const Q = intersect(P, transDir, nAnchor, nDir);

  // region measures at each intersection (both in math angles, y-up)
  const topR = regionsAt(0, a);
  const botR = regionsAt(tilt, a);

  // numbering: top 1=TL 2=TR 3=BL 4=BR ; bottom 5=TL 6=TR 7=BL 8=BR
  const num: Record<number, { at: { x: number; y: number }; reg: { measure: number; a1: number; a2: number; centroid: number } }> = {
    1: { at: P, reg: topR.TL }, 2: { at: P, reg: topR.TR }, 3: { at: P, reg: topR.BL }, 4: { at: P, reg: topR.BR },
    5: { at: Q, reg: botR.TL }, 6: { at: Q, reg: botR.TR }, 7: { at: Q, reg: botR.BL }, 8: { at: Q, reg: botR.BR },
  };

  const meta = hl && hl !== "none" ? TRANSVERSAL_PAIRS[hl] : null;
  const activePair = meta ? meta.pairs[Math.min(pairIx, meta.pairs.length - 1)] : null;
  const relHolds = meta ? (!meta.onlyIfParallel || parallel) : false;
  const highlighted = new Set(activePair ?? []);
  const hlColor = relHolds ? GEO_ACCENT : "rgb(200,60,60)";

  const pickHl = (k: TransversalConfig["highlight"]) => {
    setHl(k);
    setPairIx(0);
  };
  // tap an angle number to jump to the pair (in the current relationship)
  // that contains it — e.g. in "corresponding" mode, tapping ∠3 shows 3 & 7.
  const pickAngle = (n: number) => {
    if (!meta) return;
    const ix = meta.pairs.findIndex((p) => p.includes(n));
    if (ix >= 0) setPairIx(ix);
  };

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

  // remount key so the sweep-in animation replays whenever the selection moves
  const sweepKey = `${hl}-${pairIx}-${relHolds}`;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {/* highlighted wedges UNDER the lines: fill the angle's interior so
            there is zero ambiguity about which angle is meant */}
        {activePair && activePair.map((n) => {
          const { at, reg } = num[n];
          return (
            <path
              key={`w-${sweepKey}-${n}`}
              className="gm-wash-in"
              d={sectorPath(at.x, at.y, 30, toScreen(reg.a1), toScreen(reg.a2))}
              fill={hlColor}
              fillOpacity={0.16}
            />
          );
        })}

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

        {/* angle arcs + numbers (numbers are tap targets) */}
        {Object.entries(num).map(([k, { at, reg }]) => {
          const n = Number(k);
          const on = highlighted.has(n);
          const color = on ? hlColor : "var(--fg-3)";
          // highlighted numbers sit just past the wedge so the wash never swallows them
          const lp = ray(at.x, at.y, reg.centroid, on ? 40 : 27);
          return (
            <g key={n} onClick={() => pickAngle(n)} style={{ cursor: meta ? "pointer" : "default" }}>
              {on && (
                <path
                  key={`a-${sweepKey}-${n}`}
                  className="gm-arc-sweep"
                  pathLength={1}
                  d={arcPath(at.x, at.y, 17, toScreen(reg.a1), toScreen(reg.a2))}
                  fill="none"
                  stroke={color}
                  strokeWidth={2.4}
                  strokeLinecap="round"
                />
              )}
              {/* generous invisible hit area behind the number */}
              <circle cx={lp.x} cy={lp.y} r={12} fill="transparent" />
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
          style={{
            transition: "background 0.35s ease, border-color 0.35s ease",
            ...(relHolds
              ? { background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }
              : { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }),
          }}
        >
          <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
            {PAIR_LABEL[hl!]} angles — <b style={{ color: "var(--fg)" }}>∠{activePair[0]} and ∠{activePair[1]}</b>
            {meta.pairs.length > 1 && (
              <span style={{ color: "var(--fg-3)" }}> · tap any numbered angle to switch pairs</span>
            )}
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
              onClick={() => pickHl(k)}
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
          <button type="button" onClick={() => setATarget((v) => Math.max(35, v - 6))} disabled={aTarget <= 35} aria-label="Tilt transversal" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
          <div className="text-center text-[12px]" style={{ color: "var(--fg-3)", minWidth: 90 }}>tilt the transversal</div>
          <button type="button" onClick={() => setATarget((v) => Math.min(85, v + 6))} disabled={aTarget >= 85} aria-label="Tilt transversal" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
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
