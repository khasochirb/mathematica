"use client";

// Refinement loop — UI orchestrator (Phase 3c).
//
// Renders the current §1 state from useRefinementLoop() and dispatches events,
// delegating all question rendering to QuestionCard (review / instant / test
// modes) and all selection to lib/refinement-loop-select. The loop's content
// is ЭЕШ (Mongolian), so chrome labels here are Mongolian per design §6 Q1.
//
// Selection lists for similar/drill rounds are held in a useMemo keyed on the
// state + session id, so they stay stable within a state and re-derive
// deterministically (seeded by the session id) on resume. mini-test / retest
// lists live on the session (set when entering those states).

import { useMemo, useState } from "react";
import Link from "next/link";
import { CheckCircle2, Sparkles } from "lucide-react";
import MathText from "./MathText";
import QuestionCard from "./QuestionCard";
import { getAllQuestions, getQuestionBySource } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";
import useRefinementLoop from "@/lib/use-refinement-loop";
import {
  hashSeed,
  selectSimilarProblems,
  selectMiniTest,
  selectDrill,
} from "@/lib/refinement-loop-select";
import { drillReadyForRetest } from "@/lib/refinement-loop";

function resolve(sources: readonly string[]): Question[] {
  return sources.map((s) => getQuestionBySource(s)).filter((q): q is Question => !!q);
}

