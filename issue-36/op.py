import time

id = 1
wait = 2

print("Starting %i at %s" % (id, time.time()))

time.sleep(wait)

print("Stopping %i at %s" % (id, time.time()))
