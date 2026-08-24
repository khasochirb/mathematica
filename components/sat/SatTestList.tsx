import Link from "next/link";
import { ArrowRight, Clock, ListChecks } from "lucide-react";
import { listSatTests } from "@/lib/sat-test";

// The full SAT paper list — every test, one Start each.
//
// Extracted from the SAT hub page so the hub section and the Tests tab
// landing (/practice/sat/test) render the SAME list rather than two that
// drift. The hub previously owned this markup inline, which is exactly
// how the hubs came to disagree about everything else.
export default function SatTestList() {
  const tests = listSatTests();
  return (
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
  );
}
