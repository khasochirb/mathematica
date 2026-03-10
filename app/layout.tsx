import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
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
    <html lang="en" className={inter.variable}>
      <body>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
