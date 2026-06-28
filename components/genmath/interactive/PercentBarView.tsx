"use client";

// A double bar for "percent of a number": a 0–100% scale stacked over a
// 0–whole value scale, filled to the same point, with a marker that reads both
// at once (25% of 80 lines up with 20). Presentational.
export default function PercentBarView({
  whole,
  percent,
  color = "#e8913c",
}: {
  whole: number;
  percent: number;
  color?: string;
}) {
  const p = Math.max(0, Math.min(100, percent));
  const value = Math.round((p / 100) * whole * 100) / 100;
  const fmt = (x: number) => (Number.isInteger(x) ? String(x) : x.toFixed(2).replace(/0+$/, "").replace(/\.$/, ""));
  const left = `${p}%`;

  const Bar = ({ fill, faded }: { fill: string; faded: string }) => (
    <div className="relative w-full rounded-full" style={{ height: 14, background: faded, overflow: "hidden" }}>
      <div className="h-full rounded-full" style={{ width: `${p}%`, background: fill, transition: "width 160ms ease" }} />
    </div>
  );

  return (
    <div className="w-full" style={{ maxWidth: 360 }}>
      {/* percent chip floating above the marker */}
      <div className="relative" style={{ height: 22 }}>
        <span
          className="absolute -translate-x-1/2 serif tabular rounded px-1.5 text-[12px]"
          style={{ left, top: 0, background: "var(--accent-wash)", color: "var(--accent)", whiteSpace: "nowrap" }}
        >
          {p}%
        </span>
      </div>
      <Bar fill="var(--accent-line)" faded="var(--bg-2)" />
      <div className="mt-0.5 flex justify-between text-[10px]" style={{ color: "var(--fg-3)" }}>
        <span>0%</span>
        <span>100%</span>
      </div>

      {/* connecting marker */}
      <div className="relative" style={{ height: 10 }}>
        <div className="absolute" style={{ left, top: 0, height: 10, width: 2, background: color, transform: "translateX(-1px)" }} />
      </div>

      <Bar fill={color} faded="var(--bg-2)" />
      <div className="mt-0.5 flex justify-between text-[10px]" style={{ color: "var(--fg-3)" }}>
        <span>0</span>
        <span>{fmt(whole)}</span>
      </div>
      {/* value chip below the marker */}
      <div className="relative" style={{ height: 22 }}>
        <span
          className="absolute -translate-x-1/2 serif tabular rounded px-1.5 text-[13px]"
          style={{ left, top: 2, background: "var(--bg-2)", color: "var(--fg)", border: "1px solid var(--line)", whiteSpace: "nowrap" }}
        >
          {fmt(value)}
        </span>
      </div>
    </div>
  );
}
