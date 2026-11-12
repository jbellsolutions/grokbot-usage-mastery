# Grok Bot usage tricks: web research (2026-11-12)

Read-only research. Nothing posted, signed up for or spent. Reddit threads could not be fetched (WebFetch, curl, firecrawl all blocked); Reddit content below is search-snippet level only and marked as such. X post bodies mostly came via video/transcript quotes; x.com direct fetch returned 402.

## Platform facts (official or multiply confirmed)
- Plans (x.ai/bot, 2026-11-12): Premium $30/mo (Bot computer, routines on a schedule, desktop/iOS/Slack/Teams, weekly Grok Bot usage); Super $100 (3.5x Premium usage, peak-time priority); Ultra $200 (12x Premium usage). Enterprise/Teams included. Subscriptions include weekly usage; extra usage is billed by token cost. Source: https://x.ai/bot [docs]
- Usage is one weekly pool shared with the Grok apps (X Subscription) or with Cursor (legacy Cursor plans). Prepaid credit covers usage past the pool. Check under Usage at grok.com/dashboard. Source: https://docs.x.ai/grok-bot/faq [docs]
- When the weekly limit runs out: extra usage continues only if on-demand / Auto top-up is on; otherwise the bot stops until weekly reset. Source: docs FAQ.
- Spending caps: leave Auto Top-up off or set a monthly additional usage limit at grok.com/dashboard/billing (Cursor plans: on-demand monthly limit in Settings, Usage & Billing). A running task can exceed the cap a little. Source: docs FAQ; also stated in 3 videos.
- No model picker. Grok Bot chooses a model per task and may switch between requests; underlying model is not shown; picking a model elsewhere does not change per-token cost. Source: docs FAQ.
- Memory: per Bot (preferences, role, summaries of prior work); name and time zone are shared across all Bots; shared files, browser sessions, group messages and handoffs carry context between Bots. Ask a Bot "What do you remember about me?" to inspect. Deleting a Bot removes profile, conversation and routines. Source: docs FAQ.
- Computer: one persistent cloud computer per user shared by all their Bots (files, browser sessions, logins); NOT a security boundary between Bots. Each Bot gets its own screen and runs one computer-use task at a time. (x.ai/bot marketing says "every Bot has its own computer"; the docs FAQ says one shared per user. Docs win.) Source: docs FAQ.
- Routines: 50 per Bot, 20 run records kept per routine (third-party summary of docs, https://flaviocopes.com/grok-bot/); xAI docs say an hourly routine can use a week of usage in one day (quoted in the Charbel/Sharbel A. video 2026-11-03). Docs page skills-routines-and-automations.md returned 404 to me, so those numbers are second-hand.
- Security: credentials via Vault / password manager / Secure Form without Bot seeing values; approvals from routines or inter-Bot messages expire after about 30 minutes; docs recommend narrow "Ask first" Auto-review rules for send, publish, delete, purchase, production changes; shared templates expose config, so strip secrets first. Source: docs FAQ.
- Free trial: usage credit with 7-day window, consumed by steps and tokens, not restored; one big task can eat all of it. Source: docs FAQ.
- News window (multiply confirmed by 4+ videos, dates 2026-11-03 to 11-10): around 2026-11-01 Elon Musk said the cost of serving Grok Bot was "unsustainably high relative to revenue"; users reported weekly usage jumping to 100% in days; xAI said token-efficiency fixes were underway; on 2026-11-09/10 xAI reset weekly limits for all users (rare). A status-page issue with the usage dashboard was also reported the same morning, so part of the spike may have been a meter bug. Limits have not been published as numbers. Sources: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10), https://www.youtube.com/watch?v=gyWlFxLIl08 (2026-11-09), https://www.youtube.com/watch?v=6NIQpRr6nkQ (2026-11-06).
- Where usage actually goes (one builder's export, ~60 bots, 4.6B tokens in 7 days): about 93% of tokens were rereading chat history; answers under 1%. A fresh chat starts near 16k tokens; old bots read 200k-380k before doing anything. Reread tokens weigh less against the limit than fresh ones, so rereading was nearer 3/4 weighted. Single-source claim. Source: https://www.youtube.com/watch?v=o5vpYc6DoZ0 (2026-11-03).

## Tricks

### Run a usage audit prompt before changing anything
- category: cost-usage
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03) [platform: youtube]
- what: Paste a prompt telling the bot to list every bot and routine, estimate which use the most, say why, and propose the 5 changes that would save most, without changing anything. Cross-check against the per-bot breakdown on the usage dashboard.
- evidence: shown (creator ran it; top consumer was a monitor bot at 25%); V3ETwJAR5-I shows the dashboard per-bot breakdown too. The bot's estimate is a guess, dashboard is the real number.
- risk: low (read-only prompt)
- grokbot-fit: yes

