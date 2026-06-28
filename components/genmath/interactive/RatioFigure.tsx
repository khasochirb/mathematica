"use client";

import { type FigureSpec, type FigureGroupSpec, divideShift } from "@/lib/genmath-interactive";
import FractionBar from "@/components/genmath/interactive/FractionBar";
import DecimalGridView from "@/components/genmath/interactive/DecimalGridView";
import DecimalNumberLineView from "@/components/genmath/interactive/DecimalNumberLineView";
import DecimalColumnView from "@/components/genmath/interactive/DecimalColumnView";
import DecimalAreaView from "@/components/genmath/interactive/DecimalAreaView";
import PercentBarView from "@/components/genmath/interactive/PercentBarView";
import PercentChangeView from "@/components/genmath/interactive/PercentChangeView";
import PercentChangeFinderView from "@/components/genmath/interactive/PercentChangeFinderView";
import IntegerLineView from "@/components/genmath/interactive/IntegerLineView";

function Token({ color }: { color: string }) {
  return (
    <span
      className="rounded-lg"
      style={{ width: 26, height: 26, background: color, border: "1px solid rgba(0,0,0,0.12)", boxShadow: "0 1px 2px rgba(0,0,0,0.08)" }}
    />
  );
}

function Cluster({ group }: { group: FigureGroupSpec }) {
  return (
    <div className="flex max-w-[150px] flex-wrap content-start justify-center gap-1.5">
      {Array.from({ length: group.count }).map((_, i) => (
        <Token key={i} color={group.color} />
      ))}
    </div>
  );
}

function GroupBox({ group, label }: { group: FigureGroupSpec; label?: string }) {
  return (
    <div className="rounded-xl p-3 text-center" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <Cluster group={group} />
      <div className="mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
        <span className="serif tabular" style={{ fontSize: 16, color: "var(--fg)" }}>{group.count}</span> {label ?? group.label}
      </div>
    </div>
  );
}

const JUICE = "#e8913c";
const WATER = "#9cc6e8";

// A cross-multiply diagram for a:b vs c:d — the two diagonals you "multiply across".
function CrossFigure({ a, b, c, d }: { a: number; b: number; c: number; d: number }) {
  const p1 = a * d; // left ratio's cross-value
  const p2 = c * b; // right ratio's cross-value
  const leftBigger = p1 > p2;
  const rightBigger = p2 > p1;
  const num = (x: number, y: number, val: number, color: string) => (
    <text x={x} y={y} textAnchor="middle" dominantBaseline="central" fontSize="26" fontFamily="Georgia, serif" fill={color}>
      {val}
    </text>
  );
  return (
    <div className="gm-fade flex flex-col items-center gap-2 rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <svg width="220" height="150" viewBox="0 0 220 150" role="img" aria-label={`Cross multiply ${a} to ${b} versus ${c} to ${d}`}>
        <defs>
          <marker id="rf-arrow-j" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill={JUICE} />
          </marker>
          <marker id="rf-arrow-w" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
            <path d="M0,0 L6,3 L0,6 Z" fill={WATER} />
          </marker>
        </defs>
        {/* row labels */}
        <text x="14" y="45" fontSize="11" fill="var(--fg-3)">juice</text>
        <text x="14" y="115" fontSize="11" fill="var(--fg-3)">water</text>
        {/* diagonals */}
        <line x1="78" y1="52" x2="142" y2="108" stroke={JUICE} strokeWidth="2.5" markerEnd="url(#rf-arrow-j)" opacity="0.85" />
        <line x1="142" y1="52" x2="78" y2="108" stroke={WATER} strokeWidth="2.5" markerEnd="url(#rf-arrow-w)" opacity="0.85" />
        {/* the four numbers */}
        {num(70, 42, a, "var(--fg)")}
        {num(150, 42, c, "var(--fg)")}
        {num(70, 118, b, "var(--fg)")}
        {num(150, 118, d, "var(--fg)")}
      </svg>
      <div className="flex items-center gap-3">
        <span className="rounded-lg px-3 py-1 text-[14px]" style={{ background: leftBigger ? "var(--accent-wash)" : "var(--bg-1)", border: leftBigger ? "1px solid var(--accent-line)" : "1px solid var(--line)", color: leftBigger ? "var(--accent)" : "var(--fg-1)", fontWeight: leftBigger ? 600 : 400 }}>
          {a} × {d} = {p1}
        </span>
        <span className="rounded-lg px-3 py-1 text-[14px]" style={{ background: rightBigger ? "var(--accent-wash)" : "var(--bg-1)", border: rightBigger ? "1px solid var(--accent-line)" : "1px solid var(--line)", color: rightBigger ? "var(--accent)" : "var(--fg-1)", fontWeight: rightBigger ? 600 : 400 }}>
          {c} × {b} = {p2}
        </span>
      </div>
      <div className="text-[12px]" style={{ color: "var(--fg-2)" }}>
        bigger product = stronger mix
      </div>
    </div>
  );
}

