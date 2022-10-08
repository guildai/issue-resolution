import subprocess

head_commit = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], encoding="utf-8"
).rstrip()

print(f"HEAD: {head_commit}")
