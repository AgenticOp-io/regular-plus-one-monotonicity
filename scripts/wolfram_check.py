"""Query Wolfram Alpha and print plaintext pods.

The app id is read from the environment variable WOLFRAM_APPID, or from a
one-line file .wolfram-appid in the repository root. That file is gitignored.
The id is never printed.

Usage:
  python scripts/wolfram_check.py "simplify (d^2/n)^(1/4)"
  python scripts/wolfram_check.py --append notes/wolfram-checks.md "query"

Queries must be bare identities. Do not send theorem names, proof prose,
or the manuscript.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.wolframalpha.com/v2/query"


def app_id() -> str:
    env = os.environ.get("WOLFRAM_APPID", "").strip()
    if env:
        return env
    path = ROOT / ".wolfram-appid"
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    sys.exit("No Wolfram app id. Set WOLFRAM_APPID or write .wolfram-appid (gitignored).")


def query(text: str) -> dict:
    params = urllib.parse.urlencode(
        {
            "appid": app_id(),
            "input": text,
            "output": "json",
            "format": "plaintext",
        }
    )
    with urllib.request.urlopen(f"{API}?{params}", timeout=60) as response:
        return json.load(response)


def pods(payload: dict) -> list[tuple[str, str]]:
    result = payload.get("queryresult", {})
    if not result.get("success"):
        message = result.get("error") or "no result"
        return [("error", str(message))]
    rows: list[tuple[str, str]] = []
    for pod in result.get("pods") or []:
        title = pod.get("title") or ""
        if title in {"Plots", "Plot", "Number line", "Parametric plot"}:
            continue
        for sub in pod.get("subpods") or []:
            text = (sub.get("plaintext") or "").strip()
            if text:
                rows.append((title, text))
    return rows


def format_rows(text: str, rows: list[tuple[str, str]]) -> str:
    lines = [f"Query: {text}"]
    for title, body in rows:
        lines.append(f"[{title}]")
        lines.append(body)
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    append: Path | None = None
    args = argv[1:]
    if args[:1] == ["--append"]:
        if len(args) < 3:
            sys.exit("usage: wolfram_check.py --append notes/wolfram-checks.md QUERY")
        append = Path(args[1])
        if not append.is_absolute():
            append = ROOT / append
        args = args[2:]
    if len(args) != 1:
        sys.exit("usage: wolfram_check.py [--append FILE] QUERY")
    text = args[0]
    report = format_rows(text, pods(query(text)))
    print(report)
    if append is not None:
        with append.open("a", encoding="utf-8") as handle:
            handle.write("\n\n" + report + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
