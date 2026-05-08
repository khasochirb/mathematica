"use client";

// Dev-only preview page for the Section 2 renderer (S2.2 visual smoke
// gate). Loads one authored test's Section 2 content and renders all
// subproblems vertically so we can eyeball each one against the official
// PDF before wiring the runner.
//
// Gated to non-production environments via `process.env.NODE_ENV` check
// — production builds 404 this route.
//
// Switch tests via the dropdown at the top, or `?test=2024B` query
// param. State for slot answers is held in local component state — no
// persistence, no grading; this is purely for visual review.

import { Suspense, useEffect, useMemo, useState } from "react";
import { notFound, useRouter, useSearchParams } from "next/navigation";
import Section2Card from "@/components/esh/Section2Card";
import {
  SECTION2_AUTHORED_KEYS,
  getTestSection2,
  type Section2Item,
} from "@/lib/esh-section2";

const isDev = process.env.NODE_ENV !== "production";

function Section2PreviewInner() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const requestedKey = (searchParams.get("test") ?? "2021A").toUpperCase();
  const testKey = SECTION2_AUTHORED_KEYS.includes(requestedKey)
    ? requestedKey
    : "2021A";

  const items: Section2Item[] | undefined = useMemo(
    () => getTestSection2(testKey),
    [testKey],
  );

  const [answers, setAnswers] = useState<
    Record<string, Record<string, string>>
  >({});

  useEffect(() => {
    setAnswers({});
  }, [testKey]);

  if (!items) {
    return (
      <div className="min-h-screen pt-20 px-6 text-gray-300">
        No items for {testKey}.
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-surface-900 pt-20 pb-12 px-4 sm:px-6">
      <div className="max-w-3xl mx-auto">
        <div className="mb-6 flex items-end justify-between gap-4 flex-wrap">
          <div>
            <h1 className="font-display text-xl font-bold text-white">
              Section 2 preview
            </h1>
            <p className="text-sm text-gray-500 mt-1">
              Dev-only visual smoke. {items.length} subproblems · 28 pts ·{" "}
              {testKey}
            </p>
          </div>
          <div className="flex flex-col gap-1">
            <label className="text-xs uppercase tracking-wide text-gray-500">
              Test
            </label>
            <select
              value={testKey}
              onChange={(e) => {
                router.replace(`/dev/section2-preview?test=${e.target.value}`);
              }}
              className="bg-white/[0.05] border border-white/[0.08] rounded-lg px-3 py-2 text-sm text-white"
            >
              {SECTION2_AUTHORED_KEYS.map((k) => (
                <option key={k} value={k}>
                  {k}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="space-y-4">
          {items.map((item, i) => {
            const isFirstOfProblem =
              i === 0 || items[i - 1].problem !== item.problem;
            return (
              <Section2Card
                key={item.source}
                item={item}
                showContext={isFirstOfProblem}
                answers={answers[item.source] ?? {}}
                onAnswerChange={(label, value) =>
                  setAnswers((prev) => ({
                    ...prev,
                    [item.source]: {
                      ...(prev[item.source] ?? {}),
                      [label]: value,
                    },
                  }))
                }
                questionLabel={`${item.problem} (${item.subproblem})`}
              />
            );
          })}
        </div>

        <div className="mt-8 p-4 rounded-xl bg-white/[0.03] border border-white/[0.05] text-xs text-gray-500 leading-relaxed">
          <p className="font-semibold text-gray-400 mb-2">Smoke checklist</p>
          <ul className="list-disc list-inside space-y-1">
            <li>Cyrillic + math read like the official PDF</li>
            <li>
              Slot letters appear inline as variables (e.g.{" "}
              <code>x ≥ a/b</code>)
            </li>
            <li>
              Slot tray below shows one input per slot; widths match answer
              length
            </li>
            <li>
              Literal-prefix slots (only on 2024B/2024C 2.4.2 — label{" "}
              <code>1e</code>) render the &quot;1&quot; prefix as text before
              the input
            </li>
            <li>
              On a touch device or with <code>pointer:coarse</code>, the numeric
              keypad appears below each card
            </li>
            <li>Per-problem context shows once, above the first subproblem</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default function Section2PreviewPage() {
  if (!isDev) notFound();
  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-surface-900 pt-20 px-6 text-gray-500">
          Loading…
        </div>
      }
    >
      <Section2PreviewInner />
    </Suspense>
  );
}
