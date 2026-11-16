import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    arr = np.array(A)
    n,m = arr.shape
    trans = np.zeros((m,n))
    i = 0 
    j = 0
    while i < n and j < m :
        trans[j,i] = arr[i,j]
        j += 1 
        if j == m :
            j = 0
            i += 1
        
    return trans
