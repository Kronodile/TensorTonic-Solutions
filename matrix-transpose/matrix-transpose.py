import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    n = A.shape[0]  # rows
    m = A.shape[1]  # cols

    y = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            y[i][j] = A[j][i]
    return y
    pass
