features = ''

selected = [x.strip() for x in features.split(",") if x]

print("Selected features: %s" % selected)
