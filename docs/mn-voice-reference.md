# How mathematical Mongolian actually reads

Derived from 1,147 passages transcribed out of «Математикийн англи-монгол нэр томьёо, үг, хэллэгийн лавлах толь» (Д.Пүрэвдорж), pp. 42–223 — **1,047 of them English sentences printed beside their published Mongolian rendering**.

This file exists because terminology alone does not fix voice. Looking up the right word for `angle` and then building the sentence around it in English word order produces Mongolian that a Mongolian reader instantly clocks as translated. The patterns below are what the published renderings actually do, with counts from the corpus.

- **The rules and examples here are the part to read.** The full corpus is `mn-voice-corpus.tsv` (`kind`, `english`, `mongolian`, `source_page`) — grep it for a construction you are unsure about.
- Every Mongolian line quoted below is transcribed verbatim from the book, typos included.

---

## 1. The clause order inverts

This is the single biggest tell. **English states the thing, then the condition. Mongolian states the condition, then the thing.** `Хэрэв` appears in 226 of the 1,147 passages, and 184 of them open with it.

The definition frame is:

```
Хэрэв [нөхцөл] бол [зүйл]-ийг [нэр] гэнэ.
```

> EN — Two angles are complementary angles if the sum of their measures is 90°.
> MN — **Хэрэв** хоёр өнцгийн градусан хэмжээний нийлбэр 90°–тай тэнцүү **бол** уг хоёр өнцөгийг гүйцээлт хоёр өнцөг **гэнэ**.

> EN — Two sets are equivalent when they have the same number of elements.
> MN — **Хэрэв** хоёр олонлог ижил тооны элементтэй **бол** тэдгээрийг эквивалент хоёр олонлог **гэнэ**.

Causation inverts the same way — English *result because reason*, Mongolian *reason* `тул`/`учраас` *result*:

> EN — …{-4} is the solution set, since -4-3=-7 is correct.
> MN — -4-3=-7 нь зөв **учраас** {-4} нь уг тэгшитгэлийн шийдлийн олонлог мөн.

> EN — 57 is nearer to 60, so 57 ≈ 60.
> MN — 57 нь 50, 60 хоёрын 60–тай нь илүү дөт. **Иймд** 57 ≈ 60.

A sentence that runs English-order — subject, verb, then a trailing `хэрэв` clause — is the most common way an AI draft gives itself away.

## 2. The naming verbs

| Use | Mongolian | Count |
|---|---|---|
| "is called" — the default for a definition | `гэнэ` | 133 |
| "is called" — introducing a term more fully | `гэж нэрлэдэг` | 91 |
| "is known as", "we say" | `гэдэг` | 42 |
| "is denoted by" | `гэж тэмдэглэдэг` | 17 |

> MN — …f(x) функцийн x цэг дээрх уламжлал **гэх бөгөөд** f '(x) **гэж тэмдэглэдэг**.

## 3. "if and only if" is `л бол`

29 instances. The particle `л` carries the biconditional on its own — no longer construction is needed.

> EN — An angle is dihedral **if and only if** it consists of two noncoplanar half planes with a common line.
> MN — Хэрэв өнцөг нь нэг хавтгай дээр оршоогүй ерөнхий хилтэй хоёр хагасхавтгайгаас бүтсэн **л бол** түүнийг хоёрталст өнцөг гэнэ.

## 4. `юм` closes a definitional assertion

106 instances. It is what makes a statement land as settled rather than clipped.

> MN — …математик анализын гол хоёр сэдэв бол уламжлал, интеграл хоёр **юм**.
> MN — Тэгшитгэл бодох нэгэн арга бол өгсөн тэгшитгэлийг тэнцүү чанартай хувиргаж цуврал хялбар тэгшитгэл гаргах явдал **юм**.

## 5. Task wording is a bare imperative

Practice instructions are short and end in a bare verb stem. No `-х хэрэгтэй`, no "you should", no polite padding.

```
Доорх [юм] бүрийг [үйл үг].
```

> Доорх дүрс бүрийг хуулбарлан **зур**.
> Доорх бутархай бүрийг аравтын бутархай **болго**.
> Доорх илэрхийлэл бүрийн утгыг **ол**.
> Энэ мэдээг дүрсэлсэн гистограм **зур**.
> Суурь, илтгэгчийг **тодорхойл**.
> ⊃ буюу ⊂ тэмдэг тавьж үнэн хэллэг **үүсгэ**.

The stock verbs: `ол` (find), `бич` (write), `зур` (draw), `байгуул` (construct), `болго` (convert), `хий` (insert/do), `тодорхойл` (determine), `ангил` (classify), `хуваа` (divide), `үүсгэ` (form), `үргэлжлүүл` (continue).

`Доорх` (36) is the book's usual "the following"; `Дараах` (7) also appears. Both are fine; `Доорх` is the house default.

**The one exception** — when the text addresses the reader directly rather than setting a task, it turns polite with `-на уу` / `-нэ үү`. Only 2 instances in 1,147, so use it sparingly:

