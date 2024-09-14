import pyscipopt as scp
import json

dataPath = '../../../data/MILP_data/MF_Shortest Path Problem_Minimum Total Ascending Path (MTAP) Problem_parameters.json0th_paraminfo.json'

with open(dataPath,'r') as f:
    paraminfo = json.load(f)

N = paraminfo['N']
a_ij = paraminfo['a_{i,j}']
s = paraminfo['s']-1
t = paraminfo['t']-1
h_i = paraminfo['h_i']

model = scp.Model()#建立模型
#创建变量
x = {}

for i in range(N):
    for j in range(N):
        x[i,j] = model.addVar(name = f"x{i}_{j}",vtype = "B")


#创建目标函数  
model.setObjective(sum(sum(a_ij[i][j]*x[i,j] for i in range(N)) for j in range(N)),"minimize")

#添加约束

# node s
model.addCons( sum(x[s,j] for j in range(N)) - sum(x[i,s] for i in range(N)) ==1 )

# node t 
model.addCons( sum(x[i,t] for i in range(N)) - sum(x[t,j] for j in range(N)) ==1 )


for i in range(N):
    for j in range(N):
    # constraint 5: 
    # h_i 可以理解为 height of node i, 要求 每次路径 x_{i,j} 需要上升
        model.addCons( (h_i[j] - h_i[i]) * x[i,j] >=0)

    if i == s:
        continue
    elif i==t:
        continue
    else:
        # node i 
        model.addCons( sum(x[i,j] for j in range(N)) - sum(x[j,i] for j in range(N)) == 0 )



model.writeProblem("../../MILP_file/MF_Shortest Path Problem_Minimum Total Ascending Path (MTAP) Problem_parameters.json0th_paraminfo.lp")
