import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    u = np.mean(X, axis=0)
    Xc = X-u
    if (X.shape[0] >= 2) and X.ndim==2:
        cov = np.zeros((u.shape[0],u.shape[0]))
        cov = Xc.T @ Xc / (X.shape[0]-1) 
    else:
        return None
    return cov
    pass