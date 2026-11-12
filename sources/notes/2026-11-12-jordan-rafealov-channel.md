# GrokBot usage tricks: Jordan Rafealov channel (11 videos, seeds excluded)

Videos read: UClMrBShiYc (10-29), all9V7SdWyk (10-30), CJugC0nnfIs (10-31), 48LXEHEUiCA (11-02), OrGvdqNDt40 (11-03), akCTUJhZnZE (11-05), AmMFDRLgd7Y (11-08, long), XQc0o5ysSvk (11-08, teaser, nothing usable), R_4BLoZkU1s (11-09), jy1Tvd76f70 (11-10), 2HvNzYlGm5M (11-11, mostly Fable 5.2, little GrokBot).
Not read (seeds): DmFupd7dz3w, Zz3Ixk2Tzpo, ow6x3pdwydA.
Caveat: transcripts are auto-captions; names like "Zernio/Zonio", "Higgsfield/Higsfield", "Composio" are spelled as best understood. His own pitch (AI Systems Society, Dopamine Digital School) is skipped. Nearly every "prompt" he references is gated in his free school group; the text of the prompts is NOT in the transcripts.

## Platform facts
- Plans: Ultra is $200/month (R_4BLoZkU1s 2026-11-09; 48LXEHEUiCA 2026-11-02 "my $200 ultra plan"; AmMFDRLgd7Y 11-08 "Ultra plan"). Premium/Super/Ultra tiers exist (akCT 11-05). A Team plan exists (48LXEH, akCT). Another video says an AI employee costs "$30 a month" (OrGv 11-03), which contradicts the $200 Ultra figure only if read as the base tier; he never names that tier.
- Credit metering: usage is credit-based; he ran out of credits on one account (akCT 11-05, hack 24). ClipBot "uses credits from your GrokBot plan" (CJug 10-31). He says repeatable jobs burn credits if run through AI each time (akCT hack 19).
- Cost claim from him: GrokBot cost more than his Hermes agent on 4 of 5 tests (details below). He says Elon Musk tweeted that serving GrokBot costs are "unsustainably high relative to revenue" (R_4B 11-09, 11.5M views claim). Unverified, relayed secondhand.
- Setup: download from x.ai/bot, "less than five minutes" (AmMFDR 11-08). Desktop app, mobile app, and bots are reachable via X DMs (akCT hack 8).
- Bot marketplace: x.ai/bot/marketplace, hundreds of free importable bots, some from the GrokBot team (akCT 11-05, CJug 10-31). Install = Import Bot, then Add to GrokBot, then Add bot, which may start an onboarding flow.
- Each account has a cloud computer and browser; works 24/7 with laptop closed; syncs across phone, laptop, PC (AmMFDR, akCT hack 7). Machines can be selected (MacBook, Mac mini, iPhone) to run a task on (akCT hack 22).
- Routines: schedule daily/weekly/monthly/hourly; toggled in the details panel under "routines" (akCT hack 9). No limits stated.
- Memory/skills: skills are per-bot; "Import memory" in settings pulls ChatGPT/Claude memory in via a copy-paste prompt (48LXEH 11-02).
- Approval behavior: the platform "learns what you are okay with" and shows fewer approval cards (48LXEH 11-02). AmMFDR 11-08 claims it "never does anything without your permission."
- Vault (settings, ~4th item, "payments"): stores cards, logins, addresses, contacts; Shop Pay, X Money, Link (Stripe) supported; 1Password integration, and he says the bot never sees the passwords (48LXEH 11-02, akCT hack 15/16).
- Bot email: each account/bot gets one email address (e.g. name@mail.grokbot.com style), username chosen once, cannot be changed (48LXEH, akCT hack 17). Phone: bot can place calls, up to 10 per day, up to 85 minutes each, US only, live transcript with takeover (48LXEH 11-02).
- Pages: shareable live dashboards in a Library (pages, media, files) in the right panel, like Claude Artifacts (48LXEH, akCT hack 13).
- Teams: team bots in a shared library, share skills/plugins/secrets/context; sharing permissions per person (akCT hack 21, 48LXEH). Not available on normal plans.
- Image/video: "Imagine" models built in; sub-agents render in background (48LXEH, akCT hack 12). He says not best-in-class.
- Other updates 11-02: shopping cards with buy button, order tracking from email, Cursor cloud-agent custom modes, X Spaces/Lists, docx auto-converted to Google Doc, forwarding bot email to personal inbox, quieter notifications when at desk.
- Gift: Premium/Super/Ultra members can gift two weeks free via a gift icon (bottom-left) link (akCT hack 25).
- Contradictions/oddities: (1) He says GrokBot "never deletes or spends without permission" (AmMFDR) while also showing it auto-ordering a pastry gift into a cart before asking him to pay (OrGv; it stopped at pay, consistent). (2) 10-30 says "7,539 bots" in a directory, 10-31 says "more than 7,000"; same thing. (3) Cost claim in R_4B contradicts his "cheap" framing elsewhere ($3 builds); those are credit/Higgsfield costs on specific jobs.

