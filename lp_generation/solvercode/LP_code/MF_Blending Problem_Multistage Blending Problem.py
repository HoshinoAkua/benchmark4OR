import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Blending Problem_Multistage Blending Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
M = info["M"]
P = info["P"]
T = info["T"]
c = info["c_{i,j,t}"]
n = info["n_{i,j,t}"]
r = info["r_{i,t}"]
p = info["p_{j,t}"]
model = scp.Model()
x = {}
for i in range(M):
    for j in range(P):
        for t in range(T):
            x[i,j,t] = model.addVar(name = f"x{i}{j}{t}",vtype="C",lb=0)

exp = sum(c[i][j][t] * x[i,j,t] for i in range(M) for j in range(P) for t in range(T))
model.setObjective(exp)
for i in range(M):
    for t in range(T):
        model.addCons(sum(x[i,j,t] for j in range(P))==r[i][t])
for j in range(P):
    for t in range(T):
        model.addCons(sum(n[i][j][t]*x[i,j,t] for i in range(M))>=p[j][t])
for t in range(1,T):
    model.addCons(sum(x[i,j,t-1] for i in range(M) for j in range(P))==sum(x[i,j,t] for i in range(M) for j in range(P)))


model.writeProblem("../../lp_file/MF_Blending Problem_Multistage Blending Problem.lp")