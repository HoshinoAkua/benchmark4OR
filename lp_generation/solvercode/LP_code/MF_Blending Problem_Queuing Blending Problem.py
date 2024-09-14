import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Blending Problem_Queuing Blending Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
K = info["K"]
M = info["M"]
P = info["P"]
c = info["c_{k,i,j}"]
n = info["n_{k,i,j}"]
r = info["r_{k,i}"]
p = info["p_{k,j}"]
t = info["t_{k,i,j}"]
d = info["d_{k}"]

model = scp.Model()
x = {}
w = {}
for k in range(K):
    for i in range(M):
        for j in range(P):
            x[k,i,j] = model.addVar(name = f"x{k}{i}{j}",vtype="C")
        if k>0:
            w[i,k] = model.addVar(name = f"w{i}{k}",vtype = "C")
        elif k==0:
            w[i,k] = model.addVar(name = f"w{i}{k}", vtype = "C", ub=0)
model.setObjective(sum(c[k][i][j]*x[k,i,j] for k in range(K) for i in range(M) for j in range(P)))
for k in range(K):
    for i in range(M):
        model.addCons(sum(x[k,i,j] for j in range(P))==r[k][i])
        model.addCons(sum(x[k,i,j] for j in range(P))==w[i,k])
        if k>0:
            model.addCons(sum(x[k-1,i,j] for j in range(P))+w[i,k-1]>=w[i,k])
    for j in range(P):
        model.addCons(sum(n[k][i][j]*x[k,i,j] for i in range(M))>=p[k][j])
    model.addCons(sum(t[k][i][j]*x[k,i,j] for i in range(M) for j in range(P))<= d[k])
    
model.writeProblem("../../lp_file/MF_Blending Problem_Queuing Blending Problem.lp")