---

### Chief-of-staff bot as single front door
- category: setup
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 3; also https://youtu.be/AmMFDRLgd7Y (2026-11-08) step 1; https://youtu.be/UClMrBShiYc (2026-10-29)
- what: Create one "Chief of Staff" bot that you talk to. It routes tasks to division-head bots, which delegate to worker bots, then QA, then back up to you only for decisions. In the 11-08 video he builds it by pasting a long onboarding prompt; the bot interviews you (100-day goal, business, tools, rules), then builds worker bots (offer, outreach, sales, delivery), sets safety rules, and gives a daily morning task list needing approval. His six rules: talk to one bot, work goes up, only decisions reach you, files not chatter, four levels with dual hats, one goal per division.
- evidence: Shown on screen (org chart with 54 seats, 3 divisions, 4 levels; named chief "Cooper"). Value claims ("most valuable bot") are opinion.
- risk: low. Cost: more bots means more credits, and delegation chains multiply token use (his own cost tests below).
- grokbot-fit: yes
- seen-in: UClMrBShiYc, CJugC0nnfIs, akCTUJhZnZE, AmMFDRLgd7Y

### Fleet audit prompt (score, keep/merge/bench/delete)
- category: cost-usage
- source: https://youtu.be/UClMrBShiYc (2026-10-29), start of video; https://youtu.be/akCTUJhZnZE (hack 20)
- what: One mega prompt run against GrokBot: it scores every bot 1 to 5 on "one clear job" and "is anyone using it", across seven steps, and outputs keep/merge/bench/delete lists. Then schedule the same audit weekly (or daily per hack 20: a dedicated bot scores each bot out of 10, reports how well it did last week and how many credits it used, flags irrelevant/mergeable/deletable bots).
- evidence: Shown: his fleet went from 79 bots to ~30 (27 keep, 11 merge, 4 bench, 37 delete). Report displayed as tabbed page. Credit-per-bot reporting is claimed in hack 20, not demonstrated.
- risk: med. An auto-delete bot could remove something wanted; keep it report-only and approve deletes manually.
- grokbot-fit: yes
- seen-in: UClMrBShiYc, CJugC0nnfIs (GrokBot Auditor, Dr. Eggbot), akCTUJhZnZE

### Dr. Eggbot from the official marketplace
- category: setup
- source: https://youtu.be/CJugC0nnfIs (2026-10-31) ~end; https://youtu.be/akCTUJhZnZE (2026-11-05) hack 1
- what: Import "Dr. Eggbot" (author Lauren Tan, a GrokBot team member) from x.ai/bot/marketplace. It designs well-formed bots by asking questions, and can audit all bots daily, merge/delete them, or spin up new ones. Install: Import Bot, Add to GrokBot, Add bot, then answer the onboarding questions.
- evidence: Shown the import flow and the large packed context; no output of an audit shown. Recommended by "someone who works on the GrokBot team" (claim).
- risk: med. A bot allowed to delete/create bots autonomously can churn credits and bots; restrict to recommendations.
- grokbot-fit: yes
- seen-in: CJugC0nnfIs, akCTUJhZnZE

