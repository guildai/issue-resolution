import os

run_id = os.getenv("RUN_ID")
print("Training (%s)" % run_id)
open("train_id", "w").write(run_id)