// Two read-only mixes side by side — so a "which is more orange" question shows BOTH.
function CompareMixFigure({ mixes }: { mixes: { a: number; b: number; label?: string }[] }) {
  const Swatch = ({ m }: { m: { a: number; b: number; label?: string } }) => (
    <div className="flex flex-col items-center gap-1.5">
      <div className="flex flex-wrap content-start justify-center gap-1" style={{ maxWidth: 96 }}>
        {Array.from({ length: m.a }).map((_, i) => (
          <span key={`j${i}`} className="rounded" style={{ width: 16, height: 16, background: JUICE, border: "1px solid rgba(0,0,0,0.1)" }} />
        ))}
        {Array.from({ length: m.b }).map((_, i) => (
          <span key={`w${i}`} className="rounded" style={{ width: 16, height: 16, background: WATER, border: "1px solid rgba(0,0,0,0.1)" }} />
        ))}
      </div>
      <span className="serif tabular" style={{ fontSize: 17, color: "var(--fg)" }}>
        {m.a} : {m.b}
      </span>
      {m.label && <span className="text-[11px]" style={{ color: "var(--fg-3)" }}>{m.label}</span>}
    </div>
  );
  return (
    <div className="gm-fade flex items-center justify-center gap-5 rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <Swatch m={mixes[0]} />
      <span className="text-[12px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>vs</span>
      <Swatch m={mixes[1]} />
    </div>
  );
}

