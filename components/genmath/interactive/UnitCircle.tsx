"use client";

import { useEffect, useMemo, useState } from "react";
import { Minus, Plus, RotateCcw } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { useAnimatedValue } from "@/components/genmath/interactive/useAnimatedValue";
import { type UnitCircleConfig } from "@/lib/genmath-interactive";

// The trigonometry workbench — three modes:
//  radians: arcs of radius-length wrap around the circle on a stepper. Each
//           wrap is 1 radian ≈ 57.3°; three-and-a-bit wraps make the half-turn
//           π. CircleUnroll's idea, bent around the rim.
//  explore: an angle stepper drives a point around the unit circle; the right
//           triangle inside shows cos θ (x-leg) and sin θ (y-leg) with live
//           values, quadrant, and signs. The coordinates ARE the trig values.
//  wave:    the classic — a point orbits (auto-play) while its height traces
//           the sine wave onto a scroll to the right. Replay button.

const RED = "rgb(200,60,60)";

function fmt2(n: number): string {
  const r = Math.round(n * 100) / 100;
  return (Object.is(r, -0) ? 0 : r).toFixed(2);
}

// Pretty radian label for multiples of 15°.
function radLabel(deg: number): string {
  const num = deg; // deg/180 in lowest terms, times π
  const g = (a: number, b: number): number => (b ? g(b, a % b) : a);
  const d = g(Math.abs(num), 180);
  const top = num / d, bot = 180 / d;
  if (top === 0) return "0";
  const t = top === 1 ? "π" : `${top}π`;
  return bot === 1 ? t : `${t}/${bot}`;
}

