# Usage-mastery report: build

- Kit: grokbot-usage-mastery v1.0.0
- Target: `/Users/home/REPOS/grokbot-factory/.worktrees/usage-mastery/ideas/find-me-money/build`
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
| routines | Routine frequency audit (report only) | flag | 29 schedules, about 882 runs a week; 28 pairs start under 5 minutes apart (Grok needs 5): Morning plan `30 12 * * *` and Read answers `*/30 * * * *`; Evening report `30 23 * * *` and Read answers `*/30 * * * *`; Mine Facebook groups `30 5 * * *` and Read answers `*/30 * * * *`; 5 run more than every 3 hours (see table): candidates for a slower cron or a script doorbell |
| skills-count | Skill count check (report only) | present | 46 skills (under 90) |
| prompt-weight | Instructions weight (report only) | flag | about 3548 words of standing instructions memory holds (largest: master prompt 744, muse 330, sales 317); every turn and run re-reads them; trim duplicates and move reference detail into files |
| present | Usage habits the pack already has | present | already built in: quiet runs end [SILENT], handoffs through files (requests/), guards as scripts, STOP switch, spend gate (never spend without a yes) |

## Routines by runs per week (most first)

| Runs/week | Cron | File | Line |
|---|---|---|---|
| 336 | `*/30 * * * *` | TRIGGER-MAP.md | Schedule / `*/30 * * * *` / Read answers / `bash repo/engine/jobs/fcm-job.sh triage "Read  |
| 84 | `5 */2 * * *` | TRIGGER-MAP.md | Schedule / `5 */2 * * *` / Scorecard / `bash repo/engine/jobs/fmm-scorecard.sh` (counts on |
| 84 | `45 */2 * * *` | TRIGGER-MAP.md | Schedule / `45 */2 * * *` / Applications / `bash repo/engine/jobs/fcm-job.sh sweep "Applic |
| 84 | `15 */2 * * *` | TRIGGER-MAP.md | Schedule / `15 */2 * * *` / Sort replies / The answers the sweep found: sort, draft the ne |
| 84 | `0 */2 * * *` | TRIGGER-MAP.md | Schedule / `0 */2 * * *` / File and draft / `bash repo/engine/jobs/fmm-cycle.sh` (CRM outb |
| 56 | `50 */3 * * *` | TRIGGER-MAP.md | Schedule / `50 */3 * * *` / Watchdog / `beat.py status --hours 26`, Grok's run records; on |
| 21 | `0 18,22,2 * * *` | TRIGGER-MAP.md | Schedule / `0 18,22,2 * * *` / Handoff watch / `bash repo/engine/jobs/fcm-job.sh watch "Ha |
| 7 | `40 17 * * *` | TRIGGER-MAP.md | Schedule / `40 17 * * *` / Partner match / `lending-hub-distribution`: preview, then propo |
| 7 | `30 5 * * *` | TRIGGER-MAP.md | Schedule / `30 5 * * *` / Mine Facebook groups / `bash repo/engine/jobs/fmm-fbgroups.sh` ( |
| 7 | `30 23 * * *` | TRIGGER-MAP.md | Schedule / `30 23 * * *` / Evening report / The day's numbers to Slack, one Notion row, `v |
| 7 | `30 20 * * *` | TRIGGER-MAP.md | Schedule / `30 20 * * *` / Muse import / `metamuse-leads` `muse_to_radar.py`: the day's fi |
| 7 | `30 19 * * *` | TRIGGER-MAP.md | Schedule / `30 19 * * *` / Affiliate replies / `affiliate-reply-triage`: sort partner and  |
| 7 | `30 18 * * *` | TRIGGER-MAP.md | Schedule / `30 18 * * *` / Wholesale match / Funding need to the partner desk; deals to pa |
| 7 | `30 17 * * *` | TRIGGER-MAP.md | Schedule / `30 17 * * *` / Lead Storm feed / `lead-storm-handoff`: approved social targets |
| 7 | `30 13 * * *` | TRIGGER-MAP.md | Schedule / `30 13 * * *` / Wholesaler sweep / `wholesale-funding`: today's wholesaler rows |

## Verify

- rules: PASS
- skill: PASS
- handoff: PASS
- pack check (tools/check.py): RESULT: PASS

Backup of every touched file: `/Users/home/.usage-mastery-backups/build-20261112-134124`

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
