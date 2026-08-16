"use client";

// The placement sitting, for every course hub. Since 2026-08-13 it is driven
// by lib/diagnostic-engine.ts rather than a fixed question grid: a tutor
// working problem by problem, reading WHICH wrong answer you picked, choosing
// what to hand you next, and stopping the moment it knows where you should
// start. See that module's header for the reasoning.
//
// The model is an upgrade, never a dependency. Every failure path — no API
// key, signed out, quota spent, slow network — silently drops to the
// deterministic engine, and the student sees a normal placement.

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import useScrollToTop from "@/lib/use-scroll-to-top";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, X, Sparkles, RotateCcw, Search } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import { getMpToken } from "@/lib/api";
import { displayQuestion, type PlacementQuestion } from "@/lib/placement-bank";
import {
  initDiagnostic,
  recordAnswer,
  deterministicNext,
  stopCheck,
  buildReport,
  toPlacementResult,
  MAX_QUESTIONS,
  type DiagnosticState,
} from "@/lib/diagnostic-engine";
import { consultTutor } from "@/lib/diagnostic-client";
import { savePlacement, type StoredPlacement } from "@/lib/placement-result";

type Phase = "intro" | "quiz" | "thinking" | "done";

export type PlacementVerdictCard = {
  title: string; // e.g. "Start in Grade 8"
  body: string;
  href: string;
  cta: string;
};

export type PlacementConfig = {
  bank: PlacementQuestion[];
  namespace: string; // "grade6" | "geometry"
  crumb: string; // breadcrumb line
  homeHref: string; // where "back" and "go to my …" land
  homeLabel: string; // e.g. "topics" | "units"
  subjectNoun: string; // e.g. "Grade-6 topic" | "Geometry unit"
  topicHref: (slug: string) => string; // link into a topic/unit
  title: string; // intro heading
  /** Band placements turn the result into a "start in Grade N" verdict,
   *  rendered as the first card of the results screen. */
  verdict?: (result: StoredPlacement) => PlacementVerdictCard | null;
};

/** Course label for the tutor's grounding — never a student identifier. */
function courseLabel(config: PlacementConfig): string {
  // "Courses · Grade 11 · Placement" -> "Grade 11"
  const parts = config.crumb.split("·").map((s) => s.trim());
  return parts.length >= 2 ? parts[parts.length - 2] : config.subjectNoun;
}

export default function PlacementRunner({ config }: { config: PlacementConfig }) {
  const { bank } = config;
  const { user } = useAuth();
  const { lang } = useLang();

  const [phase, setPhase] = useState<Phase>("intro");
  const [state, setState] = useState<DiagnosticState>(() => initDiagnostic(bank));
  const [current, setCurrent] = useState<PlacementQuestion | null>(null);
  const [picked, setPicked] = useState<number | null>(null);
  const [result, setResult] = useState<StoredPlacement | null>(null);
  // A sitting in flight must not be resurrected by a late model reply after
  // the student hits "retake" — every consult is tagged with the run it began.
  const runId = useRef(0);
  useScrollToTop(current?.id ?? phase);

  const disp = useMemo(() => (current ? displayQuestion(current) : null), [current]);
  const answered = state.answers.length;
  const tutorOpts = useMemo(
    () => ({ course: courseLabel(config), lang: lang === "mn" ? ("mn" as const) : ("en" as const) }),
    [config, lang],
  );

  const start = useCallback(() => {
    runId.current += 1;
    // A fresh seed per sitting, so a retake draws different variants wherever
    // the bank has spares at the same topic × difficulty.
    const fresh = initDiagnostic(bank, Date.now() >>> 0);
    setState(fresh);
    setCurrent(deterministicNext(fresh, bank));
    setPicked(null);
    setResult(null);
    setPhase("quiz");
  }, [bank]);

  // Everything that happens between answering one question and seeing the
  // next: record the answer, then either finish (consulting the tutor for the
  // closing report) or choose what to ask next. The tutor is consulted ONLY on
  // a miss — a correct answer needs no diagnosis, it needs a harder question —
  // which is what keeps a whole sitting inside a handful of model calls.
  async function advance() {
    if (current === null || picked === null || disp === null) return;
    const myRun = runId.current;
    const after = recordAnswer(state, current, disp.toOriginal[picked]);
    const missed = !after.answers[after.answers.length - 1].correct;
    setPicked(null);
    setCurrent(null);
    setPhase("thinking");
    setState(after);

    const token = getMpToken();
    const { stop } = stopCheck(after, bank);

    if (stop) {
      const consult = token
        ? await consultTutor(after, bank, { ...tutorOpts, token, finalReport: true })
        : null;
      if (myRun !== runId.current) return;
      const finalState = consult?.state ?? after;
      setState(finalState);
      const report = buildReport(finalState, bank, { narrative: consult?.narrative ?? null });
      setResult(savePlacement(toPlacementResult(report), user?.id, config.namespace));
      setPhase("done");
      return;
    }

    let next: PlacementQuestion | null = null;
    if (missed && token) {
      const consult = await consultTutor(after, bank, { ...tutorOpts, token });
      if (myRun !== runId.current) return;
      setState(consult.state);
      next = consult.question;
    }
    // The tutor's pick when there is one, otherwise the engine's. Both draw
    // from the same bank, so the student cannot tell which path ran.
    setCurrent(next ?? deterministicNext(after, bank));
    setPhase("quiz");
  }

  // The engine can also decide the sitting is over before a question is drawn
  // (an exhausted bank on a tiny course); never strand the student on a blank.
  useEffect(() => {
    if (phase === "quiz" && current === null && state.answers.length > 0) {
      const report = buildReport(state, bank);
      setResult(savePlacement(toPlacementResult(report), user?.id, config.namespace));
      setPhase("done");
    }
  }, [phase, current, state, bank, user?.id, config.namespace]);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href={config.homeHref} className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{config.crumb}</div>
        </div>

        {phase === "intro" && <Intro onStart={start} isAuthed={!!user} config={config} />}
        {phase === "thinking" && <Thinking />}
        {phase === "quiz" && current && disp && (
          <Quiz
            q={current}
            options={disp.options}
            correctIndex={disp.correctIndex}
            picked={picked}
            onChoose={(i) => picked === null && setPicked(i)}
            onNext={advance}
            index={answered}
          />
        )}
        {phase === "done" && result && <Results result={result} onRetake={start} config={config} />}
      </div>
    </div>
  );
}

