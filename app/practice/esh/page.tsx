"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import {
  FileText,
  Target,
  BookOpen,
  BarChart3,
  ChevronRight,
  Archive,
} from "lucide-react";
import ComingSoonBadge from "@/components/ComingSoonBadge";
import useESHProgress from "@/lib/use-esh-progress";
import {
  getTestsForUser,
  getQuestionsForUser,
} from "@/lib/esh-questions";
import { useAuth } from "@/lib/auth-context";
import {
  COMING_SOON_FEATURES,
  useUpgradeModal,
} from "@/lib/upgrade-modal-context";
import { useLang } from "@/lib/lang-context";
import { HubShell, HubHero, HubSection, HubRowLink } from "@/components/hub/HubKit";

// ЭЕШ hub content is MONGOLIAN by design (content language is a hub
// property — memory/expansion-vision.md §4.7).
//
// Structure comes from HubKit and matches the SAT and IB hubs exactly:
// hero → tests → course → practice by topic → progress — followed by the
// ЭЕШ-specific extras (stats, recommendation, recent sittings, roadmap).
export default function ESHHubPage() {
  const [mounted, setMounted] = useState(false);
  const progress = useESHProgress();
  const { isAuthenticated, isSubscribed } = useAuth();
  const upgrade = useUpgradeModal();
  const { lang } = useLang();

  useEffect(() => setMounted(true), []);

  const allTests = getTestsForUser(isSubscribed);
  const totalQuestions = getQuestionsForUser(isSubscribed).length;

  // Anonymous click on the progress row falls through to sign-in with a
  // next-path back to progress, matching the test-gating pattern.
  const progressHref = isAuthenticated
    ? "/analytics"
    : `/sign-in?next=${encodeURIComponent("/analytics")}`;

  return (
    <HubShell>
      <HubHero
        eyebrow="ЭЕШ · Математик"
        title="ЭЕШ математик, "
        accent="бодитоор"
        titleAfter="."
        lede="Өмнөх жилийн бодит шалгалтууд бүрэн бодолттой, сэдэв бүрийн
          хичээл ба дадлага, сул талыг чинь олж заадаг ахицын хяналт — бүгд
          нэг дор."
        statsLine={
          <>
            <span className="tabular">{allTests.length}</span> тест ·{" "}
            <span className="tabular">{totalQuestions}</span> бодлого
          </>
        }
      />

      {/* Recommendation banner — data-driven nudge, ЭЕШ-specific extra. */}
      {mounted && progress.practiceRecommendation && (
        <div
          className="mt-6 p-5 flex gap-3 items-start"
          style={{
            background: "var(--accent-wash)",
            border: "1px solid var(--accent-line)",
            borderRadius: 12,
          }}
        >
          <span className="badge-edit badge-accent">ЗӨВЛӨГӨӨ</span>
          <p className="serif text-[15px] leading-snug" style={{ color: "var(--fg-1)" }}>
            {progress.practiceRecommendation}
          </p>
        </div>
      )}

      <HubSection label="Бодит шалгалт">
        <div className="space-y-3">
          <HubRowLink
            href="/practice/esh/test?type=previous"
            icon={Archive}
            title="Өмнө жилийн тестүүд"
            badge="Үнэгүй"
            desc="Бодит шалгалт · 20 тест · Бүрэн бодолттой"
          />
          <HubRowLink
            href="/practice/esh/test?type=premium"
            icon={FileText}
            title="Дадлага тестүүд"
            badge="Түгжээтэй"
            badgeTone="muted"
            desc="Premium · 14 тест · Багш нарын зохиосон нэмэлт тестүүд"
          />
        </div>
      </HubSection>

      <HubSection label="Сэдвээр суралцах">
        <HubRowLink
          href="/practice/esh/topics"
          icon={BookOpen}
          title="ЭЕШ-ийн сэдвүүд"
          desc="Шалгалтын жингээр эрэмбэлсэн сэдвүүд — хичээл, дадлага, тест
            сэдэв бүрд"
        />
      </HubSection>

      <HubSection label="Сэдвээр дадлагажих">
        <HubRowLink
          href="/practice/esh/practice"
          icon={Target}
          title="Сул талаа сайжруулах"
          desc="Алдсан сэдвүүд дээр чинь тохируулсан дадлага — алдах бүрд
            төстэй бодлого дараалалд нэмэгдэнэ"
        />
      </HubSection>

      <HubSection label="Ахиц">
        <HubRowLink
          href={progressHref}
          icon={BarChart3}
          title="Гүйцэтгэлийн дэлгэрэнгүй"
          desc={
            mounted && progress.totalTestsTaken > 0
              ? `${progress.averageAccuracy}% дундаж · ${progress.totalTestsTaken} тест бодсон`
              : "Тест бодож эхлээд ахицаа хяна"
          }
        />
      </HubSection>

      {/* Quick stats strip — appears once there is history. */}
      {mounted && progress.totalTestsTaken > 0 && (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-px mt-10" style={{ background: "var(--line)" }}>
          {[
            { lbl: "Тест бодсон", v: progress.totalTestsTaken },
            { lbl: "Бодлого бодсон", v: progress.totalQuestionsAnswered },
            { lbl: "Энэ долоо хоногт", v: progress.weeklyActivity.thisWeek },
            { lbl: "Тэмдэглэсэн", v: progress.flaggedCount },
          ].map((s) => (
            <div key={s.lbl} className="p-5" style={{ background: "var(--bg)" }}>
              <div className="eyebrow">{s.lbl}</div>
              <div
                className="serif tabular mt-2"
                style={{ fontSize: 28, letterSpacing: "-0.02em", color: "var(--fg)" }}
              >
                {s.v}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Recent test results */}
      {mounted && progress.completedSessions.length > 0 && (
        <div className="mt-10">
          <div className="eyebrow mb-3">Сүүлийн шалгалтууд</div>
          <div
            style={{
              border: "1px solid var(--line)",
              borderRadius: 12,
              overflow: "hidden",
            }}
          >
            {progress.completedSessions.slice(0, 5).map((s, i) => (
              <Link
                key={s.id}
                href={`/practice/esh/test/${s.testKey.toLowerCase()}/results?session=${s.id}`}
                className="flex items-center gap-4 px-5 py-3.5 transition-colors hover:opacity-90"
                style={{
                  background: "var(--bg-1)",
                  borderTop: i === 0 ? "none" : "1px solid var(--line)",
                }}
              >
                <span
                  className="badge-edit"
                  style={{
                    minWidth: 44,
                    justifyContent: "center",
                    color: "var(--accent)",
                    borderColor: "var(--accent-line)",
                    background: "var(--accent-wash)",
                  }}
                >
                  {s.testKey}
                </span>
                <div className="flex-1 min-w-0">
                  <div className="text-[14px]" style={{ color: "var(--fg)" }}>
                    Тест {s.testKey}
                  </div>
                  {s.completedAt && (
                    <div
                      className="mono tabular text-[11px] mt-0.5"
                      style={{ color: "var(--fg-3)" }}
                    >
                      {new Date(s.completedAt).toLocaleDateString("mn-MN")}
                    </div>
                  )}
                </div>
                <span
                  className="serif tabular"
                  style={{
                    fontSize: 18,
                    letterSpacing: "-0.01em",
                    color:
                      (s.score?.accuracy || 0) >= 80
                        ? "var(--accent)"
                        : (s.score?.accuracy || 0) >= 50
                          ? "var(--warn)"
                          : "var(--danger)",
                  }}
                >
                  {s.score?.accuracy || 0}%
                </span>
                <ChevronRight className="w-4 h-4" style={{ color: "var(--fg-3)" }} />
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Coming Soon — aggregated roadmap surface. One block, per-feature
          waitlist source for conversion research. No routes. */}
      <div
        className="mt-10 rounded-xl overflow-hidden"
        style={{ border: "1px solid var(--line)" }}
      >
        <div
          className="px-5 py-4 flex items-center justify-between gap-3"
          style={{ background: "var(--bg-1)", borderBottom: "1px solid var(--line)" }}
        >
          <div>
            <div className="eyebrow">Удахгүй</div>
            <h3
              className="serif mt-1"
              style={{
                fontWeight: 400,
                fontSize: 20,
                letterSpacing: "-0.02em",
                color: "var(--fg)",
              }}
            >
              Бэлдэж буй боломжууд
            </h3>
          </div>
          <ComingSoonBadge />
        </div>
        <ul>
          {COMING_SOON_FEATURES.map((f, i) => {
            const Icon = f.icon;
            const title = lang === "mn" ? f.title.mn : f.title.en;
            const desc = lang === "mn" ? f.desc.mn : f.desc.en;
            return (
              <li key={f.key}>
                <button
                  type="button"
                  onClick={() =>
                    upgrade.open({
                      source: f.source,
                      title,
                      description: desc,
                    })
                  }
                  className="w-full text-left px-5 py-4 flex items-center gap-4 transition-colors hover:opacity-90"
                  style={{
                    background: "var(--bg)",
                    borderTop: i === 0 ? "none" : "1px solid var(--line)",
                  }}
                >
                  <span
                    className="w-9 h-9 rounded-md flex items-center justify-center shrink-0"
                    style={{
                      background: "var(--bg-2)",
                      border: "1px solid var(--line)",
                      color: "var(--fg-2)",
                    }}
                  >
                    <Icon className="w-4 h-4" />
                  </span>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="text-[14px]" style={{ color: "var(--fg)" }}>
                        {title}
                      </span>
                      <ComingSoonBadge variant="inline" />
                    </div>
                    <p className="text-[12.5px] mt-0.5" style={{ color: "var(--fg-2)" }}>
                      {desc}
                    </p>
                  </div>
                  <span
                    className="mono text-[10px] uppercase shrink-0"
                    style={{ color: "var(--accent)", letterSpacing: "0.08em" }}
                  >
                    Мэдэгдэх →
                  </span>
                </button>
              </li>
            );
          })}
        </ul>
      </div>
    </HubShell>
  );
}
