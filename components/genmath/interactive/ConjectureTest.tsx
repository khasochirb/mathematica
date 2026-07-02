"use client";

import { useState } from "react";
import { Check, X, RotateCcw } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type ConjectureTestConfig } from "@/lib/genmath-interactive";

// Put a conjecture on trial. Tap each candidate to test it: passing cases pile
// up green — but a single red ✗ is a counterexample, and the conjecture is
// dead on the spot. (And if everything passes? Still not a proof.)
export default function ConjectureTest({ config }: { config: ConjectureTestConfig }) {
  const { conjecture, items } = config;
  const [tested, setTested] = useState<Set<number>>(new Set());

  const broken = items.some((it, i) => tested.has(i) && !it.holds);
  const allTested = tested.size === items.length;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="rounded-xl p-3 text-center" style={{ background: "var(--bg-2)", border: broken ? "1px solid rgb(200,60,60)" : "1px solid var(--line)" }}>
        <div className="text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>Conjecture on trial</div>
        <div className="q-math mt-1 text-[15px]" style={{ color: "var(--fg)", textDecoration: broken ? "line-through" : "none" }}>
          <MathText text={conjecture} />
        </div>
      </div>

      <div className="mt-4 flex flex-col gap-2">
        {items.map((it, i) => {
          const isTested = tested.has(i);
          return (
            <button
              key={i}
              type="button"
              disabled={isTested}
              onClick={() => setTested((s) => new Set(s).add(i))}
              className="gm-press rounded-xl px-4 py-3 text-left"
              style={{
                background: !isTested ? "var(--bg-2)" : it.holds ? "rgba(80,160,90,0.12)" : "rgba(200,60,60,0.12)",
                border: !isTested ? "1px solid var(--line)" : it.holds ? "1px solid rgba(80,160,90,0.5)" : "1px solid rgb(200,60,60)",
                cursor: isTested ? "default" : "pointer",
              }}
            >
              <div className="flex items-center gap-2.5">
                {isTested ? (
                  it.holds ? <Check className="h-4 w-4 flex-shrink-0" style={{ color: "rgb(70,150,80)" }} /> : <X className="h-4 w-4 flex-shrink-0" style={{ color: "rgb(200,60,60)" }} />
                ) : (
                  <span className="grid h-4 w-4 flex-shrink-0 place-items-center rounded-full text-[10px]" style={{ border: "1px solid var(--fg-3)", color: "var(--fg-3)" }}>?</span>
                )}
                <span className="q-math text-[14px]" style={{ color: "var(--fg)" }}>
                  <MathText text={it.label} />
                </span>
                {!isTested && <span className="ml-auto text-[12px]" style={{ color: "var(--fg-3)" }}>tap to test</span>}
              </div>
              {isTested && (
                <div className="q-math mt-1.5 pl-6 text-[13px]" style={{ color: "var(--fg-1)" }}>
                  <MathText text={it.note} />
                </div>
              )}
            </button>
          );
        })}
      </div>

      {(broken || allTested) && (
        <div
          className="mt-3 rounded-xl p-3 text-center text-[14px]"
          style={
            broken
              ? { background: "rgba(200,60,60,0.1)", border: "1px solid rgb(200,60,60)", color: "var(--fg)" }
              : { background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg-1)" }
          }
        >
          {broken ? (
            <>
              <b>Counterexample found — the conjecture is false.</b>
              <div className="mt-0.5 text-[13px]" style={{ color: "var(--fg-1)" }}>One failing case is all it takes.</div>
            </>
          ) : (
            <>
              <b>Every test passed…</b>
              <div className="mt-0.5 text-[13px]" style={{ color: "var(--fg-1)" }}>but examples alone never PROVE a conjecture — the next case could still fail.</div>
            </>
          )}
        </div>
      )}

      <div className="mt-4 flex items-center justify-center">
        <button
          type="button"
          onClick={() => setTested(new Set())}
          disabled={tested.size === 0}
          aria-label="Reset tests"
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-2.5 text-[14px] disabled:opacity-35"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        >
          <RotateCcw className="h-4 w-4" /> Reset
        </button>
      </div>
    </div>
  );
}
