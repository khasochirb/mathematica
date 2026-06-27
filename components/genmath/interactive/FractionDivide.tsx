"use client";

import { useState } from "react";
import { type FractionDivideConfig, gcd } from "@/lib/genmath-interactive";

const SHADE = "#e8913c";

export default function FractionDivide({ config }: { config: FractionDivideConfig }) {
  const { dividend, divisor } = config;
  const [counted, setCounted] = useState(false);

  // common denominator so both fractions live on the same grid of cells
  const D = (dividend.den / gcd(dividend.den, divisor.den)) * divisor.den;
  const dn = (dividend.num * D) / dividend.den; // dividend in D-ths (shaded cells)
  const vn = (divisor.num * D) / divisor.den; // divisor in D-ths (cells per group)
  const answer = dn / vn; // how many divisor-pieces fit (whole when config is clean)

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="mb-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        How many <b style={{ color: "var(--fg-1)" }}>{divisor.num}/{divisor.den}</b> fit into <b style={{ color: "var(--fg-1)" }}>{dividend.num}/{dividend.den}</b>?
      </div>

      {/* the bar: D cells, dn shaded; when counted, group separators every vn cells */}
      <div className="flex w-full overflow-hidden rounded-lg" style={{ height: 48, border: "1px solid var(--line)", background: "var(--bg-2)" }}>
        {Array.from({ length: D }).map((_, i) => {
          const shaded = i < dn;
          const groupEnd = counted && shaded && (i + 1) % vn === 0 && i + 1 < dn;
          return (
            <div
              key={i}
              style={{
                flex: 1,
                background: shaded ? SHADE : "transparent",
                borderRight: groupEnd ? "3px solid var(--bg)" : i < D - 1 ? "1px solid var(--bg)" : "none",
                transition: "background .3s, border-color .3s",
              }}
            />
          );
        })}
      </div>

      {counted && (
        <div className="gm-fade mt-2 flex flex-wrap justify-center gap-1.5">
          {Array.from({ length: answer }).map((_, i) => (
            <span key={i} className="gm-pop rounded-full px-2 py-0.5 text-[11px]" style={{ background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)", animationDelay: `${i * 70}ms` }}>
              piece {i + 1}
            </span>
          ))}
        </div>
      )}

      <div
        role="status"
        aria-live="polite"
        className="gm-fade mt-3 rounded-xl px-4 py-3 text-center text-[13px]"
        style={{
          background: counted ? "var(--accent-wash)" : "var(--bg-2)",
          border: counted ? "1px solid var(--accent-line)" : "1px solid var(--line)",
          color: "var(--fg-1)",
          transition: "background .3s, border-color .3s",
        }}
      >
        {counted ? (
          <span>
            <b>{answer}</b> pieces fit → {dividend.num}/{dividend.den} ÷ {divisor.num}/{divisor.den} = <b style={{ color: "var(--accent)" }}>{answer}</b>.
          </span>
        ) : (
          <span>Mark off pieces the size of the divisor and count how many fit.</span>
        )}
      </div>

      <div className="mt-3 flex justify-center">
        <button
          type="button"
          onClick={() => setCounted((v) => !v)}
          aria-pressed={counted}
          className="gm-press inline-flex items-center gap-2 rounded-full px-6 py-3 text-[14px] font-medium"
          style={{
            background: counted ? "var(--bg-2)" : "var(--accent)",
            color: counted ? "var(--fg-2)" : "var(--accent-ink, #fff)",
            border: counted ? "1px solid var(--line)" : "1px solid var(--accent)",
            transition: "background .2s, color .2s",
          }}
        >
          {counted ? "Reset" : "Count how many fit"}
        </button>
      </div>
    </div>
  );
}
