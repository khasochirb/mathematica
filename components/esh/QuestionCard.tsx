"use client";

import { useState } from "react";
import MathText from "./MathText";
import {
  CheckCircle2,
  XCircle,
  RotateCcw,
  ChevronDown,
  ChevronUp,
  Flag,
  Lock,
} from "lucide-react";
import type { Question } from "@/lib/esh-questions";
import { TOPIC_LABELS } from "@/lib/esh-questions";

interface QuestionCardBaseProps {
  question: Question;
  highlight?: boolean;
}

interface InstantModeProps extends QuestionCardBaseProps {
  mode: "instant";
  onAnswer?: (
    questionSource: string,
    topic: string,
    subtopic: string,
    difficulty: number,
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) => void;
  solutionsLocked?: boolean;
  onSolutionUpgrade?: () => void;
}

interface TestModeProps extends QuestionCardBaseProps {
  mode: "test";
  selectedAnswer?: string | null;
  onSelectAnswer?: (letter: string) => void;
  isFlagged?: boolean;
  onToggleFlag?: () => void;
  questionIndex?: number;
}

interface ReviewModeProps extends QuestionCardBaseProps {
  mode: "review";
  selectedAnswer?: string | null;
  isFlagged?: boolean;
  solutionsLocked?: boolean;
  onSolutionUpgrade?: () => void;
}

type QuestionCardProps = InstantModeProps | TestModeProps | ReviewModeProps;

const difficultyConfig: Record<number, { label: string; token: "accent" | "warn" | "danger" }> = {
  1: { label: "Хөнгөн", token: "accent" },
  2: { label: "Дунд", token: "warn" },
  3: { label: "Хүнд", token: "danger" },
};

function diffStyle(token: "accent" | "warn" | "danger") {
  if (token === "accent") {
    return {
      background: "var(--accent-wash)",
      borderColor: "var(--accent-line)",
      color: "var(--accent)",
    };
  }
  return {
    background: `color-mix(in oklch, var(--${token}) 12%, transparent)`,
    borderColor: `color-mix(in oklch, var(--${token}) 30%, transparent)`,
    color: `var(--${token})`,
  };
}

function QuestionHeader({
  questionNumber,
  topic,
  subtopic,
  difficulty,
  rightSlot,
}: {
  questionNumber: number;
  topic: string;
  subtopic?: string;
  difficulty: number;
  rightSlot?: React.ReactNode;
}) {
  const diff = difficultyConfig[difficulty];
  return (
    <div className="flex items-center justify-between mb-4 gap-2">
      <div className="flex items-center gap-2.5 flex-wrap">
        <span
          className="mono tabular w-7 h-7 rounded-full flex items-center justify-center text-[12px]"
          style={{
            background: "var(--accent-wash)",
            border: "1px solid var(--accent-line)",
            color: "var(--accent)",
          }}
        >
          {questionNumber}
        </span>
        <span
          className="mono text-[10px] uppercase px-2 py-1 rounded-full"
          style={{
            background: "var(--bg-2)",
            border: "1px solid var(--line)",
            color: "var(--fg-2)",
            letterSpacing: "0.06em",
          }}
        >
          {TOPIC_LABELS[topic] || topic}
        </span>
        {subtopic && (
          <span
            className="mono text-[10px]"
            style={{ color: "var(--fg-3)", letterSpacing: "0.04em" }}
          >
            {subtopic}
          </span>
        )}
      </div>
      <div className="flex items-center gap-2 shrink-0">
        {diff && (
          <span
            className="mono text-[10px] uppercase px-2 py-1 rounded-full border"
            style={{ ...diffStyle(diff.token), letterSpacing: "0.06em" }}
          >
            {diff.label}
          </span>
        )}
        {rightSlot}
      </div>
    </div>
  );
}

function LockedSolutionCTA({ onUpgrade }: { onUpgrade?: () => void }) {
  return (
    <button
      type="button"
      onClick={onUpgrade}
      className="mt-3 w-full text-left rounded-md p-3 flex items-center gap-3 transition-colors"
      style={{
        background: "var(--accent-wash)",
        border: "1px solid var(--accent-line)",
        color: "var(--accent-ink)",
      }}
    >
      <span
        className="w-7 h-7 rounded-full flex items-center justify-center shrink-0"
        style={{
          background: "var(--bg)",
          border: "1px solid var(--accent-line)",
          color: "var(--accent)",
        }}
      >
        <Lock className="w-3.5 h-3.5" />
      </span>
      <span className="flex-1 min-w-0">
        <span
          className="mono text-[10px] uppercase block"
          style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
        >
          Premium · Бодолт
        </span>
        <span className="text-[13px]" style={{ color: "var(--fg-1)" }}>
          Алхам алхмаар бодолт Premium-д нээгдэнэ
        </span>
      </span>
      <span
        className="mono text-[10px] uppercase shrink-0"
        style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
      >
        Нээх →
      </span>
    </button>
  );
}

