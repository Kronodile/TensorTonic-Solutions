import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    sop = 0.0
    if x.shape[0] == y.shape[0]:
        for i in range(x.shape[0]):
            sop = sop + ((x[i]*y[i]))
    else:
        raise ValueError
    return float(sop)
    pass