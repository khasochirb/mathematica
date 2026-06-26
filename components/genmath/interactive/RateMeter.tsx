"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type RateMeterConfig, rateValue } from "@/lib/genmath-interactive";

function formatRate(val: number): string {
  if (!isFinite(val)) return "—";
  const fixed = Number(val.toFixed(2));
  return String(fixed);
}

interface StepperProps {
  label: string;
  unit: string;
  value: number;
  min: number;
  max: number;
  step: number;
  onDec: () => void;
  onInc: () => void;
  accentPlus?: boolean;
}

function Stepper({ label, unit, value, min, max, onDec, onInc, accentPlus }: StepperProps) {
  return (
    <div
      className="flex flex-col gap-2 rounded-xl p-3"
      style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
    >
      <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
        {label}
      </div>
      <div className="flex items-center justify-between gap-2">
        <button
          type="button"
          onClick={onDec}
          disabled={value <= min}
          aria-label={`Decrease ${label}`}
          className="gm-press grid h-12 w-12 shrink-0 place-items-center rounded-full disabled:opacity-35"
          style={{
            background: "var(--bg-1)",
            border: "1px solid var(--line)",
            color: "var(--fg)",
          }}
        >
          <Minus className="h-5 w-5" />
        </button>

        <div className="flex min-w-0 flex-1 flex-col items-center text-center">
          <span
            className="serif tabular"
            style={{ fontSize: 30, lineHeight: 1, color: "var(--fg)" }}
          >
            {value}
          </span>
          <span className="mt-0.5 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {unit}
          </span>
        </div>

        <button
          type="button"
          onClick={onInc}
          disabled={value >= max}
          aria-label={`Increase ${label}`}
          className="gm-press grid h-12 w-12 shrink-0 place-items-center rounded-full disabled:opacity-35"
          style={
            accentPlus
              ? {
                  background: "var(--accent)",
                  border: "1px solid var(--accent)",
                  color: "var(--accent-ink, #fff)",
                }
              : {
                  background: "var(--bg-1)",
                  border: "1px solid var(--line)",
                  color: "var(--fg)",
                }
          }
        >
          <Plus className="h-5 w-5" />
        </button>
      </div>
    </div>
  );
}

export default function RateMeter({ config }: { config: RateMeterConfig }) {
  const [top, setTop] = useState(config.top);
  const [bottom, setBottom] = useState(config.bottom);

  const rate = rateValue(top, bottom);
  const rateDisplay = formatRate(rate);

  return (
    <div
      className="rounded-2xl p-4 sm:p-5"
      style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
    >
      {/* Two steppers */}
      <div className="flex flex-col gap-3">
        <Stepper
          label={config.topLabel}
          unit={config.topUnit}
          value={top}
          min={config.topStep}
          max={config.topMax}
          step={config.topStep}
          onDec={() => setTop((v) => Math.max(config.topStep, v - config.topStep))}
          onInc={() => setTop((v) => Math.min(config.topMax, v + config.topStep))}
          accentPlus
        />
        <Stepper
          label={config.bottomLabel}
          unit={config.bottomUnit}
          value={bottom}
          min={config.bottomStep}
          max={config.bottomMax}
          step={config.bottomStep}
          onDec={() => setBottom((v) => Math.max(config.bottomStep, v - config.bottomStep))}
          onInc={() => setBottom((v) => Math.min(config.bottomMax, v + config.bottomStep))}
        />
      </div>

      {/* Divider hint */}
      <div className="my-3 flex items-center gap-2">
        <div className="h-px flex-1" style={{ background: "var(--line)" }} />
        <span className="text-[12px]" style={{ color: "var(--fg-3)" }}>
          ÷
        </span>
        <div className="h-px flex-1" style={{ background: "var(--line)" }} />
      </div>

      {/* Live rate readout */}
      <div
        className="rounded-xl p-4 text-center"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
      >
        {/* Equation line */}
        <div className="flex flex-wrap items-baseline justify-center gap-x-1.5 gap-y-0.5">
          <span className="serif tabular" style={{ fontSize: 18, color: "var(--fg-2)" }}>
            {top}
          </span>
          <span className="text-[13px]" style={{ color: "var(--fg-3)" }}>
            {config.topUnit}
          </span>
          <span className="text-[13px]" style={{ color: "var(--fg-3)" }}>
            ÷
          </span>
          <span className="serif tabular" style={{ fontSize: 18, color: "var(--fg-2)" }}>
            {bottom}
          </span>
          <span className="text-[13px]" style={{ color: "var(--fg-3)" }}>
            {config.bottomUnit}
          </span>
          <span className="text-[13px]" style={{ color: "var(--fg-3)" }}>
            =
          </span>
        </div>

        {/* Big rate number */}
        <div
          key={rateDisplay}
          className="gm-fade mt-1.5 serif tabular"
          style={{ fontSize: 48, lineHeight: 1, color: "var(--accent)" }}
        >
          {rateDisplay}
        </div>
        <div
          className="mt-1 rounded-full px-3 py-0.5 text-[13px] inline-block"
          style={{
            background: "var(--accent-wash)",
            color: "var(--accent)",
            border: "1px solid var(--accent-line)",
          }}
        >
          {config.rateUnit}
        </div>
      </div>
    </div>
  );
}
