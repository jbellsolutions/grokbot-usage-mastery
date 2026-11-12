"""The optimizer's update path end to end: build an update from a pack's git history, apply it to an old install twice."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sh(*a, cwd=None, env=None):
    return subprocess.run(list(map(str, a)), cwd=cwd, capture_output=True, text=True, env=env)


class Update(unittest.TestCase):
    def test_build_and_apply(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            r = tmp / "pack"
            (r / "agents").mkdir(parents=True)
            (r / "skills" / "radar").mkdir(parents=True)
            (r / "policies").mkdir()
            (r / "agents" / "01-lead.md").write_text("# Lead\n")
            (r / "agents" / "02-radar.md").write_text("# Radar\n")
            (r / "skills" / "radar" / "SKILL.md").write_text("---\nname: radar\ndescription: d\n---\n# radar\n\n## Steps\n\n1. Search.\n")
            (r / "policies" / "APPROVALS.md").write_text("Ask Tommy.\n")
            (r / "manifest.json").write_text(json.dumps({"owner": "Tommy", "accounts": {"b": {"lead_bot": "Lead", "workspace": "/workspace/t"}},
                                                         "agents": [{"name": "Lead", "charter": "agents/01-lead.md"}, {"name": "Radar", "charter": "agents/02-radar.md"}]}))
            (r / "START-HERE.md").write_text("# Start\n## Step 2. Be\n## Step 3. Go\n")
            for c in (["init", "-q"], ["add", "-A"], ["-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "base"], ["tag", "v1"]):
                sh("git", *c, cwd=r)
            install = tmp / "ws" / "repo"
            shutil.copytree(r, install, ignore=shutil.ignore_patterns(".git"))
            # the kit plus a usage-only skill edit and one out-of-scope policy change
            self.assertEqual(sh(sys.executable, ROOT / "kit/bin/apply.py", r, "--owner", "Tommy", "--apply", "--backup-dir", tmp / "bk").returncode, 0)
            sk = r / "skills" / "radar" / "SKILL.md"
            t = sk.read_text()
            sk.write_text(t.replace("## Steps", "## Usage (read less)\n\nUse clean_page.\n\n## Steps", 1))
            (r / "policies" / "APPROVALS.md").write_text("Ask Tommy twice.\n")
            sh("git", "add", "-A", cwd=r)
            sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "kit", cwd=r)
            z = tmp / "u.zip"
            out = sh(sys.executable, ROOT / "kit/bin/make_update.py", r, "--since", "v1", "--version", "1.0.1", "--out", z)
            self.assertEqual(out.returncode, 0, out.stderr)
            self.assertIn("left out (needs the owner's yes): policies/APPROVALS.md", out.stdout)
            u = tmp / "u"
            zipfile.ZipFile(z).extractall(u)
            meta = json.loads((u / "update.json").read_text())
            self.assertIn("skills/radar/SKILL.md", [f["path"] for f in meta["files"]])
            env = dict(os.environ, OPTIMIZER_REPO=str(install), OPTIMIZER_WORKSPACE=str(tmp / "ws"))
            tool = u / "files" / "usage" / "optimizer" / "update.py"
            first = sh(sys.executable, tool, "apply", u, env=env).stdout
            self.assertRegex(first, r"UPDATE 1\.0\.1: \d+ files changed, 0 already current")
            self.assertIn("Use clean_page.", (install / "skills/radar/SKILL.md").read_text())
            self.assertEqual((install / "policies/APPROVALS.md").read_text(), "Ask Tommy.\n", "out-of-scope change is never copied")
            second = sh(sys.executable, tool, "apply", u, env=env).stdout
            self.assertIn("0 files changed", second)
            for st in meta["steps"]:
                sh(sys.executable, install / "usage/optimizer/update.py", "done", st["id"], env=env)
            self.assertIn("CHAT STEPS: none", sh(sys.executable, tool, "apply", u, env=env).stdout)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
