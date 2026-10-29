import ProblemBankHub from "@/components/bank/ProblemBankHub";
import { getBankTopics, getBankTopicMn } from "@/lib/bank-data";

// The Problem Bank index. A SERVER page so it can read the Mongolian subject
// blurbs (data/problembank-mn/<slug>.json) without the client touching the
// corpus: only a slug → blurb map crosses to ProblemBankHub, which renders
// from the ~55 KB manifest as before (lib/bank-split.test.ts guards this).
export default function ProblemBankPage() {
  const blurbMn: Record<string, string> = {};
  for (const t of getBankTopics()) {
    const mn = getBankTopicMn(t.slug);
    if (mn?.blurb) blurbMn[t.slug] = mn.blurb;
  }
  return <ProblemBankHub blurbMn={blurbMn} />;
}
