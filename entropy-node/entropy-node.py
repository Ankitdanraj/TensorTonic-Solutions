import numpy as np

def entropy_node(y: list[int]) -> float:
    y = np.asarray(y)
    if len(y) == 0 :
        return 0.0
    _,counts = np.unique(y, return_counts = True)
    prob = counts / len(y)
    res = abs(np.sum(prob*np.log2(prob)))
    return res