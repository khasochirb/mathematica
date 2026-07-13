import Link from "next/link";
import { ArrowRight, BarChart3, Clock, Sparkles } from "lucide-react";

export const metadata = { title: "IB Math Hub" };

// IB hub, same three-section shape as ЭЕШ and SAT: tests / weakness practice /
// study by topic. Papers aren't authored yet, so the tests section is an
// honest placeholder — but studying and progress tracking work today.
// English by design, like the SAT hub (exam realism).
export default function IbHubPage() {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="eyebrow mb-4">IB Mathematics · AA &amp; AI</div>
        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          IB Math, <em className="serif-italic" style={{ color: "var(--accent)" }}>markscheme</em>-sharp.
        </h1>
        <p className="text-[15px] mt-4" style={{ color: "var(--fg-2)", maxWidth: "52ch" }}>
          Analysis &amp; Approaches and Applications &amp; Interpretation, SL and HL —
          study the underlying math now; full practice papers with real M/A/R
          markschemes are coming.
        </p>

        <div className="eyebrow mt-10 mb-3">Practice papers</div>
        <div className="card-edit p-6" style={{ borderStyle: "dashed" }}>
          <div className="flex items-center gap-2" style={{ color: "var(--fg-1)" }}>
            <Clock className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
            <span className="serif" style={{ fontSize: 20 }}>
              Papers 1–3, IB-style — coming soon
            </span>
          </div>
          <p className="text-[13px] mt-2" style={{ color: "var(--fg-3)" }}>
            Multi-part questions marked exactly like the real exam (method,
            accuracy, and reasoning marks).
          </p>
        </div>

        <div className="eyebrow mt-10 mb-3">Practice your weaknesses</div>
        <Link
          href="/practice/ib/progress"
          className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
          style={{ display: "flex" }}
        >
          <span className="inline-flex items-center gap-2.5" style={{ color: "var(--fg-1)" }}>
            <BarChart3 className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
            <span>
              Your IB progress
              <span className="block text-[12px]" style={{ color: "var(--fg-3)" }}>
                Per-component accuracy and weakest areas, once you start practicing.
              </span>
            </span>
          </span>
          <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
        </Link>

        <div className="eyebrow mt-10 mb-3">Study by topic</div>
        <Link
          href="/math#topics"
          className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
          style={{ display: "flex" }}
        >
          <span className="inline-flex items-center gap-2.5" style={{ color: "var(--fg-1)" }}>
            <Sparkles className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
            <span>
              Full topic courses
              <span className="block text-[12px]" style={{ color: "var(--fg-3)" }}>
                Algebra 2, Precalculus, Probability &amp; Statistics, Vectors &amp;
                Matrices — the IB-tagged courses, taught from zero.
              </span>
            </span>
          </span>
          <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
        </Link>
      </div>
    </div>
  );
}
