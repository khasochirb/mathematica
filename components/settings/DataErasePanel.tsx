"use client";

// Account-wide data erasure, in one place, with an honest report.
//
// Deliberately NOT a single "delete everything" button: a student who wants
// their SAT history gone rarely wants their two years of ЭЕШ work gone with
// it. Each scope names exactly what it removes and what it leaves alone, and
// a server failure is surfaced rather than swallowed — the local copy going
// away while the server keeps the rows means the data reappears at the next
// sync, and a student who believes it is deleted is worse off than one who
// knows it failed.

import { useState } from "react";
import { Trash2, AlertTriangle, Check } from "lucide-react";
import usePerformance from "@/lib/use-performance";
import useTestSession from "@/lib/use-test-session";
import useFlaggedQuestions from "@/lib/use-flagged-questions";
import { eraseLocalScope, eraseSummary, type EraseScope } from "@/lib/data-erase";
import { useLang } from "@/lib/lang-context";

type Offered = Exclude<EraseScope, never>;

const SCOPE_LABEL: Record<Offered, { en: string; mn: string }> = {
  esh: { en: "ЭЕШ", mn: "ЭЕШ" },
  sat: { en: "SAT", mn: "SAT" },
  ib: { en: "IB", mn: "IB" },
  courses: { en: "Courses", mn: "Курсууд" },
  all: { en: "Everything", mn: "Бүгд" },
};

const SCOPE_NOTE: Record<Offered, { en: string; mn: string }> = {
  esh: {
    en: "Past-paper sittings, topic drills, flagged questions.",
    mn: "Шалгалтын сессүүд, сэдвийн дадлага, тэмдэглэсэн бодлогууд.",
  },
  sat: { en: "Mock-test answers and saved runs.", mn: "Тестийн хариулт ба хадгалсан явц." },
  ib: { en: "Paper answers, self-marking and saved runs.", mn: "Хариулт, өөрийн дүгнэлт, хадгалсан явц." },
  courses: {
    en: "Lesson checks, problem-bank mastery, placement and exam results.",
    mn: "Хичээлийн шалгалт, бодлогын сан, түвшин тогтоох ба шалгалтын дүн.",
  },
  all: {
    en: "Every hub and every course. Your account itself is kept.",
    mn: "Бүх хэсэг, бүх курс. Бүртгэл өөрөө хэвээр үлдэнэ.",
  },
};

const i18n = {
  eyebrow: { en: "Your data", mn: "Таны мэдээлэл" },
  title: { en: "Delete my data", mn: "Мэдээллээ устгах" },
  lead: {
    en: "Choose what to remove. Deleting one section never touches the others.",
    mn: "Юуг устгахаа сонгоно уу. Нэг хэсгийг устгахад бусад нь хэвээр үлдэнэ.",
  },
  confirmTitle: { en: "This cannot be undone", mn: "Буцаах боломжгүй" },
  willRemove: { en: "This removes:", mn: "Дараах зүйлс арилна:" },
  cancel: { en: "Cancel", mn: "Болих" },
  confirm: { en: "Delete", mn: "Устгах" },
  working: { en: "Deleting…", mn: "Устгаж байна…" },
  doneTitle: { en: "Deleted", mn: "Устгагдлаа" },
  doneBody: {
    en: (n: number) => `${n} recorded answer${n === 1 ? "" : "s"} removed, on this device and on the server.`,
    mn: (n: number) => `${n} хариулт энэ төхөөрөмж болон серверээс ариллаа.`,
  },
  failTitle: { en: "Not fully deleted", mn: "Бүрэн устгагдсангүй" },
  failBody: {
    en: "This device is clear, but the server copy could not be reached — the data will come back on the next sync. Check your connection and try again.",
    mn: "Энэ төхөөрөмж цэвэрлэгдсэн ч сервер лүү холбогдож чадсангүй — дараагийн синкээр эргэн гарч ирнэ. Холболтоо шалгаад дахин оролдоно уу.",
  },
  ok: { en: "OK", mn: "Ойлголоо" },
};

