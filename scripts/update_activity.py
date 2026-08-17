#!/usr/bin/env python3
"""Refresh the commit list in README.md from public GitHub events.

Rewrites only the text between the ACTIVITY markers, so the rest of the README
is never touched. Exits non-zero without writing if the markers are missing or
GitHub returns nothing usable.

The events API returns trimmed payloads — a PushEvent carries `before` and
`head` SHAs but no commit messages — so each push is expanded through the
compare endpoint to recover every commit it contained, not just the head. That
matters when a push carries several commits: showing only the head would hide
the rest.
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
COUNT = int(os.environ.get("ACTIVITY_COUNT", "7"))
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


NULL_SHA = "0" * 40


def commits_in_push(repo: str, before: str, head: str) -> list[dict]:
    """Every commit a push introduced, newest first.

    The compare endpoint gives the full range. It fails on a first push to a new
    branch (`before` is all zeroes) and after a force-push, so fall back to the
    head commit alone rather than losing the entry.
    """
    if before and before != NULL_SHA:
        data = api(f"https://api.github.com/repos/{repo}/compare/{before}...{head}")
        if isinstance(data, dict) and data.get("commits"):
            return list(reversed(data["commits"]))

    single = api(f"https://api.github.com/repos/{repo}/commits/{head}")
    return [single] if isinstance(single, dict) else []


def render_commit(repo: str, commit: dict) -> str | None:
    """One markdown line for a commit, or None if it isn't worth showing."""
    message = ((commit.get("commit") or {}).get("message") or "").strip()
    sha = commit.get("sha") or ""
    if not message or not sha:
        return None
    # Merge commits are noise on a profile — the branch's own commits show up.
    if message.startswith("Merge pull request") or message.startswith("Merge branch"):
        return None
    name = repo.split("/", 1)[-1]
    url = commit.get("html_url") or f"https://github.com/{repo}/commit/{sha}"
    return f"[`{name}`](https://github.com/{repo}) — [{truncate(message)}]({url})"


def main() -> int:
    events = api(f"https://api.github.com/users/{USER}/events/public?per_page=100")
    if not isinstance(events, list) or not events:
        print("no public events returned; leaving README as-is", file=sys.stderr)
        return 1

    lines: list[str] = []
    seen: set[str] = set()
    for event in events:
        if len(lines) >= COUNT:
            break
        if event.get("type") != "PushEvent":
            continue
        repo = (event.get("repo") or {}).get("name") or ""
        payload = event.get("payload") or {}
        head = payload.get("head")
        if not repo or not head:
            continue

        for commit in commits_in_push(repo, payload.get("before", ""), head):
            sha = commit.get("sha")
            if not sha or sha in seen:
                continue
            entry = render_commit(repo, commit)
            if not entry:
                continue
            seen.add(sha)
            lines.append(f"- {entry} · {humanize(event['created_at'])}")
            if len(lines) >= COUNT:
                break

    if not lines:
        print("no public commits found; leaving README as-is", file=sys.stderr)
        return 1

    with open(README, encoding="utf-8") as fh:
        content = fh.read()

    if START not in content or END not in content:
        print(f"markers {START} / {END} not found in {README}", file=sys.stderr)
        return 1

    # The heading lives inside the markers so its count can never drift from
    # the list beneath it — the events feed doesn't always yield COUNT commits.
    heading = f"## Last {len(lines)} Commit{'s' if len(lines) != 1 else ''}"
    block = "\n".join([heading, ""] + lines)
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
