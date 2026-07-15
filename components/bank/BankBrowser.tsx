"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Zap } from "lucide-react";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import { useAuth } from "@/lib/auth-context";
import {
  type BankTopic,
  type BankForm,
  type BankLevel,
  LEVEL_LABELS,
  recordSelfGrade,
} from "@/lib/problem-bank";
import type { LessonProblem } from "@/lib/lesson-types";

const REVEAL_LABELS = {
  reveal: "Show solution",
  hide: "Hide",
  revealAria: "Show the solution",
  hideAria: "Hide the solution",
};

// The browsable problem book: EVERY problem in the topic on one page, grouped
// by level and form, numbered like a printed problem set. Work on paper,
// reveal the solution when ready, self-grade — grades feed the same per-form
// mastery the practice runner uses. The quiz-style runner lives one click
// away at ./practice for students who want instant feedback + retry loops.
export default function BankBrowser({ topic }: { topic: BankTopic }) {
  const { user } = useAuth();
  const [level, setLevel] = useState<BankLevel>(0);

  const total = topic.forms.reduce((n, f) => n + f.variants.length, 0);
  const forms = useMemo(
    () =>
      [...topic.forms]
        .filter((f) => level === 0 || f.level === level)
        .sort((a, b) => a.level - b.level),
    [topic, level],
  );
  const shown = forms.reduce((n, f) => n + f.variants.length, 0);

  // Continuous numbering across the filtered list, like a printed booklet.
  let counter = 0;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math/problem-bank" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Problem Bank · {topic.title}</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
          {topic.title}
        </h1>
        <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "58ch" }}>
          All <b className="tabular">{total}</b> problems, in order of difficulty.
          Work each one out on paper, then reveal the solution. Neighboring
          problems under one heading are the same form with different numbers —
          missed one? The next is your second chance.
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
          <span className="mono text-[12px] tabular ml-1" style={{ color: "var(--fg-3)" }}>
            {shown} problems
          </span>
        </div>

        <Link
          href={`/math/problem-bank/${topic.slug}/practice`}
          className="card-edit mt-5 p-4 flex items-center gap-3 transition-colors"
          style={{ textDecoration: "none" }}
        >
          <Zap className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
          <span className="flex-1 text-[14px]" style={{ color: "var(--fg-1)" }}>
            Prefer instant feedback? The <b>practice set</b> quizzes one problem
            per form and brings back a similar one whenever you miss.
          </span>
          <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--fg-3)" }} />
        </Link>

        {([1, 2, 3] as const)
          .filter((lv) => forms.some((f) => f.level === lv))
          .map((lv) => (
            <section key={lv} className="mt-10">
              <div className="eyebrow mb-4">{LEVEL_LABELS[lv]}</div>
              <div className="space-y-8">
                {forms
                  .filter((f) => f.level === lv)
                  .map((form) => {
                    const start = counter;
                    counter += form.variants.length;
                    return (
                      <FormBlock
                        key={form.id}
                        topic={topic}
                        form={form}
                        startIndex={start}
                        userId={user?.id}
                      />
                    );
                  })}
              </div>
            </section>
          ))}
      </div>
    </div>
  );
}

function FormBlock({
  topic, form, startIndex, userId,
}: {
  topic: BankTopic; form: BankForm; startIndex: number; userId?: string | null;
}) {
  return (
    <div>
      <div className="mb-3">
        <p className="serif" style={{ fontSize: 18, letterSpacing: "-0.01em", color: "var(--fg)" }}>
          {form.title}
        </p>
        <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
          {form.skill}
        </p>
      </div>
      <div className="space-y-3">
        {form.variants.map((v, i) => {
          const problem: LessonProblem = {
            id: v.id,
            statement: v.statement,
            solution: `Answer: ${v.options[v.correctIndex]}. ${v.explanation}`,
            geoFigure: v.geoFigure,
          } as LessonProblem;
          return (
            <RevealProblemCard
              key={v.id}
              problem={problem}
              index={startIndex + i}
              labels={REVEAL_LABELS}
              onSelfGrade={(correct) => recordSelfGrade(topic, form.id, correct, userId)}
            />
          );
        })}
      </div>
    </div>
  );
}
