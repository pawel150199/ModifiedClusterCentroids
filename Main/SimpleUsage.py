import numpy as np
from ModifiedClusterCentroids import ModifiedClusterCentroids
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=10000,
    n_features=15,
    n_clusters_per_class=1,
    n_informative=15,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    flip_y=0.1,
    random_state=1234,
    weights=[0.2, 0.8]
)

preprocs = ModifiedClusterCentroids()
X_new, y_new = preprocs.fit_resample(X,y)

print(f"Dataset shape before undersampling: {X.shape}")
print(f"Dataset shape after undersampling: {X_new.shape}")
