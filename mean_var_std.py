import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    a=np.reshape(list,(3,3))
    mean=[np.mean(a,axis=0).tolist(),np.mean(a,axis=1).tolist(),np.mean(a).tolist()]
    var=[np.var(a,axis=0).tolist(),np.var(a,axis=1).tolist(),np.var(a).tolist()]
    std=[np.std(a,axis=0).tolist(),np.std(a,axis=1).tolist(),np.std(a).tolist()]
    maxi=[np.max(a,axis=0).tolist(),np.max(a,axis=1).tolist(),np.max(a).tolist()]
    mini=[np.min(a,axis=0).tolist(),np.min(a,axis=1).tolist(),np.min(a).tolist()]
    sums=[np.sum(a,axis=0).tolist(),np.sum(a,axis=1).tolist(),np.sum(a).tolist()]
    calculations={
                  'mean': mean,
                  'variance': var,
                  'standard deviation': std,
                  'max': maxi,
                  'min': mini,
                  'sum': sums
                 }

    return calculations