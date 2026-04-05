import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import "./globals.css";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import { LangProvider } from "@/lib/lang-context";
import { AuthProvider } from "@/lib/auth-context";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  variable: "--font-space-grotesk",
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Mongol Potential | World Class Math Education",
    template: "%s | Mongol Potential",
  },
  description:
    "High-quality math education for Mongolian students around the world—aligned with AP, IB, and US state curricula, strengthened with cultural connection.",
  keywords: ["math tutoring", "Mongolian education", "SAT math", "AMC", "online tutoring"],
  openGraph: {
    siteName: "Mongol Potential",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${spaceGrotesk.variable}`}>
      <body>
        <LangProvider>
          <AuthProvider>
            <Header />
            <main>{children}</main>
            <Footer />
          </AuthProvider>
        </LangProvider>
      </body>
    </html>
  );
}
