"use client";

import { ArrowUp, ArrowDown } from "lucide-react";

// Before/after bars for percent increase/decrease. Both bars share a scale
// (the larger amount = full width). The change is highlighted — extended in
// blue for an increase, struck/faded for a decrease — and the percent (always
// out of the ORIGINAL) shows when revealed. Presentational.
const money = (x: number, c: string) =>
  `${c}${(Math.round(x * 100) / 100).toFixed(2).replace(/\.00$/, "")}`;

const BLUE = "#3b82f6";

export default function PercentChangeFinderView({
  original,
  final,
  currency = "$",
  color = "#e8913c",
  showAnswer,
}: {
  original: number;
  final: number;
  currency?: string;
  color?: string;
  showAnswer: boolean;
}) {
  const max = Math.max(original, final) || 1;
  const isIncrease = final > original;
  const change = Math.abs(final - original);
  const pct = Math.round((change / original) * 1000) / 10; // one decimal if needed
  const pctLabel = Number.isInteger(pct) ? String(pct) : pct.toFixed(1);

  const Row = ({ label, amount }: { label: string; amount: number }) => (
    <div className="flex items-center gap-2">
      <span className="text-[11px] uppercase tracking-wide" style={{ width: 48, color: "var(--fg-3)" }}>{label}</span>
      <div className="relative flex-1 rounded-md" style={{ height: 24, background: "var(--bg-2)" }}>
        {/* the common (unchanged) part + the change region */}
        <div className="absolute left-0 top-0 h-full rounded-md" style={{ width: `${(Math.min(original, final) / max) * 100}%`, background: color, transition: "width 160ms ease" }} />
        {amount === final && isIncrease && (
          <div className="absolute top-0 h-full" style={{ left: `${(original / max) * 100}%`, width: `${(change / max) * 100}%`, background: BLUE }} />
        )}
        {amount === original && !isIncrease && (
          <div className="absolute top-0 h-full" style={{ left: `${(final / max) * 100}%`, width: `${(change / max) * 100}%`, background: "var(--bg-2)", border: "1px dashed var(--fg-3)" }} />
        )}
        <span className="absolute right-2 top-1/2 -translate-y-1/2 serif tabular text-[13px]" style={{ color: amount === Math.max(original, final) ? "#fff" : "var(--fg)" }}>
          {money(amount, currency)}
        </span>
      </div>
    </div>
  );

  return (
    <div className="w-full" style={{ maxWidth: 360 }}>
      <div className="space-y-2">
        <Row label="before" amount={original} />
        <Row label="after" amount={final} />
      </div>
      <div className="mt-3 flex items-center justify-center gap-2 text-[13px]" style={{ color: "var(--fg-2)" }}>
        change of <b className="serif tabular" style={{ color: "var(--fg)" }}>{money(change, currency)}</b> on {money(original, currency)}
      </div>
      {showAnswer && (
        <div className="gm-fade mt-2 flex justify-center">
          <span
            className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1 serif tabular"
            style={{ fontSize: 18, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}
          >
            {isIncrease ? <ArrowUp className="h-4 w-4" /> : <ArrowDown className="h-4 w-4" />}
            {pctLabel}% {isIncrease ? "increase" : "decrease"}
          </span>
        </div>
      )}
    </div>
  );
}
