import glob
import os
import sys

import yaml

assert len(sys.argv) == 3, sys.argv

run_dir = sys.argv[1]
expected_venv = sys.argv[2]

run_env = yaml.safe_load(open(os.path.join(run_dir, ".guild", "attrs", "env")))
python_path = run_env["PYTHONPATH"].split(":")

site_packages = glob.glob(os.path.join(expected_venv, "lib", "*", "site-packages"))
assert len(site_packages) == 1, expected_venv
site_packages_path = site_packages[0]

assert len(python_path) == 2, python_path
assert python_path[0] == "."
assert python_path[1] == os.path.abspath(site_packages_path)

print(f"Python path ok: {python_path}")
