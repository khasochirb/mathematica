"use client";

import { useRef, useState } from "react";
import { Check, CornerDownLeft, Eye, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import {
  type AnswerMode,
  checkNumericAnswer,
  seededOptionOrder,
} from "@/lib/bank-answer";

// COMMIT, THEN FIND OUT. The one control both bank surfaces use to take an
// answer, shared so the browse list and the practice runner behave
// identically.
//
// It is the answer to a piece of student feedback: a "Show solution" button
// sitting next to an unsolved problem is tempting even for disciplined
// students, and a peeked problem teaches nothing. So there is no way to see
// the solution here without first putting an answer on the record.
//
// Two modes, chosen per problem type by lib/bank-answer:
//   numeric — a text box, no options in sight, nothing to back-solve from.
//   choice  — the four authored options, for answers that cannot be typed
//             reliably (expressions, equations, sentences).
//
// Selecting is not committing: in both modes the student picks or types,
// then presses Check. A mis-tap should never spend the attempt.
//
// The escape hatch is deliberate and priced. "Stuck? Show me" is always
// available — trapping a student who genuinely cannot start is worse than
// letting them look — but it records a MISS, so peeking costs mastery
// instead of being free. That is the whole behavioural change: the tempting
// button now has a price tag on it.

export type AnswerOutcome = { correct: boolean; revealed: boolean };

export default function AnswerPrompt({
  variant,
  mode,
  outcome,
  onCommit,
  salt = "",
  autoFocus = false,
}: {
  variant: { id: string; options: string[]; correctIndex: number };
  mode: AnswerMode;
  /** Null until the student commits; set by the parent to lock and paint. */
  outcome: AnswerOutcome | null;
  onCommit: (outcome: AnswerOutcome) => void;
  /** Reshuffles the option order when it changes (e.g. after a reroll). */
  salt?: string;
  autoFocus?: boolean;
}) {
  return mode === "numeric" ? (
    <NumericPrompt variant={variant} outcome={outcome} onCommit={onCommit} autoFocus={autoFocus} />
  ) : (
    <ChoicePrompt variant={variant} outcome={outcome} onCommit={onCommit} salt={salt} />
  );
}

// ---------------------------------------------------------------------------
// Typed answers
// ---------------------------------------------------------------------------

function NumericPrompt({
  variant,
  outcome,
  onCommit,
  autoFocus,
}: {
  variant: { options: string[]; correctIndex: number };
  outcome: AnswerOutcome | null;
  onCommit: (outcome: AnswerOutcome) => void;
  autoFocus?: boolean;
}) {
  const [text, setText] = useState("");
  const [unreadable, setUnreadable] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const answered = outcome !== null;
  const correctAnswer = variant.options[variant.correctIndex] ?? "";

  function submit() {
    if (answered || text.trim() === "") return;
    const verdict = checkNumericAnswer(text, correctAnswer);
    if (verdict === "unparsed") {
      // Not a miss — the student was unclear, not wrong. Let them restate it.
      setUnreadable(true);
      inputRef.current?.focus();
      return;
    }
    setUnreadable(false);
    onCommit({ correct: verdict === "correct", revealed: false });
  }

  const ring = !answered
    ? "var(--line)"
    : outcome.revealed
      ? "var(--line)"
      : outcome.correct
        ? "#3fb27f"
        : "rgba(215,80,63,0.5)";

  return (
    <div className="mt-3">
      <div className="flex items-center gap-2 flex-wrap">
        <div className="relative">
          <input
            ref={inputRef}
            type="text"
            inputMode="text"
            autoComplete="off"
            autoCorrect="off"
            autoCapitalize="off"
            spellCheck={false}
            autoFocus={autoFocus}
            value={text}
            disabled={answered}
            placeholder="Your answer"
            aria-label="Your answer"
            onChange={(e) => {
              setText(e.target.value);
              setUnreadable(false);
            }}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                submit();
              }
            }}
            className="rounded-lg px-3 py-2 text-[15px] outline-none"
            style={{
              background: answered ? "var(--bg-1)" : "var(--bg-2)",
              border: `1.5px solid ${ring}`,
              color: "var(--fg)",
              width: 168,
              opacity: answered ? 0.75 : 1,
            }}
          />
        </div>

        {!answered ? (
          <button
            type="button"
            onClick={submit}
            disabled={text.trim() === ""}
            className="btn btn-primary inline-flex items-center gap-1.5 text-[13px]"
            style={{ opacity: text.trim() === "" ? 0.45 : 1 }}
          >
            Check
            <CornerDownLeft className="h-3.5 w-3.5" />
          </button>
        ) : (
          <Verdict outcome={outcome} />
        )}

        {!answered && (
          <GiveUpButton onGiveUp={() => onCommit({ correct: false, revealed: true })} />
        )}
      </div>

      {unreadable && !answered && (
        <p className="mt-1.5 text-[11.5px]" style={{ color: "#c05a49" }}>
          That doesn&apos;t read as a number — try something like 12, -2.5 or 3/4.
          This didn&apos;t count as an attempt.
        </p>
      )}
    </div>
  );
}

