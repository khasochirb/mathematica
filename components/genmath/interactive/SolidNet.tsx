"use client";

import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { rectPrismSurface, cylinderSurface } from "@/lib/geo";
import { type SolidNetConfig } from "@/lib/genmath-interactive";

// A solid unfolded into its flat NET, so surface area reads as the sum of the
// face areas: a rectangular prism opens into 6 rectangles, a cylinder into two
// circles plus one wrapped rectangle (2πr wide, h tall).
const W = 320;

export default function SolidNet({ config }: { config: SolidNetConfig }) {
  const { solid, color = GEO_ACCENT } = config;

  if (solid === "cylinder") {
    const r = config.r ?? 3, h = config.h ?? 5;
    const s = 12;
    const rectW = 2 * Math.PI * r * s * 0.5, rectH = h * s;
    const circR = r * s;
    const H = rectH + 2 * circR + 60;
    const cx = W / 2;
    const rectX = cx - rectW / 2, rectY = circR + 24;
    return (
      <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
        <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
          <circle cx={cx} cy={circR + 8} r={circR} fill={`${color}18`} stroke="var(--fg-1)" strokeWidth={1.6} />
          <text x={cx} y={circR + 12} fontSize="11" textAnchor="middle" fill={color} fontWeight={700}>πr²</text>
          <rect x={rectX} y={rectY} width={rectW} height={rectH} fill={`${GEO_BLUE}14`} stroke="var(--fg-1)" strokeWidth={1.6} />
          <text x={cx} y={rectY + rectH / 2} fontSize="11" textAnchor="middle" fill={GEO_BLUE} fontWeight={700}>2πr × h</text>
          <text x={cx} y={rectY + rectH + 14} fontSize="10" textAnchor="middle" fill="var(--fg-3)">width = circumference 2πr</text>
          <circle cx={cx} cy={rectY + rectH + circR + 20} r={circR} fill={`${color}18`} stroke="var(--fg-1)" strokeWidth={1.6} />
          <text x={cx} y={rectY + rectH + circR + 24} fontSize="11" textAnchor="middle" fill={color} fontWeight={700}>πr²</text>
        </svg>
        <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
          <span className="serif tabular">SA = 2πr² + 2πrh = <b style={{ color }}>{2 * r * r + 2 * r * h}π</b> ≈ {(cylinderSurface(r, h)).toFixed(1)}</span>
          <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>two circles ({r * r}π each) + a wrapped rectangle ({2 * r * h}π).</div>
        </div>
      </div>
    );
  }

  // rectangular prism net (cross layout)
  const l = config.l ?? 4, w = config.w ?? 3, h = config.h ?? 5;
  const s = 14;
  const H = (w + h + w) * s + 70;
  const cx = W / 2;
  const frontX = cx - (l * s) / 2, frontY = w * s + 20;
  const box = (x: number, y: number, ww: number, hh: number, fill: string, label: string) => (
    <g>
      <rect x={x} y={y} width={ww} height={hh} fill={fill} stroke="var(--fg-1)" strokeWidth={1.4} />
      <text x={x + ww / 2} y={y + hh / 2 + 4} fontSize="10" textAnchor="middle" fill="var(--fg-2)">{label}</text>
    </g>
  );
  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {box(frontX, frontY - w * s, l * s, w * s, `${color}14`, `top ${l}×${w}`)}
        {box(frontX - w * s, frontY, w * s, h * s, `${GEO_BLUE}12`, `${w}×${h}`)}
        {box(frontX, frontY, l * s, h * s, `${color}22`, `front ${l}×${h}`)}
        {box(frontX + l * s, frontY, w * s, h * s, `${GEO_BLUE}12`, `${w}×${h}`)}
        {box(frontX + l * s + w * s, frontY, l * s, h * s, `${color}14`, `back ${l}×${h}`)}
        {box(frontX, frontY + h * s, l * s, w * s, `${color}14`, `bottom ${l}×${w}`)}
      </svg>
      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">SA = 2(lw + lh + wh) = 2({l * w} + {l * h} + {w * h}) = <b style={{ color }}>{rectPrismSurface(l, w, h)}</b></span>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>the 6 faces come in 3 matching pairs.</div>
      </div>
    </div>
  );
}
