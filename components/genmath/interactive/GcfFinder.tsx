"use client";

import { useState } from "react";
import { Minus, Plus } from "lucide-react";
import { type GcfFinderConfig } from "@/lib/genmath-interactive";

function factorsOf(n: number): number[] {
  const out: number[] = [];
  for (let d = 1; d <= n; d++) if (n % d === 0) out.push(d);
  return out;
}
function gcd(a: number, b: number): number {
  while (b) [a, b] = [b, a % b];
  return a;
}

// Two adjustable numbers. Each one's factor list is laid out as chips; the
// factors they SHARE are highlighted in both rows, and the largest shared chip
// is ringed — that is the greatest common factor. A reusable primitive: change
// either number and the overlap (and the GCF) updates live.
export default function GcfFinder({ config }: { config: GcfFinderConfig }) {
  const { a: a0, b: b0, min = 2, max = 24, color = "#e8913c" } = config;
  const [a, setA] = useState(a0);
  const [b, setB] = useState(b0);

  const g = gcd(a, b);
  const shared = new Set(factorsOf(a).filter((f) => b % f === 0));

  const Row = ({ n }: { n: number }) => (
    <div className="flex flex-wrap items-center gap-1.5">
      {factorsOf(n).map((f) => {
        const isShared = shared.has(f);
        const isGcf = f === g;
        return (
          <span
            key={f}
            className="serif tabular grid place-items-center"
            style={{
              minWidth: 30,
              height: 30,
              padding: "0 8px",
              borderRadius: 7,
              fontSize: 14,
              background: isShared ? color : "var(--bg-2)",
              color: isShared ? "#fff" : "var(--fg-2)",
              border: isGcf ? "2px solid var(--fg)" : "1px solid var(--line)",
            }}
          >
            {f}
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
      <div className="serif tabular text-center" style={{ minWidth: 56, fontSize: 20, color: "var(--fg)" }}>
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
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>Factors of <b className="serif tabular" style={{ color: "var(--fg)" }}>{a}</b></span>
            <Stepper label="first number" val={a} set={setA} />
          </div>
          <Row n={a} />
        </div>
        <div style={{ borderTop: "1px solid var(--line)" }} className="pt-4">
          <div className="mb-2 flex items-center justify-between">
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>Factors of <b className="serif tabular" style={{ color: "var(--fg)" }}>{b}</b></span>
            <Stepper label="second number" val={b} set={setB} />
          </div>
          <Row n={b} />
        </div>
      </div>

      <div className="mt-4 rounded-xl p-3 text-center text-[15px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
        Greatest common factor of {a} and {b}:{" "}
        <b className="serif tabular" style={{ color: "var(--accent)" }}>GCF = {g}</b>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        Highlighted chips are <b style={{ color: "var(--fg-1)" }}>shared</b> factors; the ringed one is the <b style={{ color: "var(--fg-1)" }}>greatest</b>.
      </div>
    </div>
  );
}
