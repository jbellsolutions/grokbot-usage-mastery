# GrokBot usage mastery

Private. Never public. The ranked playbook and a kit that applies itself, so every GrokBot we build or hand to a client uses as little of its weekly allowance as the job allows.

| Path | What |
|---|---|
| [MASTERY.md](MASTERY.md) | The ranked tricks by area (setup, prompts and skills, memory and context, tools and connectors, cost and usage, scheduling, reliability, security), each with sources, dates, evidence, risk and fit |
| [APPLY.md](APPLY.md) | The entry point to hand to Claude Code or a Grok bot: detect, dry run, show the plan, apply with a backup, verify, report |
| [kit/](kit/) | `bin/apply.py` (the engine), `skill/usage-saver/` (10 scripts, the weekly audit, reset steps, the usage ledger, and `optimizer/` for updates), `prompts/USAGE-RULES.txt` (the rules block every bot keeps in memory) |
| [tricks/tricks.json](tricks/tricks.json) | The source of truth. `bin/render.py` writes MASTERY.md and `sources/INDEX.md` from it |
| [sources/](sources/INDEX.md) | Every source with its date, and our research notes in our own words |
| [refresh/](refresh/REFRESH.md) | The weekly refresh: `bin/scan.py` finds the last 7 days' videos, repos and docs changes; a scheduled task turns them into a PR |
| [applied/](applied/) | Reports and ready-to-run steps for each bot the kit was applied to |
| `kit/bin/make_update.py` | Builds an optimization-only update zip for an installed pack (only what changed since its release); the bot's `usage/optimizer/update.py` applies it |
| `bin/pack` | Builds `dist/grokbot-usage-mastery-v<ver>-{owner,client}.zip`; `--release` attaches them to a release here |
| [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md) | What only Justin can do |

## Use it

On Justin's Mac, for a pack folder:

```bash
python3 kit/bin/apply.py <pack-folder> --owner Justin            # dry run
python3 kit/bin/apply.py <pack-folder> --owner Justin --apply    # apply, verify, report
```

For a live Grok bot: download the zip from the latest release, attach it to a message in the bot's one-to-one desktop chat, and send:

> Unpack the attached zip into your workspace as usage-mastery/ and follow usage-mastery/APPLY.md. Dry run first, show me the plan, and change nothing until I say yes.

Client bots get the `client` zip and `--edition client`.

## Tests

```bash
python3 -m unittest discover tests     # engine on real layouts, the scripts, render freshness
```
