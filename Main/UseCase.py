import numpy as np
from ModifiedClusterCentroids import ModifiedClusterCentroids
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt 

# Generate data
X,y = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=1234,
    weights=[0.2, 0.8]
)

# Define undersampling
preproc = ModifiedClusterCentroids(CC_strategy='const', cluster_algorithm='DBSCAN')
X_auto, y_auto= preproc.fit_resample(X,y)
preproc = ModifiedClusterCentroids(CC_strategy='auto', cluster_algorithm='DBSCAN')
X_const, y_const= preproc.fit_resample(X,y)
preproc = ModifiedClusterCentroids(CC_strategy='auto', cluster_algorithm='OPTICS')
X_OPTICS_a, y_OPTICS_a= preproc.fit_resample(X,y)
preproc = ModifiedClusterCentroids(CC_strategy='const', cluster_algorithm='OPTICS')
X_OPTICS_c, y_OPTICS_c= preproc.fit_resample(X,y)

# Data vizualization and comparison between all ModifiedClusterCentroids versions
fig, ax = plt.subplots(2,3, figsize=(15,7))
# Before undersampling DBSCAN
ax[0,0].scatter(*X.T, c=y)
ax[0,0].set_xlim(-4,4)
ax[0,0].set_ylim(-4,4)
ax[0,0].set_xlabel('Feature 0')
ax[0,0].set_ylabel('Feature 1')
ax[0,0].set_title('Before Undersampling - DBSCAN')
# After undersampling DBSCAN - auto
ax[0,1].scatter(*X_auto.T, c=y_auto)
ax[0,1].set_xlim(-4,4)
ax[0,1].set_ylim(-4,4)
ax[0,1].set_xlabel('Feature 0')
ax[0,1].set_ylabel('Feature 1')
ax[0,1].set_title('After Undersampling - DBSCAN-auto')
# After undersampling DBSCAN - const
ax[1,0].scatter(*X_const.T, c=y_const)
ax[1,0].set_xlim(-4,4)
ax[1,0].set_ylim(-4,4)
ax[1,0].set_xlabel('Feature 0')
ax[1,0].set_ylabel('Feature 1')
ax[1,0].set_title('After undersampling - DBSCAN-const')
# After undersampling OPTICS - auto
ax[1,1].scatter(*X_OPTICS_a.T, c=y_OPTICS_a)
ax[1,1].set_xlim(-4,4)
ax[1,1].set_ylim(-4,4)
ax[1,1].set_xlabel('Feature 0')
ax[1,1].set_ylabel('Feature 1')
ax[1,1].set_title('After Undersampling - OPTICS-auto')
# After undersampling OPTICS - const
ax[0,2].scatter(*X_OPTICS_c.T, c=y_OPTICS_c)
ax[0,2].set_xlim(-4,4)
ax[0,2].set_ylim(-4,4)
ax[0,2].set_xlabel('Feature 0')
ax[0,2].set_ylabel('Feature 1')
ax[0,2].set_title('After Undersampling - OPTICS-const')

# Save plot image
plt.tight_layout()
plt.savefig('Images/comparision_own_algorithms.png')
