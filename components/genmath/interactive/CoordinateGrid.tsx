"use client";

import { useState } from "react";
import { RotateCcw } from "lucide-react";
import { type CoordinateGridConfig } from "@/lib/genmath-interactive";

// One reusable coordinate-plane primitive with several modes:
//  - plot:      draws the given labelled points on the grid.
//  - identify:  tap any lattice point to read back its (x, y) coordinates.
//  - quadrants: shades and labels the four quadrants (I–IV).
//  - reflect:   shows a point and, on tap, its mirror image across an axis.
//  - distance:  shows two points sharing a row/column and counts the units.
export default function CoordinateGrid({ config }: { config: CoordinateGridConfig }) {
  const { min = -5, max = 5, mode, points = [], reflectAxis = "x", polygon = false, showQuadrants = false, color = "#e8913c" } = config;
  const [sel, setSel] = useState<{ x: number; y: number } | null>(null);
  const [revealed, setRevealed] = useState(false);

  // Name the quadrant (or axis) a point falls in — used by the identify
  // playground so tapping a point answers "which quadrant?".
  const quadrantOf = (p: { x: number; y: number }): string => {
    if (p.x === 0 && p.y === 0) return "the origin";
    if (p.x === 0) return "on the y-axis";
    if (p.y === 0) return "on the x-axis";
    if (p.x > 0 && p.y > 0) return "Quadrant I";
    if (p.x < 0 && p.y > 0) return "Quadrant II";
    if (p.x < 0 && p.y < 0) return "Quadrant III";
    return "Quadrant IV";
  };
  const quadShade = mode === "quadrants" || (mode === "identify" && showQuadrants);

  const N = max - min;
  const cell = 30;
  const pad = 24;
  const size = N * cell;
  const W = size + pad * 2;

  // grid coord -> svg pixel
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;

  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);
  const ACCENT = color;
  const BLUE = "#5b8def";

  // reflection of the first point across the chosen axis
  const src = points[0];
  const reflected = src ? (reflectAxis === "x" ? { x: src.x, y: -src.y } : { x: -src.x, y: src.y }) : null;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Coordinate grid">
          {/* Quadrant shading */}
          {quadShade && (
            <>
              <rect x={px(0)} y={py(max)} width={size / 2} height={size / 2} fill={`${ACCENT}14`} />
              <rect x={px(min)} y={py(max)} width={size / 2} height={size / 2} fill={`${BLUE}14`} />
              <rect x={px(min)} y={py(0)} width={size / 2} height={size / 2} fill={`${ACCENT}14`} />
              <rect x={px(0)} y={py(0)} width={size / 2} height={size / 2} fill={`${BLUE}14`} />
              <text x={px(max / 2)} y={py(max / 2)} textAnchor="middle" dominantBaseline="middle" fontSize="15" fontStyle="italic" fill="var(--fg-3)">I</text>
              <text x={px(min / 2)} y={py(max / 2)} textAnchor="middle" dominantBaseline="middle" fontSize="15" fontStyle="italic" fill="var(--fg-3)">II</text>
              <text x={px(min / 2)} y={py(min / 2)} textAnchor="middle" dominantBaseline="middle" fontSize="15" fontStyle="italic" fill="var(--fg-3)">III</text>
              <text x={px(max / 2)} y={py(min / 2)} textAnchor="middle" dominantBaseline="middle" fontSize="15" fontStyle="italic" fill="var(--fg-3)">IV</text>
            </>
          )}

          {/* Gridlines */}
          {ints.map((g) => (
            <g key={`g${g}`}>
              <line x1={px(g)} y1={py(max)} x2={px(g)} y2={py(min)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(min)} y1={py(g)} x2={px(max)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}

          {/* Axes */}
          <line x1={px(min)} y1={py(0)} x2={px(max)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <line x1={px(0)} y1={py(max)} x2={px(0)} y2={py(min)} stroke="var(--fg-2)" strokeWidth={1.8} />
          <text x={px(max) + 6} y={py(0) + 4} fontSize="11" fill="var(--fg-3)">x</text>
          <text x={px(0) - 4} y={py(max) - 6} fontSize="11" fill="var(--fg-3)" textAnchor="end">y</text>

          {/* Axis number labels (skip 0) */}
          {ints.filter((g) => g !== 0 && g % (N > 12 ? 2 : 1) === 0).map((g) => (
            <g key={`lbl${g}`}>
              <text x={px(g)} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="middle">{g}</text>
              <text x={px(0) - 6} y={py(g) + 3} fontSize="9" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}
          <text x={px(0) - 6} y={py(0) + 13} fontSize="9" fill="var(--fg-3)" textAnchor="end">0</text>

          {/* Identify mode: clickable lattice points + selection */}
          {mode === "identify" && (
            <>
              {/* any reference points the question wants pre-marked */}
              {points.map((p, i) => (
                <g key={`ip${i}`}>
                  <circle cx={px(p.x)} cy={py(p.y)} r={5.5} fill={p.color || BLUE} />
                  <text x={px(p.x) + 8} y={py(p.y) - 8} fontSize="10" fill="var(--fg-1)">{p.label ? `${p.label} ` : ""}({p.x}, {p.y})</text>
                </g>
              ))}
              {ints.map((gx) => ints.map((gy) => (
                <circle
                  key={`p${gx}-${gy}`}
                  cx={px(gx)} cy={py(gy)} r={8}
                  fill="transparent" style={{ cursor: "pointer" }}
                  onClick={() => setSel({ x: gx, y: gy })}
                />
              )))}
              {sel && (
                <>
                  <line x1={px(0)} y1={py(sel.y)} x2={px(sel.x)} y2={py(sel.y)} stroke={ACCENT} strokeWidth={1.4} strokeDasharray="3 3" />
                  <line x1={px(sel.x)} y1={py(0)} x2={px(sel.x)} y2={py(sel.y)} stroke={ACCENT} strokeWidth={1.4} strokeDasharray="3 3" />
                  <circle cx={px(sel.x)} cy={py(sel.y)} r={5.5} fill={ACCENT} />
                </>
              )}
            </>
          )}

          {/* Distance mode: segment + endpoints */}
          {mode === "distance" && points.length >= 2 && (
            <>
              <line x1={px(points[0].x)} y1={py(points[0].y)} x2={px(points[1].x)} y2={py(points[1].y)} stroke={ACCENT} strokeWidth={2.5} />
              {points.map((p, i) => (
                <g key={`d${i}`}>
                  <circle cx={px(p.x)} cy={py(p.y)} r={5.5} fill={ACCENT} />
                  <text x={px(p.x) + 8} y={py(p.y) - 8} fontSize="10" fill="var(--fg-1)">({p.x}, {p.y})</text>
                </g>
              ))}
            </>
          )}

          {/* Reflect mode: source, mirror line, reflected image */}
          {mode === "reflect" && src && reflected && (
            <>
              {reflectAxis === "x"
                ? <line x1={px(min)} y1={py(0)} x2={px(max)} y2={py(0)} stroke={BLUE} strokeWidth={2.4} />
                : <line x1={px(0)} y1={py(max)} x2={px(0)} y2={py(min)} stroke={BLUE} strokeWidth={2.4} />}
              <circle cx={px(src.x)} cy={py(src.y)} r={5.5} fill={ACCENT} />
              <text x={px(src.x) + 8} y={py(src.y) - 8} fontSize="10" fill="var(--fg-1)">({src.x}, {src.y})</text>
              {revealed && (
                <>
                  <line x1={px(src.x)} y1={py(src.y)} x2={px(reflected.x)} y2={py(reflected.y)} stroke="var(--fg-3)" strokeWidth={1.4} strokeDasharray="3 3" />
                  <circle cx={px(reflected.x)} cy={py(reflected.y)} r={5.5} fill={BLUE} />
                  <text x={px(reflected.x) + 8} y={py(reflected.y) + 14} fontSize="10" fill="var(--fg-1)">({reflected.x}, {reflected.y})</text>
                </>
              )}
            </>
          )}

          {/* Plot mode: optional closed polygon through the points */}
          {mode === "plot" && polygon && points.length >= 3 && (
            <polygon
              points={points.map((p) => `${px(p.x)},${py(p.y)}`).join(" ")}
              fill={`${ACCENT}18`}
              stroke={ACCENT}
              strokeWidth={2}
              strokeLinejoin="round"
            />
          )}

          {/* Plot mode: labelled points */}
          {mode === "plot" && points.map((p, i) => (
            <g key={`pl${i}`}>
              <circle cx={px(p.x)} cy={py(p.y)} r={5.5} fill={p.color || ACCENT} />
              <text x={px(p.x) + 8} y={py(p.y) - 8} fontSize="10" fill="var(--fg-1)">{p.label ? `${p.label} ` : ""}({p.x}, {p.y})</text>
            </g>
          ))}
        </svg>
      </div>

      {/* Mode-specific footer */}
      {mode === "identify" && (
        <div className="mt-3 text-center text-[15px]" style={{ color: "var(--fg-1)" }}>
          {sel ? (
            <>
              Point: <b className="serif tabular" style={{ color: "var(--accent)" }}>({sel.x}, {sel.y})</b> — {sel.x} across, {sel.y} up
              {showQuadrants && (
                <div className="mt-1 text-[14px]" style={{ color: "var(--fg-1)" }}>
                  in <b style={{ color: BLUE }}>{quadrantOf(sel)}</b>
                </div>
              )}
            </>
          ) : (
            <span style={{ color: "var(--fg-3)" }}>Tap a grid intersection{showQuadrants ? " to see its coordinates and quadrant." : " to read its coordinates."}</span>
          )}
        </div>
      )}
      {mode === "distance" && points.length >= 2 && (
        <div className="mt-3 text-center text-[15px]" style={{ color: "var(--fg-1)" }}>
          Distance ={" "}
          <b className="serif tabular" style={{ color: "var(--accent)" }}>
            {points[0].x === points[1].x ? Math.abs(points[0].y - points[1].y) : Math.abs(points[0].x - points[1].x)}
          </b>{" "}units
        </div>
      )}
      {mode === "reflect" && src && reflected && (
        <div className="mt-4 flex items-center justify-center gap-3">
          <button type="button" onClick={() => setRevealed(false)} disabled={!revealed} aria-label="Reset" className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>
            <RotateCcw className="h-4 w-4" /> Reset
          </button>
          <button type="button" onClick={() => setRevealed(true)} disabled={revealed} className="gm-press rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}>
            Reflect across the {reflectAxis}-axis
          </button>
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {mode === "plot" && <>Each point is written as <b style={{ color: "var(--fg-1)" }}>(x, y)</b> — across first, then up.</>}
        {mode === "identify" && <>Read <b style={{ color: "var(--fg-1)" }}>across</b> for x, then <b style={{ color: "var(--fg-1)" }}>up</b> for y.</>}
        {mode === "quadrants" && <>The axes split the plane into four <b style={{ color: "var(--fg-1)" }}>quadrants</b>, numbered counter-clockwise from top-right.</>}
        {mode === "reflect" && <>Reflecting across an axis <b style={{ color: "var(--fg-1)" }}>flips the sign</b> of one coordinate.</>}
        {mode === "distance" && <>On a straight line, distance is the <b style={{ color: "var(--fg-1)" }}>difference</b> of the coordinates that change.</>}
      </div>
    </div>
  );
}