> Уншигч та бие даан **батална уу**.

## 6. Worked solutions open with `Бодолт`

7 instances. The Mongolian equivalent of "Solution:" — this is the label to use in a question bank.

> **Бодолт.** Хэрэв тодорхойлолт ашиглавал: (f∘g)(x)=f[g(x)]=(∛(x+1))³−1=x+1−1=x…
> **Бодолт:** а) f(x)=2x+5; y=2x+5, x=2y+5; 2y=x–5, y=(x–5)/2; f⁻¹(x)=(x–5)/2.

Multi-step methods label their steps `1-р алхам`, `2-р алхам`, `3-р алхам`.

## 7. Numbers — decimal **comma**, thousands **space**

The corpus is unambiguous: 56 comma-decimals against 5 period-decimals, while the English column of the same pages uses 24 period-decimals.

| English | Mongolian |
|---|---|
| 36.27 | **36,27** |
| 2.6021 | **2,6021** |
| 0.1818… | **0,1818…** |
| 1.6 | **1,6** |
| 78,696 | **78 696** |
| 123,456 | **123 456** |

This is the most mechanical thing on the list and the easiest to get wrong across a whole question bank.

## 8. Case suffixes on numerals and Latin symbols take a hyphen

264 instances. The suffix is never a separate word and never runs on unmarked.

> `x-ийн`, `3-т`, `2-ыг`, `n-ийн`, `f(x)-ийг`, `A-аас`, `90°-тай`, `0-ээс`, `b-д`, `p⇒q-ийн`

> MN — **3–д** хуваахад 2 үлдэгдэл гарах … тийм бүхэл тоо олох бодлого …

## 9. Parentheses and square brackets — not dashes

The em dash appears **once in 1,147 passages**. Mongolian mathematical prose uses `( )` for a gloss and `[ ]` for the writer's clarifying aside.

> MN — …уг функц x=c цэг дээр тасралттай **(тасрана)** **[**дараагийн нүүрийн эхний зураг f(x) функц x=2 цэг дээр … тасралттай байна.**]**.

An em-dash parenthetical in Mongolian copy is an English punctuation habit, not a Mongolian one.

## 10. Mongolian is more explicit than the English, not less

Where the English is terse, the published Mongolian routinely spells out the reasoning. Compressing to match the English word count is what makes a draft read thin.

> EN — Borrow a ten. Write 2 above the tens column and 17 above the ones.
> MN — 7-гоос 8-ыг хасаж болохгүй учир өмнөх орны арваас нэг арвыг зээлж, аравын (аравтын) орны дээр үлдсэн 2 (арвыг) бичээд зээлсэн 10 дээрээ 7-г нэмж 17 болгоод түүнийг нэгжийн орны дээр бичнэ.

The Mongolian adds *why you borrow* and *what you do with the 10*. That is not padding — it is the register.

## 11. Small connectives the book actually uses

`Иймд` (therefore, 18) · `тул` / `учраас` (because, clause-final, 31) · `бөгөөд` (and, joining clauses, 48) · `харин` (whereas) · `Тодруулж хэлбэл` (that is, i.e.) · `Үүнд` (where, namely) · `Жишээ:` / `Жишээлбэл:` / `Жишээ нь:` (for example, 48) · `1-рт, … 2-рт, …` (first, … second, …) · `нь` as the topic marker, in 569 of 1,147 passages.

Register note: this is **expository textbook Mongolian**. Parent-facing and conversational writing takes softer connectors and sentence-final softeners (`Гэхдээ`, `Тиймээс`, `Учир нь`, `байгаа`, `шүү дээ`) that this book, being a reference work, does not use. Match the register to the reader, not to this file alone.

---

## Smell test — signs a Mongolian draft was written in English first

1. **Participle phrase used as a heading.** `Үр дүнд чиглэсэн`, `Соёлтой холбогдсон`. Mongolian names things with verbs: `Үр дүн нь харагддаг`, `Соёлоо мартдаггүй`.
2. **`сонирхолтой` for "interested".** It means *the thing is interesting*. A person who is interested `сонирхдог`.
3. **`оюутан` for a school pupil.** Оюутан is a university student. School children are `сурагч`.
4. **`-тай холбогдсон` standing in for the English "-connected", "-related", "-driven", "-focused"** suffix family. There is usually a plain verb instead.
5. **Em-dash parentheticals.** See §9.
6. **Noun-stacking where a verb belongs** — abstract nominalisations chained with genitives, mirroring English noun phrases.
7. **Condition clause trailing the main clause.** See §1.
8. **Decimal points and comma thousands separators.** See §7.
9. **Sentences exactly as long as the English.** See §10.

---

## Provenance

1,147 passages, pages 42–223, by kind: 1,047 `pair` (English sentence with its published Mongolian rendering), 55 `definition`, 24 `instruction`, 21 `solution`. The Mongolian is transcribed verbatim, including the book's own typos — do not treat a typo in the corpus as a spelling model. When the next batch of pages is transcribed, these counts and any new patterns should be re-derived rather than assumed.
