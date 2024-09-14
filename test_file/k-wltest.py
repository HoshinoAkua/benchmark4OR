import torch
import numpy as np
from torch.nn import functional as F

def k_pairs(k):
    pairs = []
    for i in range(k):
        for j in range(i+1,k):
            pairs.append((i,j))
    return pairs