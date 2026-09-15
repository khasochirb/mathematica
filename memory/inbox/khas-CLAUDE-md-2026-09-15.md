# CLAUDE.md — mongolpotential.com

Create React App + TypeScript + Tailwind. User-facing copy lives in `src/pages/`,
`src/components/`; question banks live in `src/data/*.json`.

---

# Translating this site into Mongolian

The site is being rewritten in Mongolian for students preparing for **ЭЕШ, SAT, IB and
AP Calculus**. Two separate things go wrong, and there is a reference for each.

| Problem | Reference |
|---|---|
| Wrong **term** — the maths word itself | `docs/en-mn-math-glossary.md` + `.tsv` |
| Wrong **voice** — correct words, English sentences | `docs/mn-voice-reference.md` + `mn-voice-corpus.tsv` |

Both are transcribed from «Математикийн англи-монгол нэр томьёо, үг, хэллэгийн лавлах толь»
(Д.Пүрэвдорж), pp. 13–223. Batches are still being added; when a new one lands, both files and
these rules are regenerated, not hand-edited.

## A. Terminology

```bash
grep -i -P "^angle\t" docs/en-mn-math-glossary.tsv    # exact headword
grep -i    "angle"    docs/en-mn-math-glossary.tsv    # anything containing it
```

1. **Look it up first.** Before translating any mathematical term or phrase, search the
   glossary. Search the **whole phrase** you need (`alternate interior angles`,
   `common denominator`), not just its head noun — the book gives phrase-level renderings
   that differ from the sum of the parts.

2. **Use what the dictionary prints, verbatim.** Do not substitute a synonym you consider
   more natural or more modern. Where several equivalents are listed, the **first is the
   default** unless the note says otherwise. Copy the Cyrillic exactly — `ө`, `ү`, `ё` are
   distinct letters; never transliterate, never "normalise" spelling.

3. **Term not found → flag it, do not guess.** The glossary covers **A through I complete,
   and into J** (3,937 entries, pp. 13–223). Covered: *angle, area, circle, coefficient,
   decimal, denominator, derivative, equation, factor, formula, fraction, function, geometry,
   graph, hypotenuse, inequality, integer, integral, inverse, irrational number*.
   Not yet covered: *line, mean, median, multiply, number, parallel, percent, perimeter,
   polygon, prime, probability, quadratic, radius, ratio, rectangle, root, sequence, square,
   subtract, tangent, triangle, vertex, volume*.
   When a term is missing:
   - use your best rendering, and
   - mark it inline as `<!-- TERM? english_term -->` (or `// TERM? …` in code), and
   - list every such term at the end of your run, grouped and deduplicated.

   Never silently invent terminology. A wrong term repeated across a question bank is far
   more expensive to fix than a flagged one.

## B. Voice

**Read `docs/mn-voice-reference.md` before writing any Mongolian prose.** It is short, and it
is derived from 1,047 English sentences printed beside their published Mongolian rendering. The
non-negotiables from it:

4. **Condition first, thing second.** `Хэрэв [нөхцөл] бол [зүйл]-ийг [нэр] гэнэ.` English puts
   the condition last; Mongolian puts it first. Same for cause: reason + `тул`/`учраас`, then
   result. A trailing `хэрэв` clause is the clearest sign a sentence was written in English.

5. **Decimal comma, thousands space.** `36,27` not `36.27`. `78 696` not `78,696`. This applies
   to every number a student reads — question stems, answers, worked steps.

6. **Hyphenate case suffixes on numerals and Latin symbols.** `x-ийн`, `3-т`, `f(x)-ийг`,
   `90°-тай`.

7. **No em-dash parentheticals.** One appears in 745 passages of published Mongolian. Use `( )`
   for a gloss, `[ ]` for an aside.

8. **Task wording is a bare imperative.** `Доорх дүрс бүрийг хуулбарлан зур.` Not `-х хэрэгтэй`,
   not a polite construction.

9. **Do not compress to match the English.** Published Mongolian spells out reasoning the English
   leaves implicit. A step that explains *why* reads native; a clipped calque reads translated.

9a. **Worked solutions open with `Бодолт.`** and label their steps `1-р алхам`, `2-р алхам`.
    Use these in question banks rather than inventing a label.

10. **Name things with verbs, not participles.** `Үр дүн нь харагддаг`, not `Үр дүнд чиглэсэн`.
    Run the smell test at the end of the voice reference over anything you write.

11. **`сурагч`, never `оюутан`.** Оюутан is a university student; this site's readers are at school.

## C. Both

12. **Translate copy, not machinery.** Leave untouched: LaTeX and math markup, variable and
    function names, JSON keys, `className` values, route paths, IDs, code identifiers.
    Translate only the strings a student reads.

13. **Consistency across the codebase.** Once a term has a rendering, it keeps it everywhere —
    `src/data/*.json`, page copy and component labels included. If you find an existing
    translation that contradicts the glossary, fix it and say so, rather than matching it.

## Open decision — not yet settled

Students here sit **English-medium exams** (SAT, IB, AP). Whether to keep the English term
alongside the Mongolian on first use — `өнцгийн биссектрис (angle bisector)` — is a content
decision Khas has not made. **Ask before adopting either convention site-wide;** do not
decide it in passing inside a draft.
