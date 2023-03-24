from sklearn import datasets

import numpy as np

print("Loading iris dataset")
X, y = datasets.load_iris(return_X_y=True)

print("Writing iris data as X.npy and y.npy")
np.save("X.npy", X)
np.save("y.npy", y)
