"use client";

import Link from "next/link";
import { BarChart3, Target } from "lucide-react";
import BackButton from "@/components/BackButton";
import usePerformance from "@/lib/use-performance";
import { contextHref } from "@/lib/perf-context";
import { hubTopicLabel, HUB_NATIVE_METRIC_NOTE } from "@/lib/hub-analytics";

// The exam-hub progress skeleton (SAT / IB). Reads ONLY its own context from
// the shared attempt stream — the same isolation rule as everywhere else.
// Ships before the hubs have content so that the day the first mock test
// records attempts, this page lights up with zero extra wiring. Until then
// it shows an honest empty state, and the native score metric is a written
// promise instead of a fake number.
export default function HubProgress({
  context,
  title,
  comingSoonCopy,
}: {
  context: "sat" | "ib";
  title: string;
  comingSoonCopy: string;
}) {
  const perf = usePerformance();
  const overall = perf.getOverallStats(context);
  const topicStats = perf.getTopicStats(context);
  const sessions = perf.getTestOnlySessions(context);
  const hubHome = contextHref(context) ?? "/practice";
  const hasData = overall.total > 0;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          {/* History-back: this page is reachable from both the dashboard and
              the hub, so back must return to whichever the student came from. */}
          <BackButton fallback={hubHome} className="gm-press p-2 rounded-md" />
          <div className="eyebrow flex-1">{title} · Progress</div>
        </div>

        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          Your {title} <em className="serif-italic" style={{ color: "var(--accent)" }}>progress</em>.
        </h1>

        {!hasData ? (
          <section className="card-edit p-8 mt-8 text-center">
            <BarChart3 className="mx-auto h-8 w-8" style={{ color: "var(--fg-3)" }} />
            <p className="serif mt-4" style={{ fontSize: 20, color: "var(--fg)" }}>
              No {title} practice data yet.
            </p>
            <p className="text-[13px] mt-2 mx-auto" style={{ color: "var(--fg-2)", maxWidth: "44ch" }}>
              {comingSoonCopy}
            </p>
            <Link href={hubHome} className="btn btn-primary mt-6 inline-flex">
              Back to the {title} hub
            </Link>
          </section>
        ) : (
          <>
            {/* Overview — this hub's numbers only, in this hub's language */}
            <section
              className="grid gap-4 mt-8"
              style={{ gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))" }}
            >
              <div className="card-edit p-5">
                <div className="eyebrow">Questions</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                  {overall.total}
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Accuracy</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--accent)" }}>
                  {overall.accuracy}%
                </div>
              </div>
              <div className="card-edit p-5">
                <div className="eyebrow">Mock tests</div>
                <div className="serif tabular mt-2" style={{ fontSize: 36, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                  {sessions.length}
                </div>
              </div>
            </section>

            {/* Native metric: an honest placeholder until scoring curves ship */}
            <section className="card-edit p-5 mt-5" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
              <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>
                Native score
              </div>
              <p className="text-[13px]" style={{ color: "var(--fg-1)" }}>
                {HUB_NATIVE_METRIC_NOTE[context]}
              </p>
            </section>

            {/* Domain / component breakdown */}
            {topicStats.length > 0 && (
              <section className="card-edit p-6 mt-5">
                <div className="flex items-center gap-2 mb-4">
                  <Target className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
                  <div className="eyebrow">By domain</div>
                </div>
                <div className="space-y-3">
                  {topicStats.map((tt) => (
                    <div key={tt.topic}>
                      <div className="flex items-baseline justify-between mb-1.5 text-sm">
                        <span style={{ color: "var(--fg-1)" }}>{hubTopicLabel(context, tt.topic)}</span>
                        <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                          {tt.correct}/{tt.total} · {tt.accuracy}%
                        </span>
                      </div>
                      <div className="h-[3px] rounded-full overflow-hidden" style={{ background: "var(--bg-2)" }}>
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${tt.accuracy}%`,
                            background:
                              tt.accuracy >= 80 ? "var(--accent)" : tt.accuracy >= 50 ? "var(--warn)" : "var(--danger)",
                          }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </section>
            )}

            {/* Mock-test history */}
            {sessions.length > 0 && (
              <section className="card-edit p-6 mt-5">
                <div className="eyebrow mb-4">Recent mock tests</div>
                <div className="space-y-2">
                  {sessions.slice(0, 8).map((s) => (
                    <div key={s.testKey} className="flex items-baseline justify-between text-sm">
                      <span style={{ color: "var(--fg-1)" }}>{s.testKey}</span>
                      <span className="mono tabular" style={{ color: "var(--fg-3)", fontSize: 12 }}>
                        {s.correct}/{s.total} · {s.accuracy}%
                      </span>
                    </div>
                  ))}
                </div>
              </section>
            )}
          </>
        )}
      </div>
    </div>
  );
}