### Replace repeated AI work with a Python script
- category: cost-usage
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 19, approx 2/3 through
- what: For any job you repeat (scraping leads, extracting text from PDFs), ask GrokBot once to write a Python script, then tell it to run that script in future instead of re-reasoning the task. The script does the deterministic work; the AI only reads the script output and summarizes. Saves credits.
- evidence: Claim only, no numbers or demo.
- risk: low. Scripts run on the account's computer; review before trusting with credentials.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Second account plus shared GitHub repo to survive running out of credits
- category: cost-usage
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 24
- what: When credits run out, create a second GrokBot account, recreate the bots, and share context through a private GitHub repo (push context from one account, pull in the other). He built a "dual plan bot" that manages the switch and shows tasks across both accounts. Refers to a prior video "never running out of usage again" (not in this set).
- evidence: Shown switching to a second account in the app; no proof of repo sync mechanics.
- risk: high. Likely a ToS problem (multiple accounts to dodge usage limits) and risk of account action; also puts private context in GitHub.
- grokbot-fit: partial (feasible technically; ToS risk, do not recommend)
- seen-in: akCTUJhZnZE

### Claude Code plus GrokBot sharing a private GitHub repo
- category: setup
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 23
- what: Run Claude Code for grunt work (transcription, coding, since he has more Claude credits and it is faster) while GrokBot does agentic tasks. Both push/pull from one private GitHub repo so they never block each other and share context.
- evidence: Claim, no demo.
- risk: low/med. Merge conflicts and secrets in repo; keep repo private, no keys committed.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Import your Claude Code setup into GrokBot
- category: prompts-skills
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 2
- what: Paste a prompt telling GrokBot to search the computer for every Claude skill folder and every CLAUDE.md, read them, save each skill as its own skill, add what the CLAUDE.md says about you and your business to memory, then report what was brought in and left out.
- evidence: Shown running; result not shown in detail.
- risk: med. It reads local files broadly; CLAUDE.md may contain secrets or private info that land in GrokBot memory. Review the "left out" report.
- grokbot-fit: yes (the prompt text is in the transcript, paraphrased above)
- seen-in: akCTUJhZnZE

### Import ChatGPT/Claude memory
- category: memory-context
- source: https://youtu.be/48LXEHEUiCA (2026-11-02) rapid-fire section
- what: Settings, Import memory, copy the provided prompt into ChatGPT or Claude, paste its reply back into GrokBot to seed memory.
- evidence: Mentioned as a feature, not demoed.
- risk: low/med (privacy of exported memory).
- grokbot-fit: yes
- seen-in: 48LXEHEUiCA

### Teach a Task: record screen, get a skill
- category: prompts-skills
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 18
- what: Bottom-left "Teach a task" opens the bot's computer; click record, perform the task, click stop. GrokBot turns the recording into a step-by-step SOP and a reusable skill.
- evidence: Shown opening the flow; output skill not shown.
- risk: low (do not type passwords while recording).
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### "Route traffic through this computer" toggle to avoid blocks
- category: reliability
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 14
- what: If Amazon, Reddit or similar sites block the bot, go to Settings, second menu item "Computer", and enable "Route traffic through this computer" (next to "Execution on this computer"). The bot then browses via your own IP.
- evidence: Claim; he says commenters struggled and this fixes it. Not demoed.
- risk: med. Traffic originates from your home IP (bans, exposes IP); automated shopping sites may flag the account.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Computer panel to watch the bot work
- category: reliability
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 6
- what: Open the right-hand side panel to watch the bot's browser clicks and typing live (his example: Facebook Marketplace search under $500 in Sydney). Useful for catching it stuck or looping before it burns credits.
- evidence: Shown on screen.
- risk: low
- grokbot-fit: yes
- seen-in: akCTUJhZnZE, OrGvdqNDt40

