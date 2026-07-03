"use client";

import { useState } from "react";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { translate, reflectX, reflectY, reflectYeqX, rotate, dilateOrigin } from "@/lib/geo";
import { type XY } from "@/lib/geo";
import { type TransformPlaneConfig } from "@/lib/genmath-interactive";

// One figure and its image under a single transformation on the coordinate
// plane. The preimage is drawn solid; tapping "Apply" reveals the image (dashed
// accent) with each vertex's coordinate mapping, so the rule (x, y) → (…) is
// something you SEE happen, not just read. Handles slides, flips, turns, and
// resizes — every transformation in the unit — from one declarative config.
const LABELS = ["A", "B", "C", "D"];

function apply(t: TransformPlaneConfig, p: XY): XY {
  switch (t.transform) {
    case "translate": return translate(p, t.dx ?? 0, t.dy ?? 0);
    case "reflectX": return reflectX(p);
    case "reflectY": return reflectY(p);
    case "reflectYeqX": return reflectYeqX(p);
    case "rotate": return rotate(p, t.deg ?? 90);
    case "dilate": return dilateOrigin(p, t.k ?? 2);
  }
}

function ruleText(t: TransformPlaneConfig): string {
  const sgn = (n: number) => (n >= 0 ? `+ ${n}` : `− ${-n}`);
  switch (t.transform) {
    case "translate": return `(x, y) → (x ${sgn(t.dx ?? 0)}, y ${sgn(t.dy ?? 0)})`;
    case "reflectX": return "(x, y) → (x, −y)";
    case "reflectY": return "(x, y) → (−x, y)";
    case "reflectYeqX": return "(x, y) → (y, x)";
    case "rotate": return t.deg === 180 ? "(x, y) → (−x, −y)" : t.deg === 270 ? "(x, y) → (y, −x)" : "(x, y) → (−y, x)";
    case "dilate": return `(x, y) → (${fmtK(t.k ?? 2)}x, ${fmtK(t.k ?? 2)}y)`;
  }
}

function nameText(t: TransformPlaneConfig): string {
  switch (t.transform) {
    case "translate": return "Translation (slide)";
    case "reflectX": return "Reflection over the x-axis (flip)";
    case "reflectY": return "Reflection over the y-axis (flip)";
    case "reflectYeqX": return "Reflection over y = x (flip)";
    case "rotate": return `Rotation ${t.deg ?? 90}° about the origin (turn)`;
    case "dilate": return `Dilation, scale factor ${fmtK(t.k ?? 2)} (resize)`;
  }
}

function fmtK(n: number): string {
  return Number.isInteger(n) ? n.toString() : n.toFixed(1).replace(/\.0$/, "");
}
function fmt(n: number): string {
  return Number.isInteger(n) ? n.toString() : (Math.round(n * 10) / 10).toString();
}

