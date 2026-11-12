#!/usr/bin/env python3
"""Apply the GrokBot usage-mastery kit to one bot or pack.

    python3 kit/bin/apply.py <target-dir>                 # dry run: detect, plan, report. Changes nothing.
    python3 kit/bin/apply.py <target-dir> --apply         # back up, apply, verify, report
    options: --owner NAME  --edition owner|client  --only rules,skill,handoff  --report FILE  --backup-dir DIR
    python3 kit/bin/apply.py <target-dir> --restore <backup-dir>   # roll back an --apply

Target layouts it knows:
  factory-pack    a GrokBot Factory build/ folder (MASTER-PROMPT.md, TRIGGER-MAP.md, skills.json)
  multi-bot-pack  a client-build pack with several bots (START-HERE.md, agents/, manifest.json)
  workspace       a live bot workspace on the bot's computer (context/ plus repo/ or vault/)
  generic         anything else: the kit drops USAGE-RULES.md and usage/ at the root

Only additive, marker-wrapped changes. Re-running is safe: present items are reported as present,
older kit versions are upgraded in place. Gated tricks (spend, keys, sign-ins, new accounts, deletes)
are never applied; they are listed for the owner's yes.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
REPO = KIT.parent
VERSION = (REPO / "VERSION").read_text().strip() if (REPO / "VERSION").exists() else "0.0.0"
SKILL_SRC = KIT / "skill" / "usage-saver"
RULES_TPL = (KIT / "prompts" / "USAGE-RULES.txt").read_text()
RULES_START = "Usage rules (usage-mastery v"
RULES_END = "End of usage rules."
SECTION_RE = re.compile(r"\n## Usage kit \(usage-mastery v[^)]*\)\n.*?(?=\n## |\Z)", re.S)
CRON_RE = re.compile(r"`((?:[\d*/,\-]+\s+){4}[\d*/,\-A-Za-z]+)`")
OWNER_GATED = []


# ---------- helpers ----------

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tree_hash(d: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(x for x in d.rglob("*") if x.is_file() and "__pycache__" not in x.parts):
        h.update(str(f.relative_to(d)).encode())
        h.update(f.read_bytes())
    return h.hexdigest()


def detect(t: Path) -> str:
    if (t / "MASTER-PROMPT.md").exists() and (t / "TRIGGER-MAP.md").exists():
        return "factory-pack"
    if (t / "START-HERE.md").exists() and (t / "agents").is_dir():
        return "multi-bot-pack"
    if (t / "context").is_dir() and ((t / "repo").is_dir() or (t / "vault").is_dir()):
        return "workspace"
    return "generic"


def runs_per_week(cron: str) -> float:
    m, h, dom, mon, dow = cron.split()[:5]

    def count(field, lo, hi):
        if field == "*":
            return hi - lo + 1
        n = 0
        for part in field.split(","):
            step = 1
            if "/" in part:
                part, s = part.split("/")
                step = int(s)
            if part == "*":
                a, b = lo, hi
            elif "-" in part:
                a, b = (int(x) for x in part.split("-"))
            elif part.isdigit():
                a = b = int(part)
            else:
                return 1
            n += len(range(a, b + 1, step))
        return n

    per_day = count(m, 0, 59) * count(h, 0, 23)
    days = 7 if dow == "*" else count(dow, 0, 6)
    if dom != "*" and dow == "*":
        days = count(dom, 1, 31) / 4.3
    return per_day * days


def week_minutes(cron: str):
    """Every minute-of-week (0..10079) a 5-field cron fires at; dom/month treated as every day."""
    m, h, _dom, _mon, dow = cron.split()[:5]

    def vals(field, lo, hi):
        out = set()
        for part in field.split(","):
            step = 1
            if "/" in part:
                part, st = part.split("/")
                step = int(st)
            if part == "*":
                a, b = lo, hi
            elif "-" in part:
                a, b = (int(x) for x in part.split("-"))
            else:
                a = b = int(part)
            out.update(range(a, b + 1, step))
        return out

    days = vals(dow.replace("7", "0"), 0, 6) if dow != "*" else set(range(7))
    return {d * 1440 + hh * 60 + mm for d in days for hh in vals(h, 0, 23) for mm in vals(m, 0, 59)}


def spacing_conflicts(crons):
    """Pairs of different routines that start less than 5 minutes apart somewhere in the week."""
    sets = [(c, label, week_minutes(c)) for c, label in crons]
    bad = []
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i][2], sets[j][2]
            near = {(x + k) % 10080 for x in a for k in range(-4, 5)}
            if near & b:
                bad.append(f"{sets[i][1]} `{sets[i][0]}` and {sets[j][1]} `{sets[j][0]}`")
    return bad


class Ctx:
    def __init__(self, t, layout, args):
        self.t, self.layout, self.args = t, layout, args
        self.apply = args.apply
        self.touched, self.notes = [], []
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        base = Path(args.backup_dir).expanduser() if args.backup_dir else Path.home() / ".usage-mastery-backups"
        self.backup = base / f"{t.name}-{stamp}"
        self.ws = "repo"  # how the bot's prompt refers to the pack inside its workspace
        if layout == "multi-bot-pack":
            try:
                man = json.loads((t / "manifest.json").read_text())
                acct = next(iter(man.get("accounts", {}).values()), {})
                self.ws = acct.get("workspace", "/workspace") + "/repo"
                self.lead = acct.get("lead_bot", "the lead bot")
            except Exception:
                self.lead = "the lead bot"
        self.usage_dir = {"workspace": (t / "repo" / "usage") if (t / "repo").is_dir() else t / "usage"}.get(layout, t / "usage")

    def save_backup(self, p: Path):
        if p.exists():
            dst = self.backup / p.relative_to(self.t)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if p.is_dir():
                if not dst.exists():
                    shutil.copytree(p, dst)
            else:
                shutil.copy2(p, dst)

    def write(self, p: Path, text: str):
        if not self.apply:
            return
        self.save_backup(p)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        self.touched.append(str(p.relative_to(self.t)))


def rules_text(ctx: Ctx) -> str:
    owner = ctx.args.owner
    if ctx.layout == "multi-bot-pack":
        audit = f"Mondays, {ctx.lead}'s evening brief also follows {ctx.ws}/usage/AUDIT.md for the whole team (report only). Other bots: no extra run."
        path = f"{ctx.ws}/usage"
    elif ctx.layout == "workspace":
        path = str(ctx.usage_dir)
        audit = f"Once a week (Mondays), the evening scoreboard or brief also follows {path}/AUDIT.md (report only)."
    else:
        path = "repo/usage"
        audit = f"Mondays, the lead's evening scoreboard run also follows {path}/AUDIT.md (report only). No extra routine."
    return RULES_TPL.format(version=VERSION, owner=owner, usage_path=path, audit_line=audit).strip()


# ---------- actions: each returns (status, detail); status in present|planned|applied|upgraded|skipped|flag ----------

def act_rules(ctx: Ctx):
    block = rules_text(ctx)
    t = ctx.t
    if ctx.layout == "factory-pack":
        p = t / "MASTER-PROMPT.md"
        text = p.read_text()
        if RULES_START in text:
            cur = text[text.index(RULES_START): text.index(RULES_END) + len(RULES_END)]
            if cur == block:
                return "present", "usage rules already in MASTER-PROMPT.md (this version)"
            ctx.write(p, text.replace(cur, block))
            return ("upgraded" if ctx.apply else "planned"), "replace usage rules block in MASTER-PROMPT.md with this version"
        m = re.search(r"```\n(.*?)\n```", text, re.S)
        if not m:
            ctx.write(p, text.rstrip() + "\n\n```\n" + block + "\n```\n")
            return ("applied" if ctx.apply else "planned"), "append usage rules to MASTER-PROMPT.md (no fenced prompt found)"
        inner = m.group(1)
        if "[SILENT]" in inner.splitlines()[-1]:
            lines = inner.splitlines()
            new_inner = "\n".join(lines[:-1]).rstrip() + "\n\n" + block + "\n\n" + lines[-1]
        else:
            new_inner = inner.rstrip() + "\n\n" + block
        ctx.write(p, text[: m.start(1)] + new_inner + text[m.end(1):])
        return ("applied" if ctx.apply else "planned"), "add usage rules inside the master prompt (saved to memory word for word)"
    if ctx.layout == "multi-bot-pack":
        p = t / "policies" / "USAGE.md"
        doc = ("# Usage rules for every bot on this account\n\n"
               "Every bot saves the block below to memory, word for word (START-HERE Step 2 for the lead bot, Step 6 for the others). "
               f"Tools: `usage/` ([SKILL.md](../usage/SKILL.md)). Generated by grokbot-usage-mastery v{VERSION}.\n\n```\n{block}\n```\n")
        sh = t / "START-HERE.md"
        st = sh.read_text()
        need = []
        anchor = "Save its Profile block to memory, word for word, as your standing role, and set it as your description if your settings allow it."
        add = f" Read {ctx.ws}/policies/USAGE.md and save its rules block to memory, word for word."
        if anchor in st and add.strip() not in st:
            st = st.replace(anchor, anchor + add)
            need.append("Step 6 setup message")
        s2 = f"\n**Usage rules.** Read `policies/USAGE.md` and save its rules block to memory, word for word, under your standing role.\n"
        if "policies/USAGE.md` and save its rules block" not in st and "## Step 3." in st:
            st = st.replace("\n## Step 3.", s2 + "\n## Step 3.", 1)
            need.append("Step 2")
        if p.exists() and p.read_text() == doc and not need:
            return "present", "policies/USAGE.md and START-HERE lines present (this version)"
        ctx.write(p, doc)
        if need:
            ctx.write(sh, st)
        return ("applied" if ctx.apply else "planned"), "write policies/USAGE.md; START-HERE: " + (", ".join(need) or "already wired")
    p = t / ("context/usage-rules.md" if ctx.layout == "workspace" else "USAGE-RULES.md")
    doc = f"# Usage rules (save to memory word for word)\n\n```\n{block}\n```\n"
    if p.exists() and p.read_text() == doc:
        return "present", f"{p.relative_to(t)} present (this version); confirm it is saved in the bot's memory"
    ctx.write(p, doc)
    ctx.notes.append(f"The bot must save the block in {p.relative_to(t)} to its memory, word for word (a chat step, not a file step).")
    return ("applied" if ctx.apply else "planned"), f"write {p.relative_to(t)}; the bot saves it to memory"


def act_skill(ctx: Ctx):
    dst = ctx.usage_dir
    if dst.exists() and (dst / "VERSION").exists() and tree_hash(dst) == ctx.skill_hash:
        return "present", f"{dst.relative_to(ctx.t)}/ matches kit v{VERSION}"
    verb = "upgrade" if dst.exists() else "add"
    if ctx.apply:
        ctx.save_backup(dst)
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(ctx.staged_skill, dst)
        ctx.touched.append(str(dst.relative_to(ctx.t)) + "/")
    return ("applied" if ctx.apply else "planned"), f"{verb} {dst.relative_to(ctx.t)}/ (usage-saver skill: 10 scripts, AUDIT, RESET, LEDGER)"


def handoff_section(ctx: Ctx) -> str:
    u = f"{ctx.ws}/usage" if ctx.layout == "multi-bot-pack" else "repo/usage"
    who = ctx.args.owner
    return (f"\n## Usage kit (usage-mastery v{VERSION})\n\n"
            f"From `grokbot-usage-mastery`. Do these right after the workspace and memory steps.\n\n"
            f"1. Run `bash {u}/scripts/install.sh` (free, pinned, no keys) and paste its last line into `log/setup.md`.\n"
            f"2. Save `{u}/SKILL.md` as a private skill named usage-saver.\n"
            f"3. Copy `{u}/LEDGER.md` to `log/usage-ledger.md`. Ask {who} for the baseline reading (Settings → Usage: % used and reset date) before the first test day, and again after it.\n"
            f"4. The weekly audit (`{u}/AUDIT.md`) runs inside the Monday evening report; it adds no routine and changes nothing.\n"
            f"5. Check: `bash {u}/scripts/grep_lines.sh 'usage-mastery v' {u}/.. 3` prints at least one line (the rules are in place and the scripts run).\n"
            f"6. Show {who} the two owner-only steps, once per Grok account, and record the answers in `log/setup.md`:\n"
            f"   - A spending cap: grok.com/dashboard/billing → a monthly additional-usage limit, or Auto top-up off. The bot never changes billing.\n"
            f"   - Three lines for Auto-review → Custom Rules (chat only; routines never wait on approvals):\n\n"
            f"     ```\n"
            f"     Ask first before opening more than 5 web pages for one task.\n"
            f"     Ask first before starting a sub-agent or a second bot on a job.\n"
            f"     Ask first before re-running a step that has already failed twice.\n"
            f"     ```\n")


def act_handoff(ctx: Ctx):
    name = {"factory-pack": "HANDOFF.md", "multi-bot-pack": "START-HERE.md"}.get(ctx.layout)
    if not name:
        return "skipped", "no handoff file in this layout; steps are in the report"
    p = ctx.t / name
    text = p.read_text()
    sec = handoff_section(ctx)
    m = SECTION_RE.search(text)
    if m:
        if m.group(0).strip() == sec.strip():
            return "present", f"usage section in {name} (this version)"
        ctx.write(p, text[: m.start()] + sec.rstrip("\n") + text[m.end():])
        return ("upgraded" if ctx.apply else "planned"), f"replace usage section in {name}"
    for anchor in ("\n## Bring-up order", "\n## Step 7.", "\n## Step 8.", "\n## Step 9."):
        if anchor in text:
            new = text.replace(anchor, sec + anchor, 1)
            break
    else:
        new = text.rstrip() + "\n" + sec
    ctx.write(p, new)
    return ("applied" if ctx.apply else "planned"), f"add usage section to {name}"


def label_of(line: str, fname: str) -> str:
    cells = [c.strip() for c in line.split("|")]
    if len(cells) >= 3 and cells[0] in ("Schedule", "Event"):
        return cells[2][:40]
    return fname


DAYS = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}


def plain_to_crons(when: str):
    """'Every weekday at 6:17 AM', 'Mondays at 6:03 AM', 'The 1st of each month at 7:11 AM',
    'Every 2 hours' -> 5-field crons. Returns [] when it isn't a schedule."""
    w = when.lower()
    m = re.search(r"every (\d+) (minute|hour)s?", w)
    if m:
        n = int(m.group(1))
        return [f"*/{n} * * * *" if m.group(2) == "minute" else f"0 */{n} * * *"]
    if "hourly" in w or "every hour" in w:
        return ["0 * * * *"]
    times = re.findall(r"(\d{1,2}):(\d{2})\s*(am|pm)?", w)
    if not times:
        return []
    if "weekday" in w:
        dow = "1-5"
    elif re.search(r"every day|daily|each day", w):
        dow = "*"
    else:
        names = [d for d in DAYS if d in w]
        dow = ",".join(str(DAYS[d]) for d in names) if names else None
    dom = "*"
    mm = re.search(r"(\d{1,2})(?:st|nd|rd|th) of (?:each|every) month", w)
    if mm:
        dom, dow = mm.group(1), "*"
    if dow is None:
        return []
    out = []
    for h, mi, ap in times:
        h = int(h) % 12 + (12 if ap == "pm" else 0) if ap else int(h)
        out.append(f"{int(mi)} {h} {dom} * {dow}")
    return out


