import { notFound } from "next/navigation";
import { Noto_Sans } from "next/font/google";
import QRCode from "qrcode";
import PrintSheet from "@/components/pdf/PrintSheet";
import { canonicalQuery, parsePdfOptions } from "@/lib/pdf/options";
import { buildSheet } from "@/lib/pdf/sheet";
import { verifyPrint } from "@/lib/pdf/token";

// The printable worksheet. Not a page anyone browses to: POST /api/pdf signs
// a URL to it, and headless Chromium (or, in the fallback, the student's own
// browser) opens that URL. Without a valid, unexpired token it is a 404, so
// it is never a way round the sign-in wall. docs/pdf-export.md has the flow.

export const dynamic = "force-dynamic";
export const metadata = { robots: { index: false, follow: false } };

// Embedded, never a system font: the server's Chromium has no fonts of its
// own, and Mongolian needs full Cyrillic (Ө ө Ү ү) in body text and in the
// running header and footer.
const noto = Noto_Sans({
  subsets: ["latin", "cyrillic"],
  weight: ["400", "600", "700"],
  display: "block",
});

const SITE = "https://www.mongolpotential.com";

function cssString(s: string): string {
  return `"${s.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/[\r\n]+/g, " ")}"`;
}

export default async function PrintPage({ searchParams }: { searchParams: Record<string, string | string[] | undefined> }) {
  const flat: Record<string, string> = {};
  for (const [k, v] of Object.entries(searchParams)) if (typeof v === "string") flat[k] = v;
  const opts = parsePdfOptions(flat);
  if (!opts || !verifyPrint(canonicalQuery(opts), flat.t)) notFound();
  const sheet = buildSheet(opts);
  if (!sheet) notFound();

  const solutionsUrl = `${SITE}${sheet.solutionsPath}`;
  const qrSvg = await QRCode.toString(solutionsUrl, { type: "svg", margin: 0, errorCorrectionLevel: "M" });
  const font = noto.style.fontFamily;
  const running = `${sheet.title}`;

  const css = `
    html, body { background: #fff !important; }
    body > header, body header:not(.pp-head), body footer { display: none !important; }
    main { padding: 0 !important; }
    @page {
      size: A4;
      margin: 18mm 18mm 20mm 18mm;
      @top-left { content: ${cssString(running)}; font-family: ${font}; font-size: 8.5pt; color: #666; vertical-align: bottom; padding-bottom: 3mm; }
      @bottom-left { content: "mongolpotential.com"; font-family: ${font}; font-size: 8.5pt; color: #666; }
      @bottom-right { content: counter(page) " / " counter(pages); font-family: ${font}; font-size: 8.5pt; color: #666; }
    }
    @page :first { @top-left { content: none; } }
    .mp-print {
      --fg: #111; --fg-1: #222; --fg-2: #444; --fg-3: #666;
      --bg: #fff; --bg-1: #f4f4f4; --bg-2: #eaeaea; --line: #bbb;
      --accent: #0a74da; --accent-wash: #e8f1fb; --accent-line: #9cc3ee;
      font-family: ${font};
      /* The site's own faces are loaded Latin-only; inside the sheet every
         one of them (headings, figure labels) resolves to the embedded Noto. */
      --font-inter: ${font}; --font-space-grotesk: ${font}; --font-serif: ${font}; --font-mono: ${font};
      color: #111; background: #fff;
      font-size: 11pt; line-height: 1.45;
      max-width: 174mm; margin: 0 auto; padding: 0;
      -webkit-print-color-adjust: exact; print-color-adjust: exact;
    }
    @media screen { .mp-print { padding: 12mm 0 24mm; } }
    /* One face for everything but the maths. !important because figure
       components set fonts inline (serif labels, mono axes). */
    .mp-print *:not(.katex, .katex *) { font-family: ${font} !important; }
    /* Words inside formulas (\\text{эсвэл}): KaTeX's own fonts have no
       Cyrillic, so its fallback spans get Noto too. */
    .mp-print .katex .cyrillic_fallback, .mp-print .katex .latin_fallback { font-family: ${font} !important; }
    .mp-print .katex .text, .mp-print .katex .textrm { font-family: KaTeX_Main, ${font}; }
    .pp-head { border-bottom: 1.2pt solid #111; padding-bottom: 5mm; margin-bottom: 6mm; }
    .pp-logo { height: 13mm; width: auto; display: block; margin-bottom: 4mm; }
    .pp-eyebrow { font-size: 8.5pt; letter-spacing: 0.08em; text-transform: uppercase; color: #666; }
    .pp-title { font-size: 19pt; font-weight: 700; line-height: 1.2; margin: 1mm 0 0; }
    .pp-sub { font-size: 10pt; color: #444; margin-top: 1mm; }
    .pp-name { display: flex; align-items: flex-end; gap: 2mm; margin-top: 6mm; font-size: 10pt; }
    .pp-line { display: inline-block; border-bottom: 0.8pt solid #111; width: 35mm; height: 4mm; margin-right: 6mm; }
    .pp-line-long { flex: 1; }
    .pp-part { font-size: 12pt; font-weight: 700; margin: 4mm 0 2mm; break-after: avoid; }
    .pp-item { break-inside: avoid; page-break-inside: avoid; padding: 3mm 0; border-bottom: 0.4pt solid #ddd; }
    .pp-context { margin: 0 0 2mm; }
    .pp-row { display: flex; gap: 3mm; }
    .pp-n { font-weight: 700; min-width: 9mm; text-align: right; flex-shrink: 0; }
    .pp-body { flex: 1; min-width: 0; }
    .pp-statement { margin: 0; }
    .pp-fig { max-width: 105mm; margin-top: 2mm; }
    /* Figure components draw a site card around themselves; on paper the
       figure stands on the page. */
    .pp-fig div { background: transparent !important; border: 0 !important; box-shadow: none !important; padding: 0 !important; }
    .pp-fig svg { max-width: 100%; height: auto; }
    .pp-img { display: block; max-width: 100%; max-height: 70mm; width: auto; height: auto; margin-top: 2mm; }
    .pp-options { list-style: none; padding: 0; margin: 2mm 0 0; display: grid; gap: 1.5mm 5mm; }
    .pp-options li { break-inside: avoid; }
    .pp-space { display: none; }
    .pp-with-space .pp-space { display: block; height: 32mm; }
    .pp-key { break-before: page; page-break-before: always; }
    .pp-key-h { font-size: 15pt; font-weight: 700; margin: 0 0 4mm; border-bottom: 1.2pt solid #111; padding-bottom: 2mm; }
    .pp-key-list { list-style: none; padding: 0; margin: 0; column-count: 2; column-gap: 10mm; font-size: 10pt; }
    .pp-key-list li { break-inside: avoid; padding: 0.8mm 0; }
    .pp-solutions { display: flex; gap: 5mm; align-items: center; margin-top: 8mm; padding: 4mm; border: 0.8pt solid #bbb; border-radius: 2mm; break-inside: avoid; font-size: 10pt; }
    .pp-solutions p { margin: 0; }
    .pp-qr { width: 24mm; height: 24mm; flex-shrink: 0; }
    .pp-qr svg { width: 100%; height: 100%; }
    .pp-url { font-weight: 600; margin-top: 1mm !important; word-break: break-all; }
    .pp-promo { margin-top: 8mm; padding-top: 3mm; border-top: 0.4pt solid #bbb; font-size: 9pt; color: #333; break-inside: avoid; }
    .mp-print .katex { font-size: 1.05em; }
  `;

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: css }} />
      <PrintSheet
        sheet={sheet}
        answers={opts.answers === "key"}
        space={opts.space}
        nameLine={opts.nameLine}
        solutionsUrl={solutionsUrl}
        qrSvg={qrSvg}
        autoPrint={flat.print === "1"}
      />
    </>
  );
}
