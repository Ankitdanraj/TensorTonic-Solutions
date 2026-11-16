import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    arr = np.array(A)
    n,m = arr.shape
    trans = np.zeros((m,n))
    for i in range(n) :
        for j in range(m) :
            trans[j,i] = arr[i,j]
    return trans
