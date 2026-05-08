"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Delete } from "lucide-react";
import MathText from "./MathText";
import type { Section2Item, Slot } from "@/lib/esh-section2";
import { parseSlotLabel } from "@/lib/esh-section2";

// Renders one Section 2 subproblem (problem 2.X, sub Y) with:
//   - The shared problem context above the first subproblem (caller decides
//     when to show; this component shows it iff `showContext` is true).
//   - The subproblem instruction, with each `[label]` placeholder replaced
//     by the bare label so KaTeX renders the letters as variables — matches
//     how the official PDFs and answer sheets present these problems.
//   - A slot tray below the instruction with one labeled input per slot.
//     This is the answer area; values typed here are compared against
//     `slot.answer` at grading time.
//   - On coarse-pointer devices (touch / mobile), a 3×4 numeric keypad
//     under the tray. Keypad keystrokes go to whichever slot was focused
//     last. Native input keyboards still work for users who prefer them.

interface Section2CardProps {
  item: Section2Item;
  answers: Record<string, string>;
  onAnswerChange: (label: string, value: string) => void;
  disabled?: boolean;
  // When true, shows the shared problem context block above the
  // instruction. Callers typically render this only on the first
  // subproblem of each problem (e.g. 2.1.1 shows context, 2.1.2/2.1.3 do
  // not). Defaults to false so the card is safe to use bare.
  showContext?: boolean;
  // Optional human label for the subproblem (e.g. "2.1 (1)") — rendered
  // as a small badge above the instruction.
  questionLabel?: string;
}

// Replace each `[label]` placeholder with the bare label so KaTeX renders
// the letters as math variables (matching PDF presentation). For
// literal-prefix slots (`[1e]`), the full label `1e` is rendered, which
// KaTeX displays as the digit "1" followed by italic variable "e" — also
// matching the PDF.
function transformInstructionForRender(text: string): string {
  return text.replace(/\[([A-Za-z0-9]+)\]/g, "$1");
}

function useIsCoarsePointer(): boolean {
  const [coarse, setCoarse] = useState(false);
  useEffect(() => {
    if (typeof window === "undefined" || !window.matchMedia) return;
    const mq = window.matchMedia("(pointer: coarse)");
    const update = () => setCoarse(mq.matches);
    update();
    mq.addEventListener("change", update);
    return () => mq.removeEventListener("change", update);
  }, []);
  return coarse;
}

interface SlotInputProps {
  slot: Slot;
  value: string;
  onChange: (next: string) => void;
  onFocus: () => void;
  disabled?: boolean;
  registerRef?: (el: HTMLInputElement | null) => void;
}

function SlotInput({
  slot,
  value,
  onChange,
  onFocus,
  disabled,
  registerRef,
}: SlotInputProps) {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  const maxLength = slot.answer.length - prefix.length;
  const widthCh = Math.max(maxLength, 1);

  const handleChange = (raw: string) => {
    const filtered = raw.replace(/\D/g, "").slice(0, maxLength);
    onChange(filtered);
  };

  return (
    <div className="inline-flex items-center gap-1.5 rounded-lg bg-white/[0.04] border border-white/[0.08] px-2.5 py-1.5">
      <span className="text-xs font-mono text-gray-500">
        {/* The label rendered as a variable name (italic via .katex-style font
            could be applied, but plain font keeps the answer-bank readable). */}
        {slot.label}
      </span>
      <span className="text-xs text-gray-600">=</span>
      {prefix.length > 0 && (
        <span className="text-sm font-mono text-gray-300 tabular-nums">
          {prefix}
        </span>
      )}
      <input
        ref={(el) => registerRef?.(el)}
        type="text"
        inputMode="numeric"
        pattern="\d*"
        maxLength={maxLength}
        value={value}
        onChange={(e) => handleChange(e.target.value)}
        onFocus={onFocus}
        disabled={disabled}
        aria-label={`Slot ${slot.label}`}
        className="bg-transparent text-center text-sm font-mono text-white tabular-nums focus:outline-none disabled:text-gray-500 placeholder:text-gray-700"
        placeholder={"_".repeat(widthCh)}
        style={{ width: `${widthCh + 1}ch` }}
      />
    </div>
  );
}

interface NumericKeypadProps {
  onDigit: (digit: string) => void;
  onBackspace: () => void;
  onNext: () => void;
  disabled?: boolean;
}

