// THE FIVE-TAB CONTRACT (01-ARCHITECTURE.md rule 3).
//
//   Plan · Learn · Practice · Tests · Progress — that order, every hub, no
//   hub-specific tabs.
//
// The order is a const tuple and the per-hub map is keyed by it, so a hub
// CANNOT declare a sixth tab or reorder the five: both are type errors, not
// review findings. lib/hub-tabs.test.ts pins the rest.
//
// Rule 7 — "nothing enters navigation until it is attached to the graph and
// has content; half-built things live behind a flag, not a nav item" — is why
// an href may be null. A null tab is declared (so the contract is visible and
// the shape is fixed) but NOT rendered. Building Plan is filling in one href.
//
// Pure data + one selector; no React, so the contract can be tested without a
// DOM. components/hub/HubTabs.tsx renders it.

export const HUB_TAB_ORDER = ["plan", "learn", "practice", "tests", "progress"] as const;
export type HubTabKey = (typeof HUB_TAB_ORDER)[number];

export type HubKey = "eysh" | "sat";

export const HUB_TAB_LABELS: Record<HubTabKey, { en: string; mn: string }> = {
  plan: { en: "Plan", mn: "Төлөвлөгөө" },
  learn: { en: "Learn", mn: "Сурах" },
  practice: { en: "Practice", mn: "Дасгал" },
  tests: { en: "Tests", mn: "Тест" },
  progress: { en: "Progress", mn: "Ахиц" },
};

export interface HubSpec {
  base: string;
  /** Every one of the five, in order. null = not built yet, so not rendered. */
  tabs: Record<HubTabKey, string | null>;
}

export const HUBS: Record<HubKey, HubSpec> = {
  eysh: {
    base: "/practice/esh",
    tabs: {
      // Plan is the one piece of the contract that does not exist yet. It
      // stays null rather than linking somewhere approximate.
      plan: null,
      learn: "/practice/esh/learn",
      practice: "/practice/esh/practice",
      tests: "/practice/esh/test",
      progress: "/practice/esh/progress",
    },
  },
  sat: {
    // Declared so the contract is one table rather than two conventions. SAT
    // lags this phase — nothing mounts these yet.
    base: "/practice/sat",
    tabs: {
      plan: null,
      learn: "/practice/sat/learn",
      // SAT's practice surface is its problem bank. Same tab, different href:
      // the hub does not get to invent a "Bank" tab.
      practice: "/practice/sat/bank",
      // No landing page yet — app/practice/sat/test holds only [testId], so
      // /practice/sat/test resolves to nothing. Null keeps rule 7 honest
      // (lib/link-integrity.test.ts caught this pointing at a dead route).
      tests: null,
      progress: "/practice/sat/progress",
    },
  },
};

export interface ResolvedHubTab {
  key: HubTabKey;
  href: string;
  label: { en: string; mn: string };
}

/** The hub's live tabs, in contract order. Unbuilt ones are omitted. */
export function hubTabs(hub: HubKey): ResolvedHubTab[] {
  const spec = HUBS[hub];
  return HUB_TAB_ORDER.flatMap((key) => {
    const href = spec.tabs[key];
    return href ? [{ key, href, label: HUB_TAB_LABELS[key] }] : [];
  });
}

/**
 * Which tab a path sits under, or null when it sits outside the contract.
 *
 * Longest href wins, so /practice/esh/test/2025a resolves to Tests rather
 * than to the hub root. Routes the contract does not name — /practice/esh's
 * own `loop` and `topics` — return null and highlight nothing, which is the
 * honest answer: they are not tabs.
 */
export function activeHubTab(hub: HubKey, pathname: string): HubTabKey | null {
  const path = pathname.split(/[?#]/)[0].replace(/\/+$/, "") || "/";
  let best: { key: HubTabKey; len: number } | null = null;
  for (const t of hubTabs(hub)) {
    if (path === t.href || path.startsWith(`${t.href}/`)) {
      if (!best || t.href.length > best.len) best = { key: t.key, len: t.href.length };
    }
  }
  return best?.key ?? null;
}

/**
 * Paths where the hub chrome must NOT render.
 *
 * A test in progress is a timed exam: showing tabs that navigate out of it
 * mid-question invites an accidental lost session, and the runner already
 * carries its own back/submit affordances. The hub page and the four tab
 * landings all keep the bar.
 */
export function hidesHubChrome(pathname: string): boolean {
  const path = pathname.split(/[?#]/)[0].replace(/\/+$/, "");
  return /^\/practice\/[^/]+\/test\/[^/]+/.test(path);
}