### Vault logins instead of connectors
- category: tools-connectors
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 15, hack 16; https://youtu.be/48LXEHEUiCA
- what: For sites with no API/MCP (Facebook, Skool), store username/password in the vault and the bot logs in and clicks like a person. Cards for shopping go in Settings, vault/payments. 1Password integration is meant to keep passwords from the bot.
- evidence: Shown logging into Facebook Marketplace; his school bot works inside his Skool account this way (shown).
- risk: high. Bot acting as you on real accounts can post, buy, or get banned; keep payments to approval-gated and prefer 1Password integration over raw passwords.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE, 48LXEHEUiCA, CJugC0nnfIs, OrGvdqNDt40

### Composio for connectors GrokBot lacks
- category: tools-connectors
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 10
- what: GrokBot has native connectors (he lists Higgsfield, Vercel, Cloudflare, Apify, GitHub, Stripe, Gmail, Slack, Calendar) under "Connect apps" in the lower-left. For apps without a native connector, add Composio (composio.dev), which bridges thousands of apps without a native MCP.
- evidence: Claim; shows the Connect apps menu.
- risk: med. Another third-party holding OAuth tokens.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE, AmMFDRLgd7Y

### Zernio for multi-platform posting
- category: tools-connectors
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 11; https://youtu.be/CJugC0nnfIs (X bot posts through Zernio)
- what: Install the Zernio plugin from the apps list and connect social accounts (Instagram, X, YouTube, LinkedIn, Facebook, TikTok); then the bot posts across platforms. His X bot drafts replies/posts in his voice, DMs him drafts, and posts on one-button approval.
- evidence: Shown; his X bot template is free (pinned on his X, link not given).
- risk: med. Auto-posting; keep a human approve step.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE, CJugC0nnfIs

### Sections, pins and right-click organization
- category: setup
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 4
- what: Create sidebar sections and pin important bots via right-click (move to section, create section, unpin) or drag into the pinned area.
- evidence: Shown.
- risk: low
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Custom bot icons by color per division
- category: setup
- source: https://youtu.be/akCTUJhZnZE (hack 5) and https://youtu.be/UClMrBShiYc (2026-10-29)
- what: Click the pencil on a bot to pick a built-in icon, type a prompt to generate one, or upload an image. Or ask the bot to make and apply its own icon. His scheme: color-coded background per division, crown for division heads, small job badge. The 10-29 video says he generated them as Python/Pillow pixel art on a 20x20 grid and exported for import.
- evidence: Shown.
- risk: low
- grokbot-fit: yes (cosmetic)
- seen-in: akCTUJhZnZE, UClMrBShiYc

### Routines for scheduled work
- category: scheduling
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 9
- what: Ask the bot in chat to "create a routine every day at 8am that..." (news digest, keyword search). The details panel lists routines with on/off toggles; schedules can be hourly/daily/weekly/monthly. Night Shift v2 relay (marketplace/X) uses three night bots to triage inbox, draft follow-ups and research, with one brief at 7:30am (CJug 10-31).
- evidence: Shown toggle panel; Night Shift described, not shown running.
- risk: med. Unbounded routines are a silent credit drain; audit toggles weekly.
- grokbot-fit: yes
- seen-in: akCTUJhZnZE, CJugC0nnfIs

### Control bots from X DMs and phone action button
- category: setup
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hacks 7 and 8
- what: DM your bot on X to continue a conversation without the app. On iPhone, map the Action button to the GrokBot app to start voice dictation immediately; session continues on the cloud computer.
- evidence: Shown (X DM thread continuing a Marketplace chat).
- risk: low/med (messages ride on X account security).
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Offload heavy tasks to a second machine
- category: setup
- source: https://youtu.be/akCTUJhZnZE (2026-11-05) hack 22
- what: GrokBot lists multiple machines (MacBook Pro, Mac mini, iPhone); tell it to run a render/long job on the Mac mini to keep the main machine light.
- evidence: Shown machine list.
- risk: low
- grokbot-fit: yes
- seen-in: akCTUJhZnZE

