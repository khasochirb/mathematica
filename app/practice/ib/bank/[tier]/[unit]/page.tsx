import { notFound } from "next/navigation";
import BankBrowser from "@/components/bank/BankBrowser";
import { IB_BANK_CHROME } from "@/components/bank/bank-chrome";
import { getBankUnit, getIbBankTopic, type IbBankTier } from "@/lib/problem-bank";

const TIERS: IbBankTier[] = ["sl", "hl"];

export function generateStaticParams() {
  return TIERS.flatMap((tier) =>
    getIbBankTopic(tier).units.map((u) => ({ tier, unit: u.id })),
  );
}

export function generateMetadata({ params }: { params: { tier: string; unit: string } }) {
  if (!TIERS.includes(params.tier as IbBankTier)) return { title: "IB Math · Topic Practice" };
  const unit = getBankUnit(getIbBankTopic(params.tier as IbBankTier), params.unit);
  return { title: unit ? `IB Math · ${unit.title}` : "IB Math · Topic Practice" };
}

// One syllabus topic's browsable collection; the quiz runner lives at ./practice.
export default function IbBankUnitPage({ params }: { params: { tier: string; unit: string } }) {
  if (!TIERS.includes(params.tier as IbBankTier)) notFound();
  const tier = params.tier as IbBankTier;
  const topic = getIbBankTopic(tier);
  const unit = getBankUnit(topic, params.unit);
  if (!unit) notFound();
  return <BankBrowser topic={topic} unit={unit} chrome={IB_BANK_CHROME[tier]} />;
}
