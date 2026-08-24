
import IbPracticeSets from "@/components/ib/IbPracticeSets";
import {
  HubShell,
  HubHeader,
  HubProgressBanner,
  HubActionGrid,
  type HubActionCardDef,
} from "@/components/hub/HubKit";

export const metadata = { title: "IB Math Hub" };

// IB hub content is ENGLISH by design, like the SAT hub (exam realism).
// Built in the ЭШ hub's design idiom via components/hub/HubKit.tsx: the
// ЭШ page is the reference.
export default function IbHubPage() {
  const cards: HubActionCardDef[] = [
    {
      href: "/math/ib-sl",
      title: "Analysis & Approaches SL",
      subtitle: "The complete AA SL syllabus · 5 topics · one lesson per subtopic code",
      role: "course",
      badge: { label: "Live", tone: "accent" },
    },
    {
      href: "/math/ib-hl",
      title: "Analysis & Approaches HL",
      subtitle: "The AHL extension on top of AA SL · proof, complex numbers, 3D vectors, deeper calculus",
      role: "course",
      badge: { label: "Live", tone: "accent" },
    },
    {
      href: "/math/ib-ai-sl",
      title: "Applications & Interpretation SL",
      subtitle: "The complete AI SL syllabus · calculator-always, modelling-first · 5 topics",
      role: "course",
      badge: { label: "New", tone: "accent" },
    },
    {
      href: "/practice/ib/bank",
      title: "Practice by topic",
      subtitle: "Drill the 5 syllabus topics · a similar problem after every miss",
      role: "drill",
    },
  ];

  return (
    <HubShell>
      <HubHeader
        // The eyebrow was three clauses long and wrapped to two lines on a
        // phone, where ЭШ's is two words and SAT's is three; and the stats
        // line was a sentence where the other hubs carry counts. Same
        // header component, but it did not read as the same header.
        eyebrow="IB Mathematics · AA · AI"
        title="IB Math practice"
        statsLine={
          <>
            <span className="tabular">3</span> courses ·{" "}
            <span className="tabular">5</span> syllabus topics · practice sets
            marked to markscheme standard
          </>
        }
      />

      <HubProgressBanner
        href="/ib-analytics"
        eyebrow="Progress"
        title="Your IB performance"
        subtitle="Per-component accuracy and weakest areas, once you start practicing"
        cta="See the full report"
      />

      <HubActionGrid cards={cards} />

      <div className="mt-12">
        <div className="eyebrow mb-4">Practice sets — AA SL</div>
        <IbPracticeSets level="sl" />
      </div>
      <div className="mt-10">
        <div className="eyebrow mb-4">Practice sets — AA HL</div>
        <IbPracticeSets level="hl" />
      </div>
    </HubShell>
  );
}
