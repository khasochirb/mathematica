"use client";

import { useState } from "react";
import { Download, Loader2, Printer, X } from "lucide-react";
import { useLang } from "@/lib/lang-context";
import { useAuth } from "@/lib/auth-context";
import { fetchWithAuth } from "@/lib/api";
import { COUNT_CHOICES, type PdfSource } from "@/lib/pdf/options";

// "Download PDF" next to a problem-bank unit, a course exam or an ЭШ paper.
// Opens a small dialog, asks the server for a PDF (POST /api/pdf), and saves
// it. If the server render fails, it offers the browser's own print dialog
// on the same printable page instead.

type Source =
  | { kind: "bank"; bank: string; unit: string }
  | { kind: "exam"; examId: string }
  | { kind: "esh"; testKey: string };

const L = {
  mn: {
    button: "PDF татах",
    title: "PDF татах",
    problems: "Бодлого",
    all: "Бүгд",
    first: (n: number) => `Эхний ${n}`,
    level: "Түвшин",
    anyLevel: "Бүх түвшин",
    levelN: (n: number) => `${n}-р түвшин`,
    answers: "Хариу",
    noAnswers: "Хариугүй",
    key: "Төгсгөлд нь хариутай",
    keyNote: "Бодолтыг алхам алхмаар нь сайтаас үзнэ. Хариуны хуудсан дээрх QR код тийш нь хөтөлнө.",
    space: "Бодох зай үлдээх",
    nameLine: "Нэр, огнооны мөр",
    language: "Хэл",
    download: "Татах",
    working: "Бэлдэж байна…",
    failed: "PDF үүсгэж чадсангүй. Хэвлэх цонхоор нь хадгалаарай.",
    openPrint: "Хэвлэх хувилбарыг нээх",
    signIn: "PDF татахын тулд нэвтэрнэ үү.",
    limited: "Нэг цагт 20-оос олон удаа татах боломжгүй. Дараа дахин оролдоорой.",
  },
  en: {
    button: "Download PDF",
    title: "Download PDF",
    problems: "Problems",
    all: "All",
    first: (n: number) => `First ${n}`,
    level: "Level",
    anyLevel: "All levels",
    levelN: (n: number) => `Level ${n}`,
    answers: "Answers",
    noAnswers: "No answers",
    key: "Answer key at the end",
    keyNote: "Step-by-step solutions are on the site; the QR code on the answer page links there.",
    space: "Leave space for working",
    nameLine: "Name and date line",
    language: "Language",
    download: "Download",
    working: "Preparing…",
    failed: "Couldn't create the PDF. Save it from the print dialog instead.",
    openPrint: "Open printable version",
    signIn: "Sign in to download a PDF.",
    limited: "That's more than 20 downloads in an hour. Try again later.",
  },
};

