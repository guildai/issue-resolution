import re

import yaml

yaml.resolver.Resolver.add_implicit_resolver(
        "tag:yaml.org,2002:bool",
        re.compile(r"^(?:y|Y|n|N)$", re.X),
        list('yYnN'))

print(yaml.dump("n")[:-1])
print(yaml.dump("y")[:-1])
print(yaml.dump("N")[:-1])
print(yaml.dump("Y")[:-1])
