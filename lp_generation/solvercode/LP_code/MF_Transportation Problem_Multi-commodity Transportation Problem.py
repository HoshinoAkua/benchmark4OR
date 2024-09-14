import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Transportation Problem_Multi-commodity Transportation Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
S = info["S"]
D = info["D"]
K = info["K"]
a = info["a_{k,i}"]
b = info["b_{k,j}"]
c = info["c_{k,i,j}"]

model = scp.Model()
x = {}
for k in range(K):
    for i in range(S):
        for j in range(D):
           x[k,i,j]= model.addVar(name = f"x{k}{i}{j}")
model.setObjective(sum(c[k][i][j]*x[k,i,j] for k in range(K) for i in range(S) for j in range(D)))

for k in range(K):
    for i in range(S):
        model.addCons(sum(x[k,i,j] for j in range(D)) == a[k][i])
    for j in range(D):
        model.addCons(sum(x[k,i,j] for i in range(S)) == b[k][j])
model.writeProblem('../../lp_file/MF_Transportation Problem_Multi-commodity Transportation Problem.lp')