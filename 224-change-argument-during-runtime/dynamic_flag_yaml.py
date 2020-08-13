import os

import yaml

x = 1

flags_path = os.path.join(os.environ["RUN_DIR"], ".guild", "attrs", "flags")
flags = yaml.load(open(flags_path))
flags["y"] = x + 1
yaml.dump(flags, open(flags_path, "w"))
