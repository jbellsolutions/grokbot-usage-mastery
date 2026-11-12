"""End-to-end tests for kit/bin/apply.py on copies of real layouts. Run: python3 -m unittest discover tests"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPLY = ROOT / "kit" / "bin" / "apply.py"
FACTORY = Path(os.environ.get("FACTORY_TEMPLATE", Path(__file__).resolve().parent / "fixtures" / "template"))  # pre-kit snapshot of the factory template


def run(*args):
    return subprocess.run([sys.executable, str(APPLY), *map(str, args)], capture_output=True, text=True)


def snapshot(d: Path):
    return {str(p.relative_to(d)): p.read_bytes() for p in d.rglob("*") if p.is_file()}


class FactoryPack(unittest.TestCase):
    def setUp(self):
        if not FACTORY.exists():
            self.skipTest("factory template not on this machine")
        self.tmp = Path(tempfile.mkdtemp())
        self.t = self.tmp / "build"
        shutil.copytree(FACTORY, self.t)
        self.bk = self.tmp / "bk"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_dry_run_changes_nothing(self):
        before = snapshot(self.t)
        r = run(self.t)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("DRY RUN", r.stdout)
        self.assertIn("| rules |", r.stdout)
        self.assertEqual(before, snapshot(self.t))

    def test_apply_verify_rerun_restore(self):
        orig = snapshot(self.t)
        r = run(self.t, "--apply", "--owner", "Justin", "--backup-dir", self.bk)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        mp = (self.t / "MASTER-PROMPT.md").read_text()
        self.assertIn("Usage rules (usage-mastery v", mp)
        self.assertLess(mp.index("Usage rules"), mp.index("[SILENT].\n```"), "rules go inside the fence, before the [SILENT] line")
        self.assertTrue((self.t / "usage" / "SKILL.md").exists())
        self.assertIn("## Usage kit (usage-mastery v", (self.t / "HANDOFF.md").read_text())
        self.assertIn("pack check (tools/check.py): RESULT", r.stdout)
        self.assertNotIn("RESULT: FAIL", r.stdout)
        after = snapshot(self.t)
        r2 = run(self.t, "--apply", "--owner", "Justin", "--backup-dir", self.bk)
        self.assertEqual(r2.returncode, 0)
        self.assertIn("Nothing needed changing", r2.stdout)
        self.assertEqual(after, snapshot(self.t), "second apply is a no-op")
        backup = next(self.bk.iterdir())
        run(self.t, "--restore", backup)
        restored = snapshot(self.t)
        for k, v in orig.items():
            self.assertEqual(restored[k], v, k)

    def test_upgrade_replaces_block(self):
        run(self.t, "--apply", "--backup-dir", self.bk)
        mp = self.t / "MASTER-PROMPT.md"
        mp.write_text(mp.read_text().replace("Usage rules (usage-mastery v", "Usage rules (usage-mastery v0.0.1-old ", 1))
        r = run(self.t, "--apply", "--backup-dir", self.bk)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual(mp.read_text().count("Usage rules (usage-mastery v"), 1)
        self.assertNotIn("0.0.1-old", mp.read_text())


class MultiBotPack(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        t = self.t = self.tmp / "pack"
        (t / "agents").mkdir(parents=True)
        (t / "policies").mkdir()
        (t / "agents" / "01-lead.md").write_text("# Lead\n## Routines\n| Morning | `0 7 * * *` |\n| Watch | `*/15 * * * *` |\n")
        (t / "manifest.json").write_text(json.dumps({"accounts": {"business": {"lead_bot": "Lead", "workspace": "/workspace/x"}}}))
        (t / "START-HERE.md").write_text("# Start\n## Step 2. Become Lead\nSave memory.\n## Step 3. Intake\n## Step 6. Team\nRead /workspace/x/repo/agents/<f>. Save its Profile block to memory, word for word, as your standing role, and set it as your description if your settings allow it. Reply ready.\n## Step 9. Report\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_apply(self):
        r = run(self.t, "--apply", "--owner", "Tommy", "--edition", "client", "--backup-dir", self.tmp / "bk")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("multi-bot-pack", r.stdout)
        st = (self.t / "START-HERE.md").read_text()
        self.assertIn("/workspace/x/repo/policies/USAGE.md and save its rules block", st)
        self.assertIn("**Usage rules.**", st)
        self.assertLess(st.index("## Usage kit"), st.index("## Step 9."))
        self.assertIn("Tommy", (self.t / "policies" / "USAGE.md").read_text())
        self.assertIn("flag", r.stdout)  # the 15-minute routine
        self.assertIn("672 | `*/15 * * * *`", r.stdout)


class Generic(unittest.TestCase):
    def test_generic_and_workspace(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            r = run(tmp, "--apply", "--backup-dir", tmp / ".bk")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertTrue((tmp / "USAGE-RULES.md").exists())
            ws = tmp / "ws"
            (ws / "context").mkdir(parents=True)
            (ws / "vault").mkdir()
            r = run(ws, "--apply", "--backup-dir", tmp / ".bk")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn("workspace", r.stdout)
            self.assertTrue((ws / "context" / "usage-rules.md").exists())
            self.assertIn("Chat steps for the bot", r.stdout)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class Cron(unittest.TestCase):
    def test_runs_and_spacing(self):
        sys.path.insert(0, str(APPLY.parent))
        import apply
        self.assertEqual(apply.runs_per_week("*/30 * * * *"), 336)
        self.assertEqual(apply.runs_per_week("57 */3 * * *"), 56)
        self.assertEqual(apply.runs_per_week("5 15 * * 1,4"), 2)
        self.assertTrue(apply.spacing_conflicts([("0 * * * *", "a"), ("3 12 * * *", "b")]))
        self.assertFalse(apply.spacing_conflicts([("0 * * * *", "a"), ("30 12 * * *", "b")]))


class Render(unittest.TestCase):
    def test_mastery_up_to_date(self):
        r = subprocess.run([sys.executable, str(ROOT / "bin" / "render.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)


if __name__ == "__main__":
    unittest.main()
