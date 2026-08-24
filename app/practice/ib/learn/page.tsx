import { HubShell, HubHeader, HubActionGrid, type HubActionCardDef } from "@/components/hub/HubKit";

export const metadata = { title: "IB Math — Courses" };

// The Learn tab's landing.
//
// The three IB courses were reachable only from cards on the hub page, so
// the Learn tab had nowhere to point and IB rendered fewer tabs than the
// other hubs. Same cards, same roles, same grid — the tab now has a
// destination inside its own hub, which lib/hub-tabs.test.ts requires.
const COURSES: HubActionCardDef[] = [
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
    subtitle:
      "The AHL extension on top of AA SL · proof, complex numbers, 3D vectors, deeper calculus",
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
    href: "/math",
    title: "Foundations",
    subtitle: "General Math courses — every topic from zero",
    role: "foundations",
  },
];

export default function IbLearnPage() {
  return (
    <HubShell>
      <HubHeader
        eyebrow="IB Mathematics · AA · AI"
        title="IB Math courses"
        statsLine={
          <>
            <span className="tabular">3</span> courses · AA SL · AA HL · AI SL ·
            one lesson per subtopic code
          </>
        }
      />
      <HubActionGrid cards={COURSES} />
    </HubShell>
  );
}
