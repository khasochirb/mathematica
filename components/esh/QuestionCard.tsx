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
}

type QuestionCardProps = InstantModeProps | TestModeProps | ReviewModeProps;

const difficultyConfig = [
  {},
  {
    label: "Хөнгөн",
    cls: "bg-emerald-500/10 text-emerald-400 border-emerald-400/20",
  },
  {
    label: "Дунд",
    cls: "bg-yellow-500/10 text-yellow-400 border-yellow-400/20",
  },
  {
    label: "Хүнд",
    cls: "bg-red-500/10 text-red-400 border-red-400/20",
  },
];

export default function QuestionCard(props: QuestionCardProps) {
  const { question, highlight } = props;
  const mode = props.mode || "instant";

  // Instant mode local state
  const [localSelected, setLocalSelected] = useState<string | null>(null);
  const [showSolution, setShowSolution] = useState(false);

  const diff = difficultyConfig[question.difficulty] || {};

  if (mode === "test") {
    const { selectedAnswer, onSelectAnswer, isFlagged, onToggleFlag, questionIndex } =
      props as TestModeProps;

    return (
      <div className="card-glass p-5 mb-4 transition-all">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2.5">
            <span className="bg-primary-500/20 text-primary-300 text-sm font-bold rounded-full w-8 h-8 flex items-center justify-center border border-primary-400/20">
              {questionIndex ?? question.questionNumber}
            </span>
            <span className="text-xs font-medium px-2.5 py-1 rounded-full bg-primary-500/10 text-primary-300 border border-primary-400/15">
              {TOPIC_LABELS[question.topic] || question.topic}
            </span>
            {question.subtopic && (
              <span className="text-xs text-gray-500">{question.subtopic}</span>
            )}
          </div>
          <div className="flex items-center gap-2">
            {"label" in diff && (
              <span
                className={`text-xs font-medium px-2 py-1 rounded-full border ${(diff as any).cls}`}
              >
                {(diff as any).label}
              </span>
            )}
            {onToggleFlag && (
              <button
                onClick={onToggleFlag}
                className={`p-1.5 rounded-lg transition-all ${
                  isFlagged
                    ? "bg-orange-500/20 text-orange-400 border border-orange-400/30"
                    : "text-gray-500 hover:text-orange-400 hover:bg-orange-500/10 border border-transparent"
                }`}
                title="Тэмдэглэх"
              >
                <Flag className="w-4 h-4" fill={isFlagged ? "currentColor" : "none"} />
              </button>
            )}
          </div>
        </div>

        {/* Question body */}
        <div className="text-gray-200 text-[15px] leading-relaxed mb-5">
          <MathText text={question.body} />
        </div>

        {/* Options - test mode: no reveal */}
        {question.options && (
          <div className="space-y-2">
            {Object.entries(question.options).map(([letter, text]) => {
              const isSelected = selectedAnswer === letter;
              const optionCls = isSelected
                ? "border-primary-400/50 bg-primary-500/15"
                : "border-white/[0.08] hover:border-primary-400/40 hover:bg-primary-500/5";

              return (
                <button
                  key={letter}
                  onClick={() => onSelectAnswer?.(letter)}
                  className={`w-full text-left px-4 py-3 rounded-xl border transition-all flex items-center gap-3 ${optionCls}`}
                >
                  <span
                    className={`w-7 h-7 rounded-full border flex items-center justify-center text-sm font-bold shrink-0 ${
                      isSelected
                        ? "border-primary-400 bg-primary-500 text-white"
                        : "border-gray-600 text-gray-400"
                    }`}
                  >
                    {letter}
                  </span>
                  <span className="text-gray-300 text-sm">
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
    const { selectedAnswer, isFlagged } = props as ReviewModeProps;
    const isCorrect = selectedAnswer === question.answer;
    const wasAnswered = !!selectedAnswer;

    return (
      <div
        className={`card-glass p-5 mb-4 transition-all ${
          isFlagged ? "border-orange-400/30" : ""
        }`}
      >
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2.5">
            <span className="bg-primary-500/20 text-primary-300 text-sm font-bold rounded-full w-8 h-8 flex items-center justify-center border border-primary-400/20">
              {question.questionNumber}
            </span>
            <span className="text-xs font-medium px-2.5 py-1 rounded-full bg-primary-500/10 text-primary-300 border border-primary-400/15">
              {TOPIC_LABELS[question.topic] || question.topic}
            </span>
            {question.subtopic && (
              <span className="text-xs text-gray-500">{question.subtopic}</span>
            )}
          </div>
          <div className="flex items-center gap-2">
            {"label" in diff && (
              <span
                className={`text-xs font-medium px-2 py-1 rounded-full border ${(diff as any).cls}`}
              >
                {(diff as any).label}
              </span>
            )}
            {isFlagged && (
              <span className="p-1.5 rounded-lg bg-orange-500/20 text-orange-400 border border-orange-400/30">
                <Flag className="w-4 h-4" fill="currentColor" />
              </span>
            )}
          </div>
        </div>

        {/* Question body */}
        <div className="text-gray-200 text-[15px] leading-relaxed mb-5">
          <MathText text={question.body} />
        </div>

        {/* Options - review mode: show correct/incorrect */}
        {question.options && (
          <div className="space-y-2 mb-4">
            {Object.entries(question.options).map(([letter, text]) => {
              let optionCls = "border-white/[0.05] opacity-40";
              if (letter === question.answer) {
                optionCls = "border-emerald-400/50 bg-emerald-500/10";
              } else if (letter === selectedAnswer && !isCorrect) {
                optionCls = "border-red-400/50 bg-red-500/10";
              }

              return (
                <div
                  key={letter}
                  className={`w-full text-left px-4 py-3 rounded-xl border transition-all flex items-center gap-3 ${optionCls}`}
                >
                  <span
                    className={`w-7 h-7 rounded-full border flex items-center justify-center text-sm font-bold shrink-0 ${
                      letter === question.answer
                        ? "border-emerald-400 bg-emerald-500 text-white"
                        : letter === selectedAnswer && !isCorrect
                          ? "border-red-400 bg-red-500 text-white"
                          : "border-gray-600 text-gray-400"
                    }`}
                  >
                    {letter}
                  </span>
                  <span className="text-gray-300 text-sm">
                    <MathText text={text} />
                  </span>
                </div>
              );
            })}
          </div>
        )}

        {/* Result indicator */}
        <div
          className={`p-3 rounded-xl border ${
            !wasAnswered
              ? "bg-gray-500/10 border-gray-400/20"
              : isCorrect
                ? "bg-emerald-500/10 border-emerald-400/20"
                : "bg-red-500/10 border-red-400/20"
          }`}
        >
          <div className="flex items-center gap-2">
            {!wasAnswered ? (
              <span className="text-sm text-gray-400">Хариулаагүй</span>
            ) : isCorrect ? (
              <>
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span className="text-sm font-medium text-emerald-300">Зөв</span>
              </>
            ) : (
              <>
                <XCircle className="w-4 h-4 text-red-400" />
                <span className="text-sm font-medium text-red-300">
                  Буруу — Зөв хариу: {question.answer}
                </span>
              </>
            )}
          </div>
        </div>

        {/* Solution */}
        {question.solution && (
          <div className="mt-3">
            <button
              onClick={() => setShowSolution(!showSolution)}
              className="flex items-center gap-1 text-sm text-primary-400 hover:text-primary-300 font-medium transition-colors"
            >
              {showSolution ? (
                <>
                  <ChevronUp className="w-4 h-4" /> Бодолтыг нуух
                </>
              ) : (
                <>
                  <ChevronDown className="w-4 h-4" /> Бодолтыг харах
                </>
              )}
            </button>
            {showSolution && (
              <div className="mt-2 text-sm text-gray-400 leading-relaxed">
                <MathText text={question.solution} />
              </div>
            )}
          </div>
        )}
      </div>
    );
  }

  // Instant mode (original behavior)
  const { onAnswer } = props as InstantModeProps;
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
      className={`card-glass p-5 mb-4 transition-all ${
        highlight ? "border-orange-400/30 shadow-orange-500/5" : ""
      }`}
    >
      {highlight && (
        <div className="mb-3">
          <span className="text-xs font-medium px-2 py-1 rounded-full bg-orange-500/10 text-orange-400 border border-orange-400/20">
            Сайжруулах сэдэв
          </span>
        </div>
      )}

      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2.5">
          <span className="bg-primary-500/20 text-primary-300 text-sm font-bold rounded-full w-8 h-8 flex items-center justify-center border border-primary-400/20">
            {question.questionNumber}
          </span>
          <span className="text-xs font-medium px-2.5 py-1 rounded-full bg-primary-500/10 text-primary-300 border border-primary-400/15">
            {TOPIC_LABELS[question.topic] || question.topic}
          </span>
          {question.subtopic && (
            <span className="text-xs text-gray-500">{question.subtopic}</span>
          )}
        </div>
        {"label" in diff && (
          <span
            className={`text-xs font-medium px-2 py-1 rounded-full border ${(diff as any).cls}`}
          >
            {(diff as any).label}
          </span>
        )}
      </div>

      {/* Question body */}
      <div className="text-gray-200 text-[15px] leading-relaxed mb-5">
        <MathText text={question.body} />
      </div>

      {/* Options */}
      {question.options && (
        <div className="space-y-2 mb-4">
          {Object.entries(question.options).map(([letter, text]) => {
            let optionCls =
              "border-white/[0.08] hover:border-primary-400/40 hover:bg-primary-500/5";

            if (selected) {
              if (letter === question.answer) {
                optionCls = "border-emerald-400/50 bg-emerald-500/10";
              } else if (letter === selected && !isCorrect) {
                optionCls = "border-red-400/50 bg-red-500/10";
              } else {
                optionCls = "border-white/[0.05] opacity-40";
              }
            }

            return (
              <button
                key={letter}
                onClick={() => handleSelect(letter)}
                disabled={!!selected}
                className={`w-full text-left px-4 py-3 rounded-xl border transition-all flex items-center gap-3 ${optionCls}`}
              >
                <span
                  className={`w-7 h-7 rounded-full border flex items-center justify-center text-sm font-bold shrink-0 ${
                    selected && letter === question.answer
                      ? "border-emerald-400 bg-emerald-500 text-white"
                      : selected && letter === selected && !isCorrect
                        ? "border-red-400 bg-red-500 text-white"
                        : "border-gray-600 text-gray-400"
                  }`}
                >
                  {letter}
                </span>
                <span className="text-gray-300 text-sm">
                  <MathText text={text} />
                </span>
              </button>
            );
          })}
        </div>
      )}

      {/* Result */}
      {selected && hasAnswer && (
        <div
          className={`mt-4 p-4 rounded-xl border ${
            isCorrect
              ? "bg-emerald-500/10 border-emerald-400/20"
              : "bg-red-500/10 border-red-400/20"
          }`}
        >
          <div className="flex items-center gap-2">
            {isCorrect ? (
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
            ) : (
              <XCircle className="w-5 h-5 text-red-400" />
            )}
            <p
              className={`font-semibold text-sm ${
                isCorrect ? "text-emerald-300" : "text-red-300"
              }`}
            >
              {isCorrect ? "Зөв байна!" : `Буруу. Зөв хариу: ${question.answer}`}
            </p>
          </div>

          {question.solution && (
            <div className="mt-3">
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="flex items-center gap-1 text-sm text-primary-400 hover:text-primary-300 font-medium transition-colors"
              >
                {showSolution ? (
                  <>
                    <ChevronUp className="w-4 h-4" /> Бодолтыг нуух
                  </>
                ) : (
                  <>
                    <ChevronDown className="w-4 h-4" /> Бодолтыг харах
                  </>
                )}
              </button>
              {showSolution && (
                <div className="mt-2 text-sm text-gray-400 leading-relaxed">
                  <MathText text={question.solution} />
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Reset */}
      {selected && (
        <button
          onClick={() => {
            setLocalSelected(null);
            setShowSolution(false);
          }}
          className="mt-3 flex items-center gap-1.5 text-sm text-gray-500 hover:text-gray-300 transition-colors"
        >
          <RotateCcw className="w-3.5 h-3.5" /> Дахин бодох
        </button>
      )}
    </div>
  );
}
