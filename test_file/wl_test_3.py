import torch
import torch.nn.functional as F
import numpy as np

def hash_feature_var(var_features):
    N = len(var_features)
    duplicate = torch.arange(N).to(torch.int64)
    return F.one_hot(duplicate)

def hash_feature_cons(cons_features):
    return -hash_feature_var(cons_features)

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
    
def feature_detection2(feature1:torch.Tensor, feature2:torch.Tensor):
    
    N = len(feature1[0])
    for feature in feature1:
        index = torch.nonzero(torch.sum(feature == feature2, dim=1)==N).reshape(-1)
        
        if len(index)==1:
            index = index[0]
            feature2 = torch.cat((feature2[:index], feature2[index+1:]),dim=0)
        else:
            return False
    return True
        
        



def wltest(graph_matrix1, graph_matrix2, cons_feature1, cons_feature2,var_feature1, var_feature2, max_iter):
    feature1 = hash_features(cons_feature1, var_feature1)
    feature2 = hash_features(cons_feature2, var_feature2)
    
    for iter in range(max_iter):
        if feature_detection2(feature1,feature2):
            feature1 = (graph_matrix1+torch.eye(len(graph_matrix1)))@feature1
            feature2 = (graph_matrix2+torch.eye(len(graph_matrix2)))@feature2
            print('iter: ',iter,'\n','feature: ','\n',feature1,'\n' ,feature2)
        else:
            return "not same"
    return "possible same"






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
wltest(graph_matrix1, graph_matrix2, cons_feature1, cons_feature2, var_feature1, var_feature2,max_iter=10)


graph_matrix1 = torch.tensor([[0,2,1],[2,0,0],[1,0,0]])
graph_matrix2 = torch.tensor([[0,1,2],[1,0,0],[2,0,0]])
cons_feature1 = torch.tensor([[2,2,1,0,1,1]])
cons_feature2 = torch.tensor([[2,2,1,0,1,1]])
var_feature1 = torch.tensor([[1,1,1,0,1,1],[2,0,1,0,1,0]])
var_feature2 = torch.tensor([[2,0,1,0,1,0],[1,1,1,0,1,1]])
print(wltest(graph_matrix1, graph_matrix2, cons_feature1,var_feature1, cons_feature2, var_feature2, 10))


