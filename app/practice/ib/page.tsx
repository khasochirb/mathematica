import { BarChart3, BookOpen, Layers } from "lucide-react";
import IbPracticeSets from "@/components/ib/IbPracticeSets";
import { HubShell, HubHero, HubSection, HubRowLink } from "@/components/hub/HubKit";

export const metadata = { title: "IB Math Hub" };

// IB hub content is ENGLISH by design, like the SAT hub (exam realism).
//
// Structure comes from HubKit and matches the ЭЕШ and SAT hubs exactly:
// hero → tests (practice sets) → courses → practice by topic → progress.
export default function IbHubPage() {
  return (
    <HubShell>
      <HubHero
        eyebrow="IB Mathematics · Analysis & Approaches"
        title="IB Math, "
        accent="markscheme"
        titleAfter="-sharp."
        lede="The full syllabus taught code by code — booklet-flagged formulas,
          exam-format worked examples, and solutions marked the way examiners
          mark: method, accuracy, reasoning. Then full mock papers, self-marked
          against real markschemes."
      />

      <HubSection label="Practice sets">
        <div className="mono text-[11px] uppercase mb-2" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          AA SL
        </div>
        <IbPracticeSets level="sl" />
        <div className="mono text-[11px] uppercase mt-5 mb-2" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
          AA HL
        </div>
        <IbPracticeSets level="hl" />
      </HubSection>

      <HubSection label="The courses">
        <div className="space-y-3">
          <HubRowLink
            href="/math/ib-sl"
            icon={BookOpen}
            title="Standard Level (SL)"
            badge="Live"
            desc="The COMPLETE SL syllabus — all five topics, one lesson per
              subtopic code, SL 1.1 through 5.11: interactive graphs, a walkable
              unit circle, steerable distributions, and calculus you can watch
              converge."
          />
          <HubRowLink
            href="/math/ib-hl"
            icon={BookOpen}
            title="Higher Level (HL)"
            badge="Live"
            desc="The AHL extension codes on top of the SL course — proof by
              induction and contradiction, complex numbers to De Moivre, vectors
              in space, deeper calculus. Topic 1 is open; the rest land in
              syllabus order."
          />
        </div>
      </HubSection>

      <HubSection label="Practice by topic">
        <HubRowLink
          href="/practice/ib/bank"
          icon={Layers}
          title="IB topic practice"
          desc="Drill the five syllabus topics — SL and the AHL extension — with
            a similar problem queued after every miss."
        />
      </HubSection>

      <HubSection label="Your progress">
        <HubRowLink
          href="/ib-analytics"
          icon={BarChart3}
          title="Your IB progress"
          desc="Per-component accuracy and weakest areas, once you start practicing."
        />
      </HubSection>
    </HubShell>
  );
}
