import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    denom = norm_a * norm_b

    if denom == 0:
        return 0.0

    return float(dot / denom)