function NumericKeypad({
  onDigit,
  onBackspace,
  onNext,
  disabled,
}: NumericKeypadProps) {
  const KEY_CLS =
    "h-12 rounded-xl border border-white/[0.08] bg-white/[0.05] text-base font-mono font-semibold text-white active:bg-primary-500/30 transition-colors disabled:opacity-30";

  const Btn = ({
    onClick,
    label,
    children,
    extraCls = "",
  }: {
    onClick: () => void;
    label: string;
    children: React.ReactNode;
    extraCls?: string;
  }) => (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      aria-label={label}
      className={`${KEY_CLS} ${extraCls}`}
    >
      {children}
    </button>
  );

  return (
    <div
      className="grid grid-cols-3 gap-2 mt-3"
      onMouseDown={(e) => {
        // Prevent the keypad from stealing focus from the input.
        e.preventDefault();
      }}
    >
      {[1, 2, 3, 4, 5, 6, 7, 8, 9].map((d) => (
        <Btn key={d} onClick={() => onDigit(String(d))} label={String(d)}>
          {d}
        </Btn>
      ))}
      <Btn onClick={onBackspace} label="Устгах" extraCls="text-orange-300">
        <Delete className="w-5 h-5 mx-auto" />
      </Btn>
      <Btn onClick={() => onDigit("0")} label="0">
        0
      </Btn>
      <Btn onClick={onNext} label="Дараах нүд" extraCls="text-primary-300">
        →
      </Btn>
    </div>
  );
}

export default function Section2Card({
  item,
  answers,
  onAnswerChange,
  disabled = false,
  showContext = false,
  questionLabel,
}: Section2CardProps) {
  const transformedInstruction = useMemo(
    () => transformInstructionForRender(item.instruction),
    [item.instruction],
  );

  const inputRefs = useRef<Record<string, HTMLInputElement | null>>({});
  const [focusedSlot, setFocusedSlot] = useState<string | null>(null);

  // When the item changes (navigating between subproblems), clear the
  // focused-slot ref state so the keypad doesn't keep targeting an
  // off-screen input.
  useEffect(() => {
    setFocusedSlot(null);
  }, [item.source]);

  const isCoarse = useIsCoarsePointer();

  const slotIndexByLabel = useMemo(() => {
    const map: Record<string, number> = {};
    item.slots.forEach((s, i) => {
      map[s.label] = i;
    });
    return map;
  }, [item.slots]);

  const handleKeypadDigit = useCallback(
    (digit: string) => {
      if (!focusedSlot) return;
      const slot = item.slots.find((s) => s.label === focusedSlot);
      if (!slot) return;
      const { prefix } = parseSlotLabel(slot.label);
      const currentMax = slot.answer.length - prefix.length;
      const current = answers[slot.label] ?? "";
      if (current.length >= currentMax) return;
      onAnswerChange(slot.label, current + digit);
    },
    [focusedSlot, item.slots, answers, onAnswerChange],
  );

  const handleKeypadBackspace = useCallback(() => {
    if (!focusedSlot) return;
    const current = answers[focusedSlot] ?? "";
    if (current.length === 0) return;
    onAnswerChange(focusedSlot, current.slice(0, -1));
  }, [focusedSlot, answers, onAnswerChange]);

  const handleKeypadNext = useCallback(() => {
    if (!focusedSlot) {
      // No focused slot: focus the first one.
      const first = item.slots[0];
      if (first) {
        setFocusedSlot(first.label);
        inputRefs.current[first.label]?.focus();
      }
      return;
    }
    const idx = slotIndexByLabel[focusedSlot] ?? -1;
    const next = item.slots[idx + 1];
    if (next) {
      setFocusedSlot(next.label);
      inputRefs.current[next.label]?.focus();
    } else {
      // Last slot — blur to dismiss the keypad's intent.
      inputRefs.current[focusedSlot]?.blur();
    }
  }, [focusedSlot, item.slots, slotIndexByLabel]);

  return (
    <div
      className={`card-glass p-5 ${disabled ? "opacity-90" : ""}`}
      data-source={item.source}
    >
      {/* Header */}
      <div className="flex items-center gap-2 mb-3">
        <span className="text-xs font-medium px-2.5 py-1 rounded-full bg-primary-500/10 text-primary-300 border border-primary-400/15">
          {questionLabel ?? `${item.problem} (${item.subproblem})`}
        </span>
        <span className="text-xs text-gray-500">
          {item.points} {item.points === 1 ? "оноо" : "оноо"}
        </span>
      </div>

      {/* Optional shared context (for first subproblem in each problem) */}
      {showContext && item.context && (
        <div className="text-gray-300 text-[14px] leading-relaxed mb-4 pl-3 border-l-2 border-primary-400/30">
          <MathText text={item.context} />
        </div>
      )}

      {/* Instruction with letter-rendered placeholders */}
      <div className="text-gray-200 text-[15px] leading-relaxed mb-4">
        <MathText text={transformedInstruction} />
      </div>

      {/* Slot tray */}
      <div className="flex flex-wrap gap-2 mb-1" role="group" aria-label="Хариу">
        {item.slots.map((slot) => (
          <SlotInput
            key={slot.label}
            slot={slot}
            value={answers[slot.label] ?? ""}
            onChange={(v) => onAnswerChange(slot.label, v)}
            onFocus={() => setFocusedSlot(slot.label)}
            disabled={disabled}
            registerRef={(el) => {
              inputRefs.current[slot.label] = el;
            }}
          />
        ))}
      </div>

      {/* Mobile-only numeric keypad */}
      {isCoarse && !disabled && (
        <NumericKeypad
          onDigit={handleKeypadDigit}
          onBackspace={handleKeypadBackspace}
          onNext={handleKeypadNext}
        />
      )}
    </div>
  );
}
