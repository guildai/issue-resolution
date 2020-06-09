import xgboost as xgb

from sklearn.model_selection import RandomizedSearchCV, GroupKFold

import numpy as np

cv = RandomizedSearchCV(
    estimator=xgb.XGBClassifier(),
    param_distributions={"gamma": [0.5, 1]},
    cv=GroupKFold(n_splits=4),
    n_jobs=6,
    n_iter=1,
)

cv.fit(
    X=np.random.random_sample((1000, 100)),
    y=np.random.choice(3, 1000),
    groups=np.random.choice(25, 1000),
)