export default function DataErasePanel({
  scopes = ["esh", "sat", "ib", "courses", "all"],
}: {
  scopes?: Offered[];
}) {
  const { lang } = useLang();
  const perf = usePerformance();
  const testSession = useTestSession();
  const flagged = useFlaggedQuestions();

  const [pending, setPending] = useState<Offered | null>(null);
  const [busy, setBusy] = useState(false);
  const [result, setResult] = useState<{ ok: boolean; removed: number } | null>(null);

  const run = async (scope: Offered) => {
    setBusy(true);
    const { localRemoved, serverOk } = await perf.clearScope(scope);
    eraseLocalScope(scope);
    // These two hooks own ЭЕШ-only stores and hold their own React state, so
    // they need clearing through the hook rather than by key alone — otherwise
    // the page keeps rendering from memory until a reload.
    if (scope === "esh" || scope === "all") {
      testSession.clearAll();
      flagged.clearAll();
    }
    setBusy(false);
    setPending(null);
    setResult({ ok: serverOk, removed: localRemoved });
  };

  return (
    <div className="card-edit p-6 mt-8" style={{ scrollMarginTop: 80 }} id="data">
      <div className="eyebrow mb-2">{i18n.eyebrow[lang]}</div>
      <h3 className="serif" style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}>
        {i18n.title[lang]}
      </h3>
      <p className="text-[13px] mt-2 mb-5" style={{ color: "var(--fg-2)" }}>
        {i18n.lead[lang]}
      </p>

      <div className="space-y-2">
        {scopes.map((scope) => (
          <div
            key={scope}
            className="flex items-start gap-3 rounded-md p-3"
            style={{
              background: "var(--bg-2)",
              border: `1px solid ${scope === "all" ? "color-mix(in oklch, var(--danger) 30%, transparent)" : "var(--line)"}`,
            }}
          >
            <div className="flex-1 min-w-0">
              <p className="text-[14px]" style={{ color: "var(--fg)" }}>
                {SCOPE_LABEL[scope][lang]}
              </p>
              <p className="text-[12px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                {SCOPE_NOTE[scope][lang]}
              </p>
            </div>
            <button
              onClick={() => setPending(scope)}
              className="mono text-[10px] uppercase flex items-center gap-1 shrink-0 mt-1"
              style={{ color: "var(--danger)", letterSpacing: "0.06em" }}
            >
              <Trash2 className="w-3 h-3" />
              {i18n.confirm[lang]}
            </button>
          </div>
        ))}
      </div>

      {pending && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "color-mix(in oklch, var(--bg) 70%, black 30% / 60%)", backdropFilter: "blur(8px)" }}
        >
          <div className="card-edit p-6 max-w-sm w-full" style={{ background: "var(--bg-1)" }}>
            <div className="eyebrow mb-2" style={{ color: "var(--danger)" }}>
              {i18n.confirmTitle[lang]}
            </div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 21, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              {SCOPE_LABEL[pending][lang]}
            </h3>
            <p className="text-[13px] mt-3" style={{ color: "var(--fg-2)" }}>
              {i18n.willRemove[lang]}
            </p>
            <ul className="text-[13px] mt-2 mb-6 space-y-1" style={{ color: "var(--fg-1)" }}>
              {eraseSummary(pending).map((w) => (
                <li key={w} className="flex gap-2">
                  <span style={{ color: "var(--danger)" }}>·</span>
                  {w}
                </li>
              ))}
            </ul>
            <div className="flex gap-2">
              <button onClick={() => setPending(null)} disabled={busy} className="btn btn-line flex-1">
                {i18n.cancel[lang]}
              </button>
              <button
                onClick={() => run(pending)}
                disabled={busy}
                className="btn flex-1"
                style={{
                  background: "color-mix(in oklch, var(--danger) 18%, transparent)",
                  border: "1px solid color-mix(in oklch, var(--danger) 35%, transparent)",
                  color: "var(--danger)",
                  opacity: busy ? 0.6 : 1,
                }}
              >
                {busy ? i18n.working[lang] : i18n.confirm[lang]}
              </button>
            </div>
          </div>
        </div>
      )}

      {result && (
        <div
          className="fixed inset-0 z-50 flex items-center justify-center px-4"
          style={{ background: "color-mix(in oklch, var(--bg) 70%, black 30% / 60%)", backdropFilter: "blur(8px)" }}
        >
          <div className="card-edit p-6 max-w-sm w-full" style={{ background: "var(--bg-1)" }}>
            <div
              className="w-10 h-10 rounded-md flex items-center justify-center mb-4"
              style={{
                background: result.ok ? "var(--accent-wash)" : "color-mix(in oklch, var(--danger) 12%, transparent)",
                color: result.ok ? "var(--accent)" : "var(--danger)",
              }}
            >
              {result.ok ? <Check className="w-5 h-5" /> : <AlertTriangle className="w-5 h-5" />}
            </div>
            <h3 className="serif" style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}>
              {result.ok ? i18n.doneTitle[lang] : i18n.failTitle[lang]}
            </h3>
            <p className="text-[13px] mt-3 mb-6" style={{ color: "var(--fg-2)" }}>
              {result.ok ? i18n.doneBody[lang](result.removed) : i18n.failBody[lang]}
            </p>
            <button onClick={() => setResult(null)} className="btn btn-line w-full">
              {i18n.ok[lang]}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
