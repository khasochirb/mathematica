"use client";

import Link from "next/link";
import { Lock } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";
import { useLang } from "@/lib/lang-context";
import { isTopicFree } from "@/lib/course-access";

// A topic card that knows whether the reader may open it.
//
// Drop-in for the <Link> that wraps a topic/unit card on a course hub: same
// className and children, plus courseKey + topicSlug. When the topic is
// Premium and the reader is not subscribed, the card renders as a button
// that opens the upgrade modal — still showing its title, blurb and lesson
// count, dimmed, with a lock and a PREMIUM chip. Students see what they
// would get; search engines still index the catalog.
export default function TopicLink({
  courseKey,
  topicSlug,
  href,
  className,
  style,
  children,
  onMouseEnter,
  onMouseLeave,
}: {
  courseKey: string;
  topicSlug: string;
  href: string;
  className?: string;
  style?: React.CSSProperties;
  children: React.ReactNode;
  // Hover-accent handlers some hubs pass. Applied only when the card is
  // unlocked — a locked card should not light up as if it were clickable
  // through to the topic.
  onMouseEnter?: React.MouseEventHandler<HTMLAnchorElement>;
  onMouseLeave?: React.MouseEventHandler<HTMLAnchorElement>;
}) {
  const { isSubscribed } = useAuth();
  const { open: openUpgrade } = useUpgradeModal();
  const { lang } = useLang();
  const mn = lang === "mn";

  const locked = !isSubscribed && !isTopicFree(courseKey, topicSlug);

  if (!locked) {
    return (
      <Link
        href={href}
        className={className}
        style={style}
        onMouseEnter={onMouseEnter}
        onMouseLeave={onMouseLeave}
      >
        {children}
      </Link>
    );
  }

  // The locked card keeps the SAME className as the unlocked one so its own
  // flex layout still applies to the children (wrapping them in a dimming
  // <span> collapses the card's columns). Dimming goes on the button; the
  // Premium chip sits in an absolutely-positioned sibling at full opacity.
  return (
    <span className="relative block">
      <span
        className="absolute top-3 right-3 inline-flex items-center gap-1 mono uppercase rounded-full px-1.5 py-[2px] pointer-events-none"
        style={{
          fontSize: 9,
          letterSpacing: "0.08em",
          background: "color-mix(in oklch, var(--warn) 14%, var(--bg))",
          border: "1px solid color-mix(in oklch, var(--warn) 40%, transparent)",
          color: "var(--warn, #d89620)",
        }}
      >
        <Lock style={{ width: 9, height: 9 }} />
        {mn ? "Премиум" : "Premium"}
      </span>
      <button
        type="button"
        onClick={() => openUpgrade({ source: "course_topic_lock" })}
        className={`${className ?? ""} w-full text-left`}
        style={{ ...style, opacity: 0.55, cursor: "pointer" }}
        aria-label={`${mn ? "Премиум эрхээр нээнэ" : "Unlock with Premium"}`}
      >
        {children}
      </button>
    </span>
  );
}

// The one-line footnote a course hub prints under its topic grid, naming the
// free sample so the offer is legible without opening anything.
export function FreeTopicNote({ courseKey }: { courseKey: string }) {
  const { isSubscribed } = useAuth();
  const { lang } = useLang();
  if (isSubscribed) return null;
  const mn = lang === "mn";
  return (
    <p className="text-[13px] mt-6" style={{ color: "var(--fg-3)" }}>
      {mn
        ? "Эхний сэдэв үнэгүй. Үлдсэнийг Премиум эрхээр нээнэ."
        : "The first topic is free. Premium opens the rest of the course."}
    </p>
  );
}
