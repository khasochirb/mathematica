import { redirect } from "next/navigation";

// Alias for discoverability — the ЭЕШ analytics report lives at /analytics.
// This exists so the three hubs' reports share one URL shape:
// /eysh-analytics · /sat-analytics · /ib-analytics.
export default function EyshAnalyticsAlias() {
  redirect("/analytics");
}
