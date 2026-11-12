# Usage-mastery report: build

- Kit: grokbot-usage-mastery v1.0.0
- Target: `/Users/home/REPOS/grokbot-factory/.worktrees/usage-mastery/ideas/idea-incubator/build`
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
| routines | Routine frequency audit (report only) | present | 17 schedules, about 264 runs a week; none more often than every 3 hours |
| skills-count | Skill count check (report only) | present | 11 skills (under 90) |
| prompt-weight | Instructions weight (report only) | present | about 1816 words of standing instructions memory holds (largest: master prompt 698, markets 217, dev 204); every turn and run re-reads them |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 56 | `15 */3 * * *` | TRIGGER-MAP.md | Schedule / `15 */3 * * *` / DEV-INTAKE: sweep new ideas into the board |
| 56 | `0 */3 * * *` | TRIGGER-MAP.md | Schedule / `0 */3 * * *` / LEAD-WATCH: watchdog |
| 42 | `25 1,5,9,13,17,21 * * *` | TRIGGER-MAP.md | Schedule / `25 1,5,9,13,17,21 * * *` / MKT-SCOUT: crypto scout on X |
| 28 | `35 2,8,14,20 * * *` | TRIGGER-MAP.md | Schedule / `35 2,8,14,20 * * *` / MKT-MARK: mark the paper book |
| 14 | `45 14,19 * * *` | TRIGGER-MAP.md | Schedule / `45 14,19 * * *` / DEV-BUILD: move the top dev idea forward with Claude Code |
| 7 | `50 12 * * *` | TRIGGER-MAP.md | Schedule / `50 12 * * *` / MKT-BRIEF: market brief and signals |
| 7 | `40 15 * * *` | TRIGGER-MAP.md | Schedule / `40 15 * * *` / PROMO-POSTS: draft or post today's product posts |
| 7 | `40 13 * * *` | TRIGGER-MAP.md | Schedule / `40 13 * * *` / HB-CHECK: read the workspace, check named computers |
| 7 | `35 16 * * *` | TRIGGER-MAP.md | Schedule / `35 16 * * *` / MKT-CREATOR-MOONDEV: follow Moon Dev |
| 7 | `30 23 * * *` | TRIGGER-MAP.md | Schedule / `30 23 * * *` / LEAD-SCORE: evening scoreboard and vault daily note |
| 7 | `30 13 * * *` | TRIGGER-MAP.md | Schedule / `30 13 * * *` / LEAD-PLAN: morning plan |
| 7 | `25 18 * * *` | TRIGGER-MAP.md | Schedule / `25 18 * * *` / HB-BUILD: build or install the next queued pack |
| 7 | `20 17 * * *` | TRIGGER-MAP.md | Schedule / `20 17 * * *` / PROMO-LISTINGS: Gumroad listing drafts |
| 7 | `10 23 * * *` | TRIGGER-MAP.md | Schedule / `10 23 * * *` / PROMO-SALES: sales proof |
| 2 | `5 15 * * 1,4` | TRIGGER-MAP.md | Schedule / `5 15 * * 1,4` / FACTORY-RUN: vet, pick, build, package one product |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS
- pack check (tools/check.py): RESULT: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/build-20261112-132411`

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
