"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";
import { ArrowLeft, ArrowRight, BarChart3, Check, ChevronDown } from "lucide-react";
import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import TestTimer from "@/components/esh/TestTimer";
import usePerformance from "@/lib/use-performance";
import {
  IB_TOPIC_LABELS,
  IbPaper,
  IbPart,
  IbQuestion,
  clampEarned,
  getIbPaper,
  ibAnalyticsTopic,
  ibGradeEstimate,
  ibPartKey,
  tallyByTopic,
  tallyPaper,
} from "@/lib/ib-test";

// IB paper runner: work the paper against the clock, then self-mark each
// part against the real markscheme (M/A/R marks), then results with an
// indicative grade band. Session state persists in localStorage so a
// refresh resumes with the same clock. Attempts are recorded once, when
// marking is finished, into the shared performance pipeline under
// context "ib" — topic is the component key (aa-paper-1 / aa-paper-2)
// per the hub-analytics tagging contract.

type Phase = "intro" | "work" | "mark" | "done";

interface RunState {
  phase: Phase;
  index: number; // question index within the current phase
  answers: Record<string, string>; // partKey -> student's written answer
  earned: Record<string, number>; // partKey -> self-awarded marks
  workStart: number | null;
  recorded: boolean;
}

const FRESH: RunState = {
  phase: "intro",
  index: 0,
  answers: {},
  earned: {},
  workStart: null,
  recorded: false,
};

function storageKey(testId: string, paper: number) {
  return `mp-ib-run:${testId}:p${paper}`;
}

function loadRun(testId: string, paper: number): RunState {
  try {
    const raw = localStorage.getItem(storageKey(testId, paper));
    if (!raw) return FRESH;
    const parsed = JSON.parse(raw) as RunState;
    if (!parsed || typeof parsed !== "object" || !parsed.phase) return FRESH;
    return { ...FRESH, ...parsed };
  } catch {
    return FRESH;
  }
}

