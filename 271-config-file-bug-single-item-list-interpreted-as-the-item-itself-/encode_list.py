import shlex
import yaml

with open("test2.yaml") as f:
    params = yaml.full_load(f)

print(repr(shlex.split(params["encoded_list"])))
