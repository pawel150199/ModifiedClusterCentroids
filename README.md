# ModifiedClusterCentroids

[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://circleci.com/gh/circleci/circleci-docs)
![GitHub top language](https://img.shields.io/github/languages/top/pawel150199/ModifiedClusterCentroids)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pawel150199/ModifiedClusterCentroids)

## Usage algorithm
![image](https://user-images.githubusercontent.com/41188005/185382409-c7234cc9-516d-4d8e-8a78-6ac90fd0def4.png)

## Visualization of usage ModifiedClusterCentroids and comparision between other well known undersampling methods
![image](https://user-images.githubusercontent.com/41188005/185445291-27247f31-d4b3-4e97-aaa0-335319dfda94.png)

## Description
`ModifiedClusterCentroids` is an algorithm based on ClusterCentroid algorithm and increase effectiveness of selecting samples from original dataset.
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