function letterCircleStyle(state: "default" | "selected" | "correct" | "wrong") {
  switch (state) {
    case "correct":
      return {
        background: "var(--accent)",
        borderColor: "var(--accent)",
        color: "var(--accent-ink)",
      };
    case "wrong":
      return {
        background: "var(--danger)",
        borderColor: "var(--danger)",
        color: "var(--bg)",
      };
    case "selected":
      return {
        background: "var(--accent)",
        borderColor: "var(--accent)",
        color: "var(--accent-ink)",
      };
    default:
      return {
        background: "transparent",
        borderColor: "var(--line-strong)",
        color: "var(--fg-2)",
      };
  }
}

function optionContainerStyle(state: "default" | "selected" | "correct" | "wrong" | "muted") {
  switch (state) {
    case "correct":
      return {
        background: "var(--accent-wash)",
        borderColor: "var(--accent-line)",
      };
    case "wrong":
      return {
        background: "color-mix(in oklch, var(--danger) 8%, transparent)",
        borderColor: "color-mix(in oklch, var(--danger) 35%, transparent)",
      };
    case "selected":
      return {
        background: "var(--accent-wash)",
        borderColor: "var(--accent-line)",
      };
    case "muted":
      return {
        background: "transparent",
        borderColor: "var(--line)",
        opacity: 0.5,
      };
    default:
      return {
        background: "var(--bg-1)",
        borderColor: "var(--line)",
      };
  }
}

