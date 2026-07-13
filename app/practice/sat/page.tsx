import Link from "next/link";
import { ArrowRight, BarChart3, Clock, ListChecks, Sparkles } from "lucide-react";
import { listSatTests } from "@/lib/sat-test";

export const metadata = { title: "SAT Math Hub" };

// SAT hub content is ENGLISH by design — realism is the point
// (memory/expansion-vision.md §4.7). The EN/MN toggle only ever moves
// navigation chrome, never this page's content.
export default function SatHubPage() {
  const tests = listSatTests();
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="eyebrow mb-4">Digital SAT · Math</div>
        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(36px, 6vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1.0, color: "var(--fg)" }}
        >
          SAT Math, the <em className="serif-italic" style={{ color: "var(--accent)" }}>real</em> way.
        </h1>
        <p className="text-[15px] mt-4" style={{ color: "var(--fg-2)", maxWidth: "52ch" }}>
          Full-length adaptive practice tests in the exact Bluebook format:
          two 22-question modules, 35 minutes each, and your second module
          adapts to how you do on the first — just like test day.
        </p>

        <div className="eyebrow mt-10 mb-3">Practice tests</div>
        <div className="space-y-4">
          {tests.map((t) => (
            <div key={t.testId} className="card-edit p-6">
              <div className="flex items-start justify-between gap-4 flex-wrap">
                <div>
                  <div className="serif" style={{ fontSize: 22, color: "var(--fg)" }}>
                    {t.label}
                  </div>
                  <div className="flex items-center gap-4 mt-2 text-[13px]" style={{ color: "var(--fg-2)" }}>
                    <span className="inline-flex items-center gap-1.5">
                      <ListChecks className="h-3.5 w-3.5" /> 44 questions
                    </span>
                    <span className="inline-flex items-center gap-1.5">
                      <Clock className="h-3.5 w-3.5" /> 2 × {t.minutesPerModule} min
                    </span>
                    <span className="inline-flex items-center gap-1.5">
                      <Sparkles className="h-3.5 w-3.5" /> Adaptive Module 2
                    </span>
                  </div>
                </div>
                <Link href={`/practice/sat/test/${t.testId}`} className="btn btn-primary inline-flex items-center gap-1.5">
                  Start <ArrowRight className="h-4 w-4" />
                </Link>
              </div>
              <p className="text-[13px] mt-3" style={{ color: "var(--fg-3)" }}>
                Calculator allowed throughout (use Desmos, like Bluebook).
                Every question has a full worked solution at the end.
              </p>
            </div>
          ))}
        </div>

        {/* Same three-section shape as the ЭЕШ hub: tests above, then
            weakness practice, then study-by-topic into the shared courses. */}
        <div className="eyebrow mt-10 mb-3">Practice your weaknesses</div>
        <Link
          href="/practice/sat/progress"
          className="card-edit p-5 flex items-center justify-between gap-3 transition-colors hover:border-[var(--accent-line)]"
          style={{ display: "flex" }}
        >
          <span className="inline-flex items-center gap-2.5" style={{ color: "var(--fg-1)" }}>
            <BarChart3 className="h-4 w-4" style={{ color: "var(--fg-2)" }} />
            <span>
              Your SAT progress
              <span className="block text-[12px]" style={{ color: "var(--fg-3)" }}>
                Per-domain accuracy and your weakest areas, once you&apos;ve taken a test.
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
                Algebra 1 &amp; 2, Geometry, Probability &amp; Statistics — the SAT-tagged
                courses, taught from zero.
              </span>
            </span>
          </span>
          <ArrowRight className="h-4 w-4 shrink-0" style={{ color: "var(--fg-3)" }} />
        </Link>

        <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
          More practice tests and SAT-specific drills are on the way.
        </p>
      </div>
    </div>
  );
}
