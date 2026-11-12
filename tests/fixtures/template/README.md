# {{bot_name}}: GrokBot pack

Built from the GrokBot Factory template. Idea: [../IDEA.md](../IDEA.md). Rules this build follows: the factory's `PLAYBOOK.md`.

| File | What |
|---|---|
| [HANDOFF.md](HANDOFF.md) | Paste or attach to GrokBot: Justin's steps, then the bot's |
| [NEEDS-JUSTIN.md](NEEDS-JUSTIN.md) | Sign-ins, keys by name, yeses |
| [MASTER-PROMPT.md](MASTER-PROMPT.md) | The bot's master prompt |
| [CHARTER.md](CHARTER.md) | Purpose, the loop, KPIs, handoffs, workspace, milestones. Wins over a role charter |
| [roles/](roles/) | One charter per role, each with a system prompt section to paste |
| [TRIGGER-MAP.md](TRIGGER-MAP.md) | Every step: started by, role, judgment call, gate. Every routine (50 max) |
| [GATES.md](GATES.md) | The gates and the Ask-first lines for Auto-review |
| [guards/](guards/SKILL.md) | The guard skill and its scripts: suppression, send, spend, heartbeat |
| [skills.json](skills.json), [SKILLS-MAP.md](SKILLS-MAP.md), [skills/](skills/) | Which role uses which skill and account, and the skills themselves |
| [.env.example](.env.example) | Key names only |
| `tools/check.py` | Completeness and secret check: `python3 tools/check.py` |
