"use client";

import { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { ArrowLeft, ArrowRight, Check, Sparkles, Lightbulb } from "lucide-react";
import MathText from "@/components/esh/MathText";
import TutorPanel from "@/components/tutor/TutorPanel";
import WorkedExampleCard from "@/components/lesson/WorkedExampleCard";
import RevealProblemCard from "@/components/lesson/RevealProblemCard";
import StepProgress from "@/components/genmath/interactive/StepProgress";
import QuantityScaler from "@/components/genmath/interactive/QuantityScaler";
import OrderFlip from "@/components/genmath/interactive/OrderFlip";
import CompareToggle from "@/components/genmath/interactive/CompareToggle";
import TapQuestion from "@/components/genmath/interactive/TapQuestion";
import RatioTable from "@/components/genmath/interactive/RatioTable";
import RatioCompare from "@/components/genmath/interactive/RatioCompare";
import RateMeter from "@/components/genmath/interactive/RateMeter";
import DealCompare from "@/components/genmath/interactive/DealCompare";
import ProportionBuilder from "@/components/genmath/interactive/ProportionBuilder";
import FractionScaler from "@/components/genmath/interactive/FractionScaler";
import FractionSimplify from "@/components/genmath/interactive/FractionSimplify";
import FractionCompare from "@/components/genmath/interactive/FractionCompare";
import FractionCombine from "@/components/genmath/interactive/FractionCombine";
import AreaModel from "@/components/genmath/interactive/AreaModel";
import FractionDivide from "@/components/genmath/interactive/FractionDivide";
import DecimalGrid from "@/components/genmath/interactive/DecimalGrid";
import DecimalCompare from "@/components/genmath/interactive/DecimalCompare";
import DecimalRounder from "@/components/genmath/interactive/DecimalRounder";
import DecimalColumnSum from "@/components/genmath/interactive/DecimalColumnSum";
import DecimalAreaModel from "@/components/genmath/interactive/DecimalAreaModel";
import DecimalShiftDivide from "@/components/genmath/interactive/DecimalShiftDivide";
import PercentGrid from "@/components/genmath/interactive/PercentGrid";
import PercentBar from "@/components/genmath/interactive/PercentBar";
import PercentChange from "@/components/genmath/interactive/PercentChange";
import PercentChangeFinder from "@/components/genmath/interactive/PercentChangeFinder";
import IntegerLine from "@/components/genmath/interactive/IntegerLine";
import IntegerCompare from "@/components/genmath/interactive/IntegerCompare";
import AbsoluteValue from "@/components/genmath/interactive/AbsoluteValue";
import IntegerAdd from "@/components/genmath/interactive/IntegerAdd";
import IntegerSubtract from "@/components/genmath/interactive/IntegerSubtract";
import IntegerSignRule from "@/components/genmath/interactive/IntegerSignRule";
import FactorPairs from "@/components/genmath/interactive/FactorPairs";
import FactorFinder from "@/components/genmath/interactive/FactorFinder";
import MultiplesGrid from "@/components/genmath/interactive/MultiplesGrid";
import PrimeExplorer from "@/components/genmath/interactive/PrimeExplorer";
import GcfFinder from "@/components/genmath/interactive/GcfFinder";
import LcmFinder from "@/components/genmath/interactive/LcmFinder";
import FactorTree from "@/components/genmath/interactive/FactorTree";
import ExponentBuilder from "@/components/genmath/interactive/ExponentBuilder";
import OrderOfOps from "@/components/genmath/interactive/OrderOfOps";
import AlgebraTiles from "@/components/genmath/interactive/AlgebraTiles";
import Evaluator from "@/components/genmath/interactive/Evaluator";
import BalanceScale from "@/components/genmath/interactive/BalanceScale";
import CoordinateGrid from "@/components/genmath/interactive/CoordinateGrid";
import GeoCanvas from "@/components/genmath/interactive/GeoCanvas";
import SegmentRuler from "@/components/genmath/interactive/SegmentRuler";
import Protractor from "@/components/genmath/interactive/Protractor";
import AnglePairFinder from "@/components/genmath/interactive/AnglePairFinder";
import StepProof from "@/components/genmath/interactive/StepProof";
import PatternGrow from "@/components/genmath/interactive/PatternGrow";
import ConjectureTest from "@/components/genmath/interactive/ConjectureTest";
import ConditionalFlip from "@/components/genmath/interactive/ConditionalFlip";
import Transversal from "@/components/genmath/interactive/Transversal";
import TriangleAngles from "@/components/genmath/interactive/TriangleAngles";
import TriangleInequality from "@/components/genmath/interactive/TriangleInequality";
import CongruentTriangles from "@/components/genmath/interactive/CongruentTriangles";
import TriangleCenters from "@/components/genmath/interactive/TriangleCenters";
import Midsegment from "@/components/genmath/interactive/Midsegment";
import PolygonAngles from "@/components/genmath/interactive/PolygonAngles";
import QuadShape from "@/components/genmath/interactive/QuadShape";
import SimilarFigures from "@/components/genmath/interactive/SimilarFigures";
import SideSplitter from "@/components/genmath/interactive/SideSplitter";
import Dilation from "@/components/genmath/interactive/Dilation";
import PythagoreanSquares from "@/components/genmath/interactive/PythagoreanSquares";
import SpecialTriangle from "@/components/genmath/interactive/SpecialTriangle";
import TrigRatios from "@/components/genmath/interactive/TrigRatios";
import CircleFigure from "@/components/genmath/interactive/CircleFigure";
import CircleAngle from "@/components/genmath/interactive/CircleAngle";
import TangentCircle from "@/components/genmath/interactive/TangentCircle";
import ArcSector from "@/components/genmath/interactive/ArcSector";
import CircleUnroll from "@/components/genmath/interactive/CircleUnroll";
import SystemGraph from "@/components/genmath/interactive/SystemGraph";
import ScatterPlot from "@/components/genmath/interactive/ScatterPlot";
import ParabolaGraph from "@/components/genmath/interactive/ParabolaGraph";
import ExpGraph from "@/components/genmath/interactive/ExpGraph";
import PolyGraph from "@/components/genmath/interactive/PolyGraph";
import UnitCircle from "@/components/genmath/interactive/UnitCircle";
import LimitGraph from "@/components/genmath/interactive/LimitGraph";
import TangentGraph from "@/components/genmath/interactive/TangentGraph";
import AreaGraph from "@/components/genmath/interactive/AreaGraph";
import VectorGraph from "@/components/genmath/interactive/VectorGraph";
import ConicGraph from "@/components/genmath/interactive/ConicGraph";
import AreaShape from "@/components/genmath/interactive/AreaShape";
import ApothemPolygon from "@/components/genmath/interactive/ApothemPolygon";
import CompositeArea from "@/components/genmath/interactive/CompositeArea";
import Solid3D from "@/components/genmath/interactive/Solid3D";
import SolidNet from "@/components/genmath/interactive/SolidNet";
import TransformPlane from "@/components/genmath/interactive/TransformPlane";
import CoordGeo from "@/components/genmath/interactive/CoordGeo";
import TreeDiagram from "@/components/genmath/interactive/TreeDiagram";
import PascalTriangle from "@/components/genmath/interactive/PascalTriangle";
import PathGrid from "@/components/genmath/interactive/PathGrid";
import VennCounts from "@/components/genmath/interactive/VennCounts";
import LongRunFrequency from "@/components/genmath/interactive/LongRunFrequency";
import DistributionBars from "@/components/genmath/interactive/DistributionBars";
import BinomialBars from "@/components/genmath/interactive/BinomialBars";
import DotPlot from "@/components/genmath/interactive/DotPlot";
import HistogramBins from "@/components/genmath/interactive/HistogramBins";
import BoxPlot from "@/components/genmath/interactive/BoxPlot";
import NormalCurve from "@/components/genmath/interactive/NormalCurve";
import SamplingWobble from "@/components/genmath/interactive/SamplingWobble";
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import NotationToggle from "@/components/genmath/interactive/NotationToggle";
import { type GenMathLesson } from "@/lib/genmath-lessons";
import { useLang } from "@/lib/lang-context";
import usePerformance from "@/lib/use-performance";
import { contextFromPathname, lessonSlugsFromPathname } from "@/lib/perf-context";
import { type InteractiveStep, type WorkedItem, getLessonProblem } from "@/lib/genmath-interactive";

// Player chrome in both site languages; lesson CONTENT arrives already
// localized from the registry (data/genmath/8-mn mirrors).
const CHROME = {
  en: { reveal: "Show solution", hide: "Hide", answer: "Answer:", back: "Back", cont: "Continue", finish: "Finish lesson" },
  mn: { reveal: "Бодолтыг харах", hide: "Нуух", answer: "Хариу:", back: "Буцах", cont: "Үргэлжлүүлэх", finish: "Хичээлийг дуусгах" },
};

function StepHeader({ eyebrow, title }: { eyebrow?: string; title: string }) {
  return (
    <div className="mb-4">
      {eyebrow && (
        <div className="eyebrow mb-1.5" style={{ color: "var(--accent)" }}>
          {eyebrow}
        </div>
      )}
      <h2
        className="serif"
        style={{ fontWeight: 400, fontSize: "clamp(24px, 5vw, 34px)", lineHeight: 1.08, letterSpacing: "-0.03em", color: "var(--fg)" }}
      >
        {title}
      </h2>
    </div>
  );
}

function AnswerPill({ answer }: { answer: string }) {
  const { lang } = useLang();
  return (
    <span className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5" style={{ background: "var(--accent-wash)", color: "var(--accent)" }}>
      <span className="text-[12px]">{CHROME[lang].answer}</span>
      <span className="q-math text-[14px]">
        <MathText text={answer} />
      </span>
    </span>
  );
}

function WorkedItemCard({ item, index }: { item: WorkedItem; index: number }) {
  return (
    <div className="card-edit p-5">
      <div className="mb-2 flex items-center gap-2">
        <span className="grid h-6 w-6 place-items-center rounded-full text-[11px]" style={{ background: "var(--accent-wash)", color: "var(--accent)" }}>
          {index + 1}
        </span>
        <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}>
          <MathText text={item.prompt} />
        </div>
      </div>
      {item.figure && (
        <div className="my-3 flex justify-center">
          <RatioFigure figure={item.figure} />
        </div>
      )}
      <ol className="mt-2 space-y-1.5">
        {item.steps.map((s, i) => (
          <li key={i} className="flex gap-2.5">
            <span className="mono mt-0.5 text-[11px]" style={{ color: "var(--fg-3)" }}>{i + 1}</span>
            <span className="q-math text-[14px]" style={{ color: "var(--fg-1)" }}>
              <MathText text={s} />
            </span>
          </li>
        ))}
      </ol>
      <div className="mt-3">
        <AnswerPill answer={item.answer} />
      </div>
    </div>
  );
}