### Team bots (shared, permissioned)
- category: setup
- source: https://youtu.be/akCTUJhZnZE (hack 21) and https://youtu.be/48LXEHEUiCA (update 10)
- what: On a Team plan, bots with a building icon are published to the team org. Share control per person; teammates get skills, plugins, context; secrets/files/skills are hidden from non-owners. Shared login vault entries.
- evidence: Shown the share UI. He was moving to Team because he was burning through Ultra.
- risk: med (cost: team plan price not stated).
- grokbot-fit: partial (depends on whether a team plan exists for us)
- seen-in: akCTUJhZnZE, 48LXEHEUiCA

### Hermes head-to-head: GrokBot cost and time data
- category: cost-usage
- source: https://youtu.be/R_4BLoZkU1s (2026-11-09)
- what: Same five jobs on GrokBot (Ultra $200, cloud computer) vs Hermes (Mac mini, Anthropic API, stated as $4/M in and $20/M out). GrokBot cost estimated from tokens in his Cursor dashboard. Results he reports (Hermes vs GrokBot): ad teardown 16 min/$3.51 vs 26 min/>3x cost; homepage redesign 5 min/$1.00 vs 6 min/$2.41; lead hunt plus dossiers: Hermes half the time at ~1/4 cost; dream-100 gift: Hermes half the time and 1/4 cost; funnel spy: Hermes 17 min/$8.90 vs GrokBot 13 min/$4.12 (GrokBot won on cost here). Totals: Hermes 54 min vs GrokBot almost 80 min; GrokBot nearly double the cost; quality 9.6 vs 9 (self-judged by AI). He still keeps GrokBot for ease of use (own computer, phone handoff).
- evidence: Shown on screen as a scoreboard, outputs compared; scoring was AI-judged and tasks were prompted loosely. Treat as one sample.
- risk: n/a. Takeaway: GrokBot is likely pricier per task than a lean API agent; use it where interface/cloud computer matter.
- grokbot-fit: yes (as cost benchmark)
- seen-in: R_4BLoZkU1s

### Rubric-based self-scoring for agent runs
- category: reliability
- source: https://youtu.be/R_4BLoZkU1s (2026-11-09)
- what: Run each agent on identical tasks, no shared research, same start time, and score on three things: output quality, cost, and wall-clock time, with one rubric for both. Count the number of steps and blockers (e.g. Trustpilot blocked, tab crashed) per run.
- evidence: Shown scoreboard.
- risk: low
- grokbot-fit: yes (method)
- seen-in: R_4BLoZkU1s

### Pre-quote credits before spending (Higgsfield Studio bot)
- category: cost-usage
- source: https://youtu.be/jy1Tvd76f70 (2026-11-10)
- what: His Higgsfield Studio bot takes a lead, quotes the credit cost first, asks "do you want to spend the credits?", only then creates the job, and logs the cost per job. Built into the bot prompt as a spend gate.
- evidence: Described and shown the output; per-job costs given: ebook ~$3 (48 pages, 32 sources), creator-partner product ~$6, Airbnb photo pack plus video ~$20 over 100 min, lead bot ~$3 in 35 min, outreach ~$3 in 8 min. Whole six-bot build "$34" in ~3 hours. Costs are credits (Higgsfield + GrokBot), self-reported.
- risk: low. Good pattern for any paid-API bot.
- grokbot-fit: yes
- seen-in: jy1Tvd76f70

### Fact-checked content bot (sources then recheck)
- category: prompts-skills
- source: https://youtu.be/jy1Tvd76f70 (2026-11-10)
- what: Ebook bot prompt design: validate demand (real competing products, Reddit, X, search), write with a source for every fact, then re-check all claims before building the PDF. Result stated as 48 pages, 32 sources, grade-4 reading level.
- evidence: Output PDF shown.
- risk: low
- grokbot-fit: yes
- seen-in: jy1Tvd76f70