function Intro({ onStart, isAuthed, config }: { onStart: () => void; isAuthed: boolean; config: PlacementConfig }) {
  return (
    <div>
      <div className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] mb-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
        <Sparkles className="h-3.5 w-3.5" /> Personalized placement
      </div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
        {config.title}
      </h1>
      <p className="mt-4" style={{ color: "var(--fg-1)", fontSize: 16, lineHeight: 1.6 }}>
        Not a fixed test — a tutor working through problems with you. It reads
        the answer you picked, not just whether it was right, and it stops as
        soon as it knows where you should start. Usually well under{" "}
        <b className="tabular">{MAX_QUESTIONS}</b> questions.
      </p>
      <ul className="mt-5 space-y-2" style={{ color: "var(--fg-2)", fontSize: 14 }}>
        {[
          "Chooses your next problem from how you answered the last one.",
          `Finds the earliest ${config.subjectNoun} that isn't solid yet — that's where you begin.`,
          "Ends by naming the specific thing to fix first, not just a score.",
        ].map((t) => (
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
          <>You can take it now — <Link href="/sign-in" style={{ color: "var(--accent)" }}>sign in</Link> to save the plan and get the tutor&apos;s read on your answers.</>
        )}
      </div>
      <button type="button" onClick={onStart} className="btn btn-primary mt-6 inline-flex items-center gap-1.5">
        Start the test <ArrowRight className="h-4 w-4" />
      </button>
    </div>
  );
}

// Shown while the tutor decides. Honest about what is happening: the pause is
// someone looking at your answer, which is the point of the whole feature.
function Thinking() {
  return (
    <div className="flex items-center gap-3 py-16" style={{ color: "var(--fg-2)" }}>
      <Search className="h-4 w-4 animate-pulse" style={{ color: "var(--accent)" }} />
      <span style={{ fontSize: 15 }}>Looking at your answer…</span>
    </div>
  );
}