export default function UnitCircle({ config }: { config: UnitCircleConfig }) {
  const { mode, start = 45 } = config;

  // ---- geometry ----
  const W = 340;
  const H = mode === "wave" ? 240 : 340;
  const R = mode === "wave" ? 78 : 118;
  const cx = mode === "wave" ? 100 : W / 2;
  const cy = H / 2;
  const toXY = (deg: number, r = R) => ({
    x: cx + r * Math.cos((deg * Math.PI) / 180),
    y: cy - r * Math.sin((deg * Math.PI) / 180),
  });

  // ---- explore state ----
  const [deg, setDeg] = useState(start);
  const degD = useAnimatedValue(deg, { stiffness: 110, damping: 17, from: 0 });

  // ---- radians state ----
  const [nRad, setNRad] = useState(1);
  const nRadD = useAnimatedValue(nRad, { stiffness: 90, damping: 15, from: 0 });

  // ---- wave auto-play ----
  const [go, setGo] = useState(false);
  useEffect(() => {
    if (mode !== "wave") return;
    const id = setTimeout(() => setGo(true), 700);
    return () => clearTimeout(id);
  }, [mode]);
  const sweep = useAnimatedValue(go ? 1 : 0, { stiffness: 6, damping: 5.5 });
  const sp = Math.max(0, Math.min(1, sweep));
  const replay = () => {
    setGo(false);
    setTimeout(() => setGo(true), 380);
  };

  // ======================================================== radians mode
  if (mode === "radians") {
    const wrapped = Math.max(0, nRadD); // radians wrapped (animated)
    const arcPath = (fromRad: number, toRad: number) => {
      const a0 = (fromRad * 180) / Math.PI;
      const a1 = (toRad * 180) / Math.PI;
      const p0 = toXY(a0), p1 = toXY(a1);
      const large = a1 - a0 > 180 ? 1 : 0;
      return `M ${p0.x} ${p0.y} A ${R} ${R} 0 ${large} 0 ${p1.x} ${p1.y}`;
    };
    const segs: { from: number; to: number }[] = [];
    for (let k = 0; k < Math.ceil(wrapped); k++) {
      segs.push({ from: k, to: Math.min(k + 1, wrapped) });
    }
    const degEq = nRad * (180 / Math.PI);
    const end = toXY((wrapped * 180) / Math.PI);

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="Radius lengths wrapping around a circle">
          <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--line)" strokeWidth={1.6} />
          {/* the radius, as the measuring stick */}
          <line x1={cx} y1={cy} x2={cx + R} y2={cy} stroke="var(--fg-2)" strokeWidth={2} />
          <text x={cx + R / 2} y={cy + 14} fontSize="11" fill="var(--fg-2)" textAnchor="middle">r</text>
          {/* π marker at the half-turn */}
          <g opacity={0.7}>
            <circle cx={cx - R} cy={cy} r={3} fill="var(--fg-3)" />
            <text x={cx - R - 8} y={cy + 4} fontSize="11" fill="var(--fg-3)" textAnchor="end">π</text>
          </g>
          {/* wrapped radius-arcs, alternating colors */}
          {segs.map((s, i) => (
            <path key={i} d={arcPath(s.from, s.to)} fill="none" stroke={i % 2 === 0 ? GEO_ACCENT : GEO_BLUE} strokeWidth={5} strokeLinecap="round" />
          ))}
          {/* tick + label at each whole radian */}
          {Array.from({ length: Math.floor(wrapped + 1e-6) }, (_, i) => i + 1).map((k) => {
            const p = toXY((k * 180) / Math.PI, R + 14);
            return (
              <text key={k} x={p.x} y={p.y + 4} fontSize="11" fontWeight={700} fill={k % 2 === 1 ? GEO_ACCENT : GEO_BLUE} textAnchor="middle">{k}</text>
            );
          })}
          {/* moving endpoint + spoke */}
          <line x1={cx} y1={cy} x2={end.x} y2={end.y} stroke="var(--fg-3)" strokeWidth={1.2} strokeDasharray="4 4" />
          <circle cx={end.x} cy={end.y} r={5} fill="var(--fg)" />
        </svg>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            <b style={{ color: GEO_ACCENT }}>{nRad}</b> radian{nRad !== 1 ? "s" : ""} = {nRad} radius-length{nRad !== 1 ? "s" : ""} of arc ≈ <b style={{ color: GEO_BLUE }}>{fmt2(degEq)}°</b>
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {nRad < 3 ? "each wrap of one radius along the rim = 1 radian ≈ 57.3°"
              : nRad === 3 ? "three radii almost reach the half-turn — π ≈ 3.14 radians lands exactly there"
              : "past the π mark: the half-turn took π ≈ 3.14 radii of arc"}
          </div>
        </div>

        <div className="mt-4 flex items-center justify-center gap-2">
          <button type="button" onClick={() => setNRad((v) => Math.max(0, v - 1))} disabled={nRad <= 0} aria-label="Unwrap one radian" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
          <div className="serif tabular text-center" style={{ minWidth: 36, fontSize: 16, color: GEO_ACCENT }}>{nRad}</div>
          <button type="button" onClick={() => setNRad((v) => Math.min(6, v + 1))} disabled={nRad >= 6} aria-label="Wrap one radian" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
        </div>
        <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
          wrap radius-lengths around the rim — watch three-and-a-bit reach the π mark
        </div>
      </div>
    );
  }

  // ======================================================== wave mode
  if (mode === "wave") {
    const total = 360; // one full orbit
    const a = total * sp; // current angle (deg)
    const p = toXY(a);
    const waveX0 = cx + R + 26;
    const waveW = W - waveX0 - 10;
    const wx = (dd: number) => waveX0 + (dd / total) * waveW;
    const wy = (dd: number) => cy - R * Math.sin((dd * Math.PI) / 180);
    const tracePath = useMemo(() => {
      if (a <= 0.5) return "";
      const pts: string[] = [];
      for (let d = 0; d <= a; d += 3) pts.push(`${wx(d)},${wy(d)}`);
      return `M ${pts.join(" L ")}`;
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [a]);
    const sinNow = Math.sin((a * Math.PI) / 180);

    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 380, display: "block", margin: "0 auto" }} role="img" aria-label="A point orbiting a circle traces a sine wave">
          {/* circle + axes */}
          <line x1={cx - R - 8} y1={cy} x2={cx + R + 8} y2={cy} stroke="var(--line)" strokeWidth={1} />
          <line x1={cx} y1={cy - R - 8} x2={cx} y2={cy + R + 8} stroke="var(--line)" strokeWidth={1} />
          <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-2)" strokeWidth={1.6} />
          {/* wave axes */}
          <line x1={waveX0} y1={cy} x2={W - 8} y2={cy} stroke="var(--fg-2)" strokeWidth={1.4} />
          {[90, 180, 270, 360].map((d) => (
            <g key={d}>
              <line x1={wx(d)} y1={cy - 3} x2={wx(d)} y2={cy + 3} stroke="var(--fg-3)" strokeWidth={1} />
              <text x={wx(d)} y={cy + 15} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{d === 90 ? "π/2" : d === 180 ? "π" : d === 270 ? "3π/2" : "2π"}</text>
            </g>
          ))}
          <text x={waveX0 - 4} y={cy - R - 4} fontSize="9" fill="var(--fg-3)">+1</text>
          <text x={waveX0 - 4} y={cy + R + 12} fontSize="9" fill="var(--fg-3)">−1</text>

          {/* radius spoke + point */}
          <line x1={cx} y1={cy} x2={p.x} y2={p.y} stroke={GEO_ACCENT} strokeWidth={2} />
          {/* sin height inside the circle */}
          <line x1={p.x} y1={cy} x2={p.x} y2={p.y} stroke={GEO_BLUE} strokeWidth={2} strokeDasharray="4 3" />
          {/* height carried across to the wave */}
          <line x1={p.x} y1={p.y} x2={wx(a)} y2={p.y} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 4" opacity={0.7} />

          {/* the trace */}
          {tracePath && <path d={tracePath} fill="none" stroke={GEO_BLUE} strokeWidth={2.4} strokeLinecap="round" />}
          {/* pens */}
          <circle cx={p.x} cy={p.y} r={5.5} fill={GEO_ACCENT} stroke="var(--bg-1)" strokeWidth={1.4} />
          <circle cx={wx(a)} cy={wy(a)} r={4.5} fill={GEO_BLUE} stroke="var(--bg-1)" strokeWidth={1.2} />
        </svg>

        <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
          <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
            θ = <b style={{ color: GEO_ACCENT }}>{Math.round(a)}°</b> · sin θ = <b style={{ color: GEO_BLUE }}>{fmt2(sinNow)}</b>
          </div>
          <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {sp > 0.97
              ? <>One full orbit = one full wave: period <b>2π</b>. The circle IS the wave, unrolled.</>
              : <>the point&apos;s HEIGHT rides across to the scroll — sine is the height of a circling point</>}
          </div>
        </div>

        <div className="mt-3 flex justify-center">
          <button type="button" onClick={replay} aria-label="Orbit again" className="gm-press flex items-center gap-1.5 rounded-full px-4 py-2 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
            <RotateCcw className="h-3.5 w-3.5" /> Orbit again
          </button>
        </div>
      </div>
    );
  }

  // ======================================================== explore mode
  const p = toXY(degD);
  const cosV = Math.cos((deg * Math.PI) / 180);
  const sinV = Math.sin((deg * Math.PI) / 180);
  const quadrant = deg % 90 === 0 ? 0 : Math.floor((deg % 360) / 90) + 1;
  const arcR = 26;
  const arcSweep = (() => {
    const a1 = Math.max(0.01, degD % 360);
    const end = toXY(a1, arcR);
    const large = a1 > 180 ? 1 : 0;
    return `M ${cx + arcR} ${cy} A ${arcR} ${arcR} 0 ${large} 0 ${end.x} ${end.y}`;
  })();

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }} role="img" aria-label="A point on the unit circle with its coordinates">
        {/* axes + circle */}
        <line x1={10} y1={cy} x2={W - 10} y2={cy} stroke="var(--line)" strokeWidth={1.2} />
        <line x1={cx} y1={10} x2={cx} y2={H - 10} stroke="var(--line)" strokeWidth={1.2} />
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="var(--fg-2)" strokeWidth={1.6} />
        {/* unit labels */}
        <text x={cx + R + 6} y={cy + 12} fontSize="10" fill="var(--fg-3)">1</text>
        <text x={cx - R - 12} y={cy + 12} fontSize="10" fill="var(--fg-3)">−1</text>

        {/* the right triangle: cos leg + sin leg */}
        <line x1={cx} y1={cy} x2={p.x} y2={cy} stroke={GEO_ACCENT} strokeWidth={3} strokeLinecap="round" />
        <line x1={p.x} y1={cy} x2={p.x} y2={p.y} stroke={GEO_BLUE} strokeWidth={3} strokeLinecap="round" />
        <line x1={cx} y1={cy} x2={p.x} y2={p.y} stroke="var(--fg-1)" strokeWidth={1.8} />

        {/* angle arc */}
        <path d={arcSweep} fill="none" stroke={GEO_ACCENT} strokeWidth={1.6} opacity={0.8} />

        {/* the point */}
        <circle cx={p.x} cy={p.y} r={9} fill="none" stroke="var(--fg)" strokeWidth={1.1} opacity={0.35} className="gm-beacon" />
        <circle cx={p.x} cy={p.y} r={5.2} fill="var(--fg)" />
        <text x={Math.max(58, Math.min(W - 58, p.x))} y={p.y + (sinV >= 0 ? -14 : 20)} fontSize="11.5" fontWeight={700} fill="var(--fg)" textAnchor="middle">
          ({fmt2(cosV)}, {fmt2(sinV)})
        </text>

        {/* leg labels */}
        <text x={(cx + p.x) / 2} y={cy + (sinV >= 0 ? 16 : -8)} fontSize="11" fontWeight={700} fill={GEO_ACCENT} textAnchor="middle">cos θ</text>
        <text x={p.x + (cosV >= 0 ? 8 : -8)} y={(cy + p.y) / 2 + 4} fontSize="11" fontWeight={700} fill={GEO_BLUE} textAnchor={cosV >= 0 ? "start" : "end"}>sin θ</text>
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="serif tabular text-[15px]" style={{ color: "var(--fg)" }}>
          θ = <b style={{ color: GEO_ACCENT }}>{deg}°</b> = {radLabel(deg)} rad · cos θ = <b style={{ color: GEO_ACCENT }}>{fmt2(cosV)}</b> · sin θ = <b style={{ color: GEO_BLUE }}>{fmt2(sinV)}</b>
        </div>
        <div className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
          {quadrant === 0
            ? "on an axis — one coordinate is 0, the other ±1"
            : `quadrant ${["", "I: both +", "II: cos −, sin +", "III: both −", "IV: cos +, sin −"][quadrant]}`} · the coordinates ARE the trig values
        </div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-2">
        <button type="button" onClick={() => setDeg((v) => Math.max(0, v - 15))} disabled={deg <= 0} aria-label="Decrease angle" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 48, fontSize: 16, color: GEO_ACCENT }}>{deg}°</div>
        <button type="button" onClick={() => setDeg((v) => Math.min(360, v + 15))} disabled={deg >= 360} aria-label="Increase angle" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-3)" }}>
        sweep the angle in 15° steps — watch the legs and signs change quadrant by quadrant
      </div>
    </div>
  );
}