### Multi-bot pipeline (lead bot, studio bot, outreach bot)
- category: setup
- source: https://youtu.be/jy1Tvd76f70 (2026-11-10); https://youtu.be/OrGvdqNDt40 (2026-11-03)
- what: Chain separate single-job bots: lead bot finds and scores 20 candidates, keeps the best five, writes a plan; production bot builds assets; outreach bot sends sample and follow-ups. Lead bot scans AppSumo, Product Hunt, G2 via Apify (OrGv). Outreach bot suggests Gmail for under ~20 emails/day; for ~1,000/day buy domains and inboxes, set DNS, warm up in a sequencer such as Instantly.
- evidence: Shown outputs. Cold-email volume advice is from the 11-08 video (125k emails over 100 days needs ~150 inboxes, ~75 domains, ~$584/mo inboxes, ~$1,000/mo total).
- risk: med/high (spam laws, domain reputation).
- grokbot-fit: yes
- seen-in: jy1Tvd76f70, OrGvdqNDt40, AmMFDRLgd7Y

### Approve-gated gift/commerce actions (Dream 100)
- category: security
- source: https://youtu.be/OrGvdqNDt40 (2026-11-03); https://youtu.be/R_4BLoZkU1s (2026-11-09)
- what: A bot researches a prospect, builds a personal gift plan, adds it to a cart (Wolt) and stops at the pay step for human approval. Shopping cards (11-02) show the same pattern: change shipping address or card, then click Pay.
- evidence: Shown the pre-checkout cart. In R_4B he notes both agents misattributed a prospect's company and picked odd gifts, so research quality needs review.
- risk: high (money movement, wrong recipient/address). Keep approval before pay.
- grokbot-fit: yes
- seen-in: OrGvdqNDt40, R_4BLoZkU1s, 48LXEHEUiCA

### Skool/Community bot replacing a VA
- category: tools-connectors
- source: https://youtu.be/CJugC0nnfIs (2026-10-31)
- what: A bot with vault login to his Skool account posts to the free group and uploads classroom files (110 skills, 17 systems, zips) without him logging in.
- evidence: Shown the posts and uploads.
- risk: med (acts as you on a third-party platform).
- grokbot-fit: yes
- seen-in: CJugC0nnfIs, akCTUJhZnZE

### Pages as shareable dashboards (decisions dashboard, org chart, AI office)
- category: tools-connectors
- source: https://youtu.be/UClMrBShiYc (2026-10-29), parts 3 and 4; https://youtu.be/48LXEHEUiCA
- what: One prompt each builds (a) an org chart with every bot, personality, goal progress; (b) an "AI office" view where each bot has a desk, divisions have goal bars, urgent approval tasks and XP; (c) a decisions dashboard that shows only items blocked on you, with approve/done buttons, a log, and a division switcher. Store in Library, Pages and share via link. His reason: bots are often idle waiting for a button click for days.
- evidence: Shown live.
- risk: low
- grokbot-fit: yes (decision dashboard directly addresses idle bots)
- seen-in: UClMrBShiYc, akCTUJhZnZE, 48LXEHEUiCA

### Per-division KPI plus status folder plus morning briefing
- category: prompts-skills
- source: https://youtu.be/UClMrBShiYc (2026-10-29) part 2
- what: The org-structure prompt: list all bots, group into divisions, name by job, give each division one KPI/goal, create a status folder and a dashboard plus a morning briefing. Department heads each push workers toward the one daily KPI.
- evidence: Shown the resulting org (goals like 20,000 subscribers, three launch partners; progress bars).
- risk: low
- grokbot-fit: yes
- seen-in: UClMrBShiYc

### Marketplace picks he rates (useful as install candidates)
- category: tools-connectors
- source: https://youtu.be/CJugC0nnfIs (2026-10-31)
- what: His ranks (opinion): S: school bot (his), Cooper chief of staff, X growth bot (his), Dr. Eggbot. A: Haggle bot (subscription auditor, saved ~$180 on one app), ProtoBot (idea to MVP), GrokBot Auditor, Byte (X complaints to micro-SaaS), Stalk Bot (competitor funnel screenshots weekly), Stitch (daily meme merch Shopify). B: Night Shift v2, Critico (design critique), net worth page, ClipBot, SEO/AEO desk, pitch tools, media strategist, ad spend watch. C/D: family cyber shield, pitch deck coach, morning newspaper, product marketer, inbox guardian, customer proof desk, credit card max, Figma Bro.
- evidence: Mostly shown outputs; rankings are his opinion.
- risk: low/med per bot (check permissions before install).
- grokbot-fit: partial (marketplace bots are installable; quality varies)
- seen-in: CJugC0nnfIs, all9V7SdWyk

