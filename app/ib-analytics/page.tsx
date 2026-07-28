import HubProgress from "@/components/hub/HubProgress";

// The IB analytics report — same design as the ЭЕШ report at /analytics:
// predicted grade from recent papers, trajectory graph, component mastery,
// per-part sitting review with markschemes, recent attempts, and the
// mistake bank.
export default function IbAnalyticsPage() {
  return (
    <HubProgress
      context="ib"
      title="IB Mathematics"
      comingSoonCopy="Sit a practice paper and your predicted grade, trajectory, component breakdown and mistake bank appear here."
    />
  );
}
