"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, X, Sparkles, RotateCcw } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { useAuth } from "@/lib/auth-context";
import { getPlacementBank, displayQuestion, type PlacementQuestion } from "@/lib/placement-bank";
import {
  initPlacement,
  pickNext,
  applyAnswer,
  isComplete,
  totalQuestions,
  summarize,
  type PlacementState,
} from "@/lib/placement-engine";
import { savePlacement, type StoredPlacement } from "@/lib/placement-result";

type Phase = "intro" | "quiz" | "done";

export default function PlacementPage() {
  const bank = useMemo(() => getPlacementBank(), []);
  const { user } = useAuth();

  const [phase, setPhase] = useState<Phase>("intro");
  const [state, setState] = useState<PlacementState>(() => initPlacement(bank, 2));
  const [current, setCurrent] = useState<PlacementQuestion | null>(null);
  const [picked, setPicked] = useState<number | null>(null);
  const [result, setResult] = useState<StoredPlacement | null>(null);

  const total = totalQuestions(state);
  const answered = state.answers.length;
  const disp = useMemo(() => (current ? displayQuestion(current) : null), [current]);

  function start() {
    const fresh = initPlacement(bank, 2);
    setState(fresh);
    setCurrent(pickNext(fresh, bank));
    setPicked(null);
    setResult(null);
    setPhase("quiz");
  }

  function choose(i: number) {
    if (picked !== null) return;
    setPicked(i);
  }

  function next() {
    if (current === null || picked === null || disp === null) return;
    const advanced = applyAnswer(state, current, disp.toOriginal[picked]);
    setState(advanced);
    setPicked(null);
    if (isComplete(advanced)) {
      const r = summarize(advanced, bank);
      const stored = savePlacement(r, user?.id);
      setResult(stored);
      setCurrent(null);
      setPhase("done");
    } else {
      setCurrent(pickNext(advanced, bank));
    }
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math/6" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Grade 6 · Placement</div>
        </div>

        {phase === "intro" && <Intro onStart={start} total={total} isAuthed={!!user} />}
        {phase === "quiz" && current && disp && (
          <Quiz q={current} options={disp.options} correctIndex={disp.correctIndex} picked={picked} onChoose={choose} onNext={next} index={answered} total={total} level={state.level} />
        )}
        {phase === "done" && result && <Results result={result} onRetake={start} />}
      </div>
    </div>
  );
}