def act_routines(ctx: Ctx):
    files = [ctx.t / "TRIGGER-MAP.md"] if (ctx.t / "TRIGGER-MAP.md").exists() else sorted((ctx.t / "agents").glob("*.md")) if (ctx.t / "agents").is_dir() else []
    rows = []
    for f in files:
        for line in f.read_text().splitlines():
            if f.name == "TRIGGER-MAP.md" and not re.match(r"^\| (?:Schedule|Event) \|", line):
                continue  # count each routine once: the per-role tables, as tools/check.py does
            crons = CRON_RE.findall(line)
            if not crons and line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 2:
                    crons = plain_to_crons(cells[1])
                    if crons:
                        line = "| Schedule | " + " ".join(f"`{c}`" for c in crons) + f" | {cells[0]} | {cells[1]} |"
            for c in crons:
                try:
                    rows.append((runs_per_week(c), c, f.name, re.sub(r"\s+", " ", line.strip("| ")).strip()[:90]))
                except Exception:
                    pass
    if not rows:
        return "skipped", "no cron schedules found to audit"
    total = sum(r[0] for r in rows)
    hot = [r for r in rows if r[0] > 56]
    ctx.routine_rows = sorted(rows, reverse=True)
    try:
        # The 5-minute rule is per bot: one bot per agents/*.md in a multi-bot pack, one bot otherwise.
        ctx.spacing = []
        for bot in sorted({r[2] for r in rows}):
            ctx.spacing += spacing_conflicts([(c, label_of(ln, fname)) for _, c, fname, ln in rows if fname == bot])
    except Exception:
        ctx.spacing = []
    detail = f"{len(rows)} schedules, about {int(total)} runs a week"
    if ctx.spacing:
        detail += f"; {len(ctx.spacing)} pairs start under 5 minutes apart (Grok needs 5): " + "; ".join(ctx.spacing[:3])
    if hot:
        detail += f"; {len(hot)} run more than every 3 hours (see table): candidates for a slower cron or a script doorbell"
        return "flag", detail
    return "present", detail + "; none more often than every 3 hours"


