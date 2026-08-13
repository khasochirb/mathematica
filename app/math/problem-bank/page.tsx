"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Layers, Lock, PencilLine, Repeat2 } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { loadBankProgress } from "@/lib/problem-bank";
import {
  courseLadderManifest,
  manifestMastery,
  type BankTopicMeta,
} from "@/lib/bank-manifest";

// The Problem Bank hub — leveled drilling across every exam form, with
// per-form mastery tracked on this device (account-keyed). Renders from the
// ~55 KB manifest, NOT the corpus: this page lists topics, it never shows a
// problem, so it must not ship 9 MB of them (see lib/bank-data.ts).
export default function ProblemBankHub() {
  const { user } = useAuth();
  const topics = courseLadderManifest();
  const [mastery, setMastery] = useState<Record<string, { mastered: number; total: number }>>({});

  useEffect(() => {
    const m: Record<string, { mastered: number; total: number }> = {};
    for (const t of topics) {
      m[t.slug] = manifestMastery(t, loadBankProgress(t.slug, user?.id));
    }
    setMastery(m);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user?.id]);

  const totalProblems = topics.reduce((n, t) => n + t.problemCount, 0);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">Courses · Practice</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 54px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
          Problem Bank
        </h1>
        <p className="mt-4 mb-2" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "58ch" }}>
          {totalProblems} problems organized exactly like the courses: pick a
          subject, pick the unit you just finished, and work its collection —
          as an exercise set or as a practice run where missing a problem
          brings back a similar one until you&apos;ve got it. Nothing here
          reveals its answer until you&apos;ve entered one.
        </p>
        <div className="mb-8 flex flex-wrap gap-3 text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="inline-flex items-center gap-1.5"><Layers className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} /> Level 1 basics · Level 2 standard · Level 3 exam</span>
          <span className="inline-flex items-center gap-1.5"><PencilLine className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} /> Answer first, solution after</span>
          <span className="inline-flex items-center gap-1.5"><Repeat2 className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} /> Miss → practice a similar one</span>
        </div>

        <div className="space-y-3">
          {topics.map((t) => (
            <TopicCard key={t.slug} topic={t} mastery={mastery[t.slug]} />
          ))}
        </div>

        <BankAccessNote />
      </div>
    </div>
  );
}

// The bank is Premium material. Say so here, at the top of the funnel, so
// nobody works down to a unit before meeting the wall.
function BankAccessNote() {
  const { isSubscribed } = useAuth();
  if (isSubscribed) return null;
  return (
    <div
      className="mt-8 rounded-xl px-4 py-3 flex items-start gap-2.5 text-[13px]"
      style={{
        background: "color-mix(in oklch, var(--warn) 8%, var(--bg))",
        border: "1px solid color-mix(in oklch, var(--warn) 30%, transparent)",
        color: "var(--fg-1)",
      }}
    >
      <Lock className="mt-[3px] h-3.5 w-3.5 flex-shrink-0" style={{ color: "var(--warn, #d89620)" }} />
      <span>
        The Problem Bank is a Premium feature. Every subject opens its{" "}
        <b>first unit free</b> so you can try it — Premium unlocks the rest.
      </span>
    </div>
  );
}

function TopicCard({ topic, mastery }: { topic: BankTopicMeta; mastery?: { mastered: number; total: number } }) {
  const byLevel = [1, 2, 3].map((lv) => topic.forms.filter((f) => f.level === lv).length);
  const pct = mastery && mastery.total > 0 ? Math.round((mastery.mastered / mastery.total) * 100) : 0;
  return (
    <Link
      href={`/math/problem-bank/${topic.slug}`}
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
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 flex-wrap">
          <span className="serif" style={{ fontWeight: 400, fontSize: 19, letterSpacing: "-0.01em", color: "var(--fg)" }}>
            {topic.title}
          </span>
          <span className="mono text-[11px]" style={{ color: "var(--fg-3)" }}>{topic.titleMn}</span>
        </div>
        <p className="mt-1 text-[13px]" style={{ color: "var(--fg-2)" }}>{topic.blurb}</p>
        <div className="mt-2 flex items-center gap-2 flex-wrap text-[11px] mono" style={{ color: "var(--fg-3)" }}>
          <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>{topic.unitCount} units</span>
          <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>{topic.problemCount} problems</span>
          <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>L1 ×{byLevel[0]} · L2 ×{byLevel[1]} · L3 ×{byLevel[2]}</span>
        </div>
        {mastery && mastery.mastered > 0 && (
          <div className="mt-2.5 flex items-center gap-2">
            <div className="h-1.5 flex-1 max-w-[220px] overflow-hidden rounded-full" style={{ background: "var(--bg-2)" }}>
              <div className="h-full rounded-full" style={{ width: `${pct}%`, background: "#3fb27f" }} />
            </div>
            <span className="mono text-[11px] tabular" style={{ color: "var(--fg-3)" }}>
              {mastery.mastered}/{mastery.total} forms mastered
            </span>
          </div>
        )}
      </div>
      <ArrowRight className="h-4 w-4 flex-shrink-0 mt-1.5" style={{ color: "var(--fg-3)" }} />
    </Link>
  );
}
