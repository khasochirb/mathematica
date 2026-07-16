"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, BookOpen, Check, Eye, EyeOff, RefreshCw, X, Zap } from "lucide-react";
import MathText from "@/components/esh/MathText";
import GeoDiagram from "@/components/genmath/interactive/GeoDiagram";
import { useAuth } from "@/lib/auth-context";
import {
  type BankTopic,
  type BankUnit,
  type BankForm,
  type BankLevel,
  LEVEL_LABELS,
  recordSelfGrade,
  unitForms,
} from "@/lib/problem-bank";

// The unit's exercise set, textbook style: a numbered list that INTERLEAVES
// the unit's problem types (round-robin), so consecutive problems are
// different kinds — recognizing which move applies is part of the exercise.
// Sibling variants power the per-problem "new numbers" reroll instead of
// being dumped on the page, and the same siblings feed the practice runner's
// miss→similar loop. Rows are compact (number · statement · actions) like a
// printed problem set; the solution expands inline with self-grading that
// feeds per-form mastery.
export default function BankBrowser({ topic, unit }: { topic: BankTopic; unit: BankUnit }) {
  const { user } = useAuth();
  const [level, setLevel] = useState<BankLevel>(0);

  const allForms = unitForms(topic, unit.id);
  const total = allForms.reduce((n, f) => n + f.variants.length, 0);
  const forms = useMemo(
    () =>
      allForms
        .filter((f) => level === 0 || f.level === level)
        .sort((a, b) => a.level - b.level),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [topic, unit.id, level],
  );
  const unitIndex = topic.units.findIndex((u) => u.id === unit.id);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href={`/math/problem-bank/${topic.slug}`} className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">
            Problem Bank · {topic.title} · Unit {unitIndex + 1}
          </div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
          {unit.title}
        </h1>
        <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15.5, maxWidth: "58ch" }}>
          A mixed exercise set, like a textbook: every problem type this unit
          covers, shuffled together and getting harder as you go. Work on
          paper, reveal to check — and hit <RefreshCw className="inline h-3.5 w-3.5 -mt-0.5" /> on
          any problem for the same kind with new numbers ({total} in the pool).
        </p>

        <div className="mt-5 flex items-center gap-2 flex-wrap">
          {([0, 1, 2, 3] as const).map((lv) => (
            <button
              key={lv}
              type="button"
              onClick={() => setLevel(lv)}
              className="gm-press rounded-full px-3.5 py-1.5 text-[13px]"
              style={
                level === lv
                  ? { background: "var(--accent)", border: "1px solid var(--accent)", color: "var(--accent-ink, #fff)" }
                  : { background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }
              }
            >
              {lv === 0 ? "All levels" : LEVEL_LABELS[lv]}
            </button>
          ))}
        </div>

        <div className="mt-5 grid gap-2 sm:grid-cols-2">
          <Link
            href={`/math/problem-bank/${topic.slug}/${unit.id}/practice`}
            className="card-edit px-4 py-3 flex items-center gap-2.5 transition-colors"
            style={{ textDecoration: "none" }}
          >
            <Zap className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
            <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
              <b>Practice set</b> — quiz with instant feedback and retries.
            </span>
            <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
          </Link>
          <Link
            href={`/math/${topic.slug}/${unit.id}`}
            className="card-edit px-4 py-3 flex items-center gap-2.5 transition-colors"
            style={{ textDecoration: "none" }}
          >
            <BookOpen className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
            <span className="flex-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
              <b>Review the lessons</b> for this unit first.
            </span>
            <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
          </Link>
        </div>

        <ExerciseSet key={level} topic={topic} forms={forms} userId={user?.id} />
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// The interleaved, numbered exercise list
// ---------------------------------------------------------------------------

type Slot = { form: BankForm; round: number };

// Deterministic (SSR-safe) but well-spread pick: stride through the variant
// pool with a step co-prime to its size, so consecutive rounds of the same
// form land in different parameter neighborhoods instead of v01, v02, v03…
function spreadIndex(round: number, n: number): number {
  const stride = n % 13 === 0 ? (n % 11 === 0 ? 7 : 11) : 13;
  return (round * stride) % n;
}

function buildSlots(forms: BankForm[], rounds: number): Slot[] {
  // Round-robin across forms (within the level-sorted order), so problem
  // n+1 is a different kind than problem n. Each round serves a spread-out
  // variant as the starting point (reroll can move it later).
  const slots: Slot[] = [];
  for (let r = 0; r < rounds; r++) {
    for (const form of forms) {
      if (r < form.variants.length) slots.push({ form, round: r });
    }
  }
  return slots;
}

