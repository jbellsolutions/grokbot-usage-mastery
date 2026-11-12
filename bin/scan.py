#!/usr/bin/env python3
"""Weekly scan: list what is new in the last N days. Free and deterministic; the agent does the judging.

    python3 -I bin/scan.py [--days 7] [--out refresh/candidates/<date>.md] [--no-captions]

Writes a candidates file: new videos (with caption text saved beside it), new or updated GitHub repos,
and any change on the xAI docs pages. It never posts, signs in, or spends.
"""
import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAVER = ROOT / "kit" / "skill" / "usage-saver" / "scripts"
STATE = ROOT / "refresh" / "state"


def sh(cmd, timeout=240):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except Exception as e:  # noqa: BLE001
        return f"ERROR {e}"


def known_ids():
    ids = set()
    for p in [ROOT / "tricks" / "tricks.json", *(ROOT / "sources" / "notes").glob("*.md"), *(ROOT / "refresh" / "candidates").glob("*.md")]:
        if p.exists():
            ids |= set(re.findall(r"(?:youtu\.be/|watch\?v=)([\w-]{11})", p.read_text()))
    return ids


def videos(wl, since, seen):
    out, rx = {}, re.compile(wl["title_must_match"], re.I)
    fmt = "%(id)s\t%(upload_date)s\t%(channel)s\t%(duration)s\t%(title)s"
    srcs = [f"https://www.youtube.com/channel/{c['id']}/videos" for c in wl["youtube_channels"]]
    srcs += [f"ytsearchdate15:{q}" for q in wl["youtube_searches"]]
    for s in srcs:
        args = ["yt-dlp", "--skip-download", "--ignore-errors", "--print", fmt, "--dateafter", since.strftime("%Y%m%d")]
        if "/channel/" in s:
            args += ["--playlist-end", "12", "--break-on-reject"]
        for line in sh(args + [s], timeout=600).splitlines():
            parts = line.split("\t")
            if len(parts) != 5 or parts[1] == "NA" or parts[1] < since.strftime("%Y%m%d"):
                continue
            vid, date, chan, dur, title = parts
            if vid in seen or not rx.search(title + " " + chan):
                continue
            out[vid] = {"date": f"{date[:4]}-{date[4:6]}-{date[6:]}", "channel": chan, "title": title, "minutes": round(float(dur or 0) / 60) if dur.replace(".", "").isdigit() else "?"}
    return out


def captions(vid, d: Path):
    d.mkdir(parents=True, exist_ok=True)
    sh(["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs", "--sub-langs", "en-orig,en", "--sub-format", "vtt",
        "-o", str(d / "%(id)s.%(ext)s"), f"https://youtu.be/{vid}"], timeout=300)
    vtts = sorted(d.glob(f"{vid}*.vtt"))
    if not vtts:
        return None
    lines, last = [], None
    for l in vtts[0].read_text(errors="replace").splitlines():
        l = re.sub(r"<[^>]+>", "", l).strip()
        if not l or "-->" in l or l.startswith(("WEBVTT", "Kind:", "Language:")) or l == last:
            continue
        lines.append(l)
        last = l
    txt = d / f"{vid}.txt"
    txt.write_text(" ".join(lines))
    for v in vtts:
        v.unlink()
    return txt


def repos(wl, since):
    rows = {}
    for q in wl["github_searches"]:
        raw = sh(["gh", "search", "repos", q, "--updated", f">={since:%Y-%m-%d}", "--limit", "25",
                  "--json", "fullName,stargazersCount,pushedAt,description,license,url"])
        try:
            for r in json.loads(raw):
                rows[r["fullName"]] = r
        except Exception:  # noqa: BLE001
            pass
    old = json.loads((STATE / "repos.json").read_text()) if (STATE / "repos.json").exists() else {}
    new = {k: v for k, v in rows.items() if k not in old}
    STATE.mkdir(parents=True, exist_ok=True)
    (STATE / "repos.json").write_text(json.dumps({**old, **{k: v["pushedAt"] for k, v in rows.items()}}, indent=1, sort_keys=True))
    return new


def docs(wl):
    out = {}
    for url in wl["docs_pages"]:
        r = subprocess.run([sys.executable, "-I", str(SAVER / "page_diff.py"), url, str(STATE / "docs"), "--max-lines", "60"],
                           capture_output=True, text=True, timeout=120)
        out[url] = (r.stdout or r.stderr).strip()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", default="")
    ap.add_argument("--no-captions", action="store_true")
    a = ap.parse_args()
    today = dt.date.today()
    since = today - dt.timedelta(days=a.days)
    wl = json.loads((ROOT / "refresh" / "watchlist.json").read_text())
    out = Path(a.out) if a.out else ROOT / "refresh" / "candidates" / f"{today}.md"
    capdir = ROOT / "refresh" / "captions" / str(today)  # gitignored
    if not shutil.which("yt-dlp"):
        print("scan: yt-dlp missing; video scan skipped", file=sys.stderr)
    vids = videos(wl, since, known_ids()) if shutil.which("yt-dlp") else {}
    L = [f"# Weekly scan {today} (since {since})", "", f"## New videos ({len(vids)})", "",
         "| Date | Channel | Min | Title | Captions |", "|---|---|---|---|---|"]
    for vid, m in sorted(vids.items(), key=lambda kv: kv[1]["date"], reverse=True):
        cap = None if a.no_captions else captions(vid, capdir)
        L.append(f"| {m['date']} | {m['channel'].replace('|', '/')} | {m['minutes']} | [{m['title']}](https://youtu.be/{vid}) | {cap.relative_to(ROOT) if cap else 'none'} |")
    nr = repos(wl, since)
    L += ["", f"## New GitHub repos ({len(nr)})", "", "| Repo | Stars | Pushed | License | About |", "|---|---|---|---|---|"]
    for k, r in sorted(nr.items(), key=lambda kv: -kv[1].get("stargazersCount", 0)):
        L.append(f"| [{k}]({r['url']}) | {r.get('stargazersCount', 0)} | {r['pushedAt'][:10]} | {(r.get('license') or {}).get('key', 'none')} | {(r.get('description') or '')[:90].replace('|', '/')} |")
    L += ["", "## xAI docs changes", ""]
    for url, diff in docs(wl).items():
        L += [f"### {url}", "", "```", diff or "(no change)", "```", ""]
    L += ["## Read by hand (browser)", ""] + [f"- {m['what']}: {m['url']}" for m in wl["manual"]]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n")
    print(f"scan: {len(vids)} videos, {len(nr)} repos -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


if __name__ == "__main__":
    main()
