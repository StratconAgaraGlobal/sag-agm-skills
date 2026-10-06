"""Keep the SAG skills in step with GitHub main, during a session as well as at its start.

Claude Code's own plugin auto-update runs once per session, so a push made while a session
is open never reaches it. This hook (wired up in hooks/hooks.json and shipped with every
plugin in this marketplace) compares the installed sag-agm-skills plugins with GitHub main
and, if they differ, updates them on disk right away and tells the user to run
/reload-plugins.

    sag_update.py --event SessionStart --every 15
    sag_update.py --event UserPromptSubmit --every 300

--every N skips the check if this profile checked less than N seconds ago, so the
per-message hook costs nothing most of the time (one `git ls-remote` per five minutes).
A lock stops two SAG plugins installed side by side from running it twice at once.
Everything acts on the session's own Claude profile (CLAUDE_CONFIG_DIR), and any failure
(offline, no access to the private repo, no `claude` CLI on PATH) exits quietly.
"""
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = "https://github.com/StratconAgaraGlobal/sag-agm-skills.git"
MARKET = "sag-agm-skills"


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


event = arg("--event", "SessionStart")
every = int(arg("--every", "0"))

home = Path.home()
cfg = Path(os.environ.get("CLAUDE_CONFIG_DIR") or home / ".claude")
env = dict(os.environ)
# A profile kept in ~/.claude has its account file at ~/.claude.json; pointing
# CLAUDE_CONFIG_DIR at ~/.claude would make the CLI look inside the folder instead.
if os.path.normcase(os.path.normpath(cfg)) == os.path.normcase(os.path.normpath(home / ".claude")):
    env.pop("CLAUDE_CONFIG_DIR", None)

lock = cfg / "sag-skills-update.lock"
stamp = cfg / "sag-skills-update.last-check"


def say(message, context):
    print(json.dumps({"systemMessage": message,
                      "hookSpecificOutput": {"hookEventName": event, "additionalContext": context}}))


def installed_versions():
    data = json.loads((cfg / "plugins" / "installed_plugins.json").read_text(encoding="utf-8"))
    found = {}
    for pid, entries in data.get("plugins", data).items():
        if pid.endswith("@" + MARKET):
            entries = entries if isinstance(entries, list) else [entries]
            found[pid] = {e.get("version") for e in entries}
    return found


def main():
    try:
        if time.time() - stamp.stat().st_mtime < every:
            return
    except FileNotFoundError:
        pass
    stamp.touch()

    installed = installed_versions()
    if not installed:
        return

    out = subprocess.run(["git", "ls-remote", REPO, "refs/heads/main"], capture_output=True,
                         text=True, timeout=20, env=env)
    remote = out.stdout.split()[0][:12] if out.returncode == 0 and out.stdout.strip() else ""
    if not remote or all(v == {remote} for v in installed.values()):
        return

    claude = shutil.which("claude")
    if claude:
        subprocess.run([claude, "plugin", "marketplace", "update", MARKET], capture_output=True,
                       timeout=180, env=env)
        for pid in installed:
            subprocess.run([claude, "plugin", "update", pid], capture_output=True, timeout=180, env=env)
    if not claude or any(v != {remote} for v in installed_versions().values()):
        say(f"A newer version of the SAG skills ({remote}) is on GitHub but could not be installed "
            f"automatically. Update it in /plugin (Marketplaces > {MARKET} > Update), then run /reload-plugins.",
            "A newer SAG skills version is on GitHub but could not be installed automatically. "
            "If the user is about to use a SAG skill, remind them once to update it in /plugin.")
        return
    say(f"SAG skills updated from GitHub to {remote}. Run /reload-plugins to use the new version "
        "in this session (new sessions get it automatically).",
        "The SAG skills (sag-agm-skills plugins) were just updated on disk, but this session still "
        "has the previous version loaded until the user runs /reload-plugins. If the user is about "
        "to use a SAG skill, remind them once to run /reload-plugins first.")


try:
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
except FileExistsError:
    try:
        if time.time() - lock.stat().st_mtime < 300:
            sys.exit(0)          # another SAG plugin's copy of this hook is already running
        lock.unlink()
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except Exception:
        sys.exit(0)
except Exception:
    sys.exit(0)
try:
    os.close(fd)
    main()
except Exception:
    pass
finally:
    try:
        lock.unlink()
    except OSError:
        pass
sys.exit(0)