### Cut routine frequency; merge to one daily and one weekly check
- category: scheduling
- source: https://x.com/poteto/status/2091368467060662497 (2026-11, from search snippet) [platform: x]; also https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188 (2026-10-18) [platform: forum]; videos 2026-11-03/10
- what: A 15-minute routine is about 96-100 runs a day, each a full reread. Move to hourly or a few times a day; fold several small checks into one daily plus one weekly routine. Ask the bot to list each routine, its frequency, and how often it found something new, then slow or merge the ones that mostly find nothing.
- evidence: many independent reports (xAI-aligned post, 4 videos, forum, docs' hourly-uses-a-week line). Numbers shown: 43 of 45 watchdogs found nothing; wake-ups 1,022/week to 219 with no deletions (one builder, claim).
- risk: low (reduces runs; pause rather than delete)
- grokbot-fit: yes

### Pause, do not delete, routines that produced nothing in 7 days
- category: scheduling
- source: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10) [platform: youtube]
- what: Prompt: list routines that produced nothing useful in 7 days with their last 3 runs, then pause only the ones I mark; do not delete. Also pause routines for things that are down (e.g. site offline).
- evidence: shown on screen, creator paused several. Savings number not given.
- risk: low
- grokbot-fit: yes

### Give routines their own bot
- category: scheduling
- source: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10) [platform: youtube], attributed to an X article by "Maestro"
- what: Every scheduled run lands in the owner bot's chat. If your day-to-day chat bot owns the routines, each wake-up rereads that long chat. Create a separate "routines" bot and move recurring jobs there; keep the main bot for live work.
- evidence: claim from article, creator started doing it (result not shown). Logic is consistent with the docs (history reread each turn).
- risk: low/med (moving routines can break references; check each after)
- grokbot-fit: yes

### One task per chat; start fresh with a handoff note
- category: memory-context
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03), https://www.youtube.com/watch?v=o5vpYc6DoZ0 (2026-11-03), https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10) [platform: youtube]
- what: Press + for a new chat per task (old chats cost nothing sitting idle). For a heavy long-lived bot, ask it to write a ~600-word handoff note (role, rules, open tasks, finished work), then either start a new chat or duplicate the bot and paste the note. Duplicating keeps settings, skills and routines but NOT chat or memory, so the note is required. Stop the old bot's routines before relying on the copy so nothing runs twice.
- evidence: mechanism is docs-consistent; the 93%-reread export is one source. Fresh vs old chat sizes (16k vs 200-380k) are claim. Duplicate behaviour is shown on screen in one video.
- risk: low/med (lose context if note is thin; verify the new bot before deleting the old)
- grokbot-fit: yes

### Batch small requests into one message
- category: prompts-skills
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03) [platform: youtube]
- what: Standing rule for each bot: if I send a few short requests in a row, wait and ask if there is more, then do all at once; do not reply to "thanks" or "ok". Each turn rereads the chat.
- evidence: logic consistent with docs; no measured saving shown. Claim.
- risk: low (slight delay)
- grokbot-fit: yes

### Prefer connectors over browser/computer use
- category: tools-connectors
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03); https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188 (2026-10-18) [platform: youtube, forum]
- what: Browser use is screenshot, click, check, repeated, each step metered. Where a Connect app exists (Gmail, Slack, Calendar), use it. Prompt: find every job where the bot uses the browser for an app with a connector, tell me which to switch.
- evidence: two independent sources, mechanism plausible; no number given. Claim.
- risk: low
- grokbot-fit: yes

### Remove unused plugins/app tools
- category: tools-connectors
- source: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10) [platform: youtube]
- what: Open plugins in the desktop app, uninstall ones erroring or unused so they do not load into each turn.
- evidence: shown being done; effect not measured. Claim that it helps.
- risk: low
- grokbot-fit: partial (mirrors "turn off app tools the bot does not need" in the Maestro list)

