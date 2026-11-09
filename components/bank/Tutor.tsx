"use client";

import { useState } from "react";
import { BookOpen, ChevronDown, ChevronRight, Lightbulb, Stethoscope } from "lucide-react";
import MathText from "@/components/esh/MathText";
import type { BankStep } from "@/lib/problem-bank";

// The pieces that let a bank problem teach on its own, for a student working
// with no teacher (Khas, 1 Nov 2026: "students can learn everything without
// any teacher's help"). Each is optional and renders nothing without data, so
// units that have not been authored with tutoring look exactly as before.

/** "How to solve this type": the form's method as a checklist, on demand. */
export function MethodCard({ method, mn }: { method?: string[]; mn: boolean }) {
  const [open, setOpen] = useState(false);
  if (!method || method.length === 0) return null;
  return (
    <div className="mt-3">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        className="inline-flex items-center gap-1.5 text-[12.5px]"
        style={{ color: "var(--accent)" }}
        aria-expanded={open}
      >
        <BookOpen className="h-3.5 w-3.5" />
        {mn ? "Энэ төрлийн бодлогыг яаж бодох вэ?" : "How do you solve this type?"}
        {open ? <ChevronDown className="h-3.5 w-3.5" /> : <ChevronRight className="h-3.5 w-3.5" />}
      </button>
      {open && (
        <ol className="mt-2 rounded-xl p-3.5 space-y-1.5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
          {method.map((m, i) => (
            <li key={i} className="flex gap-2.5 text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
              <span className="mono text-[12px] mt-0.5" style={{ color: "var(--accent)", minWidth: 14 }}>{i + 1}</span>
              <span><MathText text={m} /></span>
            </li>
          ))}
        </ol>
      )}
    </div>
  );
}

/** Hints, mildest first, one per click. Free: asking is part of learning. */
export function HintPanel({ hints, mn, disabled }: { hints?: string[]; mn: boolean; disabled?: boolean }) {
  const [shown, setShown] = useState(0);
  if (!hints || hints.length === 0) return null;
  return (
    <div className="mt-4 space-y-2">
      {hints.slice(0, shown).map((h, i) => (
        <div key={i} className="flex gap-2.5 rounded-xl p-3" style={{ background: "rgba(216,150,32,0.08)", border: "1px solid rgba(216,150,32,0.35)" }}>
          <Lightbulb className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "var(--warn, #d89620)" }} />
          <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
            <span className="mono text-[11px] mr-1.5" style={{ color: "var(--fg-3)" }}>
              {mn ? `Сануулга ${i + 1}` : `Hint ${i + 1}`}
            </span>
            <MathText text={h} />
          </p>
        </div>
      ))}
      {shown < hints.length && !disabled && (
        <button
          type="button"
          onClick={() => setShown((n) => n + 1)}
          className="inline-flex items-center gap-1.5 text-[12.5px]"
          style={{ color: "var(--warn, #d89620)" }}
        >
          <Lightbulb className="h-3.5 w-3.5" />
          {shown === 0
            ? mn ? "Сануулга авах" : "Get a hint"
            : mn ? "Дараагийн сануулга" : "Next hint"}
          <span style={{ color: "var(--fg-3)" }}>({shown + 1}/{hints.length})</span>
        </button>
      )}
    </div>
  );
}

/** What a wrong answer most likely means, said the way a teacher would. */
export function Diagnosis({ text, mn }: { text: string; mn: boolean }) {
  return (
    <div className="mt-4 flex gap-2.5 rounded-xl p-3.5" style={{ background: "rgba(215,80,63,0.06)", border: "1px solid rgba(215,80,63,0.35)" }}>
      <Stethoscope className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "#c05a49" }} />
      <div>
        <div className="eyebrow mb-1" style={{ color: "#c05a49" }}>{mn ? "Алдаа хаана байна вэ?" : "What went wrong?"}</div>
        <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
          <MathText text={text} />
        </p>
      </div>
    </div>
  );
}

/**
 * The solution one step at a time. A student who has just got it wrong
 * learns more from finding the next move themselves than from reading the
 * whole page, so steps open one by one; "show all" is there for review.
 */
