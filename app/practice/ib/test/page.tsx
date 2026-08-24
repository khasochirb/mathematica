import { HubShell, HubHeader } from "@/components/hub/HubKit";
import IbPracticeSets from "@/components/ib/IbPracticeSets";

export const metadata = { title: "IB Math — Practice sets" };

// The Tests tab's landing.
//
// Like SAT's, this route held only test/[testId]/[paper], so the tab had
// nowhere to point. The practice sets already existed as a component on
// the hub page; this gives them their own destination under the tab that
// names them, rather than making the hub page the only way in.
export default function IbTestsPage() {
  return (
    <HubShell>
      <HubHeader
        eyebrow="IB Mathematics · Analysis & Approaches"
        title="Practice sets"
        statsLine={<>AA SL and AA HL · marked to markscheme standard</>}
      />
      <div>
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
