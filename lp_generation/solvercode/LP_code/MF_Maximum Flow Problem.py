import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Maximum Flow Problem_parameter.json0th_paraminfo.json") as f:
    info = json.load(f)
model = scp.Model()
N = info["N"]
c = info["c_{i, j}"]
s = info["s"]-1
t = info["t"]-1
f = {}
for i in range(N):
    for j in range(N):
        f[i,j] = model.addVar(name = f"f{i}{j}", vtype = "C", lb= 0,ub = c[i][j])
model.setObjective(sum(f[i,j] for i in range(N) for j in range(N)),"maximize")
for k in range(N):
    if k not in [s,t]:
        exp = sum(f[i,k] for i in range(N))-sum(f[k,j] for j in range(N))
        model.addCons(exp==0)
model.writeProblem('../../lp_file/MF_Maximum Flow Problem.lp')
model.writeProblem('../../success/MF_Maximum Flow Problem.lp')