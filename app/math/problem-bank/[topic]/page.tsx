import { notFound } from "next/navigation";
import BankUnitList from "@/components/bank/BankUnitList";
import { getBankTopic, getBankTopics } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getBankTopics().map((t) => ({ topic: t.slug }));
}

export function generateMetadata({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  return { title: topic ? `Problem Bank · ${topic.title}` : "Problem Bank" };
}

// The subject page: the course's units in taught order — click a unit to open
// its problem collection.
export default function BankTopicPage({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  if (!topic) notFound();
  return <BankUnitList topic={topic} />;
}
