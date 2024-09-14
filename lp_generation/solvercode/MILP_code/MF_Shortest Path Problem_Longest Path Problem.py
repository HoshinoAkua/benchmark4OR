#########################################
# done-CH0527
#########################################

import pyscipopt as scp
import json

dataPath = '../../../data/MILP_data/MF_Shortest Path Problem_Longest Path Problem_parameters.json0th_paraminfo.json'

with open(dataPath,'r') as f:
    paraminfo = json.load(f)

N = paraminfo['N']
d_ij = paraminfo['d_{i,j}']
s = paraminfo['s']-1
t = paraminfo['t']-1

model = scp.Model()#建立模型
#创建变量
x = {}

for i in range(N):
    for j in range(N):
        x[i,j] = model.addVar(name = f"x{i}_{j}",vtype = "B")
            # vtype: type of the variable: 
            # 'C' continuous, 'I' integer, 'B' binary, and 'M' implicit integer
# def 	addVar (self, name='', vtype='C', lb=0.0, ub=None, obj=0.0, pricedVar=False, pricedVarScore=1.0)

#创建目标函数  
model.setObjective(sum(sum(d_ij[i][j]*x[i,j]  for i in range(N)) for j in range(N)),"maximize")

#添加约束

# node s -constraints 2
model.addCons( sum(x[s,j] for j in range(N)) - sum(x[i,s] for i in range(N)) ==1 )

# node t  -constraints 3
model.addCons( sum(x[i,t] for i in range(N)) - sum(x[t,j] for j in range(N)) ==1 )

# node i 
for i in range(N):
    if i == s:
        continue
    elif i==t:
        continue
    else:
        model.addCons( sum(x[i,j] for j in range(N)) - sum(x[j,i] for j in range(N)) == 0 )

model.writeProblem("../../MILP_file/MF_Shortest Path Problem_Longest Path Problem.lp")
