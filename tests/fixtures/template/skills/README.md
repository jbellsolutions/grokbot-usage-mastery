# Skills

One folder per skill under `skills/<role>/<skill>/`, each with a `SKILL.md` whose frontmatter has `name` and `description` (the bot loads it when a request matches the description). Scripts and references sit next to it. List each in `skills.json`.

Copy from Justin's existing skills before writing new ones: `jbellsolutions/grokbot-revenue-os` `skills/` has the Revenue OS set (gohighlevel-cli, crm-operator, slack-crm, the sales skills, speakeragent, cold email, revenue-partner, orgo-fleet, computer use). Rewrite Mac paths (`~/.claude`, `/Users/home`) and Hermes commands to workspace paths and `requests/<role>/` files; `python3 tools/check.py` flags any left.
