import { readFileSync } from "node:fs";
import { join } from "node:path";
import { ImageResponse } from "next/og";

// Social link-preview card for /tutoring — this is what unfurls when the page
// link is shared on Facebook / Messenger / iMessage. Prerendered to a 1200x630
// PNG at build time. Brand-matched: dark surface, indigo accent, serif headline.
//
// Fonts are bundled in-repo (assets/fonts) and read from disk so OG generation
// never depends on build-time network access — @vercel/og has no default font
// and requires at least one. Instrument Serif = brand serif (headline + quote);
// Inter = labels / url.

export const runtime = "nodejs";
export const alt = "1-on-1 Online Math Tutoring — Mongol Potential";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const HEADLINE = "The best math support your child will have.";
const QUOTE = "A 100-point jump on her state test.";

const serifFont = readFileSync(join(process.cwd(), "assets/fonts/InstrumentSerif-Regular.ttf"));
const sansFont = readFileSync(join(process.cwd(), "assets/fonts/Inter-Regular.ttf"));

export default function OpengraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          height: "100%",
          width: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          background: "#14161b",
          padding: 72,
          position: "relative",
          fontFamily: "Inter",
        }}
      >
        {/* accent glow */}
        <div
          style={{
            position: "absolute",
            top: -160,
            right: -120,
            width: 620,
            height: 620,
            display: "flex",
            backgroundImage:
              "radial-gradient(circle at center, rgba(99,102,241,0.30), transparent 60%)",
          }}
        />

        {/* top — brand + eyebrow */}
        <div style={{ display: "flex", flexDirection: "column", gap: 26 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
            <div
              style={{ width: 24, height: 24, borderRadius: 7, background: "#6366f1", display: "flex" }}
            />
            <div style={{ display: "flex", fontSize: 24, color: "#e7e9ee", fontWeight: 600, letterSpacing: 2 }}>
              MONGOL POTENTIAL
            </div>
          </div>
          <div style={{ display: "flex", fontSize: 22, color: "#818cf8", letterSpacing: 5, fontWeight: 600 }}>
            1-ON-1 ONLINE MATH TUTORING
          </div>
        </div>

        {/* middle — headline + proof */}
        <div style={{ display: "flex", flexDirection: "column", gap: 34 }}>
          <div
            style={{
              display: "flex",
              fontFamily: "Instrument Serif",
              fontSize: 76,
              lineHeight: 1.04,
              color: "#f5f6f8",
              maxWidth: 980,
            }}
          >
            {HEADLINE}
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div style={{ display: "flex", width: 4, height: 78, background: "#6366f1", borderRadius: 2 }} />
            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
              <div
                style={{ display: "flex", fontFamily: "Instrument Serif", fontSize: 34, color: "#d7dae2" }}
              >
                {`“${QUOTE}”`}
              </div>
              <div style={{ display: "flex", fontSize: 20, color: "#9aa0ac", letterSpacing: 1 }}>
                — Parent of a 9th-grade student
              </div>
            </div>
          </div>
        </div>

        {/* bottom — url + tags */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", fontSize: 24, color: "#c3c7d1", fontWeight: 600 }}>
            mongolpotential.com/tutoring
          </div>
          <div style={{ display: "flex", fontSize: 20, color: "#9aa0ac", letterSpacing: 1 }}>
            Any grade · Any curriculum · Fully online
          </div>
        </div>
      </div>
    ),
    {
      ...size,
      fonts: [
        { name: "Instrument Serif", data: serifFont, style: "normal", weight: 400 },
        { name: "Inter", data: sansFont, style: "normal", weight: 400 },
      ],
    },
  );
}
