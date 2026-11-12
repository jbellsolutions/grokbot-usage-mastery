# Tommy (TMEC Services): ready to push

**Status, 2026-11-12, round 2.** Everything is built and verified. Nothing is pushed or sent, because `tmec-grokbot` is public and is Tommy's install source.

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
