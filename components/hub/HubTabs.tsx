"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useLang } from "@/lib/lang-context";
import { activeHubTab, hubTabs, type HubKey } from "@/lib/hub-tabs";

// The five-tab bar every hub wears (01-ARCHITECTURE.md rule 3). The order and
// the tab set come from lib/hub-tabs.ts and cannot be overridden here — this
// component takes a hub key and nothing else, so there is no prop through
// which a hub could add a sixth tab or reorder the five.
export default function HubTabs({ hub }: { hub: HubKey }) {
  const pathname = usePathname() ?? "";
  const { lang } = useLang();
  const mn = lang === "mn";
  const tabs = hubTabs(hub);
  const active = activeHubTab(hub, pathname);

  if (tabs.length === 0) return null;

  return (
    <nav
      aria-label={mn ? "Хэсгүүд" : "Hub sections"}
      className="sticky top-16 z-30"
      style={{ background: "var(--bg)", borderBottom: "1px solid var(--line)" }}
    >
      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <ul className="flex items-center gap-1 overflow-x-auto" style={{ scrollbarWidth: "none" }}>
          {tabs.map((t) => {
            const isActive = t.key === active;
            return (
              <li key={t.key} className="flex-shrink-0">
                <Link
                  href={t.href}
                  aria-current={isActive ? "page" : undefined}
                  className="inline-block px-3.5 py-3 text-[13.5px] transition-colors"
                  style={{
                    color: isActive ? "var(--accent)" : "var(--fg-1)",
                    fontWeight: isActive ? 600 : 500,
                    borderBottom: `2px solid ${isActive ? "var(--accent)" : "transparent"}`,
                    marginBottom: -1,
                  }}
                >
                  {mn ? t.label.mn : t.label.en}
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    </nav>
  );
}
