"use client";

// Refinement loop — UI orchestrator (Phase 3c).
//
// Renders the current §1 state from useRefinementLoop() and dispatches events,
// delegating question rendering to QuestionCard (review / instant / test modes)
// and selection to lib/refinement-loop-select.
//
// Language: question CONTENT stays in its own language (ЭЕШ = Mongolian), but
// all chrome — buttons, headings, instructions — follows the global EN/MN
// toggle (per the §4 Q7 rule: navigation is bilingual, content is not).
//
// "Илүү тайлбар" / step-by-step is intentionally NOT offered as an optional
// branch yet: step_by_step_solution content isn't authored, so it would just
// re-show the same solution. It remains reachable only on the relearn path
// (mini-test < 40%), where re-reading the solution before retrying is useful.

import { useMemo, useState } from "react";
import Link from "next/link";
import { CheckCircle2, Sparkles } from "lucide-react";
import MathText from "./MathText";
import QuestionCard from "./QuestionCard";
import TutorPanel from "@/components/tutor/TutorPanel";
import { useLang } from "@/lib/lang-context";
import { getAllQuestions, getQuestionBySource } from "@/lib/esh-questions";
import usePerformance from "@/lib/use-performance";
import type { Question } from "@/lib/esh-questions";
import useRefinementLoop from "@/lib/use-refinement-loop";
import {
  hashSeed,
  selectSimilarProblems,
  selectMiniTest,
  selectDrill,
} from "@/lib/refinement-loop-select";
import { drillReadyForRetest } from "@/lib/refinement-loop";

type Bi = { en: string; mn: string };
const T = {
  loading: { en: "Loading…", mn: "Ачааллаж байна…" },
  noActive: { en: "No active practice loop.", mn: "Идэвхтэй давтлага алга байна." },
  noActiveBody: {
    en: "From a test's results page, pick a missed question and press “Master this” to begin.",
    mn: "Шалгалтын дүнгийн хуудаснаас алдсан бодлогоо сонгож «Бүрэн эзэмших» товчийг дарж эхлүүлээрэй.",
  },
  back: { en: "Back to practice", mn: "Дасгал руу буцах" },
  notFound: { en: "Question not found", mn: "Бодлого олдсонгүй" },
  missTitle: { en: "The question you missed", mn: "Алдсан бодлого" },
  continue: { en: "Continue", mn: "Үргэлжлүүлэх" },
  skip: { en: "Skip", mn: "Алгасах" },
  stepTitle: { en: "Review the solution", mn: "Бодолтыг дахин үзэх" },
  similarTitle: { en: "Similar problems", mn: "Төстэй бодлого" },
  takeTest: { en: "Take the test", mn: "Шалгалт хийх" },
  miniTitle: { en: "Mini-test", mn: "Шалгалт" },
  retestTitle: { en: "Retest", mn: "Дахин шалгалт" },
  miniInstr: { en: "Pick an answer for each, then press Submit below.", mn: "Хариугаа сонгоод доор «Илгээх» дарна уу." },
  submit: { en: "Submit", mn: "Илгээх" },
  miniResult: { en: "Test result", mn: "Шалгалтын дүн" },
  retestResult: { en: "Retest result", mn: "Дахин шалгалтын дүн" },
  finish: { en: "Finish", mn: "Дуусгах" },
  doDrills: { en: "Practice drills", mn: "Дасгал хийх" },
  reviewAgain: { en: "Review again", mn: "Дахин үзэх" },
  drillTitle: { en: "Drills", mn: "Дасгал" },
  streak: { en: "Correct in a row", mn: "Дараалан зөв бодсон" },
  retake: { en: "Retake the test", mn: "Шалгалт давтах" },
  masteredTitle: { en: "Mastered! 🎉", mn: "Бүрэн эзэмшлээ! 🎉" },
  abandonedTitle: { en: "Continue another time", mn: "Дараа дахин үргэлжлүүлээрэй" },
  masteredBody: {
    en: "You've got a solid grip on this topic now. Pick a new topic whenever you're ready.",
    mn: "Энэ сэдвийг сайн эзэмшсэн байна. Бэлэн болоход шинэ сэдэв дээр давтлага хийж болно.",
  },
  abandonedBody: {
    en: "This topic is tough right now. Give it another go in a few days.",
    mn: "Энэ сэдэв одоохондоо хэцүү байна. Хэдэн хоногийн дараа дахин оролдоорой.",
  },
};

function resolve(sources: readonly string[]): Question[] {
  return sources.map((s) => getQuestionBySource(s)).filter((q): q is Question => !!q);
}