def act_skills_count(ctx: Ctx):
    n = len([p for p in ctx.t.rglob("SKILL.md") if "usage" not in p.parts and ".git" not in p.parts])
    if n > 90:
        return "flag", f"{n} skills: over the ~90 a creator keeps per account (his rule of thumb, unverified). Check that each role loads only what it needs"
    return "present", f"{n} skills (under 90)"


def act_present(ctx: Ctx):
    t = ctx.t
    blob = ""
    for name in ("MASTER-PROMPT.md", "START-HERE.md", "CHARTER.md", "GATES.md", "PLAYBOOK.md"):
        if (t / name).exists():
            blob += (t / name).read_text()
    for d in ("agents", "roles", "policies"):
        if (t / d).is_dir():
            blob += "".join(p.read_text() for p in (t / d).glob("*.md"))
    have = {
        "quiet runs end [SILENT]": "[SILENT]" in blob,
        "handoffs through files (requests/)": "requests/" in blob,
        "guards as scripts": (t / "guards" / "scripts").is_dir() or "send gate" in blob.lower() or "send_guard" in blob,
        "STOP switch": "STOP" in blob,
        "spend gate (never spend without a yes)": bool(re.search(r"never spend|spend_guard|spend-approvals|no spend|send, post, spend|before buying anything|never buy", blob, re.I)),
    }
    ctx.present_map = have
    missing = [k for k, v in have.items() if not v]
    return ("present" if not missing else "flag"), ("already built in: " + ", ".join(k for k, v in have.items() if v)) + (f"; missing: {', '.join(missing)}" if missing else "")


