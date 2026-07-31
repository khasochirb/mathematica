import { notFound } from "next/navigation";
import BankRunner from "@/components/bank/BankRunner";
import { SAT_BANK_CHROME } from "@/components/bank/bank-chrome";
import { getBankUnit, getSatBankTopic } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getSatBankTopic().units.map((u) => ({ unit: u.id }));
}

export function generateMetadata({ params }: { params: { unit: string } }) {
  const unit = getBankUnit(getSatBankTopic(), params.unit);
  return { title: unit ? `SAT Math · ${unit.title} · Practice` : "SAT Math · Topic Practice" };
}

export default function SatBankUnitPracticePage({ params }: { params: { unit: string } }) {
  const topic = getSatBankTopic();
  const unit = getBankUnit(topic, params.unit);
  if (!unit) notFound();
  return <BankRunner topic={topic} unit={unit} chrome={SAT_BANK_CHROME} />;
}
