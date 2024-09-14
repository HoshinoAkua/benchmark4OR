import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Maximum Flow Problem_Multicommodity Flow Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)

N = info["N"]
K = info["K"]
c = info["c_{i,j}"]
d = info["d_k"]
s = info["s_k"]
t = info["s_k"]
model = scp.Model()
f = {}
for i in range(N):
    for j in range(N):
        for k in range(K):
            f[i,j,k] = model.addVar(name = f"f{i}{j}{k}", vtype = "C", ub =1.0)
model.setObjective(sum(f[i,j,k] for i in range(N) for j in range(N) for k in range(K)),"maximize")
for i in range(N):
    for j in range(N):
        model.addCons(sum(f[i,j,k]*d[k] for k in range(K))<= c[i][j])
for K in range(K):
    for i in range(N):
        if i not in [s[k]-1,t[k]-1]:
            exp = sum(f[i,j,k] for j in range(K))-sum(f[j,i,k] for j in range(N))
            model.addCons(exp==0)
        elif i == s[k]-1:
            exp = sum(f[i,j,k] for j in range(N))-sum(f[j,i,k] for j in range(N))
            model.addCons(exp == 1)
        elif i == t[k]-1:
            exp = sum(f[j,i,k] for j in range(N))-sum(f[i,j,k] for j in range(N))
            model.addCons(exp == 1)

model.writeProblem("../../lp_file/MF_Maximum Flow Problem_Multicommodity Flow Problem.lp")