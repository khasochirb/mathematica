// The problem-bank CORPUS — every topic's full variants, ~9 MB of JSON.
//
// SERVER-SIDE ONLY. Import this from server route pages (which pass one
// topic at a time to the client components as props) and from Node-side
// code (tests, harvesters). Importing it from a client component or a
// client-reachable lib module bundles all seventeen subjects into the
// browser chunk — the 10 MB-chunk regression this module exists to
// prevent. lib/bank-split.test.ts enforces the boundary; client code that
// only needs the topic LIST uses lib/bank-manifest.ts (~55 KB).
//
// Loading strips each variant's `check` array: it is sympy source for the
// verify gate, never rendered, and dropping it keeps ~700 KB of dead
// weight out of every page's RSC payload.

import {
  type BankTopic,
  type BankVariant,
} from "@/lib/problem-bank";

import algebra1 from "@/data/problembank/algebra-1.json";
import algebra2 from "@/data/problembank/algebra-2.json";
import geometry from "@/data/problembank/geometry.json";
import trigonometry from "@/data/problembank/trigonometry.json";
import solidGeometry from "@/data/problembank/solid-geometry.json";
import probStats from "@/data/problembank/prob-stats.json";
import precalculus from "@/data/problembank/precalculus.json";
import calculus from "@/data/problembank/calculus.json";
import vectorsMatrices from "@/data/problembank/vectors-matrices.json";
import integrated1 from "@/data/problembank/integrated-1.json";
import integrated2 from "@/data/problembank/integrated-2.json";
import integrated3 from "@/data/problembank/integrated-3.json";
import grade5 from "@/data/problembank/5.json";
import grade9 from "@/data/problembank/9.json";
import grade12 from "@/data/problembank/12.json";
import sat from "@/data/problembank/sat.json";
import ibSl from "@/data/problembank/ib-sl.json";
import ibHl from "@/data/problembank/ib-hl.json";

function stripChecks(raw: unknown): BankTopic {
  const t = raw as BankTopic;
  return {
    ...t,
    forms: t.forms.map((f) => ({
      ...f,
      variants: f.variants.map((v) => {
        const { check: _check, ...rest } = v as Required<BankVariant>;
        return rest as BankVariant;
      }),
    })),
  };
}

const TOPICS: BankTopic[] = [
  algebra1,
  algebra2,
  geometry,
  trigonometry,
  solidGeometry,
  probStats,
  precalculus,
  calculus,
  vectorsMatrices,
  integrated1,
  integrated2,
  integrated3,
  // Primary band: Grade 5 (slug mirrors the course path /math/5), one
  // collection per unit of the year.
  grade5,
  // Band exit levels (slugs mirror the course paths /math/9 and /math/12);
  // also the source pools for the band exit exams.
  grade9,
  grade12,
].map(stripChecks);

export function getBankTopics(): BankTopic[] {
  return TOPICS;
}

export function getBankTopic(slug: string): BankTopic | null {
  return TOPICS.find((t) => t.slug === slug) ?? null;
}

// Hub-owned banks. Deliberately NOT in TOPICS: getBankTopics() is the /math
// course-ladder list (it feeds the General Math hub page, the ratings card,
// and placement wiring), while these belong to their exam hubs and follow
// the hub's own taxonomy — the four Digital SAT domains at /practice/sat/bank,
// the five IB syllabus topics per tier at /practice/ib/bank. Their mastery
// stores (mp-bank:sat:*, mp-bank:ib-*) are likewise scoped to the hub, not
// to "courses", in lib/data-erase.ts.
const SAT_BANK: BankTopic = stripChecks(sat);
const IB_SL_BANK: BankTopic = stripChecks(ibSl);
const IB_HL_BANK: BankTopic = stripChecks(ibHl);

export function getSatBankTopic(): BankTopic {
  return SAT_BANK;
}

export type IbBankTier = "sl" | "hl";

export function getIbBankTopic(tier: IbBankTier): BankTopic {
  return tier === "sl" ? IB_SL_BANK : IB_HL_BANK;
}
