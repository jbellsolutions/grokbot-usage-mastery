# Tommy (TMEC Services): pushed and released

**Status, 2026-11-12: pushed and released on Justin's word ("Push and release").** `tmec-grokbot` `main` is at 61a8b2a, and release [v1.0.2](https://github.com/jbellsolutions/tmec-grokbot/releases/tag/v1.0.2) is the latest. A signed-out download of `releases/latest/download/tmec-grokbot.zip` returns 200, and the zip has `usage/` and `policies/USAGE.md` inside. Nothing was sent to Tommy. The local branch below was merged and deleted.

- **Local branch** `usage/kit-v1` in `Client Builds/Tommy/tmec-grokbot`, commit `61a8b2a`, on top of `main` `9f6af7f`. The repo is left on `main`.
- **Attachable zip:** `Client Builds/Tommy/deliver/tmec-grokbot-usage-v1.zip` (a `git archive` of 61a8b2a, the same form as the release zip).
- **Patch copy:** [`tmec-grokbot-usage-v1.0.0.patch`](tmec-grokbot-usage-v1.0.0.patch).
- **Checks:** `cb verify --platform grokbot --owner Tommy`: ok, no errors. Kit verify: rules, skill and handoff all PASS ([report.md](report.md)).

## What Tommy's bots get

1. **Usage rules in every bot's memory.** TMEC Command saves them at START-HERE Step 2, and every other bot saves them from its Step 6 setup message (`policies/USAGE.md`).
2. **`usage/`**, the usage-saver scripts, plus the weekly audit inside TMEC Command's Monday evening brief (no new routine), the reset steps and the usage ledger.
3. **Read-less lines in 14 skills**, where the reading happens:

   | Skills | What changes |
   |---|---|
   | partner-score, segment-list-build, trades-list-build, seo-audit, radar-sweep | Pages go through `clean_page.py`; a radar thread is opened only when the snippet can't decide |
   | rebate-watch, vendor-review | `page_diff.py` first: an unchanged government or vendor page costs a few lines, and only the changes reach Tommy |
   | crm-sweep, reactivation-batch, quiet-quote-followup, newsletter-issue | HubSpot replies cut with `pick.py`; due rows picked with `sheet_q.py` |
   | cold-email-wave, scoreboard | Rows, checks and numbers answered with `sheet_q.py` and `grep_lines.sh` |
   | content-week | Work from the shoot sheet; never open a whole video |
4. **Owner steps for Tommy:** a spending cap at grok.com/dashboard/billing (Auto top-up off, or a monthly limit), and the three Auto-review lines.

His schedule was already lean, so nothing changed there: 18 routines, about 55 runs a week, none more often than every 3 hours.

## Push it (Justin's yes)

**Route A: through the public repo.** Tommy's one-paste install downloads the latest release, so this is the route that reaches his bots by itself.

```bash
cd "/Users/home/AI OS Market Share /AIOS/Client Builds/Tommy/tmec-grokbot"
git checkout main && git merge --ff-only usage/kit-v1 && git push origin main
git archive --format=zip -o ../deliver/tmec-grokbot.zip HEAD
gh release create v1.0.2 ../deliver/tmec-grokbot.zip -R jbellsolutions/tmec-grokbot --title "TMEC Grok Bot team v1.0.2" --notes "Usage kit: read-less scripts, usage rules, weekly audit"
```

**Route B: attach without publishing.** In TMEC Command's one-to-one chat, attach `deliver/tmec-grokbot-usage-v1.zip` and send:

> Unpack the attached zip over /workspace/tmec-team/repo (keep context/, data/ and log/), then follow the "Usage kit" section of START-HERE.md and the usage-mastery steps: save the rules in policies/USAGE.md to your memory word for word, run the install, start the usage ledger, and have every other bot save the same rules. Show me the plan first and change nothing until I say yes.

If the team isn't installed yet, the normal install from the new release (Route A), or the attached zip, includes all of it.

## Update-only path and Optimizer (1.0.3): released

Justin, 2026-11-12: "update his GrokBot to have a separate one just to update optimization." Published on his word "Publish v1.0.3".

- **`tmec-grokbot` `main` 825438d, pushed** (origin matches local). Release https://github.com/jbellsolutions/tmec-grokbot/releases/tag/v1.0.3 holds `tmec-grokbot.zip` (full install) and `tmec-grokbot-update.zip` (update only, 40 files, nothing left out). What it adds:
  - `agents/12-optimizer.md` and `routines/optimizer-check.prompt` (Optimizer bot, created only on Tommy's yes; routine paused);
  - `usage/optimizer/`;
  - the manifest entry;
  - `PACK-VERSION` 1.0.3.

  `cb verify`: ok, no errors.
- **Signed-out check:** both `releases/latest/download/` links return 200, and their sha256 hashes match the local zips. The update's version is 1.0.3.
- **The downloaded update, run on a v1.0.1 install:** the first run changed 39 files (with a backup), the second run changed none, and the result matches the v1.0.3 tag exactly (`diff -rq` clean).
- **The line to paste into TMEC Command,** paste it once (nothing was sent to Tommy):

> Download https://github.com/jbellsolutions/tmec-grokbot/releases/latest/download/tmec-grokbot-update.zip, unzip it into /workspace/tmec-team/updates/1.0.3/ and follow UPDATE.md inside it. This is an optimization-only update from Justin's team: no approvals, sends or schedules change.
