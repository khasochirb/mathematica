"use client";

import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type CompositeAreaConfig, type CompositePart } from "@/lib/genmath-interactive";

// A composite figure built from positioned rectangles, triangles, and
// circles/semicircles, each ADDED or SUBTRACTED. Part areas and the total are
// authored (exact, sympy-verified in the lesson), so the readout is honest; the
// renderer draws the figure and lists the breakdown.
const W = 320;

export default function CompositeArea({ config }: { config: CompositeAreaConfig }) {
  const { width, height, parts, total, caption } = config;
  const pad = 16;
  const scale = (W - 2 * pad) / width;
  const H = height * scale + 2 * pad;
  const sx = (x: number) => pad + x * scale;
  const sy = (y: number) => H - pad - y * scale; // y up

  const draw = (p: CompositePart, i: number) => {
    const add = p.op !== "subtract";
    const fill = add ? `${p.color ?? GEO_ACCENT}22` : "var(--bg-1)";
    const stroke = add ? (p.color ?? GEO_ACCENT) : GEO_BLUE;
    const dash = add ? undefined : "5 4";
    if (p.kind === "rect") {
      return <rect key={i} x={sx(p.x ?? 0)} y={sy((p.y ?? 0) + (p.h ?? 0))} width={(p.w ?? 0) * scale} height={(p.h ?? 0) * scale} fill={fill} stroke={stroke} strokeWidth={1.8} strokeDasharray={dash} />;
    }
    if (p.kind === "triangle" && p.pts) {
      const pts = p.pts.map(([x, y]) => `${sx(x)},${sy(y)}`).join(" ");
      return <polygon key={i} points={pts} fill={fill} stroke={stroke} strokeWidth={1.8} strokeDasharray={dash} strokeLinejoin="round" />;
    }
    if (p.kind === "circle") {
      return <circle key={i} cx={sx(p.cx ?? 0)} cy={sy(p.cy ?? 0)} r={(p.r ?? 0) * scale} fill={fill} stroke={stroke} strokeWidth={1.8} strokeDasharray={dash} />;
    }
    if (p.kind === "semicircle") {
      const r = (p.r ?? 0) * scale, cx = sx(p.cx ?? 0), cy = sy(p.cy ?? 0);
      // default: top half
      const path = `M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy} Z`;
      return <path key={i} d={path} fill={fill} stroke={stroke} strokeWidth={1.8} strokeDasharray={dash} />;
    }
    return null;
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        {parts.map(draw)}
      </svg>

      <div className="mt-3 rounded-xl p-3 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="flex flex-col gap-1">
          {parts.filter((p) => p.area).map((p, i) => (
            <div key={i} className="flex items-center justify-between">
              <span style={{ color: p.op === "subtract" ? GEO_BLUE : "var(--fg-1)" }}>
                {p.op === "subtract" ? "− " : "+ "}{p.label ?? p.kind}
              </span>
              <span className="serif tabular">{p.area}</span>
            </div>
          ))}
          {total && (
            <div className="mt-1 flex items-center justify-between border-t pt-1" style={{ borderColor: "var(--line)" }}>
              <b>Total area</b>
              <b className="serif tabular" style={{ color: GEO_ACCENT }}>{total}</b>
            </div>
          )}
        </div>
      </div>
      {caption && <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>{caption}</div>}
    </div>
  );
}
