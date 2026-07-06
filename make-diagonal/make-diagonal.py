import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v0 = np.zeros((len(v),len(v)))
    m = v0.shape[0]
    n = v0.shape[1]
    for i in range(m):
        v0[i][i] = v[i]
    return v0
    pass
