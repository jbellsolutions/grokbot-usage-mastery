# Usage-mastery report: tmec-grokbot

- Kit: grokbot-usage-mastery v1.0.0
- Target: `/Users/home/AI OS Market Share /AIOS/Client Builds/Tommy/tmec-grokbot`
- Layout: multi-bot-pack
- Mode: APPLY
- Edition: client
- When: 2026-11-12T13:43:38

## Plan and result

| Step | What | Status | Detail |
|---|---|---|---|
| rules | Usage rules in every bot's memory | present | policies/USAGE.md and START-HERE lines present (this version) |
| skill | usage-saver skill and scripts | applied | upgrade usage/ (usage-saver skill: 10 scripts, AUDIT, RESET, LEDGER) |
| handoff | Install, ledger and weekly audit steps in the handoff | present | usage section in START-HERE.md (this version) |
| routines | Routine frequency audit (report only) | present | 18 schedules, about 55 runs a week; none more often than every 3 hours |
| skills-count | Skill count check (report only) | present | 28 skills (under 90) |
| prompt-weight | Instructions weight (report only) | present | about 318 words of standing instructions memory holds (largest: 06-crm-reactivation 318, 07-content-studio 295, 03-dream-100 293); every turn and run re-reads them |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 7 | `13 5 * * *` | 02-lead-radar.md | Schedule / `13 5 * * *` / Radar sweep / Every day at 5:13 AM |
| 5 | `57 5 * * 1-5` | 09-ops.md | Schedule / `57 5 * * 1-5` / Capacity board / Every weekday at 5:57 AM |
| 5 | `49 13 * * 1-5` | 05-trades-outreach.md | Schedule / `49 13 * * 1-5` / Trades replies / Every weekday at 1:49 PM |
| 5 | `47 17 * * 1-5` | 01-tmec-command.md | Schedule / `47 17 * * 1-5` / Evening brief / Every weekday at 5:47 PM |
| 5 | `43 13 * * 1-5` | 04-dream-500.md | Schedule / `43 13 * * 1-5` / Dream 500 replies / Every weekday at 1:43 PM |
| 5 | `37 13 * * 1-5` | 03-dream-100.md | Schedule / `37 13 * * 1-5` / Dream 100 replies / Every weekday at 1:37 PM |
| 5 | `31 5 * * 1-5` | 06-crm-reactivation.md | Schedule / `31 5 * * 1-5` / CRM sweep / Every weekday at 5:31 AM |
| 5 | `23 7 * * 1-5` | 03-dream-100.md | Schedule / `23 7 * * 1-5` / Dream 100 drafts / Every weekday at 7:23 AM |
| 5 | `17 6 * * 1-5` | 01-tmec-command.md | Schedule / `17 6 * * 1-5` / Morning brief / Every weekday at 6:17 AM |
| 1 | `7 8 * * 1` | 07-content-studio.md | Schedule / `7 8 * * 1` / Content week / Every Monday at 8:07 AM |
| 1 | `53 7 * * 3` | 06-crm-reactivation.md | Schedule / `53 7 * * 3` / Reactivation batch / Every Wednesday at 7:53 AM |
| 1 | `43 6 * * 4` | 07-content-studio.md | Schedule / `43 6 * * 4` / Newsletter / Every Thursday at 6:43 AM |
| 1 | `41 7 * * 2` | 05-trades-outreach.md | Schedule / `41 7 * * 2` / Trades wave prep / Every Tuesday at 7:41 AM |
| 1 | `41 7 * * 1` | 04-dream-500.md | Schedule / `41 7 * * 1` / Dream 500 wave prep / Every Monday at 7:41 AM |
| 1 | `3 6 * * 1` | 10-forecast.md | Schedule / `3 6 * * 1` / Monday scoreboard / Mondays at 6:03 AM |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/tmec-grokbot-20261112-134338`

Touched: `usage/`

## Needs the owner's yes (not applied)

| Trick | Why it waits | What it needs |
|---|---|---|
| Free 'intern': let a free model read long media first | Needs a new key and sends content to a third party | A Gemini API key from the owner, and a rule limiting it to public material |
| Outside 'doorbell' for page watching (Cloudflare Worker or changedetection.io) | Needs a Cloudflare (or server) account and the webhook path confirmed | Owner's Cloudflare sign-in, and one test that a routine webhook wakes the bot |
| Ready-made scrapers (Apify actors) instead of bot browsing | Paid per run; spend needs a yes, and lead data must not be bought enrichment | Owner's yes per use, with a capped cost |
| A second plan seat with a synced 'fleet brain' | Spend, a terms question, and a conflict with one-account-per-business | Owner's decision after the ledger shows the first account still runs out with every other trick applied |
| Hand heavy coding to a coding CLI on the bot's computer | Puts a subscription token on a shared computer | Owner's yes, with the token entered only through the secure secret path |
| 'Route traffic through this computer' for sites that block the bot | Exposes the owner's IP; near the never-get-around-a-block gate | Owner's yes per site |
| Import Claude skills and memory | Can copy private details into memory | Owner reviews what would be imported first |

## Measure it

Savings in MASTERY.md are the sources' own tests until your ledger shows them. Take a usage reading before this change and one a week later (`usage/LEDGER.md`).
