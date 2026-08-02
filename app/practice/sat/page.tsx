import Link from "next/link";
import { ArrowRight, BarChart3, BookOpen, Clock, FileText, Layers, ListChecks, Sparkles } from "lucide-react";
import { listSatTests } from "@/lib/sat-test";
import {
  HubShell,
  HubHeader,
  HubProgressBanner,
  HubActionGrid,
  type HubActionCardDef,
} from "@/components/hub/HubKit";

export const metadata = { title: "SAT Math Hub" };

// SAT hub content is ENGLISH by design — realism is the point
// (memory/expansion-vision.md §4.7). Built in the ЭЕШ hub's design idiom
// via components/hub/HubKit.tsx: the ЭЕШ page is the reference.
export default function SatHubPage() {
  const tests = listSatTests();
  const firstTest = tests[0];

  const cards: HubActionCardDef[] = [
    {
      href: "#practice-tests",
      title: "Practice tests",
      subtitle: `Bluebook format · ${tests.length} ${tests.length === 1 ? "test" : "tests"} · 44 questions · adaptive Module 2`,
      icon: FileText,
      badge: { label: "Free", tone: "accent" },
    },
    {
      href: "/practice/sat/learn",
      title: "SAT Math course",
      subtitle: "4 College Board domains · 27 units · lessons, practice, unit tests",
      icon: Sparkles,
    },
    {
      href: "/practice/sat/bank",
      title: "Practice by topic",
      subtitle: "Drill the 4 domains · a similar problem after every miss",
      icon: Layers,
    },
    {
      href: "/math",
      title: "Foundations",
      subtitle: "General Math courses — every topic from zero",
      icon: BookOpen,
    },
  ];

  return (
    <HubShell>
      <HubHeader
        eyebrow="Digital SAT · Math"
        title="SAT Math practice"
        statsLine={
          <>
            <span className="tabular">{tests.length}</span> full-length adaptive{" "}
            {tests.length === 1 ? "test" : "tests"} ·{" "}
            <span className="tabular">44</span> questions each ·{" "}
            <span className="tabular">2</span> × {firstTest.minutesPerModule} min
          </>
        }
      />

      <HubProgressBanner
        href="/sat-analytics"
        icon={BarChart3}
        eyebrow="Progress"
        title="Your SAT performance"
        subtitle="Per-domain accuracy and your weakest areas, once you've taken a test"
        cta="See the full report"
      />

      <HubActionGrid cards={cards} />

      {/* The full test list — every paper, one Start each. */}
      <div className="mt-12" id="practice-tests">
        <div className="eyebrow mb-4">Practice tests · {tests.length}</div>
        <div style={{ border: "1px solid var(--line)", borderRadius: 12, overflow: "hidden" }}>
          {tests.map((t, i) => (
            <Link
              key={t.testId}
              href={`/practice/sat/test/${t.testId}`}
              className="flex items-center gap-4 px-5 py-3.5 transition-colors hover:opacity-90 group"
              style={{
                background: "var(--bg-1)",
                borderTop: i === 0 ? "none" : "1px solid var(--line)",
              }}
            >
              <span
                className="badge-edit"
                style={{
                  minWidth: 44,
                  justifyContent: "center",
                  color: "var(--accent)",
                  borderColor: "var(--accent-line)",
                  background: "var(--accent-wash)",
                }}
              >
                {String(i + 1).padStart(2, "0")}
              </span>
              <div className="flex-1 min-w-0">
                <div className="text-[14px]" style={{ color: "var(--fg)" }}>
                  {t.label}
                </div>
                <div className="flex items-center gap-3 mono text-[11px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                  <span className="inline-flex items-center gap-1">
                    <ListChecks className="h-3 w-3" /> 44 questions
                  </span>
                  <span className="inline-flex items-center gap-1">
                    <Clock className="h-3 w-3" /> 2 × {t.minutesPerModule} min
                  </span>
                </div>
              </div>
              <span
                className="mono text-[11px] uppercase shrink-0 inline-flex items-center gap-1"
                style={{ color: "var(--accent)", letterSpacing: "0.06em" }}
              >
                Start
                <ArrowRight className="w-3.5 h-3.5 transition-transform group-hover:translate-x-0.5" />
              </span>
            </Link>
          ))}
        </div>
      </div>

      <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
        Calculator allowed throughout (use Desmos, like Bluebook). Every
        question ends with a full worked solution.
      </p>
    </HubShell>
  );
}
