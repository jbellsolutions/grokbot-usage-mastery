# Trigger map

The loop is deterministic: schedules and webhooks start every step, and the agent makes only the judgment call inside it. Gates stay on until replies prove good. Every cron is UTC. **50 routines max per bot**; `tools/check.py` counts the cron rows below.

## The loop, step by step

| # | Step | Started by | Role | Judgment call | Human gate |
|---|---|---|---|---|---|
| 1 | Plan the day | Schedule `30 13 * * *` | lead | What matters today | None |
| <!-- FILL --> | | | | | |
| n | Report | Schedule `30 23 * * *` | lead | Proof check on each number | None |

## Every schedule and event, by role

### lead

| Kind | When or what | Does |
|---|---|---|
| Schedule | `30 13 * * *` | Morning plan |
| Schedule | `0 * * * *` | Watchdog |
| Schedule | `30 23 * * *` | Evening scoreboard and vault daily note |

<!-- FILL: one section per role: "### <role>", then its table. Schedule rows count toward 50. -->
