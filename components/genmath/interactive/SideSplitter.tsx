"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type SideSplitterConfig } from "@/lib/genmath-interactive";

// A triangle cut by a line DE parallel to its base BC. Slide the line: because
// D and E sit the same fraction of the way down each side, the two sides are
// ALWAYS split in the same ratio, AD : DB = AE : EC — the Triangle
// Proportionality (Side-Splitter) Theorem, shown live.
const W = 320;
const H = 250;
const TS = [0.25, 0.375, 0.5, 0.625, 0.75];

export default function SideSplitter({ config }: { config: SideSplitterConfig }) {
  const { ab = 8, ac = 12, color = GEO_ACCENT } = config;
  const [ti, setTi] = useState(() => {
    const i = TS.indexOf(config.start ?? 0.5);
    return i < 0 ? 2 : i;
  });
  const t = TS[ti];

  // triangle in math coords (y up); A apex, B bottom-left, C bottom-right,
  // placed so |AB| : |AC| ≈ ab : ac
  const A = { x: 3, y: 7 }, B = { x: 0, y: 0 }, C = { x: 10, y: 0 };
  const D = { x: A.x + t * (B.x - A.x), y: A.y + t * (B.y - A.y) };
  const E = { x: A.x + t * (C.x - A.x), y: A.y + t * (C.y - A.y) };

  const pts = [A, B, C];
  const minX = Math.min(...pts.map((p) => p.x)) - 1, maxX = Math.max(...pts.map((p) => p.x)) + 1;
  const minY = Math.min(...pts.map((p) => p.y)) - 1, maxY = Math.max(...pts.map((p) => p.y)) + 1;
  const scale = Math.min((W - 40) / (maxX - minX), (H - 50) / (maxY - minY));
  const ox = (W - (maxX - minX) * scale) / 2, oy = (H - (maxY - minY) * scale) / 2;
  const sx = (x: number) => ox + (x - minX) * scale;
  const sy = (y: number) => H - (oy + (y - minY) * scale);

  const ad = ab * t, db = ab * (1 - t), ae = ac * t, ec = ac * (1 - t);
  const fmt = (n: number) => (Number.isInteger(n) ? n.toString() : n.toFixed(1));
  const ratio = (p: number, q: number) => (q === 0 ? "—" : (p / q).toFixed(2));

  const lab = (P: any, Q: any, text: string, side: number) => {
    const mx = (sx(P.x) + sx(Q.x)) / 2, my = (sy(P.y) + sy(Q.y)) / 2;
    return <text x={mx + side * 12} y={my} fontSize="11" textAnchor="middle" fill="var(--fg-2)" dominantBaseline="middle">{text}</text>;
  };

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ maxWidth: 340, display: "block", margin: "0 auto" }}>
        <polygon points={`${sx(A.x)},${sy(A.y)} ${sx(B.x)},${sy(B.y)} ${sx(C.x)},${sy(C.y)}`} fill="rgba(120,120,120,0.05)" stroke="var(--fg-1)" strokeWidth={2} strokeLinejoin="round" />
        {/* the parallel cut DE */}
        <line x1={sx(D.x)} y1={sy(D.y)} x2={sx(E.x)} y2={sy(E.y)} stroke={color} strokeWidth={2.4} />
        {/* parallel arrow marks on DE and BC */}
        <text x={(sx(D.x) + sx(E.x)) / 2} y={sy(D.y) - 6} fontSize="12" textAnchor="middle" fill={color}>›</text>
        <text x={(sx(B.x) + sx(C.x)) / 2} y={sy(B.y) - 6} fontSize="12" textAnchor="middle" fill="var(--fg-2)">›</text>
        {lab(A, D, fmt(ad), -1)}
        {lab(D, B, fmt(db), -1)}
        {lab(A, E, fmt(ae), 1)}
        {lab(E, C, fmt(ec), 1)}
        {[["A", A], ["B", B], ["C", C], ["D", D], ["E", E]].map(([n, p]: any) => (
          <g key={n}>
            <circle cx={sx(p.x)} cy={sy(p.y)} r={3} fill={n === "D" || n === "E" ? color : "var(--fg)"} />
            <text x={sx(p.x) + (p.x < 4 ? -11 : 9)} y={sy(p.y) + (p.y > 3.5 ? -6 : 14)} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg)">{n}</text>
          </g>
        ))}
      </svg>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <span className="serif tabular">
          <span style={{ color }}>AD/DB = {ratio(ad, db)}</span> = <span style={{ color: GEO_BLUE }}>AE/EC = {ratio(ae, ec)}</span> <b style={{ color: "#3fa06a" }}>✓</b>
        </span>
        <div className="mt-1 text-[12px]" style={{ color: "var(--fg-2)" }}>DE ∥ BC, so the two sides split in the same ratio — wherever the line sits.</div>
      </div>

      <div className="mt-4 flex items-center justify-center gap-3">
        <span className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>slide the line</span>
        <button type="button" onClick={() => setTi((v) => Math.max(0, v - 1))} disabled={ti <= 0} aria-label="Up" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
        <button type="button" onClick={() => setTi((v) => Math.min(TS.length - 1, v + 1))} disabled={ti >= TS.length - 1} aria-label="Down" className="gm-press grid h-9 w-9 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
      </div>
    </div>
  );
}
