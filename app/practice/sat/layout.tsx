"use client";

import { usePathname } from "next/navigation";
import HubTabs from "@/components/hub/HubTabs";
import { hidesHubChrome } from "@/lib/hub-tabs";

// The SAT hub wears the five-tab contract, like ЭШ and IB.
//
// lib/hub-tabs.ts had declared SAT's tabs since the contract was written,
// but nothing mounted them — so the bar was a ЭШ-only feature and the two
// hubs did not look like each other at all. A spec with no layout to
// render it is not a shared design.
export default function SatLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname() ?? "";
  return (
    <>
      {!hidesHubChrome(pathname) && <HubTabs hub="sat" />}
      {children}
    </>
  );
}
