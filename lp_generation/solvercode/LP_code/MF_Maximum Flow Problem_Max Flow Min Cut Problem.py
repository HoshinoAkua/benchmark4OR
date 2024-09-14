import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Maximum Flow Problem_Max Flow Min Cut Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
    
N=info["N"]
c = info["c_{i, j}"]
s = info["s"]-1
t = info["t"]-1

model = scp.Model()
x = {}
y = {}
for i in range(N):
    for j in range(N):
        if c[i][j]>0:
            x[i,j] = model.addVar(name = f"x{i}{j}" , vtype = "C",lb=1)
        else:
            x[i,j] = model.addVar(name = f"x{i}{j}" , vtype = "C")
    if i not in [s,t]:
        y[i] = model.addVar(name = f"y{i}", vtype ="C", lb=None)
model.setObjective(c[i][j]*x[i,j])

for i in range(N):
    for j in range(N):
        if i not in [s,t] and j not in [s,t]:
            model.addCons((y[j]-y[i]+x[i,j])>=0)
for j in range(N):
    if j not in [s,t]:
        model.addCons((x[s,j]+y[j])>=1)
for i in range(N):
    if i not in  [s,t]:
        model.addCons((x[i,t]-y[i])>=0) 
model.writeProblem("../../lp_file/MF_Maximum Flow Problem_Max Flow Min Cut Problem.lp")
        