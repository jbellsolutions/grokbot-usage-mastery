#!/usr/bin/env python3
"""Render MASTERY.md and sources/INDEX.md from tricks/tricks.json. Run after any change to tricks.json.

    python3 bin/render.py          # write both
    python3 bin/render.py --check  # exit 1 if either is stale (used by the weekly refresh and tests)
"""
import json
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if "--root" in sys.argv:  # render a staged copy (bin/pack's client edition)
    ROOT = Path(sys.argv[sys.argv.index("--root") + 1]).resolve()
CATS = OrderedDict([
    ("setup", "Setup"), ("prompts-skills", "Prompts and skills"), ("memory-context", "Memory and context"),
    ("tools-connectors", "Tools and connectors"), ("cost-usage", "Cost and usage limits"), ("scheduling", "Scheduling"),
    ("reliability", "Reliability"), ("security", "Security"),
])
KIND = {"auto": "kit applies it", "built-in": "already in our packs", "owner": "owner click or paste",
        "gated": "owner decides (spend, keys, accounts, deletes)", "info": "know it, nothing to apply"}
LEVEL = {"measured-here": "measured here", "official": "xAI docs", "shown": "shown in source", "claim": "claim"}

AUTO_REVIEW = """Ask first before opening more than 5 web pages for one task.
Ask first before starting a sub-agent or a second bot on a job.
Ask first before re-running a step that has already failed twice."""


def main():
    data = json.loads((ROOT / "tricks" / "tricks.json").read_text())
    version = (ROOT / "VERSION").read_text().strip()
    tricks = sorted(data["tricks"], key=lambda t: t["rank"])
    L = [f"# GrokBot usage mastery, v{version}", "",
         "The ranked playbook for getting the most out of Grok Bot (xAI) for the least usage. Every trick names its sources, dates, evidence, risk and fit. "
         "Generated from [`tricks/tricks.json`](tricks/tricks.json) by `bin/render.py`; edit the JSON, not this page.", "",
         "**How usage works (xAI FAQ, 2026-11-12):** one weekly pool per account, shared with the Grok apps; extra usage bills by token only if on-demand or Auto top-up is on. "
         "There is no model picker. All your bots share one cloud computer, which is not a security boundary between them. Memory is per bot. "
         "**Where it goes:** each turn and each routine run re-reads the chat. In the one export we have, about 93% of tokens were re-reading history and under 1% were answers. "
         "So the big levers are fewer wake-ups, shorter chats, and smaller things to read.", "",
         "**Apply it:** hand this repo (or its release zip) to Claude Code or your Grok bot and point it at [APPLY.md](APPLY.md).", "",
         "## The top ten", "", "| # | Trick | Evidence | How it lands |", "|---|---|---|---|"]
    for t in tricks[:10]:
        L.append(f"| {t['rank']} | [{t['title']}](#{t['id']}) | {LEVEL[t['evidence_level']]} | {KIND[t['apply']['kind']]} |")
    for cat, name in CATS.items():
        group = [t for t in tricks if t["category"] == cat]
        if not group:
            continue
        L += ["", f"## {name}", ""]
        for t in group:
            src = "; ".join(f"[{s['platform']} {s['date']}]({s['url']})" for s in t["sources"])
            L += [f'<a id="{t["id"]}"></a>', f"### {t['rank']}. {t['title']}", "",
                  t["what"], "",
                  f"- **Evidence ({LEVEL[t['evidence_level']]}):** {t['evidence']}",
                  f"- **Risk:** {t['risk']}",
                  f"- **Fits GrokBot:** {t['fit']}",
                  f"- **Lands as:** {KIND[t['apply']['kind']]}" + (f". {t['apply']['needs']}" if t['apply'].get('needs') else ""),
                  f"- **Sources:** {src}", ""]
    L += ["## Auto-review lines to paste", "",
          "Settings → Auto-review → Custom Rules. These apply in chat; our routines never wait on an approval (they draft, queue and stop).", "",
          "```", AUTO_REVIEW, "```", "",
          "## Rejected", "", "| Idea | Why not |", "|---|---|"]
    L += [f"| {r['title']} | {r['why']} |" for r in data["rejected"]]
    L += ["", "## Gaps in this version", "",
          "- The paid Skool group (AI Systems Society) was not read: the signed-in browser wasn't reachable. Its items will be added as `source_class: paid`, kept in our own words, and never shipped to clients.",
          "- Reddit and X post bodies could not be fetched (WebFetch, curl, firecrawl, and the app's built-in browser, which refuses reddit.com). Claims from them are search snippets, marked as such in `sources/`. Reading them needs Justin's Chrome connected (NEEDS-JUSTIN 2).",
          "- No trick here is measured on a Grok account yet. The ledger (trick 11) is how each one gets proven or dropped.", ""]
    mastery = "\n".join(L)

    seen = OrderedDict()
    for t in tricks:
        for s in t["sources"]:
            seen.setdefault(s["url"], {"date": s["date"], "platform": s["platform"], "tricks": []})["tricks"].append(t["rank"])
    S = ["# Sources", "", f"Every source behind MASTERY.md v{version}, newest first, with the tricks it supports. Research notes in our own words: [notes/](notes/).", "",
         "| Date | Platform | Source | Tricks |", "|---|---|---|---|"]
    for url, m in sorted(seen.items(), key=lambda kv: kv[1]["date"], reverse=True):
        S.append(f"| {m['date']} | {m['platform']} | {url} | {', '.join(str(x) for x in sorted(set(m['tricks'])))} |")
    S.append("")
    index = "\n".join(S)

    targets = {ROOT / "MASTERY.md": mastery, ROOT / "sources" / "INDEX.md": index}
    if "--check" in sys.argv:
        stale = [str(p.relative_to(ROOT)) for p, txt in targets.items() if not p.exists() or p.read_text() != txt]
        print("render: stale " + ", ".join(stale) if stale else "render: up to date")
        sys.exit(1 if stale else 0)
    for p, txt in targets.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(txt)
    print(f"render: wrote MASTERY.md ({len(tricks)} tricks) and sources/INDEX.md ({len(seen)} sources)")


if __name__ == "__main__":
    main()
