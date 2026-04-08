"use client";
import Link from "next/link";
import { Lock, Zap, BarChart3, Target } from "lucide-react";

export default function UpgradePage() {
  return (
    <div className="min-h-screen bg-surface-900 pt-20 flex items-center justify-center px-4">
      <div className="max-w-md w-full text-center">
        <div className="w-16 h-16 bg-accent-gold/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
          <Lock className="h-8 w-8 text-accent-gold" />
        </div>
        <h1 className="font-display text-2xl font-bold text-white mb-3">
          Өдрийн хязгаарт хүрлээ
        </h1>
        <p className="text-gray-400 mb-8">
          Үнэгүй хэрэглэгч өдөрт 10 бодлого бодох боломжтой. Хязгааргүй
          дасгал хийж, дэлгэрэнгүй шинжилгээ авахын тулд элс.
        </p>

        <div className="card-glass mb-6 text-left space-y-3">
          {[
            { icon: Zap, text: "Хязгааргүй бодлого өдөр бүр" },
            { icon: BarChart3, text: "Сул талуудын дэлгэрэнгүй шинжилгээ" },
            {
              icon: Target,
              text: "Таны хамгийн хэцүү сэдвээр давтан дасгал",
            },
          ].map(({ icon: Icon, text }) => (
            <div key={text} className="flex items-center gap-3">
              <Icon className="h-4 w-4 text-accent-gold flex-shrink-0" />
              <span className="text-gray-300 text-sm">{text}</span>
            </div>
          ))}
        </div>

        <div className="card-glass mb-6">
          <p className="text-gray-400 text-sm mb-1">Сарын төлбөр</p>
          <p className="font-display text-3xl font-bold text-white">
            19,900 ₮
          </p>
          <p className="text-gray-500 text-xs mt-1">/ сар</p>
        </div>

        <a
          href="https://wa.me/14153367764?text=Mongolpotential subscription-д элсэхийг хүсч байна"
          target="_blank"
          rel="noopener noreferrer"
          className="btn-primary w-full py-3 text-center block mb-3"
        >
          Одоо элсэх
        </a>
        <Link
          href="/practice"
          className="text-sm text-gray-500 hover:text-gray-300"
        >
          ← Буцах
        </Link>
      </div>
    </div>
  );
}
