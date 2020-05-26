from __future__ import print_function

import os

for name in ("PROJECT_DIR", "GUILD_OP"):
    print(name, os.getenv(name))
