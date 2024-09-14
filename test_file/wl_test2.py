import torch
import torch.nn.functional
from wl_test.graph_generation.helper_modified import get_a_new2
import numpy as np

def hash_feature_var(features): #把features映射成onehot编码
    if isinstance(features, torch.Tensor):
        features = features.cpu().numpy()
    
    N = len(features)
    hash = {}
    copy = torch.zeros(N)
    for i in range(N):
        if tuple(features[i]) in hash.keys():
            pass
        else:
            hash[tuple(features[i])] = i
        copy[i] = hash[tuple(features[i])]
    copy = copy.to(torch.int64)
    coding = torch.nn.functional.one_hot(copy)
    return coding

def hash_feature_cons(features):
    return -hash_feature_var(features)

def hash_features(cons_feature, var_feature):
    N_1 = len(cons_feature)
    N_2 = len(var_feature)
    cons_feature = hash_feature_cons(cons_feature)
    var_feature = hash_feature_var(var_feature)
    M_1 = len(cons_feature[0])
    M_2 = len(var_feature[0])
    
    feature_matrix = torch.zeros((N_1+N_2, M_1+M_2))
    feature_matrix[:N_1,:M_1] = cons_feature
    feature_matrix[N_1:, M_1:] = var_feature
    
    return feature_matrix

def torch_to_dict(A):
    assert len(A.shape) == 1
    dit = {}
    for a in A:
        if float(a) in dit.keys():
            dit[float(a)]+=1
        else:
            dit[float(a)] = 1
            
    return dit

#若AB同构, 则存在t, 使得t(A) = B, 从而sum(t(A)) = sum(B). 逆否命题为: 若不存在t, 使得sum(t(A)) = sum(B), 则AB不同构.
def feature_detection(feature1, feature2):
    #检查这样的t是否存在
    feature1 = torch.sum(feature1, dim=1).reshape(-1)
    feature2 = torch.sum(feature2, dim=1).reshape(-1)
    dit1 = torch_to_dict(feature1)
    dit2 = torch_to_dict(feature2)

    if dit1 == dit2:
        return True
    else:
        return False


def wltest(graph_matrix1, graph_matrix2, cons_feature1, cons_feature2,var_feature1, var_feature2, max_iter):
    feature1 = hash_features(cons_feature1, var_feature1)
    feature2 = hash_features(cons_feature2, var_feature2)
    
    for iter in range(max_iter):
        print(iter)
        if feature_detection(feature1,feature2):
            feature1 = (graph_matrix1+torch.eye(len(graph_matrix1)))@feature1
            feature2 = (graph_matrix2+torch.eye(len(graph_matrix2)))@feature2
            
        else:
            return "not same"
    return "possible same"


if __name__ == "__main__":
    graph_matrix1 = torch.tensor([[0.,2.,1.],[2.,0.,0.],[1.,0.,0.]])
    graph_matrix2 = torch.tensor([[0.,1.,2.],[1.,0.,0.],[2.,0.,0.]])
    cons_feature1 = torch.tensor([[2,2,1,0,1,1]])
    cons_feature2 = torch.tensor([[2,2,1,0,1,1]])
    var_feature1 = torch.tensor([[1,1,1,0,1,1],[2,0,1,0,1,0]])
    var_feature2 = torch.tensor([[2,0,1,0,1,0],[1,1,1,0,1,1]])
    print(wltest(graph_matrix1, graph_matrix2, cons_feature1,cons_feature2, var_feature1, var_feature2, 10))


    graph_matrix1 = torch.tensor([[0,0,0,0,1,1,0,0],
                              [0,0,0,0,1,1,0,0],
                              [0,0,0,0,0,0,1,1],
                              [0,0,0,0,0,0,1,1],
                              [1,1,0,0,0,0,0,0],
                              [1,1,0,0,0,0,0,0],
                              [0,0,1,1,0,0,0,0],
                              [0,0,1,1,0,0,0,0]])
    graph_matrix2 = torch.tensor([[0,0,0,0,1,0,0,1],
                              [0,0,0,0,1,1,0,0],
                              [0,0,0,0,0,1,1,0],
                              [0,0,0,0,0,0,1,1],
                              [1,1,0,0,0,0,0,0],
                              [0,1,1,0,0,0,0,0],
                              [0,0,1,1,0,0,0,0],
                              [1,0,0,1,0,0,0,0]])
    cons_feature1 = torch.ones(size=(4,2))
    cons_feature2 = torch.ones(size=(4,2))
    var_feature1 = torch.ones(size=(4,4))
    var_feature2 = torch.ones(size=(4,4))
    print(wltest(graph_matrix1, graph_matrix2, cons_feature1, cons_feature2, var_feature1, var_feature2,max_iter=10))