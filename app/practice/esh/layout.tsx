"use client";

import { usePathname } from "next/navigation";
import HubTabs from "@/components/hub/HubTabs";
import { hidesHubChrome } from "@/lib/hub-tabs";

// The ЭШ hub wears the five-tab contract (01-ARCHITECTURE.md rule 3) on
// every one of its routes — except inside a running test, which is a timed
// exam and gets no navigation out of itself.
export default function ESHLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname() ?? "";
  return (
    <>
      {!hidesHubChrome(pathname) && <HubTabs hub="eysh" />}
      {children}
    </>
  );
}
