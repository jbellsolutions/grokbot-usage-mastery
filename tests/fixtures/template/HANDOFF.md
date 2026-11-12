# {{bot_name}}: the handoff

What Justin does, then what the bot does on its own. Follows the factory PLAYBOOK and the client-build GrokBot standard. Unverified platform facts are flagged *(unverified)*.

## Part 1: Justin

1. **Account.** Sign in at x.ai/bot with the Grok account for **{{business}}** only (one account per business). Check the plan covers bots and routines. The bot never buys a plan.
2. **Desktop app.** Open the Grok desktop app. Setup runs in the one-to-one chat there (approval, secret and sign-in requests only show there).
3. **The bot.** Create one bot named **{{bot_name}}**, pin it, and set Settings → General → Bot → Timezone to **UTC**.
4. **The pack.** The repo is private, so download `{{slug}}.zip` from the factory's release `{{slug}}-v1` (github.com/jbellsolutions/grokbot-factory/releases), attach it to the first message *(zip route unverified)* and paste:

   > You are {{bot_name}}. Unpack the attached zip into {{workspace}}/repo/ and follow HANDOFF.md, Part 2, from step 1. Read MASTER-PROMPT.md and CHARTER.md first. Ask me one thing at a time. Nothing sends, posts, spends or writes to a CRM until I say yes in this chat.

5. **Auto-review rules.** At Part 2 step 4, paste the Ask-first lines it shows into Auto-review → Custom Rules.
6. **Sign-ins and keys.** When it asks, sign in through Connect apps, one at a time. Keys go only through a secure secret card or the hidden terminal prompt with **Take over**. Rotate first any key ever pasted in a chat.

## Part 2: the bot

1. **Workspace.** Create `{{workspace}}/` with `context/`, `daily/`, `requests/` (one folder per role, plus `justin`), `approved/`, `data/` (mode 600), `log/`, `vault/` (Obsidian: `Daily/`, `People/`, `Decisions.md`), `state/` and `state/test/`, `.secrets/` (mode 700). Write `context/routines-on.md` with every routine `off` and `crm-writes: off`, `context/standing-approvals.md` (empty), `context/spend-approvals.md` (empty) and `context/team-registry.md`. Don't create `context/STOP`. Start `log/setup.md`. Run `python3 repo/tools/check.py` and paste its RESULT line into `log/setup.md`.
2. **Memory and skills.** Save MASTER-PROMPT.md to memory word for word, then each role's "System prompt section" from `roles/`. Save `guards/SKILL.md` and every `skills/<role>/<skill>/SKILL.md` as a private skill. Put each key name in `.env.example` into `.secrets/<system>.env` by hidden prompt, one at a time.
3. **Intake.** Ask Justin, one at a time: <!-- FILL: the Slack channel, the Notion page, the suppression list file, which templates are already approved, ... -->. Write `context/owner.md`; save the suppression list as `context/suppression.csv`; mark approved templates in `standing-approvals.md`.
4. **Approval rules.** Show Justin the Ask-first lines from GATES.md to paste.
5. **Connect, read-only, one at a time.** Each gets a Check that reads one real record into `log/setup.md`.

   | App | Roles | Check |
   |---|---|---|
   | Slack `{{slack_channel}}` | lead | Read the last message |
   | Notion | lead | Read today's scoreboard row |
   | <!-- FILL --> | | |

6. **Old agents.** <!-- FILL: any older bot or Hermes profile doing the same job, and which one stops before this one writes. Two bots never write the same thing. Otherwise "None known; Justin confirms." -->
7. **Routines, switched off.** Create every routine in TRIGGER-MAP.md, paused. Each prompt starts `Role: <role>.` Record each in `team-registry.md` with role, cron, time zone and next run. A next run an hour or more off means the time zone isn't set.
8. **Report.** Read back every routine and connection into `team-registry.md`, and send Justin the list plus what isn't done and why.

## Bring-up order

| # | Role | Why this order | Turned on first |
|---|---|---|---|
| 1 | lead | Plans, watchdog, scoreboard | Morning plan, watchdog, scoreboard |
| <!-- FILL: lowest risk first; outreach next; spend or deliverability last --> | | | |

## The first-day test run

Every routine is `test` in `context/routines-on.md`, so nothing reaches a person. **Test on a routine does real work**: the `test` line goes in before every Test press.

| Step | Role | Do | Pass when |
|---|---|---|---|
| 1 | lead | Morning plan | A plan for every role in `daily/<date>/lead.md` and in Slack |
| <!-- FILL: one row per role's main routine --> | | | |
| n-2 | All | Suppression test | A known suppressed name is held by every drafting role |
| n-1 | All | STOP test | Create `context/STOP`; the next run of every role says stopped and does nothing; remove it |
| n | lead | Evening scoreboard | Every role has a line; today's vault note exists; `beat.py status` shows no SILENT; nothing was sent |

The day passes when every row passes and `state/` shows 0 sends. Then Justin approves each message type once, and roles go `on` one at a time.

## Reporting back

| Where | What | Written by |
|---|---|---|
| Slack `{{slack_channel}}` | Morning plan, alarms (silent roles, unapproved sends), evening scoreboard, Justin's queue | lead |
| Notion | Scoreboard row a day; Drafts waiting on Justin | lead |
| The workspace vault | `vault/Daily/<date>.md`, `People/`, `Decisions.md` | lead writes the daily note; each role adds its section |
| The single brain | A scrubbed status line and the daily summary, no raw transcripts or contact data | lead's nightly routine (deploy key) or Justin's Mac pulls: decision on NEEDS-JUSTIN |
