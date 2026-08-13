"use client";

// A pictograph with a key — rows of repeated symbols, each standing for
// `key` things, with half-symbols when a row's value is half a key. This is
// the figure the pictograph lessons teach ABOUT; until 2026-08-13 those
// lessons described symbol rows in prose because no renderer existed.
import type { FigureSpec } from "@/lib/genmath-interactive";

export default function PictographView({ spec }: { spec: NonNullable<FigureSpec["pictograph"]> }) {
  const symbol = spec.symbol ?? "●";
  const color = spec.color ?? "#3b82f6";
  const key = Math.max(1, spec.key);

  return (
    <div className="gm-fade flex justify-center rounded-xl p-4" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
      <div>
        <table role="img" aria-label={`Pictograph, one ${symbol} means ${key}: ${spec.rows.map((r) => `${r.label} ${r.value}`).join(", ")}`}>
          <tbody>
            {spec.rows.map((row) => {
              const whole = Math.floor(row.value / key);
              const half = row.value - whole * key >= key / 2 - 1e-9 && row.value - whole * key > 0;
              return (
                <tr key={row.label}>
                  <td className="pr-3 text-right text-[12px] align-middle" style={{ color: "var(--fg-2)", whiteSpace: "nowrap" }}>
                    {row.label}
                  </td>
                  <td className="align-middle" style={{ fontSize: 20, letterSpacing: 3, color, lineHeight: 1.6 }}>
                    {Array.from({ length: whole }).map((_, i) => (
                      <span key={i}>{symbol}</span>
                    ))}
                    {half && (
                      // a half symbol: the same glyph clipped to its left half
                      <span
                        aria-hidden
                        style={{ display: "inline-block", width: "0.62em", overflow: "hidden", verticalAlign: "bottom" }}
                      >
                        {symbol}
                      </span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <p className="mt-2 text-[11px]" style={{ color: "var(--fg-3)" }}>
          <span style={{ color, fontSize: 14 }}>{symbol}</span> = {key}
        </p>
      </div>
    </div>
  );
}
