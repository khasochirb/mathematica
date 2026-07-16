"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Layers, Repeat2 } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import {
  getBankTopics,
  loadBankProgress,
  topicMastery,
  type BankTopic,
} from "@/lib/problem-bank";

// The Problem Bank hub — leveled drilling across every exam form, with
// per-form mastery tracked on this device (account-keyed).
export default function ProblemBankHub() {
  const { user } = useAuth();
  const topics = getBankTopics();
  const [mastery, setMastery] = useState<Record<string, { mastered: number; total: number }>>({});

  useEffect(() => {
    const m: Record<string, { mastered: number; total: number }> = {};
    for (const t of topics) {
      m[t.slug] = topicMastery(t, loadBankProgress(t.slug, user?.id));
    }
    setMastery(m);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [user?.id]);

  const totalProblems = topics.reduce(
    (n, t) => n + t.forms.reduce((k, f) => k + f.variants.length, 0),
    0,
  );

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/math" className="p-2 rounded-md transition-colors" style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">General Math · Practice</div>
        </div>

        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(32px, 5vw, 54px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}>
          Problem Bank
        </h1>
        <p className="mt-4 mb-2" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "58ch" }}>
          {totalProblems} problems organized exactly like the courses: pick a
          subject, pick the unit you just finished, and work its collection —
          on paper with reveal-to-check, or as a practice set where missing a
          problem brings back a similar one until you've got it.
        </p>
        <div className="mb-8 flex flex-wrap gap-3 text-[13px]" style={{ color: "var(--fg-2)" }}>
          <span className="inline-flex items-center gap-1.5"><Layers className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} /> Level 1 basics · Level 2 standard · Level 3 exam</span>
          <span className="inline-flex items-center gap-1.5"><Repeat2 className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} /> Miss → practice a similar one</span>
        </div>

        <div className="space-y-3">
          {topics.map((t) => (
            <TopicCard key={t.slug} topic={t} mastery={mastery[t.slug]} />
          ))}
        </div>
      </div>
    </div>
  );
}

function TopicCard({ topic, mastery }: { topic: BankTopic; mastery?: { mastered: number; total: number } }) {
  const problems = topic.forms.reduce((n, f) => n + f.variants.length, 0);
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
          <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>{topic.units.length} units</span>
          <span className="rounded-full px-2 py-0.5" style={{ background: "var(--bg-2)", border: "1px solid var(--line)" }}>{problems} problems</span>
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
