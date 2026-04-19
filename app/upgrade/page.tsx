"use client";
import Link from "next/link";
import { Lock, Zap, BarChart3, Target } from "lucide-react";

export default function UpgradePage() {
  return (
    <div
      className="min-h-screen pt-24 pb-16 flex items-center justify-center px-4"
      style={{ background: "var(--bg)" }}
    >
      <div className="max-w-md w-full">
        <div
          className="w-14 h-14 rounded-md flex items-center justify-center mx-auto mb-6"
          style={{
            background: "rgba(245, 158, 11, 0.10)",
            border: "1px solid rgba(245, 158, 11, 0.32)",
            color: "var(--warn)",
          }}
        >
          <Lock className="h-6 w-6" />
        </div>

        <div className="eyebrow mb-2 text-center">Lock · daily limit</div>
        <h1
          className="serif text-center"
          style={{
            fontWeight: 400,
            fontSize: 36,
            letterSpacing: "-0.03em",
            lineHeight: 1.05,
            color: "var(--fg)",
          }}
        >
          Өдрийн <em className="serif-italic" style={{ color: "var(--accent)" }}>хязгаарт</em> хүрлээ
        </h1>
        <p className="mt-4 text-center text-[14px] leading-relaxed" style={{ color: "var(--fg-2)" }}>
          Үнэгүй хэрэглэгч өдөрт 10 бодлого бодох боломжтой. Хязгааргүй
          дасгал хийж, дэлгэрэнгүй шинжилгээ авахын тулд элс.
        </p>

        <div className="card-edit p-5 mt-8 space-y-3">
          {[
            { icon: Zap, text: "Хязгааргүй бодлого өдөр бүр" },
            { icon: BarChart3, text: "Сул талуудын дэлгэрэнгүй шинжилгээ" },
            { icon: Target, text: "Таны хамгийн хэцүү сэдвээр давтан дасгал" },
          ].map(({ icon: Icon, text }) => (
            <div key={text} className="flex items-center gap-3">
              <Icon className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
              <span className="text-[13px]" style={{ color: "var(--fg-1)" }}>{text}</span>
            </div>
          ))}
        </div>

        <div
          className="card-edit p-5 mt-3 flex items-end justify-between"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div>
            <div className="eyebrow">Сарын төлбөр</div>
            <div
              className="serif tabular mt-1"
              style={{ fontSize: 36, letterSpacing: "-0.02em", color: "var(--fg)" }}
            >
              19,900<span className="mono text-[14px] ml-1" style={{ color: "var(--fg-3)" }}>₮</span>
            </div>
          </div>
          <span className="mono text-[11px]" style={{ color: "var(--fg-3)" }}>/ САР</span>
        </div>

        <a
          href="https://wa.me/14153367764?text=Mongolpotential subscription-д элсэхийг хүсч байна"
          target="_blank"
          rel="noopener noreferrer"
          className="btn btn-primary w-full mt-6"
        >
          Одоо элсэх
        </a>
        <Link
          href="/practice"
          className="block text-center text-[12px] mt-4 mono"
          style={{ color: "var(--fg-3)" }}
        >
          ← БУЦАХ
        </Link>
      </div>
    </div>
  );
}
