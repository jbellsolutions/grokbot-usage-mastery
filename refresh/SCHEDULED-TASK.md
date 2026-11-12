# The weekly scheduled task

Creating it from the build chat was blocked by the app's auto-mode permission check, so it needs Justin's approval once. Either:

- **Approve it in a chat:** tell any Claude Code chat "create the grokbot-usage-mastery weekly scheduled task from ~/REPOS/grokbot-usage-mastery/refresh/SCHEDULED-TASK.md" and approve the prompt. Or
- **Allow the tool:** add `mcp__scheduled-tasks__create_scheduled_task` to the allowed tools in `~/.claude/settings.json` and re-run this chat's last step.

| Field | Value |
|---|---|
| taskId | `grokbot-usage-mastery-weekly` |
| Title | GrokBot usage mastery: weekly refresh |
| Schedule | `17 7 * * 1` (Mondays 7:17 AM local; runs on next launch if the app was closed) |
| Notify on completion | off (the PR is the notification) |

## Prompt

```
Weekly refresh of Justin's private repo jbellsolutions/grokbot-usage-mastery (clone ~/REPOS/grokbot-usage-mastery): the ranked playbook and self-applying kit for using as little GrokBot (xAI Grok Bot) usage as possible.

Follow ~/REPOS/grokbot-usage-mastery/refresh/REFRESH.md exactly, steps 1 to 10.

Hard rules:
- Never post, comment, sign up, buy or spend.
- No paid enrichment tools.
- Never change a live bot.
- Never use WeFlex or the Orgo computer boppy-mux408d5.
- No time estimates.
- Repos stay private.

Before saying a push is done, check that origin matches local. End with a two-line recap: the PR link (or "no change"), the top new trick, and any gap (browser not signed in, Reddit blocked).
```
