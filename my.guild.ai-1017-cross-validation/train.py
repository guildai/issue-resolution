import numpy as np

from sklearn import model_selection
from sklearn import svm

k = 5
fold = 1

print("Loading iris data")
X = np.load("X.npy")
y = np.load("y.npy")

print(f"Using fold {fold} of {k}")
kf = model_selection.KFold(n_splits=k)
train, test = list(kf.split(X))[fold - 1]
X_train, X_test = X[train], X[test]
y_train, y_test = y[train], y[test]

print("Training model")
clf = svm.SVC(kernel="linear", C=1)
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print(f"score: {score}")
