import ContentGate from "@/components/genmath/ContentGate";
import { isBankUnitFree } from "@/lib/course-access";
import type { BankTopic } from "@/lib/problem-bank";

// The ONE wall in front of bank content. Every bank unit page and every bank
// practice page renders through this, so the paywall has a single
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
      upgradeSource="bank_content_lock"
      premiumBody={{
        en: "The first unit of every subject is free. Premium opens the whole bank — every unit, every problem type, and the practice sets that bring a similar problem back when you miss one.",
        mn: "Хичээл бүрийн эхний бүлэг үнэгүй. Премиум эрх нь бүх бүлэг, бүх төрлийн бодлого, мөн алдсан үед ижил төстэй бодлогыг эргүүлж өгдөг дасгалын багцыг нээнэ.",
      }}
    >
      {children}
    </ContentGate>
  );
}
