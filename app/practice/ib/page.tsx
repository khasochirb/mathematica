import Link from "next/link";
import { ArrowRight, BarChart3, BookOpen } from "lucide-react";
import IbPracticeSets from "@/components/ib/IbPracticeSets";

export const metadata = { title: "IB Math Hub" };

// IB hub: courses first (the SL class is live), then papers (coming), then
// progress. English by design, like the SAT hub (exam realism).
export default function IbHubPage() {
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="eyebrow mb-4">IB Mathematics · Analysis &amp; Approaches</div>
        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          IB Math, <em className="serif-italic" style={{ color: "var(--accent)" }}>markscheme</em>-sharp.
        </h1>
        <p className="text-[15px] mt-4" style={{ color: "var(--fg-2)", maxWidth: "52ch" }}>
          The full syllabus taught code by code — booklet-flagged formulas,
          exam-format worked examples, and solutions marked the way examiners
          mark: method, accuracy, reasoning. Then full mock papers, self-marked
          against real markschemes.
        </p>

        <div className="eyebrow mt-10 mb-3">The courses</div>
        <div className="space-y-3">
          <Link
            href="/math/ib-sl"
            className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
            style={{ display: "flex" }}
          >
            <span className="inline-flex items-start gap-2.5" style={{ color: "var(--fg-1)" }}>
              <BookOpen className="h-4 w-4 mt-1" style={{ color: "var(--accent)" }} />
              <span>
                <span className="serif" style={{ fontSize: 20, color: "var(--fg)" }}>
                  Standard Level (SL)
                </span>
                <span className="mono text-[10px] uppercase ml-2 px-1.5 py-0.5 rounded" style={{ color: "var(--accent)", border: "1px solid var(--accent-line)", letterSpacing: "0.08em" }}>
                  Live
                </span>
                <span className="block text-[12px] mt-1" style={{ color: "var(--fg-3)" }}>
                  The COMPLETE SL syllabus — all five topics, one lesson per
                  subtopic code, SL 1.1 through 5.11: interactive graphs, a
                  walkable unit circle, steerable distributions, and calculus
                  you can watch converge.
                </span>
              </span>
            </span>
            <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
          </Link>
          <Link
            href="/math/ib-hl"
            className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
            style={{ display: "flex" }}
          >
            <span className="inline-flex items-start gap-2.5" style={{ color: "var(--fg-1)" }}>
              <BookOpen className="h-4 w-4 mt-1" style={{ color: "var(--accent)" }} />
              <span>
                <span className="serif" style={{ fontSize: 20, color: "var(--fg)" }}>
                  Higher Level (HL)
                </span>
                <span className="mono text-[10px] uppercase ml-2 px-1.5 py-0.5 rounded" style={{ color: "var(--accent)", border: "1px solid var(--accent-line)", letterSpacing: "0.08em" }}>
                  Live
                </span>
                <span className="block text-[12px] mt-1" style={{ color: "var(--fg-3)" }}>
                  The AHL extension codes on top of the SL course — proof by
                  induction and contradiction, complex numbers to De Moivre,
                  vectors in space, deeper calculus. Topic 1 is open; the rest
                  land in syllabus order.
                </span>
              </span>
            </span>
            <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
          </Link>
        </div>

        <div className="eyebrow mt-10 mb-3">Practice sets — AA SL</div>
        <IbPracticeSets />

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

      </div>
    </div>
  );
}
