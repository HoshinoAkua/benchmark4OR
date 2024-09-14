from helper_modified import  graph_generator
import torch
from wl_test_l2O import wl_test
from wl_test_final import WLtest
torch.set_printoptions(profile="full")


info1 = graph_generator('wl_test/lp_generation/test/model.lp')
info2 = graph_generator('wl_test/lp_generation/test/answer_eoe.lp')
#print(info[1],info[2],info[3],info[4])
A1 = info1[0]
A2 = info2[0]
f1 = info1[1]#variable
f2 = info2[1]
c1 = info1[2]#constrain
c2 = info2[2]
#print(A1,info1[0])
# print('cons feature:',c1)
# print('var feature:',f2)
#print('size:',A1)
# permidx_cons = torch.randperm(len(A1))
# permidx_vars = torch.randperm(len(A1[0]))
# rowperm = torch.eye(len(A1))[permidx_cons]
# colperm = torch.eye(len(A1[0]))[permidx_vars]


wltest = WLtest(A1, c1,f1,A2,c2,f2)

print(wltest.test())




