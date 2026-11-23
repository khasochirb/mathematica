import ContentGate from "@/components/genmath/ContentGate";
import { isBankUnitFree } from "@/lib/course-access";
import type { BankTopic } from "@/lib/problem-bank";

// The ONE wall in front of bank content. Every bank unit page and every bank
// practice page renders through this, so the sign-in wall has a single
// implementation across all three surfaces — /math/problem-bank, the SAT
// hub's bank and the IB hub's bank. lib/course-access.test.ts pins that no
// bank content route slips past it.
//
// A server component on purpose: it resolves the policy at render time and
// hands the client gate a plain boolean, so the corpus never travels just to
// answer "is this free?".
export default function BankGate({
  topic,
  unitId,
  backHref,
  children,
}: {
  topic: BankTopic;
  unitId: string;
  /** The bank's unit list — where the gate's back link goes. */
  backHref: string;
  children: React.ReactNode;
}) {
  const free = isBankUnitFree(
    topic.slug,
    unitId,
    topic.units.map((u) => u.id),
  );

  return (
    <ContentGate
      free={free}
      backHref={backHref}
      backLabel="Back to the unit list"
    >
      {children}
    </ContentGate>
  );
}
