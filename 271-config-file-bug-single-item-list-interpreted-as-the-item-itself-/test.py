import yaml

with open("test.yaml") as f:
    params = yaml.full_load(f)

print(repr(params["a_list"]))
