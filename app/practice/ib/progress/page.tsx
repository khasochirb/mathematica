import HubProgress from "@/components/hub/HubProgress";

// IB progress — pre-wired analytics skeleton. Lights up automatically the
// day the first IB paper records attempts with context "ib".
export default function IbProgressPage() {
  return (
    <HubProgress
      context="ib"
      title="IB Mathematics"
      comingSoonCopy="IB practice papers (AA and AI, SL and HL) are on the way. Your per-paper performance and predicted grade will appear here from your very first marked paper."
    />
  );
}
