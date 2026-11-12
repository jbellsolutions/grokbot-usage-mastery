# Jesse (Smart Contracting, Jesse and Mike)

**Applied to the pack, 2026-11-12.** The Smart Contracting chat ran the step below on `ideas/smart-contracting/build`: client edition, rules, skill and handoff all PASS, `tools/check.py` RESULT PASS. The pack runs 12 routines, about 47 runs a week, none more often than every 3 hours. Its standing instructions are about 2,750 words (master prompt 1,061), which the report flags for trimming. Report: [report.md](report.md). The live bot still waits on Justin's yes (below).

**Status, 2026-11-12:** Justin is building the bot today in the factory chat "GrokBot idea: Smart Contracting (Jesse and Mike)". Its pack is `ideas/smart-contracting/build/` on branch `idea/smart-contracting` of `jbellsolutions/grokbot-factory`. The chat started from the template on `main`, before factory PR #5 put the usage kit into the template, so the pack doesn't carry the kit until this step runs. This is a client bot: client edition, owner names Jesse and Mike.

## Before that pack's PR (Claude Code, on Justin's Mac)

```bash
python3 ~/REPOS/grokbot-usage-mastery/kit/bin/apply.py <factory worktree>/ideas/smart-contracting/build --owner "Jesse and Mike" --edition client          # dry run
python3 ~/REPOS/grokbot-usage-mastery/kit/bin/apply.py <factory worktree>/ideas/smart-contracting/build --owner "Jesse and Mike" --edition client --apply \
  --report ~/REPOS/grokbot-usage-mastery/applied/jesse/report.md
```

Then check the routine table in the report: nothing more often than every 3 hours unless the job needs it, the watchdog every 3 hours, and no two routines of the bot under 5 minutes apart. `tools/check.py` must still print RESULT PASS.

If the pack ends up in another layout (a client-build pack with `START-HERE.md` and `agents/`), the same command works. The kit detects `multi-bot-pack`.

## Once the bot is live on Jesse's account (needs Justin's yes: client production)

1. Download `grokbot-usage-mastery-v<ver>-client.zip` from this repo's latest release.
2. In the bot's one-to-one desktop chat, attach it and send:
   > Unpack the attached zip into your workspace as usage-mastery/ and follow usage-mastery/APPLY.md with --edition client and owner "Jesse and Mike". Dry run first, show me the plan, and change nothing until I say yes.
3. Jesse or Mike: set a monthly additional-usage limit at grok.com/dashboard/billing, and paste the three Auto-review lines the bot shows.
4. A usage reading now, and one a week later, in `log/usage-ledger.md`.
