#!/usr/bin/env python3
"""Fail closed on specialist-branch changes outside the current exact order."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def die(message: str) -> None:
    print(f"BLOCKER: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        die(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def is_protected(path: str, config: dict) -> bool:
    if path in config.get("protected_exact_paths", []):
        return True
    return any(path.startswith(prefix) for prefix in config.get("protected_prefixes", []))


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()

    # Old specialist workflows already fetch this entry point from integration.
    # Load the v4 checker AND its validator from that same exact trusted commit.
    authority = git("rev-parse", "refs/remotes/origin/v2.7-design", check=False)
    state_text = git("show", f"{authority}:governance/v4/runtime/STATE.json", check=False) if authority else ""
    if state_text:
        try:
            active = json.loads(state_text)
        except ValueError as exc:
            die(f"invalid authoritative v4 state: {exc}")
        if active.get("migration_control", {}).get("cutover_performed") is True:
            with tempfile.TemporaryDirectory(prefix="foulwake-trusted-ci-") as temporary:
                for name in ("ci.py", "validator.py"):
                    Path(temporary, name).write_text(git("show", f"{authority}:governance/v4/{name}") + "\n", encoding="utf-8")
                result = subprocess.run([sys.executable, "-B", str(Path(temporary, "ci.py")),
                                         "--authority", authority, "--branch", args.branch, "--head", args.head], check=False)
                raise SystemExit(result.returncode)

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    branches = config.get("branches", {})
    if args.branch not in branches:
        die(f"unknown specialist branch: {args.branch}")

    policy = branches[args.branch]
    if policy.get("branch_must_not_exist"):
        die(f"{args.branch} is not authorized to exist in the current stage")

    baseline = policy.get("baseline_commit")
    if not baseline or not re.fullmatch(r"[0-9a-f]{40}", baseline):
        die(f"invalid reset baseline for {args.branch}")

    if git("cat-file", "-t", baseline, check=False) != "commit":
        die(f"reset baseline is not available as a commit: {baseline}")

    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", baseline, args.head],
        check=False,
    )
    if ancestry.returncode != 0:
        die(f"{args.head} is not a descendant of reset baseline {baseline}")

    changed = [
        line for line in git("diff", "--name-only", f"{baseline}..{args.head}").splitlines()
        if line
    ]
    if not changed:
        print(f"FOULWAKE scope: PASS — {args.branch} is at its reset baseline")
        return

    protected = [path for path in changed if is_protected(path, config)]
    if protected:
        die("specialist changed Chief Editor protected paths: " + ", ".join(protected))

    authorization = policy.get("authorization")
    if not authorization:
        die(
            f"{args.branch} has no active write authorization; changed: "
            + ", ".join(changed)
        )

    allowed = set(authorization.get("exact_paths", []))
    invalid = [path for path in changed if path not in allowed]
    if invalid:
        die("files outside exact authorization: " + ", ".join(invalid))

    maximum = authorization.get("max_changed_files")
    if not isinstance(maximum, int) or len(changed) > maximum:
        die(f"changed file count {len(changed)} exceeds budget {maximum}")

    extensions = set(authorization.get("allowed_extensions", []))
    if extensions:
        wrong_type = [path for path in changed if Path(path).suffix not in extensions]
        if wrong_type:
            die("disallowed file type: " + ", ".join(wrong_type))

    numstat = git("diff", "--numstat", f"{baseline}..{args.head}").splitlines()
    binary_paths = []
    for line in numstat:
        parts = line.split("\t")
        if len(parts) >= 3 and (parts[0] == "-" or parts[1] == "-"):
            binary_paths.append(parts[-1])
    if binary_paths and not authorization.get("binary_files_allowed", False):
        die("binary changes are forbidden: " + ", ".join(binary_paths))

    max_words = authorization.get("max_words_per_file")
    if max_words is not None:
        for path in changed:
            content = git("show", f"{args.head}:{path}")
            count = word_count(content)
            if count > max_words:
                die(f"{path} has {count} words; maximum is {max_words}")

    stage = authorization.get("stage_id")
    if not stage:
        die("authorization has no stage_id")

    print(
        f"FOULWAKE scope: PASS — {args.branch}, stage {stage}, "
        f"{len(changed)} authorized file(s)"
    )


if __name__ == "__main__":
    main()
