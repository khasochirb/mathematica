import { HubShell, HubHeader } from "@/components/hub/HubKit";
import SatTestList from "@/components/sat/SatTestList";
import { listSatTests } from "@/lib/sat-test";

export const metadata = { title: "SAT Math — Practice tests" };

// The Tests tab's landing.
//
// This route existed only as test/[testId], so /practice/sat/test resolved
// to nothing and lib/hub-tabs.ts had to declare the Tests tab null to stay
// honest under rule 7. The result was a hub wearing three tabs next to a
// hub wearing four — the difference the owner could see and I could not,
// because I had been comparing icons.
//
// It renders the same SatTestList the hub page does, so the list cannot
// fork into two versions of itself.
export default function SatTestsPage() {
  const tests = listSatTests();
  const first = tests[0];
  return (
    <HubShell>
      <HubHeader
        eyebrow="Digital SAT · Math"
        title="Practice tests"
        statsLine={
          <>
            <span className="tabular">{tests.length}</span> full-length adaptive{" "}
            {tests.length === 1 ? "test" : "tests"} ·{" "}
            <span className="tabular">44</span> questions each ·{" "}
            <span className="tabular">2</span> × {first.minutesPerModule} min
          </>
        }
      />
      <SatTestList />
      <p className="text-[13px] mt-8" style={{ color: "var(--fg-3)" }}>
        Calculator allowed throughout (use Desmos, like Bluebook). Every
        question ends with a full worked solution.
      </p>
    </HubShell>
  );
}
