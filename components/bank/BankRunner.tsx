"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, X, RotateCcw, Repeat2, Layers, Target } from "lucide-react";
import MathText from "@/components/esh/MathText";
import GeoDiagram from "@/components/genmath/interactive/GeoDiagram";
import { useAuth } from "@/lib/auth-context";
import {
  type BankTopic,
  type BankSession,
  type BankLevel,
  type BankSummary,
  LEVEL_LABELS,
  initSession,
  currentItem,
  answerCurrent,
  isDone,
  summarize,
  displayVariant,
  getForm,
  getVariant,
  sessionForms,
  saveBankSession,
} from "@/lib/problem-bank";

type Phase = "setup" | "quiz" | "done";

// The bank runner: pick a level → sweep one problem per exam form → any miss
// immediately queues a SIMILAR problem (sibling variant of the same form) →
// summary names the forms that still need work and can re-drill just those.
export default function BankRunner({ topic }: { topic: BankTopic }) {
  const { user } = useAuth();
  const [phase, setPhase] = useState<Phase>("setup");
  const [level, setLevel] = useState<BankLevel>(0);
  const [session, setSession] = useState<BankSession | null>(null);
  const [picked, setPicked] = useState<number | null>(null);
  const [summary, setSummary] = useState<BankSummary | null>(null);
  const [seed, setSeed] = useState(0); // re-shuffle key per question

  const item = session ? currentItem(session) : null;
  const form = item ? getForm(topic, item.formId) : null;
  const variantData = item ? getVariant(topic, item.formId, item.variantId) : null;
  const disp = useMemo(
    () => (variantData ? displayVariant(variantData) : null),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [variantData?.id, seed],
  );

  function start(lv: BankLevel, formIds?: string[]) {
    const s = initSession(topic, lv, Math.random, formIds);
    setLevel(lv);
    setSession(s);
    setPicked(null);
    setSummary(null);
    setSeed((n) => n + 1);
    setPhase("quiz");
  }

  function choose(i: number) {
    if (picked !== null) return;
    setPicked(i);
  }

  function next() {
    if (!session || picked === null || !disp) return;
    const correct = picked === disp.correctIndex;
    const advanced = answerCurrent(topic, session, correct);
    setPicked(null);
    setSeed((n) => n + 1);
    if (isDone(advanced)) {
      const sum = summarize(topic, advanced);
      saveBankSession(topic, sum, user?.id);
      setSummary(sum);
      setSession(advanced);
      setPhase("done");
    } else {
      setSession(advanced);
    }
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math/problem-bank" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Problem Bank · {topic.title}</div>
        </div>

        {phase === "setup" && <Setup topic={topic} onStart={start} />}

        {phase === "quiz" && session && item && form && variantData && disp && (
          <div>
            <div className="flex items-center justify-between mb-2 text-[12px]" style={{ color: "var(--fg-3)" }}>
              <span className="mono">
                Problem {session.pos + 1} / {session.queue.length}
              </span>
              <span className="mono">{LEVEL_LABELS[form.level]}</span>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full mb-6" style={{ background: "var(--bg-2)" }}>
              <div className="h-full rounded-full" style={{ width: `${(session.pos / session.queue.length) * 100}%`, background: "var(--accent)", transition: "width 0.4s cubic-bezier(0.22,1,0.36,1)" }} />
            </div>

            <div className="flex items-center gap-2 flex-wrap mb-2">
              <span className="eyebrow">{form.title}</span>
              {item.isRetry && (
                <span className="inline-flex items-center gap-1 rounded-full px-2.5 py-0.5 text-[11px] font-medium" style={{ background: "rgba(216,150,32,0.12)", border: "1px solid rgba(216,150,32,0.4)", color: "var(--warn, #d89620)" }}>
                  <Repeat2 className="h-3 w-3" /> Similar problem — try again
                </span>
              )}
            </div>

            <p className="font-sans" style={{ fontSize: 18, lineHeight: 1.5, color: "var(--fg)" }}>
              <MathText text={variantData.statement} />
            </p>

            {variantData.geoFigure && (
              <div className="mt-4">
                <GeoDiagram spec={variantData.geoFigure} />
              </div>
            )}

            <div className="mt-5 grid gap-2.5 sm:grid-cols-2">
              {disp.options.map((opt, i) => {
                const answered = picked !== null;
                const isCorrect = answered && i === disp.correctIndex;
                const isWrong = answered && i === picked && i !== disp.correctIndex;
                let bg = "var(--bg-2)", border = "var(--line)", color = "var(--fg)";
                if (isCorrect) { bg = "rgba(63,178,127,0.14)"; border = "#3fb27f"; }
                else if (isWrong) { bg = "rgba(215,80,63,0.10)"; border = "rgba(215,80,63,0.5)"; color = "var(--fg-2)"; }
                return (
                  <button
                    key={i}
                    type="button"
                    onClick={() => choose(i)}
                    disabled={answered}
                    className="gm-press flex items-center justify-between gap-2 rounded-xl px-4 py-3 text-left"
                    style={{ background: bg, border: `1.5px solid ${border}`, color, opacity: answered && !isCorrect && i !== picked ? 0.5 : 1 }}
                  >
                    <span className="q-math" style={{ fontSize: 15 }}><MathText text={opt} /></span>
                    {isCorrect && <span className="grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "#3fb27f", color: "#fff" }}><Check className="h-4 w-4" /></span>}
                    {isWrong && <span className="grid h-6 w-6 flex-shrink-0 place-items-center rounded-full" style={{ background: "rgba(215,80,63,0.85)", color: "#fff" }}><X className="h-4 w-4" /></span>}
                  </button>
                );
              })}
            </div>

            {picked !== null && (
              <>
                <div className="mt-4 rounded-xl p-3" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
                  <p className="font-sans" style={{ fontSize: 14, lineHeight: 1.55, color: "var(--fg-1)" }}>
                    <MathText text={variantData.explanation} />
                  </p>
                </div>
                <div className="mt-5 flex items-center justify-between gap-3">
                  <span className="text-[13px]" style={{ color: "var(--fg-3)" }}>
                    {picked !== disp.correctIndex ? "A similar problem is queued next — same form, new numbers." : ""}
                  </span>
                  <button type="button" onClick={next} className="btn btn-primary inline-flex items-center gap-1.5 flex-shrink-0">
                    {session.pos + 1 >= session.queue.length
                      ? "See my results"
                      : picked !== disp.correctIndex
                        ? "Try a similar one"
                        : "Next problem"}
                    <ArrowRight className="h-4 w-4" />
                  </button>
                </div>
              </>
            )}
          </div>
        )}

        {phase === "done" && summary && (
          <Summary topic={topic} summary={summary} level={level} onRetake={() => start(level)} onDrill={(ids) => start(0, ids)} />
        )}
      </div>
    </div>
  );
}

function Setup({ topic, onStart }: { topic: BankTopic; onStart: (lv: BankLevel) => void }) {
  const counts = [1, 2, 3].map((lv) => sessionForms(topic, lv as BankLevel).length);
  const total = topic.forms.length;
  const problems = topic.forms.reduce((n, f) => n + f.variants.length, 0);
  return (
    <div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
        {topic.title}
      </h1>
      <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 16, lineHeight: 1.6 }}>
        {topic.blurb}
      </p>
      <ul className="mt-5 space-y-2" style={{ color: "var(--fg-2)", fontSize: 14 }}>
        <li className="flex items-start gap-2">
          <Layers className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <span><b>{total} exam forms</b>, {problems} problems — every shape this topic takes on a test, labeled Level 1–3.</span>
        </li>
        <li className="flex items-start gap-2">
          <Repeat2 className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <span>Miss one and a <b>similar problem</b> (same form, new numbers) comes right back — you fix the mistake while it's fresh.</span>
        </li>
        <li className="flex items-start gap-2">
          <Target className="mt-0.5 h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <span>The summary names the forms that still need work, and you can re-drill <b>just those</b>.</span>
        </li>
      </ul>

      <div className="eyebrow mt-8 mb-3">Choose your level</div>
      <div className="grid gap-2.5 sm:grid-cols-2">
        <button type="button" onClick={() => onStart(0)} className="card-edit gm-press p-4 text-left">
          <div className="serif" style={{ fontSize: 17, color: "var(--fg)" }}>All levels</div>
          <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>The full sweep — {total} forms, easiest first.</div>
        </button>
        {[1, 2, 3].map((lv) => (
          <button key={lv} type="button" onClick={() => onStart(lv as BankLevel)} className="card-edit gm-press p-4 text-left">
            <div className="serif" style={{ fontSize: 17, color: "var(--fg)" }}>{LEVEL_LABELS[lv]}</div>
            <div className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{counts[lv - 1]} forms at this level.</div>
          </button>
        ))}
      </div>
    </div>
  );
}

