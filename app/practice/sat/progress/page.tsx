import { redirect } from "next/navigation";

// One report per hub, many doors: the SAT report lives at /sat-analytics.
// This route stays as a redirect because the hub, the dashboard, and old
// bookmarks all link here.
export default function SatProgressRedirect() {
  redirect("/sat-analytics");
}
