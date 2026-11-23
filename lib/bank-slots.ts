// The unit exercise list's order and variant pick, shared by the browse page
// (components/bank/BankBrowser.tsx) and the printable worksheet
// (lib/pdf/sheet.ts) so a printed problem 7 is the site's problem 7.

import type { BankForm } from "@/lib/problem-bank";

export type Slot = { form: BankForm; round: number };

// Deterministic (SSR-safe) but well-spread pick: stride through the variant
// pool with a step co-prime to its size, so consecutive rounds of the same
// form land in different parameter neighborhoods instead of v01, v02, v03…
export function spreadIndex(round: number, n: number): number {
  const stride = n % 13 === 0 ? (n % 11 === 0 ? 7 : 11) : 13;
  return (round * stride) % n;
}

export function buildSlots(forms: BankForm[], rounds: number): Slot[] {
  // Round-robin across forms (within the level-sorted order), so problem
  // n+1 is a different kind than problem n. Each round serves a spread-out
  // variant as the starting point (reroll can move it later).
  const slots: Slot[] = [];
  for (let r = 0; r < rounds; r++) {
    for (const form of forms) {
      if (r < form.variants.length) slots.push({ form, round: r });
    }
  }
  return slots;
}

