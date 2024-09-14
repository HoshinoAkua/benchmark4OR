from pyscipopt import Model

import json
with open('../../../data/lp_data/MF_Shorest Path Problem_parameter.json0th_paraminfo.json') as f:
    info = json.load(f)
    
N = info["N"]
d = info["d_{i,j}"]
s = info['s']-1
t = info['t']-1

model =Model()

x ={}
for i in range(N):
    for j in range(N):
        x[i,j]=model.addVar(name = f'x{i}{j}',vtype = "C", lb=0)

model.setObjective(sum(d[i][j]*x[i,j] for i in range(N) for j in range(N)))

model.addCons((sum(x[s,j] for j in range(N))-sum(x[i,s] for i in range(N)))==1)
model.addCons((sum(x[t,j] for j in range(N))-sum(x[i,t] for i in range(N)))==-1)
for k in range(N):
    if k not in [s,t]:
        model.addCons((sum(x[k,j] for j in range(N))-sum(x[i,k] for i in range(N)))==0)

model.writeProblem("../../lp_file/MF_Shortest Path Problem.lp")