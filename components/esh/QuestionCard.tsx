"use client";

import { useState } from "react";
import MathText from "./MathText";
import { CheckCircle2, XCircle, RotateCcw, ChevronDown, ChevronUp } from "lucide-react";

interface Question {
  source: string;
  questionNumber: number;
  type: string;
  topic: string;
  subtopic: string;
  difficulty: number;
  body: string;
  options?: Record<string, string>;
  answer: string;
  solution: string;
}

interface QuestionCardProps {
  question: Question;
  onAnswer?: (
    questionSource: string,
    topic: string,
    subtopic: string,
    difficulty: number,
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) => void;
  highlight?: boolean;
}

const topicLabels: Record<string, string> = {
  algebra: "Алгебр",
  geometry: "Геометр",
  trigonometry: "Тригнометр",
  calculus: "Анализ",
  probability: "Магадлал",
  statistics: "Статистик",
  sequences: "Дараалал",
  functions: "Функц",
  logarithms: "Логарифм",
  combinatorics: "Комбинаторик",
  other: "Бусад",
};

const difficultyConfig = [
  {},
  { label: "Хөнгөн", cls: "bg-emerald-500/10 text-emerald-400 border-emerald-400/20" },
  { label: "Дунд", cls: "bg-yellow-500/10 text-yellow-400 border-yellow-400/20" },
  { label: "Хүнд", cls: "bg-red-500/10 text-red-400 border-red-400/20" },
];

export default function QuestionCard({ question, onAnswer, highlight }: QuestionCardProps) {
  const [selected, setSelected] = useState<string | null>(null);
  const [showSolution, setShowSolution] = useState(false);

  const isCorrect = selected === question.answer;
  const hasAnswer = question.answer && question.answer.length > 0;
  const diff = difficultyConfig[question.difficulty] || {};

  const handleSelect = (letter: string) => {
    if (selected) return;
    setSelected(letter);
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
            {topicLabels[question.topic] || question.topic}
          </span>
          {question.subtopic && (
            <span className="text-xs text-gray-500">{question.subtopic}</span>
          )}
        </div>
        {'label' in diff && (
          <span className={`text-xs font-medium px-2 py-1 rounded-full border ${(diff as any).cls}`}>
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
              {isCorrect
                ? "Зөв байна!"
                : `Буруу. Зөв хариу: ${question.answer}`}
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
            setSelected(null);
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
