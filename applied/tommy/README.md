# Tommy (TMEC Services): prepared, not applied

**Status, 2026-11-12:** prepared only.
- The change is [`tmec-grokbot-usage-v1.0.0.patch`](tmec-grokbot-usage-v1.0.0.patch), made with the kit's client edition against `jbellsolutions/tmec-grokbot` at `9f6af7f`. It applies cleanly (`git apply --check` passed).
- Nothing is committed or pushed to his repo. That repo is **public** and is Tommy's install source, so a push publishes the change and reaches his bots on their next install.
- Report: [report.md](report.md).

## What the patch does

- `usage/`: the usage-saver skill (10 scripts, the weekly AUDIT, RESET and LEDGER).
- `policies/USAGE.md`: the rules block, with Tommy as owner and the audit inside TMEC Command's Monday evening brief.
- `START-HERE.md`, three edits:
  - Step 2: TMEC Command saves the rules.
  - Step 6: every bot's setup message saves them too.
  - A "Usage kit" section before Step 7: install, ledger, spend cap, Auto-review lines.

## What the audit found

- Already lean: 18 routines across 11 bots, about 55 runs a week. None runs more often than every 3 hours, and no bot has two routines under 5 minutes apart.
- Standing instructions per bot: about 300 words. Light.
- Already in place: the send gate, the stop file, file handoffs, and no spending without Tommy's yes.

The win for Tommy is mostly the read-less scripts, the ledger, and the spend cap. His schedule is already sound.

## On Justin's yes

```bash
cd "/Users/home/AI OS Market Share /AIOS/Client Builds/Tommy/tmec-grokbot"
git am ~/REPOS/grokbot-usage-mastery/applied/tommy/tmec-grokbot-usage-v1.0.0.patch
git push origin main
# then cut the release the install downloads (the repo's own release step, e.g. v1.0.2 with tmec-grokbot.zip rebuilt)
```

If Tommy's bots are already installed by then: in TMEC Command's one-to-one chat, send "Pull the latest tmec-grokbot release and follow the Usage kit section of START-HERE.md. Show me the plan first." Tommy sets the spend cap and pastes the Auto-review lines himself.
