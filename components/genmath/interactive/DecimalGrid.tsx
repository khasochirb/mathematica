"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type DecimalGridConfig } from "@/lib/genmath-interactive";
import DecimalGridView from "@/components/genmath/interactive/DecimalGridView";

export default function DecimalGrid({ config }: { config: DecimalGridConfig }) {
  const { start = 0, color = "#e8913c" } = config;
  const [h, setH] = useState(Math.max(0, Math.min(100, Math.round(start * 100))));

  const tenths = Math.floor(h / 10);
  const hundredths = h % 10;
  const value = (h / 100).toFixed(2);

  const step = (d: number) => setH((v) => Math.max(0, Math.min(100, v + d)));

  const Stepper = ({
    label,
    sub,
    onDown,
    onUp,
    downDisabled,
    upDisabled,
  }: {
    label: string;
    sub: string;
    onDown: () => void;
    onUp: () => void;
    downDisabled: boolean;
    upDisabled: boolean;
  }) => (
    <div className="flex items-center gap-2.5">
      <button
        type="button"
        onClick={onDown}
        disabled={downDisabled}
        aria-label={`One fewer ${label}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-5 w-5" />
      </button>
      <div className="text-center" style={{ minWidth: 78 }}>
        <div className="serif tabular" style={{ fontSize: 18, color: "var(--fg)" }}>
          {label}
        </div>
        <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
          {sub}
        </div>
      </div>
      <button
        type="button"
        onClick={onUp}
        disabled={upDisabled}
        aria-label={`One more ${label}`}
        className="gm-press grid h-11 w-11 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-5 w-5" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      {/* the grid — one whole, cut into 100 */}
      <div className="flex justify-center">
        <DecimalGridView hundredths={h} color={color} />
      </div>

      <div className="mt-2 text-center text-[12px]" style={{ color: "var(--fg-2)" }}>
        the whole = 100 small squares
      </div>

      {/* readout: decimal = fraction, with the place-value split */}
      <div className="mt-3 flex flex-wrap items-center justify-center gap-3">
        <span className="serif tabular" style={{ fontSize: 26, color: "var(--fg)" }}>
          {value}
        </span>
        <span style={{ color: "var(--fg-3)" }}>=</span>
        <span
          className="serif tabular rounded-lg px-3 py-1"
          style={{ fontSize: 22, background: "var(--accent-wash)", color: "var(--accent)", border: "1px solid var(--accent-line)" }}
        >
          {h}/100
        </span>
      </div>

      <div className="mt-2 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        <b style={{ color: "var(--fg-1)" }}>{tenths}</b> tenth{tenths === 1 ? "" : "s"}
        {" + "}
        <b style={{ color: "var(--fg-1)" }}>{hundredths}</b> hundredth{hundredths === 1 ? "" : "s"}
      </div>

      {/* two steppers — a tenth (whole column) and a hundredth (one square) */}
      <div className="mt-4 flex flex-wrap items-center justify-center gap-x-6 gap-y-3">
        <Stepper
          label="tenth"
          sub="+0.1"
          onDown={() => step(-10)}
          onUp={() => step(10)}
          downDisabled={h < 10}
          upDisabled={h > 90}
        />
        <Stepper
          label="hundredth"
          sub="+0.01"
          onDown={() => step(-1)}
          onUp={() => step(1)}
          downDisabled={h <= 0}
          upDisabled={h >= 100}
        />
      </div>
    </div>
  );
}
