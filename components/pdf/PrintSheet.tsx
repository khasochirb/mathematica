"use client";

import { useEffect } from "react";
import MathText from "@/components/esh/MathText";
import GeoDiagram from "@/components/genmath/interactive/GeoDiagram";
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import LogoLockup from "@/components/layout/LogoLockup";
import { LangContext } from "@/lib/lang-context";
import type { Sheet, SheetItem } from "@/lib/pdf/sheet";

// The worksheet itself: plain black on white, sized for A4, laid out by
// print CSS (see the <style> in app/math/print/page.tsx). Used two ways:
//   - headless Chromium on the server opens it, waits for window.__READY__
//     and prints it to PDF (POST /api/pdf);
//   - the fallback: the student's own browser opens it and we call
//     window.print() once it is ready (autoPrint).

declare global {
  interface Window {
    __READY__?: boolean;
  }
}

const T = {
  mn: {
    eyebrow: "Дасгалын хуудас",
    name: "Нэр",
    date: "Огноо",
    key: "Хариу",
    solutions: "Алхам алхмаар бодолт, сануулга, алдааны тайлбарыг сайтаас үзээрэй:",
    solutionsSit: "Энэ тестийг сайт дээр бөглөөд, бодлого бүрийн бодолтыг алхам алхмаар үзээрэй:",
    promoH: "Багштай танхимд суралцвал илүү хурдан ахина.",
    promo: "Mongol Potential Academy · Улаанбаатар, Хан-Уул, Мандала Гарден · 8862 7927",
  },
  en: {
    eyebrow: "Worksheet",
    name: "Name",
    date: "Date",
    key: "Answer key",
    solutions: "Step-by-step solutions, hints and mistake explanations are on the site:",
    solutionsSit: "Sit this paper on the site to see a step-by-step solution for every question:",
    promoH: "Learning with a teacher in the room is faster.",
    promo: "Mongol Potential Academy · Ulaanbaatar, Khan-Uul, Mandala Garden · 8862 7927",
  },
} as const;

function plainLen(s: string): number {
  return s.replace(/\$[^$]*\$/g, (m) => "x".repeat(Math.ceil(m.length / 2))).length;
}

function optionColumns(item: SheetItem): number {
  const longest = Math.max(...(item.options ?? []).map((o) => plainLen(o.text)));
  const n = item.options?.length ?? 0;
  if (longest <= 14 && n <= 5) return n;
  if (longest <= 34) return 2;
  return 1;
}

function Item({ item }: { item: SheetItem }) {
  return (
    <>
      {item.heading && <h2 className="pp-part">{item.heading}</h2>}
      <section className="pp-item">
        {item.context && (
          <p className="pp-context">
            <MathText text={item.context} />
          </p>
        )}
        <div className="pp-row">
          <span className="pp-n">{item.n}.</span>
          <div className="pp-body">
            <p className="pp-statement">
              <MathText text={item.statement} />
            </p>
            {item.image && (
              // eslint-disable-next-line @next/next/no-img-element
              <img
                className="pp-img"
                src={item.image.src}
                alt={item.image.alt}
                width={item.image.width}
                height={item.image.height}
              />
            )}
            {item.geoFigure && (
              <div className="pp-fig">
                <GeoDiagram spec={item.geoFigure} />
              </div>
            )}
            {item.figure && (
              <div className="pp-fig">
                <RatioFigure figure={item.figure} />
              </div>
            )}
            {item.options && (
              <ol className="pp-options" style={{ gridTemplateColumns: `repeat(${optionColumns(item)}, minmax(0, 1fr))` }}>
                {item.options.map((o) => (
                  <li key={o.label}>
                    <b>{o.label})</b> <MathText text={o.text} />
                  </li>
                ))}
              </ol>
            )}
            <div className="pp-space" />
          </div>
        </div>
      </section>
    </>
  );
}

export default function PrintSheet({
  sheet,
  answers,
  space,
  nameLine,
  solutionsUrl,
  qrSvg,
  autoPrint,
}: {
  sheet: Sheet;
  answers: boolean;
  space: boolean;
  nameLine: boolean;
  solutionsUrl: string;
  qrSvg: string;
  autoPrint: boolean;
}) {
  const t = T[sheet.lang];

  useEffect(() => {
    let cancelled = false;
    (async () => {
      try {
        await document.fonts.ready;
        await Promise.all(
          Array.from(document.images).map((img) =>
            img.complete ? Promise.resolve() : img.decode().catch(() => undefined),
          ),
        );
      } catch {
        // A missing image must not block the sheet; it prints without it.
      }
      await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
      if (cancelled) return;
      window.__READY__ = true;
      document.documentElement.dataset.printReady = "1";
      if (autoPrint) window.print();
    })();
    return () => {
      cancelled = true;
    };
  }, [autoPrint]);

  return (
    <LangContext.Provider value={{ lang: sheet.lang, setLang: () => {} }}>
      <div className={`mp-print${space ? " pp-with-space" : ""}`}>
        <header className="pp-head">
          <LogoLockup className="pp-logo" markColor="#0a74da" textColor="#111111" />
          <div className="pp-eyebrow">{t.eyebrow}</div>
          <h1 className="pp-title">{sheet.title}</h1>
          <div className="pp-sub">{sheet.subtitle}</div>
          {nameLine && (
            <div className="pp-name">
              <span>{t.name}:</span>
              <span className="pp-line pp-line-long" />
              <span>{t.date}:</span>
              <span className="pp-line" />
            </div>
          )}
        </header>

        <main className="pp-items">
          {sheet.items.map((item, i) => (
            <Item key={`${item.n}-${i}`} item={item} />
          ))}
        </main>

        {answers && (
          <section className="pp-key">
            <h2 className="pp-key-h">{t.key}</h2>
            <ol className="pp-key-list">
              {sheet.items.map((item, i) => (
                <li key={`${item.n}-${i}`}>
                  <b>{item.n}.</b> <MathText text={item.answer} />
                </li>
              ))}
            </ol>
            <div className="pp-solutions">
              <div className="pp-qr" dangerouslySetInnerHTML={{ __html: qrSvg }} />
              <div>
                <p>{sheet.solutionsMode === "sit" ? t.solutionsSit : t.solutions}</p>
                <p className="pp-url">{solutionsUrl.replace(/^https?:\/\//, "")}</p>
              </div>
            </div>
          </section>
        )}

        <aside className="pp-promo">
          <b>{t.promoH}</b> {t.promo} · mongolpotential.com/academy
        </aside>
      </div>
    </LangContext.Provider>
  );
}
