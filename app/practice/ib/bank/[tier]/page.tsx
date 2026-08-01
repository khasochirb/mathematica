import { notFound } from "next/navigation";
import BankUnitList from "@/components/bank/BankUnitList";
import { IB_BANK_CHROME } from "@/components/bank/bank-chrome";
import { getIbBankTopic, type IbBankTier } from "@/lib/bank-data";

const TIERS: IbBankTier[] = ["sl", "hl"];

export function generateStaticParams() {
  return TIERS.map((tier) => ({ tier }));
}

export function generateMetadata({ params }: { params: { tier: string } }) {
  return {
    title: params.tier === "hl" ? "IB Math HL · Topic Practice" : "IB Math SL · Topic Practice",
  };
}

export default function IbBankTierPage({ params }: { params: { tier: string } }) {
  if (!TIERS.includes(params.tier as IbBankTier)) notFound();
  const tier = params.tier as IbBankTier;
  return <BankUnitList topic={getIbBankTopic(tier)} chrome={IB_BANK_CHROME[tier]} />;
}
