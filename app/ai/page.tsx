"use client";

import { useState, type ReactNode } from "react";
import usePerformance from "@/lib/use-performance";

const TOPICS = [
  { n: "Definite integration", v: 38, weak: true },
  { n: "Sequences · limits", v: 41, weak: true },
  { n: "Complex numbers", v: 48, weak: true },
  { n: "Vectors · 3D", v: 62, weak: false },
];

const STEPS: { n: string; t: ReactNode }[] = [
  {
    n: "01",
    t: (
      <>
        Notice something special: <span className="q-math">2x</span> is the derivative of{" "}
        <span className="q-math">x²</span>. That&apos;s a hint to substitute!
      </>
    ),
  },
  {
    n: "02",
    t: (
      <>
        Let <span className="q-math">u = x²</span>. Then <span className="q-math">du = 2x dx</span>. The integral
        becomes <span className="q-math">∫cos(u) du</span>.
      </>
    ),
  },
  {
    n: "03",
    t: (
      <>
        Change the limits: when <span className="q-math">x = 0</span>, <span className="q-math">u = 0</span>. When{" "}
        <span className="q-math">x = √π</span>, <span className="q-math">u = π</span>.
      </>
    ),
  },
  {
    n: "04",
    t: (
      <>
        So we want{" "}
        <span className="q-math">
          ∫₀^π cos(u) du = sin(π) − sin(0) = 0 − 0 ={" "}
          <strong style={{ color: "var(--accent)" }}>0</strong>
        </span>
        .
      </>
    ),
  },
  {
    n: "✓",
    t: (
      <>
        <strong style={{ color: "var(--accent)" }}>Lesson:</strong> When you see{" "}
        <span className="q-math">f(x)</span> multiplied by the derivative of the &ldquo;inside,&rdquo; substitution
        is almost always the trick.
      </>
    ),
  },
];

const inputStyle: React.CSSProperties = {
  background: "var(--bg-1)",
  border: "1px solid var(--line)",
  borderRadius: 8,
  color: "var(--fg)",
  padding: "9px 12px",
  fontSize: 13,
  fontFamily: "var(--font-mono)",
  outline: "none",
};

