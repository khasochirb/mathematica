"use client";

import { useEffect, useMemo, useState } from "react";
import {
  CheckCircle2,
  XCircle,
  ChevronDown,
  ChevronUp,
  BookOpen,
} from "lucide-react";
import MathText from "./MathText";
import EshFigure from "./EshFigure";
import {
  getTestSection2,
  gradeSection2Subproblem,
  parseSlotLabel,
  type Section2Item,
} from "@/lib/esh-section2";
import { api } from "@/lib/api";

interface ServerAttempt {
  test_key: string;
  problem: string;
  subproblem: number;
  slot_answers: Record<string, string>;
  is_correct: boolean;
  points_earned: number;
  points_max: number;
}

interface SubproblemView {
  item: Section2Item;
  slotAnswers: Record<string, string>;
  isCorrect: boolean;
  pointsEarned: number;
  pointsMax: number;
}

interface Section2ResultsProps {
  testKey: string;
  sessionId: string;
  // Per-letter answers stored in the local TestSession; the canonical
  // source for anon users (no DB row) and the fallback for authed users
  // when the server fetch fails.
  localAnswers: Record<string, Record<string, string>>;
  isAuthed: boolean;
}

export default function Section2Results({
  testKey,
  sessionId,
  localAnswers,
  isAuthed,
}: Section2ResultsProps) {
  const items = useMemo<Section2Item[]>(
    () => getTestSection2(testKey) ?? [],
    [testKey],
  );
  const [serverAttempts, setServerAttempts] = useState<ServerAttempt[] | null>(
    null,
  );
  const [serverFetchDone, setServerFetchDone] = useState(false);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());

  useEffect(() => {
    if (!isAuthed || !sessionId) {
      setServerFetchDone(true);
      return;
    }
    let cancelled = false;
    (async () => {
      try {
        const result = await api.section2.getAttempts(sessionId, testKey);
        if (!cancelled) setServerAttempts(result.attempts);
      } catch {
        // Fall back silently to client-side grading via localAnswers.
      } finally {
        if (!cancelled) setServerFetchDone(true);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [isAuthed, sessionId, testKey]);

  const perSubproblem: SubproblemView[] = useMemo(() => {
    const serverBySource = new Map<string, ServerAttempt>();
    if (serverAttempts) {
      for (const sa of serverAttempts) {
        const item = items.find(
          (i) => i.problem === sa.problem && i.subproblem === sa.subproblem,
        );
        if (item) serverBySource.set(item.source, sa);
      }
    }
    return items.map((item) => {
      const sa = serverBySource.get(item.source);
      if (sa) {
        return {
          item,
          slotAnswers: sa.slot_answers ?? {},
          isCorrect: sa.is_correct,
          pointsEarned: sa.points_earned,
          pointsMax: sa.points_max,
        };
      }
      const slotAnswers = localAnswers[item.source] ?? {};
      const grade = gradeSection2Subproblem(item, slotAnswers);
      return {
        item,
        slotAnswers,
        isCorrect: grade.correct,
        pointsEarned: grade.pointsEarned,
        pointsMax: grade.pointsMax,
      };
    });
  }, [items, serverAttempts, localAnswers]);

  const totalEarned = perSubproblem.reduce((s, p) => s + p.pointsEarned, 0);
  const totalMax = perSubproblem.reduce((s, p) => s + p.pointsMax, 0);
  const correctCount = perSubproblem.filter((p) => p.isCorrect).length;

  const problemIds = useMemo(
    () => Array.from(new Set(items.map((i) => i.problem))),
    [items],
  );
  const byProblem = useMemo(() => {
    const groups: Record<string, SubproblemView[]> = {};
    for (const p of perSubproblem) {
      const pid = p.item.problem;
      if (!groups[pid]) groups[pid] = [];
      groups[pid].push(p);
    }
    return groups;
  }, [perSubproblem]);

  const toggleExpand = (source: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(source)) next.delete(source);
      else next.add(source);
      return next;
    });
  };

  if (items.length === 0) return null;

  if (isAuthed && !serverFetchDone) {
    return (
      <div className="card-edit p-6 mb-4 text-center">
        <p
          className="mono text-[11px] uppercase"
          style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
        >
          АЧААЛЛАЖ БАЙНА...
        </p>
      </div>
    );
  }

  const headerColor =
    totalMax > 0 && totalEarned === totalMax
      ? "var(--accent)"
      : totalEarned > 0
        ? "var(--warn)"
        : "var(--danger)";

  return (
    <div className="mt-6">
      {/* Header */}
      <div className="card-edit p-6 mb-4">
        <div className="flex items-center justify-between flex-wrap gap-3">
          <div>
            <div className="eyebrow mb-1">Хэсэг 2 · Нээлттэй бодлого</div>
            <p
              className="serif tabular"
              style={{
                fontSize: 36,
                color: headerColor,
                letterSpacing: "-0.02em",
                lineHeight: 1.05,
              }}
            >
              {totalEarned}
              <span
                className="mono text-[16px]"
                style={{ color: "var(--fg-3)" }}
              >
                /{totalMax}
              </span>
              <span
                className="mono text-[11px] ml-2 uppercase"
                style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
              >
                оноо
              </span>
            </p>
          </div>
          <p
            className="mono text-[10px] uppercase"
            style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}
          >
            {correctCount}/{perSubproblem.length} зөв
          </p>
        </div>
      </div>

      {/* Per-problem cards */}
      <div className="space-y-4">
        {problemIds.map((pid) => {
          const subs = byProblem[pid] ?? [];
          const earned = subs.reduce((s, p) => s + p.pointsEarned, 0);
          const max = subs.reduce((s, p) => s + p.pointsMax, 0);
          const allCorrect = subs.length > 0 && subs.every((p) => p.isCorrect);
          const noneCorrect = subs.every((p) => !p.isCorrect);
          const tintBase = allCorrect
            ? "var(--accent)"
            : noneCorrect
              ? "var(--danger)"
              : "var(--warn)";
          return (
            <div
              key={pid}
              className="card-edit p-5"
              style={{
                background: `color-mix(in oklch, ${tintBase} 5%, transparent)`,
                borderColor: `color-mix(in oklch, ${tintBase} 25%, transparent)`,
              }}
            >
              <div className="flex items-center justify-between mb-3">
                <div className="eyebrow">{pid}</div>
                <span
                  className="mono text-[11px] tabular uppercase"
                  style={{
                    color: "var(--fg-2)",
                    letterSpacing: "0.06em",
                  }}
                >
                  {earned}/{max} оноо
                </span>
              </div>

              {/* Figure: rendered once per problem on the first
                  subproblem (item.figure is only set on subproblem===1
                  by wire-figures-to-json.py). Sits above the shared
                  context block, mirroring the Section2Card layout in
                  the runner so review-mode visual matches test-mode. */}
              {subs[0]?.item.figure && (
                <div className="mb-3">
                  <EshFigure {...subs[0].item.figure} />
                </div>
              )}

              {subs[0]?.item.context && (
                <div
                  className="text-[13px] mb-3 leading-relaxed"
                  style={{ color: "var(--fg-1)" }}
                >
                  <MathText text={subs[0].item.context} />
                </div>
              )}

              <div className="space-y-2">
                {subs.map((p) => (
                  <SubproblemRow
                    key={p.item.source}
                    view={p}
                    isExpanded={expanded.has(p.item.source)}
                    onToggle={() => toggleExpand(p.item.source)}
                  />
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function SubproblemRow({
  view,
  isExpanded,
  onToggle,
}: {
  view: SubproblemView;
  isExpanded: boolean;
  onToggle: () => void;
}) {
  const { item, slotAnswers, isCorrect, pointsEarned, pointsMax } = view;
  return (
    <div>
      <button
        onClick={onToggle}
        className="w-full flex items-center gap-3 px-4 py-3 rounded-md transition-all text-left"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
      >
        <span
          className="mono tabular px-2.5 h-7 rounded flex items-center justify-center text-[11px] shrink-0"
          style={{
            background: "var(--bg-1)",
            border: "1px solid var(--line)",
            color: "var(--fg-2)",
          }}
        >
          ({item.subproblem})
        </span>
        <span
          className="flex-1 mono text-[11px] uppercase"
          style={{ color: "var(--fg-2)", letterSpacing: "0.06em" }}
        >
          {pointsEarned}/{pointsMax} оноо
        </span>
        {isCorrect ? (
          <CheckCircle2
            className="w-4 h-4 shrink-0"
            style={{ color: "var(--accent)" }}
          />
        ) : (
          <XCircle
            className="w-4 h-4 shrink-0"
            style={{ color: "var(--danger)" }}
          />
        )}
        {isExpanded ? (
          <ChevronUp className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
        ) : (
          <ChevronDown className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
        )}
      </button>

      {isExpanded && (
        <div
          className="mt-2 mb-1 p-5 rounded-md"
          style={{
            background: "var(--bg-1)",
            border: "1px solid var(--line)",
          }}
        >
          <div
            className="text-[14px] leading-relaxed mb-4"
            style={{ color: "var(--fg-1)" }}
          >
            <MathText text={item.instruction} />
          </div>
          <SlotComparison item={item} slotAnswers={slotAnswers} />
          <SolutionAccordion solution={item.solution} />
        </div>
      )}
    </div>
  );
}

function SlotComparison({
  item,
  slotAnswers,
}: {
  item: Section2Item;
  slotAnswers: Record<string, string>;
}) {
  return (
    <div className="mb-4">
      <div className="eyebrow mb-2">Хариу</div>
      <div className="grid gap-1.5">
        {[...item.slots]
          .sort((a, b) =>
            parseSlotLabel(a.label).varPart.localeCompare(
              parseSlotLabel(b.label).varPart,
            ),
          )
          .flatMap((slot) => {
          const { prefix, varPart } = parseSlotLabel(slot.label);
          const correctVarDigits = slot.answer.slice(prefix.length).split("");
          return varPart.split("").map((letter, i) => {
            const userDigit = slotAnswers[letter] ?? "";
            const correctDigit = correctVarDigits[i] ?? "";
            const matches = userDigit !== "" && userDigit === correctDigit;
            const labelText =
              prefix && i === 0 ? `${prefix}${letter}` : letter;
            return (
              <div
                key={`${slot.label}-${letter}`}
                className="flex items-center gap-3 text-[13px]"
              >
                <span
                  className="mono w-12 shrink-0 text-right"
                  style={{ color: "var(--fg-2)" }}
                >
                  {labelText}:
                </span>
                <span
                  className="mono tabular w-9 h-9 rounded shrink-0 flex items-center justify-center"
                  style={{
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                    color: userDigit ? "var(--fg)" : "var(--fg-3)",
                    fontSize: 15,
                  }}
                >
                  {userDigit || "—"}
                </span>
                {matches ? (
                  <CheckCircle2
                    className="w-4 h-4 shrink-0"
                    style={{ color: "var(--accent)" }}
                  />
                ) : (
                  <>
                    <XCircle
                      className="w-4 h-4 shrink-0"
                      style={{ color: "var(--danger)" }}
                    />
                    <span
                      className="mono text-[11px]"
                      style={{ color: "var(--fg-2)" }}
                    >
                      зөв:{" "}
                      <span
                        className="tabular"
                        style={{ color: "var(--accent)" }}
                      >
                        {correctDigit}
                      </span>
                    </span>
                  </>
                )}
              </div>
            );
          });
        })}
      </div>
    </div>
  );
}

function SolutionAccordion({ solution }: { solution: string }) {
  const [open, setOpen] = useState(false);
  if (!solution) return null;
  return (
    <div>
      <button
        onClick={() => setOpen(!open)}
        className="w-full flex items-center justify-between px-3 py-2 rounded-md text-left"
        style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}
      >
        <span
          className="mono text-[11px] uppercase flex items-center gap-2"
          style={{ color: "var(--fg-2)", letterSpacing: "0.06em" }}
        >
          <BookOpen className="w-3.5 h-3.5" />
          Бодолт
        </span>
        {open ? (
          <ChevronUp className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
        ) : (
          <ChevronDown className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
        )}
      </button>
      {open && (
        <div
          className="mt-2 p-4 rounded-md text-[13px] leading-relaxed"
          style={{
            background: "var(--bg-2)",
            border: "1px solid var(--line)",
            color: "var(--fg-1)",
          }}
        >
          <MathText text={solution} />
        </div>
      )}
    </div>
  );
}
