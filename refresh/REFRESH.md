# The weekly refresh

A scheduled Claude Code task on Justin's Mac runs this every Monday. It needs nothing from Justin and spends nothing. It ends with a PR on this private repo, or with "no change".

Why local and not a GitHub Action: YouTube rate-limits datacenter IPs (we hit 429s even from home), Skool and X need the signed-in browser, and search APIs would mean keys and spend.

## Steps for the agent

1. `cd ~/REPOS/grokbot-usage-mastery && git checkout main && git pull --ff-only`.
2. `python3 -I bin/scan.py --days 7`. It writes `refresh/candidates/<date>.md` with new videos (captions saved under `refresh/captions/`, gitignored), new repos, and xAI docs diffs.
3. Read the candidates. For each video with captions, read the text (use `kit/skill/usage-saver/scripts/grep_lines.sh` on the captions folder for "usage|credit|routine|token|limit|skill|memory" first; read only the parts that matter). Skip money pitches.
4. Browser (optional, read only, post nothing): Skool AI Systems Society posts from the last 7 days, r/GrokBot top of the week, X search. If the browser isn't connected or signed in, write that in the PR body and go on.
5. For each new or changed trick, edit `tricks/tricks.json` in our own words:
   - Keep only tricks that are safe and shown to work. New claims enter as `evidence_level: claim`.
   - Every trick needs at least one source with its date, plus risk, fit and `apply.kind`.
   - Anything that spends, needs a key, a sign-in or a new account, deletes, or raises a terms question is `gated`.
   - Skool content: `source_class: paid`, summarized, never quoted.
   - A docs change that contradicts a trick: fix the trick and say so in the changelog.
   - Re-rank only with a reason.
   - Add dropped ideas to `rejected`.
6. If a trick changes what the kit does (the rules block, a script, the audit), change `kit/` and add or adjust a test.
7. Bump `VERSION`: patch for wording or sources, minor for new or re-ranked tricks or kit changes. Add a `CHANGELOG.md` entry: what is new, changed or dropped, with links.
8. `python3 -I bin/render.py && python3 -m unittest discover tests`. Both must pass.
9. Commit on `refresh/<date>`, push, open a PR titled `Weekly refresh <date>: <n> new, <n> changed`. Its body holds the candidates summary, what was skipped and why, and the gaps (browser, Reddit). Don't merge it. If nothing changed: commit only the candidates file and repos state to main with "Weekly scan <date>: no change", and stop.
10. After Justin merges a version bump, `bin/pack` builds the release zip, and re-running APPLY on each bot upgrades it in place.

Never post, comment, sign up, buy, or change a bot from this task.
