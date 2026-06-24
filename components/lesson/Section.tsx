import type { ReactNode } from "react";

// Numbered lesson section wrapper. Shared across hubs.
export default function Section({
  n,
  label,
  children,
}: {
  n: string;
  label: string;
  children: ReactNode;
}) {
  return (
    <section className="mt-10 pt-10" style={{ borderTop: "1px solid var(--line)" }}>
      <div className="eyebrow mb-4">
        {n} · {label}
      </div>
      {children}
    </section>
  );
}