function Intro({ onStart, total, isAuthed }: { onStart: () => void; total: number; isAuthed: boolean }) {
  return (
    <div>
      <div className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] mb-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
        <Sparkles className="h-3.5 w-3.5" /> Personalized placement
      </div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
        Find your starting point
      </h1>
      <p className="mt-4" style={{ color: "var(--fg-1)", fontSize: 16, lineHeight: 1.6 }}>
        About <b className="tabular">{total}</b> questions that start easy and get harder as you go. We'll place you at a level and build a plan that tells you exactly which topics to focus on first.
      </p>
      <ul className="mt-5 space-y-2" style={{ color: "var(--fg-2)", fontSize: 14 }}>
        {["Adapts to you — right answers unlock harder questions.", "Covers every Grade-6 topic so we can spot your weak spots.", "Ends with a plan and “important for you” marks on the topics that need attention."].map((t) => (
          <li key={t} className="flex items-start gap-2">
            <Check className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
            <span><MathText text={t} /></span>
          </li>
        ))}
      </ul>
      <div className="mt-6 rounded-xl p-3 text-[13px]" style={{ background: "var(--bg-1)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
        {isAuthed ? (
          <>Your result and plan will be saved to <b>your account</b> on this device.</>
        ) : (
          <>You can take it now — <Link href="/sign-in" style={{ color: "var(--accent)" }}>sign in</Link> to save the plan to your account so it's always here.</>
        )}
      </div>
      <button type="button" onClick={onStart} className="btn btn-primary mt-6 inline-flex items-center gap-1.5">
        Start the test <ArrowRight className="h-4 w-4" />
      </button>
    </div>
  );
}

function Quiz({
  q, options, correctIndex, picked, onChoose, onNext, index, total, level,
}: {
  q: PlacementQuestion; options: string[]; correctIndex: number; picked: number | null; onChoose: (i: number) => void; onNext: () => void; index: number; total: number; level: number;
}) {
  const pct = total > 0 ? (index / total) * 100 : 0;
  const answered = picked !== null;
  const diffLabel = ["", "Easier", "Medium", "Harder"][q.difficulty] ?? "";
  return (
    <div>
      {/* progress */}
      <div className="flex items-center justify-between mb-2 text-[12px]" style={{ color: "var(--fg-3)" }}>
        <span className="mono">Question {index + 1} / {total}</span>
        <span className="mono">{diffLabel} · level {level}</span>
      </div>
      <div className="h-1.5 w-full overflow-hidden rounded-full mb-6" style={{ background: "var(--bg-2)" }}>
        <div className="h-full rounded-full" style={{ width: `${pct}%`, background: "var(--accent)", transition: "width 0.4s cubic-bezier(0.22,1,0.36,1)" }} />
      </div>

      <div className="eyebrow mb-1">{q.topicTitle}</div>
      <p className="font-sans" style={{ fontSize: 18, lineHeight: 1.5, color: "var(--fg)" }}>
        <MathText text={q.prompt} />
      </p>

      <div className="mt-5 grid gap-2.5 sm:grid-cols-2">
        {options.map((opt, i) => {
          const isCorrect = answered && i === correctIndex;
          const isYours = answered && i === picked;
          const isWrong = isYours && i !== q.correctIndex;
          let bg = "var(--bg-2)", border = "var(--line)", color = "var(--fg)";
          if (isCorrect) { bg = "rgba(63,178,127,0.14)"; border = "#3fb27f"; }
          else if (isWrong) { bg = "rgba(215,80,63,0.10)"; border = "rgba(215,80,63,0.5)"; color = "var(--fg-2)"; }
          return (
            <button
              key={i}
              type="button"
              onClick={() => onChoose(i)}
              disabled={answered}
              className="gm-press flex items-center justify-between gap-2 rounded-xl px-4 py-3 text-left"
              style={{ background: bg, border: `1.5px solid ${border}`, color, opacity: answered && !isCorrect && !isYours ? 0.5 : 1 }}
            >
              <span className="q-math" style={{ fontSize: 15 }}><MathText text={opt} /></span>
              {isCorrect && <span className="grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "#3fb27f", color: "#fff" }}><Check className="h-4 w-4" /></span>}
              {isWrong && <span className="grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "rgba(215,80,63,0.85)", color: "#fff" }}><X className="h-4 w-4" /></span>}
            </button>
          );
        })}
      </div>

      {answered && (
        <>
          {q.explanation && (
            <div className="mt-4 rounded-xl p-3" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
              <p className="font-sans" style={{ fontSize: 14, lineHeight: 1.5, color: "var(--fg-1)" }}>
                <MathText text={q.explanation} />
              </p>
            </div>
          )}
          <div className="mt-5 flex justify-end">
            <button type="button" onClick={onNext} className="btn btn-primary inline-flex items-center gap-1.5">
              {index + 1 >= total ? "See my results" : "Next question"} <ArrowRight className="h-4 w-4" />
            </button>
          </div>
        </>
      )}
    </div>
  );
}

function Results({ result, onRetake }: { result: StoredPlacement; onRetake: () => void }) {
  const priority = result.priorityTopics
    .map((slug) => result.topicScores.find((t) => t.slug === slug))
    .filter((t): t is NonNullable<typeof t> => !!t);
  const strong = result.topicScores.filter((t) => t.accuracy >= 0.75).sort((a, b) => b.accuracy - a.accuracy);
  const pct = Math.round(result.overallAccuracy * 100);

  return (
    <div>
      <div className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] mb-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
        <Sparkles className="h-3.5 w-3.5" /> Your plan is ready
      </div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(28px, 5vw, 44px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
        You're at the <span style={{ color: "var(--accent)" }}>{result.level}</span> level
      </h1>
      <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15 }}>
        You answered <b className="tabular">{pct}%</b> correct across the topics we tested.
      </p>

      {/* Priority plan */}
      {priority.length > 0 ? (
        <div className="mt-8">
          <div className="eyebrow mb-3">Start here — important for you</div>
          <div className="space-y-2.5">
            {priority.map((t, i) => (
              <Link key={t.slug} href={`/math/6/${t.slug}`} className="card-edit p-4 flex items-center gap-4" style={{ textDecoration: "none" }}>
                <span className="mono text-[12px] tabular flex-shrink-0" style={{ color: "var(--accent)", minWidth: 20 }}>{i + 1}</span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <p className="serif" style={{ fontSize: 17, color: "var(--fg)" }}>{t.title}</p>
                    <span className="rounded-full px-2 py-0.5 text-[10px] font-medium" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
                      Important for you
                    </span>
                  </div>
                  <TopicBar accuracy={t.accuracy} />
                </div>
                <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
              </Link>
            ))}
          </div>
        </div>
      ) : (
        <div className="mt-8 rounded-xl p-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg-1)" }}>
          Strong across the board — no single topic stands out as a weak spot. Keep going and try the harder practice sets.
        </div>
      )}

      {/* Strengths */}
      {strong.length > 0 && (
        <div className="mt-8">
          <div className="eyebrow mb-3">You're already solid on</div>
          <div className="flex flex-wrap gap-2">
            {strong.map((t) => (
              <Link key={t.slug} href={`/math/6/${t.slug}`} className="rounded-full px-3 py-1.5 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)", textDecoration: "none" }}>
                {t.title}
              </Link>
            ))}
          </div>
        </div>
      )}

      <div className="mt-10 flex items-center gap-3">
        <Link href="/math/6" className="btn btn-primary inline-flex items-center gap-1.5">
          Go to my topics <ArrowRight className="h-4 w-4" />
        </Link>
        <button type="button" onClick={onRetake} className="btn btn-line inline-flex items-center gap-1.5">
          <RotateCcw className="h-4 w-4" /> Retake
        </button>
      </div>
    </div>
  );
}

function TopicBar({ accuracy }: { accuracy: number }) {
  const pct = Math.round(accuracy * 100);
  const col = accuracy >= 0.75 ? "#3fb27f" : accuracy >= 0.4 ? "var(--accent)" : "var(--danger, #d7503f)";
  return (
    <div className="mt-1.5 flex items-center gap-2">
      <div className="h-1.5 flex-1 overflow-hidden rounded-full" style={{ background: "var(--bg-3, var(--bg-2))" }}>
        <div className="h-full rounded-full" style={{ width: `${pct}%`, background: col }} />
      </div>
      <span className="mono text-[11px] tabular" style={{ color: "var(--fg-3)" }}>{pct}%</span>
    </div>
  );
}
