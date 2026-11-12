# Usage-mastery report: template

- Kit: grokbot-usage-mastery v1.0.0
- Target: `/Users/home/REPOS/grokbot-factory/.worktrees/usage-mastery/template`
- Layout: factory-pack
- Mode: APPLY
- Edition: owner
- When: 2026-11-12T13:41:25

## Plan and result

| Step | What | Status | Detail |
|---|---|---|---|
| rules | Usage rules in every bot's memory | present | usage rules already in MASTER-PROMPT.md (this version) |
| skill | usage-saver skill and scripts | applied | upgrade usage/ (usage-saver skill: 10 scripts, AUDIT, RESET, LEDGER) |
| handoff | Install, ledger and weekly audit steps in the handoff | present | usage section in HANDOFF.md (this version) |
| routines | Routine frequency audit (report only) | flag | 3 schedules, about 182 runs a week; 1 run more than every 3 hours (see table): candidates for a slower cron or a script doorbell |
| skills-count | Skill count check (report only) | present | 1 skills (under 90) |
| prompt-weight | Instructions weight (report only) | present | about 803 words of standing instructions memory holds (largest: master prompt 539, _role-template 140, lead 124); every turn and run re-reads them |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 168 | `0 * * * *` | TRIGGER-MAP.md | Schedule / `0 * * * *` / Watchdog |
| 7 | `30 23 * * *` | TRIGGER-MAP.md | Schedule / `30 23 * * *` / Evening scoreboard and vault daily note |
| 7 | `30 13 * * *` | TRIGGER-MAP.md | Schedule / `30 13 * * *` / Morning plan |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS
- pack check (tools/check.py): RESULT: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/template-20261112-134125`

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
