-- Topic + subtopic canonicalization for existing attempts rows.
-- Run on staging first, then prod. Idempotent (IS DISTINCT FROM clauses prevent
-- redundant updates). Matches the canonicalizeTopic / canonicalizeSubtopic
-- functions in lib/esh-questions.ts.

-- Topic: lowercase + trim + fall back to "other" for non-canonical values
UPDATE attempts
SET topic = CASE
  WHEN LOWER(TRIM(topic)) IN (
    'algebra','geometry','trigonometry','calculus','probability',
    'statistics','sequences','functions','logarithms','combinatorics'
  ) THEN LOWER(TRIM(topic))
  ELSE 'other'
END
WHERE topic IS DISTINCT FROM (
  CASE
    WHEN LOWER(TRIM(topic)) IN (
      'algebra','geometry','trigonometry','calculus','probability',
      'statistics','sequences','functions','logarithms','combinatorics'
    ) THEN LOWER(TRIM(topic))
    ELSE 'other'
  END
);

-- Subtopic: trim + lowercase + collapse internal whitespace; preserve NULL
UPDATE attempts
SET subtopic = REGEXP_REPLACE(LOWER(TRIM(subtopic)), '\s+', ' ', 'g')
WHERE subtopic IS NOT NULL
  AND subtopic IS DISTINCT FROM REGEXP_REPLACE(LOWER(TRIM(subtopic)), '\s+', ' ', 'g');

-- Verification queries (run after, expect canonical-only output):
-- SELECT DISTINCT topic FROM attempts ORDER BY topic;
-- SELECT subtopic, COUNT(*) FROM attempts WHERE subtopic IS NOT NULL GROUP BY subtopic ORDER BY subtopic;
