"use client";

import { useState } from "react";
import { ArrowLeftRight, Check, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { GEO_ACCENT, GEO_BLUE } from "@/components/genmath/interactive/GeoDiagram";
import { type ConditionalFlipConfig } from "@/lib/genmath-interactive";

// A conditional statement with its hypothesis and conclusion as colored chips.
// Tap "Flip" to swap them into the converse — and watch the truth value: a
// true statement's converse is NOT automatically true.
export default function ConditionalFlip({ config }: { config: ConditionalFlipConfig }) {
  const { hypothesis, conclusion, statementTrue, converseTrue, statementNote, converseNote } = config;
  const [flipped, setFlipped] = useState(false);

  const first = flipped ? conclusion : hypothesis;
  const second = flipped ? hypothesis : conclusion;
  const isTrue = flipped ? converseTrue : statementTrue;
  const note = flipped ? converseNote : statementNote;

  const Chip = ({ text, color, tag }: { text: string; color: string; tag: string }) => (
    <span className="inline-block rounded-lg px-2.5 py-1 align-middle" style={{ background: `${color}18`, border: `1px solid ${color}`, margin: "2px 0" }}>
      <span className="block text-[9px] uppercase tracking-wide" style={{ color }}>{tag}</span>
      <span className="q-math text-[13.5px]" style={{ color: "var(--fg)" }}>
        <MathText text={text} />
      </span>
    </span>
  );

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="text-center text-[11px] uppercase tracking-wide" style={{ color: "var(--fg-3)" }}>
        {flipped ? "The converse" : "The statement"}
      </div>

      <div className="mt-2 rounded-xl p-4 text-center leading-relaxed" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
        <span className="text-[15px]" style={{ color: "var(--fg-1)" }}>If </span>
        <Chip text={first} color={flipped ? GEO_BLUE : GEO_ACCENT} tag={flipped ? "was the conclusion" : "hypothesis"} />
        <span className="text-[15px]" style={{ color: "var(--fg-1)" }}> then </span>
        <Chip text={second} color={flipped ? GEO_ACCENT : GEO_BLUE} tag={flipped ? "was the hypothesis" : "conclusion"} />
      </div>

      {/* verdict */}
      <div
        className="mt-3 rounded-xl p-3 text-center"
        style={
          isTrue
            ? { background: "rgba(80,160,90,0.1)", border: "1px solid rgba(80,160,90,0.5)" }
            : { background: "rgba(200,60,60,0.08)", border: "1px solid rgb(200,60,60)" }
        }
      >
        <span className="inline-flex items-center gap-1.5 text-[15px]" style={{ color: "var(--fg)" }}>
          {isTrue ? <Check className="h-4 w-4" style={{ color: "rgb(70,150,80)" }} /> : <X className="h-4 w-4" style={{ color: "rgb(200,60,60)" }} />}
          <b>{isTrue ? "True" : "False"}</b>
        </span>
        <div className="q-math mt-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
          <MathText text={note} />
        </div>
      </div>

      <div className="mt-4 flex items-center justify-center">
        <button
          type="button"
          onClick={() => setFlipped((v) => !v)}
          className="gm-press inline-flex items-center gap-1.5 rounded-full px-5 py-2.5 text-[14px]"
          style={{ background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <ArrowLeftRight className="h-4 w-4" /> {flipped ? "Back to the statement" : "Flip to the converse"}
        </button>
      </div>

      <div className="mt-3 text-center text-[13px]" style={{ color: "var(--fg-2)" }}>
        The converse <b style={{ color: "var(--fg-1)" }}>swaps</b> the if-part and the then-part — and must be judged on its own.
      </div>
    </div>
  );
}
