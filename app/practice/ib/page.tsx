import { BarChart3, BookOpen, Layers } from "lucide-react";
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
// Built in the ЭЕШ hub's design idiom via components/hub/HubKit.tsx: the
// ЭЕШ page is the reference.
export default function IbHubPage() {
  const cards: HubActionCardDef[] = [
    {
      href: "/math/ib-sl",
      title: "Analysis & Approaches SL",
      subtitle: "The complete AA SL syllabus · 5 topics · one lesson per subtopic code",
      icon: BookOpen,
      badge: { label: "Live", tone: "accent" },
    },
    {
      href: "/math/ib-hl",
      title: "Analysis & Approaches HL",
      subtitle: "The AHL extension on top of AA SL · proof, complex numbers, 3D vectors, deeper calculus",
      icon: BookOpen,
      badge: { label: "Live", tone: "accent" },
    },
    {
      href: "/math/ib-ai-sl",
      title: "Applications & Interpretation SL",
      subtitle: "The other IB track — calculator-always, modelling-first · Topics 1–4 open",
      icon: BookOpen,
      badge: { label: "New", tone: "accent" },
    },
    {
      href: "/practice/ib/bank",
      title: "Practice by topic",
      subtitle: "Drill the 5 syllabus topics · a similar problem after every miss",
      icon: Layers,
    },
  ];

  return (
    <HubShell>
      <HubHeader
        eyebrow="IB Mathematics · Analysis & Approaches · Applications & Interpretation"
        title="IB Math practice"
        statsLine={
          <>
            AA SL + HL and AI SL courses · topic drills · practice sets
            marked to markscheme standard
          </>
        }
      />

      <HubProgressBanner
        href="/ib-analytics"
        icon={BarChart3}
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
