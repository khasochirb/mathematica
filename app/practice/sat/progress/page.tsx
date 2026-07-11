import HubProgress from "@/components/hub/HubProgress";

// SAT progress — pre-wired analytics skeleton. Lights up automatically the
// day the first SAT mock test records attempts with context "sat".
export default function SatProgressPage() {
  return (
    <HubProgress
      context="sat"
      title="SAT Math"
      comingSoonCopy="Full-length adaptive mock tests are on the way. Your per-domain performance and scaled-score projection will appear here from your very first test."
    />
  );
}
