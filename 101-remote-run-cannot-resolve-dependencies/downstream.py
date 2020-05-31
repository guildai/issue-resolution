import os

print("I am downstream %s" % os.getenv("RUN_ID"))
print("I am using upstream %s" % os.getenv("FLAG_UPSTREAM"))
