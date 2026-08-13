"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, BookOpen } from "lucide-react";
import TopicLink from "@/components/genmath/TopicLink";
import { useAuth } from "@/lib/auth-context";
import { isBankUnitFree } from "@/lib/course-access";
import {
  type BankTopic,
  type BankProgress,
  loadBankProgress,
  unitForms,
  unitMastery,
} from "@/lib/problem-bank";
import { type BankChrome, defaultBankChrome } from "./bank-chrome";

// The subject page: the course's units in taught order, each opening its own
// problem collection. This mirrors /math/<subject> exactly — finish a unit in
// the course, then come here to solidify it against the full collection.
export default function BankUnitList({ topic, chrome }: { topic: BankTopic; chrome?: BankChrome }) {
  const c = chrome ?? defaultBankChrome(topic);
  const { user } = useAuth();
  const [progress, setProgress] = useState<BankProgress | null>(null);

  useEffect(() => {
    setProgress(loadBankProgress(topic.slug, user?.id));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [topic.slug, user?.id]);

  const totalProblems = topic.forms.reduce((n, f) => n + f.variants.length, 0);
  // Hub-owned banks (SAT) have no course spine to read freeness from, so the
  // policy needs this bank's own unit order — see lib/course-access.
  const unitOrder = useMemo(() => topic.units.map((u) => u.id), [topic]);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-20">
        <div className="flex items-center gap-3 mb-6">
          <Link href={c.backHref} className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{c.eyebrow} · {topic.title}</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(30px, 5vw, 48px)", letterSpacing: "-0.04em", lineHeight: 1.02, color: "var(--fg)" }}>
          {topic.title}
        </h1>
        <p className="mt-3 mb-8" style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "58ch" }}>
          <b className="tabular">{totalProblems}</b> problems organized
          {c.courseHref ? (
            <>
              {" "}by the course&apos;s {topic.units.length} units. Finish a unit in the{" "}
              <Link href={c.courseHref} style={{ color: "var(--accent)" }}>
                {topic.title} course
              </Link>
              , then open it here and work the collection.
            </>
          ) : (
            <>
              {" "}into {topic.units.length} units. Pick a unit and work its
              collection — as an exercise set or as a practice run. Either way
              you enter your answer and it gets checked; the solution opens
              after that.
            </>
          )}
        </p>

        <div className="space-y-3">
          {topic.units.map((u, i) => {
            const forms = unitForms(topic, u.id);
            const problems = forms.reduce((n, f) => n + f.variants.length, 0);
            const m = progress ? unitMastery(topic, u.id, progress) : null;
            const pct = m && m.total > 0 ? Math.round((m.mastered / m.total) * 100) : 0;
            return (
              <TopicLink
                key={u.id}
                courseKey={topic.slug}
                topicSlug={u.id}
                free={isBankUnitFree(topic.slug, u.id, unitOrder)}
                upgradeSource="bank_unit_lock"
                href={`${c.topicBase}/${u.id}`}
                className="card-edit p-5 flex items-start gap-4 transition-colors"
                style={{ textDecoration: "none" }}
                onMouseEnter={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "var(--accent-line)";
                  (e.currentTarget as HTMLAnchorElement).style.background = "var(--accent-wash)";
                }}
                onMouseLeave={(e) => {
                  (e.currentTarget as HTMLAnchorElement).style.borderColor = "";
                  (e.currentTarget as HTMLAnchorElement).style.background = "";
                }}
              >
                <span className="mono text-[12px] tabular mt-1.5 flex-shrink-0" style={{ color: "var(--fg-3)" }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div className="flex-1 min-w-0">
                  <span className="serif" style={{ fontWeight: 400, fontSize: 19, letterSpacing: "-0.01em", color: "var(--fg)" }}>
                    {u.title}
                  </span>
                  {u.blurb && (
                    <p className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{u.blurb}</p>
                  )}
                  <div className="mt-2 flex items-center gap-2 flex-wrap text-[11px] mono" style={{ color: "var(--fg-3)" }}>
                    <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
                      {problems} problems
                    </span>
                    <span className="inline-flex items-center gap-1 rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>
                      <BookOpen className="h-3 w-3" /> {forms.length} forms
                    </span>
                  </div>
                  {m && m.mastered > 0 && (
                    <div className="mt-2.5 flex items-center gap-2">
                      <div className="h-1.5 flex-1 max-w-[220px] overflow-hidden rounded-full" style={{ background: "var(--bg-2)" }}>
                        <div className="h-full rounded-full" style={{ width: `${pct}%`, background: "#3fb27f" }} />
                      </div>
                      <span className="mono text-[11px] tabular" style={{ color: "var(--fg-3)" }}>
                        {m.mastered}/{m.total} forms mastered
                      </span>
                    </div>
                  )}
                </div>
                <ArrowRight className="h-4 w-4 flex-shrink-0 mt-1.5" style={{ color: "var(--fg-3)" }} />
              </TopicLink>
            );
          })}
        </div>

        <FreeUnitNote />
      </div>
    </div>
  );
}

// Names the offer under the unit list, so a student reads the wall here
// rather than discovering it after picking a unit.
function FreeUnitNote() {
  const { isSubscribed } = useAuth();
  if (isSubscribed) return null;
  return (
    <p className="text-[13px] mt-6" style={{ color: "var(--fg-3)" }}>
      The first unit is free. Premium opens the rest of the bank.
    </p>
  );
}
