import { notFound } from "next/navigation";
import BankRunner from "@/components/bank/BankRunner";
import { getBankTopic, getBankTopics, getBankUnit } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getBankTopics().flatMap((t) =>
    t.units.map((u) => ({ topic: t.slug, unit: u.id })),
  );
}

export function generateMetadata({ params }: { params: { topic: string; unit: string } }) {
  const topic = getBankTopic(params.topic);
  const unit = topic ? getBankUnit(topic, params.unit) : null;
  return {
    title:
      topic && unit
        ? `Problem Bank · ${unit.title} · Practice`
        : "Problem Bank",
  };
}

export default function BankUnitPracticePage({ params }: { params: { topic: string; unit: string } }) {
  const topic = getBankTopic(params.topic);
  if (!topic) notFound();
  const unit = getBankUnit(topic, params.unit);
  if (!unit) notFound();
  return <BankRunner topic={topic} unit={unit} />;
}