### Audit and shrink the bot roster
- category: cost-usage
- source: https://www.youtube.com/watch?v=V7dsUn8xh6Y (2026-11-03) [platform: youtube]
- what: The chief-of-staff style bot checks the roster (who the other bots are and what they do) on each prompt, so more bots means more tokens per prompt. Prompt: audit which bots I use most and least, recommend deletions and a smaller setup. Creator had 30 bots and used 6.
- evidence: audit run shown; token saving per prompt is the creator's reasoning, not measured. Claim.
- risk: med (deleting a bot removes its routines and chat; use hide, which keeps work, or export handoff first)
- grokbot-fit: yes

### Turn recurring AI jobs into scripts saved as skills
- category: prompts-skills
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03) [platform: youtube]
- what: After a weekly job (pull numbers into a sheet, sort files) is verified correct, ask the bot to turn it into a script, save it as a skill, and run the script next time, flagging only anomalies.
- evidence: described, not demonstrated with numbers. Sound in principle. Creator warns do it only after the job is right.
- risk: low/med (a buggy job gets frozen into a script; test on sample input first)
- grokbot-fit: yes

### Offload "is the page changed?" watching to a free Cloudflare Worker
- category: scheduling
- source: https://www.youtube.com/watch?v=o5vpYc6DoZ0 (2026-11-03) [platform: youtube]
- what: Instead of an hourly bot routine (about 720 runs a month, nearly all empty), the bot builds a small no-AI Cloudflare Worker once that checks the page hourly and wakes the bot only on change.
- evidence: claim with arithmetic (720 runs to about 2); not demonstrated working here. The same video is a promo for a paid community.
- risk: med (needs a Cloudflare account and a webhook into Grok Bot; do not paste keys into chat; test before connecting)
- grokbot-fit: partial (needs a bot-wake webhook/trigger path to be confirmed)

### Send text, not screenshots or long PDFs
- category: memory-context
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03) [platform: youtube]
- what: Copy the needed line instead of a full-screen screenshot; crop screenshots; convert long PDFs to text first. Images cost more to read than text.
- evidence: claim, widely accepted generally for LLMs; not metered in Grok Bot in the source.
- risk: low
- grokbot-fit: yes

### Add Auto-review "ask first" rules for expensive actions
- category: cost-usage
- source: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10), docs FAQ [platform: youtube, docs]
- what: Custom rule (always ask): before opening more than 5 web pages for a task, starting a sub-agent, rerunning a step that already failed twice, or starting any job expected to take over 5 minutes. Review the "allow without asking" list and turn off unneeded ones. Docs separately recommend ask-first for send, publish, delete, purchase, production changes. Note approvals from routines expire in about 30 minutes, so an ask-first rule in a routine can stall it.
- evidence: rules UI shown in video; docs recommend the safety rules. Saving unmeasured.
- risk: low
- grokbot-fit: yes

### Cap spending: no Auto top-up, or a hard monthly additional-usage limit
- category: cost-usage
- source: https://docs.x.ai/grok-bot/faq (fetched 2026-11-12); https://www.youtube.com/watch?v=6NIQpRr6nkQ (2026-11-06) [platform: docs, youtube]
- what: In grok.com/dashboard/billing set a monthly additional usage limit (there is no default cap per one creator) or leave Auto top-up off. Docs warn a running task can overshoot slightly. Per Cursor-plan users, turn on-demand off.
- evidence: official doc; 3 videos agree.
- risk: low (bot stops at limit instead of billing)
- grokbot-fit: yes

### Check the meter before big jobs; scope tasks tightly with a stop condition
- category: cost-usage
- source: https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10); docs FAQ (trial and "start small" guidance) [platform: youtube, docs]
- what: Look at Usage before long runs. Brief tasks with a goal, a limit (pages, steps, minutes) and a stop condition. Reddit snippet (r/GrokBot 1xembjd, 2026-11, not fully read) also suggests rules like "test on a real sample and show output before done" and "estimate weekly cost before scheduling a routine".
- evidence: docs say start small then scale; the rest claim.
- risk: low
- grokbot-fit: yes

### Keep shared rules in one file that bots read only when needed
- category: memory-context
- source: https://www.reddit.com/r/GrokBot/comments/1xembjd/running_about_20_grok_bots_as_a_team_and_burning/ (2026-11, snippet only) [platform: reddit]
- what: For a ~20-bot team, move rule-based jobs off the bots; keep shared rules in one place and have each bot read them only when doing the job, not on every turn.
- evidence: single snippet, thread not read in full. Claim.
- risk: low
- grokbot-fit: partial (verify in thread)

