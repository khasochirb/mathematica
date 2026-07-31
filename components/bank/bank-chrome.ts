// Where a bank topic LIVES. The same three components (BankUnitList,
// BankBrowser, BankRunner) serve the /math course-ladder banks and the SAT
// hub's topic bank — only the surrounding chrome differs: base URLs, the
// breadcrumb label, and whether there is a course to send the student back
// to. Kept as plain data (no functions) so server route pages can pass it
// straight into the client components.

import type { BankTopic } from "@/lib/problem-bank";

export type BankChrome = {
  /** This topic's unit-list page; unit pages hang off it as `${topicBase}/${unitId}`. */
  topicBase: string;
  /** Where the unit list's back arrow goes (the bank hub, or the SAT hub). */
  backHref: string;
  /** Breadcrumb prefix: "Problem Bank" / "SAT Math · Topic practice". */
  eyebrow: string;
  /** The companion course; unit lesson links are `${courseHref}/${unitId}`. null = no course yet, hide those links. */
  courseHref: string | null;
};

export function defaultBankChrome(topic: BankTopic): BankChrome {
  return {
    topicBase: `/math/problem-bank/${topic.slug}`,
    backHref: "/math/problem-bank",
    eyebrow: "Problem Bank",
    courseHref: `/math/${topic.slug}`,
  };
}

// The SAT course (backlog #245) doesn't exist yet, so courseHref is null —
// linking into General Math from here is the exact dead-end the resource
// blueprint forbids.
export const SAT_BANK_CHROME: BankChrome = {
  topicBase: "/practice/sat/bank",
  backHref: "/practice/sat",
  eyebrow: "SAT Math · Topic practice",
  courseHref: null,
};
