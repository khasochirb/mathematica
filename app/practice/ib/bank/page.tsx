import Link from "next/link";
import { ArrowLeft, ArrowRight, Layers } from "lucide-react";
import { getIbBankTopic } from "@/lib/bank-data";

export const metadata = { title: "IB Math · Topic Practice" };

// The IB hub's topic-focused practice branch (resource blueprint: every hub
// offers Tests · Courses · Topic practice in ITS OWN taxonomy — here the five
// syllabus topics, split SL / AHL-extension exactly like the live courses).
export default function IbBankPage() {
  const tiers = [
    {
      tier: "sl" as const,
      label: "Standard Level (SL)",
      note: "The SL syllabus drilled by topic — sequences to calculus at Paper 1/2 short-question difficulty. HL students master this bank too.",
    },
    {
      tier: "hl" as const,
      label: "Higher Level (AHL extension)",
      note: "The HL-only material — complex numbers, polynomial theorems, vectors, Bayes and harder calculus — on top of the SL bank.",
    },
  ];
  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/practice/ib" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">IB Math · Topic practice</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
          Topic practice
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "58ch" }}>
          Every exam form across the five syllabus topics, organized like the
          courses. Work a unit&apos;s collection as an exercise set, or run it as
          a practice set where a miss immediately queues a similar problem.
          You enter an answer and it gets checked — the worked solution opens
          after that, never before.
        </p>

        <div className="space-y-3">
          {tiers.map(({ tier, label, note }) => {
            const t = getIbBankTopic(tier);
            const problems = t.forms.reduce((n, f) => n + f.variants.length, 0);
            return (
              <Link
                key={tier}
                href={`/practice/ib/bank/${tier}`}
                className="card-edit p-5 flex items-start gap-4 transition-colors"
                style={{ textDecoration: "none" }}
              >
                <Layers className="h-4 w-4 mt-1.5 flex-shrink-0" style={{ color: "var(--accent)" }} />
                <div className="flex-1 min-w-0">
                  <span className="serif" style={{ fontWeight: 400, fontSize: 19, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                    {label}
                  </span>
                  <p className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{note}</p>
                  <div className="mt-2 flex items-center gap-2 flex-wrap text-[11px] mono" style={{ color: "var(--fg-3)" }}>
                    <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
                      {t.units.length} topics
                    </span>
                    <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
                      {t.forms.length} forms
                    </span>
                    <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
                      {problems} problems
                    </span>
                  </div>
                </div>
                <ArrowRight className="h-4 w-4 flex-shrink-0 mt-1.5" style={{ color: "var(--fg-3)" }} />
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
