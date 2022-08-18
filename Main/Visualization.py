import numpy as np
from ModifiedClusterCentroids import ModifiedClusterCentroids
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt 
from imblearn.under_sampling import NearMiss, ClusterCentroids, RandomUnderSampler

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

preproc = RandomUnderSampler(random_state=1234)
X_ru, y_ru= preproc.fit_resample(X,y)

preproc = ClusterCentroids(random_state=1234)
X_cc, y_cc= preproc.fit_resample(X,y)

preproc = NearMiss(version=1)
X_nm, y_nm= preproc.fit_resample(X,y)

preproc = NearMiss(version=2)
X_nmm, y_nmm= preproc.fit_resample(X,y)

# Data vizualization and comparison between all ModifiedClusterCentroids versions
fig, ax = plt.subplots(3,3, figsize=(15,7))

# Before undersampling DBSCAN
ax[0,0].scatter(*X.T, c=y)
ax[0,0].set_xlim(-4,4)
ax[0,0].set_ylim(-4,4)
ax[0,0].set_xlabel('Feature 0')
ax[0,0].set_ylabel('Feature 1')
ax[0,0].set_title('Before Undersampling - MCC DBSCAN')

# After undersampling DBSCAN - auto
ax[0,1].scatter(*X_auto.T, c=y_auto)
ax[0,1].set_xlim(-4,4)
ax[0,1].set_ylim(-4,4)
ax[0,1].set_xlabel('Feature 0')
ax[0,1].set_ylabel('Feature 1')
ax[0,1].set_title('After Undersampling - MCC DBSCAN-auto')

# After undersampling DBSCAN - const
ax[0,2].scatter(*X_const.T, c=y_const)
ax[0,2].set_xlim(-4,4)
ax[0,2].set_ylim(-4,4)
ax[0,2].set_xlabel('Feature 0')
ax[0,2].set_ylabel('Feature 1')
ax[0,2].set_title('After undersampling - MCC DBSCAN-const')

# After undersampling OPTICS - auto
ax[1,0].scatter(*X_OPTICS_a.T, c=y_OPTICS_a)
ax[1,0].set_xlim(-4,4)
ax[1,0].set_ylim(-4,4)
ax[1,0].set_xlabel('Feature 0')
ax[1,0].set_ylabel('Feature 1')
ax[1,0].set_title('After Undersampling - MCC OPTICS-auto')

# After undersampling OPTICS - const
ax[1,1].scatter(*X_OPTICS_c.T, c=y_OPTICS_c)
ax[1,1].set_xlim(-4,4)
ax[1,1].set_ylim(-4,4)
ax[1,1].set_xlabel('Feature 0')
ax[1,1].set_ylabel('Feature 1')
ax[1,1].set_title('After Undersampling - MCC OPTICS-const')

# After Cluster Centroids undersampling
ax[1,2].scatter(*X_cc.T, c=y_cc)
ax[1,2].set_xlim(-4,4)
ax[1,2].set_ylim(-4,4)
ax[1,2].set_xlabel('Feature 0')
ax[1,2].set_ylabel('Feature 1')
ax[1,2].set_title('After Undersampling - Cluster Centroids')

# After Random undersampling
ax[2,0].scatter(*X_ru.T, c=y_ru)
ax[2,0].set_xlim(-4,4)
ax[2,0].set_ylim(-4,4)
ax[2,0].set_xlabel('Feature 0')
ax[2,0].set_ylabel('Feature 1')
ax[2,0].set_title('After Undersampling - Random Undersampler')

# After NearMiss version 1 undersampling
ax[2,1].scatter(*X_nm.T, c=y_nm)
ax[2,1].set_xlim(-4,4)
ax[2,1].set_ylim(-4,4)
ax[2,1].set_xlabel('Feature 0')
ax[2,1].set_ylabel('Feature 1')
ax[2,1].set_title('After Undersampling - Near Miss version 1')

# After NearMiss version 2 undersampling
ax[2,2].scatter(*X_nmm.T, c=y_nmm)
ax[2,2].set_xlim(-4,4)
ax[2,2].set_ylim(-4,4)
ax[2,2].set_xlabel('Feature 0')
ax[2,2].set_ylabel('Feature 1')
ax[2,2].set_title('After Undersampling - Near Miss version 2')

# Save plot image
plt.tight_layout()
plt.savefig('Images/comparision_algorithms.png')