### Haggle bot: subscription audit
- category: cost-usage
- source: https://youtu.be/CJugC0nnfIs (2026-10-31)
- what: Bot reviews software subscriptions and seats (found on X thread by "Mahax") and suggests downgrades. He claims ~$180 saved on one app (HubSpot example), covering one month of Ultra.
- evidence: Claim.
- risk: low/med (reads billing info).
- grokbot-fit: yes
- seen-in: CJugC0nnfIs

### Money-bot ideas (roof radar, tax appeal, plan to 3D, mobile rebuild, ads lead finder)
- category: tools-connectors
- source: https://youtu.be/all9V7SdWyk (2026-10-30)
- what: Seven bots from a community directory (credited to someone named Brian). Mostly selling plays. Usable tooling takeaways: ads lead finder reads Meta Ad Library and Google ads (which he says many AIs cannot); Google Earth flyover bot combined with Higgsfield; plan-to-3D bot that spins a 2D floor plan into a spinnable model.
- evidence: Shown examples; revenue claims ($373/day) are pitch.
- risk: low/med
- grokbot-fit: partial
- seen-in: all9V7SdWyk

### Spec-work agent loop (Upwork job to finished sample to human approval)
- category: scheduling
- source: https://youtu.be/2HvNzYlGm5M (2026-11-11)
- what: Daily scan of a job board by keyword, agent builds the deliverable first, drafts proposal, brings it to him for yes/no before sending. Run on Hermes, not GrokBot, in that video. Claimed cost ~$3 and 9 minutes per job.
- evidence: Shown example outputs; not GrokBot. Other content in that video is about Claude "Fable 5.2" model claims and 3D web demos, not GrokBot.
- risk: med (auto-applying to jobs).
- grokbot-fit: partial (pattern transfers; he did it on Hermes)
- seen-in: 2HvNzYlGm5M

### Start from an existing GitHub repo and put it on a test loop
- category: prompts-skills
- source: https://youtu.be/2HvNzYlGm5M (2026-11-11)
- what: Cut cost and time by starting from an open-source repo (for a story-book app, for a 3D site) and pasting a long prompt that makes the model loop: test, QA, improve. Reported ~$5 and ~16 min for a 3D site, ~$6 and 26 min for a playable ad, ~$5 and 12 min for a storybook (Fable 5.2 model, not Grok).
- evidence: Shown outputs; timings and costs self-reported.
- risk: low
- grokbot-fit: partial (technique general; repo names not given)
- seen-in: 2HvNzYlGm5M

### Prompt design: give rules, not scripts
- category: prompts-skills
- source: https://youtu.be/R_4BLoZkU1s (2026-11-09)
- what: In the comparison he gave both agents rules and suggestions rather than exact steps, and let them decide actions. Combined with a fixed rubric this gave comparable runs.
- evidence: Stated.
- risk: low
- grokbot-fit: yes
- seen-in: R_4BLoZkU1s

## Repos and tools named
- x.ai/bot (download), x.ai/bot/marketplace (free bots, Import Bot then Add to GrokBot)
- composio.dev (connector bridge)
- Zernio (social posting plugin; also heard "Zonio")
- Higgsfield (image/video generation connector, credits; Kling 3.0 image-to-video inside it)
- Apify (scraping connector), Instantly (cold email sequencer), ScaleMail (inboxes), HeyReach (LinkedIn), Stripe, Vercel, Cloudflare, GitHub, Gmail, Slack, ClickUp, 1Password, Hermes (his open-source agent, runs on Mac mini), Cursor (cloud agents, used for cost dashboard)
- Named marketplace bots: Dr. Eggbot (Lauren Tan), GrokBot Auditor, Haggle Bot, Night Shift v2 relay, ProtoBot, Critico, ClipBot, Stalk Bot, Byte, Stitch (his), credit card max (Trevin Chow)
- No GitHub repo URLs were given in any of these transcripts. His prompts are in the Dopamine Digital School group (free, gated); no URL stated.