// ---------------------------------------------------------------------------
// Multiple choice
// ---------------------------------------------------------------------------

function ChoicePrompt({
  variant,
  outcome,
  onCommit,
  salt,
}: {
  variant: { id: string; options: string[]; correctIndex: number };
  outcome: AnswerOutcome | null;
  onCommit: (outcome: AnswerOutcome) => void;
  salt: string;
}) {
  const [picked, setPicked] = useState<number | null>(null);
  const answered = outcome !== null;
  // Seeded, not random: these rows are server-rendered, so a Math.random
  // order would hydrate differently than it was sent.
  const disp = seededOptionOrder(variant, salt);

  return (
    <div className="mt-3">
      <div className="grid gap-2 sm:grid-cols-2">
        {disp.options.map((opt, i) => {
          const isCorrect = answered && i === disp.correctIndex;
          const isWrongPick = answered && i === picked && i !== disp.correctIndex;
          const isSelected = !answered && i === picked;

          let bg = "var(--bg-2)";
          let border = "var(--line)";
          let color = "var(--fg)";
          if (isCorrect) {
            bg = "rgba(63,178,127,0.14)";
            border = "#3fb27f";
          } else if (isWrongPick) {
            bg = "rgba(215,80,63,0.10)";
            border = "rgba(215,80,63,0.5)";
            color = "var(--fg-2)";
          } else if (isSelected) {
            bg = "var(--accent-wash)";
            border = "var(--accent)";
          }

          return (
            <button
              key={i}
              type="button"
              onClick={() => !answered && setPicked(i)}
              disabled={answered}
              aria-pressed={isSelected}
              className="gm-press flex items-center justify-between gap-2 rounded-xl px-3.5 py-2.5 text-left"
              style={{
                background: bg,
                border: `1.5px solid ${border}`,
                color,
                opacity: answered && !isCorrect && i !== picked ? 0.45 : 1,
              }}
            >
              <span className="q-math" style={{ fontSize: 14.5 }}>
                <MathText text={opt} />
              </span>
              {isCorrect && (
                <span
                  className="grid h-5 w-5 flex-shrink-0 place-items-center rounded-full"
                  style={{ background: "#3fb27f", color: "#fff" }}
                >
                  <Check className="h-3.5 w-3.5" />
                </span>
              )}
              {isWrongPick && (
                <span
                  className="grid h-5 w-5 flex-shrink-0 place-items-center rounded-full"
                  style={{ background: "rgba(215,80,63,0.85)", color: "#fff" }}
                >
                  <X className="h-3.5 w-3.5" />
                </span>
              )}
            </button>
          );
        })}
      </div>

      <div className="mt-2.5 flex items-center gap-2 flex-wrap">
        {!answered ? (
          <>
            <button
              type="button"
              onClick={() =>
                picked !== null && onCommit({ correct: picked === disp.correctIndex, revealed: false })
              }
              disabled={picked === null}
              className="btn btn-primary text-[13px]"
              style={{ opacity: picked === null ? 0.45 : 1 }}
            >
              Check
            </button>
            <GiveUpButton onGiveUp={() => onCommit({ correct: false, revealed: true })} />
          </>
        ) : (
          <Verdict outcome={outcome} />
        )}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Shared bits
// ---------------------------------------------------------------------------

function Verdict({ outcome }: { outcome: AnswerOutcome }) {
  if (outcome.revealed) {
    return (
      <span
        className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12.5px]"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
      >
        <Eye className="h-3.5 w-3.5" /> Revealed — counted as a miss
      </span>
    );
  }
  return outcome.correct ? (
    <span
      className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12.5px] font-medium"
      style={{ background: "rgba(63,178,127,0.12)", border: "1px solid rgba(63,178,127,0.45)", color: "#2f9868" }}
    >
      <Check className="h-3.5 w-3.5" /> Correct
    </span>
  ) : (
    <span
      className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12.5px] font-medium"
      style={{ background: "rgba(215,80,63,0.08)", border: "1px solid rgba(215,80,63,0.4)", color: "#c05a49" }}
    >
      <X className="h-3.5 w-3.5" /> Not quite
    </span>
  );
}

// Priced, not forbidden. A student who cannot start still needs a way
// through; making it cost a miss is what stops it being the default move.
//
// Pushed to the far edge (ml-auto) rather than sitting beside Check: the
// price only deters if the eye lands on Check first. Naming the cost in the
// label is the point — it is the difference between this and the "Show
// solution" button it replaces.
function GiveUpButton({ onGiveUp }: { onGiveUp: () => void }) {
  return (
    <button
      type="button"
      onClick={onGiveUp}
      className="ml-auto text-[11.5px]"
      style={{ color: "var(--fg-3)", textDecoration: "underline", textUnderlineOffset: 3 }}
    >
      Stuck? Show me — counts as a miss
    </button>
  );
}
