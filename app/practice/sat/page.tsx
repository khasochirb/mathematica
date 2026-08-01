import Link from "next/link";
import { ArrowRight, BarChart3, Clock, Layers, ListChecks, Sparkles } from "lucide-react";
import { listSatTests } from "@/lib/sat-test";
import { HubShell, HubHero, HubSection, HubRowLink } from "@/components/hub/HubKit";

export const metadata = { title: "SAT Math Hub" };

// SAT hub content is ENGLISH by design — realism is the point
// (memory/expansion-vision.md §4.7). The EN/MN toggle only ever moves
// navigation chrome, never this page's content.
//
// Structure comes from HubKit and matches the ЭЕШ and IB hubs exactly:
// hero → tests → course → practice by topic → progress.
export default function SatHubPage() {
  const tests = listSatTests();
  return (
    <HubShell>
      <HubHero
        eyebrow="Digital SAT · Math"
        title="SAT Math, the "
        accent="real"
        titleAfter=" way."
        lede="Full-length adaptive practice tests in the exact Bluebook format:
          two 22-question modules, 35 minutes each, and your second module
          adapts to how you do on the first — just like test day."
        statsLine={
          <>
            <span className="tabular">{tests.length}</span> full-length adaptive{" "}
            {tests.length === 1 ? "test" : "tests"} ·{" "}
            <span className="tabular">44</span> questions each
          </>
        }
      />

      <HubSection label="Practice tests">
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
      </HubSection>

      <HubSection label="The course">
        <HubRowLink
          href="/practice/sat/learn"
          icon={Sparkles}
          title="SAT Math course"
          desc="Four courses, one per College Board domain — Algebra, Advanced
            Math, Problem-Solving & Data, Geometry & Trig — lessons, practice
            and unit tests, weighted like the real section."
        />
      </HubSection>

      <HubSection label="Practice by topic">
        <HubRowLink
          href="/practice/sat/bank"
          icon={Layers}
          title="SAT topic practice"
          desc="Drill the four SAT domains — Algebra, Advanced Math,
            Problem-Solving & Data, Geometry & Trig — with a similar problem
            queued after every miss."
        />
      </HubSection>

      <HubSection label="Your progress">
        <HubRowLink
          href="/sat-analytics"
          icon={BarChart3}
          title="Your SAT progress"
          desc="Per-domain accuracy and your weakest areas, once you've taken a test."
        />
      </HubSection>

      <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
        More practice tests are on the way. Need the fundamentals first? The{" "}
        <Link href="/math#topics" style={{ color: "var(--accent)" }}>
          General Math courses
        </Link>{" "}
        teach every topic from zero.
      </p>
    </HubShell>
  );
}
