import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    sum = 0
    if (x.shape[0] == y.shape[0]):
        for i in range(x.shape[0]):
            sum = sum + ((x[i]-y[i])**2)
    else:
        raise ValueError
    return float(np.sqrt(sum))
    pass