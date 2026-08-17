import HubProgress from "@/components/hub/HubProgress";

// The SAT analytics report — same design as the ЭШ report at /analytics:
// projected score from recent sittings, trajectory graph, domain mastery,
// per-question sitting review, recent attempts, and the mistake bank.
export default function SatAnalyticsPage() {
  return (
    <HubProgress
      context="sat"
      title="SAT Math"
      comingSoonCopy="Sit a full-length adaptive mock test and your projected scaled score, trajectory, domain breakdown and mistake bank appear here."
    />
  );
}
