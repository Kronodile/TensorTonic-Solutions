import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if (X.shape[0] >= 2) and X.ndim==2:
        cov = np.cov(X, rowvar=False)
        cov = np.atleast_2d(cov)
        return cov
    else:
        return None
    pass