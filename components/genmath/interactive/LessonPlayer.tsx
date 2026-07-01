"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowLeft, ArrowRight, Check, Sparkles, Lightbulb } from "lucide-react";
import MathText from "@/components/esh/MathText";
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
import RatioFigure from "@/components/genmath/interactive/RatioFigure";
import NotationToggle from "@/components/genmath/interactive/NotationToggle";
import { type GenMathLesson } from "@/lib/genmath-lessons";
import { type InteractiveStep, type WorkedItem, getLessonProblem } from "@/lib/genmath-interactive";

const REVEAL = { reveal: "Show solution", hide: "Hide", revealAria: "Show solution", hideAria: "Hide solution" };

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
  return (
    <span className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5" style={{ background: "var(--accent-wash)", color: "var(--accent)" }}>
      <span className="text-[12px]">Answer:</span>
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

function StepBody({ lesson, step }: { lesson: GenMathLesson; step: InteractiveStep }) {
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
          <div className="space-y-3">
            {step.problems.map((p, i) => (
              <TapQuestion
                key={i}
                prompt={p.prompt}
                options={p.options}
                correctIndex={p.correctIndex}
                explanation={p.explanation}
                figure={p.figure}
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
    case "tapQuestion":
      return (
        <>
          <StepHeader eyebrow={step.eyebrow} title={step.title} />
          <TapQuestion
            prompt={step.prompt}
            options={step.options}
            correctIndex={step.correctIndex}
            explanation={step.explanation}
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
          {p ? <RevealProblemCard problem={p} index={0} labels={REVEAL} /> : null}
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
}: {
  lesson: GenMathLesson;
  topicSlug: string;
  topicTitle: string;
}) {
  const steps = lesson.interactive?.steps ?? [];
  const [i, setI] = useState(0);
  const total = steps.length;
  const isLast = i >= total - 1;
  const topicHref = `/math/6/${topicSlug}`;

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
              <div className="eyebrow truncate">General Math · Grade 6 · {topicTitle}</div>
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
          <StepBody lesson={lesson} step={steps[i]} />
        </div>
      </main>

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
            <ArrowLeft className="h-4 w-4" /> Back
          </button>
          {isLast ? (
            <Link
              href={topicHref}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              <Check className="h-4 w-4" /> Finish lesson
            </Link>
          ) : (
            <button
              type="button"
              onClick={() => setI((v) => Math.min(total - 1, v + 1))}
              className="gm-press ml-auto inline-flex items-center gap-1.5 rounded-full px-6 py-3 text-[14px]"
              style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
            >
              Continue <ArrowRight className="h-4 w-4" />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
