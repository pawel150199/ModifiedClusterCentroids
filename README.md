# ModifiedClusterCentroids

[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=svg)](https://circleci.com/gh/circleci/circleci-docs)
![GitHub top language](https://img.shields.io/github/languages/top/pawel150199/ModifiedClusterCentroids)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pawel150199/ModifiedClusterCentroids)
![GitHub last commit](https://img.shields.io/github/last-commit/pawel150199/ModifiedClusterCentroids)

## Usage algorithm
![image](https://user-images.githubusercontent.com/41188005/185746655-ea88cab0-c279-4d9d-a5c1-5ef9960d5087.png)

### Output
![image](https://user-images.githubusercontent.com/41188005/185746677-7e8c9944-62eb-47ba-954b-03b93782eacb.png)

## Visualization of ModifiedClusterCentroids algorithm and comparision between other well known undersampling methods
![image](https://user-images.githubusercontent.com/41188005/185745359-9ad036e2-e859-41b4-a6af-3688a69112d4.png)

## Description
`ModifiedClusterCentroids` is an algorithm based on ClusterCentroid algorithm and increase effectiveness of selecting samples from original dataset.
### How it works?
- Original dataset is dividing to separate clusters
- If `CC_strategy` is equal `const` then amount of samples reduced in each cluster will be calculate by apriori probability, but at the end majority class will be reduced to minority class with minimal margin of error. If `CC_strategy` is equal `auto` then amount of samples reduced in each cluster will be calculated using std value for each cluster, but finally amount of samples which will left depends on std.
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
