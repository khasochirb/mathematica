import type { Metadata } from "next";

// Server component wrapper so the (client) tutoring page gets real, crawlable
// metadata — this is what Facebook / Messenger / search engines read when the
// /tutoring link is shared. The card image comes from opengraph-image.tsx in
// this same folder (Next wires it into og:image + twitter:image automatically).

const TITLE = "1-on-1 Online Math Tutoring";
const DESCRIPTION =
  "Personalized 1-on-1 online math tutoring — any grade, any curriculum, anywhere in the world. A plan built around your child, taught by an experienced mathematician. Real help, real plans, real progress.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/tutoring" },
  openGraph: {
    title: `${TITLE} | Mongol Potential`,
    description: DESCRIPTION,
    url: "/tutoring",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: `${TITLE} | Mongol Potential`,
    description: DESCRIPTION,
  },
};

export default function TutoringLayout({ children }: { children: React.ReactNode }) {
  return children;
}