### Guard multi-bot teams against runaway discussions
- category: reliability
- source: Facebook group snippet (via search, 2026-11) https://www.facebook.com/groups/1025166646935100/posts/1132630826188681/ [platform: other]
- what: One user burned all usage overnight when a team bot erred and bots discussed it all night. Mitigate: ask-first rule for starting sub-agents, a stop condition on inter-bot loops, spending cap, and routines pause-after-no-reply (Grok Bot may ask whether to keep routines running after a long absence).
- evidence: single anecdote; mitigations are logical.
- risk: low
- grokbot-fit: yes

### Hand heavy coding to a coding CLI on the Bot's computer
- category: tools-connectors
- source: https://www.youtube.com/watch?v=V7dsUn8xh6Y (2026-11-03), https://www.youtube.com/watch?v=V3ETwJAR5-I (2026-11-10) [platform: youtube]
- what: Install Claude Code CLI or Codex CLI on the Bot's computer, authenticate with a subscription token, and tell the bot to use it for coding. Moves coding spend off the Grok pool onto a separate plan. V3ETwJAR5-I also suggests a Cursor cloud agent route for the coordinator pattern.
- evidence: install shown; savings and better output are creator claims. Both creators are Claude Code/Cursor users.
- risk: med/high (puts a subscription token on the shared cloud computer, which is not a boundary between Bots; use the secure Vault/Secure Form path, never paste in chat; token lives for all bots)
- grokbot-fit: partial (acceptable only with the token scoping caveat)

### Weekly "usage guard" bot
- category: cost-usage
- source: https://www.youtube.com/watch?v=vR5lzCWpp6o (2026-11-03) [platform: youtube]
- what: One bot with a single Monday routine that reports which bots and routines used most, which found nothing, which chats got long, and any browser use that has a connector; one fix each; never deletes or touches other bots without asking. Template link is in the creator's description (not fetched).
- evidence: first report shown. Value not quantified. Note this routine itself costs usage; weekly cadence is fine.
- risk: low if template reviewed before install (shared templates can contain instructions)
- grokbot-fit: yes

### Keep open-ended brainstorming in regular Grok chat
- category: cost-usage
- source: https://forum.cursor.com/t/best-practices-for-using-grok-bot-more-token-efficiently/175188 (2026-10-18) [platform: forum]
- what: Use normal Grok chat for discussion and decisions; use Grok Bot only for clear executable tasks and routines. Note the chats share one pool on the X Subscription, so the gain is shorter bot context, not a separate allowance.
- evidence: one forum user's experiment, unmeasured. Claim.
- risk: low
- grokbot-fit: partial

### Link a SuperGrok account if on a Cursor plan (take the larger allowance)
- category: setup
- source: https://docs.x.ai/grok-bot/faq (2026-11-12) [platform: docs]
- what: Cursor plan and linked SuperGrok do not add; Grok Bot uses whichever grants more weekly usage. "Get Access with Grok" shows only when it would raise your usage. Links are permanent (support needed to unlink). Allow up to 24h after a SuperGrok upgrade.
- evidence: official doc.
- risk: low/med (permanent link)
- grokbot-fit: partial (only if account is on the legacy Cursor path)

### Track usage with a local dashboard or menu-bar meter
- category: cost-usage
- source: https://github.com/Amine-cnslt/grok-bot-usage (pushed 2026-10-04, MIT, 0 stars); https://github.com/marotron/QuotAI (pushed 2026-11-12, MIT, 0 stars) [platform: github]
- what: grok-bot-usage runs a local Python server on 127.0.0.1:8765 and signs into your Cursor account to show per-bot usage (README says session stays on the computer, deleted on sign-out). QuotAI is a macOS menu-bar app showing Cursor/Grok Bot quota rings; ships an unsigned/ad-hoc .dmg and asks for Keychain access.
- evidence: README claims only; I did not run or audit code. Both are tiny, new, unknown authors.
- risk: med (grok-bot-usage requires a login session; QuotAI binary asks for Keychain "Always Allow")
- grokbot-fit: partial (the official dashboard at grok.com/dashboard already gives per-bot breakdown; prefer that)

