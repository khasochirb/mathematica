import { describe, expect, it } from "vitest";
import { getBankTopic } from "@/lib/bank-data";
import { BANK_MN } from "@/lib/bank-data-mn";
import { localizeTopic } from "@/lib/problem-bank";

// Every Mongolian bank mirror must localize EVERY variant of its subject: the
// mirror is generated from per-unit tables that ship whole, so a variant left
// in English after localizeTopic means the merge lost it (it did once, when a
// form id repeated across two units of integrated-1).
describe("Mongolian bank mirrors localize completely", () => {
  for (const slug of Object.keys(BANK_MN)) {
    it(slug, () => {
      const en = getBankTopic(slug);
      expect(en).not.toBeNull();
      const mn = BANK_MN[slug];
      const out = localizeTopic(en!, mn);
      const mnByKey = new Map(mn.forms.map((f) => [`${f.unit}/${f.id}`, f]));
      let missed = 0;
      out.forms.forEach((f, i) => {
        const src = mnByKey.get(`${f.unit}/${f.id}`);
        expect(src, `${slug}: no Mongolian form ${f.unit}/${f.id}`).toBeDefined();
        expect(f.title).toBe(src!.title);
        const mv = new Map(src!.variants.map((v) => [v.id, v]));
        f.variants.forEach((v, j) => {
          const want = mv.get(v.id);
          if (!want || v.statement !== want.statement) missed++;
          // The key never moves: scoring reads correctIndex from the English.
          expect(v.correctIndex).toBe(en!.forms[i].variants[j].correctIndex);
        });
      });
      expect(missed).toBe(0);
    });
  }
});
