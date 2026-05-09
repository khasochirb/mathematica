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
    <div
      className="min-h-screen pt-20 pb-12 px-4 sm:px-6"
      style={{ background: "var(--bg)", color: "var(--fg)" }}
    >
      <div className="max-w-3xl mx-auto">
        <div className="mb-6 flex items-end justify-between gap-4 flex-wrap">
          <div>
            <h1
              className="font-display text-xl font-bold"
              style={{ color: "var(--fg)" }}
            >
              Section 2 preview
            </h1>
            <p className="text-sm mt-1" style={{ color: "var(--fg-2)" }}>
              Dev-only visual smoke. {items.length} subproblems · 28 pts ·{" "}
              {testKey}
            </p>
          </div>
          <div className="flex flex-col gap-1">
            <label
              className="text-xs uppercase tracking-wide"
              style={{ color: "var(--fg-3)" }}
            >
              Test
            </label>
            <select
              value={testKey}
              onChange={(e) => {
                router.replace(`/dev/section2-preview?test=${e.target.value}`);
              }}
              className="rounded-lg px-3 py-2 text-sm"
              style={{
                background: "var(--bg-1)",
                border: "1px solid var(--line)",
                color: "var(--fg)",
              }}
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

        <div
          className="mt-8 p-4 rounded-xl text-xs leading-relaxed"
          style={{
            background: "var(--bg-1)",
            border: "1px solid var(--line)",
            color: "var(--fg-2)",
          }}
        >
          <p
            className="font-semibold mb-2"
            style={{ color: "var(--fg-1)" }}
          >
            Smoke checklist
          </p>
          <ul className="list-disc list-inside space-y-1">
            <li>Cards visible against page bg in both light + dark themes</li>
            <li>
              Formula: each <code>[label]</code> renders as a{" "}
              <code>\boxed{"{"}varPart{"}"}</code> rectangle (no input)
            </li>
            <li>
              Answer panel below: per-letter inputs in a grid (one digit
              each)
            </li>
            <li>Click any answer-panel input → focus ring → type a digit</li>
            <li>
              2024B/2024C 2.4.2 (literal-prefix <code>1e</code>): formula
              shows literal <code>1</code> + <code>\boxed{"{"}e{"}"}</code>;
              answer panel has one input labeled <code>e</code>
            </li>
            <li>
              Multi-letter slots (e.g. <code>bc</code>, <code>fgh</code>)
              split into separate inputs in the answer panel
            </li>
            <li>Per-problem context shows once, above the first subproblem</li>
            <li>Toggle theme via nav sun/moon — both modes readable</li>
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
