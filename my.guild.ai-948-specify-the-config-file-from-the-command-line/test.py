import yaml

config = yaml.safe_load(open("config.yml").read())
print(config["msg"])