export default function RefinementLoop() {
  const { session, loading, dispatch } = useRefinementLoop();
  const pool = useMemo(() => getAllQuestions(), []);
  // Local answer collection for the no-feedback test phases (mini-test / retest).
  const [answers, setAnswers] = useState<Record<string, string>>({});

  const trigger = session ? getQuestionBySource(session.triggeredQuestion) : undefined;
  const seed = session ? hashSeed(session.id) : 0;

  // Similar / drill question batches — stable within a state, deterministic on resume.
  const similars = useMemo(
    () => (trigger && session?.state === "similar_problems" ? selectSimilarProblems(trigger, pool, { seed }) : []),
    [trigger, session?.state, pool, seed],
  );
  const drills = useMemo(
    () => (trigger && session?.state === "drill_mode" ? selectDrill(trigger, pool, { seed, count: 10 }) : []),
    [trigger, session?.state, pool, seed],
  );

  if (loading) {
    return <Shell><p style={{ color: "var(--fg-2)" }}>Ачааллаж байна…</p></Shell>;
  }
  if (!session) {
    return (
      <Shell>
        <p className="serif" style={{ fontSize: 22 }}>Идэвхтэй давтлага алга байна.</p>
        <p style={{ color: "var(--fg-2)", marginTop: 8 }}>
          Шалгалтын дүнгийн хуудаснаас алдсан бодлогоо сонгож &laquo;Бүрэн эзэмших&raquo; товчийг дарж эхлүүлээрэй.
        </p>
        <Link href="/practice/esh" className="btn btn-line mt-6">Дасгал руу буцах</Link>
      </Shell>
    );
  }
  if (!trigger) {
    return <Shell><p style={{ color: "var(--danger)" }}>Бодлого олдсонгүй ({session.triggeredQuestion}).</p></Shell>;
  }

  const s = session.state;

  // ── POST_MISS_RESULT ────────────────────────────────────────────────
  if (s === "post_miss_result") {
    const onContinue = () => {
      const sims = selectSimilarProblems(trigger, pool, { seed });
      if (sims.length > 0) {
        dispatch({ type: "continue", similarShown: sims.length });
      } else {
        const mini = selectMiniTest(trigger, pool, { seed });
        dispatch({ type: "continue", similarShown: 0, miniTest: mini.map((q) => q.source) });
      }
    };
    return (
      <Shell title="Алдсан бодлого">
        <QuestionCard mode="review" question={trigger} />
        <div className="flex gap-3 flex-wrap mt-6">
          <button className="btn btn-primary" onClick={onContinue}>Үргэлжлүүлэх</button>
          <button className="btn btn-line" onClick={() => dispatch({ type: "explain" })}>Илүү тайлбар</button>
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>
            Алгасах
          </button>
        </div>
      </Shell>
    );
  }

  // ── STEP_BY_STEP (graceful: shows the full solution; step list not authored yet)
  if (s === "step_by_step") {
    return (
      <Shell title="Алхам алхмаар">
        <div className="p-5 rounded-xl" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
          <div className="serif" style={{ fontSize: 18, marginBottom: 12 }}><MathText text={trigger.body} /></div>
          <MathText text={trigger.solution} />
        </div>
        <button className="btn btn-primary mt-6" onClick={() => dispatch({ type: "stepDone" })}>Үргэлжлүүлэх</button>
      </Shell>
    );
  }

  // ── SIMILAR_PROBLEMS ────────────────────────────────────────────────
  if (s === "similar_problems") {
    const answeredCount = session.similarAttempts.length - ((session.meta.similarMark as number) ?? 0);
    const allAnswered = answeredCount >= similars.length && similars.length > 0;
    const roundCorrect = session.similarAttempts.slice((session.meta.similarMark as number) ?? 0).every((a) => a.correct);
    const goMini = (wantDeeper: boolean) => {
      const mini = selectMiniTest(trigger, pool, { seed, exclude: similars.map((q) => q.source) });
      dispatch({ type: "finishSimilar", wantDeeper, miniTest: mini.map((q) => q.source) });
    };
    return (
      <Shell title="Төстэй бодлого">
        {similars.map((q) => (
          <div key={q.source} className="mb-4">
            <QuestionCard
              mode="instant"
              question={q}
              onAnswer={(src, _t, _st, _sel, _cor, isCorrect) =>
                dispatch({ type: "answerSimilar", source: src, correct: isCorrect })
              }
            />
          </div>
        ))}
        {allAnswered && (
          <div className="flex gap-3 flex-wrap mt-4">
            <button className="btn btn-primary" onClick={() => goMini(false)}>Шалгалт хийх</button>
            {!roundCorrect && (
              <button className="btn btn-line" onClick={() => dispatch({ type: "finishSimilar", wantDeeper: true })}>
                Илүү тайлбар үзэх
              </button>
            )}
          </div>
        )}
      </Shell>
    );
  }

  // ── MINI_TEST / RETEST (no instant feedback; submit at end) ─────────
  if (s === "mini_test" || s === "retest") {
    const sources = s === "mini_test" ? session.miniTestQuestions : session.retestQuestions;
    const qs = resolve(sources);
    const allAnswered = qs.length > 0 && qs.every((q) => answers[q.source]);
    const submit = () => {
      const score = qs.filter((q) => answers[q.source] === q.answer).length;
      setAnswers({});
      if (s === "mini_test") dispatch({ type: "submitMiniTest", score });
      else dispatch({ type: "submitRetest", score });
    };
    return (
      <Shell title={s === "mini_test" ? "Бясалгалын шалгалт" : "Дахин шалгалт"}>
        <p style={{ color: "var(--fg-2)", marginBottom: 16 }}>
          {qs.length} бодлого · хариугаа сонгоод доор &laquo;Илгээх&raquo; дарна уу.
        </p>
        {qs.map((q, i) => (
          <div key={q.source} className="mb-4">
            <QuestionCard
              mode="test"
              question={q}
              questionIndex={i + 1}
              selectedAnswer={answers[q.source] ?? null}
              onSelectAnswer={(letter) => setAnswers((a) => ({ ...a, [q.source]: letter }))}
            />
          </div>
        ))}
        <button className="btn btn-primary mt-2" disabled={!allAnswered} onClick={submit} style={{ opacity: allAnswered ? 1 : 0.5 }}>
          Илгээх
        </button>
      </Shell>
    );
  }

  // ── MINI_TEST_RESULT ────────────────────────────────────────────────
  if (s === "mini_test_result") {
    const total = session.miniTestQuestions.length;
    const disp = session.meta.miniDisposition as "mastered" | "drill" | "relearn";
    const label = disp === "mastered" ? "Дуусгах" : disp === "drill" ? "Дасгал хийх" : "Дахин тайлбар үзэх";
    return (
      <ResultShell score={session.miniTestScore ?? 0} total={total} title="Шалгалтын дүн">
        <button className="btn btn-primary" onClick={() => dispatch({ type: "acceptMiniTestOutcome" })}>{label}</button>
        {disp !== "mastered" && (
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>Алгасах</button>
        )}
      </ResultShell>
    );
  }

  // ── DRILL_MODE ──────────────────────────────────────────────────────
  if (s === "drill_mode") {
    const ready = drillReadyForRetest(session.drillStreak);
    const retake = () => {
      const used = Array.from(
        new Set<string>([...session.miniTestQuestions, ...session.drillAttempts.map((d) => d.source)]),
      );
      const rt = selectMiniTest(trigger, pool, { seed, exclude: used });
      dispatch({ type: "retakeFromDrill", retest: rt.map((q) => q.source) });
    };
    return (
      <Shell title="Дасгал">
        <p style={{ color: "var(--fg-2)", marginBottom: 16 }}>
          Дараалан зөв бодсон: <b style={{ color: "var(--accent)" }}>{session.drillStreak}</b> / 3
        </p>
        {drills.map((q) => (
          <div key={q.source} className="mb-4">
            <QuestionCard
              mode="instant"
              question={q}
              onAnswer={(src, _t, _st, _sel, _cor, isCorrect) =>
                dispatch({ type: "answerDrill", source: src, correct: isCorrect })
              }
            />
          </div>
        ))}
        <div className="flex gap-3 flex-wrap mt-2">
          <button className="btn btn-primary" disabled={!ready} onClick={retake} style={{ opacity: ready ? 1 : 0.5 }}>
            Шалгалт давтах
          </button>
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>Алгасах</button>
        </div>
      </Shell>
    );
  }

  // ── RETEST_RESULT ───────────────────────────────────────────────────
  if (s === "retest_result") {
    return (
      <ResultShell score={session.retestScore ?? 0} total={session.retestQuestions.length} title="Дахин шалгалтын дүн">
        <button className="btn btn-primary" onClick={() => dispatch({ type: "acceptRetestOutcome" })}>Үргэлжлүүлэх</button>
      </ResultShell>
    );
  }

  // ── TERMINAL ────────────────────────────────────────────────────────
  const mastered = s === "exit_mastered";
  return (
    <Shell>
      <div className="text-center py-10">
        {mastered ? (
          <CheckCircle2 className="mx-auto mb-4" style={{ width: 56, height: 56, color: "var(--accent)" }} />
        ) : (
          <Sparkles className="mx-auto mb-4" style={{ width: 48, height: 48, color: "var(--fg-3)" }} />
        )}
        <h2 className="serif" style={{ fontSize: 30, fontWeight: 400 }}>
          {mastered ? "Бүрэн эзэмшлээ! 🎉" : "Дараа дахин үргэлжлүүлээрэй"}
        </h2>
        <p style={{ color: "var(--fg-2)", marginTop: 10, maxWidth: "44ch", marginInline: "auto" }}>
          {mastered
            ? "Энэ сэдвийг сайн эзэмшсэн байна. Шинэ сэдэв дээр давтлага хийж болно."
            : "Энэ сэдэв одоохондоо хэцүү байна. Хэдэн хоногийн дараа дахин оролдоорой."}
        </p>
        <Link href="/practice/esh" className="btn btn-primary mt-8">Дасгал руу буцах</Link>
      </div>
    </Shell>
  );
}

function Shell({ title, children }: { title?: string; children: React.ReactNode }) {
  return (
    <div className="max-w-3xl mx-auto px-5 py-10" style={{ minHeight: "70vh" }}>
      {title && <div className="eyebrow mb-6">{title}</div>}
      {children}
    </div>
  );
}

function ResultShell({ score, total, title, children }: { score: number; total: number; title: string; children: React.ReactNode }) {
  const pct = total > 0 ? Math.round((score / total) * 100) : 0;
  return (
    <Shell title={title}>
      <div className="text-center py-6">
        <div className="serif" style={{ fontSize: 64, letterSpacing: "-0.03em", lineHeight: 1 }}>
          {score}
          <span className="mono" style={{ fontSize: 22, color: "var(--fg-3)" }}>/{total}</span>
        </div>
        <div className="mono mt-2" style={{ color: pct >= 80 ? "var(--accent)" : "var(--fg-2)", fontSize: 14 }}>{pct}%</div>
      </div>
      <div className="flex gap-3 flex-wrap justify-center mt-4">{children}</div>
    </Shell>
  );
}
