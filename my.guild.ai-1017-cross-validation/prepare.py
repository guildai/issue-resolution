from sklearn import datasets

import numpy as np

print("Loading iris dataset")
X, y = datasets.load_iris(return_X_y=True)

print("Writing X.npy")
np.save("X.npy", X)

print("Writing y.npy")
np.save("y.npy", y)