export default function IbPaperRunnerPage() {
  const params = useParams();
  const testId = params.testId as string;
  const paperNum = parseInt(params.paper as string, 10);
  const paper: IbPaper | undefined = getIbPaper(testId, paperNum);
  const perf = usePerformance();

  const [mounted, setMounted] = useState(false);
  const [run, setRun] = useState<RunState>(FRESH);
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  useEffect(() => {
    setMounted(true);
    setRun(loadRun(testId, paperNum));
  }, [testId, paperNum]);

  const update = useCallback(
    (patch: Partial<RunState>) => {
      setRun((prev) => {
        const next = { ...prev, ...patch };
        try {
          localStorage.setItem(storageKey(testId, paperNum), JSON.stringify(next));
        } catch {
          // Private-mode storage failures degrade to in-memory only.
        }
        return next;
      });
    },
    [testId, paperNum],
  );

  const finishMarking = useCallback(() => {
    if (!paper) return;
    if (!run.recorded) {
      for (const q of paper.questions) {
        for (const p of q.parts) {
          const key = ibPartKey(q, p);
          const got = clampEarned(run.earned[key] ?? 0, p.marks);
          perf.recordAttempt({
            questionSource: key,
            topic: ibAnalyticsTopic(paper.meta),
            subtopic: q.topic,
            selectedAnswer: `${got}/${p.marks}`,
            correctAnswer: `${p.marks}/${p.marks}`,
            isCorrect: got === p.marks,
            source: "test",
            context: "ib",
          });
        }
      }
    }
    update({ phase: "done", index: 0, recorded: true });
  }, [paper, perf, run.earned, run.recorded, update]);

  const questions: IbQuestion[] = useMemo(() => paper?.questions ?? [], [paper]);

  if (!mounted) return <div className="min-h-screen" style={{ background: "var(--bg)" }} />;

  if (!paper) {
    return (
      <Shell>
        <div className="card-edit p-8 mt-10 text-center">
          <p className="serif" style={{ fontSize: 20, color: "var(--fg)" }}>
            This practice paper does not exist.
          </p>
          <Link href="/practice/ib" className="btn btn-primary mt-6 inline-flex">
            Back to the IB hub
          </Link>
        </div>
      </Shell>
    );
  }

  const meta = paper.meta;
  const sectionA = questions.filter((q) => q.section === "A");
  const sectionB = questions.filter((q) => q.section === "B");

  // ── intro ──────────────────────────────────────────────────────────
  if (run.phase === "intro") {
    return (
      <Shell backHref="/practice/ib" eyebrow={meta.label}>
        <h1 className="serif mt-2" style={{ fontSize: "clamp(30px, 5vw, 44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
          {meta.calculator ? "GDC at the ready." : "Pens down to exact values."}
        </h1>
        <div className="card-edit p-6 mt-6 space-y-3 text-[14px]" style={{ color: "var(--fg-1)" }}>
          <p>
            • <strong>{meta.timeMinutes} minutes</strong>, {meta.totalMarks} marks.
            Section A: {sectionA.length} short questions ({sectionA.reduce((s, q) => s + q.maximumMark, 0)} marks).
            Section B: {sectionB.length} long questions ({sectionB.reduce((s, q) => s + q.maximumMark, 0)} marks).
          </p>
          <p>
            • {meta.calculator
              ? "A graphic display calculator is REQUIRED. Unless the answer is exact, give final answers to 3 significant figures."
              : "NO calculator. Every answer can and must be written exactly — fractions, surds, multiples of π."}
          </p>
          <p>
            • Work each part on paper exactly as in the exam. You can note your
            answers here as you go; when the clock stops you will mark your own
            work against the full IB-style markscheme (M/A/R marks).
          </p>
          <p>
            • Marks: full working earns method (M) marks even when the final
            answer slips — award yourself honestly, the way an examiner would.
          </p>
        </div>
        <button
          className="btn btn-primary mt-6 inline-flex items-center gap-1.5"
          onClick={() => update({ phase: "work", workStart: Date.now(), index: 0 })}
        >
          Start the paper <ArrowRight className="h-4 w-4" />
        </button>
      </Shell>
    );
  }

  // ── results ────────────────────────────────────────────────────────
  if (run.phase === "done") {
    const { earned, total } = tallyPaper(paper, run.earned);
    const pct = total ? (100 * earned) / total : 0;
    const grade = ibGradeEstimate(pct);
    const byTopic = tallyByTopic(paper, run.earned);

    return (
      <Shell backHref="/practice/ib" eyebrow={`${meta.label} · Results`}>
        <h1 className="serif mt-2" style={{ fontSize: "clamp(30px, 5vw, 44px)", letterSpacing: "-0.03em", color: "var(--fg)" }}>
          {earned} of {total} marks
        </h1>
        <section className="card-edit p-5 mt-6" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
            Indicative grade
          </div>
          <div className="serif tabular" style={{ fontSize: 40, letterSpacing: "-0.03em", color: "var(--fg)" }}>
            {grade} <span style={{ fontSize: 16, color: "var(--fg-2)" }}>/ 7 · {Math.round(pct)}%</span>
          </div>
          <p className="text-[12px] mt-2" style={{ color: "var(--fg-2)" }}>
            Estimated from typical AA {meta.level.toUpperCase()} boundaries on
            this single paper — real IB grades combine both papers and
            boundaries move each session.
          </p>
        </section>

        <section className="card-edit p-6 mt-5">
          <div className="eyebrow mb-4">By syllabus topic</div>
          <div className="space-y-3">
            {Object.entries(byTopic).map(([topic, s]) => {
              const acc = s.total ? Math.round((100 * s.earned) / s.total) : 0;
              return (
                <div key={topic}>
                  <div className="flex items-baseline justify-between mb-1.5 text-sm">
                    <span style={{ color: "var(--fg-1)" }}>
                      {IB_TOPIC_LABELS[topic as keyof typeof IB_TOPIC_LABELS] ?? topic}
                    </span>
                    <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                      {s.earned}/{s.total} · {acc}%
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
            {questions.map((q) => {
              const qEarned = q.parts.reduce(
                (s, p) => s + clampEarned(run.earned[ibPartKey(q, p)] ?? 0, p.marks),
                0,
              );
              const isOpen = !!expanded[q.source];
              return (
                <div key={q.source} className="card-edit overflow-hidden">
                  <button
                    className="w-full flex items-center gap-3 p-4 text-left"
                    onClick={() => setExpanded((e) => ({ ...e, [q.source]: !e[q.source] }))}
                  >
                    <span className="text-sm flex-1" style={{ color: "var(--fg-1)" }}>
                      Q{q.number} · Section {q.section}
                      <span style={{ color: "var(--fg-3)" }}> · {IB_TOPIC_LABELS[q.topic]}</span>
                    </span>
                    <span className="mono text-xs tabular" style={{ color: qEarned === q.maximumMark ? "var(--accent)" : "var(--fg-3)" }}>
                      {qEarned}/{q.maximumMark}
                    </span>
                    <ChevronDown
                      className="h-4 w-4 shrink-0 transition-transform"
                      style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
                    />
                  </button>
                  {isOpen && (
                    <div className="px-4 pb-4 border-t" style={{ borderColor: "var(--line)" }}>
                      <QuestionBody q={q} />
                      {q.parts.map((p) => (
                        <PartMarking
                          key={p.label}
                          q={q}
                          p={p}
                          earned={clampEarned(run.earned[ibPartKey(q, p)] ?? 0, p.marks)}
                          studentAnswer={run.answers[ibPartKey(q, p)]}
                          readOnly
                        />
                      ))}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>

        <div className="flex items-center gap-3 mt-8">
          <Link href="/practice/ib/progress" className="btn btn-primary inline-flex items-center gap-1.5">
            <BarChart3 className="h-4 w-4" /> View IB progress
          </Link>
          <button
            className="btn inline-flex"
            style={{ border: "1px solid var(--line)", color: "var(--fg-1)" }}
            onClick={() => {
              localStorage.removeItem(storageKey(testId, paperNum));
              setRun(FRESH);
              setExpanded({});
            }}
          >
            Retake this paper
          </button>
        </div>
      </Shell>
    );
  }

  // ── work + mark phases share the question frame ────────────────────
  const q = questions[run.index];
  if (!q) return null;
  const isMarking = run.phase === "mark";

  return (
    <Shell
      eyebrow={`${meta.label} · ${isMarking ? "Self-marking" : `Section ${q.section}`}`}
      right={
        !isMarking && run.workStart ? (
          <TestTimer
            startTime={run.workStart}
            durationMs={meta.timeMinutes * 60 * 1000}
            onExpiry={() => update({ phase: "mark", index: 0 })}
          />
        ) : null
      }
    >
      {/* question navigator strip */}
      <div className="flex flex-wrap gap-1.5 mt-2">
        {questions.map((qq, i) => {
          const isCurrent = i === run.index;
          const touched = qq.parts.some((p) =>
            isMarking
              ? run.earned[ibPartKey(qq, p)] !== undefined
              : (run.answers[ibPartKey(qq, p)] ?? "") !== "",
          );
          return (
            <button
              key={qq.source}
              aria-label={`Go to question ${qq.number}`}
              onClick={() => update({ index: i })}
              className="h-7 w-7 rounded-md text-[11px] mono transition-colors"
              style={{
                border: "1px solid",
                borderColor: isCurrent ? "var(--accent)" : touched ? "var(--accent-line)" : "var(--line)",
                background: touched ? "var(--accent-wash)" : "transparent",
                color: isCurrent ? "var(--accent)" : "var(--fg-2)",
              }}
            >
              {qq.number}
            </button>
          );
        })}
      </div>

      <div className="card-edit p-6 mt-4">
        <div className="flex items-baseline justify-between">
          <div className="eyebrow">
            Question {q.number} · Section {q.section}
          </div>
          <div className="text-[11px] mono" style={{ color: "var(--fg-3)" }}>
            [Maximum mark: {q.maximumMark}]
          </div>
        </div>
        <QuestionBody q={q} />

        {q.parts.map((p) => {
          const key = ibPartKey(q, p);
          return isMarking ? (
            <PartMarking
              key={p.label}
              q={q}
              p={p}
              earned={run.earned[key] ?? undefined}
              studentAnswer={run.answers[key]}
              onAward={(m) => update({ earned: { ...run.earned, [key]: m } })}
            />
          ) : (
            <div key={p.label} className="mt-5">
              <div className="flex items-baseline gap-2">
                <span className="mono text-[12px]" style={{ color: "var(--accent)" }}>
                  ({p.label})
                </span>
                <div className="text-[15px] flex-1" style={{ color: "var(--fg)", lineHeight: 1.7 }}>
                  <MathText text={p.body} />
                </div>
                <span className="mono text-[11px] shrink-0" style={{ color: "var(--fg-3)" }}>
                  [{p.marks}]
                </span>
              </div>
              <input
                value={run.answers[key] ?? ""}
                onChange={(e) => update({ answers: { ...run.answers, [key]: e.target.value } })}
                placeholder="Your final answer (work on paper)"
                className="mono rounded-md px-3 py-2 text-[13px] w-full max-w-md mt-2"
                style={{ border: "1px solid var(--line)", background: "var(--bg-2)", color: "var(--fg)" }}
              />
            </div>
          );
        })}
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
        ) : isMarking ? (
          <button className="btn btn-primary inline-flex items-center gap-1.5" onClick={finishMarking}>
            <Check className="h-4 w-4" /> Finish marking
          </button>
        ) : (
          <button
            className="btn btn-primary"
            onClick={() => update({ phase: "mark", index: 0 })}
          >
            Finish &amp; mark my work
          </button>
        )}
      </div>
    </Shell>
  );
}

function QuestionBody({ q }: { q: IbQuestion }) {
  return (
    <>
      {q.contextIntro && (
        <div className="text-[15px] mt-3" style={{ color: "var(--fg)", lineHeight: 1.7 }}>
          <MathText text={q.contextIntro} />
        </div>
      )}
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
    </>
  );
}

// One part in the marking/review phase: statement, the student's noted
// answer, the official answer + markscheme table + solution, and (unless
// readOnly) the 0..N mark picker.
function PartMarking({
  q,
  p,
  earned,
  studentAnswer,
  onAward,
  readOnly,
}: {
  q: IbQuestion;
  p: IbPart;
  earned: number | undefined;
  studentAnswer: string | undefined;
  onAward?: (marks: number) => void;
  readOnly?: boolean;
}) {
  return (
    <div className="mt-5 pt-4 border-t" style={{ borderColor: "var(--line)" }}>
      <div className="flex items-baseline gap-2">
        <span className="mono text-[12px]" style={{ color: "var(--accent)" }}>
          ({p.label})
        </span>
        <div className="text-[14px] flex-1" style={{ color: "var(--fg-1)", lineHeight: 1.7 }}>
          <MathText text={p.body} />
        </div>
        <span className="mono text-[11px] shrink-0" style={{ color: "var(--fg-3)" }}>
          [{p.marks}]
        </span>
      </div>

      {studentAnswer ? (
        <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
          Your noted answer: <span className="mono">{studentAnswer}</span>
        </p>
      ) : null}

      <div className="rounded-md px-3 py-2 mt-2 text-[14px]" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg)" }}>
        <MathText text={p.answer} />
      </div>

      <div className="mt-3 space-y-1">
        {p.markscheme.map((m, i) => (
          <div key={i} className="flex items-start gap-2 text-[13px]">
            <span
              className="mono shrink-0 rounded px-1.5 py-0.5 text-[11px] mt-0.5"
              style={{ border: "1px solid var(--line)", color: "var(--accent)" }}
            >
              {m.mark}
            </span>
            <span style={{ color: "var(--fg-1)" }}>
              <MathText text={m.note} />
            </span>
          </div>
        ))}
      </div>

      <details className="mt-2">
        <summary className="text-[12px] cursor-pointer" style={{ color: "var(--fg-3)" }}>
          Full worked solution
        </summary>
        <div className="text-[14px] mt-2" style={{ color: "var(--fg-1)", lineHeight: 1.7 }}>
          <MathText text={p.solution} />
        </div>
      </details>

      <div className="flex items-center gap-1.5 mt-3">
        <span className="text-[12px] mr-1" style={{ color: "var(--fg-3)" }}>
          {readOnly ? "Awarded:" : "Marks earned:"}
        </span>
        {Array.from({ length: p.marks + 1 }, (_, m) => {
          const selected = earned === m;
          return readOnly ? (
            selected ? (
              <span
                key={m}
                className="mono h-7 w-7 rounded-md text-[12px] inline-flex items-center justify-center"
                style={{ border: "1px solid var(--accent)", color: "var(--accent)", background: "var(--accent-wash)" }}
              >
                {m}
              </span>
            ) : null
          ) : (
            <button
              key={m}
              className="mono h-7 w-7 rounded-md text-[12px] transition-colors"
              style={{
                border: "1px solid",
                borderColor: selected ? "var(--accent)" : "var(--line)",
                background: selected ? "var(--accent-wash)" : "transparent",
                color: selected ? "var(--accent)" : "var(--fg-2)",
              }}
              onClick={() => onAward?.(m)}
            >
              {m}
            </button>
          );
        })}
      </div>
    </div>
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
