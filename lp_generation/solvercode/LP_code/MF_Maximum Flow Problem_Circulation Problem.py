import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Maximum Flow Problem_Circulation Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
N= info["N"]
c = info["c_{i, j}"]
model = scp.Model()
f = {}
for i in range(N):
    for j in range(N):
        f[i,j] = model.addVar(name = f"f{i}{j}",vtype = "C", lb=0,ub=c[i][j])
for j in range(N):
    model.addCons(sum(f[i,j] for i in range(N))==sum(f[j,i] for i in range(N)))

model.writeProblem("../../lp_file/MF_Maximum Flow Problem_Circulation Problem.lp")