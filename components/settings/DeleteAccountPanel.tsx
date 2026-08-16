"use client";

// Deleting the account itself — kept apart from DataErasePanel on purpose.
//
// That panel erases WORK and keeps the account; this one ends the account.
// They read similarly and their consequences do not, so they are separate
// cards with separate colours and a password step here that the other does
// not have. A student meaning to clear their SAT history must not be one
// mis-click from deleting everything they own.
//
// Three deliberate frictions, in order of how much they cost the user:
//   1. type the word DELETE — defeats a stray click
//   2. re-enter the password — defeats a borrowed/stolen session, which on a
//      shared family or school device is the realistic threat
//   3. a plain statement of what goes, before either
//
// On success the session is over: the server clears the refresh cookie and we
// clear the local token and every local store, then send the user to the home
// page. Leaving a signed-in-looking UI over a deleted account is its own bug.

import { useState } from "react";
import { useRouter } from "next/navigation";
import { AlertTriangle, Loader2 } from "lucide-react";
import { api, clearToken } from "@/lib/api";
import { eraseLocalScope } from "@/lib/data-erase";
import { useLang } from "@/lib/lang-context";

const i18n = {
  eyebrow: { en: "Account", mn: "Бүртгэл" },
  title: { en: "Delete my account", mn: "Бүртгэлээ устгах" },
  lead: {
    en: "Ends your account and removes everything stored about you: your profile, all answer history, mastery, streaks, achievements and billing history. This cannot be undone.",
    mn: "Таны бүртгэлийг хааж, таны тухай хадгалсан бүх зүйлийг устгана: профайл, бүх хариултын түүх, эзэмшилт, цуврал, амжилт, төлбөрийн түүх. Буцаах боломжгүй.",
  },
  keepsNothing: {
    en: "If you only want to clear your practice history, use “Delete my data” above instead — that keeps your account.",
    mn: "Зөвхөн дадлагын түүхээ цэвэрлэхийг хүсвэл дээрх “Мэдээллээ устгах”-ыг ашиглана уу — тэр тохиолдолд бүртгэл хэвээр үлдэнэ.",
  },
  start: { en: "Delete my account", mn: "Бүртгэлээ устгах" },
  typeLabel: {
    en: "Type DELETE to confirm",
    mn: "Баталгаажуулахын тулд DELETE гэж бичнэ үү",
  },
  passwordLabel: { en: "Your password", mn: "Нууц үг" },
  cancel: { en: "Cancel", mn: "Болих" },
  confirm: { en: "Permanently delete", mn: "Бүрмөсөн устгах" },
  working: { en: "Deleting…", mn: "Устгаж байна…" },
  badPassword: { en: "That password is not correct.", mn: "Нууц үг буруу байна." },
  failed: {
    en: "Your account was not deleted. Nothing has been removed — please try again, or contact us if this keeps happening.",
    mn: "Бүртгэл устгагдсангүй. Юу ч арилаагүй — дахин оролдоно уу, эсвэл давтагдвал бидэнтэй холбогдоно уу.",
  },
  // The one case where the account is gone but rows survived. It must not read
  // as success, and it must tell the student what to do about it.
  partial: {
    en: "Your account was closed, but some records could not be removed. We have logged this — please contact us so we can finish erasing your data.",
    mn: "Таны бүртгэл хаагдсан ч зарим бичлэгийг устгаж чадсангүй. Бид үүнийг бүртгэлээ — мэдээллээ бүрэн устгуулахын тулд бидэнтэй холбогдоно уу.",
  },
};

const CONFIRM_WORD = "DELETE";

