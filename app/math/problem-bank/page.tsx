import ProblemBankHub from "@/components/bank/ProblemBankHub";
import { getBankTopics, getBankTopicMn } from "@/lib/bank-data";

// Grades 2–4 have no Mongolian bank mirror (data/problembank-mn/), so their
// blurbs live here, written on the pattern of the mirrored grades' blurbs
// («6-р ангийн бүх бүлгийн дасгал: …»). NEW Oct 2026, awaiting Khas. A
// mirror's own blurb, once one exists, takes precedence.
const BLURB_MN_FALLBACK: Record<string, string> = {
  "2": "2-р ангийн бүх бүлгийн дасгал: 1000 хүртэлх тоо, дөрвөн үйлдэл, анхны бутархай, дүрс, хэмжилт ба өгөгдөл. Бүлэг бүр өөрийн бодлогын цуглуулгатай.",
  "3": "3-р ангийн бүх бүлгийн дасгал: 10 000 хүртэлх тоо, дөрвөн үйлдэл, анхны бутархай, дүрс ба тэгш хэм, хэмжилт ба өгөгдөл. Бүлэг бүр өөрийн бодлогын цуглуулгатай.",
  "4": "4-р ангийн бүх бүлгийн дасгал: орны утга ба дөрвөн үйлдлээс энгийн ба аравтын бутархай, хэмжилт, геометр, өгөгдөл хүртэл. Бүлэг бүр өөрийн бодлогын цуглуулгатай.",
};

// The Problem Bank index. A SERVER page so it can read the Mongolian subject
// blurbs (data/problembank-mn/<slug>.json) without the client touching the
// corpus: only a slug → blurb map crosses to ProblemBankHub, which renders
// from the ~55 KB manifest as before (lib/bank-split.test.ts guards this).
export default function ProblemBankPage() {
  const blurbMn: Record<string, string> = { ...BLURB_MN_FALLBACK };
  for (const t of getBankTopics()) {
    const mn = getBankTopicMn(t.slug);
    if (mn?.blurb) blurbMn[t.slug] = mn.blurb;
  }
  return <ProblemBankHub blurbMn={blurbMn} />;
}
