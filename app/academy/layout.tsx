import type { Metadata } from "next";

// Server wrapper so the (client) academy page gets crawlable metadata: this
// is what search engines and Facebook read when the link is shared.

const TITLE = "Mongol Potential Academy: In-Person Classes in Ulaanbaatar";
const DESCRIPTION =
  "In-person math classes in Ulaanbaatar from grade 6: ЭШ prep, SAT prep and olympiad prep, in groups or one-on-one. Mandala Garden, Khan-Uul District.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/academy" },
  openGraph: {
    title: TITLE,
    description: DESCRIPTION,
    url: "/academy",
    type: "website",
  },
  twitter: {
    card: "summary",
    title: TITLE,
    description: DESCRIPTION,
  },
};

export default function AcademyLayout({ children }: { children: React.ReactNode }) {
  return children;
}
