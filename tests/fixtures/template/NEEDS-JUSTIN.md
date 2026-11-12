# NEEDS-JUSTIN: {{bot_name}}

Only what Justin can do. Each line: what, the exact click or command, what it unblocks. Ticked off in order when he works the list.

| # | What | The exact step | What it unblocks |
|---|---|---|---|
| 1 | [ ] Grok account for {{business}} | Sign in at x.ai/bot with the account for this business only; check the plan includes bots and routines | Everything |
| 2 | [ ] Create the bot | Grok desktop app: new bot "{{bot_name}}", time zone UTC, attach `{{slug}}.zip` from release `{{slug}}-v1`, paste the message in HANDOFF.md Part 1 step 4 | Setup |
| 3 | [ ] Auto-review rules | Paste the Ask-first lines from GATES.md into Auto-review → Custom Rules | Safe routines |
| 4 | [ ] Sign-ins | Slack, Notion <!-- FILL: every other sign-in --> through Connect apps when the bot asks | Read-only checks |
| 5 | [ ] Keys, by hidden prompt (names only) | `SLACK_BOT_TOKEN`, `NOTION_TOKEN` <!-- FILL: every key in .env.example --> | The tools each role uses |
| 6 | [ ] Suppression list | Give the bot the file when it asks (never in the repo) | Any draft to a person |
| 7 | [ ] Single brain path | "Deploy key" (the bot pushes its daily note) or "Mac pulls" | Reports reach the single brain |
| 8 | [ ] Approve each message type once | Reply yes to each draft type in Notion Drafts; say "auto" for a type once its replies look right | Sends |
