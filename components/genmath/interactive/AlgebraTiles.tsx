"use client";

import { useState } from "react";
import { Minus, Plus, Check } from "lucide-react";
import { type AlgebraTilesConfig } from "@/lib/genmath-interactive";

// Visualizes an expression as tiles: each "x" is a wide accent tile (an unknown
// amount), each "1" is a small unit square. Two modes:
//  - build:   steppers add/remove x-tiles and unit-tiles; the expression ax + b
//             is written underneath.
//  - collect: the tiles start scattered (x's and units interleaved). Tapping
//             "Collect like terms" groups them, revealing ax + b — combining
//             like terms made physical.
function expr(a: number, b: number): string {
  const xPart = a === 0 ? "" : a === 1 ? "x" : `${a}x`;
  const bPart = b === 0 ? "" : `${b}`;
  if (xPart && bPart) return `${xPart} + ${bPart}`;
  return xPart || bPart || "0";
}

export default function AlgebraTiles({ config }: { config: AlgebraTilesConfig }) {
  const { x: x0, units: u0, mode = "build", maxX = 5, maxUnits = 8, color = "#e8913c" } = config;
  const [x, setX] = useState(x0);
  const [units, setUnits] = useState(u0);
  const [collected, setCollected] = useState(false);

  const XTile = () => (
    <span
      className="serif grid place-items-center"
      style={{ width: 46, height: 32, borderRadius: 7, background: color, color: "#fff", fontSize: 15, fontStyle: "italic" }}
    >
      x
    </span>
  );
  const UnitTile = () => (
    <span style={{ width: 22, height: 22, borderRadius: 5, background: "var(--bg-2)", border: "1px solid var(--line)", display: "inline-block" }} />
  );

  // Scattered order for collect mode: interleave x's and units.
  const scattered: ("x" | "u")[] = [];
  {
    let xi = x, ui = units, turn = 0;
    while (xi > 0 || ui > 0) {
      if (turn % 2 === 0 && xi > 0) { scattered.push("x"); xi--; }
      else if (ui > 0) { scattered.push("u"); ui--; }
      else if (xi > 0) { scattered.push("x"); xi--; }
      turn++;
    }
  }

  const showGrouped = mode === "build" || collected;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="min-h-[80px] rounded-xl p-3 flex flex-wrap items-center justify-center gap-2" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {showGrouped ? (
          <>
            {Array.from({ length: x }).map((_, i) => <XTile key={`x${i}`} />)}
            {x > 0 && units > 0 && <span className="serif" style={{ color: "var(--fg-3)", fontSize: 18, padding: "0 4px" }}>+</span>}
            <span className="flex flex-wrap items-center gap-1" style={{ maxWidth: 180 }}>
              {Array.from({ length: units }).map((_, i) => <UnitTile key={`u${i}`} />)}
            </span>
          </>
        ) : (
          scattered.map((t, i) => (t === "x" ? <XTile key={i} /> : <UnitTile key={i} />))
        )}
      </div>

      <div className="mt-3 text-center serif tabular" style={{ fontSize: 20, color: "var(--fg)" }}>
        {showGrouped ? (
          <span style={{ color: collected || mode === "build" ? "var(--accent)" : "var(--fg)" }}>{expr(x, units)}</span>
        ) : (
          <span style={{ color: "var(--fg-3)" }}>collect to simplify…</span>
        )}
      </div>

      {mode === "build" ? (
        <div className="mt-4 flex items-center justify-around gap-3">
          <div className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>x-tiles</div>
            <div className="mt-1 flex items-center gap-2">
              <button type="button" onClick={() => setX((v) => Math.max(0, v - 1))} disabled={x <= 0} aria-label="Fewer x" className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
              <div className="serif tabular text-center" style={{ minWidth: 28, fontSize: 18, color: "var(--fg)" }}>{x}</div>
              <button type="button" onClick={() => setX((v) => Math.min(maxX, v + 1))} disabled={x >= maxX} aria-label="More x" className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
            </div>
          </div>
          <div className="text-center">
            <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>units</div>
            <div className="mt-1 flex items-center gap-2">
              <button type="button" onClick={() => setUnits((v) => Math.max(0, v - 1))} disabled={units <= 0} aria-label="Fewer units" className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}><Minus className="h-4 w-4" /></button>
              <div className="serif tabular text-center" style={{ minWidth: 28, fontSize: 18, color: "var(--fg)" }}>{units}</div>
              <button type="button" onClick={() => setUnits((v) => Math.min(maxUnits, v + 1))} disabled={units >= maxUnits} aria-label="More units" className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Plus className="h-4 w-4" /></button>
            </div>
          </div>
        </div>
      ) : (
        <div className="mt-4 flex items-center justify-center gap-3">
          <button type="button" onClick={() => setCollected(false)} disabled={!collected} className="gm-press rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}>Scatter</button>
          <button type="button" onClick={() => setCollected(true)} disabled={collected} className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px] disabled:opacity-35" style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}><Check className="h-4 w-4" /> Collect like terms</button>
        </div>
      )}

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        {mode === "build"
          ? <>Each <b style={{ color: "var(--accent)" }}>x</b>-tile is one unknown; each small square is <b style={{ color: "var(--fg-1)" }}>1</b>.</>
          : <>Group the <b style={{ color: "var(--accent)" }}>x</b>-tiles together and the units together — that's combining <b style={{ color: "var(--fg-1)" }}>like terms</b>.</>}
      </div>
    </div>
  );
}
