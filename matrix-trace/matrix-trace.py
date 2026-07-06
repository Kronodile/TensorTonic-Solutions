import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.asarray(A)
    sum = 0
    for i in range(A.shape[0]):
        sum = sum + A[i][i]
    return sum
    pass
