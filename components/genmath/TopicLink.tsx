"use client";

import Link from "next/link";

// A topic card link on a course hub or bank unit list.
//
// Drop-in for the <Link> that wraps a topic/unit card: same className and
// children, plus courseKey + topicSlug so each card still names what it
// opens. Until 2026-11-23 a Premium topic rendered here as a dimmed, locked
// button; the site is now free (policy: lib/course-access.ts), so every card
// is a plain link. Anonymous readers meet the sign-in wall on the content
// route itself (ContentGate), not here — the catalog stays browsable and
// indexable.
export default function TopicLink({
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
  onMouseEnter?: React.MouseEventHandler<HTMLAnchorElement>;
  onMouseLeave?: React.MouseEventHandler<HTMLAnchorElement>;
}) {
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