export default function TransformPlane({ config }: { config: TransformPlaneConfig }) {
  const color = config.color ?? GEO_ACCENT;
  const [shown, setShown] = useState(false);

  const pre: XY[] = config.shape ?? [{ x: 1, y: 1 }, { x: 4, y: 1 }, { x: 1, y: 3 }];
  const img = pre.map((p) => apply(config, p));
  const isRigid = config.transform !== "dilate";

  const min = config.min ?? -6;
  const max = config.max ?? 6;
  const N = max - min;
  const cell = 26;
  const pad = 20;
  const size = N * cell;
  const W = size + pad * 2;
  const px = (gx: number) => pad + (gx - min) * cell;
  const py = (gy: number) => pad + (max - gy) * cell;
  const ints = Array.from({ length: N + 1 }, (_, i) => min + i);
  const poly = (ps: XY[]) => ps.map((p) => `${px(p.x)},${py(p.y)}`).join(" ");
  const step = N > 12 ? 2 : 1;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex justify-center">
        <svg viewBox={`0 0 ${W} ${W}`} width="100%" style={{ maxWidth: 340 }} role="img" aria-label="Transformation on the coordinate plane">
          {/* Gridlines */}
          {ints.map((g) => (
            <g key={`g${g}`}>
              <line x1={px(g)} y1={py(max)} x2={px(g)} y2={py(min)} stroke="var(--line)" strokeWidth={1} />
              <line x1={px(min)} y1={py(g)} x2={px(max)} y2={py(g)} stroke="var(--line)" strokeWidth={1} />
            </g>
          ))}
          {/* Mirror line for reflections */}
          {config.transform === "reflectYeqX" && (
            <line x1={px(Math.max(min, -max))} y1={py(Math.max(min, -max))} x2={px(Math.min(max, max))} y2={py(Math.min(max, max))} stroke={GEO_BLUE} strokeWidth={1.6} strokeDasharray="5 4" />
          )}
          {/* Axes */}
          <line x1={px(min)} y1={py(0)} x2={px(max)} y2={py(0)} stroke="var(--fg-2)" strokeWidth={config.transform === "reflectX" && shown ? 2.4 : 1.8} />
          <line x1={px(0)} y1={py(max)} x2={px(0)} y2={py(min)} stroke="var(--fg-2)" strokeWidth={config.transform === "reflectY" && shown ? 2.4 : 1.8} />
          <text x={px(max) + 5} y={py(0) + 4} fontSize="11" fill="var(--fg-3)">x</text>
          <text x={px(0) - 4} y={py(max) - 5} fontSize="11" fill="var(--fg-3)" textAnchor="end">y</text>
          {/* Axis number labels */}
          {ints.filter((g) => g !== 0 && g % step === 0).map((g) => (
            <g key={`lbl${g}`}>
              <text x={px(g)} y={py(0) + 12} fontSize="8.5" fill="var(--fg-3)" textAnchor="middle">{g}</text>
              <text x={px(0) - 5} y={py(g) + 3} fontSize="8.5" fill="var(--fg-3)" textAnchor="end">{g}</text>
            </g>
          ))}

          {/* center marker for rotations/dilations */}
          {(config.transform === "rotate" || config.transform === "dilate") && (
            <circle cx={px(0)} cy={py(0)} r={3.4} fill={GEO_BLUE} />
          )}

          {/* dilation rays from origin through image vertices */}
          {config.transform === "dilate" && shown && pre.map((p, i) => (
            <line key={`ray${i}`} x1={px(0)} y1={py(0)} x2={px(img[i].x)} y2={py(img[i].y)} stroke="var(--fg-3)" strokeWidth={1} strokeDasharray="3 3" />
          ))}

          {/* image figure */}
          {shown && (
            <polygon points={poly(img)} fill={`${color}14`} stroke={color} strokeWidth={2.2} strokeDasharray="6 3" strokeLinejoin="round" />
          )}
          {/* preimage figure */}
          <polygon points={poly(pre)} fill="rgba(120,120,120,0.10)" stroke="var(--fg-1)" strokeWidth={2.2} strokeLinejoin="round" />

          {/* vertex labels */}
          {pre.map((p, i) => (
            <g key={`pl${i}`}>
              <circle cx={px(p.x)} cy={py(p.y)} r={2.8} fill="var(--fg-1)" />
              <text x={px(p.x) - 5} y={py(p.y) - 6} fontSize="12" fontStyle="italic" fontFamily="serif" fill="var(--fg-1)">{LABELS[i]}</text>
            </g>
          ))}
          {shown && img.map((p, i) => (
            <g key={`il${i}`}>
              <circle cx={px(p.x)} cy={py(p.y)} r={2.8} fill={color} />
              <text x={px(p.x) + 5} y={py(p.y) - 6} fontSize="12" fontStyle="italic" fontFamily="serif" fill={color}>{LABELS[i]}′</text>
            </g>
          ))}
        </svg>
      </div>

      <div className="mt-2 rounded-xl p-3 text-center text-[14px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        <div className="serif" style={{ color }}>{nameText(config)}</div>
        <div className="mt-1 serif tabular text-[15px]">{ruleText(config)}</div>
        {shown && (
          <div className="mt-2 text-[12px] tabular" style={{ color: "var(--fg-2)" }}>
            {pre.map((p, i) => (
              <span key={i} className="inline-block px-1.5">
                {LABELS[i]}({fmt(p.x)}, {fmt(p.y)}) → {LABELS[i]}′({fmt(img[i].x)}, {fmt(img[i].y)})
              </span>
            ))}
            <div className="mt-1" style={{ color: "var(--fg-3)" }}>
              {isRigid ? "Same size and shape — the image is congruent to the original." : "Same shape, different size — the image is similar to the original."}
            </div>
          </div>
        )}
      </div>

      <div className="mt-4 flex justify-center">
        <button
          type="button"
          onClick={() => setShown((v) => !v)}
          className="gm-press rounded-full px-5 py-2 text-[14px] font-medium"
          style={{ background: shown ? "var(--bg-2)" : "var(--accent)", border: "1px solid var(--accent)", color: shown ? "var(--fg)" : "var(--accent-ink, #fff)" }}
        >
          {shown ? "Reset" : `Apply the ${config.transform === "dilate" ? "dilation" : config.transform === "rotate" ? "rotation" : config.transform === "translate" ? "translation" : "reflection"}`}
        </button>
      </div>
    </div>
  );
}
