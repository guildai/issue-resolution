import os
import sys

fail = True

print(f"Running {os.getenv('GUILD_OP')}", file=sys.stderr)
assert not fail
