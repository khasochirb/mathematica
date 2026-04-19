"use client";

import React, { useMemo } from "react";
import Link from "next/link";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import { useAuth } from "@/lib/auth-context";
import { getTestInfo, TOPIC_LABELS } from "@/lib/esh-questions";

function formatRelative(ts: number): string {
  const diff = Date.now() - ts;
  const min = Math.floor(diff / 60_000);
  if (min < 1) return "just now";
  if (min < 60) return `${min}m ago`;
  const hr = Math.floor(min / 60);
  if (hr < 24) return `${hr}h ago`;
  const day = Math.floor(hr / 24);
  if (day < 7) return `${day}d ago`;
  const d = new Date(ts);
  return d.toLocaleDateString(undefined, { month: "short", day: "numeric" });
}

function formatTime(ts: number): string {
  const d = new Date(ts);
  return d.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" });
}

function trendArrow(delta: number): { text: string; color: string } {
  if (delta > 1) return { text: `▲ +${delta}`, color: "var(--accent)" };
  if (delta < -1) return { text: `▼ ${delta}`, color: "var(--warn)" };
  return { text: "∼ flat", color: "var(--fg-2)" };
}

export default function AnalyticsPage() {
  const perf = usePerformance();
  const ts = useTestSession();
  const { user } = useAuth();

  const overall = perf.getOverallStats();
  const topicStats = perf.getTopicStats();
  const completed = ts.getCompletedSessions();
  const incorrectAttempts = useMemo(
    () => perf.attempts.filter((a) => !a.isCorrect).slice().reverse(),
    [perf.attempts],
  );

  const hasData = overall.total > 0 || completed.length > 0;

  const latestSession = completed[0];
  const latestPct = latestSession?.score?.accuracy ?? null;
  const bestPct = completed.length
    ? Math.max(...completed.map((s) => s.score?.accuracy ?? 0))
    : null;
  const projected = bestPct !== null ? Math.min(800, Math.round(bestPct * 8)) : null;

  const weakTopics = topicStats.filter((t) => t.accuracy < 70 && t.total >= 3);

  // Build score trajectory from completed sessions, oldest → newest.
  const trajectory = useMemo(() => {
    return completed
      .slice()
      .reverse()
      .map((s) => ({
        ts: s.completedAt || s.startedAt,
        pct: s.score?.accuracy ?? 0,
        testKey: s.testKey,
      }));
  }, [completed]);

  // Topic deltas: compare last 5 attempts vs prior attempts per topic.
  const topicTrends = useMemo(() => {
    const map: Record<string, { recent: number[]; prior: number[] }> = {};
    for (const a of perf.attempts) {
      if (!map[a.topic]) map[a.topic] = { recent: [], prior: [] };
    }
    for (const t of Object.keys(map)) {
      const tAttempts = perf.attempts.filter((a) => a.topic === t);
      const split = Math.max(0, tAttempts.length - 5);
      map[t].prior = tAttempts.slice(0, split).map((a) => (a.isCorrect ? 1 : 0));
      map[t].recent = tAttempts.slice(split).map((a) => (a.isCorrect ? 1 : 0));
    }
    const out: Record<string, number> = {};
    for (const [topic, { recent, prior }] of Object.entries(map)) {
      if (recent.length === 0 || prior.length === 0) {
        out[topic] = 0;
        continue;
      }
      const r = (recent.reduce((a, b) => a + b, 0) / recent.length) * 100;
      const p = (prior.reduce((a, b) => a + b, 0) / prior.length) * 100;
      out[topic] = Math.round(r - p);
    }
    return out;
  }, [perf.attempts]);

  const displayTopics = topicStats.map((s) => {
    const delta = topicTrends[s.topic] ?? 0;
    const arrow = trendArrow(delta);
    return {
      topic: s.topic,
      label: TOPIC_LABELS[s.topic] || s.label,
      accuracy: s.accuracy,
      total: s.total,
      trend: arrow.text,
      trendColor: arrow.color,
      weak: s.accuracy < 50,
    };
  });

  const displayName = user?.displayName || "Student";

  return (
    <div className="grid min-h-[calc(100vh-64px)] pt-16" style={{ gridTemplateColumns: "minmax(0, 240px) minmax(0, 1fr)", background: "var(--bg)" }}>
      {/* Side nav */}
      <aside
        className="hidden md:block sticky overflow-y-auto"
        style={{
          top: 64,
          alignSelf: "start",
          height: "calc(100vh - 64px)",
          padding: "24px 18px",
          borderRight: "1px solid var(--line)",
        }}
      >
        <h5 className="eyebrow mb-2.5 px-2">Sections</h5>
        {[
          { label: "Overview", href: "#overview" },
          { label: "Topic mastery", href: "#topic-mastery" },
          { label: "Test history", href: "#test-history" },
          { label: "Recent attempts", href: "#recent-attempts" },
          { label: "Mistakes", href: "#mistakes" },
        ].map((s) => (
          <a key={s.label} href={s.href} className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
            {s.label}
          </a>
        ))}

        <h5 className="eyebrow mb-2.5 px-2 mt-5">Quick actions</h5>
        <Link href="/practice/esh" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          Take an ЭЕШ test
        </Link>
        <Link href="/practice/esh/previous-years" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          Previous year tests
        </Link>
        <Link href="/practice" className="block px-2.5 py-2 text-[13px] rounded-md" style={{ color: "var(--fg-1)" }}>
          Practice hub
        </Link>
      </aside>

      {/* Main */}
      <section className="px-6 md:px-10 py-9 md:py-12 min-w-0">
        {/* Head */}
        <div id="overview" className="flex items-end justify-between flex-wrap gap-6 pb-7" style={{ borderBottom: "1px solid var(--line)" }}>
          <div>
            <div className="eyebrow">Performance analytics</div>
            <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(40px, 5vw, 56px)", letterSpacing: "-0.03em", margin: "8px 0 0", lineHeight: 1, color: "var(--fg)" }}>
              {projected !== null ? (
                <>
                  Projected {projected}
                  <span className="mono" style={{ color: "var(--fg-3)", fontSize: 28, letterSpacing: 0 }}>/800</span>
                </>
              ) : (
                <>No tests yet</>
              )}
            </h1>
            <div className="mt-2.5 text-[13px]" style={{ color: "var(--fg-2)" }}>
              <strong style={{ color: "var(--fg)" }}>{displayName}</strong>
              {" · "}
              <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.04em" }}>
                ON THIS DEVICE · ACCOUNT SYNC COMING SOON
              </span>
            </div>
          </div>
          <div className="flex gap-2 items-center">
            <Link href="/practice/esh" className="btn btn-line">Take an ЭЕШ test</Link>
            <Link href="/practice/esh/previous-years" className="btn btn-primary">Previous years</Link>
          </div>
        </div>

        {!hasData && (
          <div
            className="card-edit p-10 mt-7 text-center"
            style={{ borderStyle: "dashed" }}
          >
            <div className="eyebrow" style={{ color: "var(--accent)" }}>Get started</div>
            <h2 className="serif mt-2" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              Take a test to see your analytics.
            </h2>
            <p className="mt-2 mb-5 text-[14px]" style={{ color: "var(--fg-2)" }}>
              Your projected score, weak topics, and mistakes show up here as soon as you complete a test.
            </p>
            <div className="flex gap-3 justify-center">
              <Link href="/practice/esh" className="btn btn-primary">Start an ЭЕШ test</Link>
              <Link href="/practice/esh/previous-years" className="btn btn-line">Previous year tests</Link>
            </div>
          </div>
        )}

        {hasData && (
          <>
            {/* KPI band */}
            <div
              className="mt-7 grid card-edit overflow-hidden"
              style={{ gridTemplateColumns: "minmax(0,1.4fr) minmax(0,1fr) minmax(0,1fr) minmax(0,1fr)" }}
            >
              <div className="p-7" style={{ borderRight: "1px solid var(--line)" }}>
                <div className="eyebrow mb-2.5">Projected ЭЕШ score</div>
                <div className="serif tabular" style={{ fontWeight: 400, fontSize: 72, letterSpacing: "-0.04em", lineHeight: 0.95, color: "var(--fg)" }}>
                  {projected ?? "—"}
                  {projected !== null && (
                    <sup className="mono ml-1" style={{ fontSize: 20, color: "var(--fg-3)", verticalAlign: "top" }}>/800</sup>
                  )}
                </div>
                <div className="mono mt-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                  Based on your best test ({bestPct ?? 0}% accuracy)
                </div>
                {trajectory.length >= 2 && (
                  <svg viewBox="0 0 400 80" preserveAspectRatio="none" width="100%" height="80" style={{ marginTop: 16 }}>
                    {(() => {
                      const max = 100;
                      const min = 0;
                      const w = 400;
                      const h = 80;
                      const pts = trajectory.map((p, i) => {
                        const x = (i / Math.max(1, trajectory.length - 1)) * w;
                        const y = h - ((p.pct - min) / (max - min)) * (h - 8) - 4;
                        return { x, y };
                      });
                      const d = pts.map((p, i) => `${i === 0 ? "M" : "L"}${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
                      const area = `${d} L${w},${h} L0,${h} Z`;
                      return (
                        <>
                          <defs>
                            <linearGradient id="k1" x1="0" x2="0" y1="0" y2="1">
                              <stop offset="0" stopColor="var(--accent)" stopOpacity={0.25} />
                              <stop offset="1" stopColor="var(--accent)" stopOpacity={0} />
                            </linearGradient>
                          </defs>
                          <path d={area} fill="url(#k1)" />
                          <path d={d} fill="none" stroke="var(--accent)" strokeWidth={1.5} />
                        </>
                      );
                    })()}
                  </svg>
                )}
              </div>
              {[
                { lbl: "Overall accuracy", val: `${overall.accuracy}`, suffix: "%" },
                { lbl: "Tests completed", val: `${completed.length}`, suffix: "" },
                { lbl: "Weak topics", val: `${weakTopics.length}`, suffix: ` / ${topicStats.length || 0}` },
              ].map((s, i) => (
                <div
                  key={s.lbl}
                  className="p-7"
                  style={{ borderRight: i < 2 ? "1px solid var(--line)" : "none" }}
                >
                  <div className="eyebrow mb-2.5">{s.lbl}</div>
                  <div className="serif tabular" style={{ fontSize: 44, lineHeight: 1, letterSpacing: "-0.03em", color: "var(--fg)" }}>
                    {s.val}
                    {s.suffix && <span className="mono ml-1" style={{ fontSize: 20, color: "var(--fg-3)" }}>{s.suffix}</span>}
                  </div>
                  <div className="mono mt-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                    {s.lbl === "Overall accuracy"
                      ? `${overall.correct}/${overall.total} correct`
                      : s.lbl === "Tests completed"
                        ? latestSession
                          ? `Latest: ${latestPct}% · ${formatRelative(latestSession.completedAt || latestSession.startedAt)}`
                          : "No completed tests yet"
                        : weakTopics.length > 0
                          ? `Lowest: ${TOPIC_LABELS[weakTopics[0].topic] || weakTopics[0].topic}`
                          : "Nothing under 70%"}
                  </div>
                </div>
              ))}
            </div>

            {/* Row 1: Score trajectory + Recommendations */}
            <div className="grid gap-5 mt-5" style={{ gridTemplateColumns: "minmax(0,1.4fr) minmax(0,1fr)" }}>
              <div id="test-history" className="card-edit overflow-hidden">
                <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                  <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                    Score trajectory · {trajectory.length} test{trajectory.length === 1 ? "" : "s"}
                  </h3>
                  <div className="mono uppercase flex gap-3" style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.08em" }}>
                    <span><span className="inline-block mr-1.5" style={{ width: 8, height: 8, background: "var(--accent)", borderRadius: 2 }} />Accuracy %</span>
                  </div>
                </div>
                <div className="p-5">
                  {trajectory.length === 0 && (
                    <div className="text-[13px] py-10 text-center" style={{ color: "var(--fg-2)" }}>
                      Complete a test to plot your trajectory.
                    </div>
                  )}
                  {trajectory.length > 0 && (
                    (() => {
                      const W = 720;
                      const H = 300;
                      const padL = 50;
                      const padR = 20;
                      const padT = 30;
                      const padB = 40;
                      const innerW = W - padL - padR;
                      const innerH = H - padT - padB;
                      const n = trajectory.length;
                      const xFor = (i: number) =>
                        padL + (n === 1 ? innerW / 2 : (i / (n - 1)) * innerW);
                      const yFor = (pct: number) =>
                        padT + innerH - (pct / 100) * innerH;
                      const linePath = trajectory
                        .map((p, i) => `${i === 0 ? "M" : "L"}${xFor(i).toFixed(1)},${yFor(p.pct).toFixed(1)}`)
                        .join(" ");
                      const areaPath = `${linePath} L${xFor(n - 1).toFixed(1)},${(padT + innerH).toFixed(1)} L${xFor(0).toFixed(1)},${(padT + innerH).toFixed(1)} Z`;
                      return (
                        <svg viewBox={`0 0 ${W} ${H}`} width="100%" height={H}>
                          <defs>
                            <linearGradient id="band2" x1="0" x2="0" y1="0" y2="1">
                              <stop offset="0" stopColor="var(--accent)" stopOpacity={0.22} />
                              <stop offset="1" stopColor="var(--accent)" stopOpacity={0} />
                            </linearGradient>
                          </defs>
                          <g stroke="var(--line)" strokeWidth={1}>
                            {[0, 25, 50, 75, 100].map((v) => (
                              <line key={v} x1={padL} y1={yFor(v)} x2={W - padR} y2={yFor(v)} />
                            ))}
                          </g>
                          <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                            {[0, 25, 50, 75, 100].map((v) => (
                              <text key={v} x={padL - 8} y={yFor(v) + 3} textAnchor="end">{v}%</text>
                            ))}
                          </g>
                          <path d={areaPath} fill="url(#band2)" />
                          <path d={linePath} fill="none" stroke="var(--accent)" strokeWidth={2} />
                          <g fill="var(--fg)">
                            {trajectory.map((p, i) => (
                              <circle key={i} cx={xFor(i)} cy={yFor(p.pct)} r={3.5} />
                            ))}
                          </g>
                          <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                            {trajectory.map((p, i) => {
                              if (n > 8 && i % Math.ceil(n / 8) !== 0 && i !== n - 1) return null;
                              const d = new Date(p.ts);
                              const lbl = d.toLocaleDateString(undefined, { month: "short", day: "numeric" });
                              return (
                                <text key={i} x={xFor(i)} y={H - 12} textAnchor="middle">{lbl}</text>
                              );
                            })}
                          </g>
                        </svg>
                      );
                    })()
                  )}
                </div>
              </div>

              <div className="grid gap-5" style={{ alignContent: "start" }}>
                <div
                  className="card-edit p-6"
                  style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
                >
                  <div className="eyebrow" style={{ color: "var(--accent)" }}>Recommended next</div>
                  <h4 className="serif mt-1.5" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--accent)" }}>
                    {weakTopics.length > 0
                      ? `Focus on ${TOPIC_LABELS[weakTopics[0].topic] || weakTopics[0].topic}.`
                      : completed.length === 0
                        ? "Take your first ЭЕШ test."
                        : "You're solid across the board."}
                  </h4>
                  <p className="mt-2 mb-4 text-sm" style={{ color: "var(--fg-1)" }}>
                    {weakTopics.length > 0
                      ? `You're at ${weakTopics[0].accuracy}% on ${weakTopics.length} weak topic${weakTopics.length === 1 ? "" : "s"}. Drill them to lift your projected score.`
                      : completed.length === 0
                        ? "We'll start tracking weak topics and trends as soon as you complete one."
                        : "Try a previous year test to confirm exam-day pacing."}
                  </p>
                  <div className="grid gap-2">
                    {weakTopics.slice(0, 3).map((t) => (
                      <div
                        key={t.topic}
                        className="grid items-center gap-3 px-3 py-2.5 rounded-lg text-[13px]"
                        style={{
                          background: "var(--bg-1)",
                          border: "1px solid var(--line)",
                          gridTemplateColumns: "1fr auto",
                        }}
                      >
                        <div>
                          <div style={{ color: "var(--fg)" }}>{TOPIC_LABELS[t.topic] || t.label}</div>
                          <div className="eyebrow" style={{ fontSize: 10 }}>
                            {t.accuracy}% · {t.total} attempt{t.total === 1 ? "" : "s"}
                          </div>
                        </div>
                        <Link
                          href={`/practice/esh/learn/${t.topic}`}
                          className="btn btn-line"
                          style={{ fontSize: 12, padding: "7px 12px" }}
                        >
                          Practice
                        </Link>
                      </div>
                    ))}
                    {weakTopics.length === 0 && (
                      <Link
                        href="/practice/esh/previous-years"
                        className="btn btn-primary"
                        style={{ fontSize: 12, padding: "9px 12px" }}
                      >
                        Try a previous year test →
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Row 2: Topic mastery */}
            <div id="topic-mastery" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  Topic mastery · {displayTopics.length} tracked
                </h3>
                <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  {overall.total} ATTEMPT{overall.total === 1 ? "" : "S"}
                </span>
              </div>
              {displayTopics.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  No attempts recorded yet.
                </div>
              ) : (
                <table className="w-full" style={{ borderCollapse: "collapse" }}>
                  <thead>
                    <tr style={{ background: "var(--bg-2)" }}>
                      {["Topic", "Mastery", "%", "Attempts", "Recent trend", ""].map((h) => (
                        <th
                          key={h}
                          className="mono uppercase text-left"
                          style={{
                            padding: "12px 18px",
                            fontSize: 10,
                            letterSpacing: "0.1em",
                            color: "var(--fg-3)",
                            fontWeight: 500,
                            borderBottom: "1px solid var(--line)",
                          }}
                        >
                          {h}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {displayTopics.map((t) => (
                      <tr key={t.topic} style={{ borderBottom: "1px solid var(--line)" }}>
                        <td style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg)", fontWeight: 500 }}>{t.label}</td>
                        <td style={{ padding: "12px 18px" }}>
                          <span style={{ display: "inline-block", width: 160, height: 4, borderRadius: 99, background: "var(--bg-3)", overflow: "hidden" }}>
                            <span
                              style={{
                                display: "block",
                                height: "100%",
                                width: `${t.accuracy}%`,
                                background: t.weak ? "var(--warn)" : "var(--accent)",
                              }}
                            />
                          </span>
                        </td>
                        <td className="mono tabular" style={{ padding: "12px 18px", fontSize: 13, textAlign: "right", width: 48, color: t.weak ? "var(--warn)" : "var(--fg-1)" }}>
                          {t.accuracy}
                        </td>
                        <td className="mono tabular" style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg-2)" }}>
                          {t.total}
                        </td>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 11, color: t.trendColor }}>
                          {t.trend}
                        </td>
                        <td style={{ padding: "12px 18px", fontSize: 12 }}>
                          <Link href={`/practice/esh/learn/${t.topic}`} style={{ color: "var(--accent)" }}>Practice →</Link>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>

            {/* Row 3: Recent test history */}
            <div id="recent-attempts" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  Recent tests
                </h3>
                <Link href="/practice/esh" className="mono" style={{ fontSize: 11, color: "var(--accent)", letterSpacing: "0.08em" }}>TAKE ANOTHER →</Link>
              </div>
              {completed.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  No completed tests yet.
                </div>
              ) : (
                <div>
                  {completed.slice(0, 8).map((s, i) => {
                    const info = getTestInfo(s.testKey);
                    const completedAt = s.completedAt || s.startedAt;
                    const score = s.score;
                    const pct = score?.accuracy ?? 0;
                    return (
                      <div
                        key={s.id}
                        className="grid items-center gap-3.5 px-5 py-3.5 text-[13px]"
                        style={{
                          gridTemplateColumns: "100px 1fr auto auto",
                          borderBottom: i < Math.min(7, completed.length - 1) ? "1px solid var(--line)" : "none",
                        }}
                      >
                        <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.05em" }}>
                          {formatRelative(completedAt)}
                          <br />
                          <span style={{ fontSize: 10 }}>{formatTime(completedAt)}</span>
                        </span>
                        <span style={{ color: "var(--fg)" }}>
                          <span
                            className="inline-block mr-2"
                            style={{ width: 8, height: 8, borderRadius: 99, background: pct >= 70 ? "var(--accent)" : pct >= 50 ? "var(--fg-2)" : "var(--warn)", verticalAlign: 1 }}
                          />
                          <strong>{info?.label || s.testKey}</strong>
                          {score && (
                            <span style={{ color: "var(--fg-2)" }}>
                              {" · "}{score.correct}/{score.total} correct{score.skipped > 0 ? ` · ${score.skipped} skipped` : ""}
                            </span>
                          )}
                        </span>
                        <span className="mono tabular" style={{ fontSize: 13, color: pct >= 70 ? "var(--accent)" : pct >= 50 ? "var(--fg-1)" : "var(--warn)" }}>
                          {pct}%
                        </span>
                        <Link
                          href={`/practice/esh/test/${s.testKey.toLowerCase()}/results?session=${s.id}`}
                          className="mono"
                          style={{ fontSize: 11, color: "var(--accent)", letterSpacing: "0.05em" }}
                        >
                          REVIEW
                        </Link>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            {/* Mistake library */}
            <div id="mistakes" className="card-edit overflow-hidden mt-5">
              <div className="px-5 py-4 flex items-center justify-between" style={{ borderBottom: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  Mistake library · {incorrectAttempts.length}
                </h3>
                <span className="mono" style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.08em" }}>
                  MOST RECENT FIRST
                </span>
              </div>
              {incorrectAttempts.length === 0 ? (
                <div className="p-8 text-[13px] text-center" style={{ color: "var(--fg-2)" }}>
                  No incorrect attempts yet — keep going.
                </div>
              ) : (
                <table className="w-full" style={{ borderCollapse: "collapse" }}>
                  <thead>
                    <tr style={{ background: "var(--bg-2)" }}>
                      {["Question", "Topic", "Your answer", "Correct", "When", ""].map((h) => (
                        <th
                          key={h}
                          className="mono uppercase text-left"
                          style={{
                            padding: "12px 18px",
                            fontSize: 10,
                            letterSpacing: "0.1em",
                            color: "var(--fg-3)",
                            fontWeight: 500,
                            borderBottom: "1px solid var(--line)",
                          }}
                        >
                          {h}
                        </th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {incorrectAttempts.slice(0, 12).map((m, i) => (
                      <tr key={`${m.questionSource}-${m.timestamp}-${i}`} style={{ borderBottom: "1px solid var(--line)" }}>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 12, color: "var(--fg)", fontWeight: 500 }}>{m.questionSource}</td>
                        <td style={{ padding: "12px 18px", fontSize: 13, color: "var(--fg-2)" }}>{TOPIC_LABELS[m.topic] || m.topic}</td>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 13, color: "var(--danger)" }}>{m.selectedAnswer || "—"}</td>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 13, color: "var(--accent)" }}>{m.correctAnswer}</td>
                        <td className="mono" style={{ padding: "12px 18px", fontSize: 12, color: "var(--fg-3)" }}>{formatRelative(m.timestamp)}</td>
                        <td style={{ padding: "12px 18px", fontSize: 12 }}>
                          <Link href={`/practice/esh/learn/${m.topic}`} style={{ color: "var(--accent)" }}>Practice →</Link>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )}
            </div>
          </>
        )}
      </section>
    </div>
  );
}