export default function RefinementLoop() {
  const { lang } = useLang();
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);
  const { session, loading, dispatch } = useRefinementLoop();
  const perf = usePerformance();
  const pool = useMemo(() => getAllQuestions(), []);

  // Every answered question inside the loop also lands in the main attempt
  // stream as a drill (never "test" — loop mini-tests must not masquerade as
  // full practice-test sessions in projections). The loop session row keeps
  // its own copy for the state machine; this fan-out is what makes loop work
  // visible to topic/skill analytics and the dashboard.
  const recordLoopAttempt = (
    src: string,
    topic: string,
    subtopic: string,
    selected: string,
    correct: string,
    isCorrect: boolean,
  ) =>
    perf.recordAttempt({
      questionSource: src,
      topic,
      subtopic,
      selectedAnswer: selected,
      correctAnswer: correct,
      isCorrect,
      source: "drill",
    });
  const [answers, setAnswers] = useState<Record<string, string>>({});

  const trigger = session ? getQuestionBySource(session.triggeredQuestion) : undefined;
  const seed = session ? hashSeed(session.id) : 0;

  const similars = useMemo(
    () => (trigger && session?.state === "similar_problems" ? selectSimilarProblems(trigger, pool, { seed }) : []),
    [trigger, session?.state, pool, seed],
  );
  const drills = useMemo(
    () => (trigger && session?.state === "drill_mode" ? selectDrill(trigger, pool, { seed, count: 10 }) : []),
    [trigger, session?.state, pool, seed],
  );

  if (loading) return <Shell><p style={{ color: "var(--fg-2)" }}>{L(T.loading)}</p></Shell>;
  if (!session) {
    return (
      <Shell>
        <p className="serif" style={{ fontSize: 22 }}>{L(T.noActive)}</p>
        <p style={{ color: "var(--fg-2)", marginTop: 8 }}>{L(T.noActiveBody)}</p>
        <Link href="/practice/esh" className="btn btn-line mt-6">{L(T.back)}</Link>
      </Shell>
    );
  }
  if (!trigger) {
    return <Shell><p style={{ color: "var(--danger)" }}>{L(T.notFound)} ({session.triggeredQuestion}).</p></Shell>;
  }

  const s = session.state;

  if (s === "post_miss_result") {
    const onContinue = () => {
      const sims = selectSimilarProblems(trigger, pool, { seed });
      if (sims.length > 0) dispatch({ type: "continue", similarShown: sims.length });
      else dispatch({ type: "continue", similarShown: 0, miniTest: selectMiniTest(trigger, pool, { seed }).map((q) => q.source) });
    };
    return (
      <Shell title={L(T.missTitle)}>
        <QuestionCard mode="review" question={trigger} />
        <div className="flex gap-3 flex-wrap mt-6">
          <button className="btn btn-primary" onClick={onContinue}>{L(T.continue)}</button>
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>{L(T.skip)}</button>
        </div>
        {/* AI tutor grounded on the exact missed question. */}
        <TutorPanel
          context={{
            kind: "question",
            course: "ЭЕШ",
            unit: trigger.topic,
            question: trigger.body,
            options: trigger.options,
            correctAnswer: trigger.answer,
            solution: trigger.solution,
          }}
        />
      </Shell>
    );
  }

  if (s === "step_by_step") {
    return (
      <Shell title={L(T.stepTitle)}>
        <div className="p-5 rounded-xl" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
          <div className="serif" style={{ fontSize: 18, marginBottom: 12 }}><MathText text={trigger.body} /></div>
          <MathText text={trigger.solution} />
        </div>
        <button className="btn btn-primary mt-6" onClick={() => dispatch({ type: "stepDone" })}>{L(T.continue)}</button>
      </Shell>
    );
  }

  if (s === "similar_problems") {
    const answeredCount = session.similarAttempts.length - ((session.meta.similarMark as number) ?? 0);
    const allAnswered = answeredCount >= similars.length && similars.length > 0;
    const goMini = () => {
      const mini = selectMiniTest(trigger, pool, { seed, exclude: similars.map((q) => q.source) });
      dispatch({ type: "finishSimilar", wantDeeper: false, miniTest: mini.map((q) => q.source) });
    };
    return (
      <Shell title={L(T.similarTitle)}>
        {similars.map((q) => (
          <div key={q.source} className="mb-4">
            <QuestionCard
              mode="instant"
              question={q}
              onAnswer={(src, t, st, sel, cor, isCorrect) => {
                recordLoopAttempt(src, t, st, sel, cor, isCorrect);
                dispatch({ type: "answerSimilar", source: src, correct: isCorrect });
              }}
            />
          </div>
        ))}
        {allAnswered && (
          <button className="btn btn-primary mt-4" onClick={goMini}>{L(T.takeTest)}</button>
        )}
      </Shell>
    );
  }

  if (s === "mini_test" || s === "retest") {
    const sources = s === "mini_test" ? session.miniTestQuestions : session.retestQuestions;
    const qs = resolve(sources);
    const allAnswered = qs.length > 0 && qs.every((q) => answers[q.source]);
    const submit = () => {
      const score = qs.filter((q) => answers[q.source] === q.answer).length;
      for (const q of qs) {
        const picked = answers[q.source];
        if (!picked) continue;
        recordLoopAttempt(q.source, q.topic, q.subtopic, picked, q.answer, picked === q.answer);
      }
      setAnswers({});
      if (s === "mini_test") dispatch({ type: "submitMiniTest", score });
      else dispatch({ type: "submitRetest", score });
    };
    return (
      <Shell title={s === "mini_test" ? L(T.miniTitle) : L(T.retestTitle)}>
        <p style={{ color: "var(--fg-2)", marginBottom: 16 }}>{qs.length} · {L(T.miniInstr)}</p>
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
          {L(T.submit)}
        </button>
      </Shell>
    );
  }

  if (s === "mini_test_result") {
    const disp = session.meta.miniDisposition as "mastered" | "drill" | "relearn";
    const label = disp === "mastered" ? L(T.finish) : disp === "drill" ? L(T.doDrills) : L(T.reviewAgain);
    return (
      <ResultShell score={session.miniTestScore ?? 0} total={session.miniTestQuestions.length} title={L(T.miniResult)}>
        <button className="btn btn-primary" onClick={() => dispatch({ type: "acceptMiniTestOutcome" })}>{label}</button>
        {disp !== "mastered" && (
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>{L(T.skip)}</button>
        )}
      </ResultShell>
    );
  }

  if (s === "drill_mode") {
    const ready = drillReadyForRetest(session.drillStreak);
    const retake = () => {
      const used = Array.from(new Set<string>([...session.miniTestQuestions, ...session.drillAttempts.map((d) => d.source)]));
      const rt = selectMiniTest(trigger, pool, { seed, exclude: used });
      dispatch({ type: "retakeFromDrill", retest: rt.map((q) => q.source) });
    };
    return (
      <Shell title={L(T.drillTitle)}>
        <p style={{ color: "var(--fg-2)", marginBottom: 16 }}>
          {L(T.streak)}: <b style={{ color: "var(--accent)" }}>{session.drillStreak}</b> / 3
        </p>
        {drills.map((q) => (
          <div key={q.source} className="mb-4">
            <QuestionCard
              mode="instant"
              question={q}
              onAnswer={(src, t, st, sel, cor, isCorrect) => {
                recordLoopAttempt(src, t, st, sel, cor, isCorrect);
                dispatch({ type: "answerDrill", source: src, correct: isCorrect });
              }}
            />
          </div>
        ))}
        <div className="flex gap-3 flex-wrap mt-2">
          <button className="btn btn-primary" disabled={!ready} onClick={retake} style={{ opacity: ready ? 1 : 0.5 }}>{L(T.retake)}</button>
          <button className="btn btn-line" onClick={() => dispatch({ type: "skip" })} style={{ color: "var(--fg-3)" }}>{L(T.skip)}</button>
        </div>
      </Shell>
    );
  }

  if (s === "retest_result") {
    return (
      <ResultShell score={session.retestScore ?? 0} total={session.retestQuestions.length} title={L(T.retestResult)}>
        <button className="btn btn-primary" onClick={() => dispatch({ type: "acceptRetestOutcome" })}>{L(T.continue)}</button>
      </ResultShell>
    );
  }

  const mastered = s === "exit_mastered";
  return (
    <Shell>
      <div className="text-center py-10">
        {mastered ? (
          <CheckCircle2 className="mx-auto mb-4" style={{ width: 56, height: 56, color: "var(--accent)" }} />
        ) : (
          <Sparkles className="mx-auto mb-4" style={{ width: 48, height: 48, color: "var(--fg-3)" }} />
        )}
        <h2 className="serif" style={{ fontSize: 30, fontWeight: 400 }}>{mastered ? L(T.masteredTitle) : L(T.abandonedTitle)}</h2>
        <p style={{ color: "var(--fg-2)", marginTop: 10, maxWidth: "44ch", marginInline: "auto" }}>
          {mastered ? L(T.masteredBody) : L(T.abandonedBody)}
        </p>
        <Link href="/practice/esh" className="btn btn-primary mt-8">{L(T.back)}</Link>
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
