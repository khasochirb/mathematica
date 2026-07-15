import { notFound } from "next/navigation";
import BankRunner from "@/components/bank/BankRunner";
import { getBankTopic, getBankTopics } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getBankTopics().map((t) => ({ topic: t.slug }));
}

export function generateMetadata({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  return { title: topic ? `Problem Bank · ${topic.title} · Practice` : "Problem Bank" };
}

export default function BankPracticePage({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  if (!topic) notFound();
  return <BankRunner topic={topic} />;
}