export default function RatioFigure({ figure }: { figure: FigureSpec }) {
  const { mode } = figure;
  const groups = figure.groups ?? [];

  if (mode === "cross" && figure.cross) {
    return <CrossFigure {...figure.cross} />;
  }

  if (mode === "compareMix" && figure.mixes && figure.mixes.length >= 2) {
    return <CompareMixFigure mixes={figure.mixes} />;
  }

  if (mode === "fractionBar" && figure.fraction) {
    const { num, den, label } = figure.fraction;
    return (
      <div className="gm-fade w-full max-w-[320px] rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <FractionBar num={num} den={den} />
        <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="serif tabular" style={{ fontSize: 17, color: "var(--fg)" }}>{num}/{den}</span>
          {label ? ` — ${label}` : ""}
        </div>
      </div>
    );
  }

  if (mode === "decimalGrid" && figure.decimal) {
    const { value, label } = figure.decimal;
    const hundredths = Math.round(value * 100);
    return (
      <div className="gm-fade rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="flex justify-center">
          <DecimalGridView hundredths={hundredths} size={180} />
        </div>
        <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="serif tabular" style={{ fontSize: 17, color: "var(--fg)" }}>{value.toFixed(2)}</span>
          {" = "}
          <span className="serif tabular" style={{ color: "var(--fg)" }}>{hundredths}/100</span>
          {label ? ` — ${label}` : ""}
        </div>
      </div>
    );
  }

  if (mode === "numberLine" && figure.numberLine) {
    const { min, max, points } = figure.numberLine;
    return (
      <div className="gm-fade w-full max-w-[360px] rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="flex justify-center">
          <DecimalNumberLineView min={min} max={max} points={points} />
        </div>
      </div>
    );
  }

  if (mode === "decimalColumn" && figure.column) {
    const { a, b, op } = figure.column;
    return (
      <div className="gm-fade rounded-xl px-6 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <DecimalColumnView a={a} b={b} op={op} showAnswer />
      </div>
    );
  }

  if (mode === "decimalArea" && figure.area) {
    const { a, b } = figure.area;
    const aT = Math.round(a * 10);
    const bT = Math.round(b * 10);
    return (
      <div className="gm-fade rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="flex justify-center">
          <DecimalAreaView aTenths={aT} bTenths={bT} size={180} />
        </div>
        <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="serif tabular" style={{ fontSize: 17, color: "var(--fg)" }}>{a.toFixed(1)} × {b.toFixed(1)} = {(a * b).toFixed(2)}</span>
          {" — "}{aT * bT} of 100 squares
        </div>
      </div>
    );
  }

  if (mode === "divideChain" && figure.divide) {
    const { dividend, divisor } = figure.divide;
    const { shifts, scaledDividend, scaledDivisor, quotient } = divideShift(dividend, divisor);
    const f = (x: number) => x.toFixed(6).replace(/0+$/, "").replace(/\.$/, "");
    return (
      <div className="gm-fade flex flex-col items-center gap-1.5 rounded-xl px-6 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <div className="flex flex-wrap items-center justify-center gap-2.5 serif tabular" style={{ fontSize: 22, color: "var(--fg)" }}>
          <span>{f(dividend)} ÷ {f(divisor)}</span>
          {shifts > 0 && (
            <>
              <span style={{ color: "var(--fg-3)" }}>=</span>
              <span>{f(scaledDividend)} ÷ {f(scaledDivisor)}</span>
            </>
          )}
          <span style={{ color: "var(--fg-3)" }}>=</span>
          <span style={{ color: "var(--accent)" }}>{f(quotient)}</span>
        </div>
        {shifts > 0 && (
          <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
            ×10{shifts > 1 ? ` (${shifts} times)` : ""} on both
          </div>
        )}
      </div>
    );
  }

  if (mode === "percentBar" && figure.percentBar) {
    const { whole, percent } = figure.percentBar;
    const value = Math.round((percent / 100) * whole * 100) / 100;
    const fmt = (x: number) => (Number.isInteger(x) ? String(x) : x.toFixed(2).replace(/0+$/, "").replace(/\.$/, ""));
    return (
      <div className="gm-fade flex flex-col items-center gap-2 rounded-xl px-6 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <PercentBarView whole={whole} percent={percent} />
        <div className="text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="serif tabular" style={{ fontSize: 16, color: "var(--fg)" }}>{percent}% of {fmt(whole)} = {fmt(value)}</span>
        </div>
      </div>
    );
  }

  if (mode === "percentChange" && figure.percentChange) {
    const { original, percent, mode: m, currency } = figure.percentChange;
    return (
      <div className="gm-fade flex justify-center rounded-xl px-6 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <PercentChangeView original={original} percent={percent} mode={m} currency={currency} />
      </div>
    );
  }

  if (mode === "percentChangeFinder" && figure.percentChangeFinder) {
    const { original, final, currency } = figure.percentChangeFinder;
    return (
      <div className="gm-fade flex justify-center rounded-xl px-6 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <PercentChangeFinderView original={original} final={final} currency={currency} showAnswer />
      </div>
    );
  }

  if (mode === "integerLine" && figure.integerLine) {
    const { min, max, points } = figure.integerLine;
    return (
      <div className="gm-fade flex justify-center rounded-xl px-4 py-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <IntegerLineView min={min} max={max} points={points} />
      </div>
    );
  }

  // Plain side-by-side groups (used on teach pages).
  if (mode === "groups") {
    return (
      <div className="gm-fade flex flex-wrap items-start justify-center gap-5 rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        {groups.map((g, i) => (
          <div key={i} className="text-center">
            <Cluster group={g} />
            <div className="mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
              <span className="serif tabular" style={{ fontSize: 16, color: "var(--fg)" }}>{g.count}</span> {g.label}
            </div>
          </div>
        ))}
      </div>
    );
  }

  // PART-TO-PART: two clearly separated, boxed groups with a colon between.
  if (mode === "partToPart") {
    return (
      <div className="gm-fade flex flex-col items-center gap-1.5">
        <span className="rounded-full px-2.5 py-0.5 text-[11px] uppercase tracking-wide" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-3)" }}>
          group to group
        </span>
        <div className="flex items-center justify-center gap-2">
          <GroupBox group={groups[0]} />
          <span className="serif" style={{ fontSize: 30, color: "var(--fg-3)" }}>:</span>
          <GroupBox group={groups[1]} />
        </div>
      </div>
    );
  }

  // PART-TO-WHOLE: every item shown in real colour, all enclosed in a "Total = N"
  // box; the highlighted part sits in its own inner box, so "part of the whole" is literal.
  const partIdx = figure.highlightIndex ?? 0;
  const total = groups.reduce((s, g) => s + g.count, 0);
  const part = groups[partIdx];
  const rest = groups.filter((_, i) => i !== partIdx);
  return (
    <div className="gm-fade flex flex-col items-center gap-1.5">
      <span className="rounded-full px-2.5 py-0.5 text-[11px] uppercase tracking-wide" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-3)" }}>
        group to total
      </span>
      <div className="relative rounded-2xl p-4 pt-7" style={{ background: "var(--bg-2)", border: "2px dashed var(--fg-3)" }}>
        <span className="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-full px-3 py-0.5 text-[12px]" style={{ background: "var(--fg-2)", color: "var(--bg)" }}>
          Total = {total}
        </span>
        <div className="flex flex-wrap items-center justify-center gap-2">
          {/* the highlighted part, in its own box */}
          <div className="rounded-xl p-2 text-center" style={{ background: "var(--accent-wash)", border: "2px solid var(--accent)" }}>
            <Cluster group={part} />
            <div className="mt-1 text-[11px]" style={{ color: "var(--accent)" }}>
              <span className="serif tabular" style={{ fontSize: 15 }}>{part.count}</span> {part.label}
            </div>
          </div>
          {/* the rest of the whole */}
          {rest.map((g, i) => (
            <div key={i} className="text-center">
              <Cluster group={g} />
              <div className="mt-1 text-[11px]" style={{ color: "var(--fg-3)" }}>
                <span className="serif tabular" style={{ fontSize: 15 }}>{g.count}</span> {g.label}
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="text-[12px]" style={{ color: "var(--fg-2)" }}>
        <span className="serif tabular" style={{ fontSize: 16, color: "var(--accent)" }}>{part.count}</span> {part.label}
        {" "}out of{" "}
        <span className="serif tabular" style={{ fontSize: 16, color: "var(--fg)" }}>{total}</span> total
      </div>
    </div>
  );
}