export function StepSolution({ steps, answer, mn }: { steps: BankStep[]; answer: string; mn: boolean }) {
  const [shown, setShown] = useState(1);
  const all = shown >= steps.length;
  return (
    <div className="mt-4 rounded-xl p-4" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="eyebrow mb-3">{mn ? "Алхам алхмаар бодолт" : "Step-by-step solution"}</div>
      <ol className="space-y-3">
        {steps.slice(0, shown).map((s, i) => (
          <li key={i} className="gm-fade flex gap-3">
            <span
              className="mono grid h-6 w-6 flex-shrink-0 place-items-center rounded-full text-[11px]"
              style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
            >
              {i + 1}
            </span>
            <div className="min-w-0">
              <p className="text-[15px] leading-relaxed" style={{ color: "var(--fg)" }}>
                <MathText text={s.do} />
              </p>
              {s.why && (
                <p className="mt-0.5 text-[13px] leading-relaxed" style={{ color: "var(--fg-2)" }}>
                  <MathText text={s.why} />
                </p>
              )}
            </div>
          </li>
        ))}
      </ol>
      {all ? (
        <p className="mt-4 text-[14px]" style={{ color: "var(--fg-1)" }}>
          <b>{mn ? "Хариу: " : "Answer: "}</b>
          <MathText text={answer} />
        </p>
      ) : (
        <div className="mt-4 flex items-center gap-4">
          <button type="button" onClick={() => setShown((n) => n + 1)} className="btn btn-line text-[13px]">
            {mn ? "Дараагийн алхам" : "Next step"} ({shown + 1}/{steps.length})
          </button>
          <button
            type="button"
            onClick={() => setShown(steps.length)}
            className="text-[12px]"
            style={{ color: "var(--fg-3)", textDecoration: "underline", textUnderlineOffset: 3 }}
          >
            {mn ? "Бүгдийг харах" : "Show all"}
          </button>
        </div>
      )}
    </div>
  );
}

/** The bank's header: what the skill is, what goes wrong, what mastery looks
 *  like (problem-bank-authoring §1), so a student knows the target before
 *  starting. */
export function MasteryHeader({
  mastery,
  calculator,
  mn,
}: {
  mastery?: { skill: string; mistakes: string[]; canDo: string };
  calculator?: boolean;
  mn: boolean;
}) {
  if (!mastery) return null;
  return (
    <div className="mt-4 rounded-xl p-4 space-y-3" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div>
        <div className="eyebrow mb-1">{mn ? "Энэ сэдэвт сурах зүйл" : "What you will learn"}</div>
        <p className="text-[14.5px] leading-relaxed" style={{ color: "var(--fg)" }}><MathText text={mastery.skill} /></p>
      </div>
      {mastery.mistakes.length > 0 && (
        <div>
          <div className="eyebrow mb-1">{mn ? "Ихэвчлэн гаргадаг алдаа" : "Where students usually slip"}</div>
          <ul className="space-y-1">
            {mastery.mistakes.map((m, i) => (
              <li key={i} className="flex gap-2 text-[13.5px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
                <span style={{ color: "#c05a49" }}>•</span>
                <span><MathText text={m} /></span>
              </li>
            ))}
          </ul>
        </div>
      )}
      <div>
        <div className="eyebrow mb-1">{mn ? "Эзэмшсэн гэдэг нь" : "You have mastered it when"}</div>
        <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}><MathText text={mastery.canDo} /></p>
      </div>
      {calculator !== undefined && (
        <p className="text-[12px]" style={{ color: "var(--fg-3)" }}>
          {calculator ? (mn ? "Тооны машин ашиглаж болно." : "Calculator allowed.") : mn ? "Тооны машингүйгээр бодно." : "No calculator."}
        </p>
      )}
    </div>
  );
}

/**
 * An open answer ("explain why", "write an equation whose solution is 3"):
 * the student writes their own, then compares with the model answer and marks
 * it honestly. Open questions cannot be auto-graded fairly, and leaving them
 * out would drop the explain/open types the manual requires (§4).
 */
export function SelfAnswer({
  model,
  outcome,
  onCommit,
  mn,
}: {
  model: string;
  outcome: { correct: boolean } | null;
  onCommit: (o: { correct: boolean; revealed: boolean }) => void;
  mn: boolean;
}) {
  const [text, setText] = useState("");
  const [shown, setShown] = useState(false);
  return (
    <div className="mt-3">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        disabled={shown}
        rows={3}
        placeholder={mn ? "Хариугаа энд бичээрэй" : "Write your answer here"}
        className="w-full rounded-lg px-3 py-2 text-[15px] outline-none"
        style={{ background: "var(--bg-2)", border: "1.5px solid var(--line)", color: "var(--fg)" }}
      />
      {!shown && text.trim() !== "" && (
        <button type="button" onClick={() => setShown(true)} className="btn btn-primary gm-fade mt-2 text-[13px]">
          {mn ? "Загвар хариутай харьцуулах" : "Compare with the model answer"}
        </button>
      )}
      {shown && (
        <div className="mt-3 rounded-xl p-3.5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
          <div className="eyebrow mb-1">{mn ? "Загвар хариу" : "Model answer"}</div>
          <p className="text-[14.5px] leading-relaxed" style={{ color: "var(--fg)" }}><MathText text={model} /></p>
          {!outcome && (
            <div className="mt-3 flex items-center gap-2 flex-wrap">
              <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>{mn ? "Таны хариу:" : "Yours was:"}</span>
              <button type="button" onClick={() => onCommit({ correct: true, revealed: false })} className="btn btn-line text-[13px]">
                {mn ? "Зөв байсан" : "Right"}
              </button>
              <button type="button" onClick={() => onCommit({ correct: false, revealed: false })} className="btn btn-line text-[13px]">
                {mn ? "Буруу эсвэл дутуу байсан" : "Wrong or incomplete"}
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
