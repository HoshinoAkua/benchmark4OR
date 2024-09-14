#########################################
# done --CH 0527
#########################################

import pyscipopt as scp
import json

dataPath = '../../../data/lp_data/MF_Shortest Path Problem_K-Shortest Path Problem_parameters.json0th_paraminfo.json'

with open(dataPath,'r') as f:
    paraminfo = json.load(f)

K = paraminfo['K']
N = paraminfo['N']
d_ij = paraminfo['d_{i,j}']
s = paraminfo['s']-1
t = paraminfo['t']-1

model = scp.Model()#建立模型
#创建变量
x = {}

for k in range(K):
    for i in range(N):
        for j in range(N):
            x[k,i,j] = model.addVar(name = f"x{k}_{i}_{j}",ub=1,vtype = "C")
            # vtype: type of the variable: 
            # 'C' continuous, 'I' integer, 'B' binary, and 'M' implicit integer
# def 	addVar (self, name='', vtype='C', lb=0.0, ub=None, obj=0.0, pricedVar=False, pricedVarScore=1.0)

#创建目标函数  
model.setObjective(sum(sum(sum(d_ij[i][j]*x[k,i,j] for k in range(K)) for i in range(N)) for j in range(N)),"minimize")

#添加约束
for k in range(K):
    # node s
    model.addCons( sum(x[k,s,j] for j in range(N)) - sum(x[k,i,s] for i in range(N)) ==1 )

    # node t 
    model.addCons( sum(x[k,i,t] for i in range(N)) - sum(x[k,t,j] for j in range(N)) ==1 )

    # node i 
    for i in range(N):
        if i == s:
            continue
        elif i==t:
            continue
        else:
            model.addCons( sum(x[k,i,j] for j in range(N)) - sum(x[k,j,i] for j in range(N)) == 0 )


for i in range(N):
    for j in range(N):
        model.addCons(  sum(x[k,i,j] for k in range(K)) <= 1 )


model.writeProblem("../../lp_file/MF_Shortest Path Problem_K-Shortest Path Problem.lp")
