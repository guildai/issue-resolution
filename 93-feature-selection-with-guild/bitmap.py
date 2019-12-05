FEATURES = ["f1", "f2", "f3"]

features = 0

selected = [
    name for i, name in enumerate(FEATURES)
    if pow(2, i) & features
]

print("Selected features: %s" % selected)
