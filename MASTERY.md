# GrokBot usage mastery, v1.0.0

The ranked playbook for getting the most out of Grok Bot (xAI) for the least usage. Every trick names its sources, dates, evidence, risk and fit. Generated from [`tricks/tricks.json`](tricks/tricks.json) by `bin/render.py`; edit the JSON, not this page.

**How usage works (xAI FAQ, 2026-11-12):** one weekly pool per account, shared with the Grok apps; extra usage bills by token only if on-demand or Auto top-up is on. There is no model picker. All your bots share one cloud computer, which is not a security boundary between them. Memory is per bot. **Where it goes:** each turn and each routine run re-reads the chat. In the one export we have, about 93% of tokens were re-reading history and under 1% were answers. So the big levers are fewer wake-ups, shorter chats, and smaller things to read.

**Apply it:** hand this repo (or its release zip) to Claude Code or your Grok bot and point it at [APPLY.md](APPLY.md).

## The top ten

| # | Trick | Evidence | How it lands |
|---|---|---|---|
| 1 | [Slow routines down; merge small checks](#routine-frequency) | xAI docs | kit applies it |
| 2 | [Hard cap on extra usage: Auto top-up off or a monthly limit](#spend-cap) | xAI docs | owner click or paste |
| 3 | [Find where usage goes: analyze the usage export](#usage-export) | shown in source | kit applies it |
| 4 | [Trim the instructions every turn re-reads](#trim-instructions) | shown in source | kit applies it |
| 5 | [One job per chat; restart heavy chats from a handoff note](#fresh-chat) | shown in source | kit applies it |
| 6 | [Shrink before the bot reads: clean pages, pick fields, grep lines, query sheets, PDF to text](#read-less-scripts) | measured here | kit applies it |
| 7 | [Turn a repeated job into a script that needs no AI](#script-the-repeat) | claim | kit applies it |
| 8 | [Connectors and APIs before the browser](#connectors-first) | claim | kit applies it |
| 9 | [Text, not screenshots; crop when you must](#text-not-images) | claim | kit applies it |
| 10 | [Batch fixes into one message](#batch-fixes) | claim | kit applies it |

## Setup

<a id="few-bots-few-roles"></a>
### 20. Few bots, few roles, handoffs through files

Sources split two ways. One bot per kind of job keeps each chat short (the seed creator claims 4x less re-reading). A separate bot for routines keeps scheduled runs out of the chat you use all day: every scheduled run lands in its bot's chat (an X article, relayed in a video). Our factory rule is one bot with a few roles, routines that open with 'Role: X', and handoffs through requests/ files. Justin chose it ('keep it the simplified version'). The open question is whether each routine run re-reads the bot's whole chat. If it does, a one-bot pack with 45 routines grows one long chat fast. Measure it on the test day: compare the usage of the same quiet run on day 1 and day 7. Until then: chat with the bot in fresh chats, not the routines' chat; let the weekly audit flag a heavy chat; reset from a handoff note (trick 16). Split routines into a second bot only if the measurement says so.

- **Evidence (claim):** Claims on both sides; nothing measured on Grok Bot. Our rule comes from the Hermes-to-Grok comparison and Justin's choice.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** already in our packs. Test-day measurement decides whether routines move to their own bot
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I)


## Prompts and skills

<a id="script-the-repeat"></a>
### 7. Turn a repeated job into a script that needs no AI

Do the job once with the bot, check and fix it, then: 'Turn exactly what you just did into a script that needs no AI. Test it on today's data and show it matches.' Save it as a skill; next time the bot runs the script and replies in two lines, flagging only odd numbers. Never script a job that isn't right yet.

- **Evidence (claim):** Three independent creators recommend it; claimed up to 11x less usage. Not metered by them. Our factory packs already run their plumbing as scripts (guards, beat.py, job scripts).
- **Risk:** low: a wrong job frozen into a script, so test first
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-05](https://youtu.be/akCTUJhZnZE); [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o)

<a id="batch-fixes"></a>
### 10. Batch fixes into one message

Brain-dump every change at once (dictation helps), send once, apply in one pass. Standing rule: if fixes arrive one at a time, ask whether there are more before starting. Don't send 'thanks' or 'ok': each is a full re-read.

- **Evidence (claim):** Two creators; the seed creator claims about 10x less reading. Mechanism matches the docs.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o)

<a id="brief-once"></a>
### 11. Brief once with a done list

State the goal, why, what to avoid, and 3 to 5 lines that must be true at the end, plus a limit (pages, steps, minutes) and a stop condition. At the end the bot marks each line pass, fail or unknown and fixes only the fails.

- **Evidence (claim):** Claimed about 5x less per job (seed creator). A vague ask gets a guess, and every 'not like that' re-reads the growing chat.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I)

<a id="short-replies"></a>
### 17. Short replies and silent quiet runs

No preamble, no recap, no thanks; a quiet routine run ends with exactly [SILENT]. Small win: answers are under 1% of tokens in the one export we have, so the gain is in not growing the chat that later turns re-read.

- **Evidence (claim):** Claim; the factory packs already do [SILENT].
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** already in our packs
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="teach-a-task"></a>
### 24. Teach a task: record it once, get a skill

'Teach a task' (bottom left) records you doing a job on the bot's computer and turns it into an SOP and skill. Then script it (trick 5). Never type a password while recording.

- **Evidence (shown in source):** Flow shown; the resulting skill not shown.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** know it, nothing to apply
- **Sources:** [youtube 2026-11-05](https://youtu.be/akCTUJhZnZE)

<a id="import-claude-setup"></a>
### 31. Import Claude skills and memory

Settings → Import memory, or a prompt that finds Claude skill folders and CLAUDE.md files on the computer and saves them as skills and memory.

- **Evidence (shown in source):** Shown running.
- **Risk:** med: CLAUDE.md files can carry private details into the bot's memory; more skills means more to load
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner reviews what would be imported first
- **Sources:** [youtube 2026-11-05](https://youtu.be/akCTUJhZnZE); [youtube 2026-11-02](https://youtu.be/48LXEHEUiCA)


## Memory and context

<a id="trim-instructions"></a>
### 4. Trim the instructions every turn re-reads

Master prompt, role sections and saved memory are re-read on every turn and every routine run. Cut duplicated rules and stale facts. Move reference detail into files the bot opens only when a job needs it ('see context/x.md'). Keep the always-on part to rules and pointers. The kit's own rules block is about 150 words for this reason, and apply.py reports each pack's weight.

- **Evidence (shown in source):** Shown: about 13% saving in one creator's export analysis. The pointer-to-file pattern is from a community recipe marked unverified by its own author.
- **Risk:** low: a rule moved to a file the bot never opens is a rule lost, so keep the gates in the prompt
- **Fits GrokBot:** yes
- **Lands as:** kit applies it. The kit reports weight; trimming a pack's prompt goes through its PR
- **Sources:** [youtube 2026-11-09](https://youtu.be/WRqZktcjJl8); [github 2026-10-18](https://github.com/sit-in/awesome-grokbot-playbooks/blob/main/examples/routine-budget.md)

<a id="fresh-chat"></a>
### 5. One job per chat; restart heavy chats from a handoff note

Each message makes the bot re-read the whole chat, files it dragged in included. Start a new chat (+) per job; idle chats cost nothing. When a chat is long, have the bot write a short handoff note (role, rules, open jobs, done work) and continue from it in a fresh chat.

- **Evidence (shown in source):** One builder's export of about 60 bots and 4.6B tokens in a week: about 93% of tokens were re-reading history and under 1% were answers. A fresh chat started near 16k tokens; old bots read 200k to 380k before acting. The seed creator claims about 75% less per turn after a reset. Single sources, consistent with the docs' description of memory.
- **Risk:** low: a thin note loses context, so check the new chat on current work first
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-03](https://www.youtube.com/watch?v=o5vpYc6DoZ0); [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o); [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="read-less-scripts"></a>
### 6. Shrink before the bot reads: clean pages, pick fields, grep lines, query sheets, PDF to text

Run a small free script on the bot's computer and give the model only its output: trafilatura for the article text of a page, jq or pick.py for the fields of a big JSON reply, ripgrep for matching lines, DuckDB (or sqlite) for a one-line answer from a spreadsheet, pdftotext or pypdf for a PDF. The kit ships all of these as the usage-saver skill, with stdlib fallbacks.

- **Evidence (measured here):** Measured here (characters in vs out): Wikipedia's Costco page 1,242,861 → 103,714 (92% less, trafilatura); GitHub search reply 197,044 → 2,573 (98.7%, pick.py); 86,352-row airports CSV 12.76 MB → an 85-character answer (sheet_q.py, DuckDB and sqlite agree); a 15-page PDF 2.2 MB → 59,599 characters of text (pdf2txt.py); 12,449 characters of code → 772 matching lines (grep_lines.sh). The creator's own tests: 4.5M tokens → 57,900 across seven jobs.
- **Risk:** low: open-source, pinned, no keys, nothing leaves the computer
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-06](https://youtu.be/ow6x3pdwydA); [github 2026-11-11](https://github.com/adbar/trafilatura); [github 2026-11-02](https://github.com/jqlang/jq); [github 2026-11-09](https://github.com/BurntSushi/ripgrep); [github 2026-11-12](https://github.com/duckdb/duckdb)

<a id="text-not-images"></a>
### 9. Text, not screenshots; crop when you must

Copy the words instead of a screenshot; crop to the part that matters; turn a PDF into a text file first. Saying 'the blue button top right' beats a full-screen image.

- **Evidence (claim):** Two creators; the seed creator claims images cost about 20 times text (unmeasured on Grok Bot).
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o)

<a id="reset-heavy-bot"></a>
### 18. Reset a heavy bot from its must-keep memory

Export the rules, facts and open jobs that must survive, duplicate the bot (duplicating keeps settings, skills and routines but not chat or memory), feed the note back, stop the old bot's routines so nothing runs twice, keep the old one hidden a week, delete only on a separate yes. Steps in usage/RESET.md.

- **Evidence (shown in source):** Shown in one video; claimed about 75% less per turn.
- **Risk:** med: routines can run twice or context can be lost; owner-approved only
- **Fits GrokBot:** yes
- **Lands as:** owner click or paste. Owner's yes per bot, after the weekly audit flags it
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I)

<a id="rtk"></a>
### 32. rtk for long developer command output

A proxy that shortens git, test and build output. The kit's shorten.py covers the general case without an install; rtk is worth it only on a bot that codes.

- **Evidence (shown in source):** The creator's test: 56% fewer tokens.
- **Risk:** low
- **Fits GrokBot:** partial
- **Lands as:** know it, nothing to apply
- **Sources:** [github 2026-11-12](https://github.com/rtk-ai/rtk); [youtube 2026-11-06](https://youtu.be/ow6x3pdwydA)


## Tools and connectors

<a id="connectors-first"></a>
### 8. Connectors and APIs before the browser

Browser use is screenshot, click, check, repeated, each step metered. Where a Connect app (Gmail, Slack, Calendar, GitHub) or an API exists, use it. Weekly: 'Which jobs used the browser for an app that has a connector?'

- **Evidence (claim):** Two independent sources plus the seed creator's estimate that a web page visit costs about 70 times a chat turn (his claim, unmeasured).
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o); [forum 2026-10-18](https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188); [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="prune-plugins-roster"></a>
### 19. Prune unused plugins, skills and bots

Uninstall plugins that error or go unused; a front-door bot that checks the roster each turn pays for every extra bot. The seed creator keeps each account under about 90 skills. Hide rather than delete; deleting a bot removes its chat and routines.

- **Evidence (shown in source):** Shown being done; savings are the creators' reasoning, unmeasured. The 90-skill figure is one creator's rule of thumb.
- **Risk:** med for deletes: owner-approved only
- **Fits GrokBot:** yes
- **Lands as:** owner click or paste. Owner acts on the weekly audit's list
- **Sources:** [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I); [youtube 2026-11-03](https://www.youtube.com/watch?v=V7dsUn8xh6Y); [youtube 2026-10-29](https://youtu.be/UClMrBShiYc); [youtube 2026-11-04](https://youtu.be/Zz3Ixk2Tzpo)

<a id="gemini-intern"></a>
### 25. Free 'intern': let a free model read long media first

Store a Google Gemini free-tier key as a secret; long PDFs, videos and audio go to Gemini for a summary, and the bot reads only the summary.

- **Evidence (claim):** Claimed 96% less reading; not shown measured.
- **Risk:** med: free tiers may use inputs for training, so public material only, never client, contact or deal data
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). A Gemini API key from the owner, and a rule limiting it to public material
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="apify-actors"></a>
### 27. Ready-made scrapers (Apify actors) instead of bot browsing

Connect Apify in Connect apps and let an actor do bulk scraping; the bot only configures it and reads the result.

- **Evidence (shown in source):** Shown connecting; savings claimed.
- **Risk:** med: paid per run, and lead scraping sits close to the no-paid-enrichment rule
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner's yes per use, with a capped cost
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="coding-cli-on-box"></a>
### 29. Hand heavy coding to a coding CLI on the bot's computer

Install Claude Code or Codex on the bot's computer and route coding to it, moving that spend to a separate plan. Or keep coding on a Mac with Claude Code and share a private repo with the bot.

- **Evidence (shown in source):** Install shown; savings claimed.
- **Risk:** med/high: one cloud computer is shared by every bot and is not a security boundary, so the token is visible to all of them
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner's yes, with the token entered only through the secure secret path
- **Sources:** [youtube 2026-11-03](https://www.youtube.com/watch?v=V7dsUn8xh6Y); [youtube 2026-11-05](https://youtu.be/akCTUJhZnZE)


## Cost and usage limits

<a id="spend-cap"></a>
### 2. Hard cap on extra usage: Auto top-up off or a monthly limit

Past the weekly pool, usage bills by token only if on-demand or Auto top-up is on. Leave Auto top-up off, or set a monthly additional-usage limit at grok.com/dashboard/billing. A running task can overshoot the cap a little.

- **Evidence (xAI docs):** Official FAQ. The seed creator spent about $550 of extra credits in one day without a cap.
- **Risk:** low: the bot pauses at the limit instead of billing
- **Fits GrokBot:** yes
- **Lands as:** owner click or paste. Owner: grok.com/dashboard/billing → monthly additional usage limit (or Auto top-up off)
- **Sources:** [docs 2026-11-12](https://docs.x.ai/grok-bot/faq); [youtube 2026-11-06](https://www.youtube.com/watch?v=6NIQpRr6nkQ); [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="usage-export"></a>
### 3. Find where usage goes: analyze the usage export

Export the detailed usage CSV from the usage dashboard (on Cursor-linked plans: cursor.com/dashboard → Usage → Export CSV) and break it down by bot and kind. Do it with usage_csv.py on the computer, not by uploading the file into a bot chat, which would itself be read on every later turn. Fix the biggest line first.

- **Evidence (shown in source):** Shown: one creator found 58% of usage was routines and 81% was bots re-reading their instructions and memory. Trimming instructions saved about 13% and stopping one hourly routine about 7% (his estimate from the export). Another builder's export showed 93% re-reading. The CSV's columns aren't documented, so usage_csv.py guesses them.
- **Risk:** low: the export may name bots and jobs, so keep it out of public places
- **Fits GrokBot:** yes
- **Lands as:** kit applies it. Owner downloads the CSV into data/usage/ (the bot can't sign in to the dashboard)
- **Sources:** [youtube 2026-11-09](https://youtu.be/WRqZktcjJl8); [docs 2026-11-12](https://docs.x.ai/grok-bot/faq); [youtube 2026-11-03](https://www.youtube.com/watch?v=o5vpYc6DoZ0)

<a id="usage-audit"></a>
### 12. Weekly usage audit, report only

Once a week the bot lists its routines (runs, found-anything rate), browser sessions, screenshots, whole-file reads, repeat jobs, skill count and heavy chats, and proposes the top three changes. It changes nothing. Cross-check with the per-bot breakdown on the usage dashboard. The kit folds it into the Monday evening report, so it adds no routine.

- **Evidence (shown in source):** Shown in three videos (one fleet went from 79 bots to about 30; another found a monitor bot using 25%). The bot's own estimate is a guess; the dashboard is the real number.
- **Risk:** low: report only
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o); [youtube 2026-10-29](https://youtu.be/UClMrBShiYc); [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I)

<a id="usage-ledger"></a>
### 13. Measure: a usage reading before and after every change

Usage shows under Usage at grok.com/dashboard, with a per-bot breakdown. Write the % used and the reset date into log/usage-ledger.md before a change and a week after. Every saving in this playbook is a source's claim until the ledger shows it.

- **Evidence (xAI docs):** Official: the dashboard exists. No published limit numbers, and a dashboard bug was reported the week of 2026-11-09, so read it twice.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it. Owner reads the usage screen if the bot can't
- **Sources:** [docs 2026-11-12](https://docs.x.ai/grok-bot/faq)

<a id="ask-first-expensive"></a>
### 14. Auto-review 'ask first' for expensive actions

Custom rules: ask first before opening more than 5 web pages for one task, starting a sub-agent, or re-running a step that already failed twice. Review the 'allow without asking' list. Approvals raised by routines expire after about 30 minutes, so a routine must never wait on one: our packs draft, queue and stop instead.

- **Evidence (shown in source):** Rules UI shown; the docs recommend ask-first rules for risky actions. Saving unmeasured.
- **Risk:** low: a rule too broad can stall chat work
- **Fits GrokBot:** yes
- **Lands as:** owner click or paste. Owner pastes three lines into Auto-review → Custom Rules (text in MASTERY.md)
- **Sources:** [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I); [docs 2026-11-12](https://docs.x.ai/grok-bot/faq)

<a id="pre-quote-paid-jobs"></a>
### 21. Quote the cost before any paid job

A bot that spends credits elsewhere (image/video tools, scrapers) quotes the cost, asks, and logs cost per job. Our packs go further: never spend; draft the plan with its cost into the owner's queue.

- **Evidence (shown in source):** Shown; self-reported job costs of about $3 to $20.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** already in our packs
- **Sources:** [youtube 2026-11-10](https://youtu.be/jy1Tvd76f70)

<a id="brainstorm-in-chat"></a>
### 23. Think in plain Grok chat; run jobs in the bot

Open-ended discussion goes in regular Grok chat; the bot gets a clear brief. Both draw on one pool on the X subscription, so the gain is a shorter bot chat, not a separate allowance.

- **Evidence (claim):** One forum user's experiment, unmeasured.
- **Risk:** low
- **Fits GrokBot:** partial
- **Lands as:** know it, nothing to apply
- **Sources:** [forum 2026-10-18](https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188)

<a id="second-plan"></a>
### 28. A second plan seat with a synced 'fleet brain'

Buy a second seat on a Team plan, share bots to the team, and sync skills, memory and context both ways through a private GitHub repo (push before switching, pull after). Team-shared bots can't reach the original account's vault.

- **Evidence (shown in source):** Shown end to end with a phrase test.
- **Risk:** high: new spend; may breach the terms if used to dodge limits; breaks 'one account per business'; private context in GitHub
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner's decision after the ledger shows the first account still runs out with every other trick applied
- **Sources:** [youtube 2026-11-04](https://youtu.be/Zz3Ixk2Tzpo)


## Scheduling

<a id="routine-frequency"></a>
### 1. Slow routines down; merge small checks

Every routine run wakes the bot and re-reads its context. A 15-minute routine is about 96 runs a day; an hourly one is 168 a week. List each routine's runs per week and how often it found anything. Slow the ones that mostly end silent, fold small checks into one daily and one weekly run, and pause (never delete) routines that produced nothing in 7 days. Keep every pair of routines at least 5 minutes apart. Run non-urgent routines only in working hours in the bot's time zone. When the week's usage is nearly gone: pause all but the lead, then re-enable in tiers (KEEP, then SLOW, then EVENT) with a reading between each.

- **Evidence (xAI docs):** xAI's own guidance (quoted in two videos) is that one hourly routine can use a week of usage in a day. One builder reports 43 of 45 watchdog runs found nothing, and 1,022 weekly wake-ups cut to 219 with no deletions. In our packs the audit found hourly watchdogs in all three and a 30-minute sweep in Find Me Money.
- **Risk:** low: fewer runs; slower reaction for anything time-critical, so pick cadence per job
- **Fits GrokBot:** yes
- **Lands as:** kit applies it. The kit reports; cron changes in a pack go through its PR
- **Sources:** [docs 2026-11-12](https://docs.x.ai/grok-bot/faq); [youtube 2026-11-10](https://www.youtube.com/watch?v=V3ETwJAR5-I); [youtube 2026-11-03](https://www.youtube.com/watch?v=vR5lzCWpp6o); [forum 2026-10-18](https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188); [github 2026-10-18](https://github.com/sit-in/awesome-grokbot-playbooks/blob/main/examples/routine-budget.md); [youtube 2026-11-09](https://youtu.be/WRqZktcjJl8)

<a id="watch-dont-poll"></a>
### 16. Watch pages for changes instead of re-reading them

page_diff.py keeps a snapshot and prints only what changed, or nothing, so the run ends [SILENT] after reading a few lines. The routine still wakes the bot; to stop the wake-ups too, the check must run outside the bot (changedetection.io or a Cloudflare Worker) and call the bot only on a change, which needs a webhook into Grok Bot (seen live, not documented) and an account (see the gated list).

- **Evidence (shown in source):** Seed creator: 43% fewer tokens re-reading a changed page; the outside-the-bot version is arithmetic (720 runs to about 2), not shown.
- **Risk:** low for page_diff.py
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-06](https://youtu.be/ow6x3pdwydA); [github 2026-11-12](https://github.com/dgtlmoon/changedetection.io); [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w)

<a id="outside-doorbell"></a>
### 26. Outside 'doorbell' for page watching (Cloudflare Worker or changedetection.io)

A free worker checks the page on its own schedule and wakes the bot only when it changes, so the routine disappears.

- **Evidence (claim):** Arithmetic only (720 runs a month to about 2); never shown working end to end.
- **Risk:** med: a new account, and a webhook into Grok Bot that is seen live but not documented
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner's Cloudflare sign-in, and one test that a routine webhook wakes the bot
- **Sources:** [youtube 2026-11-01](https://youtu.be/DmFupd7dz3w); [youtube 2026-11-03](https://www.youtube.com/watch?v=o5vpYc6DoZ0); [github 2026-11-12](https://github.com/dgtlmoon/changedetection.io)


## Reliability

<a id="retry-and-shape"></a>
### 15. Retry the call, not the job; check shapes before saving

Wrap flaky calls in retry.py (or tenacity in Python) so a failed download doesn't restart the job; run check_shape.py (or pydantic) on results before they go into a sheet or CRM, and fix only the bad fields.

- **Evidence (measured here):** Shown in the seed video (three tries in 2.2 s; two bad fields caught). Our scripts are tested here.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** kit applies it
- **Sources:** [youtube 2026-11-06](https://youtu.be/ow6x3pdwydA); [github 2026-11-01](https://github.com/jd/tenacity); [github 2026-11-10](https://github.com/pydantic/pydantic)

<a id="decisions-page"></a>
### 22. A decisions page so bots don't idle waiting

One shared Page that shows only what waits on the owner, with approve and done buttons. Bots otherwise sit for days waiting for a click. Our packs use requests/<owner>/ and the morning brief for the same job.

- **Evidence (shown in source):** Shown live.
- **Risk:** low
- **Fits GrokBot:** yes
- **Lands as:** know it, nothing to apply
- **Sources:** [youtube 2026-10-29](https://youtu.be/UClMrBShiYc)

<a id="route-traffic"></a>
### 30. 'Route traffic through this computer' for sites that block the bot

Settings → Computer → Route traffic through this computer, so the bot browses from your own connection.

- **Evidence (claim):** Claim; not shown.
- **Risk:** med: your own IP takes any ban; close to getting around a block, which our gates forbid
- **Fits GrokBot:** partial
- **Lands as:** owner decides (spend, keys, accounts, deletes). Owner's yes per site
- **Sources:** [youtube 2026-11-05](https://youtu.be/akCTUJhZnZE)

## Auto-review lines to paste

Settings → Auto-review → Custom Rules. These apply in chat; our routines never wait on an approval (they draft, queue and stop).

```
Ask first before opening more than 5 web pages for one task.
Ask first before starting a sub-agent or a second bot on a job.
Ask first before re-running a step that has already failed twice.
```

## Rejected

| Idea | Why not |
|---|---|
| Stacking free trials or sharing one subscription between people | Terms risk; the trial is a single-use credit. |
| Turning on Auto top-up or on-demand as the fix | No default cap; only acceptable with a hard monthly limit. |
| Linking a second plan expecting the allowances to add | The FAQ says Grok Bot uses whichever plan grants more; links are permanent. |
| Duplicating a bot to reset it without a handoff note | Duplicates keep settings, skills and routines but not chat or memory (FAQ). |
| Third-party usage meters (grok-bot-usage, QuotAI) | Zero-star, new, unaudited; one signs into your account, the other asks for Keychain 'Always Allow'. The official dashboard already shows per-bot usage. |
| 'Limits halved' or '+25%' claims | User reports only; xAI has published no limit numbers. |
| Paid prompt packs | The tricks are reproducible from public sources; buying is spend, and paid text can't be shipped to clients. |
| Terse-output modes as a main saving | Answers were under 1% of tokens in the only export we have; re-reading is the cost. |

## Gaps in this version

- The paid Skool group (AI Systems Society) was not read: the signed-in browser wasn't reachable. Its items will be added as `source_class: paid`, kept in our own words, and never shipped to clients.
- Reddit and X post bodies could not be fetched; claims from them are search snippets and marked as such in `sources/`.
- No trick here is measured on a Grok account yet. The ledger (trick 11) is how each one gets proven or dropped.
