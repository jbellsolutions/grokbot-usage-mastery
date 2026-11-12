# NEEDS-JUSTIN

Only Justin can do these. Each item gives the exact click or command and what it unblocks. Tick them off here as they're done.

1. [ ] **Turn on the weekly refresh.**
   - The build chat's request to create the scheduled task was denied by the app's auto-mode permission check.
   - Do: in any Claude Code chat, say "create the grokbot-usage-mastery weekly scheduled task from ~/REPOS/grokbot-usage-mastery/refresh/SCHEDULED-TASK.md" and approve it.
   - Unblocks: a PR every Monday with new and changed tricks. Costs nothing.
2. [ ] **Let a chat read the Skool group** (AI Systems Society, https://www.skool.com/aisystems).
   - Do one of: connect the Claude in Chrome extension (open the Claude side panel in Chrome and sign in with this app's account), or sign in to skool.com once in the app's built-in browser pane.
   - Also close the stray Chrome tab on skool.com/aisystems/classroom that a read attempt opened.
   - Unblocks: the paid group's tricks. They go into the next version as `source_class: paid`, in our own words, and never ship to clients.
3. [x] **Review and merge factory PR #5** (done 2026-11-12: merged 9ed5492; v2 releases of all three packs) (https://github.com/jbellsolutions/grokbot-factory/pull/5).
   - It adds the kit to the template and the three packs, and moves the watchdogs to every 3 hours.
   - Then run `bin/pack <slug> --release` for revenue-os-max, find-me-money and idea-incubator. Or tell the usage-mastery chat "merge it" and it will.
   - Unblocks: every future bot gets the kit, and the v2 zips carry it.
4. [ ] **Find Me Money's reply sweep.**
   - "Read answers" runs every 30 minutes: 336 wake-ups a week, and it starts under 5 minutes from other routines (Grok wants 5).
   - Decide: keep it, or run it every 2 hours at :20.
   - Unblocks: about 250 fewer wake-ups a week on that account.
5. [ ] **Spend cap, once per Grok account** (AI Guy, Find Me Money, the incubator, and each client's own).
   - Do: grok.com/dashboard/billing → set a monthly additional-usage limit, or turn Auto top-up off.
   - Then paste the three lines under "Auto-review lines to paste" in MASTERY.md into Settings → Auto-review → Custom Rules.
   - Unblocks: no more surprise bills like the seed creator's $550 day.
6. [x] **Tommy (client production, public repo):** (done 2026-11-12: tmec-grokbot 61a8b2a, release v1.0.2; his bots get it on install. Still his: the spending cap and the Auto-review lines) yes or no to `applied/tommy/README.md`.
   - Do: `git am` the patch, push `tmec-grokbot`, cut its release.
   - Unblocks: his 11 bots get the kit at install.
7. [ ] **Jesse and Mike (client production).**
   - The Smart Contracting chat has the step for its pack.
   - Once their bot is live: yes or no to sending it the client zip (`applied/jesse/README.md`).
8. [ ] **The first measurement, on each account.**
   - Do: take the Settings → Usage reading (% used and reset date) before the kit goes live and again a week later, into `log/usage-ledger.md`.
   - Optional: export the usage CSV into the bot's `data/usage/` so `usage_csv.py` can break it down.
   - Unblocks: proof of which tricks actually save.
9. [ ] **Held for your word.** Each one needs spend, a key, an account or a terms call:
   - a second plan seat with a synced "fleet brain";
   - a Gemini free-tier key for reading long media (public material only);
   - a Cloudflare doorbell;
   - Apify actors;
   - a coding CLI on the bot's computer;
   - "route traffic through this computer".

   Risks for each are in MASTERY.md.