export default function AITutorPage() {
  const perf = usePerformance();
  const overall = perf.getOverallStats();
  const [activeTopic, setActiveTopic] = useState(0);
  const [showSteps, setShowSteps] = useState(false);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState<{ msg: string; ok?: boolean } | null>({
    msg: "Try the answer as a number (e.g. 0, π, 2π) or press Explain.",
  });
  const [count, setCount] = useState(5);

  const onCheck = () => {
    const v = answer.trim().toLowerCase();
    const ok = ["0", "zero", "тэг"].includes(v);
    if (ok) {
      setFeedback({ msg: "✓ Correct. The substitution brings this to 0 cleanly.", ok: true });
      setShowSteps(true);
    } else {
      setFeedback({ msg: "✗ Not quite — try a substitution. Open the explanation?", ok: false });
    }
  };

  return (
    <div
      className="grid pt-16"
      style={{
        gridTemplateColumns: "minmax(0, 300px) minmax(0, 1fr) minmax(0, 340px)",
        minHeight: "calc(100vh - 4rem)",
      }}
    >
      {/* LEFT: topics */}
      <aside
        className="hidden lg:block sticky overflow-y-auto"
        style={{
          top: 64,
          alignSelf: "start",
          height: "calc(100vh - 64px)",
          padding: "28px 20px",
          borderRight: "1px solid var(--line)",
        }}
      >
        <div className="eyebrow" style={{ marginBottom: 14 }}>
          Weak topics · AI prioritized
        </div>
        <div className="grid gap-2" style={{ gridTemplateColumns: "1fr 1fr" }}>
          {TOPICS.map((t, i) => {
            const active = activeTopic === i;
            return (
              <button
                key={t.n}
                onClick={() => setActiveTopic(i)}
                className="rounded-md flex justify-between items-center text-left text-[13px]"
                style={{
                  padding: "10px 12px",
                  border: `1px solid ${active ? "var(--accent-line)" : "var(--line)"}`,
                  background: active ? "var(--accent-wash)" : "transparent",
                  color: active ? "var(--accent)" : "var(--fg)",
                  cursor: "pointer",
                }}
              >
                <span>{t.n}</span>
                <span
                  className="mono"
                  style={{
                    fontSize: 11,
                    color: active ? "var(--accent)" : t.weak ? "var(--warn)" : "var(--fg-3)",
                  }}
                >
                  {t.v}%
                </span>
              </button>
            );
          })}
        </div>

        <div className="mt-5 pt-4" style={{ borderTop: "1px solid var(--line)" }}>
          <div className="eyebrow" style={{ marginBottom: 10 }}>
            All topics
          </div>
          <div className="grid gap-1 text-[13px]" style={{ color: "var(--fg-1)" }}>
            {[
              { n: "Functions & graphs", v: "92%" },
              { n: "Algebra · polynomials", v: "95%" },
              { n: "Trigonometry", v: "84%" },
              { n: "Probability", v: "72%" },
            ].map((t) => (
              <div key={t.n} className="flex justify-between py-1.5 px-1">
                <span>{t.n}</span>
                <span className="mono" style={{ color: "var(--fg-3)" }}>
                  {t.v}
                </span>
              </div>
            ))}
          </div>
        </div>
      </aside>

      {/* CENTER */}
      <section className="px-6 md:px-12 py-10 md:py-12 min-w-0">
        {/* Head */}
        <div
          className="flex justify-between items-end pb-6 mb-7"
          style={{ borderBottom: "1px solid var(--line)" }}
        >
          <div>
            <div className="eyebrow">{TOPICS[activeTopic].n} · 5 problems</div>
            <h1
              className="serif"
              style={{
                fontWeight: 400,
                fontSize: "clamp(32px, 4vw, 44px)",
                letterSpacing: "-0.03em",
                margin: "6px 0 0",
              }}
            >
              {TOPICS[activeTopic].n}
            </h1>
          </div>
          <div className="flex gap-2.5 items-center">
            <span className="badge-edit badge-accent live-dot">AI · GENERATING</span>
            <button className="btn btn-line">↻ Regenerate</button>
          </div>
        </div>

        {/* Problem 1 */}
        <div className="card-edit p-7 md:p-9 mb-4">
          <div
            className="flex justify-between items-center mb-4 mono uppercase"
            style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.1em" }}
          >
            <span>
              PROBLEM <strong style={{ color: "var(--accent)" }}>02</strong> / 05
            </span>
            <span>HARD · CONCEPT</span>
          </div>
          <p
            className="serif leading-snug mb-5"
            style={{ fontSize: 26, letterSpacing: "-0.01em", color: "var(--fg)" }}
          >
            If <span className="q-math">f(x) = 2x · cos(x²)</span>, evaluate{" "}
            <span className="q-math">∫₀^√π f(x) dx</span>.
          </p>

          <div className="flex gap-4 flex-wrap">
            <button onClick={() => setShowSteps((s) => !s)} className="btn btn-line">
              {showSteps ? "Hide explanation" : "Explain like I'm 10"}
            </button>
            <button className="btn btn-line">↑ Upload my solution</button>
            <button className="btn btn-ghost">Give me a hint</button>
          </div>

          <div className="flex gap-2 mt-5 items-center">
            <input
              type="text"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && onCheck()}
              placeholder="Your answer..."
              className="flex-1"
              style={inputStyle}
            />
            <button onClick={onCheck} className="btn btn-primary">
              Check
            </button>
          </div>
          {feedback && (
            <div
              className="mono mt-2.5"
              style={{
                fontSize: 12,
                color:
                  feedback.ok === undefined
                    ? "var(--fg-3)"
                    : feedback.ok
                      ? "var(--accent)"
                      : "var(--danger)",
              }}
            >
              {feedback.msg}
            </div>
          )}

          {showSteps && (
            <div className="mt-5 pt-5" style={{ borderTop: "1px solid var(--line)" }}>
              <div
                className="mono uppercase mb-3.5"
                style={{ fontSize: 10, letterSpacing: "0.1em", color: "var(--accent)" }}
              >
                Step-by-step · 5th-grade explanation
              </div>
              {STEPS.map((s) => (
                <div
                  key={s.n}
                  className="grid gap-3 py-2 text-sm"
                  style={{ gridTemplateColumns: "28px 1fr", color: "var(--fg-1)" }}
                >
                  <div className="mono" style={{ color: "var(--accent)", fontSize: 11, paddingTop: 2 }}>
                    {s.n}
                  </div>
                  <div>{s.t}</div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Problem 2 (preview) */}
        <div className="card-edit p-7 md:p-9 mb-4" style={{ opacity: 0.55 }}>
          <div
            className="flex justify-between items-center mb-4 mono uppercase"
            style={{ fontSize: 11, color: "var(--fg-2)", letterSpacing: "0.1em" }}
          >
            <span>
              PROBLEM <strong>03</strong> / 05
            </span>
            <span>HARD · APPLICATION</span>
          </div>
          <p
            className="serif leading-snug"
            style={{ fontSize: 26, letterSpacing: "-0.01em", color: "var(--fg)" }}
          >
            Find the area enclosed between <span className="q-math">y = x²</span> and{" "}
            <span className="q-math">y = x + 2</span>.
          </p>
          <div
            className="mono mt-3 flex items-center gap-2 live-dot"
            style={{ fontSize: 13, color: "var(--fg-2)" }}
          >
            Solution streaming...
          </div>
        </div>

        {/* Generate panel */}
        <div
          className="mt-7 p-6"
          style={{
            border: "1px dashed var(--line-strong)",
            borderRadius: 14,
          }}
        >
          <h3
            className="serif mb-3.5"
            style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em" }}
          >
            Generate another set
          </h3>
          <p className="mb-3 text-[13px]" style={{ color: "var(--fg-2)" }}>
            3–5 fresh problems · seeded from real ЭЕШ patterns · explanations in{" "}
            <strong>Mongolian</strong>.
          </p>
          {[
            {
              lbl: "Topic" as ReactNode,
              el: (
                <select style={{ ...inputStyle, width: "auto" }}>
                  <option>Definite integration</option>
                  <option>Sequences · limits</option>
                  <option>Complex numbers</option>
                </select>
              ),
            },
            {
              lbl: "Difficulty" as ReactNode,
              el: (
                <select style={{ ...inputStyle, width: "auto" }}>
                  <option>Match my level (Hard)</option>
                  <option>Easier (Medium)</option>
                  <option>Harder (Very Hard)</option>
                </select>
              ),
            },
            {
              lbl: (
                <>
                  Count · <span className="mono">{count}</span>
                </>
              ) as ReactNode,
              el: (
                <input
                  type="range"
                  min={3}
                  max={5}
                  value={count}
                  onChange={(e) => setCount(+e.target.value)}
                  style={{ ...inputStyle, width: 200 }}
                />
              ),
            },
            {
              lbl: "Explanation depth" as ReactNode,
              el: (
                <select style={{ ...inputStyle, width: "auto" }}>
                  <option>5th-grade (step-by-step)</option>
                  <option>High-school</option>
                  <option>University</option>
                </select>
              ),
            },
          ].map((row, i) => (
            <div
              key={i}
              className="flex justify-between items-center my-2.5 text-[13px]"
              style={{ color: "var(--fg-2)" }}
            >
              <span>{row.lbl}</span>
              {row.el}
            </div>
          ))}
          <button className="btn btn-primary mt-2.5">Generate {count} problems</button>
        </div>
      </section>

      {/* RIGHT */}
      <aside
        className="hidden xl:block sticky overflow-y-auto"
        style={{
          top: 64,
          alignSelf: "start",
          height: "calc(100vh - 64px)",
          padding: "28px 20px",
          borderLeft: "1px solid var(--line)",
          background: "var(--bg-1)",
        }}
      >
        <div className="eyebrow">Session</div>
        <div className="serif mt-1.5 mb-4" style={{ fontSize: 24, letterSpacing: "-0.02em" }}>
          Integration drill
        </div>

        <div
          className="grid gap-1.5 py-3.5 text-[13px]"
          style={{ borderTop: "1px solid var(--line)", borderBottom: "1px solid var(--line)" }}
        >
          {[
            { k: "Problems solved", v: "1 / 5" },
            { k: "Time elapsed", v: "12:44" },
            { k: "Credits used", v: `${Math.min(50, overall.total + 3)} / 50` },
          ].map((r) => (
            <div key={r.k} className="flex justify-between">
              <span style={{ color: "var(--fg-2)" }}>{r.k}</span>
              <span className="mono">{r.v}</span>
            </div>
          ))}
        </div>

        <div className="eyebrow mt-7">Suggested next</div>
        <div className="grid gap-2 mt-2.5">
          {[
            { t: "Sequences · limits drill", meta: "5 problems · 41% mastery" },
            { t: "Complex numbers review", meta: "3 problems · 48% mastery" },
          ].map((s) => (
            <div key={s.t} className="card-edit p-3.5 text-[13px]">
              <div style={{ color: "var(--fg)", fontWeight: 500 }}>{s.t}</div>
              <div className="mt-0.5" style={{ color: "var(--fg-2)", fontSize: 12 }}>
                {s.meta}
              </div>
            </div>
          ))}
        </div>

        <div className="eyebrow mt-7">Sources</div>
        <div
          className="mono mt-1.5"
          style={{ fontSize: 11, color: "var(--fg-3)", lineHeight: 1.8 }}
        >
          ЭЕШ 2024 · PROBLEM 23
          <br />
          ЭЕШ 2022 · PROBLEM 19
          <br />
          SPIVAK · CH 14 §3
          <br />
          THOMAS · 5.6
        </div>
      </aside>
    </div>
  );
}
