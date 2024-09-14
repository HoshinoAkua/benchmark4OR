import torch
import torch.nn as nn
#from wl_test.helper_modified import get_a_new2


#var feature 是[obj coeff, lower bound, upper bound, bin?] -> [obj coeff, (n,1), (k,1), 1/0](如果是无穷就用(1,0)表示)
#cons feature是[degree, rhs, sense, euqal?]->[m, (k,1)or(0,1), (1,0)or(0,1)or(1,1), 1or0]

def from_vars_to_cons(graph_matrix, var_features, cons_features):
    cons_num = len(cons_features)
    var_num = len(var_features)
    assert cons_num+var_num == torch.sum(torch.tensor(graph_matrix.shape))
    aggregation_features = graph_matrix@var_features
    return (cons_features+aggregation_features)/2

def from_cons_to_vars(graph_matrix, var_features, cons_features):
    aggregation_features = graph_matrix.T@cons_features
    return (var_features+aggregation_features)/2

#输入三个tensor, 第一个是(N_1+N_2)×(N_1+N_2)的, 表示cons=N_1 and var=N_2共有N_1+N_2个节点, 记录了节点间的权重
#第二个是N_1×d_1, 表示cons feature
#第三个是N_2×d_2, 表示var feature
def wl_test(graph_matrix1, graph_matrix2, cons_feature1, var_feature1, cons_feature2, var_feature2 ,Max_iter):
    cons_num = len(cons_feature1)
    for iter in range(Max_iter):
        if not torch.sum(torch.abs(var_feature1-var_feature2)) and not torch.sum(torch.abs(cons_feature1 - cons_feature2)) and iter>=1:
            return 'same'
        else:
            cons_feature1 = from_vars_to_cons(graph_matrix1, var_feature1, cons_feature1)
            cons_feature2 = from_vars_to_cons(graph_matrix2, var_feature2, cons_feature2)
            var_feature1 = from_cons_to_vars(graph_matrix1, var_feature1, cons_feature1)
            var_feature2 = from_cons_to_vars(graph_matrix2, var_feature2, cons_feature2)
            
        return 'possible not same'
    
    