export default function DownloadPdfButton({
  source,
  langs = ["mn", "en"],
  className = "btn btn-line text-[13px]",
}: {
  source: Source;
  /** Languages the material exists in (ЭШ papers: Mongolian only). */
  langs?: ("mn" | "en")[];
  className?: string;
}) {
  const { lang: siteLang } = useLang();
  const { user } = useAuth();
  const t = L[siteLang === "mn" ? "mn" : "en"];
  const [open, setOpen] = useState(false);
  const [count, setCount] = useState<number | "all">("all");
  const [level, setLevel] = useState<0 | 1 | 2 | 3>(0);
  const [answers, setAnswers] = useState<"none" | "key">("key");
  const [space, setSpace] = useState(false);
  const [nameLine, setNameLine] = useState(true);
  const bilingual = langs.length > 1;
  const preferred = siteLang === "mn" ? "mn" : "en";
  const [pdfLang, setPdfLang] = useState<"mn" | "en">(langs.includes(preferred) ? preferred : langs[0]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [fallback, setFallback] = useState<string | null>(null);

  const isBank = source.kind === "bank";

  async function download() {
    setBusy(true);
    setError(null);
    setFallback(null);
    const full: PdfSource =
      source.kind === "bank" ? { ...source, level, count } : source;
    try {
      const res = await fetchWithAuth("/api/pdf", {
        method: "POST",
        body: JSON.stringify({ ...full, lang: pdfLang, answers, space, nameLine, mode: "pdf" }),
      });
      if (res.ok && res.headers.get("content-type")?.includes("application/pdf")) {
        const blob = await res.blob();
        const disposition = res.headers.get("content-disposition") ?? "";
        const name = disposition.split("filename=")[1]?.replace(/["']/g, "").trim() || "MongolPotential.pdf";
        const href = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = href;
        a.download = name;
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(() => URL.revokeObjectURL(href), 10_000);
        setOpen(false);
        return;
      }
      const json = (await res.json().catch(() => ({}))) as { fallback?: string };
      if (res.status === 401) setError(t.signIn);
      else if (res.status === 429) setError(t.limited);
      else {
        setError(t.failed);
        if (json.fallback) setFallback(json.fallback);
      }
    } catch {
      setError(t.failed);
    } finally {
      setBusy(false);
    }
  }

  if (!user) return null;

  const chip = (active: boolean) =>
    ({
      padding: "6px 10px",
      fontSize: 13,
      borderRadius: 8,
      border: `1px solid ${active ? "var(--accent)" : "var(--line)"}`,
      background: active ? "var(--accent-wash)" : "transparent",
      color: active ? "var(--accent)" : "var(--fg-1)",
    }) as const;

  return (
    <>
      <button type="button" onClick={() => setOpen(true)} className={className}>
        <Download className="h-3.5 w-3.5" /> {t.button}
      </button>
      {open && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center p-4"
          style={{ background: "rgba(0,0,0,0.45)" }}
          onClick={() => !busy && setOpen(false)}
          role="dialog"
          aria-modal="true"
          aria-label={t.title}
        >
          <div
            className="w-full max-w-md rounded-2xl p-5 space-y-4 max-h-[90vh] overflow-y-auto"
            style={{ background: "var(--bg)", border: "1px solid var(--line)" }}
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between">
              <h2 className="serif" style={{ fontSize: 22, fontWeight: 400, margin: 0 }}>{t.title}</h2>
              <button type="button" onClick={() => setOpen(false)} aria-label="Close" style={{ color: "var(--fg-2)" }}>
                <X className="h-5 w-5" />
              </button>
            </div>

            {isBank && (
              <>
                <fieldset>
                  <legend className="eyebrow mb-2">{t.problems}</legend>
                  <div className="flex flex-wrap gap-2">
                    {[...COUNT_CHOICES, "all" as const].map((c) => (
                      <button key={c} type="button" style={chip(count === c)} onClick={() => setCount(c)}>
                        {c === "all" ? t.all : t.first(c)}
                      </button>
                    ))}
                  </div>
                </fieldset>
                <fieldset>
                  <legend className="eyebrow mb-2">{t.level}</legend>
                  <div className="flex flex-wrap gap-2">
                    {([0, 1, 2, 3] as const).map((l) => (
                      <button key={l} type="button" style={chip(level === l)} onClick={() => setLevel(l)}>
                        {l === 0 ? t.anyLevel : t.levelN(l)}
                      </button>
                    ))}
                  </div>
                </fieldset>
              </>
            )}

            <fieldset>
              <legend className="eyebrow mb-2">{t.answers}</legend>
              <div className="flex flex-wrap gap-2">
                <button type="button" style={chip(answers === "none")} onClick={() => setAnswers("none")}>{t.noAnswers}</button>
                <button type="button" style={chip(answers === "key")} onClick={() => setAnswers("key")}>{t.key}</button>
              </div>
              {answers === "key" && (
                <p className="mt-2 text-[12px]" style={{ color: "var(--fg-3)" }}>{t.keyNote}</p>
              )}
            </fieldset>

            {bilingual && (
              <fieldset>
                <legend className="eyebrow mb-2">{t.language}</legend>
                <div className="flex gap-2">
                  <button type="button" style={chip(pdfLang === "mn")} onClick={() => setPdfLang("mn")}>Монгол</button>
                  <button type="button" style={chip(pdfLang === "en")} onClick={() => setPdfLang("en")}>English</button>
                </div>
              </fieldset>
            )}

            <div className="space-y-2 text-[14px]" style={{ color: "var(--fg-1)" }}>
              <label className="flex items-center gap-2">
                <input type="checkbox" checked={space} onChange={(e) => setSpace(e.target.checked)} /> {t.space}
              </label>
              <label className="flex items-center gap-2">
                <input type="checkbox" checked={nameLine} onChange={(e) => setNameLine(e.target.checked)} /> {t.nameLine}
              </label>
            </div>

            {error && (
              <div className="text-[13px] space-y-2" style={{ color: "#c05a49" }}>
                <p>{error}</p>
                {fallback && (
                  <a href={fallback} target="_blank" rel="noopener" className="btn btn-line text-[13px]">
                    <Printer className="h-3.5 w-3.5" /> {t.openPrint}
                  </a>
                )}
              </div>
            )}

            <button type="button" onClick={download} disabled={busy} className="btn btn-primary w-full text-[14px]">
              {busy ? <Loader2 className="h-4 w-4 animate-spin" /> : <Download className="h-4 w-4" />}
              {busy ? t.working : t.download}
            </button>
          </div>
        </div>
      )}
    </>
  );
}
