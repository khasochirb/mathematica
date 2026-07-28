import { redirect } from "next/navigation";

// ЭЕШ used to have TWO progress reports: this one, reached from the hub, and
// /analytics, reached from the dashboard — while SAT and IB each had ONE page
// reached from both places. The two ЭЕШ pages held different things, so a
// student saw a different report depending on which door they came through.
//
// The dashboard report won, and everything this page owned that it lacked
// (per-sitting question review, topic breakdown, weak-topic → course routing,
// flagged questions, next-test recommendation) moved into it as
// components/esh/progress/EshStudyReport.tsx. Data erasure moved to the
// account-level panel on the same page.
//
// This route stays as a redirect rather than a 404: it is linked from the hub,
// from test-result screens, and from anywhere a student has bookmarked it.
export default function EshProgressPage() {
  redirect("/analytics");
}
