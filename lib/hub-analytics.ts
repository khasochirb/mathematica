// Exam-hub analytics vocabulary — the SAT and IB counterpart of
// TOPIC_LABELS. These label maps double as the TAGGING CONTRACT: when the
// SAT/IB question banks are authored, their `topic` values must come from
// these keys so hub progress pages label them correctly. (Per the
// skill-taxonomy manual: one locked vocabulary per hub, never shared.)
//
// Native score projections (SAT 200–800 scaled, IB grade 1–7) deliberately
// do NOT ship here yet — they require real scoring curves from the first
// authored mock tests. Until then the hubs show accuracy and say so.

// The four Digital SAT Math content domains (College Board naming).
export const SAT_DOMAIN_LABELS: Record<string, string> = {
  algebra: "Algebra",
  "advanced-math": "Advanced Math",
  "problem-solving-data": "Problem-Solving & Data Analysis",
  "geometry-trig": "Geometry & Trigonometry",
};

// IB Mathematics components: course track × paper.
export const IB_COMPONENT_LABELS: Record<string, string> = {
  "aa-paper-1": "AA · Paper 1 (no calculator)",
  "aa-paper-2": "AA · Paper 2 (calculator)",
  "aa-paper-3": "AA · Paper 3 (HL)",
  "ai-paper-1": "AI · Paper 1",
  "ai-paper-2": "AI · Paper 2",
  "ai-paper-3": "AI · Paper 3 (HL)",
};

// Topic label inside an exam hub, with a humanized fallback so an
// unexpected slug degrades to readable text instead of raw kebab-case.
export function hubTopicLabel(context: string, slug: string): string {
  const table = context === "sat" ? SAT_DOMAIN_LABELS : context === "ib" ? IB_COMPONENT_LABELS : {};
  if (table[slug]) return table[slug];
  const s = slug.replace(/-/g, " ");
  return s.charAt(0).toUpperCase() + s.slice(1);
}

// What the hub's native headline metric will be, and why it isn't shown
// yet — surfaced verbatim on the progress skeletons so the placeholder is
// honest rather than a fake number.
export const HUB_NATIVE_METRIC_NOTE: Record<string, string> = {
  sat: "Scaled-score projection (200–800) arrives with the first full adaptive mock test.",
  ib: "Predicted grade (1–7) arrives with the first marked paper — IB attempts will carry markscheme points, not just correct/incorrect.",
};
