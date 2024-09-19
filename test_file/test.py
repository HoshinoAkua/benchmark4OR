from helper_modified import  graph_generator
import torch
from wl_test_l2O import wl_test
from wl_test_final import WLtest
torch.set_printoptions(profile="full")

import os
dir = '/home/hanyizhou/wl_test/lp_generation/test'
n = 0
for root, dirs, files in os.walk(dir):
        for dir_name in dirs:
                if dir_name.startswith("T"):
                    n+=1
                    newpath = os.path.join(root, dir_name)
                    try: 
                        info1 = graph_generator(os.path.join(newpath, 'model.lp'))
                    except:
                        print(os.path.join(newpath, 'model.lp'))
                    try:
                        info2 = graph_generator(os.path.join(newpath, 'answer_eoe_gpt-4o-2024-08-06.lp'))
                    except:
                        print(os.path.join(newpath,'answer_eoe_gpt-4o-2024-08-06.lp'))
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
                    if wl_test!= None:

                        print(wltest.test(),n)
                    else:
                        print(1)




