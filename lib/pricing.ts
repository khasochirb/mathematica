// Premium pricing — SINGLE SOURCE OF TRUTH for every price shown anywhere
// on the site. Change a number here and every surface follows.
//
// Launch model (v1, no payment gateway): prices are public, the upgrade modal
// takes a purchase request (email → premium_waitlist with a purchase_* source),
// the owner collects payment out-of-band (bank transfer / QPay invoice) and
// activates the account — either in the Supabase dashboard
// (profiles.is_subscribed + subscription_expires_at) or via
// POST /api/subscription/activate with the ADMIN_ACTIVATION_KEY header.
// A real gateway can replace the manual step later without touching this file.

export interface PricingPlan {
  key: "monthly" | "quarter";
  months: number;
  /** Total price for the whole period, in MNT. */
  priceMnt: number;
  label: { en: string; mn: string };
  /** Shown under the price — what the period works out to. */
  note: { en: string; mn: string };
  /** Savings badge vs paying monthly; null on the base plan. */
  badge: { en: string; mn: string } | null;
}

export const PRICING_PLANS: PricingPlan[] = [
  {
    key: "monthly",
    months: 1,
    priceMnt: 19_900,
    label: { en: "Monthly", mn: "Сарын эрх" },
    note: { en: "per month", mn: "сар бүр" },
    badge: null,
  },
  {
    key: "quarter",
    months: 3,
    priceMnt: 49_900,
    label: { en: "3 months", mn: "3 сарын эрх" },
    note: { en: "≈ ₮16,633 / month", mn: "≈ ₮16,633 / сар" },
    badge: { en: "Save 16%", mn: "16% хэмнэлт" },
  },
];

/** ₮19,900 style — thin-space-free, comma-grouped, tugrik sign in front. */
export function formatMnt(amount: number): string {
  return `₮${amount.toLocaleString("en-US")}`;
}
