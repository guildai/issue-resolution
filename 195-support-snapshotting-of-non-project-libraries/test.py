import os

# If we're running under Guild, find `shared` and copy it to the Guild
# source code directory. This ensures that we have an exact record of
# the library source code.
try:
    guild_sourcecode = os.environ["GUILD_SOURCECODE"]
except KeyError:
    pass
else:
    import imp
    import shutil
    _f, path, _dest = imp.find_module("shared")
    shutil.copytree(path, os.path.join(guild_sourcecode, "shared"))

# Only import `shared` after we've had a chance to copy the library
# source code to the Guild run directory.
import shared

print("shared module loaded from %s" % shared.__file__)
print(shared.msg)
