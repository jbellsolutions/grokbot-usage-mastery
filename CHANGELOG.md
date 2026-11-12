# Changelog

## 1.1.0 (2026-11-12)

- **Optimizer.** `usage/optimizer/` (SKILL.md, update.py) ships with the kit to every pack. It applies optimization updates by itself: only what changed, with a backup, plus a few chat steps. It never sends, spends, deletes, or changes a gate, approval, schedule or charter.
- **`kit/bin/make_update.py`.** Builds a pack's update zip from its git history. Usage changes, docs and new bots go in. Anything else is left out and named for the owner.
- **`apply.py`.** New `--workspace` and `--update-url` options write the optimizer's config. The handoff gains an optimizer step.
- **First use: Tommy (TMEC).** `tmec-grokbot-update.zip` on the public latest release, plus an Optimizer bot that is created only on Tommy's yes.
- **Tests.** 13, including the update path end to end.

## 1.0.0 (2026-11-12)

First version.
- **Research.** The three seed videos and the seed creator's 11 other videos from the last 14 days. Six other creators' videos from the same window. xAI's Grok Bot FAQ and plans page. GitHub.
- **Frames.** Contact sheets of seed 3 (the before/after token table) and seed 1 (the reset steps, the usage bots) were checked against the transcripts.
- **Research gaps.** Reddit and X post bodies could not be fetched (WebFetch, curl, firecrawl, and the built-in browser, which refuses reddit.com); claims from them come from search snippets. The paid Skool group was not read because the signed-in browser wasn't reachable.
- **Playbook.** 32 ranked tricks, each with sources, evidence level, risk, fit and how it lands. 9 rejected ideas.
- **Kit.**
  - `APPLY.md` and `kit/bin/apply.py`: detect, dry run, back up, apply, verify, report, restore. Works on Factory packs, multi-bot client packs, live workspaces and anything else.
  - The usage-saver skill: 10 scripts with stdlib fallbacks, measured locally, including `usage_csv.py` for the dashboard export.
  - The weekly audit, the reset steps and the usage ledger.
- **Weekly refresh.** `bin/scan.py` and `refresh/REFRESH.md`, run by a local scheduled task.