type TapAnswerHandler = (subId: string, correct: boolean, selected: string, correctOption: string) => void;

function StepBody({
  lesson,
  step,
  onTapAnswer,
}: {
  lesson: GenMathLesson;
  step: InteractiveStep;
  onTapAnswer?: TapAnswerHandler;
}) {
  const { lang } = useLang();
  const REVEAL = lang === "mn"
    ? { reveal: "Бодолтыг харах", hide: "Нуух", revealAria: "Бодолтыг харах", hideAria: "Бодолтыг нуух" }
    : { reveal: "Show solution", hide: "Hide", revealAria: "Show solution", hideAria: "Hide solution" };
  switch (step.kind) {
    case "concept":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
            <MathText text={step.body} />
          </p>
        </>
      );
    case "teach":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {/* Visual first — the figure leads, then the explanation. */}
          {step.figure && (
            <div className="mb-5 flex justify-center">
              <RatioFigure figure={step.figure} />
            </div>
          )}
          {step.beats && step.beats.length > 0 ? (
            <ul className="space-y-3">
              {step.beats.map((b, i) => (
                <li key={i} className="gm-step flex items-start gap-3" style={{ animationDelay: `${i * 70}ms` }}>
                  <span
                    className="mt-0.5 grid h-6 w-6 flex-shrink-0 place-items-center rounded-full text-[12px] font-medium"
                    style={{ background: "var(--accent-wash)", color: "var(--accent)" }}
                  >
                    {i + 1}
                  </span>
                  <span className="font-sans" style={{ fontSize: 16, lineHeight: 1.5, color: "var(--fg-1)" }}>
                    <MathText text={b} />
                  </span>
                </li>
              ))}
            </ul>
          ) : step.body ? (
            <p className="font-sans" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
              <MathText text={step.body} />
            </p>
          ) : null}
        </>
      );
    case "notationToggle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <NotationToggle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "workedSet":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {step.intro && (
            <p className="font-sans mb-3" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
              <MathText text={step.intro} />
            </p>
          )}
          <div className="space-y-3">
            {step.examples.map((ex, i) => (
              <WorkedItemCard key={i} item={ex} index={i} />
            ))}
          </div>
        </>
      );
    case "tryItSet":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {step.intro && (
            <p className="font-sans mb-3" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
              <MathText text={step.intro} />
            </p>
          )}
          {step.grid && (
            <div className="mb-3">
              <CoordinateGrid config={step.grid} />
            </div>
          )}
          <div className="space-y-3">
            {step.problems.map((p, i) => (
              <TapQuestion
                key={i}
                prompt={p.prompt}
                options={p.options}
                correctIndex={p.correctIndex}
                explanation={p.explanation}
                figure={p.figure}
                grid={p.grid}
                onAnswer={(correct, selected, correctOption) =>
                  onTapAnswer?.(`t${i}`, correct, selected, correctOption)
                }
              />
            ))}
          </div>
        </>
      );
    case "scaler":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <QuantityScaler config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "orderFlip":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <OrderFlip config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "compareToggle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CompareToggle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "ratioTable":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <RatioTable config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "ratioCompare":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <RatioCompare config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "rateMeter":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <RateMeter config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "dealCompare":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DealCompare config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "proportionBuilder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ProportionBuilder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "fractionScaler":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FractionScaler config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "fractionSimplify":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FractionSimplify config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "fractionCompare":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FractionCompare config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "fractionCombine":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FractionCombine config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "areaModel":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AreaModel config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "fractionDivide":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FractionDivide config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalGrid":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalGrid config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalCompare":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalCompare config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalRounder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalRounder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalColumnSum":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalColumnSum config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalArea":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalAreaModel config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "decimalShiftDivide":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DecimalShiftDivide config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "percentGrid":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PercentGrid config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "percentBar":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PercentBar config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "percentChange":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PercentChange config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "percentChangeFinder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PercentChangeFinder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "integerLine":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <IntegerLine config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "integerCompare":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <IntegerCompare config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "absoluteValue":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AbsoluteValue config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "integerAdd":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <IntegerAdd config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "integerSubtract":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <IntegerSubtract config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "integerSignRule":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <IntegerSignRule config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "factorPairs":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FactorPairs config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "factorFinder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FactorFinder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "multiplesGrid":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <MultiplesGrid config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "primeExplorer":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PrimeExplorer config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "gcfFinder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <GcfFinder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "lcmFinder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <LcmFinder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "factorTree":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <FactorTree config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "exponentBuilder":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ExponentBuilder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "orderOfOps":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <OrderOfOps config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "algebraTiles":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AlgebraTiles config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "evaluator":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Evaluator config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "balanceScale":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <BalanceScale config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "coordinateGrid":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CoordinateGrid config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "geoCanvas":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <GeoCanvas config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "segmentRuler":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SegmentRuler config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "protractor":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Protractor config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "anglePairs":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AnglePairFinder config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "stepProof":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <StepProof config={step.config} />
          {step.teach && (
            <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
              <MathText text={step.teach} />
            </p>
          )}
        </>
      );
    case "patternGrow":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PatternGrow config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "conjectureTest":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ConjectureTest config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "conditionalFlip":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ConditionalFlip config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "transversal":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Transversal config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "triangleAngles":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TriangleAngles config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "triangleInequality":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TriangleInequality config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "congruentTriangles":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CongruentTriangles config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "triangleCenters":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TriangleCenters config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "midsegment":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Midsegment config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "polygonAngles":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PolygonAngles config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "quadShape":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <QuadShape config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "similarFigures":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SimilarFigures config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "sideSplitter":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SideSplitter config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "dilation":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Dilation config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "pythagoreanSquares":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PythagoreanSquares config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "specialTriangle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SpecialTriangle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "trigRatios":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TrigRatios config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "circleFigure":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CircleFigure config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "circleAngle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CircleAngle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "tangentCircle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TangentCircle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "scatterPlot":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ScatterPlot config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "treeDiagram":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TreeDiagram config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "pascalTriangle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PascalTriangle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "pathGrid":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PathGrid config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "vennCounts":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <VennCounts config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "longRunFrequency":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <LongRunFrequency config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "distributionBars":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DistributionBars config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "binomialBars":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <BinomialBars config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "dotPlot":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <DotPlot config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "histogramBins":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <HistogramBins config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "boxPlot":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <BoxPlot config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "normalCurve":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <NormalCurve config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "samplingWobble":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SamplingWobble config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "unitCircle":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <UnitCircle config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "limitGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <LimitGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "tangentGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TangentGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "areaGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AreaGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "vectorGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <VectorGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "conicGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ConicGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "polyGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <PolyGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "expGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ExpGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "parabolaGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ParabolaGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "systemGraph":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SystemGraph config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "circleUnroll":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CircleUnroll config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "arcSector":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ArcSector config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "areaShape":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <AreaShape config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "apothemPolygon":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ApothemPolygon config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "compositeArea":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CompositeArea config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "solid3d":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <Solid3D config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "solidNet":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <SolidNet config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "transformPlane":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TransformPlane config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "coordGeo":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <CoordGeo config={step.config} />
          <p className="font-sans mt-4" style={{ fontSize: 15, lineHeight: 1.55, color: "var(--fg-2)" }}>
            <MathText text={step.teach} />
          </p>
        </>
      );
    case "tapQuestion":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TapQuestion
            prompt={step.prompt}
            options={step.options}
            correctIndex={step.correctIndex}
            explanation={step.explanation}
            grid={step.grid}
            onAnswer={(correct, selected, correctOption) =>
              onTapAnswer?.("q", correct, selected, correctOption)
            }
          />
        </>
      );
    case "worked": {
      const p = getLessonProblem(lesson, step.problemId);
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {p ? <WorkedExampleCard problem={p} index={0} /> : null}
        </>
      );
    }
    case "tryIt": {
      const p = getLessonProblem(lesson, step.problemId);
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          {p ? (
            <RevealProblemCard
              problem={p}
              index={0}
              labels={REVEAL}
              onSelfGrade={(correct) =>
                onTapAnswer?.("r", correct, correct ? "self:correct" : "self:incorrect", "self")
              }
            />
          ) : null}
        </>
      );
    }
    case "funFact":
      return (
        <div className="rounded-2xl p-5 sm:p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
          <div className="mb-3 flex items-center gap-2">
            <span className="grid h-9 w-9 place-items-center rounded-full" style={{ background: "rgba(239,159,39,0.16)", color: "#b97316" }}>
              <Sparkles className="h-5 w-5" />
            </span>
            <div className="eyebrow" style={{ color: "#b97316" }}>{step.eyebrow ?? "Fun fact"}</div>
          </div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(20px, 4vw, 28px)", lineHeight: 1.12, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            {step.title}
          </h2>
          <p className="font-sans mt-2" style={{ fontSize: 16, lineHeight: 1.6, color: "var(--fg-1)" }}>
            <MathText text={step.body} />
          </p>
        </div>
      );
    case "tip":
      return (
        <div className="rounded-2xl p-5 sm:p-6" style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}>
          <div className="mb-3 flex items-center gap-2">
            <span className="grid h-9 w-9 place-items-center rounded-full" style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}>
              <Lightbulb className="h-5 w-5" />
            </span>
            <div className="eyebrow" style={{ color: "var(--accent)" }}>{step.eyebrow ?? "Tip"}</div>
          </div>
          <h2 className="serif" style={{ fontWeight: 400, fontSize: "clamp(20px, 4vw, 28px)", lineHeight: 1.12, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            {step.title}
          </h2>
          <p className="font-sans mt-2" style={{ fontSize: 16, lineHeight: 1.6, color: "var(--fg-1)" }}>
            <MathText text={step.body} />
          </p>
        </div>
      );
    case "recap":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <ul className="space-y-2.5">
            {step.points.map((pt, i) => (
              <li key={i} className="flex items-start gap-2.5">
                <span
                  className="mt-0.5 grid h-5 w-5 flex-shrink-0 place-items-center rounded-full"
                  style={{ background: "var(--accent-wash)", color: "var(--accent)" }}
                >
                  <Check className="h-3 w-3" />
                </span>
                <span className="font-sans" style={{ fontSize: 16, lineHeight: 1.5, color: "var(--fg-1)" }}>
                  <MathText text={pt} />
                </span>
              </li>
            ))}
          </ul>
        </>
      );
  }
}

