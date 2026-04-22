import type { Metadata } from "next";
import { Inter, Space_Grotesk, Instrument_Serif, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import { LangProvider } from "@/lib/lang-context";
import { AuthProvider } from "@/lib/auth-context";
import { ThemeProvider } from "@/lib/theme-context";
import { UpgradeModalProvider } from "@/lib/upgrade-modal-context";
import AttemptsSyncIndicator from "@/components/AttemptsSyncIndicator";

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

const instrumentSerif = Instrument_Serif({
  subsets: ["latin"],
  weight: "400",
  style: ["normal", "italic"],
  variable: "--font-serif",
  display: "swap",
});

const jetBrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-mono",
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
    <html
      lang="en"
      data-theme="light"
      suppressHydrationWarning
      className={`${inter.variable} ${spaceGrotesk.variable} ${instrumentSerif.variable} ${jetBrainsMono.variable}`}
    >
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `(function(){try{var t=localStorage.getItem('mp_theme');if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();`,
          }}
        />
      </head>
      <body>
        <ThemeProvider>
          <LangProvider>
            <AuthProvider>
              <UpgradeModalProvider>
                <Header />
                <main>{children}</main>
                <Footer />
                <AttemptsSyncIndicator />
              </UpgradeModalProvider>
            </AuthProvider>
          </LangProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
