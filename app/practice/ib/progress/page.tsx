import { redirect } from "next/navigation";

// One report per hub, many doors: the IB report lives at /ib-analytics.
export default function IbProgressRedirect() {
  redirect("/ib-analytics");
}
