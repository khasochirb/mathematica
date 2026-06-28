"use client";

// A price bar for percent word problems. In "discount" mode the original-price
// bar splits into what you pay (accent) and the discount taken off (struck,
// faded). In "increase" mode the bar shows the original (accent) plus the tax
// or tip added on (blue), so the final total is original + added. Presentational.
const money = (x: number, c: string) =>
  `${c}${(Math.round(x * 100) / 100).toFixed(2).replace(/\.00$/, "")}`;

const BLUE = "#3b82f6";

export default function PercentChangeView({
  original,
  percent,
  mode,
  currency = "$",
  color = "#e8913c",
}: {
  original: number;
  percent: number;
  mode: "discount" | "increase";
  currency?: string;
  color?: string;
}) {
  const part = Math.round(original * (percent / 100) * 100) / 100; // discount or add
  const final = mode === "discount" ? original - part : original + part;
  const total = mode === "discount" ? original : final; // bar's full length
  const leftPct = mode === "discount" ? (final / total) * 100 : (original / total) * 100;
  const rightPct = 100 - leftPct;

  return (
    <div className="w-full" style={{ maxWidth: 380 }}>
      {/* the split bar — inline labels hide when a segment is too narrow to fit */}
      <div className="flex w-full overflow-hidden rounded-lg" style={{ height: 40, border: "1px solid var(--line)" }}>
        <div
          className="flex items-center justify-center"
          style={{ width: `${leftPct}%`, background: color, color: "#fff", fontSize: 13, transition: "width 160ms ease" }}
        >
          {leftPct >= 16 ? (mode === "discount" ? money(final, currency) : money(original, currency)) : ""}
        </div>
        <div
          className="flex items-center justify-center"
          style={{
            width: `${rightPct}%`,
            background: mode === "discount" ? "var(--bg-2)" : BLUE,
            color: mode === "discount" ? "var(--fg-3)" : "#fff",
            fontSize: 12,
            textDecoration: mode === "discount" ? "line-through" : "none",
            transition: "width 160ms ease",
          }}
        >
          {rightPct >= 16 ? (mode === "discount" ? `−${money(part, currency)}` : `+${money(part, currency)}`) : ""}
        </div>
      </div>

      {/* labels under each segment */}
      <div className="mt-1 flex w-full text-[10px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
        <span style={{ width: `${leftPct}%`, textAlign: "center" }}>
          {mode === "discount" ? "you pay" : "original"}
        </span>
        <span style={{ width: `${rightPct}%`, textAlign: "center" }}>
          {mode === "discount" ? `${percent}% off` : `+${percent}%`}
        </span>
      </div>

      {/* the equation */}
      <div className="mt-3 flex flex-wrap items-center justify-center gap-2 serif tabular" style={{ fontSize: 19, color: "var(--fg)" }}>
        {mode === "discount" ? (
          <>
            <span style={{ color: "var(--fg-3)", textDecoration: "line-through" }}>{money(original, currency)}</span>
            <span style={{ color: "var(--fg-3)" }}>−</span>
            <span>{money(part, currency)}</span>
            <span style={{ color: "var(--fg-3)" }}>=</span>
            <span className="rounded-lg px-2.5 py-0.5" style={{ background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{money(final, currency)}</span>
          </>
        ) : (
          <>
            <span>{money(original, currency)}</span>
            <span style={{ color: "var(--fg-3)" }}>+</span>
            <span>{money(part, currency)}</span>
            <span style={{ color: "var(--fg-3)" }}>=</span>
            <span className="rounded-lg px-2.5 py-0.5" style={{ background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}>{money(final, currency)}</span>
          </>
        )}
      </div>
    </div>
  );
}
