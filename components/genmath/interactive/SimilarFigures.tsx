"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { arcPath, GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { perimeterScale, areaScale } from "@/lib/geo";
import { type SimilarFiguresConfig } from "@/lib/genmath-interactive";

// Two similar right triangles side by side. The left is a fixed 3-4-5 shape;
// the right is the same shape scaled by k. Corresponding angles stay equal
// (marked), every side is k times its partner, the perimeter scales by k and
// the area by k². The 3-4-5 base keeps every length and the area exact.
const W = 340;
const H = 250;
const KS = [1, 1.5, 2, 2.5, 3];

export default function SimilarFigures({ config }: { config: SimilarFiguresConfig }) {
  const { show = "sides", color = GEO_ACCENT } = config;
  const [ki, setKi] = useState(() => {
    const i = KS.indexOf(config.start ?? 1.5);
    return i < 0 ? 1 : i;
  });
  const k = KS[ki];

  // base right triangle: legs 3 (up) and 4 (across), hypotenuse 5
  const baseLegs = { a: 4, b: 3, hyp: 5 };
  const unit = 22; // px per length unit for the LEFT triangle
  // left triangle vertices (screen)
  const L = { A: { x: 30, y: H - 40 }, B: { x: 30 + baseLegs.a * unit, y: H - 40 }, C: { x: 30, y: H - 40 - baseLegs.b * unit } };
  // right triangle scaled by k, but drawn at a fixed smaller px-unit so it fits
  const rUnit = 16;
  const rx0 = 200;
  const R = { A: { x: rx0, y: H - 40 }, B: { x: rx0 + baseLegs.a * k * rUnit, y: H - 40 }, C: { x: rx0, y: H - 40 - baseLegs.b * k * rUnit } };

  const Tri = ({ P, sides, tagK }: { P: { A: any; B: any; C: any }; sides: [number, number, number]; tagK: boolean }) => (
    <g>
      <polygon points={`${P.A.x},${P.A.y} ${P.B.x},${P.B.y} ${P.C.x},${P.C.y}`} fill={`${color}12`} stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
      {/* right-angle square at A */}
      <path d={`M ${P.A.x + 9} ${P.A.y} L ${P.A.x + 9} ${P.A.y - 9} L ${P.A.x} ${P.A.y - 9}`} fill="none" stroke={GEO_BLUE} strokeWidth={1.4} />
      {/* equal acute-angle arc at B */}
      <path d={arcPath(P.B.x, P.B.y, 16, 180, Math.atan2(P.C.y - P.B.y, P.C.x - P.B.x) * 180 / Math.PI)} fill="none" stroke={GEO_ACCENT} strokeWidth={1.5} />
      {/* side labels */}
      <text x={(P.A.x + P.B.x) / 2} y={P.A.y + 15} fontSize="11" textAnchor="middle" fill="var(--fg-2)">{sides[0]}</text>
      <text x={P.A.x - 9} y={(P.A.y + P.C.y) / 2} fontSize="11" textAnchor="middle" fill="var(--fg-2)">{sides[1]}</text>
      <text x={(P.B.x + P.C.x) / 2 + 8} y={(P.B.y + P.C.y) / 2 - 4} fontSize="11" textAnchor="middle" fill="var(--fg-2)">{sides[2]}</text>
    </g>
  );

  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(1));
  const perim = 12; // 3+4+5
  const area = 6; // ½·3·4

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 360, display: "block", margin: "0 auto" }}>
        <text x={L.A.x} y={22} fontSize="12" fill="var(--fg-3)">original</text>
        <text x={R.A.x} y={22} fontSize="12" fill="var(--fg-3)">image (×{fmt(k)})</text>
        <Tri P={L} sides={[baseLegs.a, baseLegs.b, baseLegs.hyp]} tagK={false} />
        <Tri P={R} sides={[baseLegs.a * k, baseLegs.b * k, baseLegs.hyp * k]} tagK />
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {show === "sides" ? (
          <>
            <div className="serif tabular">scale factor <b style={{ color }}>k = {fmt(k)}</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>Every image side is {fmt(k)} × its match: {baseLegs.a}→{fmt(baseLegs.a * k)}, {baseLegs.b}→{fmt(baseLegs.b * k)}, {baseLegs.hyp}→{fmt(baseLegs.hyp * k)}. Angles are unchanged.</div>
          </>
        ) : (
          <>
            <div className="serif tabular">perimeter ×<b style={{ color }}>{fmt(perimeterScale(k))}</b> · area ×<b style={{ color: GEO_BLUE }}>{fmt(areaScale(k))}</b></div>
            <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>Perimeter {perim} → {fmt(perim * k)} (×k). Area {area} → {fmt(area * k * k)} (×k²).</div>
          </>
        )}
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>scale factor</span>
        <button type="button" onClick={() => setKi((v) => Math.max(0, v - 1))} disabled={ki <= 0} aria-label="Smaller" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <div className="serif tabular text-center" style={{ minWidth: 44, fontSize: 17, color: "var(--fg)" }}>{fmt(k)}</div>
        <button type="button" onClick={() => setKi((v) => Math.min(KS.length - 1, v + 1))} disabled={ki >= KS.length - 1} aria-label="Larger" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
