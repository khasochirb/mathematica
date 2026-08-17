// UNPUBLISHED ROUTES — Phase 0's "cut" without deleting anything.
//
// IB, AP, the standalone topic courses and grades 6–7 leave navigation, leave
// internal links, and go noindex. Every file stays exactly where it is: we
// want IB back in 2027, and re-publishing should be deleting a line from
// data/unpublished-routes.json, not an archaeology project.
//
// One list, three consumers:
//   • next.config.mjs   — serves X-Robots-Tag: noindex on these prefixes
//   • navigation        — filters entries through isUnpublished()
//   • scripts/verify-unpublished.test.ts — fails the build if a PUBLISHED
//     file links into an unpublished prefix (rule 7: nothing half-cut stays
//     in navigation)
//
// The JSON rather than a .ts literal is so next.config.mjs, which cannot
// import TypeScript, reads the same source — the same trick the primary-band
// redirect table already uses.

import unpublished from "@/data/unpublished-routes.json";

export const UNPUBLISHED_PREFIXES: readonly string[] = unpublished.prefixes;

/**
 * Is this path inside an unpublished area?
 *
 * Matches the prefix exactly or at a path boundary, so a grade-6 prefix
 * catches its own sub-routes but never a longer segment that merely starts
 * with the same digits. Query strings and hashes are ignored.
 */
export function isUnpublished(href: string): boolean {
  if (!href.startsWith("/")) return false; // external or relative: not ours
  const path = href.split(/[?#]/)[0].replace(/\/+$/, "") || "/";
  return UNPUBLISHED_PREFIXES.some((p) => path === p || path.startsWith(`${p}/`));
}

/** Drop every entry whose href points into an unpublished area. */
export function publishedOnly<T extends { href: string }>(items: readonly T[]): T[] {
  return items.filter((i) => !isUnpublished(i.href));
}
