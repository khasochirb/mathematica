import { notFound } from "next/navigation";
import BankBrowser from "@/components/bank/BankBrowser";
import { SAT_BANK_CHROME } from "@/components/bank/bank-chrome";
import { getSatBankTopic } from "@/lib/bank-data";
import { getBankUnit } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getSatBankTopic().units.map((u) => ({ unit: u.id }));
}

export function generateMetadata({ params }: { params: { unit: string } }) {
  const unit = getBankUnit(getSatBankTopic(), params.unit);
  return { title: unit ? `SAT Math · ${unit.title}` : "SAT Math · Topic Practice" };
}

// One SAT domain's browsable problem collection; the quiz-style runner lives
// at ./practice.
export default function SatBankUnitPage({ params }: { params: { unit: string } }) {
  const topic = getSatBankTopic();
  const unit = getBankUnit(topic, params.unit);
  if (!unit) notFound();
  return <BankBrowser topic={topic} unit={unit} chrome={SAT_BANK_CHROME} />;
}