def act_prompt_weight(ctx: Ctx):
    """Words every turn re-reads: the master prompt (or charters' Profile blocks) plus role prompt sections."""
    t, words, parts = ctx.t, 0, []
    if (t / "MASTER-PROMPT.md").exists():
        m = re.search(r"```\n(.*?)\n```", (t / "MASTER-PROMPT.md").read_text(), re.S)
        if m:
            n = len(m.group(1).split()); words += n; parts.append(f"master prompt {n}")
        for r in sorted((t / "roles").glob("*.md")) if (t / "roles").is_dir() else []:
            sec = re.search(r"## System prompt section.*?```\n(.*?)\n```", r.read_text(), re.S)
            if sec:
                n = len(sec.group(1).split()); words += n; parts.append(f"{r.stem} {n}")
    elif (t / "agents").is_dir():
        for a in sorted((t / "agents").glob("*.md")):
            sec = re.search(r"## Profile\n(.*?)(?=\n## |\Z)", a.read_text(), re.S)
            if sec:
                n = len(sec.group(1).split()); words = max(words, n); parts.append(f"{a.stem} {n}")
    if not parts:
        return "skipped", "no prompt found to weigh"
    big = sorted(parts, key=lambda x: -int(x.split()[-1]))[:3]
    detail = f"about {words} words of standing instructions memory holds (largest: {', '.join(big)}); every turn and run re-reads them"
    return ("flag" if words > 2500 else "present"), detail + ("; trim duplicates and move reference detail into files" if words > 2500 else "")