export default function LessonPlayer({
  lesson,
  topicSlug,
  topicTitle,
  baseHref,
  crumb,
}: {
  lesson: GenMathLesson;
  topicSlug: string;
  topicTitle: string;
  // Where "exit" and "finish" land (defaults to the grade-6 topic page), and
  // the breadcrumb label — lets other courses (Geometry) reuse the player.
  baseHref?: string;
  crumb?: string;
}) {
  const steps = lesson.interactive?.steps ?? [];
  const [i, setI] = useState(0);
  const total = steps.length;
  const isLast = i >= total - 1;
  const topicHref = baseHref ?? `/math/6/${topicSlug}`;
  const { lang } = useLang();
  const C = CHROME[lang];
  const pathname = usePathname();
  const perf = usePerformance();
  // Most recent wrong in-lesson answer — grounds the AI tutor's
  // "explain my mistake" flow. Cleared when the student moves on.
  const [lastMiss, setLastMiss] = useState<{ selected: string; correct: string } | null>(null);

  // Every first-attempt tapQuestion answer becomes a performance event in
  // this course's context ("course:prob-stats", "course:grade-6", ...),
  // with the unit slug as topic and lesson slug as subtopic — the raw
  // material for the per-course dashboard sections. Off the course tree
  // (context null) nothing is recorded.
  const handleTapAnswer = useCallback(
    (stepIndex: number): TapAnswerHandler =>
      (subId, correct, selected, correctOption) => {
        // Feed the AI tutor's "why was my answer wrong?" context, on or off
        // the course tree (the attempt recording below is course-tree-only).
        if (!correct) setLastMiss({ selected, correct: correctOption });
        const context = contextFromPathname(pathname ?? "");
        if (!context) return;
        const slugs = lessonSlugsFromPathname(pathname ?? "");
        perf.recordAttempt({
          questionSource: `lesson:${slugs?.unit ?? topicSlug}/${slugs?.lesson ?? lesson.slug}#s${stepIndex}${subId}`,
          topic: slugs?.unit ?? topicSlug,
          subtopic: slugs?.lesson ?? lesson.slug,
          selectedAnswer: selected,
          correctAnswer: correctOption,
          isCorrect: correct,
          source: "lesson",
          context,
        });
      },
    [pathname, perf, topicSlug, lesson.slug],
  );

  // On every step change, bring the page back to the top so the learner starts
  // the next step at its heading instead of wherever they'd scrolled to answer.
  useEffect(() => {
    if (typeof window !== "undefined") {
      window.scrollTo({ top: 0, behavior: "auto" });
    }
    setLastMiss(null);
  }, [i]);

  if (total === 0) return null;

  return (
    <div className="flex min-h-screen flex-col pt-20" style={{ background: "var(--bg)" }}>
      {/* Top bar: exit + lesson title + progress */}
      <div
        className="sticky top-16 z-10"
        style={{ background: "var(--bg)", borderBottom: "1px solid var(--line)" }}
      >
        <div className="mx-auto max-w-2xl px-4 py-3 sm:px-6">
          <div className="mb-2.5 flex items-center gap-3">
            <Link
              href={topicHref}
              aria-label="Exit lesson"
              className="gm-press grid h-8 w-8 place-items-center rounded-md"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
            >
              <ArrowLeft className="h-4 w-4" />
            </Link>
            <div className="min-w-0">
              <div className="eyebrow truncate">{crumb ?? `General Math · Grade 6 · ${topicTitle}`}</div>
              <div className="serif truncate" style={{ fontSize: 15, color: "var(--fg)" }}>
                {lesson.title}
              </div>
            </div>
            <span className="mono ml-auto text-[11px]" style={{ color: "var(--fg-3)" }}>
              {i + 1}/{total}
            </span>
          </div>
          <StepProgress total={total} current={i} onJump={(j) => setI(j)} />
        </div>
      </div>

      {/* Step content (re-keyed so it animates in on every step change) */}
      <main className="flex-1">
        <div key={i} className="gm-step mx-auto max-w-2xl px-4 py-8 sm:px-6">
          <StepBody lesson={lesson} step={steps[i]} onTapAnswer={handleTapAnswer(i)} />
        </div>
      </main>

      {/* AI tutor, grounded on the exact step the student sees (plus their
          latest wrong answer on this step, if any). */}
      <TutorPanel
        context={{
          kind: "lesson",
          course: crumb ?? topicTitle,
          unit: topicSlug,
          title: lesson.title,
          content: JSON.stringify(steps[i]).slice(0, 6000),
          selectedAnswer: lastMiss?.selected,
          correctAnswer: lastMiss?.correct,
        }}
      />

      {/* Bottom nav */}
      <div
        className="sticky bottom-0 z-10"
        style={{ background: "var(--bg)", borderTop: "1px solid var(--line)" }}
      >
        <div className="mx-auto flex max-w-2xl items-center gap-3 px-4 py-3 sm:px-6">
          <button
            type="button"
            onClick={() => setI((v) => Math.max(0, v - 1))}
            disabled={i === 0}
            className="gm-press inline-flex items-center gap-1.5 rounded-full px-4 py-3 text-[14px] disabled:opacity-35"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
          >
            <ArrowLeft className="h-4 w-4" /> {C.back}
          </button>
          {isLast ? (
            <Link
              href={topicHref}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              <Check className="h-4 w-4" /> {C.finish}
            </Link>
          ) : (
            <button
              type="button"
              onClick={() => setI((v) => Math.min(total - 1, v + 1))}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              {C.cont} <ArrowRight className="h-4 w-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