export default function DeleteAccountPanel() {
  const { lang } = useLang();
  const router = useRouter();

  const [open, setOpen] = useState(false);
  const [typed, setTyped] = useState("");
  const [password, setPassword] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const armed = typed.trim().toUpperCase() === CONFIRM_WORD && password.length > 0 && !busy;

  const run = async () => {
    if (!armed) return;
    setBusy(true);
    setError(null);
    try {
      await api.account.delete({ password });

      // The account is gone; make this device agree. Local stores would
      // otherwise keep rendering a deleted student's work to whoever uses
      // this browser next.
      eraseLocalScope("all");
      clearToken();
      router.push("/");
    } catch (err) {
      const msg = err instanceof Error ? err.message : "";
      if (/invalid password/i.test(msg)) {
        setError(i18n.badPassword[lang]);
      } else if (/INCOMPLETE/i.test(msg)) {
        setError(i18n.partial[lang]);
      } else {
        setError(i18n.failed[lang]);
      }
      setBusy(false);
    }
  };

  return (
    <div
      className="card-edit p-6 mt-8"
      style={{ scrollMarginTop: 80, borderColor: "var(--danger, #b3261e)" }}
      id="delete-account"
    >
      <div className="eyebrow mb-2" style={{ color: "var(--danger, #b3261e)" }}>
        {i18n.eyebrow[lang]}
      </div>
      <h3
        className="serif"
        style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}
      >
        {i18n.title[lang]}
      </h3>
      <p className="text-[13px] mt-2" style={{ color: "var(--fg-2)" }}>
        {i18n.lead[lang]}
      </p>
      <p className="text-[13px] mt-2 mb-5" style={{ color: "var(--fg-2)" }}>
        {i18n.keepsNothing[lang]}
      </p>

      {!open ? (
        <button
          type="button"
          onClick={() => setOpen(true)}
          className="rounded-md px-4 py-2 text-[13px]"
          style={{ border: "1px solid var(--danger, #b3261e)", color: "var(--danger, #b3261e)" }}
        >
          {i18n.start[lang]}
        </button>
      ) : (
        <div className="rounded-md p-4" style={{ background: "var(--bg-2)" }}>
          <div className="flex items-start gap-2 mb-4">
            <AlertTriangle size={16} style={{ color: "var(--danger, #b3261e)", flexShrink: 0, marginTop: 2 }} />
            <span className="text-[13px]" style={{ color: "var(--fg)" }}>
              {i18n.lead[lang]}
            </span>
          </div>

          <label className="block text-[12px] mb-1" style={{ color: "var(--fg-2)" }}>
            {i18n.typeLabel[lang]}
          </label>
          <input
            type="text"
            value={typed}
            onChange={(e) => setTyped(e.target.value)}
            autoComplete="off"
            className="w-full rounded-md px-3 py-2 text-[13px] mb-3"
            style={{ border: "1px solid var(--border)", background: "var(--bg)", color: "var(--fg)" }}
          />

          <label className="block text-[12px] mb-1" style={{ color: "var(--fg-2)" }}>
            {i18n.passwordLabel[lang]}
          </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
            className="w-full rounded-md px-3 py-2 text-[13px]"
            style={{ border: "1px solid var(--border)", background: "var(--bg)", color: "var(--fg)" }}
          />

          {error && (
            <p className="text-[13px] mt-3" style={{ color: "var(--danger, #b3261e)" }}>
              {error}
            </p>
          )}

          <div className="flex gap-2 mt-4">
            <button
              type="button"
              onClick={() => {
                setOpen(false);
                setTyped("");
                setPassword("");
                setError(null);
              }}
              disabled={busy}
              className="rounded-md px-4 py-2 text-[13px]"
              style={{ border: "1px solid var(--border)", color: "var(--fg-2)" }}
            >
              {i18n.cancel[lang]}
            </button>
            <button
              type="button"
              onClick={run}
              disabled={!armed}
              className="rounded-md px-4 py-2 text-[13px] inline-flex items-center gap-2"
              style={{
                background: armed ? "var(--danger, #b3261e)" : "var(--bg-2)",
                color: armed ? "#fff" : "var(--fg-3, var(--fg-2))",
                border: "1px solid var(--danger, #b3261e)",
                opacity: armed ? 1 : 0.5,
              }}
            >
              {busy && <Loader2 size={14} className="animate-spin" />}
              {busy ? i18n.working[lang] : i18n.confirm[lang]}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