function ExerciseSet({ topic, forms, userId }: { topic: BankTopic; forms: BankForm[]; userId?: string | null }) {
  const maxRounds = forms.reduce((m, f) => Math.max(m, f.variants.length), 0);
  // Start with enough rounds to feel like a real set (~2 passes over the
  // types, at least 12 problems), never more than exists.
  const initialRounds = Math.min(
    maxRounds,
    Math.max(2, Math.ceil(12 / Math.max(forms.length, 1))),
  );
  const [rounds, setRounds] = useState(initialRounds);

  const slots = buildSlots(forms, Math.min(rounds, maxRounds));
  const totalSlots = buildSlots(forms, maxRounds).length;
  const remaining = totalSlots - slots.length;

  if (forms.length === 0) return null;

  return (
    <div className="mt-8">
      <div className="flex items-baseline justify-between gap-3 mb-1">
        <div className="eyebrow">Exercises</div>
        <span className="mono text-[11px] tabular" style={{ color: "var(--fg-3)" }}>
          {slots.length} of {totalSlots} shown
        </span>
      </div>
      <div style={{ borderTop: "1px solid var(--line)" }}>
        {slots.map((s, i) => (
          <ExerciseRow
            key={`${s.form.id}:${s.round}`}
            topic={topic}
            form={s.form}
            initialIndex={spreadIndex(s.round, s.form.variants.length)}
            number={i + 1}
            userId={userId}
          />
        ))}
      </div>
      {remaining > 0 && (
        <div className="mt-4 flex items-center gap-3">
          <button
            type="button"
            onClick={() => setRounds((r) => r + 1)}
            className="btn btn-line text-[13px]"
          >
            More problems (+{Math.min(forms.length, remaining)})
          </button>
          <button
            type="button"
            onClick={() => setRounds(maxRounds)}
            className="text-[13px]"
            style={{ color: "var(--fg-2)", textDecoration: "underline", textUnderlineOffset: 3 }}
          >
            Show all {totalSlots}
          </button>
        </div>
      )}
    </div>
  );
}

// One numbered exercise: compact row, solution expands inline, and the
// reroll swaps in a sibling variant (same type, new numbers).
function ExerciseRow({
  topic, form, initialIndex, number, userId,
}: {
  topic: BankTopic; form: BankForm; initialIndex: number; number: number; userId?: string | null;
}) {
  const [idx, setIdx] = useState(initialIndex);
  const [open, setOpen] = useState(false);
  const [graded, setGraded] = useState<boolean | null>(null);
  const v = form.variants[idx] ?? form.variants[0];

  function reroll() {
    const n = form.variants.length;
    if (n < 2) return;
    let j = Math.floor(Math.random() * (n - 1));
    if (j >= idx) j += 1;
    setIdx(j);
    setOpen(false);
    setGraded(null);
  }

  function grade(correct: boolean) {
    setGraded(correct);
    recordSelfGrade(topic, form.id, correct, userId);
  }

  return (
    <div className="py-3.5" style={{ borderBottom: "1px solid var(--line)" }}>
      <div className="flex items-start gap-3">
        <span className="mono text-[12px] tabular flex-shrink-0 mt-1 select-none" style={{ color: "var(--fg-3)", minWidth: 24, textAlign: "right" }}>
          {number}.
        </span>
        <div className="flex-1 min-w-0">
          <p className="font-sans" style={{ fontSize: 15.5, lineHeight: 1.5, color: "var(--fg)" }}>
            <MathText text={v.statement} />
          </p>
          {v.geoFigure && (
            <div className="mt-2" style={{ maxWidth: 300 }}>
              <GeoDiagram spec={v.geoFigure} />
            </div>
          )}
          {open && (
            <div className="mt-2.5 rounded-lg px-3.5 py-3" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
              <p className="font-sans" style={{ fontSize: 14, lineHeight: 1.55, color: "var(--fg-1)" }}>
                <b>Answer: <MathText text={v.options[v.correctIndex]} /></b>{" "}
                <MathText text={v.explanation} />
              </p>
              <p className="mt-1.5 text-[12px]" style={{ color: "var(--fg-3)" }}>
                {form.skill}
              </p>
              <div className="mt-2.5 flex items-center gap-2">
                {graded === null ? (
                  <>
                    <span className="text-[12px] mr-1" style={{ color: "var(--fg-3)" }}>Did you have it?</span>
                    <button type="button" onClick={() => grade(true)} className="gm-press inline-flex items-center gap-1 rounded-full px-3 py-1 text-[12px]" style={{ background: "rgba(63,178,127,0.12)", border: "1px solid rgba(63,178,127,0.45)", color: "#2f9868" }}>
                      <Check className="h-3.5 w-3.5" /> Got it
                    </button>
                    <button type="button" onClick={() => grade(false)} className="gm-press inline-flex items-center gap-1 rounded-full px-3 py-1 text-[12px]" style={{ background: "rgba(215,80,63,0.08)", border: "1px solid rgba(215,80,63,0.4)", color: "#c05a49" }}>
                      <X className="h-3.5 w-3.5" /> Missed it
                    </button>
                  </>
                ) : (
                  <button type="button" onClick={reroll} className="gm-press inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[12px]" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}>
                    <RefreshCw className="h-3.5 w-3.5" />
                    {graded ? "Another like this" : "Try again with new numbers"}
                  </button>
                )}
              </div>
            </div>
          )}
        </div>
        <div className="flex items-center gap-1 flex-shrink-0 mt-0.5">
          <button
            type="button"
            onClick={reroll}
            title="Same kind, new numbers"
            aria-label="Same kind of problem with new numbers"
            className="gm-press grid h-8 w-8 place-items-center rounded-md"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
          >
            <RefreshCw className="h-3.5 w-3.5" />
          </button>
          <button
            type="button"
            onClick={() => setOpen((o) => !o)}
            title={open ? "Hide the solution" : "Show the solution"}
            aria-label={open ? "Hide the solution" : "Show the solution"}
            className="gm-press inline-flex h-8 items-center gap-1.5 rounded-md px-2.5 text-[12.5px]"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}
          >
            {open ? <EyeOff className="h-3.5 w-3.5" /> : <Eye className="h-3.5 w-3.5" />}
            <span className="hidden sm:inline">{open ? "Hide" : "Solution"}</span>
          </button>
        </div>
      </div>
    </div>
  );
}
