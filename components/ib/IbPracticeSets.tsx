"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { ArrowRight, Check, ChevronDown, FileText } from "lucide-react";
import usePerformance from "@/lib/use-performance";
import { deriveTestRuns, runMarks, TestRun } from "@/lib/test-history";
import {
  IbPaperMeta,
  ibGradeEstimate,
  ibPaperSourcePrefix,
  listIbPracticeSets,
} from "@/lib/ib-test";

// One card per practice SET: Paper 1 + Paper 2 make the whole exam, so
// they live behind a single expandable card. A paper is "done" when a
// marked sitting exists for it — from the server-synced attempt stream
// (survives devices and storage wipes) or, for signed-out students, the
// local run state. The set is complete when BOTH papers are done.

type PaperStatus = "none" | "inProgress" | "done";

function localPhase(testId: string, paper: number): string | null {
  try {
    const raw = localStorage.getItem(`mp-ib-run:${testId}:p${paper}`);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as { phase?: string };
    return parsed?.phase ?? null;
  } catch {
    return null;
  }
}

export default function IbPracticeSets({ level }: { level?: "sl" | "hl" }) {
  const perf = usePerformance();
  const [mounted, setMounted] = useState(false);
  const [open, setOpen] = useState<Record<string, boolean>>({});

  useEffect(() => setMounted(true), []);

  const sets = listIbPracticeSets().filter((s) => !level || s.level === level);
  const runs = useMemo(() => deriveTestRuns(perf.attempts, "ib"), [perf.attempts]);

  const paperState = (meta: IbPaperMeta): { status: PaperStatus; latest: TestRun | null } => {
    if (!mounted) return { status: "none", latest: null };
    const prefix = ibPaperSourcePrefix(meta.testId, meta.paper);
    const latest = prefix ? runs.find((r) => r.testId === prefix) ?? null : null;
    if (latest) return { status: "done", latest };
    const phase = localPhase(meta.testId, meta.paper);
    if (phase === "done") return { status: "done", latest: null };
    if (phase === "work" || phase === "mark") return { status: "inProgress", latest: null };
    return { status: "none", latest: null };
  };

  return (
    <div className="space-y-3">
      {sets.map((set) => {
        const states = set.papers.map((p) => paperState(p));
        const doneCount = states.filter((s) => s.status === "done").length;
        const complete = doneCount === set.papers.length && set.papers.length > 0;
        const isOpen = !!open[set.testId];
        return (
          <div key={set.testId} className="card-edit overflow-hidden">
            <button
              className="w-full flex items-center gap-3 p-5 text-left"
              onClick={() => setOpen((o) => ({ ...o, [set.testId]: !o[set.testId] }))}
              aria-expanded={isOpen}
            >
              <FileText className="h-4 w-4 shrink-0" style={{ color: "var(--accent)" }} />
              <span className="flex-1">
                <span className="serif" style={{ fontSize: 20, color: "var(--fg)" }}>
                  {set.label}
                </span>
                {complete ? (
                  <span
                    className="mono text-[10px] uppercase ml-2 px-1.5 py-0.5 rounded inline-flex items-center gap-1"
                    style={{ color: "var(--accent)", border: "1px solid var(--accent-line)", background: "var(--accent-wash)", letterSpacing: "0.08em" }}
                  >
                    <Check className="h-3 w-3" /> Complete
                  </span>
                ) : (
                  <span
                    className="mono text-[10px] uppercase ml-2 px-1.5 py-0.5 rounded"
                    style={{ color: "var(--fg-3)", border: "1px solid var(--line)", letterSpacing: "0.08em" }}
                  >
                    {doneCount}/{set.papers.length} papers
                  </span>
                )}
                <span className="block text-[12px] mt-1" style={{ color: "var(--fg-3)" }}>
                  One full mock exam: Paper 1 (no calculator) + Paper 2 (GDC).
                  Sit both against the clock, mark yourself with the full
                  M/A/R markscheme — the set counts as done when both papers are.
                </span>
              </span>
              <ChevronDown
                className="h-4 w-4 shrink-0 transition-transform"
                style={{ color: "var(--fg-3)", transform: isOpen ? "rotate(180deg)" : "none" }}
              />
            </button>
            {isOpen && (
              <div className="px-5 pb-4 space-y-2 border-t pt-4" style={{ borderColor: "var(--line)" }}>
                {set.papers.map((p, i) => {
                  const { status, latest } = states[i];
                  const marks = latest ? runMarks(latest) : null;
                  return (
                    <Link
                      key={p.paper}
                      href={`/practice/ib/test/${p.testId}/${p.paper}`}
                      className="flex items-center gap-3 rounded-md px-4 py-3 transition-colors hover:border-[var(--accent-line)]"
                      style={{ border: "1px solid var(--line)", background: "var(--bg-2)" }}
                    >
                      {status === "done" ? (
                        <Check className="h-4 w-4 shrink-0" style={{ color: "var(--accent)" }} />
                      ) : (
                        <span
                          className="h-4 w-4 shrink-0 rounded-full"
                          style={{ border: `1.5px ${status === "inProgress" ? "dashed var(--warn)" : "solid var(--line)"}` }}
                        />
                      )}
                      <span className="flex-1">
                        <span className="text-[14px]" style={{ color: "var(--fg)" }}>
                          Paper {p.paper}
                          <span className="mono text-[10px] uppercase ml-2 px-1.5 py-0.5 rounded" style={{ color: "var(--accent)", border: "1px solid var(--accent-line)", letterSpacing: "0.08em" }}>
                            {p.calculator ? "GDC" : "No calculator"}
                          </span>
                        </span>
                        <span className="block text-[12px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                          {p.timeMinutes} minutes · {p.totalMarks} marks
                          {marks && (
                            <span className="mono tabular" style={{ color: "var(--fg-2)" }}>
                              {" "}· last sitting {marks.earned}/{marks.total} (grade ≈{ibGradeEstimate((100 * marks.earned) / marks.total)})
                            </span>
                          )}
                          {!marks && status === "inProgress" && (
                            <span style={{ color: "var(--warn)" }}> · in progress</span>
                          )}
                        </span>
                      </span>
                      <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
                    </Link>
                  );
                })}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
