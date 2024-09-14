import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Blending Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
M = info["M"]
P = info["P"]
c = info["c_{i,j}"]
n = info["n_{i,j}"]
r = info["r_i"]
p = info["p_j"]
model = scp.Model()
x = {}
for i in range(M):
    for j in range(P):
        x[i,j] = model.addVar(name = f"x{i}{j}",vtype = "C")
model.setObjective(sum(c[i][j]*x[i,j] for i in range(M) for j in range(P)))
for i in range(M):
    model.addCons(sum(x[i,j] for j in range(P))==r[i])
for j in range(P):
    model.addCons(sum(x[i,j]*n[i][j] for i in range(M))>=p[j])

model.writeProblem("../../lp_file/MF_Blending Problem.lp")