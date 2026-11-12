# Usage-mastery report: build

- Kit: grokbot-usage-mastery v1.0.0
- Target: `<factory>/ideas/smart-contracting/build`
- Layout: factory-pack
- Mode: APPLY
- Edition: client
- When: 2026-11-12T13:32:20

## Plan and result

| Step | What | Status | Detail |
|---|---|---|---|
| rules | Usage rules in every bot's memory | present | usage rules already in MASTER-PROMPT.md (this version) |
| skill | usage-saver skill and scripts | applied | upgrade usage/ (usage-saver skill: 10 scripts, AUDIT, RESET, LEDGER) |
| handoff | Install, ledger and weekly audit steps in the handoff | present | usage section in HANDOFF.md (this version) |
| routines | Routine frequency audit (report only) | present | 12 schedules, about 47 runs a week; none more often than every 3 hours |
| skills-count | Skill count check (report only) | present | 11 skills (under 90) |
| prompt-weight | Instructions weight (report only) | flag | about 2753 words of standing instructions memory holds (largest: master prompt 1061, lead 356, dream100 329); every turn and run re-reads them; trim duplicates and move reference detail into files |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 10 | `0 10,14 * * 1-5` | TRIGGER-MAP.md | Schedule / `0 10,14 * * 1-5` / SC Reply sweep: sort replies, draft each, call cards |
| 6 | `15 6 * * 1-6` | TRIGGER-MAP.md | Schedule / `15 6 * * 1-6` / SC Radar sweep: group posts, reply drafts, storm watch |
| 5 | `45 6 * * 1-5` | TRIGGER-MAP.md | Schedule / `45 6 * * 1-5` / SC Trades batch: today's 10 rows of an approved wave, as one i |
| 5 | `30 7 * * 1-5` | TRIGGER-MAP.md | Schedule / `30 7 * * 1-5` / SC Morning list: the numbered approval list, in chat and copie |
| 5 | `30 6 * * 1-5` | TRIGGER-MAP.md | Schedule / `30 6 * * 1-5` / SC Dream 500 batch: today's 10 rows of an approved wave, as on |
| 5 | `0 6 * * 1-5` | TRIGGER-MAP.md | Schedule / `0 6 * * 1-5` / SC Dream 100 drafts: 5 first emails, plus follow-ups due |
| 5 | `0 17 * * 1-5` | TRIGGER-MAP.md | Schedule / `0 17 * * 1-5` / SC Evening wrap: watchdog, the wrap in Slack, the vault daily  |
| 2 | `0 5 * * 1,3` | TRIGGER-MAP.md | Schedule / `0 5 * * 1,3` / SC Dream 100 research: keep the list at 100, scored |
| 1 | `30 5 * * 3` | TRIGGER-MAP.md | Schedule / `30 5 * * 3` / SC Trades list build: top ten per trade, scored |
| 1 | `0 9 * * 2` | TRIGGER-MAP.md | Schedule / `0 9 * * 2` / SC Referral campaigns: each referral partner's next step |
| 1 | `0 5 * * 2` | TRIGGER-MAP.md | Schedule / `0 5 * * 2` / SC Dream 500 wave prep: next segment's list and wave item |
| 1 | `0 15 * * 5` | TRIGGER-MAP.md | Schedule / `0 15 * * 5` / SC Friday scoreboard for Mike |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS
- pack check (tools/check.py): RESULT: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/build-20261112-133220`

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