ACTIONS = [
    ("rules", "Usage rules in every bot's memory", act_rules, True),
    ("skill", "usage-saver skill and scripts", act_skill, True),
    ("handoff", "Install, ledger and weekly audit steps in the handoff", act_handoff, True),
    ("routines", "Routine frequency audit (report only)", act_routines, False),
    ("skills-count", "Skill count check (report only)", act_skills_count, False),
    ("prompt-weight", "Instructions weight (report only)", act_prompt_weight, False),
    ("present", "Usage habits the pack already has", act_present, False),
]


def gated(edition: str):
    p = REPO / "tricks" / "tricks.json"
    if not p.exists():
        return []
    out = []
    for tr in json.loads(p.read_text())["tricks"]:
        if tr.get("apply", {}).get("kind") != "gated":
            continue
        if edition == "client" and tr.get("source_class") == "paid":
            continue
        out.append(tr)
    return out


def verify(ctx: Ctx):
    res = []
    for aid, _, fn, writes in ACTIONS:
        if writes and (not ctx.args.only or aid in ctx.args.only):
            st, _ = fn(ctx_readonly(ctx))
            res.append((aid, st))
    chk = None
    if ctx.layout == "factory-pack" and (ctx.t / "tools" / "check.py").exists():
        r = subprocess.run([sys.executable, "tools/check.py"], cwd=ctx.t, capture_output=True, text=True)
        chk = next((l for l in r.stdout.splitlines() if l.startswith("RESULT")), r.stdout.strip().splitlines()[-1] if r.stdout.strip() else f"exit {r.returncode}")
    return res, chk


