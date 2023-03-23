import json
import numpy as np

runs = json.load(open("runs.json"))
scores = [run["scalars"]["score"] for run in runs]

print(f"score_avg: {np.mean(scores)}")
