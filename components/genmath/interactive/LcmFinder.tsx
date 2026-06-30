"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type LcmFinderConfig } from "@/lib/genmath-interactive";

function gcd(a: number, b: number): number {
  while (b) [a, b] = [b, a % b];
  return a;
}

// Two adjustable numbers, each shown as a skip-counting strip of its first
// several multiples. Multiples that appear in BOTH strips are highlighted, and
// the first (smallest) shared one is ringed — the least common multiple.
// Reusable: change either number and the strips and LCM update live.
export default function LcmFinder({ config }: { config: LcmFinderConfig }) {
  const { a: a0, b: b0, min = 2, max = 12, count = 6, color = "#5b8def" } = config;
  const [a, setA] = useState(a0);
  const [b, setB] = useState(b0);

  const lcm = (a / gcd(a, b)) * b;
  const multiples = (n: number) => Array.from({ length: count }, (_, i) => n * (i + 1));
  const inBoth = (m: number) => m % a === 0 && m % b === 0;

  const Strip = ({ n }: { n: number }) => (
    <div className="flex flex-wrap items-center gap-1.5">
      {multiples(n).map((m) => {
        const shared = inBoth(m);
        const isLcm = m === lcm;
        return (
          <span
            key={m}
            className="serif tabular grid place-items-center"
            style={{
              minWidth: 34,
              height: 30,
              padding: "0 8px",
              borderRadius: 7,
              fontSize: 14,
              background: shared ? color : "var(--bg-2)",
              color: shared ? "#fff" : "var(--fg-2)",
              border: isLcm ? "2px solid var(--fg)" : "1px solid var(--line)",
            }}
          >
            {m}
          </span>
        );
      })}
    </div>
  );

  const Stepper = ({ label, val, set }: { label: string; val: number; set: (f: (v: number) => number) => void }) => (
    <div className="flex items-center gap-2">
      <button
        type="button"
        onClick={() => set((v) => Math.max(min, v - 1))}
        disabled={val <= min}
        aria-label={`Decrease ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
      >
        <Minus className="h-4 w-4" />
      </button>
      <div className="serif tabular text-center" style={{ minWidth: 48, fontSize: 20, color: "var(--fg)" }}>
        {val}
      </div>
      <button
        type="button"
        onClick={() => set((v) => Math.min(max, v + 1))}
        disabled={val >= max}
        aria-label={`Increase ${label}`}
        className="gm-press grid h-10 w-10 place-items-center rounded-full disabled:opacity-35"
        style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Plus className="h-4 w-4" />
      </button>
    </div>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="flex flex-col gap-4">
        <div>
          <div className="mb-2 flex items-center justify-between">
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>Multiples of <b className="serif tabular" style={{ color: "var(--fg)" }}>{a}</b></span>
            <Stepper label="first number" val={a} set={setA} />
          </div>
          <Strip n={a} />
        </div>
        <div style={{ borderTop: "1px solid var(--line)" }} className="pt-4">
          <div className="mb-2 flex items-center justify-between">
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>Multiples of <b className="serif tabular" style={{ color: "var(--fg)" }}>{b}</b></span>
            <Stepper label="second number" val={b} set={setB} />
          </div>
          <Strip n={b} />
        </div>
      </div>

      <div className="mt-4 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        {lcm <= a * count || lcm <= b * count ? (
          <>
            Least common multiple of {a} and {b}:{" "}
            <b className="serif tabular" style={{ color: "var(--accent)" }}>LCM = {lcm}</b>
          </>
        ) : (
          <>
            LCM of {a} and {b} is <b className="serif tabular" style={{ color: "var(--accent)" }}>{lcm}</b> — keep skip-counting to reach it.
          </>
        )}
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Highlighted numbers appear in <b style={{ color: "var(--fg-1)" }}>both</b> lists; the ringed one is the <b style={{ color: "var(--fg-1)" }}>smallest</b>.
      </div>
    </div>
  );
}
