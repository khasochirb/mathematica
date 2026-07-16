import { notFound } from "next/navigation";
import BankBrowser from "@/components/bank/BankBrowser";
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
        ? `Problem Bank · ${topic.title} · ${unit.title}`
        : "Problem Bank",
  };
}

// The unit's browsable problem collection — every problem for this course
// unit on one page. The quiz-style runner lives at ./practice.
export default function BankUnitPage({ params }: { params: { topic: string; unit: string } }) {
  const topic = getBankTopic(params.topic);
  if (!topic) notFound();
  const unit = getBankUnit(topic, params.unit);
  if (!unit) notFound();
  return <BankBrowser topic={topic} unit={unit} />;
}
