"use client";

import { usePathname } from "next/navigation";
import HubTabs from "@/components/hub/HubTabs";
import { hidesHubChrome } from "@/lib/hub-tabs";

// The IB hub wears the five-tab contract, like ЭШ and SAT.
//
// IB was not even in HubKey, so it could not have had tabs — the contract
// covered two of the three exam hubs and nobody noticed, because the only
// hub anyone compared against was the one that had them.
export default function IbLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname() ?? "";
  return (
    <>
      {!hidesHubChrome(pathname) && <HubTabs hub="ib" />}
      {children}
    </>
  );
}
