# Project charter: {{bot_name}}

The bot loads this page first. Where a role's charter and this page differ, this page wins.

## Purpose

<!-- FILL: one paragraph. What this bot does for Justin, and what "done well" looks like. -->

## The loop

<!-- FILL: the deterministic loop, step by step (find → check → act → record → report, or whatever fits). Each step's trigger and judgment call is in TRIGGER-MAP.md. -->

## KPIs

| Measure | Target | Source (Justin's words and date) |
|---|---|---|
| Silent roles | None for more than 26 hours | Factory standard |
| Messages sent without an approved template | 0 | Factory standard |
| <!-- FILL --> | | |

## Gates

Every gate in [GATES.md](GATES.md). They never move.

## Handoffs between roles

Through files only: `daily/<date>/<role>.md` for what each role did, `requests/<role>/<id>.md` for work handed over, `requests/justin/` for Justin's queue.

| From | What | To |
|---|---|---|
| Any role | Price, terms, an upset person, an account warning | `requests/justin/` |
| <!-- FILL --> | | |

## Roles

| Role | Job | Routines |
|---|---|---|
| [lead](roles/lead.md) | Plans the day, watchdog, scoreboard, the vault daily note, Justin's queue | 3 |
| <!-- FILL: one row per role. Keep it few. --> | | |

## Workspace

`{{workspace}}/`: `repo/` (this pack), `context/` (owner, routines-on, standing-approvals, team-registry, suppression), `daily/<date>/`, `requests/<role>/` and `requests/justin/`, `approved/`, `data/` (mode 600), `log/runs-<YYYY-MM>.md`, `vault/` (Obsidian: `Daily/`, `People/`, `Decisions.md`), `state/` and `state/test/`, `.secrets/` (mode 700).

## Milestones

| # | Milestone | Done when |
|---|---|---|
| K0 | Account and bot | Justin signed in, the bot has the pack and wrote `log/setup.md` |
| K1 | Read-only | Every app connected read-only, each with one real record read back |
| K2 | Routines | Every routine created and paused, read back into `team-registry.md` |
| K3 | Test day | The first-day run in HANDOFF.md passes with zero sends |
| K4 | Drafts approved | Justin approved each message type once |
| K5 | Low-risk lanes on | <!-- FILL --> |
| K6 | Outreach or writes on | <!-- FILL --> |

## Done means

<!-- FILL: the last milestone reached, and what Justin can see (Slack, Notion, the vault). -->
