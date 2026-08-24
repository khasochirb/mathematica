import Link from "next/link";
import { listSatTests } from "@/lib/sat-test";
import SatTestList from "@/components/sat/SatTestList";
import {
  HubShell,
  HubHeader,
  HubProgressBanner,
  HubActionGrid,
  type HubActionCardDef,
} from "@/components/hub/HubKit";

export const metadata = { title: "SAT Math Hub" };

// SAT hub content is ENGLISH by design — realism is the point
// (memory/expansion-vision.md §4.7). Built in the ЭШ hub's design idiom
// via components/hub/HubKit.tsx: the ЭШ page is the reference.
export default function SatHubPage() {
  const tests = listSatTests();
  const firstTest = tests[0];

  const cards: HubActionCardDef[] = [
    {
      // Points at the Tests tab landing, like ЭШ's tests card does,
      // rather than scroll-jumping to an anchor further down itself.
      href: "/practice/sat/test",
      title: "Practice tests",
      subtitle: `Bluebook format · ${tests.length} ${tests.length === 1 ? "test" : "tests"} · 44 questions · adaptive Module 2`,
      role: "tests",
      badge: { label: "Free", tone: "accent" },
    },
    {
      href: "/practice/sat/learn",
      title: "SAT Math course",
      subtitle: "4 College Board domains · 27 units · lessons, practice, unit tests",
      role: "course",
    },
    {
      href: "/practice/sat/bank",
      title: "Practice by topic",
      subtitle: "Drill the 4 domains · a similar problem after every miss",
      role: "drill",
    },
    {
      href: "/math",
      title: "Foundations",
      subtitle: "General Math courses — every topic from zero",
      role: "foundations",
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
        eyebrow="Progress"
        title="Your SAT performance"
        subtitle="Per-domain accuracy and your weakest areas, once you've taken a test"
        cta="See the full report"
      />

      <HubActionGrid cards={cards} />

      {/* The full test list — every paper, one Start each. */}
      <div className="mt-12" id="practice-tests">
        <div className="eyebrow mb-4">Practice tests · {tests.length}</div>
        <SatTestList />
      </div>

      <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
        Calculator allowed throughout (use Desmos, like Bluebook). Every
        question ends with a full worked solution.
      </p>
    </HubShell>
  );
}
