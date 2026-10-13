#!/usr/bin/env python3
"""Render card/card.svg: ASCII portrait on the left, neofetch-style info on the right.

Standard library only. Run by .github/workflows/card.yml once a day.
Stats come from the GitHub GraphQL API when GH_TOKEN or GITHUB_TOKEN is set;
otherwise the last values in card/stats.json are reused.
"""
import json
import os
import urllib.request
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "card"
LOGIN = "Smars-Bin-Hu"

FONT_SIZE = 14
CHAR_W = 8.43          # advance of one monospace glyph at FONT_SIZE
LINE_H = 19
PAD = 28
GAP_COLS = 4           # blank columns between portrait and info
INFO_COLS = 58

BG, FRAME = "#0d1117", "#30363d"
FG, DIM, KEY, VAL, HEAD, ART = "#c9d1d9", "#484f58", "#ffa657", "#79c0ff", "#7ee787", "#8b949e"

# ("head", title) | ("kv", key, value) | ("blank",)
INFO = [
    ("head", "smars@toronto"),
    ("kv", "Role", "Data Engineer, AI Agent Engineering"),
    ("kv", "Industry", "Banking, Regulatory Technology"),
    ("kv", "Location", "Toronto, Canada"),
    ("kv", "Education", "MSc Big Data Analytics, Trent University"),
    ("blank",),
    ("head", "Focus"),
    ("kv", "Agent.Harness", "hooks, gates, approved write-back"),
    ("kv", "Agent.Evals", "acceptance checks, independent review"),
    ("kv", "Agent.Context", "knowledge base, instructions, skills"),
    ("kv", "Data", "Spark, Databricks, Delta Lake, Airflow"),
    ("kv", "Now.Building", "copilot-agentic-harness"),
    ("blank",),
    ("head", "Contact"),
    ("kv", "Website", "smarshu.com"),
    ("kv", "LinkedIn", "linkedin.com/in/smars-hu"),
    ("kv", "X", "@SmarsBHu"),
    ("kv", "Meeting", "cal.com/smars-hu"),
    ("blank",),
    ("head", "GitHub Stats"),
    ("kv", "Repos", "{repos}"),
    ("kv", "Stars", "{stars}"),
    ("kv", "Followers", "{followers}"),
    ("kv", "Contributions.LastYear", "{contributions}"),
]

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection { contributionCalendar { totalContributions } }
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false, first: 100) {
      totalCount
      nodes { stargazerCount }
    }
  }
}
"""


def fetch_stats():
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    cache = CARD / "stats.json"
    if not token:
        return json.loads(cache.read_text())
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": LOGIN},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        user = json.load(resp)["data"]["user"]
    repos = user["repositories"]
    stats = {
        "repos": repos["totalCount"],
        "stars": sum(n["stargazerCount"] for n in repos["nodes"]),
        "followers": user["followers"]["totalCount"],
        "contributions": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
    }
    cache.write_text(json.dumps(stats, indent=2) + "\n")
    return stats


def text(x, y, cols, body, fill=FG):
    """One fixed-width line; textLength pins the width whatever font the viewer has."""
    return (
        f'<text x="{x:.1f}" y="{y}" fill="{fill}" xml:space="preserve" '
        f'textLength="{cols * CHAR_W:.1f}" lengthAdjust="spacing">{body}</text>'
    )


def info_line(item, stats):
    if item[0] == "blank":
        return None, 0
    if item[0] == "head":
        title = item[1]
        rule = "─" * (INFO_COLS - len(title) - 1)
        return f'<tspan fill="{HEAD}">{escape(title)}</tspan> <tspan fill="{DIM}">{rule}</tspan>', INFO_COLS
    key, value = item[1], f"{item[2]}".format(**{k: f"{v:,}" for k, v in stats.items()})
    dots = "." * max(INFO_COLS - len(key) - len(value) - 3, 2)
    body = (
        f'<tspan fill="{KEY}">{escape(key)}</tspan><tspan fill="{DIM}">: {dots} </tspan>'
        f'<tspan fill="{VAL}">{escape(value)}</tspan>'
    )
    return body, len(key) + len(value) + len(dots) + 3


def main():
    stats = fetch_stats()
    art = (CARD / "portrait.txt").read_text().splitlines()
    art_cols = max(len(line) for line in art)
    rows = max(len(art), len(INFO))

    info_x = PAD + (art_cols + GAP_COLS) * CHAR_W
    width = round(info_x + INFO_COLS * CHAR_W + PAD)
    height = PAD * 2 + rows * LINE_H

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" '
        f'role="img" aria-label="Smars Hu: data engineer building AI agent harnesses in Toronto">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{BG}" stroke="{FRAME}"/>',
        f'<g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, \'Liberation Mono\', monospace" '
        f'font-size="{FONT_SIZE}">',
    ]
    art_top = PAD + FONT_SIZE + (rows - len(art)) * LINE_H // 2
    for i, line in enumerate(art):
        if line.strip():
            out.append(text(PAD, art_top + i * LINE_H, len(line), escape(line), ART))
    info_top = PAD + FONT_SIZE + (rows - len(INFO)) * LINE_H // 2
    for i, item in enumerate(INFO):
        body, cols = info_line(item, stats)
        if body:
            out.append(text(info_x, info_top + i * LINE_H, cols, body))
    out += ["</g>", "</svg>"]
    (CARD / "card.svg").write_text("\n".join(out) + "\n")
    print(f"card.svg {width}x{height}  {stats}")


if __name__ == "__main__":
    main()
