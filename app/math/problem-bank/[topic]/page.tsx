import { notFound } from "next/navigation";
import BankBrowser from "@/components/bank/BankBrowser";
import { getBankTopic, getBankTopics } from "@/lib/problem-bank";

export function generateStaticParams() {
  return getBankTopics().map((t) => ({ topic: t.slug }));
}

export function generateMetadata({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  return { title: topic ? `Problem Bank · ${topic.title}` : "Problem Bank" };
}

// The topic's browsable problem book — every problem on one page. The
// quiz-style runner (instant feedback + miss→similar retry) lives at
// ./practice, linked from the top of the list.
export default function BankTopicPage({ params }: { params: { topic: string } }) {
  const topic = getBankTopic(params.topic);
  if (!topic) notFound();
  return <BankBrowser topic={topic} />;
}
