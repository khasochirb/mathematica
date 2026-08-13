"use client";

// How much work a student has BUILT UP in the problem bank, across every bank
// surface — the /math course ladder, the SAT hub's bank and the IB hub's.
//
// This is a work counter, not a score. Every number it reports only ever goes
// up, because the underlying store is monotone (lib/problem-bank) and because
// counting attempts-you-got-wrong would turn practice into something with a
// downside. There is deliberately no accuracy figure here.
//
// Reads the ~55 KB manifest, never the ~9 MB corpus: the dashboard renders
// this on every visit (see lib/bank-manifest).

import { useEffect, useState } from "react";
import { useAuth } from "./auth-context";
import { bankManifest } from "./bank-manifest";
import { bankSolved, loadBankProgress } from "./problem-bank";

export type BankWork = {
  /** Problems answered correctly, all banks. */
  solvedProblems: number;
  /** Distinct problem TYPES solved at least once. */
  solvedForms: number;
  /** Problem types that exist across the banks the student has opened. */
  totalForms: number;
  /** Subjects with at least one solved problem. */
  subjects: number;
  /** The subject with the most solved problems, for a "most work here" line. */
  topSubject: { slug: string; title: string; solvedProblems: number } | null;
};

const EMPTY: BankWork = {
  solvedProblems: 0,
  solvedForms: 0,
  totalForms: 0,
  subjects: 0,
  topSubject: null,
};

export default function useBankWork(): { work: BankWork; ready: boolean } {
  const { user } = useAuth();
  const userId = user?.id ?? null;
  // localStorage loads after mount so the server and client renders match.
  const [work, setWork] = useState<BankWork>(EMPTY);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let solvedProblems = 0;
    let solvedForms = 0;
    let totalForms = 0;
    let subjects = 0;
    let topSubject: BankWork["topSubject"] = null;

    for (const topic of bankManifest()) {
      const progress = loadBankProgress(topic.slug, userId);
      const s = bankSolved(progress, topic.forms.map((f) => f.id));
      if (s.solvedProblems <= 0) continue;
      solvedProblems += s.solvedProblems;
      solvedForms += s.solvedForms;
      totalForms += topic.forms.length;
      subjects++;
      if (!topSubject || s.solvedProblems > topSubject.solvedProblems) {
        topSubject = { slug: topic.slug, title: topic.title, solvedProblems: s.solvedProblems };
      }
    }

    setWork({ solvedProblems, solvedForms, totalForms, subjects, topSubject });
    setReady(true);
  }, [userId]);

  return { work, ready };
}
