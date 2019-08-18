import os

DATA_DIR = 'data'

print("Contents of %s" % os.path.abspath(DATA_DIR))
for name in os.listdir(DATA_DIR):
    print(name)
