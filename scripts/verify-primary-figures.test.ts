// The primary band's chart figures, rendered for real. The 2026-08-13 audit
// found the band's data lessons DESCRIBING charts in prose because no chart
// figure existed; these tests render the new FigureSpec modes through the
// actual components (server render, no browser needed) and assert the
// picture says what the data says — a bar per category with its value
// labelled, a symbol row that multiplies back to its value. If a renderer
// regresses, this fails before a child meets it.
import { describe, it, expect } from "vitest";
import { createElement as h } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import BarChartView from "@/components/genmath/interactive/BarChartView";
import PictographView from "@/components/genmath/interactive/PictographView";
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import type { FigureSpec } from "@/lib/genmath-interactive";

describe("barChart figure", () => {
  const spec: NonNullable<FigureSpec["barChart"]> = {
    categories: [
      { label: "wrestling", value: 20 },
      { label: "archery", value: 15 },
    ],
    step: 5,
  };

  it("draws one bar per category with its value labelled", () => {
    const html = renderToStaticMarkup(h(BarChartView, { spec }));
    expect(html).toContain("aria-label");
    expect((html.match(/<rect/g) ?? []).length).toBe(2);
    for (const s of ["wrestling", "archery", ">20<", ">15<"]) {
      expect(html).toContain(s);
    }
    for (const tick of [">0<", ">5<", ">10<"]) expect(html).toContain(tick);
  });

  it("reaches the renderer through the FigureSpec dispatcher", () => {
    const html = renderToStaticMarkup(h(RatioFigure, { figure: { mode: "barChart", barChart: spec } }));
    expect(html).toContain("Bar chart");
  });
});

describe("pictograph figure", () => {
  it("draws value ÷ key symbols per row, plus the key line", () => {
    const spec = { rows: [{ label: "Monday", value: 30 }, { label: "Tuesday", value: 20 }], key: 5 };
    const html = renderToStaticMarkup(h(PictographView, { spec }));
    // 30/5 = 6 and 20/5 = 4 symbols → 10 in rows, plus 1 in the key legend
    // and 1 inside the table's aria-label ("one ● means 5")
    expect((html.match(/●/g) ?? []).length).toBe(12);
    expect(html).toContain("= 5");
  });

  it("renders a half symbol when the value is half a key over", () => {
    const spec = { rows: [{ label: "Sheep", value: 45 }], key: 10 };
    const html = renderToStaticMarkup(h(PictographView, { spec }));
    // 4 full + 1 clipped half + 1 key legend + 1 in the aria-label = 7
    expect((html.match(/●/g) ?? []).length).toBe(7);
    expect(html).toContain("overflow:hidden");
  });

  it("reaches the renderer through the FigureSpec dispatcher", () => {
    const html = renderToStaticMarkup(
      h(RatioFigure, { figure: { mode: "pictograph", pictograph: { rows: [{ label: "x", value: 4 }], key: 2 } } }),
    );
    expect(html).toContain("Pictograph");
  });
});

describe("the shipped grade-3 data unit uses the real figures", () => {
  it("pictograph and bar-chart lessons carry their own chart modes", async () => {
    const unit = (await import("@/data/genmath/3/data-and-pictographs.json")).default;
    const raw = JSON.stringify(unit);
    expect(raw.includes('"pictograph"')).toBe(true);
    expect(raw.includes('"barChart"')).toBe(true);
  });
});
