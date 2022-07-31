import unittest
import sys
import numpy as np
from sklearn.datasets import make_classification
sys.path.append("../.")
from  Main.ModifiedClusterCentroids import ModifiedClusterCentroids

class Test(unittest.TestCase):
    def test_size(self):
        X,y = make_classification(
            n_samples=1000,
            n_features=2,
            n_informative=2,
            n_redundant=0,
            n_repeated=0,
            random_state=1234,
            weights=[0.2, 0.8]
        )
        preprocs = ModifiedClusterCentroids()
        X_new, y_new = preprocs.fit_resample(X,y)
        self.assertNotEquals(X.shape[0], X_new.shape[0])
        self.assertEqual(X.shape[1], X_new.shape[1])
        self.assertNotEquals(X.shape[0], 0)
        self.assertNotEquals(X.shape[1], 0)


        

if __name__=="__main__":
    unittest.main()