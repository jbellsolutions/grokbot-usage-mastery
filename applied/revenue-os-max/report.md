# Usage-mastery report: build

- Kit: grokbot-usage-mastery v1.0.0
- Target: `/Users/home/REPOS/grokbot-factory/.worktrees/usage-mastery/ideas/revenue-os-max/build`
- Layout: factory-pack
- Mode: APPLY
- Edition: owner
- When: 2026-11-12T13:24:11

## Plan and result

| Step | What | Status | Detail |
|---|---|---|---|
| rules | Usage rules in every bot's memory | upgraded | replace usage rules block in MASTER-PROMPT.md with this version |
| skill | usage-saver skill and scripts | applied | upgrade usage/ (usage-saver skill: 10 scripts, AUDIT, RESET, LEDGER) |
| handoff | Install, ledger and weekly audit steps in the handoff | present | usage section in HANDOFF.md (this version) |
| routines | Routine frequency audit (report only) | present | 43 schedules, about 473 runs a week; none more often than every 3 hours |
| skills-count | Skill count check (report only) | present | 70 skills (under 90) |
| prompt-weight | Instructions weight (report only) | flag | about 3919 words of standing instructions memory holds (largest: master prompt 866, cold-email 335, sales-crm 300); every turn and run re-reads them; trim duplicates and move reference detail into files |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 56 | `57 */3 * * *` | TRIGGER-MAP.md | Schedule / `57 */3 * * *` / Watchdog |
| 49 | `30 13-19 * * *` | TRIGGER-MAP.md | Schedule / `30 13-19 * * *` / Show research |
| 42 | `50 13-23/2 * * *` | TRIGGER-MAP.md | Schedule / `50 13-23/2 * * *` / Partner replies |
| 42 | `15 12-22/2 * * *` | TRIGGER-MAP.md | Schedule / `15 12-22/2 * * *` / Reply check |
| 28 | `40 12-21/3 * * *` | TRIGGER-MAP.md | Schedule / `40 12-21/3 * * *` / Work the tickets |
| 21 | `25 13,17,21 * * *` | TRIGGER-MAP.md | Schedule / `25 13,17,21 * * *` / Pipeline sweep |
| 21 | `15 9,15,19 * * *` | TRIGGER-MAP.md | Schedule / `15 9,15,19 * * *` / Skool sweep |
| 7 | `50 20 * * *` | TRIGGER-MAP.md | Schedule / `50 20 * * *` / Follow-up |
| 7 | `50 11 * * *` | TRIGGER-MAP.md | Schedule / `50 11 * * *` / Partner find |
| 7 | `5 22 * * *` | TRIGGER-MAP.md | Schedule / `5 22 * * *` / Daily content |
| 7 | `5 18 * * *` | TRIGGER-MAP.md | Schedule / `5 18 * * *` / Apply to Justin's picks |
| 7 | `5 15 * * *` | TRIGGER-MAP.md | Schedule / `5 15 * * *` / Campaign read and copy |
| 7 | `5 14 * * *` | TRIGGER-MAP.md | Schedule / `5 14 * * *` / Radar sweep and Needs-you |
| 7 | `5 11 * * *` | TRIGGER-MAP.md | Schedule / `5 11 * * *` / Call prep |
| 7 | `45 19 * * *` | TRIGGER-MAP.md | Schedule / `45 19 * * *` / X engagement |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS
- pack check (tools/check.py): RESULT: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/build-20261112-132410`

Touched: `MASTER-PROMPT.md`, `usage/`

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
