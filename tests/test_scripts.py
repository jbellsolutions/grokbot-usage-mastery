"""Offline tests for the usage-saver scripts (stdlib fallbacks; no network)."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

S = Path(__file__).resolve().parent.parent / "kit" / "skill" / "usage-saver" / "scripts"


def py(name, *args, stdin=None):
    return subprocess.run([sys.executable, "-I", str(S / name), *map(str, args)], capture_output=True, text=True, input=stdin)


class Scripts(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())

    def test_clean_page_drops_nav_and_scripts(self):
        f = self.d / "p.html"
        f.write_text("<html><nav>Home About Shop Cart Login</nav><script>var x=1</script><article><p>"
                     + "The real article sentence that matters to the reader here. " * 5 + "</p></article><footer>(c) 2026</footer></html>")
        r = py("clean_page.py", f)
        self.assertIn("real article sentence", r.stdout)
        self.assertNotIn("var x", r.stdout)
        self.assertNotIn("Login", r.stdout)

    def test_pick_and_sheet_and_shape(self):
        j = self.d / "r.json"
        j.write_text(json.dumps({"items": [{"name": "a", "stars": 3, "junk": "x" * 500}]}))
        self.assertEqual(py("pick.py", j, "--path", "items", "--fields", "name,stars").stdout.strip(), '{"name":"a","stars":3}')
        c = self.d / "d.csv"
        c.write_text("city,amount\nA,1\nB,5\nA,2\n")
        r = py("sheet_q.py", c, "select city, sum(amount) s from t group by city order by s desc")
        self.assertEqual(r.stdout.split()[1], "B,5")
        shape = self.d / "s.json"
        shape.write_text('{"required": {"name": "str", "email": "email"}}')
        good = self.d / "g.json"
        good.write_text('[{"name": "a", "email": "a@b.co"}]')
        self.assertEqual(py("check_shape.py", shape, good).returncode, 0)
        good.write_text('[{"name": "", "email": "nope"}]')
        r = py("check_shape.py", shape, good)
        self.assertEqual(r.returncode, 1)
        self.assertIn("FAIL 2", r.stdout)

    def test_shorten_and_retry(self):
        out = py("shorten.py", "--head", "2", "--tail", "2", stdin="\n".join(["line %d" % i for i in range(100)] + ["ERROR boom"] + ["x"] * 5)).stdout
        self.assertIn("ERROR boom", out)
        self.assertIn("lines cut", out)
        flag = self.d / "flag"
        r = py("retry.py", "--tries", "3", "--wait", "0.01", "--", "sh", "-c", f"test -f {flag} || {{ touch {flag}; exit 1; }}")
        self.assertEqual(r.returncode, 0)
        self.assertIn("ok on try 2", r.stderr)

    def test_usage_csv(self):
        c = self.d / "u.csv"
        c.write_text("Date,Bot,Kind,Tokens\n1,lead,routine,900\n1,lead,chat,100\n2,sales,routine,1000\n")
        out = py("usage_csv.py", c).stdout
        self.assertIn("Tokens by Bot", out)
        self.assertIn("95.0%  1,900  routine", out)  # routines 1900 of 2000

    def test_page_diff_silent_when_unchanged(self):
        f = self.d / "p.html"
        f.write_text("<p>" + "Price is ten dollars for the basic plan this month. " * 2 + "</p>")
        st = self.d / "st"
        py("page_diff.py", f, st)
        self.assertEqual(py("page_diff.py", f, st).stdout, "")
        f.write_text("<p>" + "Price is twelve dollars for the basic plan this month. " * 2 + "</p>")
        self.assertIn("changed lines", py("page_diff.py", f, st).stdout)


if __name__ == "__main__":
    unittest.main()
