"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";
import { ArrowLeft, ArrowRight, BarChart3, Check, ChevronDown, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import TestTimer from "@/components/esh/TestTimer";
import usePerformance from "@/lib/use-performance";
import { hubTopicLabel } from "@/lib/hub-analytics";
import {
  EASY_MODULE2_CAP,
  SatModuleKey,
  SatQuestion,
  getSatTest,
  gradeSatQuestion,
  module2KeyForRaw,
  satAnalyticsTopic,
  scaledScoreEstimate,
} from "@/lib/sat-test";

// Adaptive SAT Math runner: Module 1 → (routing) → Module 2 easy/hard →
// results. Session state persists in localStorage so a refresh mid-test
// resumes with the same clock (start timestamps are wall-clock). Attempts
// are recorded once, at each module submit, into the shared performance
// pipeline under context "sat" — the topic vocabulary is the
// hub-analytics domain keys, per the tagging contract.

type Phase = "intro" | "m1" | "interlude" | "m2" | "done";

interface RunState {
  phase: Phase;
  m1Answers: Record<string, string>;
  m2Answers: Record<string, string>;
  m2Key: SatModuleKey | null;
  moduleStart: number | null;
  index: number;
}

const FRESH: RunState = {
  phase: "intro",
  m1Answers: {},
  m2Answers: {},
  m2Key: null,
  moduleStart: null,
  index: 0,
};

function storageKey(testId: string) {
  return `mp-sat-run:${testId}`;
}

function loadRun(testId: string): RunState {
  try {
    const raw = localStorage.getItem(storageKey(testId));
    if (!raw) return FRESH;
    const parsed = JSON.parse(raw) as RunState;
    if (!parsed || typeof parsed !== "object" || !parsed.phase) return FRESH;
    return { ...FRESH, ...parsed };
  } catch {
    return FRESH;
  }
}

export default function SatTestRunnerPage() {
  const params = useParams();
  const testId = params.testId as string;
  const test = getSatTest(testId);
  const perf = usePerformance();

  const [mounted, setMounted] = useState(false);
  const [run, setRun] = useState<RunState>(FRESH);
  const [confirmSubmit, setConfirmSubmit] = useState(false);
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  useEffect(() => {
    setMounted(true);
    setRun(loadRun(testId));
  }, [testId]);

  const update = useCallback(
    (patch: Partial<RunState>) => {
      setRun((prev) => {
        const next = { ...prev, ...patch };
        try {
          localStorage.setItem(storageKey(testId), JSON.stringify(next));
        } catch {
          // Private-mode storage failures degrade to in-memory only.
        }
        return next;
      });
    },
    [testId],
  );

  const moduleKey: SatModuleKey | null =
    run.phase === "m1" ? "module1" : run.phase === "m2" ? run.m2Key : null;
  const questions: SatQuestion[] = useMemo(
    () => (test && moduleKey ? test[moduleKey] : []),
    [test, moduleKey],
  );
  const answers = run.phase === "m1" ? run.m1Answers : run.m2Answers;
  const answersField = run.phase === "m1" ? "m1Answers" : "m2Answers";

  const recordModule = useCallback(
    (qs: SatQuestion[], given: Record<string, string>) => {
      for (const q of qs) {
        const input = given[q.source];
        perf.recordAttempt({
          questionSource: q.source,
          topic: satAnalyticsTopic(q.domain),
          subtopic: q.skill_tag,
          selectedAnswer: input ?? "",
          correctAnswer: q.format === "mcq" ? q.answer ?? "" : (q.acceptedAnswers ?? [])[0] ?? "",
          isCorrect: gradeSatQuestion(q, input),
          source: "test",
          context: "sat",
        });
      }
    },
    [perf],
  );

  const submitModule = useCallback(() => {
    if (!test || !moduleKey) return;
    const qs = test[moduleKey];
    const given = run.phase === "m1" ? run.m1Answers : run.m2Answers;
    recordModule(qs, given);
    setConfirmSubmit(false);
    if (run.phase === "m1") {
      const raw = qs.filter((q) => gradeSatQuestion(q, given[q.source])).length;
      update({
        phase: "interlude",
        m2Key: module2KeyForRaw(raw, test.meta.module2Threshold),
        moduleStart: null,
        index: 0,
      });
    } else {
      update({ phase: "done", moduleStart: null, index: 0 });
    }
  }, [test, moduleKey, run.phase, run.m1Answers, run.m2Answers, recordModule, update]);

  if (!mounted) return <div className="min-h-screen" style={{ background: "var(--bg)" }} />;

  if (!test) {
    return (
      <Shell>
        <div className="card-edit p-8 mt-10 text-center">
          <p className="serif" style={{ fontSize: 20, color: "var(--fg)" }}>
            This practice test does not exist.
          </p>
          <Link href="/practice/sat" className="btn btn-primary mt-6 inline-flex">
            Back to the SAT hub
          </Link>
        </div>
      </Shell>
    );
  }

  const minutes = test.meta.minutesPerModule;

  // ── intro ──────────────────────────────────────────────────────────
  if (run.phase === "intro") {
    return (
      <Shell backHref="/practice/sat" eyebrow={test.meta.label}>
        <h1 className="serif mt-2" style={{ fontSize: "clamp(30px, 5vw, 44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
          Ready when you are.
        </h1>
        <div className="card-edit p-6 mt-6 space-y-3 text-[14px]" style={{ color: "var(--fg-1)" }}>
          <p>• Two modules of 22 questions, <strong>{minutes} minutes</strong> each. The clock runs per module and submits the module when it hits zero.</p>
          <p>• Module 2 adapts: your Module 1 work decides whether you get the harder or easier second module — like the real Digital SAT.</p>
          <p>• A calculator is allowed on every question (keep Desmos open in another tab, as in Bluebook).</p>
          <p>• Student-produced responses: enter up to 5 characters (6 with a minus sign). Fractions like 7/2 are fine; mixed numbers are not.</p>
          <p>• You can move freely within a module, but once you submit it there is no going back.</p>
        </div>
        <button
          className="btn btn-primary mt-6 inline-flex items-center gap-1.5"
          onClick={() => update({ phase: "m1", moduleStart: Date.now(), index: 0 })}
        >
          Start Module 1 <ArrowRight className="h-4 w-4" />
        </button>
      </Shell>
    );
  }

  // ── interlude ──────────────────────────────────────────────────────
  if (run.phase === "interlude") {
    return (
      <Shell eyebrow={test.meta.label}>
        <h1 className="serif mt-2" style={{ fontSize: "clamp(30px, 5vw, 44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
          Module 1 submitted.
        </h1>
        <p className="text-[14px] mt-4" style={{ color: "var(--fg-2)", maxWidth: "50ch" }}>
          Module 2 has been calibrated from your Module 1 work. Same rules:
          22 questions, {minutes} minutes. Take a breath, then continue.
        </p>
        <button
          className="btn btn-primary mt-6 inline-flex items-center gap-1.5"
          onClick={() => update({ phase: "m2", moduleStart: Date.now(), index: 0 })}
        >
          Start Module 2 <ArrowRight className="h-4 w-4" />
        </button>
      </Shell>
    );
  }

  // ── results ────────────────────────────────────────────────────────
  if (run.phase === "done") {
    const m2Key = run.m2Key ?? "module2Easy";
    const taken: Array<{ q: SatQuestion; input: string | undefined }> = [
      ...test.module1.map((q) => ({ q, input: run.m1Answers[q.source] })),
      ...test[m2Key].map((q) => ({ q, input: run.m2Answers[q.source] })),
    ];
    const raw = taken.filter(({ q, input }) => gradeSatQuestion(q, input)).length;
    const scaled = scaledScoreEstimate(raw);
    const tookEasy = m2Key === "module2Easy";
    const byDomain: Record<string, { correct: number; total: number }> = {};
    for (const { q, input } of taken) {
      const key = satAnalyticsTopic(q.domain);
      byDomain[key] = byDomain[key] ?? { correct: 0, total: 0 };
      byDomain[key].total++;
      if (gradeSatQuestion(q, input)) byDomain[key].correct++;
    }

    return (
      <Shell backHref="/practice/sat" eyebrow={`${test.meta.label} · Results`}>
        <h1 className="serif mt-2" style={{ fontSize: "clamp(30px, 5vw, 44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
          {raw} of 44
        </h1>
        <section className="card-edit p-5 mt-6" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
            Estimated scaled score
          </div>
          <div className="serif tabular" style={{ fontSize: 40, letterSpacing: "-0.03em", color: "var(--fg)" }}>
            ≈ {scaled} <span style={{ fontSize: 16, color: "var(--fg-2)" }}>/ 800</span>
          </div>
          <p className="text-[12px] mt-2" style={{ color: "var(--fg-2)" }}>
            An estimate from an anchor curve — real SAT equating varies by
            form.{" "}
            {tookEasy
              ? `You took the standard Module 2; reaching Module 1 raw ${test.meta.module2Threshold}+ unlocks the upper-level module, which is what scores above ~${EASY_MODULE2_CAP} require.`
              : "You unlocked the upper-level Module 2 with your Module 1 performance."}
          </p>
        </section>

        <section className="card-edit p-6 mt-5">
          <div className="eyebrow mb-4">By domain</div>
          <div className="space-y-3">
            {Object.entries(byDomain).map(([topic, s]) => {
              const acc = s.total ? Math.round((100 * s.correct) / s.total) : 0;
              return (
                <div key={topic}>
                  <div className="flex items-baseline justify-between mb-1.5 text-sm">
                    <span style={{ color: "var(--fg-1)" }}>{hubTopicLabel("sat", topic)}</span>
                    <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                      {s.correct}/{s.total} · {acc}%
                    </span>
                  </div>
                  <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                    <div
                      className="h-full rounded-full"
                      style={{
                        width: `${acc}%`,
                        background: acc >= 80 ? "var(--accent)" : acc >= 50 ? "var(--warn)" : "var(--danger)",
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        <section className="mt-6">
          <div className="eyebrow mb-3">Review every question</div>
          <div className="space-y-2">
            {taken.map(({ q, input }, i) => {
              const correct = gradeSatQuestion(q, input);
              const isOpen = !!expanded[q.source];
              const correctShown = q.format === "mcq" ? q.answer : (q.acceptedAnswers ?? []).join(" or ");
              return (
                <div key={q.source} className="card-edit overflow-hidden">
                  <button
                    className="w-full flex items-center gap-3 p-4 text-left"
                    onClick={() => setExpanded((e) => ({ ...e, [q.source]: !e[q.source] }))}
                  >
                    {correct ? (
                      <Check className="h-4 w-4 shrink-0" style={{ color: "var(--accent)" }} />
                    ) : (
                      <X className="h-4 w-4 shrink-0" style={{ color: "var(--danger)" }} />
                    )}
                    <span className="text-sm flex-1" style={{ color: "var(--fg-1)" }}>
                      {i < 22 ? "Module 1" : "Module 2"} · Q{q.questionNumber}
                      <span style={{ color: "var(--fg-3)" }}> · {hubTopicLabel("sat", satAnalyticsTopic(q.domain))}</span>
                    </span>
                    <span className="mono text-xs" style={{ color: "var(--fg-3)" }}>
                      {input ? `you: ${input}` : "blank"} · key: {correctShown}
                    </span>
                    <ChevronDown
                      className="h-4 w-4 shrink-0 transition-transform"
                      style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
                    />
                  </button>
                  {isOpen && (
                    <div className="px-4 pb-4 border-t" style={{ borderColor: "var(--line)" }}>
                      <div className="text-sm mt-3" style={{ color: "var(--fg)" }}>
                        <MathText text={q.body} />
                      </div>
                      {q.figure && (
                        <div className="mt-3 max-w-md">
                          <EshFigure
                            src={q.figure.src}
                            alt_en={q.figure.alt_en}
                            alt_mn={q.figure.alt_en}
                            width={q.figure.width}
                            height={q.figure.height}
                          />
                        </div>
                      )}
                      {q.format === "mcq" && q.options && (
                        <div className="mt-3 space-y-1.5">
                          {Object.entries(q.options).map(([letter, text]) => (
                            <div
                              key={letter}
                              className="text-sm rounded-md px-3 py-1.5"
                              style={{
                                border: "1px solid",
                                borderColor: letter === q.answer ? "var(--accent-line)" : "var(--line)",
                                background: letter === q.answer ? "var(--accent-wash)" : "transparent",
                                color: "var(--fg-1)",
                              }}
                            >
                              <span className="mono mr-2" style={{ color: "var(--fg-3)" }}>{letter}</span>
                              <MathText text={text} />
                            </div>
                          ))}
                        </div>
                      )}
                      <div className="text-sm mt-4 pt-3 border-t" style={{ borderColor: "var(--line)", color: "var(--fg-1)" }}>
                        <MathText text={q.solution} />
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>

        <div className="flex items-center gap-3 mt-8">
          <Link href="/practice/sat/progress" className="btn btn-primary inline-flex items-center gap-1.5">
            <BarChart3 className="h-4 w-4" /> View SAT progress
          </Link>
          <button
            className="btn inline-flex"
            style={{ border: "1px solid var(--line)", color: "var(--fg-1)" }}
            onClick={() => {
              localStorage.removeItem(storageKey(testId));
              setRun(FRESH);
              setExpanded({});
            }}
          >
            Retake this test
          </button>
        </div>
      </Shell>
    );
  }

  // ── active module ──────────────────────────────────────────────────
  const q = questions[run.index];
  if (!q) return null;
  const moduleLabel = run.phase === "m1" ? "Module 1" : "Module 2";
  const answered = questions.filter((qq) => (answers[qq.source] ?? "") !== "").length;
  const input = answers[q.source] ?? "";

  const setAnswer = (value: string) => {
    update({ [answersField]: { ...answers, [q.source]: value } } as Partial<RunState>);
  };

  return (
    <Shell
      eyebrow={`${test.meta.label} · ${moduleLabel}`}
      right={
        run.moduleStart ? (
          <TestTimer
            startTime={run.moduleStart}
            durationMs={minutes * 60 * 1000}
            onExpiry={submitModule}
          />
        ) : null
      }
    >
      {/* question navigator strip */}
      <div className="flex flex-wrap gap-1.5 mt-2">
        {questions.map((qq, i) => {
          const isCurrent = i === run.index;
          const has = (answers[qq.source] ?? "") !== "";
          return (
            <button
              key={qq.source}
              aria-label={`Go to question ${i + 1}`}
              onClick={() => { setConfirmSubmit(false); update({ index: i }); }}
              className="h-7 w-7 rounded-md text-[11px] mono transition-colors"
              style={{
                border: "1px solid",
                borderColor: isCurrent ? "var(--accent)" : has ? "var(--accent-line)" : "var(--line)",
                background: has ? "var(--accent-wash)" : "transparent",
                color: isCurrent ? "var(--accent)" : "var(--fg-2)",
              }}
            >
              {i + 1}
            </button>
          );
        })}
      </div>

      <div className="card-edit p-6 mt-4">
        <div className="flex items-baseline justify-between">
          <div className="eyebrow">Question {q.questionNumber} of 22</div>
          <div className="text-[11px] mono" style={{ color: "var(--fg-3)" }}>
            {q.format === "spr" ? "student-produced response" : ""}
          </div>
        </div>
        <div className="text-[15px] mt-3" style={{ color: "var(--fg)", lineHeight: 1.7 }}>
          <MathText text={q.body} />
        </div>
        {q.figure && (
          <div className="mt-4 max-w-md">
            <EshFigure
              src={q.figure.src}
              alt_en={q.figure.alt_en}
              alt_mn={q.figure.alt_en}
              width={q.figure.width}
              height={q.figure.height}
            />
          </div>
        )}

        {q.format === "mcq" && q.options ? (
          <div className="mt-5 space-y-2">
            {Object.entries(q.options).map(([letter, text]) => {
              const selected = input === letter;
              return (
                <button
                  key={letter}
                  className="w-full text-left rounded-md px-4 py-2.5 text-[14px] transition-colors"
                  style={{
                    border: "1px solid",
                    borderColor: selected ? "var(--accent)" : "var(--line)",
                    background: selected ? "var(--accent-wash)" : "transparent",
                    color: "var(--fg)",
                  }}
                  onClick={() => setAnswer(selected ? "" : letter)}
                >
                  <span className="mono mr-3" style={{ color: selected ? "var(--accent)" : "var(--fg-3)" }}>
                    {letter}
                  </span>
                  <MathText text={text} />
                </button>
              );
            })}
          </div>
        ) : (
          <div className="mt-5">
            <input
              value={input}
              onChange={(e) => setAnswer(e.target.value.replace(/[^0-9./-]/g, "").slice(0, 6))}
              placeholder="Your answer"
              inputMode="decimal"
              className="mono rounded-md px-4 py-2.5 text-[15px] w-44"
              style={{ border: "1px solid var(--line)", background: "var(--bg-2)", color: "var(--fg)" }}
            />
            <p className="text-[12px] mt-2" style={{ color: "var(--fg-3)" }}>
              Digits, decimal point, fraction slash, minus sign. Max 5
              characters (6 if negative).
            </p>
          </div>
        )}
      </div>

      <div className="flex items-center justify-between mt-4">
        <button
          className="btn inline-flex items-center gap-1.5"
          style={{ border: "1px solid var(--line)", color: "var(--fg-1)", opacity: run.index === 0 ? 0.4 : 1 }}
          disabled={run.index === 0}
          onClick={() => update({ index: run.index - 1 })}
        >
          <ArrowLeft className="h-4 w-4" /> Back
        </button>
        {run.index < questions.length - 1 ? (
          <button
            className="btn btn-primary inline-flex items-center gap-1.5"
            onClick={() => update({ index: run.index + 1 })}
          >
            Next <ArrowRight className="h-4 w-4" />
          </button>
        ) : confirmSubmit ? (
          <div className="flex items-center gap-3">
            <span className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              {answered < questions.length
                ? `${questions.length - answered} unanswered — submit anyway?`
                : "Submit this module?"}
            </span>
            <button className="btn btn-primary" onClick={submitModule}>
              Submit {moduleLabel}
            </button>
          </div>
        ) : (
          <button className="btn btn-primary" onClick={() => setConfirmSubmit(true)}>
            Finish {moduleLabel}
          </button>
        )}
      </div>
    </Shell>
  );
}

function Shell({
  children,
  eyebrow,
  backHref,
  right,
}: {
  children: React.ReactNode;
  eyebrow?: string;
  backHref?: string;
  right?: React.ReactNode;
}) {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-16">
        {(eyebrow || backHref || right) && (
          <div className="flex items-center gap-3">
            {backHref && (
              <Link
                href={backHref}
                className="p-2 rounded-md transition-colors"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
              >
                <ArrowLeft className="w-4 h-4" />
              </Link>
            )}
            {eyebrow && <div className="eyebrow flex-1">{eyebrow}</div>}
            {right}
          </div>
        )}
        {children}
      </div>
    </div>
  );
}
