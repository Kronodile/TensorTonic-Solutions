import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    sum = 0
    x = np.asarray(x)
    y = np.asarray(y)
    for i in range(x.shape[0]):
        sum = sum + abs(x[i]-y[i])
    return float(sum)
    pass