function Summary({
  topic, summary, level, onRetake, onDrill,
}: {
  topic: BankTopic; summary: BankSummary; level: BankLevel; onRetake: () => void; onDrill: (formIds: string[]) => void;
}) {
  const pct = Math.round(summary.accuracy * 100);
  const recovered = summary.forms.filter((f) => f.recovered);
  const clean = summary.forms.filter((f) => f.firstTryCorrect);
  return (
    <div>
      <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(28px, 5vw, 44px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
        <span style={{ color: "var(--accent)" }}>{pct}%</span> across {summary.total} problems
      </h1>
      <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15 }}>
        {clean.length} of {summary.forms.length} forms first try
        {recovered.length > 0 && <> · <b>{recovered.length} recovered</b> on the similar problem</>}
        {summary.needsWork.length > 0 && <> · {summary.needsWork.length} still need work</>}.
      </p>

      {summary.perLevel.length > 1 && (
        <div className="mt-6 grid gap-2.5 sm:grid-cols-3">
          {summary.perLevel.map((l) => (
            <div key={l.level} className="rounded-xl p-3" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
              <div className="text-[12px] mono" style={{ color: "var(--fg-3)" }}>{LEVEL_LABELS[l.level]}</div>
              <div className="serif tabular mt-1" style={{ fontSize: 20, color: "var(--fg)" }}>
                {l.correct}/{l.total}
              </div>
            </div>
          ))}
        </div>
      )}

      {summary.needsWork.length > 0 ? (
        <div className="mt-8">
          <div className="eyebrow mb-3">Work on these forms</div>
          <div className="space-y-2.5">
            {summary.needsWork.map((f) => (
              <div key={f.formId} className="card-edit p-4">
                <div className="flex items-center gap-2 flex-wrap">
                  <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>{f.title}</p>
                  <span className="mono text-[10px] uppercase rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-3)" }}>
                    {LEVEL_LABELS[f.level]}
                  </span>
                </div>
                <p className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{f.skill}</p>
              </div>
            ))}
          </div>
          <button
            type="button"
            onClick={() => onDrill(summary.needsWork.map((f) => f.formId))}
            className="btn btn-primary mt-4 inline-flex items-center gap-1.5"
          >
            <Repeat2 className="h-4 w-4" /> Practice these {summary.needsWork.length} forms again
          </button>
        </div>
      ) : (
        <div className="mt-8 rounded-xl p-4" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--fg-1)" }}>
          Every form ended on a correct answer — this set is mastered. Step up a level, or take on another topic.
        </div>
      )}

      {recovered.length > 0 && (
        <div className="mt-8">
          <div className="eyebrow mb-3">Recovered with a similar problem</div>
          <div className="flex flex-wrap gap-2">
            {recovered.map((f) => (
              <span key={f.formId} className="rounded-full px-3 py-1.5 text-[13px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
                {f.title} ✓
              </span>
            ))}
          </div>
        </div>
      )}

      <div className="mt-10 flex items-center gap-3 flex-wrap">
        <button type="button" onClick={onRetake} className="btn btn-line inline-flex items-center gap-1.5">
          <RotateCcw className="h-4 w-4" /> New set{level !== 0 ? ` · ${LEVEL_LABELS[level]}` : ""}
        </button>
        <Link href="/math/problem-bank" className="btn btn-line inline-flex items-center gap-1.5" style={{ textDecoration: "none" }}>
          All topics <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </div>
  );
}
