# ModifiedClusterCentroids

[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://circleci.com/gh/circleci/circleci-docs)
![GitHub top language](https://img.shields.io/github/languages/top/pawel150199/ModifiedClusterCentroids)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pawel150199/ModifiedClusterCentroids)

## Usage algorithm
![image](https://user-images.githubusercontent.com/41188005/185382409-c7234cc9-516d-4d8e-8a78-6ac90fd0def4.png)

## Visualization of usage ModifiedClusterCentroids and comparision between other well known undersampling methods
![image](https://user-images.githubusercontent.com/41188005/185744439-cac65587-e2d7-4f7e-aecf-a0252ecf791b.png)

## Description
`ModifiedClusterCentroids` is an algorithm based on ClusterCentroid algorithm and increase effectiveness of selecting samples from original dataset.
### How it works?
- Original dataset is dividing to separate clusters
- If `CC_strategy` is equal `const` then amount of sample reduced in each cluster will be calculate by apriori probability, but at the end majority class will be reduced to minority class with minimal margin of error. If `CC_strategy` is equal `auto` then amount of sample reduced in each cluster will be calculated using std value for each cluster, but finally amount of samples which will left depends on std.
- Finally output is an numpy array and returned dataset is smaller than original but basically can be more efficient in estimation than original.
### Parameters available in this algorithm:
- `CC_strategy`:
  * `const` -> reduce major class to minor ones
  * `auto` -> reduce major class using std calculate per cluster
- `cluster_algorithm`:
  * `DBSCAN` -> used by DBSACAN algorithm to detect clusters from original dataset
  * `OPTICS` -> used by OPTICS algorithm to detect clusters from original dataset
- `eps` -> define cluster  size, used by DBSCAN
- `min_samples` -> used by OPTICS and define minimal amount of samples
- `metric` -> used by DBSCAN and define how to calculate distance between samples, natively use euclidean metric
- `max_eps` -> used by OPTICS and define analyzing area, if max_eps is equal to infinity whole area will be analyzed