function Quiz({
  q, options, correctIndex, picked, onChoose, onNext, index,
}: {
  q: PlacementQuestion; options: string[]; correctIndex: number; picked: number | null; onChoose: (i: number) => void; onNext: () => void; index: number;
}) {
  const answered = picked !== null;
  const diffLabel = ["", "Easier", "Medium", "Harder"][q.difficulty] ?? "";
  return (
    <div>
      <div className="flex items-center justify-between mb-6 text-[12px]" style={{ color: "var(--fg-3)" }}>
        {/* No "x of N": the length is an OUTCOME here, and a fake denominator
            would be the one dishonest number on the screen. */}
        <span className="mono">Question {index + 1}</span>
        <span className="mono">{diffLabel}</span>
      </div>

      <div className="eyebrow mb-1">{q.topicTitle}</div>
      <p className="font-sans" style={{ fontSize: 18, lineHeight: 1.5, color: "var(--fg)" }}>
        <MathText text={q.prompt} />
      </p>

      <div className="mt-5 grid gap-2.5 sm:grid-cols-2">
        {options.map((opt, i) => {
          const isCorrect = answered && i === correctIndex;
          const isYours = answered && i === picked;
          const isWrong = isYours && i !== correctIndex;
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
              Continue <ArrowRight className="h-4 w-4" />
            </button>
          </div>
        </>
      )}
    </div>
  );
}

function Results({ result, onRetake, config }: { result: StoredPlacement; onRetake: () => void; config: PlacementConfig }) {
  const d = result.diagnosis;
  const seen = result.topicScores.filter((t) => t.seen > 0);
  const priority = result.priorityTopics
    .map((slug) => result.topicScores.find((t) => t.slug === slug))
    .filter((t): t is NonNullable<typeof t> => !!t);
  const strong = seen.filter((t) => t.accuracy >= 0.75).sort((a, b) => b.accuracy - a.accuracy);
  const pct = Math.round(result.overallAccuracy * 100);
  const verdict = config.verdict?.(result) ?? null;
  const findingTitle = (slug: string) => result.topicScores.find((t) => t.slug === slug)?.title ?? slug;

  return (
    <div>
      <div className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px] mb-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}>
        <Sparkles className="h-3.5 w-3.5" /> Your plan is ready
      </div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(28px, 5vw, 44px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
        {d?.startTitle ? (
          <>Start with <span style={{ color: "var(--accent)" }}>{d.startTitle}</span></>
        ) : (
          <>You&apos;re at the <span style={{ color: "var(--accent)" }}>{result.level}</span> level</>
        )}
      </h1>
      <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15 }}>
        {d
          ? <>We got there in <b className="tabular">{d.questionsAsked}</b> question{d.questionsAsked === 1 ? "" : "s"} — you answered <b className="tabular">{pct}%</b> of them correctly.</>
          : <>You answered <b className="tabular">{pct}%</b> correct across the {config.homeLabel} we tested.</>}
      </p>

      {d?.narrative && (
        <div className="mt-5 card-edit p-4" style={{ borderColor: "var(--accent-line)" }}>
          <div className="eyebrow mb-1.5" style={{ color: "var(--accent)" }}>What I noticed</div>
          <p className="font-sans" style={{ fontSize: 15, lineHeight: 1.6, color: "var(--fg-1)" }}>
            <MathText text={d.narrative} />
          </p>
        </div>
      )}

      {d && d.findings.length > 0 && (
        <div className="mt-6">
          <div className="eyebrow mb-3">The specific thing to fix</div>
          <div className="space-y-2">
            {d.findings.map((f) => (
              <div key={f.topicSlug} className="card-edit p-3.5">
                <p className="mono text-[11px] uppercase" style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}>{findingTitle(f.topicSlug)}</p>
                <p className="mt-1" style={{ fontSize: 14.5, lineHeight: 1.5, color: "var(--fg-1)" }}>
                  <MathText text={f.hypothesis} />
                </p>
              </div>
            ))}
          </div>
        </div>
      )}

      <p className="mt-4 text-[13px]" style={{ color: "var(--fg-3)" }}>
        On your dashboard this placement rates a skill up to 90 — real mocks
        (ЭЕШ, IB, SAT) and unit tests are what push it beyond. Retakes draw a
        fresh mix of questions.
      </p>

      {verdict && (
        <div className="mt-8 card-edit p-5" style={{ borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}>
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Your starting point</div>
          <p className="serif" style={{ fontSize: 22, color: "var(--fg)" }}>{verdict.title}</p>
          <p className="mt-1.5 text-[14px]" style={{ color: "var(--fg-1)" }}>{verdict.body}</p>
          <Link href={verdict.href} className="btn btn-primary mt-4 inline-flex items-center gap-1.5">
            {verdict.cta} <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
      )}

      {priority.length > 0 ? (
        <div className="mt-8">
          <div className="eyebrow mb-3">Start here — important for you</div>
          <div className="space-y-2.5">
            {priority.map((t, i) => (
              <Link key={t.slug} href={config.topicHref(t.slug)} className="card-edit p-4 flex items-center gap-4" style={{ textDecoration: "none" }}>
                <span className="mono text-[12px] tabular flex-shrink-0" style={{ color: "var(--accent)", minWidth: 20 }}>{i + 1}</span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 flex-wrap">
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
          Strong across the board — no single area stands out as a weak spot. Keep going and push into the harder material.
        </div>
      )}

      {strong.length > 0 && (
        <div className="mt-8">
          <div className="eyebrow mb-3">You&apos;re already solid on</div>
          <div className="flex flex-wrap gap-2">
            {strong.map((t) => (
              <Link key={t.slug} href={config.topicHref(t.slug)} className="rounded-full px-3 py-1.5 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)", textDecoration: "none" }}>
                {t.title}
              </Link>
            ))}
          </div>
        </div>
      )}

      <div className="mt-10 flex items-center gap-3">
        <Link href={d?.startSlug ? config.topicHref(d.startSlug) : config.homeHref} className="btn btn-primary inline-flex items-center gap-1.5">
          {d?.startSlug ? "Start here" : `Go to my ${config.homeLabel}`} <ArrowRight className="h-4 w-4" />
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
