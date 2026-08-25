"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import PreferencesPanel from "@/components/settings/PreferencesPanel";
import DataErasePanel from "@/components/settings/DataErasePanel";
import DeleteAccountPanel from "@/components/settings/DeleteAccountPanel";

// Account settings.
//
// WHY THIS PAGE EXISTS. Erasure and account deletion used to live at the
// bottom of /analytics. That page is the ЭШ score report — lib/perf-context.ts
// maps only ЭШ contexts to it, and both /eysh-analytics and the ЭШ hub's
// progress tab redirect into it. So a student who only ever took SAT or IB
// had NO ROUTE TO DELETE THEIR ACCOUNT AT ALL. Not a hard one to find: none.
// On a product whose users are minors, that is the thing that has to work.
//
// WHY /dashboard/settings AND NOT /settings. Product rule 4: the top-level
// route budget is fixed at what exists today, and adding one needs Khas's
// explicit call. /dashboard already exists, so a child segment of it spends
// nothing. It is also the only signed-in-shaped top-level route there is.
//
// The gate is here rather than in a dashboard layout on purpose:
// /dashboard itself renders for signed-out visitors
// (components/dashboard/DashboardHome.tsx uses `user` optionally), and a
// layout gate would silently change that page too.
export default function SettingsPage() {
  const { user, isLoading } = useAuth();
  const { lang } = useLang();
  const router = useRouter();
  const mn = lang === "mn";

  useEffect(() => {
    if (!isLoading && !user) {
      router.replace(`/sign-in?next=${encodeURIComponent("/dashboard/settings")}`);
    }
  }, [isLoading, user, router]);

  if (isLoading || !user) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <p className="mono text-[12px]" style={{ color: "var(--fg-3)" }}>
            {mn ? "Ачааллаж байна…" : "Loading…"}
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8 pb-6" style={{ borderBottom: "1px solid var(--line)" }}>
          <div className="eyebrow mb-1.5">{mn ? "Бүртгэл" : "Account"}</div>
          <h1
            className="serif"
            style={{
              fontWeight: 400,
              fontSize: "clamp(32px, 4vw, 44px)",
              letterSpacing: "-0.03em",
              lineHeight: 1,
              color: "var(--fg)",
            }}
          >
            {mn ? "Тохиргоо" : "Settings"}
          </h1>
          <p className="mono mt-2 text-[12px]" style={{ color: "var(--fg-2)" }}>
            {user.displayName || user.username} · {user.email}
          </p>
        </div>

        {/* Identity is READ-ONLY for now, and says so rather than offering a
            field that does nothing. Changing a display name needs a server
            route (client UPDATE on profiles is revoked — migration 016), and
            changing an email needs a mail provider the site does not have
            yet, so a half-built email change would strand a student between
            two unconfirmed addresses. */}
        <div className="card-edit p-6">
          <div className="eyebrow">{mn ? "Таны бүртгэл" : "Your account"}</div>
          <h2
            className="serif mt-1"
            style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", lineHeight: 1.1 }}
          >
            {user.displayName || user.username}
          </h2>
          <dl className="mt-4 text-[13px]">
            {[
              [mn ? "Хэрэглэгчийн нэр" : "Username", user.username],
              [mn ? "И-мэйл" : "Email", user.email],
              ...(user.grade ? [[mn ? "Анги" : "Grade", user.grade] as const] : []),
            ].map(([k, v]) => (
              <div key={k} className="flex justify-between gap-4 py-1.5">
                <dt style={{ color: "var(--fg-3)" }}>{k}</dt>
                <dd className="mono" style={{ color: "var(--fg-1)" }}>
                  {v}
                </dd>
              </div>
            ))}
          </dl>
          <p className="text-[12px] mt-3" style={{ color: "var(--fg-3)" }}>
            {mn ? (
              <>
                Эдгээрийг өөрчлөхийн тулд{" "}
                <Link href="/contact" style={{ color: "var(--accent)" }}>
                  бидэнтэй холбогдоно уу
                </Link>
                .
              </>
            ) : (
              <>
                To change any of these,{" "}
                <Link href="/contact" style={{ color: "var(--accent)" }}>
                  get in touch
                </Link>{" "}
                — self-service editing is not built yet.
              </>
            )}
          </p>
        </div>

        <PreferencesPanel />

        {/* Erasure, then account deletion, in that order and never merged:
            one keeps the account and the other ends it. DeleteAccountPanel's
            own copy points the reader back up to "Delete my data", so the
            order is load-bearing, not cosmetic. */}
        <DataErasePanel />
        <DeleteAccountPanel />
      </div>
    </div>
  );
}
