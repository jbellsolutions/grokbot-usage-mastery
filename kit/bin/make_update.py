#!/usr/bin/env python3
"""Build an optimization-only update zip for an installed GrokBot pack (any client or factory pack).

    python3 kit/bin/make_update.py <pack-git-repo> --since <tag-or-commit> --version <v> --out <zip> [--name <pack>]

Everything that changed since --since is sorted into:
  usage  the kit's own files (usage/, policies/USAGE.md) and skills whose only change is the
         "## Usage (read less)" section  -> copied by update.py, plus chat steps to re-save rules and skills
  doc    install docs and metadata (START-HERE.md, README.md, manifest.json)  -> copied, nothing to do
  new    a new bot's charter and routine files  -> copied (inert) plus one "ask" step for the owner
  other  anything else (charters, policies, routines, gates)  -> NOT copied; one "ask" step names it
The bot never needs to read the files: update.py applies them and prints only the steps.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

USAGE_SECTION = re.compile(r"## Usage \(read less\)\n\n.*?\n\n", re.S)
DOCS = {"START-HERE.md", "README.md", "manifest.json", ".gitignore", "PACK-VERSION"}


def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=True).stdout


def at(repo, ref, path):
    r = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def slug(charter):
    return re.sub(r"^\d+-", "", Path(charter).stem)


def classify(repo, base, path):
    if path.startswith("usage/") or path == "policies/USAGE.md":
        return "usage"
    if path in DOCS:
        return "doc"
    old = at(repo, base, path)
    if old is None and (path.startswith("agents/") or path.startswith("routines/")):
        return "new"
    if path.startswith("skills/") and path.endswith("SKILL.md") and old is not None:
        new = (repo / path).read_text()
        if USAGE_SECTION.sub("", new, count=1) == old:
            return "usage"
    if path.startswith("skills/") and old is None:
        return "usage" if path.startswith("skills/optimizer/") else "other"
    return "other"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--since", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", default="")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    man = json.loads((repo / "manifest.json").read_text()) if (repo / "manifest.json").exists() else {}
    acct = next(iter(man.get("accounts", {}).values()), {})
    ws = acct.get("workspace", "/workspace/bot")
    lead = acct.get("lead_bot", "the lead bot")
    owner = man.get("owner", "the owner")
    name = a.name or man.get("name") or repo.name
    rp = f"{ws}/repo"
    changed = [p for p in git(repo, "diff", "--name-only", a.since, "HEAD").splitlines() if (repo / p).exists()]
    files, other, skills, new_agents = [], [], [], []
    for p in changed:
        c = classify(repo, a.since, p)
        if c == "other":
            other.append(p)
            continue
        files.append({"path": p, "class": c, "sha256": hashlib.sha256((repo / p).read_bytes()).hexdigest()})
        if c == "usage" and p.startswith("skills/") and p.endswith("SKILL.md"):
            skills.append(Path(p).parent.name)
        if c == "new" and p.startswith("agents/"):
            new_agents.append(p)
    tool = f"python3 {rp}/usage/optimizer/update.py"
    steps = []
    if any(f["path"] == "policies/USAGE.md" for f in files):
        steps.append({"id": f"memory-{a.version}", "kind": "memory",
                      "text": f"Replace any older 'Usage rules (usage-mastery v...)' block in your memory with the block in {rp}/policies/USAGE.md, word for word."})
    if (repo / "usage" / "optimizer" / "SKILL.md").exists():
        steps.append({"id": "skill-optimizer", "kind": "skill",
                      "text": f"Save {rp}/usage/optimizer/SKILL.md as a private skill named optimizer (re-save it if you have it), then run {tool} init."})
    if skills:
        steps.append({"id": f"skills-{a.version}", "kind": "skill",
                      "text": "Re-save these private skills from their files in " + rp + "/skills/<name>/SKILL.md (only their 'Usage (read less)' section changed): " + ", ".join(sorted(set(skills))) + "."})
    team = [ag for ag in man.get("agents", []) if ag.get("name") != lead and not any(ag.get("charter") == n for n in new_agents)]
    if team and steps:
        names = ", ".join(ag["name"] for ag in team)
        steps.append({"id": f"team-{a.version}", "kind": "team",
                      "text": f"For each other bot ({names}): write {ws}/requests/to-<bot>/usage-update-{a.version}.md saying: 'Optimization update {a.version} from Justin's team, reading habits only, no approvals or sends change. "
                              f"1) Replace any older Usage rules (usage-mastery v...) block in your memory with the block in {rp}/policies/USAGE.md, word for word. "
                              f"2) Re-save any of your private skills named in this list from {rp}/skills/<name>/SKILL.md: {', '.join(sorted(set(skills))) or 'none'}. 3) Note done in your daily file.' "
                              f"Then nudge each bot the usual way. If nudges don't work, each bot picks the file up on its next run."})
    for ag in new_agents:
        nm = next((x["name"] for x in man.get("agents", []) if x.get("charter") == ag), slug(ag))
        steps.append({"id": f"ask-new-bot-{slug(ag)}", "kind": "ask",
                      "text": f"Put one line in {owner}'s approval list: 'Add the {nm} bot ({rp}/{ag}) with its routine created paused? It only applies optimization updates; until then {lead} does that job.' Do nothing more about it until {owner} answers."})
    if other:
        steps.append({"id": f"ask-other-{a.version}", "kind": "ask",
                      "text": f"Tell Justin's team (not {owner}) that update {a.version} left out changes that need {owner}'s yes: " + ", ".join(other) + "."})
    meta = {"pack": name, "version": a.version, "base": a.since, "head": git(repo, "rev-parse", "--short", "HEAD").strip(),
            "workspace": ws, "repo": rp, "lead": lead, "owner": owner, "files": files, "steps": steps, "left_out": other}
    upd = f"""# Optimization update {a.version} for {name}

You are {lead}. This is an optimization-only update from Justin's team. It changes how the team reads and saves usage. It changes no approval, gate, send limit, schedule or charter, and it sends nothing.

1. Run `python3 files/usage/optimizer/update.py apply .` from this folder. It copies only what is new into `{rp}` (with a backup), skips what is already current, and prints the chat steps.
2. Do each CHAT STEP it prints, in order, and mark each one with `{tool} done <id>`. Don't open or read the update's other files.
3. In your next brief, tell {owner} in at most three lines: update {a.version} applied, how many files changed, and anything waiting on their yes. Message no one else about it.

Running it twice is safe: the second run changes nothing.
"""
    with tempfile.TemporaryDirectory() as t:
        root = Path(t) / "update"
        for f in files:
            dst = root / "files" / f["path"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(repo / f["path"], dst)
        (root / "update.json").write_text(json.dumps(meta, indent=1) + "\n")
        (root / "UPDATE.md").write_text(upd)
        out = Path(a.out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(root.rglob("*")):
                if p.is_file():
                    z.write(p, p.relative_to(root))
    by = {}
    for f in files:
        by[f["class"]] = by.get(f["class"], 0) + 1
    print(f"make_update: {name} {a.version} ({a.since}..{meta['head']}): {len(files)} files {by}, {len(steps)} steps, left out {len(other)} -> {out}")
    for p in other:
        print(f"  left out (needs the owner's yes): {p}")


if __name__ == "__main__":
    main()
