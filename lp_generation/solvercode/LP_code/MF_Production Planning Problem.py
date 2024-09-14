import pyscipopt as scp
import json
with open("../../../data/lp_data/MF_Production Planning Problem_parameters.json0th_paraminfo.json") as f:
    info = json.load(f)
P = info['P']
R = info["R"]
c = info["c_i"]
a = info["a_{i,j}"]
b = info["b_j"]

model = scp.Model()
x = {}
for i in range(P):

    x[i] = model.addVar(name = f"x{i}", vtype = "C")
    
model.setObjective(sum(c[i] * x[i] for i in range(P)),"maximize")

for j in range(R):
    model.addCons(sum(a[i][j] * x[i]for i in range(P))<=b[j])

model.writeProblem("../../lp_file/MF_Production Planning Problem.lp")