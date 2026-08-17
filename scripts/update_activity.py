#!/usr/bin/env python3
"""Refresh the "Recent Activity" block in README.md from public GitHub events.

Rewrites only the text between the ACTIVITY markers, so the rest of the README
is never touched. Exits non-zero without writing if the markers are missing or
GitHub returns nothing usable.

The events API returns trimmed payloads: a PushEvent carries the head SHA but
no commit messages, and a PullRequestEvent carries a number but no title. So we
collect candidates first, then fetch details only for the handful we display.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("GH_USER", "arundhatisingh17")
COUNT = int(os.environ.get("ACTIVITY_COUNT", "3"))
README = os.environ.get("README_PATH", "README.md")

START = "<!--START:activity-->"
END = "<!--END:activity-->"

MAX_SUBJECT = 90


def api(url: str) -> dict | list | None:
    """GET a JSON endpoint, returning None on any failure."""
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-readme",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"  fetch failed for {url}: {exc}", file=sys.stderr)
        return None


def humanize(iso: str) -> str:
    when = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    seconds = (datetime.now(timezone.utc) - when).total_seconds()
    for limit, div, unit in (
        (3600, 60, "minute"),
        (86400, 3600, "hour"),
        (2592000, 86400, "day"),
    ):
        if seconds < limit:
            n = max(1, int(seconds // div))
            return f"{n} {unit}{'s' if n != 1 else ''} ago"
    return when.strftime("%b %-d, %Y")


def truncate(text: str) -> str:
    text = text.splitlines()[0].strip()
    return text[: MAX_SUBJECT - 3].rstrip() + "..." if len(text) > MAX_SUBJECT else text


def render(event: dict) -> str | None:
    """Build one markdown line, fetching details when the payload is trimmed."""
    kind = event.get("type")
    repo = (event.get("repo") or {}).get("name") or ""
    payload = event.get("payload") or {}
    if not repo:
        return None
    link = f"[`{repo.split('/', 1)[-1]}`](https://github.com/{repo})"

    if kind == "PushEvent":
        branch = (payload.get("ref") or "").removeprefix("refs/heads/")
        sha = payload.get("head")
        if not sha:
            return None
        commit = api(f"https://api.github.com/repos/{repo}/commits/{sha}")
        if isinstance(commit, dict):
            message = ((commit.get("commit") or {}).get("message") or "").strip()
            if message:
                return f"{link} — {truncate(message)}"
        # Details unavailable (private, deleted, or rate-limited): still useful.
        return f"{link} — pushed to `{branch or 'default'}`"

    if kind == "PullRequestEvent" and payload.get("action") in {"opened", "reopened"}:
        pr = payload.get("pull_request") or {}
        number = pr.get("number")
        if not number:
            return None
        title = pr.get("title")
        if not title and pr.get("url"):
            detail = api(pr["url"])
            if isinstance(detail, dict):
                title = detail.get("title")
        url = pr.get("html_url") or f"https://github.com/{repo}/pull/{number}"
        suffix = f": {truncate(title)}" if title else ""
        return f"{link} — opened PR [#{number}]({url}){suffix}"

    if kind == "CreateEvent" and payload.get("ref_type") == "repository":
        return f"{link} — created a new repository"

    if kind == "ReleaseEvent" and payload.get("action") == "published":
        rel = payload.get("release") or {}
        name = rel.get("name") or rel.get("tag_name")
        if not name:
            return None
        url = rel.get("html_url") or f"https://github.com/{repo}/releases"
        return f"{link} — released [{name}]({url})"

    return None


def main() -> int:
    events = api(f"https://api.github.com/users/{USER}/events/public?per_page=100")
    if not isinstance(events, list) or not events:
        print("no public events returned; leaving README as-is", file=sys.stderr)
        return 1

    lines: list[str] = []
    seen: set[str] = set()
    for event in events:
        entry = render(event)
        if not entry or entry in seen:
            continue
        seen.add(entry)
        lines.append(f"- {entry} · {humanize(event['created_at'])}")
        if len(lines) == COUNT:
            break

    if not lines:
        print("no displayable public events found; leaving README as-is", file=sys.stderr)
        return 1

    with open(README, encoding="utf-8") as fh:
        content = fh.read()

    if START not in content or END not in content:
        print(f"markers {START} / {END} not found in {README}", file=sys.stderr)
        return 1

    block = "\n".join(lines)
    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{block}\n{END}",
        content,
        flags=re.DOTALL,
    )

    if updated == content:
        print("activity unchanged")
        return 0

    with open(README, "w", encoding="utf-8") as fh:
        fh.write(updated)
    print(f"updated {len(lines)} activity entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
