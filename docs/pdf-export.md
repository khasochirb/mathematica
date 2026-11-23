# PDF export (worksheets)

A signed-in student can download any problem-bank unit, course exam or ЭШ
paper as an A4 worksheet PDF. The button sits next to the unit title on bank
pages and under each paper in the course-exam and ЭШ test lists.

## The decision: answers, not solutions

A PDF carries **at most an answer key**. The step-by-step solutions stay on
the site, and the answer page has a QR code and link to them. (Khas asked for
a business call on 23 Nov 2026; this is it.)

- **The solutions are what brings students back.** On the site a wrong
  answer gets a diagnosis, hints and a solution one step at a time. Paper
  can't do any of that. An answer key is enough to mark a worksheet. When a
  student is wrong, the QR code sends them to where they actually learn,
  which is also where the Academy invitation and activity tracking live.
- **A PDF travels.** Worksheets get forwarded, printed in bulk and handed out
  by other tutors. Full solutions would give away the most expensive part of
  the product, as a ready-made course, to people who never visit the site.
- **Shorter files.** A 40-problem unit with full solutions is 3–4× the pages.

To change it, add `"solutions"` to `answers` in `lib/pdf/options.ts` and
render `steps`/`explanation` in `components/pdf/PrintSheet.tsx`.

## How it works

```
DownloadPdfButton (client) ── POST /api/pdf {source, lang, answers, space, nameLine}
                                   │  1. login required (lib/server-auth), else 401
                                   │  2. options parsed strictly (lib/pdf/options.ts), else 400
                                   │  3. source must exist (lib/pdf/sheet.ts), else 404
                                   │  4. 20 exports / account / hour, else 429
                                   │  5. signs /math/print?<options>&t=<HMAC, 10 min>
                                   ▼
             headless Chromium (lib/pdf/render.ts) opens /math/print, waits for
             window.__READY__ (fonts, KaTeX, images), page.pdf() → attachment
                                   │  on failure: 503 + a signed link; the dialog
                                   ▼  offers "Open printable version" → window.print()
```

- **`/math/print`** (`app/math/print/page.tsx`) renders the worksheet from
  the same static data the site uses. Without a valid, unexpired token it is
  a 404, so it is never a way round the sign-in wall. The token signs the
  exact canonical query, so an edited URL fails too.
- **The token key** is `PDF_PRINT_SECRET` if set, otherwise a SHA-256
  derivation of the service-role key with a fixed label. The service-role key
  itself never leaves the server and is not the HMAC key.
- **Numbering** matches the site. Bank units use the browse page's order
  (`lib/bank-slots.ts`, shared with `BankBrowser`) and its option shuffle
  (`seededOptionOrder(v, v.id)`). Exams use authored order. ЭШ papers use the
  paper's own numbers (Section 2 as `2.1.1`).
- **Fonts:** Noto Sans (Latin + Cyrillic, including Ө ө Ү ү) is embedded via
  `next/font`. Every non-maths element is forced onto it, including figure
  labels and the Cyrillic fallback spans inside KaTeX, because the server's
  Chromium has no system fonts. KaTeX keeps its own maths fonts.
- **Running header and footer** come from CSS `@page` margin boxes (Chromium
  131+), so they use the embedded font: section title top-left (from page 2),
  `mongolpotential.com` bottom-left, `page / pages` bottom-right.

## Changing the layout

All print styling is the `css` string in `app/math/print/page.tsx`:

- page size and margins: `@page { size: A4; margin: … }`
- working space under each problem: `.pp-with-space .pp-space { height }`
- answer key columns: `.pp-key-list { column-count }`
- figure width: `.pp-fig { max-width }`

Markup and wording (header, name line, key, the Academy line) are in
`components/pdf/PrintSheet.tsx`. Check a change locally:

```bash
PDF_PRINT_SECRET=dev npx next dev -p 3921
# sign a URL with lib/pdf/token.ts (same secret) and open it, or call
# renderPdf() from lib/pdf/render.ts; it uses /opt/pw-browsers/chromium
# (or CHROME_PATH) when not on Vercel.
```

## Deployment notes

- `@sparticuz/chromium@131.0.1` and `puppeteer-core@23.11.1` are kept
  external and traced into `/api/pdf` (`next.config.mjs`,
  `experimental.outputFileTracingIncludes`). The function runs on Node
  (`runtime = "nodejs"`, `maxDuration = 60`). The project is on Node 22.
- **Preview deployments** are behind Vercel login, so the server renderer
  cannot open the preview's print page unless "Protection Bypass for
  Automation" is enabled (`VERCEL_AUTOMATION_BYPASS_SECRET`). Without it,
  previews fall back to the browser print dialog. Production is not affected.
- The rate limit is in memory, per server instance. It stops a runaway loop,
  not a determined abuser.
- No watermark: the material is free since 23 Nov 2026, and printing a
  minor's email on a file meant to be shared is the privacy problem the
  watermark was supposed to prevent.
- No storage cache: renders take a few seconds, and caching would need a
  bucket and a migration. Revisit if `/api/pdf` shows up in usage.

Tests: `lib/pdf/pdf-export.test.ts` (parsing, token, numbering, and the
route's 401/400/404/429/503 paths).