## GitHub repos checked
| repo | stars | last push | license | note |
|---|---|---|---|---|
| megahertz8/grok-bot-packs | 0 | 2026-11-12 | none | skill packs; README says pin to tagged raw URL and verify sha256 before install; two tags flagged do-not-use. Safe pattern, but a skill bootstrap that fetches remote files, so review before install. |
| owenservera/grokbot-telemetry | 1 | 2026-11-12 | none | mirror of an agent box's tool/process logs; secrets claimed redacted; pushes via gh/MCP. Not a saver. Do not copy its collectors. |
| Amine-cnslt/grok-bot-usage | 0 | 2026-10-04 | MIT | see above |
| marotron/QuotAI | 0 | 2026-11-12 | MIT | see above |
| bostonaholic/grokbot-skills, asktolik/grokbot-skills-Public (10), d-gangz/grokbot-skills, others | 0-10 | recent | unchecked | generic SKILL.md collections; not read in detail |
| milind-soni/OpenMausBot (21.6k), elie222/rakazo (8.1k), rome-os/rome (898), nuphos/nuphos (492), alexsergivan/kwant (530), vstorm-co/agenticos (260) | as shown | 2026-11-12 | mixed | open-source alternatives to Grok Bot, not tricks for it; star counts of fresh repos are unverified and may be inflated. Not evaluated. |
No repo found specifically for context compression, caveman-style terse output, or prompt compression aimed at Grok Bot. The "terse output" idea has no Grok Bot-specific evidence; answers are under 1% of tokens per the one export, so it would save little.

## Rejected
- Sharing one account/subscription across people or stacking free trials: ToS risk, and free trial is single-use credit with Cancel Trial being irreversible. Not researched further.
- Linking a second plan expecting usage to add: docs say it does not add.
- Turning on on-demand / Auto top-up as a "fix": creators and docs say it has no default cap; only OK with a hard monthly limit.
- "Duplicate bot to reset memory" without a handoff note: loses memory (docs-confirmed).
- Claims that xAI "cut limits by half" or "added 25%": user reports only, no official numbers.
- Paid community templates/prompt packs (AI Profit Boardroom, Skool): promo, prompts are reproducible free from the videos.
- QuotAI Keychain "Always Allow" binary and any bot-session-token tools: security risk for little gain.
- Reddit post bodies (1x7sov2, 1xact0a, 1w7c6kg, 1xs28kd) and X post 2119954776674996374: could not be read; no claims taken from them beyond search snippets.

## Sources searched
- WebSearch "xAI Grok Bot x.ai/bot docs routines skills memory credits usage limits": flaviocopes.com, aibuilderclub, eesel.ai, docs.x.ai FAQ, smartscope, vpsranking.
- WebFetch x.ai/bot (plans); docs.x.ai/grok-bot/faq (usage, models, memory, computer, security); docs skills-routines-and-automations.md = 404; x.com/poteto = 402; reddit/old.reddit = blocked.
- gh search repos "grok bot", "grokbot skills", "grok bot token usage" plus READMEs of grok-bot-packs, grokbot-telemetry, QuotAI, grok-bot-usage.
- firecrawl search: "Grok Bot credits usage tips", "Grok Bot usage tips reduce token bill x.com", "Maestro 12 ways reduce GrokBot token bill", "reddit r/GrokBot credits burning routines tips", "xAI Grok Bot token efficiency fixes reset weekly limits", "r/GrokBot tips improving usage...". Returned Reddit titles/snippets, Cursor forum, a Facebook group, LinkedIn (scrape failed), x.ai/bot/guides/grok-bot-101 (not read in full).
- yt-dlp ytsearch12 for "grok bot credits usage", "grok bot skills routines", "grok bot setup tips". Captions saved (en-orig, 429s on en track) to /private/tmp/claude-501/-Users-home-Master-Claude-Session--claude-worktrees-grokbot-usage-mastery-c61ede/83fdb4f8-048a-499a-8ade-ed26b4113673/scratchpad/web-dl/: V3ETwJAR5-I (AI Automation Station, 11-10), vR5lzCWpp6o (Sharbel A., 11-03), o5vpYc6DoZ0 (Julian Goldie, 11-03), V7dsUn8xh6Y (Alex Finn, 11-03), gyWlFxLIl08 (Joel Blackman, 11-09), 6NIQpRr6nkQ (Brock Mesarich, 11-06). Not pulled: 4gH4WbXGOqY ("So You Keep Hitting GrokBot Limits", routine math 96 runs/day), IsUpatC9obI (full course), wXChVdv8Z9A (09-16, too old), DmFupd7dz3w/Zz3Ixk2Tzpo (Jordan Rafealov, excluded).