export default function QuestionCard(props: QuestionCardProps) {
  const { question, highlight } = props;
  const mode = props.mode || "instant";

  const [localSelected, setLocalSelected] = useState<string | null>(null);
  const [showSolution, setShowSolution] = useState(false);

  if (mode === "test") {
    const { selectedAnswer, onSelectAnswer, isFlagged, onToggleFlag, questionIndex } =
      props as TestModeProps;

    return (
      <div className="card-edit p-5 mb-4">
        <QuestionHeader
          questionNumber={questionIndex ?? question.questionNumber}
          topic={question.topic}
          subtopic={question.subtopic}
          difficulty={question.difficulty}
          rightSlot={
            onToggleFlag && (
              <button
                onClick={onToggleFlag}
                className="p-1.5 rounded-md transition-colors"
                style={
                  isFlagged
                    ? {
                        background: "color-mix(in oklch, var(--warn) 14%, transparent)",
                        border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                        color: "var(--warn)",
                      }
                    : {
                        border: "1px solid transparent",
                        color: "var(--fg-3)",
                      }
                }
                title="Тэмдэглэх"
              >
                <Flag className="w-4 h-4" fill={isFlagged ? "currentColor" : "none"} />
              </button>
            )
          }
        />

        <div className="q-math text-[15px] leading-relaxed mb-5" style={{ color: "var(--fg)" }}>
          <MathText text={question.body} />
        </div>

        {question.options && (
          <div className="space-y-2">
            {Object.entries(question.options).map(([letter, text]) => {
              const isSelected = selectedAnswer === letter;
              return (
                <button
                  key={letter}
                  onClick={() => onSelectAnswer?.(letter)}
                  className="w-full text-left px-4 py-3 rounded-md border transition-colors flex items-center gap-3"
                  style={optionContainerStyle(isSelected ? "selected" : "default")}
                >
                  <span
                    className="mono w-7 h-7 rounded-full border flex items-center justify-center text-[12px] shrink-0"
                    style={letterCircleStyle(isSelected ? "selected" : "default")}
                  >
                    {letter}
                  </span>
                  <span className="text-[14px]" style={{ color: "var(--fg-1)" }}>
                    <MathText text={text} />
                  </span>
                </button>
              );
            })}
          </div>
        )}
      </div>
    );
  }

  if (mode === "review") {
    const { selectedAnswer, isFlagged, solutionsLocked, onSolutionUpgrade } =
      props as ReviewModeProps;
    const isCorrect = selectedAnswer === question.answer;
    const wasAnswered = !!selectedAnswer;

    return (
      <div
        className="card-edit p-5 mb-4"
        style={
          isFlagged
            ? { borderColor: "color-mix(in oklch, var(--warn) 35%, transparent)" }
            : undefined
        }
      >
        <QuestionHeader
          questionNumber={question.questionNumber}
          topic={question.topic}
          subtopic={question.subtopic}
          difficulty={question.difficulty}
          rightSlot={
            isFlagged && (
              <span
                className="p-1.5 rounded-md"
                style={{
                  background: "color-mix(in oklch, var(--warn) 14%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
                  color: "var(--warn)",
                }}
              >
                <Flag className="w-4 h-4" fill="currentColor" />
              </span>
            )
          }
        />

        <div className="q-math text-[15px] leading-relaxed mb-5" style={{ color: "var(--fg)" }}>
          <MathText text={question.body} />
        </div>

        {question.options && (
          <div className="space-y-2 mb-4">
            {Object.entries(question.options).map(([letter, text]) => {
              let containerState: "correct" | "wrong" | "muted" = "muted";
              let circleState: "correct" | "wrong" | "default" = "default";
              if (letter === question.answer) {
                containerState = "correct";
                circleState = "correct";
              } else if (letter === selectedAnswer && !isCorrect) {
                containerState = "wrong";
                circleState = "wrong";
              }

              return (
                <div
                  key={letter}
                  className="w-full text-left px-4 py-3 rounded-md border flex items-center gap-3"
                  style={optionContainerStyle(containerState)}
                >
                  <span
                    className="mono w-7 h-7 rounded-full border flex items-center justify-center text-[12px] shrink-0"
                    style={letterCircleStyle(circleState)}
                  >
                    {letter}
                  </span>
                  <span className="text-[14px]" style={{ color: "var(--fg-1)" }}>
                    <MathText text={text} />
                  </span>
                </div>
              );
            })}
          </div>
        )}

        <div
          className="p-3 rounded-md border"
          style={
            !wasAnswered
              ? {
                  background: "var(--bg-2)",
                  borderColor: "var(--line)",
                }
              : isCorrect
                ? {
                    background: "var(--accent-wash)",
                    borderColor: "var(--accent-line)",
                  }
                : {
                    background: "color-mix(in oklch, var(--danger) 8%, transparent)",
                    borderColor: "color-mix(in oklch, var(--danger) 35%, transparent)",
                  }
          }
        >
          <div className="flex items-center gap-2">
            {!wasAnswered ? (
              <span className="mono text-[11px] uppercase" style={{ color: "var(--fg-2)", letterSpacing: "0.06em" }}>
                Хариулаагүй
              </span>
            ) : isCorrect ? (
              <>
                <CheckCircle2 className="w-4 h-4" style={{ color: "var(--accent)" }} />
                <span className="mono text-[11px] uppercase" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>
                  Зөв
                </span>
              </>
            ) : (
              <>
                <XCircle className="w-4 h-4" style={{ color: "var(--danger)" }} />
                <span className="mono text-[11px] uppercase" style={{ color: "var(--danger)", letterSpacing: "0.06em" }}>
                  Буруу — Зөв хариу: {question.answer}
                </span>
              </>
            )}
          </div>
        </div>

        {question.solution &&
          (solutionsLocked ? (
            <LockedSolutionCTA onUpgrade={onSolutionUpgrade} />
          ) : (
            <div className="mt-3">
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="mono text-[11px] uppercase inline-flex items-center gap-1 transition-colors"
                style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
              >
                {showSolution ? (
                  <>
                    <ChevronUp className="w-3.5 h-3.5" /> Бодолтыг нуух
                  </>
                ) : (
                  <>
                    <ChevronDown className="w-3.5 h-3.5" /> Бодолтыг харах
                  </>
                )}
              </button>
              {showSolution && (
                <div
                  className="mt-2 q-math text-[14px] leading-relaxed"
                  style={{ color: "var(--fg-1)" }}
                >
                  <MathText text={question.solution} />
                </div>
              )}
            </div>
          ))}
      </div>
    );
  }

  // Instant mode
  const { onAnswer, solutionsLocked, onSolutionUpgrade } = props as InstantModeProps;
  const selected = localSelected;
  const isCorrect = selected === question.answer;
  const hasAnswer = question.answer && question.answer.length > 0;

  const handleSelect = (letter: string) => {
    if (selected) return;
    setLocalSelected(letter);
    if (hasAnswer && onAnswer) {
      onAnswer(
        question.source,
        question.topic,
        question.subtopic,
        question.difficulty,
        letter,
        question.answer,
        letter === question.answer,
      );
    }
  };

  return (
    <div
      className="card-edit p-5 mb-4"
      style={
        highlight
          ? { borderColor: "color-mix(in oklch, var(--warn) 35%, transparent)" }
          : undefined
      }
    >
      {highlight && (
        <div className="mb-3">
          <span
            className="mono text-[10px] uppercase px-2 py-1 rounded-full border"
            style={{
              background: "color-mix(in oklch, var(--warn) 12%, transparent)",
              borderColor: "color-mix(in oklch, var(--warn) 30%, transparent)",
              color: "var(--warn)",
              letterSpacing: "0.06em",
            }}
          >
            Сайжруулах сэдэв
          </span>
        </div>
      )}

      <QuestionHeader
        questionNumber={question.questionNumber}
        topic={question.topic}
        subtopic={question.subtopic}
        difficulty={question.difficulty}
      />

      <div className="q-math text-[15px] leading-relaxed mb-5" style={{ color: "var(--fg)" }}>
        <MathText text={question.body} />
      </div>

      {question.options && (
        <div className="space-y-2 mb-4">
          {Object.entries(question.options).map(([letter, text]) => {
            let containerState: "default" | "correct" | "wrong" | "muted" = "default";
            let circleState: "default" | "correct" | "wrong" = "default";

            if (selected) {
              if (letter === question.answer) {
                containerState = "correct";
                circleState = "correct";
              } else if (letter === selected && !isCorrect) {
                containerState = "wrong";
                circleState = "wrong";
              } else {
                containerState = "muted";
              }
            }

            return (
              <button
                key={letter}
                onClick={() => handleSelect(letter)}
                disabled={!!selected}
                className="w-full text-left px-4 py-3 rounded-md border transition-colors flex items-center gap-3"
                style={{
                  ...optionContainerStyle(containerState),
                  cursor: selected ? "default" : "pointer",
                }}
              >
                <span
                  className="mono w-7 h-7 rounded-full border flex items-center justify-center text-[12px] shrink-0"
                  style={letterCircleStyle(circleState)}
                >
                  {letter}
                </span>
                <span className="text-[14px]" style={{ color: "var(--fg-1)" }}>
                  <MathText text={text} />
                </span>
              </button>
            );
          })}
        </div>
      )}

      {selected && hasAnswer && (
        <div
          className="mt-4 p-4 rounded-md border"
          style={
            isCorrect
              ? {
                  background: "var(--accent-wash)",
                  borderColor: "var(--accent-line)",
                }
              : {
                  background: "color-mix(in oklch, var(--danger) 8%, transparent)",
                  borderColor: "color-mix(in oklch, var(--danger) 35%, transparent)",
                }
          }
        >
          <div className="flex items-center gap-2">
            {isCorrect ? (
              <CheckCircle2 className="w-5 h-5" style={{ color: "var(--accent)" }} />
            ) : (
              <XCircle className="w-5 h-5" style={{ color: "var(--danger)" }} />
            )}
            <p
              className="mono text-[11px] uppercase"
              style={{
                color: isCorrect ? "var(--accent)" : "var(--danger)",
                letterSpacing: "0.06em",
              }}
            >
              {isCorrect ? "Зөв байна!" : `Буруу. Зөв хариу: ${question.answer}`}
            </p>
          </div>

          {question.solution &&
            (solutionsLocked ? (
              <LockedSolutionCTA onUpgrade={onSolutionUpgrade} />
            ) : (
              <div className="mt-3">
                <button
                  onClick={() => setShowSolution(!showSolution)}
                  className="mono text-[11px] uppercase inline-flex items-center gap-1"
                  style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
                >
                  {showSolution ? (
                    <>
                      <ChevronUp className="w-3.5 h-3.5" /> Бодолтыг нуух
                    </>
                  ) : (
                    <>
                      <ChevronDown className="w-3.5 h-3.5" /> Бодолтыг харах
                    </>
                  )}
                </button>
                {showSolution && (
                  <div
                    className="mt-2 q-math text-[14px] leading-relaxed"
                    style={{ color: "var(--fg-1)" }}
                  >
                    <MathText text={question.solution} />
                  </div>
                )}
              </div>
            ))}
        </div>
      )}

      {selected && (
        <button
          onClick={() => {
            setLocalSelected(null);
            setShowSolution(false);
          }}
          className="mt-3 mono text-[11px] uppercase inline-flex items-center gap-1.5 transition-colors"
          style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
        >
          <RotateCcw className="w-3 h-3" /> Дахин бодох
        </button>
      )}
    </div>
  );
}
