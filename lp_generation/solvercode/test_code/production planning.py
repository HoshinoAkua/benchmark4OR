import pyscipopt as scp
import json
with open("../../../data/test_data/MF_Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
P = info['P']
R = info["R"]
c = info["c_i"]
a = info["a_{i,j}"]
b = info["b_j"]

model = scp.Model()
x = {}
for i in range(P):
    for j in range(R):
        x[i,j] = model.addVar(name = f"x{i}{j}", vtype = "C")
    
model.setObjective(sum(sum(c[i] * x[i,j] for i in range(P))for j in range(R)),"maximize")

for j in range(R):
    model.addCons(sum(a[i][j] * x[i,j]for i in range(P))>=b[j] )

model.writeProblem("production.lp")