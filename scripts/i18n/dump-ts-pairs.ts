// Dumps the English/Mongolian pairs that live in TypeScript (placement
// questions and the chrome dictionary) as JSON on stdout,
// for scripts/i18n/export_review.py. Run: npx tsx scripts/i18n/dump-ts-pairs.ts
import { PLACEMENT_BANKS } from "@/lib/placement-bank-mn";
import { ALL_CHROME } from "@/lib/i18n/chrome";

const placement: Record<string, unknown>[] = [];
for (const [bank, { en, table }] of Object.entries(PLACEMENT_BANKS)) {
  for (const q of en()) {
    const t = table.questions[q.id];
    const row = (field: string, e: string, m: string | undefined) =>
      placement.push({ bank, id: q.id, topic: q.topicSlug, field, en: e, mn: m ?? "" });
    row("topic title", q.topicTitle, table.topics[q.topicSlug]);
    row("prompt", q.prompt, t?.prompt);
    q.options.forEach((o, i) => row(`option ${i + 1}${i === q.correctIndex ? " (correct)" : ""}`, o, t?.options[i]));
    row("explanation", q.explanation, t?.explanation);
  }
}
const chrome = ALL_CHROME.map((c) => ({ en: c.en, mn: c.mn, approved: c.ok ?? "", note: c.note ?? "" }));
process.stdout.write(JSON.stringify({ placement, chrome }));