def ctx_readonly(ctx: Ctx):
    class A:  # same args, apply off
        pass
    a = A()
    a.__dict__.update(vars(ctx.args))
    a.apply = False
    c = Ctx(ctx.t, ctx.layout, a)
    c.skill_hash, c.staged_skill = ctx.skill_hash, ctx.staged_skill
    return c


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--owner", default="the owner")
    ap.add_argument("--edition", choices=["owner", "client"], default="owner")
    ap.add_argument("--only", default="")
    ap.add_argument("--report", default="")
    ap.add_argument("--backup-dir", default="")
    ap.add_argument("--restore", default="", help="copy a backup folder from an earlier --apply back over the target, then exit")
    args = ap.parse_args()
    if args.restore:
        src, dst = Path(args.restore).expanduser(), Path(args.target).expanduser().resolve()
        n = 0
        for f in src.rglob("*"):
            if f.is_file():
                out = dst / f.relative_to(src)
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, out)
                n += 1
        print(f"restore: {n} files copied back from {src}. Files the kit added (usage/, USAGE-RULES.md, policies/USAGE.md) stay; delete them by hand if you want them gone.")
        return
    args.only = [x for x in args.only.split(",") if x]
    t = Path(args.target).expanduser().resolve()
    if not t.is_dir():
        sys.exit(f"apply: {t} is not a folder")
    layout = detect(t)
    ctx = Ctx(t, layout, args)
    # stage the skill with a VERSION file so a re-run can compare exactly
    stage = Path(os.environ.get("TMPDIR", "/tmp")) / f"usage-saver-stage-{os.getpid()}"
    if stage.exists():
        shutil.rmtree(stage)
    shutil.copytree(SKILL_SRC, stage, ignore=shutil.ignore_patterns("__pycache__"))
    (stage / "VERSION").write_text(VERSION + "\n")
    ctx.staged_skill, ctx.skill_hash = stage, tree_hash(stage)
    ctx.routine_rows = []

    results = []
    for aid, title, fn, _ in ACTIONS:
        if args.only and aid not in args.only:
            continue
        st, detail = fn(ctx)
        results.append((aid, title, st, detail))
    ver, chk = verify(ctx) if args.apply else ([], None)
    shutil.rmtree(stage, ignore_errors=True)

    mode = "APPLY" if args.apply else "DRY RUN (nothing changed; add --apply)"
    L = [f"# Usage-mastery report: {t.name}", "",
         f"- Kit: grokbot-usage-mastery v{VERSION}", f"- Target: `{t}`", f"- Layout: {layout}",
         f"- Mode: {mode}", f"- Edition: {args.edition}", f"- When: {dt.datetime.now().isoformat(timespec='seconds')}", "",
         "## Plan and result", "", "| Step | What | Status | Detail |", "|---|---|---|---|"]
    L += [f"| {a} | {ti} | {st} | {d} |" for a, ti, st, d in results]
    if ctx.routine_rows:
        L += ["", "## Routines by runs per week (most first)", "", "| Runs/week | Cron | File | Line |", "|---|---|---|---|"]
        L += [f"| {int(r)} | `{c}` | {f} | {ln.replace('|', '/')} |" for r, c, f, ln in ctx.routine_rows[:15]]
    if args.apply:
        L += ["", "## Verify", ""]
        L += [f"- {a}: {'PASS' if st in ('present', 'skipped') else 'FAIL (' + st + ')'}" for a, st in ver]
        if chk:
            L.append(f"- pack check (tools/check.py): {chk}")
        L += ["", f"Backup of every touched file: `{ctx.backup}`" if ctx.touched else "Nothing needed changing.",
              "", "Touched: " + (", ".join(f"`{x}`" for x in ctx.touched) or "nothing")]
    g = gated(args.edition)
    if g:
        L += ["", "## Needs the owner's yes (not applied)", "", "| Trick | Why it waits | What it needs |", "|---|---|---|"]
        L += [f"| {x['title']} | {x['apply'].get('why', '')} | {x['apply'].get('needs', '')} |" for x in g]
    if ctx.notes:
        L += ["", "## Chat steps for the bot", ""] + [f"- {n}" for n in ctx.notes]
    L += ["", "## Measure it", "", "Savings in MASTERY.md are the sources' own tests until your ledger shows them. Take a usage reading before this change and one a week later (`usage/LEDGER.md`)."]
    out = "\n".join(L) + "\n"
    if args.report:
        Path(args.report).expanduser().parent.mkdir(parents=True, exist_ok=True)
        Path(args.report).expanduser().write_text(out)
    print(out)
    bad = [a for a, st in ver if st not in ("present", "skipped")]
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
