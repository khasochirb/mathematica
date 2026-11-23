-- Who actually uses the site (Khas, 23 Nov 2026).
--
-- Run in the Supabase SQL editor (or via the Supabase MCP, read-only). One
-- row per account, oldest first, no emails: accounts are numbered so the
-- report can be shared. Activity = page views and 5-minute heartbeats from
-- components/ActivityTracker.tsx (from 23 Nov 2026 on), plus answers,
-- section-2 answers, other events and login-session refreshes (all history).
--
--   active_days            distinct days with any activity
--   active_days_after_signup   the same, excluding the signup day: 0 means
--                              "signed up and never came back"
--   minutes_est            heartbeats × 5, a floor on time spent since 23 Nov
--   pages                  distinct pages viewed since 23 Nov

with u as (
  select id, created_at,
         case when email like '%@mp.mn' or email like '%@mp.com' then 'school' else 'self sign-up' end as kind
  from auth.users
),
act as (
  select user_id, answered_at as t from public.attempts
  union all select user_id, created_at from public.section2_attempts
  union all select user_id, created_at from public.events where user_id is not null
  union all select user_id, coalesce(refreshed_at, updated_at) from auth.sessions
),
pv as (
  select user_id,
         count(*) filter (where name = 'heartbeat') * 5 as minutes_est,
         count(distinct properties->>'path') filter (where name = 'page_view') as pages,
         max(created_at) filter (where name in ('page_view', 'heartbeat')) as last_seen
  from public.events
  where name in ('page_view', 'heartbeat') and user_id is not null
  group by user_id
)
select row_number() over (order by u.created_at) as account,
       u.kind,
       u.created_at::date as signed_up,
       max(a.t)::date as last_activity,
       count(distinct a.t::date) as active_days,
       count(distinct a.t::date) filter (where a.t::date > u.created_at::date) as active_days_after_signup,
       coalesce(pv.minutes_est, 0) as minutes_est,
       coalesce(pv.pages, 0) as pages,
       (select count(*) from public.attempts x where x.user_id = u.id) as answers
from u
left join act a on a.user_id = u.id
left join pv on pv.user_id = u.id
group by u.id, u.kind, u.created_at, pv.minutes_est, pv.pages
order by u.created_at;
