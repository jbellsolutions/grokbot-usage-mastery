"""Shared: find the workspace. The pack lives at <workspace>/repo/, so the workspace is three levels up
from repo/guards/scripts/. BOT_HOME overrides it (tests use a scratch folder)."""
import os, pathlib
WS = pathlib.Path(os.environ.get("BOT_HOME") or pathlib.Path(__file__).resolve().parents[3])
def p(*parts): return WS.joinpath(*parts)
def stopped(): return p("context", "STOP").exists()
def norm(s): return " ".join("".join(c.lower() if c.isalnum() or c in "@." else " " for c in s).split())
