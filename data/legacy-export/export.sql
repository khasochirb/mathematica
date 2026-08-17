-- Reproduces data/legacy-export/topics-and-problems.json.
--
-- Run against the production project (gsvfcnfbrzysaiiwgchf) BEFORE dropping
-- `topics` or `problems`. Both are non-empty; Supabase list_tables reports 0
-- for them, which is a stale planner estimate and is wrong.
--
-- Always re-check the real counts immediately before anything destructive:
--   select count(*) from topics;    -- 13 at export time
--   select count(*) from problems;  -- 20 at export time

select json_build_object(
  'exported_note',  'pre-drop export, Phase 0',
  'source_project', current_database(),
  'topics_count',   (select count(*) from topics),
  'problems_count', (select count(*) from problems),
  'topics',         (select coalesce(json_agg(to_jsonb(t) order by t.id), '[]'::json) from topics t),
  'problems',       (select coalesce(json_agg(to_jsonb(p) order by p.id), '[]'::json) from problems p)
) as export;
