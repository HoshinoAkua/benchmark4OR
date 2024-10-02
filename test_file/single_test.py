from helper_modified_grb import  graph_generator
import torch
from wl_test.test_file.extend_wltest import WLtest
torch.set_printoptions(profile="full")

import os
dir = '/home/hanyizhou/wl_test/lp_generation/test'
info1 = graph_generator(os.path.join(dir, 'model.lp'))
info2 = graph_generator(os.path.join(dir, 'answer_concise_eoe_o1-preview.lp'))

A1 = info1[0]
A2 = info2[0]
f1 = info1[1]#variable
f2 = info2[1]
c1 = info1[2]#constrain
c2 = info2[2]
print(A1.shape, A2.shape)
wltest = WLtest(A1, c1,f1,A2,c2,f2)
print('开始测试')
print(wltest.test())