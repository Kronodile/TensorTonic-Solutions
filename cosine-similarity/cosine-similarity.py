import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    
    dot_product = np.dot(a,b)
    cross_product = np.linalg.norm(a) * np.linalg.norm(b)
    cosine_similarity = dot_product/cross_product
    if cross_product==0:
        return 0
    else:
        return float(cosine_similarity)
    pass