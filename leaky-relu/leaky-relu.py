import numpy as np

def leaky_relu(x, a=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x)
    leaky=np.where(x<0,a*x,x)
    return leaky
    pass